#!/usr/bin/env python3
"""「## معلومات السوق في السعودية」段落的許可證表改由程式依證據包產生（2026-11-24，用戶決定；全程不用 AI；比照 HkTxGNN 同名檔）。

為什麼：以前這張表是報告（AI）寫的自由格式表（表頭十幾種寫法：「| رقم الترخيص | اسم المنتج | الشكل الدوائي | الاستطباب المعتمد |」等，
劑型、適應症欄多半寫「غير مسجّل」，狀態寫在品名格「(ملغى)」或狀態欄），每週許可證排程只改得到概覽表的狀態列與張數列，
表裡寫死的狀態與選列跟著主管機關資料變動就過期，checker 擋整頁（2026-11-12 就以 33 筆 sa-row 紀錄人工更正過「ملغى」）。
改成程式表後，每週排程（scripts/license_adapter.py 的 sync_tables 掛鉤）依同一套規則重排，gate 依快照驗內容。

資料與口徑：證據包 tfda.records＝SFDA 開放資料的已註冊人用藥清單（本地與非本地兩份 xlsx）。清單沒有獨立的許可證號，
站上一直以產品註冊名（TradeName）當 license_id（site.py 的 ID_MATCH），清單只列已註冊品項，狀態一律 Registered。
表格（欄位照 SFDA 原文，不翻譯；表頭註明是英文原文）：
  | اسم المنتج المسجل (بالإنجليزية كما في SFDA) | المادة الفعالة (بالإنجليزية) | الشركة المصنّعة | الحالة |
  第一欄＝license_id（產品註冊名，gate 與 checker 依它對本藥號碼）；成分＝Active Ingredient／ScientificName；
  廠商＝Manufacturer_Name（清單裡跟 Marketing Company 相同）；狀態＝ساري（清單在列＝Registered；license_status＝cancelled 寫 مُلغى）。
選列與順序：換表當時報告原表依序列出的品項（config/license_table_pins.json，對到證據包 license_id 的才收）在前——
正文常寫「أدناه أبرز 5 تراخيص」「الترخيصان الآخران: …」，換成別的列會對不上；其餘依程式排序：單一成分在前、複方在後，再依品名。
單一成分／複方照成分欄以「,」分隔的個數（證據包原收集器與事實層用「;;」切，本站每張都會算成單方，不能用）。
列數＝原表列數（最多 20）；總數多於列數時，表下加一句 SHOW；證據包只收到部分品項（total_matches＞紀錄數）時再加 PARTIAL_LINE。
段落裡沒有表的頁：在標題下補程式表（min(5, 總數) 列）；證據包沒有任何紀錄時補 NONE_LINE。
換表時（--migrate）另拿掉緊鄰舊表、只講「表上列了幾筆」的說明行（CAPTION_RX，例「(عُرضت 5 من أصل 7 تراخيص.)」）；
查核紀錄更正文字所在的行不動。表以外的其他文字不動（正文張數由 scripts/rewrite_license_counts.py 依快照事實層改寫）。
程式區塊標記：程式表（連同表下說明句，或 NONE_LINE）前後各一行「<!-- licenses:begin -->」「<!-- licenses:end -->」。
program_rows 給 scripts/build_license_snapshot.py；carry_block 給 scripts/sync_notes_to_docs.py；run 給 scripts/license_adapter.py 的 sync_tables。
用法（repo 根目錄，先還原 data/）：
  python3 scripts/sync_license_tables.py [--dry-run] [--migrate] [頁 ...]
  python3 scripts/sync_license_tables.py --pins      # 依現行頁面的報告表建 config/license_table_pins.json（只在換表前跑一次）
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECS = ("معلومات السوق في السعودية", "معلومات السوق في المملكة العربية السعودية")
HEAD = ["| اسم المنتج المسجل (بالإنجليزية كما في SFDA) | المادة الفعالة (بالإنجليزية) | الشركة المصنّعة | الحالة |",
        "|------|------|------|------|"]
NONE_LINE = "لا تتضمن قائمة الأدوية المسجلة لدى الهيئة العامة للغذاء والدواء (البيانات المستخدمة في هذا التقرير) أي منتج يحتوي على مكوّن هذا الدواء."
SHOW = "يعرض الجدول أعلاه {n} من أصل {m} من المنتجات المسجلة في البيانات."
SHOW_RX = re.compile(r"^يعرض الجدول أعلاه \d+ من أصل \d+ من المنتجات المسجلة في البيانات\.$")
PARTIAL_LINE = "تتضمن البيانات جزءاً فقط من التراخيص؛ قد تكون القائمة غير مكتملة."
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
MAX_ROWS = 20
ST_VALID, ST_CANC = "ساري", "مُلغى"
DIAC = re.compile(r"[ً-ْـ]")
# 舊表的說明行：整行只講「表上列了幾筆（共幾筆）」（換表後由 SHOW 取代）
CAPTION_RX = re.compile(r"^\(?\s*(عرضت|يعرض|يُعرض|عُرض|يعرض أعلاه|يعرض الجدول)\s+(أعلاه\s+)?\d+\s+(تراخيص|ترخيصا|ترخيص)?\s*من أصل\s+\d+"
                        r"(\s+(تراخيص|ترخيصا|ترخيص)(\s+(سارية|صالحة|ساريا))?)?\s*[.۔]?\s*\)?\s*[.]?$|"
                        r"^\(\s*إجمالي التراخيص \d+، والجدول يعرض \d+ منها فقط\.?\s*\)$|"
                        r"^الأدوية المذكورة هي \d+ من أصل \d+ (ترخيصا|تراخيص) (صالحا|سارية|ساريا)\.$")


def cell(x, cap=None):
    s = re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()
    return s[:cap].rstrip() + "…" if cap and len(s) > cap else s


def ings(r):
    return [x for x in re.split(r"\s*,\s*", str(r.get("ingredients") or "")) if x.strip()]


def is_combo(r):
    return len(ings(r)) > 1


def is_cancelled(r):
    return str(r.get("license_status") or "").lower() == "cancelled"


def uniq(recs):
    seen = {}
    for r in recs or []:
        k = str(r.get("license_id") or "").strip()
        if k and k not in seen:
            seen[k] = r
    return list(seen.values())


def mix(recs):
    """單一成分／複方張數（含有效張數），給快照與正文張數改寫用（成分欄以「,」分隔）"""
    u = uniq(recs)
    s = [r for r in u if not is_combo(r)]
    c = [r for r in u if is_combo(r)]
    return {"single_total": len(s), "combo_total": len(c),
            "valid_single": sum(1 for r in s if not is_cancelled(r)), "valid_combo": sum(1 for r in c if not is_cancelled(r))}


PINS_FILE = ROOT / "config" / "license_table_pins.json"
_PINS = None


def pins_for(stem):
    global _PINS
    if _PINS is None:
        _PINS = json.loads(PINS_FILE.read_text(encoding="utf-8")).get("pins", {}) if PINS_FILE.exists() else {}
    return _PINS.get(stem) or _PINS.get(stem.replace("-", "_")) or _PINS.get(stem.replace("_", "-")) or []


def table_rows(recs, pins=()):
    rows = []
    u = sorted(uniq(recs), key=lambda r: (is_combo(r), is_cancelled(r), str(r.get("license_id")).strip().upper()))
    rank = {k: i for i, k in enumerate(pins or [])}
    u.sort(key=lambda r: rank.get(str(r.get("license_id")).strip(), len(rank)))  # 穩定排序：沒選的保持程式排序
    for r in u:
        ing = cell(r.get("ingredients"), 90) or "—"
        mf = cell(r.get("manufacturer") or r.get("license_holder"), 70) or "—"
        rows.append(f"| {cell(r['license_id'])} | {ing} | {mf} | {ST_CANC if is_cancelled(r) else ST_VALID} |")
    return rows


def block_for(tf, n=None, pins=()):
    recs = tf.get("records") or []
    rows = table_rows(recs, pins)
    if not rows:
        return [NONE_LINE]
    n = min(5, len(rows)) if n is None else min(n, len(rows))
    out = HEAD + rows[:n]
    tail = ([SHOW.format(n=n, m=len(rows))] if len(rows) > n else []) + ([PARTIAL_LINE] if partial(tf) else [])
    return out + ([""] + tail if tail else [])


def partial(tf):
    return (tf.get("total_matches") or 0) > len(tf.get("records") or [])


def program_rows(tf, fc=None, pins=()):
    return table_rows(tf.get("records") or [], pins)[:MAX_ROWS], None


def strip_marks(lines):
    return [l for l in lines if l.strip() not in (BEGIN, END)]


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


def bounds(lines):
    for i, ln in enumerate(lines):
        m = re.match(r"^(#{2,3}) (.+?)\s*$", ln)
        if m and m.group(2) in SECS:
            lv = len(m.group(1))
            j = next((k for k in range(i + 1, len(lines)) if re.match(rf"^#{{1,{lv}}} ", lines[k])), len(lines))
            return i + 1, j
    return None, None


def _first_table(lines, a, b):
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        return None, None
    x = y = tb[0]
    while y + 1 < b and lines[y + 1].startswith("|"):
        y += 1
    return x, y


def is_caption(ln):
    return bool(CAPTION_RX.match(DIAC.sub("", ln.strip())))


def _protected():
    p = ROOT / "docs/_data/drug_reviews.json"
    out = set()
    if p.exists():
        for r in json.loads(p.read_text(encoding="utf-8")).get("records", []):
            for k in ("replacement", "anchor", "claim"):
                v = (r.get(k) or "").strip()
                if len(v) >= 6:
                    out.add(v)
    return out


def _prog_line(l):
    s = l.strip()
    return bool(SHOW_RX.match(s)) or s in (NONE_LINE, PARTIAL_LINE)


def process(text, tf, pins=(), migrate=False, protect=()):
    lines = strip_marks(text.split("\n"))
    a, b = bounds(lines)
    if a is None:
        return None
    x, y = _first_table(lines, a, b)
    if x is None:
        lines = lines[:a] + [""] + wrap(block_for(tf, None, pins)) + [""] + [l for l in lines[a:] if not _prog_line(l)]
    else:
        n = min(MAX_ROWS, max(1, y - x - 1))
        rest = lines[y + 1:b]
        if migrate:  # 緊鄰舊表（中間只有空行）的說明行
            k = 0
            while k < len(rest) and not rest[k].strip():
                k += 1
            if k < len(rest) and is_caption(rest[k]) and not any(rest[k].strip() in p or p in rest[k] for p in protect):
                rest = rest[:k] + rest[k + 1:]
        rest = [l for l in rest if not _prog_line(l)]
        lines = lines[:x] + ([""] if lines[x - 1].strip() else []) + wrap(block_for(tf, n, pins)) + [""] + rest + lines[b:]
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))
    return t2 if t2 != text else None


def carry_block(old_text, new_text):
    old = old_text.replace("\r\n", "\n").split("\n")
    if BEGIN not in old or END not in old:
        return new_text
    blk = old[old.index(BEGIN):old.index(END) + 1]
    lines = strip_marks(new_text.split("\n"))
    a, b = bounds(lines)
    if a is None:
        return new_text
    x, y = _first_table(lines, a, b)
    if x is None:
        out = lines[:a] + [""] + blk + [""] + lines[a:]
    else:
        prot = _protected()  # 新頁照樣會帶舊表的說明行（「(عُرضت 5 من أصل 7 تراخيص.)」）：跟換表時一樣拿掉（查核紀錄錨著的不動）
        rest = [l for l in lines[y + 1:b] if not _prog_line(l)
                and not (is_caption(l) and not any(l.strip() in q or q in l for q in prot))]
        out = lines[:x] + [""] + blk + [""] + rest + lines[b:]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


def bundle_file(stem):
    for key in dict.fromkeys((stem, stem.replace("-", "_"), stem.replace("_", "-"))):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return f
    return None


def _pages():
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        raw = page.read_text(encoding="utf-8")
        if "layout: id_redirect" in raw[:3000] or 'http-equiv="refresh"' in raw[:3000]:
            continue
        yield page, raw


def _norm(x):
    return re.sub(r"[^0-9A-Z؀-ۿ]", "", re.sub(r"[*_`\[\]]", "", DIAC.sub("", x or "")).upper())


def build_pins():
    """現行頁面報告表第一欄依序對到證據包 license_id（完全相同→去符號相同→唯一前綴）；對不到的列不收"""
    pins, stat = {}, {"pages": 0, "rows": 0, "mapped": 0}
    for page, raw in _pages():
        bf = bundle_file(page.stem)
        if bf is None:
            continue
        lines = raw.split("\n")
        a, b = bounds(lines)
        if a is None:
            continue
        x, y = _first_table(lines, a, b)
        if x is None:
            continue
        recs = uniq((json.loads(bf.read_text(encoding="utf-8")).get("tfda") or {}).get("records") or [])
        ids = [str(r["license_id"]).strip() for r in recs]
        nid = {}
        for k in ids:
            nid.setdefault(_norm(k), k)
        got = []
        for ln in lines[x + 2:y + 1]:
            raw0 = ln.strip().strip("|").split("|")[0].strip()
            c0 = re.sub(r"[*_`]", "", raw0).strip()
            c0 = re.sub(r"\s*\((ساري|سارٍ|ملغى|مُلغى|ملغي|ملغاة)[^)]*\)\s*$", "", c0)
            stat["rows"] += 1
            k = raw0 if raw0 in ids else c0 if c0 in ids else None
            if k is None and _norm(c0) in nid and nid[_norm(c0)] not in got:
                k = nid[_norm(c0)]
            if k is None:  # 同一個去符號鍵有多個號（「… Injection」「… Injection*」）：取還沒列的
                k = next((v for v in ids if _norm(v) == _norm(c0) and v not in got), None)
            if k is None and len(_norm(c0)) >= 4:
                cand = [v for nk, v in nid.items() if nk.startswith(_norm(c0)) or _norm(c0).startswith(nk)]
                k = cand[0] if len(cand) == 1 else None
            if k and k not in got:
                got.append(k)
                stat["mapped"] += 1
        if got:
            pins[page.stem] = got
            stat["pages"] += 1
    PINS_FILE.parent.mkdir(exist_ok=True)
    PINS_FILE.write_text(json.dumps({"_doc": "2026-11-24 換表時報告原表依序列出的品項（對到證據包 tfda.records 的 license_id），"
                                             "scripts/sync_license_tables.py 的程式表照這個順序列；對不到的列不收",
                                     "built": __import__("datetime").date.today().isoformat(), "stats": stat, "pins": pins},
                                    ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return stat


def run(only=None, dry=False, migrate=False):
    """全站（或 only 指定的頁）重排程式表。回傳改到的頁（檔名去 .md）。沒有 data/bundles 就什麼都不做。"""
    changed = []
    if not (ROOT / "data/bundles").is_dir():
        return changed
    prot = _protected() if migrate else ()
    for page, raw in _pages():
        if only and page.stem not in only:
            continue
        bf = bundle_file(page.stem)
        if bf is None:
            continue
        tf = json.loads(bf.read_text(encoding="utf-8")).get("tfda") or {}
        new = process(raw, tf, pins_for(page.stem), migrate, prot)
        if new is None:
            continue
        changed.append(page.stem)
        if not dry:
            page.write_text(new, encoding="utf-8")
    return changed


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--pins" in a:
        print("pins:", build_pins())
        sys.exit(0)
    ch = run({x for x in a if not x.startswith("--")} or None, "--dry-run" in a, "--migrate" in a)
    print(f"許可證表{'（試跑）' if '--dry-run' in a else ''}改 {len(ch)} 頁")
