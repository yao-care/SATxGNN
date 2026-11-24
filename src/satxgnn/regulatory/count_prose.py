"""正文許可證張數的程式改寫（2026-11-24 建，用戶決定；做法移植 KrTxGNN／MyTxGNN／HkTxGNN 的 count_prose，規則是本站阿拉伯文句型）。

用戶 2026-11-24 決定：正文裡「N ترخيصًا／N تراخيص」這類許可證張數敘述，由程式依許可證快照（snapshots/sa_licenses.json.gz 的 facts，
單一成分／複方張數用快照的 mix）改寫，每週資料更新後跟著改，不逐筆寫查核紀錄（同 Tw／Kr／My／Hk：程式改寫的張數敘述是程式產生的正文）。
本站的事實層：SFDA 開放資料的已註冊人用藥清單只列已註冊品項，所以有效數＝總數、註銷數＝0（證據包只收部分品項的頁 total 是 None）。

只改「句型明確、數字確定是本藥許可證張數」的地方，其餘一律不動：
  - 數字是阿拉伯數字（0-9），左右幾個字內有「ترخيص／تراخيص／ترخيصًا」（「(4 من 4)」這種括號比數也算，句子要講許可證）；
    句子沒有試驗、研究、文獻、病例、交互作用等字樣（那些數字不是許可證）。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、引言框、front matter；
    查核紀錄 replacement／anchor 所在的句子（改了紀錄會對不上）。
  - 整句不動（hedged/subset）：有保留（على الأقل、جزئية、غير مكتملة）、相對數（آخر／أخرى／إضافي、باستثناء、عدا）、
    講資料或查詢（تتضمن البيانات、حزمة الأدلة、البحث）、劑型或廠商子集（أقراص、حقن、مرهم、قطرة… mg、شركة；數字所在的子句有英文字母
    ＝點名品牌或廠商，也算子集）；事實層 partial 的頁整頁不動。
  - 數字不動（display）：顯示筆數（عُرضت／يعرض／أُدرج／أبرز／أول／أدناه／أعلاه／الجدول／المذكورة／منها）；「X من أصل Y」裡 X≠Y 的 X。
角色：數字前後是「ملغى／ملغاة／أُلغيت」→註銷；「سار／ساري／سارية／صالح」→有效；「أحادية المكوّن／مفرد」→單方；「مركّب／مركبة」→複方；其餘→總數。
同一行只要有一句含許可證數字而被略過，整行都不動。
阿拉伯文數詞跟名詞的配合（1、2 用「ترخيص واحد／ترخيصان」，3～10「N تراخيص」，11 以上「N ترخيصًا」，形容詞也跟著變）：
數字後面直接接許可證名詞時，新舊數字不在同一組（3～10 或 11～99）就不改、列為 agreement（只換數字會文法錯）。
句子另用文字數詞（الأربعة、الخمسة、ترخيصان…）講張數時整句不改、列為 numeral-word（只換阿拉伯數字會跟文字數詞對不上）；
只有文字數詞的句子，跟事實與程式表列數都不符時列出。
單一成分／複方的數字只驗、不改（列為 single-combo；事實層用「;;」切，本站成分欄是「,」分隔）。
數字已等於該角色的任一合理讀法就不動；原數字是 0、要改成 0 的不改（zero-premise／to-zero）。
前提檢查（premise）：句子說「全部有效／無註銷」而有效≠總數、「全部單方」而單方≠總數時整句不動、列出。
"""
from __future__ import annotations

import re

from . import site as C

DIAC = re.compile(r"[ً-ْـ]")
SENT_SPLIT = re.compile(r"(?<=[.!؟])(?=\s)")
NOUN = r"(?:ال)?(?:تراخيص|ترخيصا|ترخيصان|ترخيصين|ترخيص)"
NUM = re.compile(r"(?<![\d/A-Za-z\-])(?<!\d[.,])(\d{1,4})(?!\d|[.,]\d|/|\s*(?:mg|MG|ml|ML|%|ملغ|مل\b|ميكرو|وحدة))")
LICENSE = re.compile(NOUN)
NOT_LICENSE = re.compile(r"تجرب|تجارب|دراس|PMID|NCT|مريض|مرضى|حالات? سريرية|تفاعل|مقال|منشور|ورقة|بحث علمي|تنبؤ|مرشح|درجة|مستوى الدليل|L\d")
HEDGED = re.compile(r"على الأقل|جزئي|جزءا|جزء من|(?:القائمة|البيانات|الجدول)\s+(?:قد تكون\s+)?غير مكتمل|قد تكون القائمة|(?<!\w)آخر(?:ان|ين|ى)?(?!\w)|أخرى|إضافي|بالإضافة|باستثناء|(?<!\w)عدا|سوى|"
                    r"سابق|سابقا|في الماضي|نحو|حوالي|تقريبا|أكثر من|يزيد|يتجاوز|أقل من|"
                    r"تتضمن البيانات|تضم البيانات|البيانات المجمعة|حزمة الأدلة|البحث في|الاستعلام|عثر|وجدنا")
SUBSET = re.compile(r"أقراص|(?<!\w)قرص|كبسول|حقن|مرهم|كريم|قطرة|قطرات|شراب|بخاخ|استنشا|فموي|موضعي|بيطري|تسريب|لصق|لصاق|تحامي|محلول|معلق|هلام|"
                    r"(?<!\w)جل(?!\w)|غسول|مسحوق|أمبول|فيال|(?<!\w)قلم|خرطوش|(?<!\w)ملغ(?![ىاي])|(?<!\w)مل(?!\w)|mg|MG|ml|ML|%|شرك|مصن|وكيل|[A-Za-z]")
DISPLAY_LEFT = re.compile(r"(عرضت|عرض|يعرض|تعرض|أدرج|أدرجت|يدرج|أبرز|أول|أهم|أدناه|أعلاه|الجدول|المذكورة|المدرجة|هي|منها|من بينها|من بين)\s*(\(?\s*)$")
DISPLAY_RIGHT = re.compile(r"^\s*(?:" + NOUN + r"\s*)?(?:منها|فقط منها|أدناه|أعلاه|في الجدول|مدرجة|معروضة)")
PART_OF = re.compile(r"^\s*(?:" + NOUN + r"\s*)?(?:\S+\s+)?من\s+(?:أصل\s+)?(\d{1,4})")
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)
CANC = r"ملغ[ىاي]\w*|ملغاة|ألغيت|ألغي|إلغاء|منتهي\w*|مسحوب\w*"
CANC_L = re.compile(r"(" + CANC + r")\s*(?:" + NOUN + r")?\s*$")
CANC_R = re.compile(r"^\s*(?:" + NOUN + r"\s*)?(?:\S+\s+)?(" + CANC + r")")
VALID_L = re.compile(r"(سار\w*|صالح\w*)\s*(?:" + NOUN + r")?\s*$")
VALID_R = re.compile(r"^\s*(?:" + NOUN + r"\s*)?(?:\S+\s+)?(سار\w*|صالح\w*)")
SINGLE = re.compile(r"أحادي\w* المكون|أحادية|مفرد\w*|مكون واحد|مادة فعالة واحدة")
COMBO = re.compile(r"مركب\w*|متعدد\w* المكون|توليف\w*")
ALL_VALID = re.compile(r"(جميع|كل|كافة|كلا|كلها|جميعها|كلاهما)[^.؟!]{0,40}(سار|صالح)|(لا|ولا) (يوجد|توجد)[^.؟!]{0,20}" r"(ملغ)")
ALL_SINGLE = re.compile(r"(جميع|كل|كافة|كلها|جميعها|كلاهما)[^.؟!]{0,40}(أحادي|مفرد)")
_NUMW = {"واحد": 1, "الوحيد": 1, "ترخيصان": 2, "ترخيصين": 2, "الترخيصين": 2, "الترخيصان": 2, "اثنان": 2, "اثنين": 2,
         "ثلاثة": 3, "أربعة": 4, "خمسة": 5, "ستة": 6, "سبعة": 7, "ثمانية": 8, "تسعة": 9, "عشرة": 10}
WNUM = re.compile(r"(?:" + NOUN + r"\s+(?:ال)?(ثلاثة|أربعة|خمسة|ستة|سبعة|ثمانية|تسعة|عشرة)(\s+عشر)?(?!\w)|"
                  r"(?<!\w)(ثلاثة|أربعة|خمسة|ستة|سبعة|ثمانية|تسعة|عشرة)(\s+عشر)?\s+" + NOUN + r"|"
                  r"(?<!\w)(ال)?(ترخيصان|ترخيصين)(?!\w)|" + NOUN + r"\s+(واحد)(?!\w))")
CLAUSE_SEP = "،,؛;:()"
LINE_HOLD = re.compile(r"الباقي|المتبقي|الأخرى|(?<!\w)الآخر|(?<!\w)آخر|"
                       r"(?<!أبرز )(?<!أول )(?<!أهم )(?<!هذه )(?<!منها )(?<!عرضت )(?<!عرضت منها )(?<!أعلاه )(?<!\w)(ال)?(ثلاثة|أربعة|خمسة|ستة|سبعة|ثمانية|تسعة|عشرة)(?!\w)(?! منها)")


def _clause(s, a, b):
    i = max(s.rfind(c, 0, a) for c in CLAUSE_SEP)
    j = min([k for k in (s.find(c, b) for c in CLAUSE_SEP) if k >= 0] or [len(s)])
    return s[i + 1:j]


def _wvals(s):
    out = []
    for m in WNUM.finditer(s):
        g = [x for x in m.groups() if x]
        w = next((x for x in g if x in _NUMW or x.lstrip("ال") in _NUMW), None)
        if w is None:
            continue
        v = _NUMW.get(w, _NUMW.get(w[2:] if w.startswith("ال") else w))
        if any(x.strip() == "عشر" for x in g):
            v += 10
        out.append(v)
    return out


def _klass(n):
    if 3 <= n <= 10:
        return "pl"
    if 11 <= n <= 99:
        return "acc"
    return None


def _role(s, a, b):
    left, right = s[max(0, a - 25):a], s[b:b + 30]
    if DISPLAY_LEFT.search(left) or DISPLAY_RIGHT.match(right):
        return "display"
    if CANC_L.search(left) or CANC_R.match(right):
        return "cancelled"
    clause = _clause(s, a, b)
    valid = bool(VALID_L.search(left) or VALID_R.match(right))
    if SINGLE.search(clause):
        return "valid_single" if valid else "single"
    if COMBO.search(clause):
        return "valid_combo" if valid else "combo"
    return "valid" if valid else "total"


def _readings(role, f, explicit):
    t, v, c = f.get("total"), f.get("valid"), f.get("cancelled")
    st, sc, vs, vc = f.get("single_total"), f.get("combo_total"), f.get("valid_single"), f.get("valid_combo")
    if role == "cancelled":
        return {c}, c
    if role == "valid":
        return {v}, v
    if role == "valid_single":
        return {vs}, vs
    if role == "valid_combo":
        return {vc}, vc
    if role == "single":
        return ({st}, st) if explicit else ({st, vs}, st if st == vs else None)
    if role == "combo":
        return ({sc}, sc) if explicit else ({sc, vc}, sc if sc == vc else None)
    return ({t}, t) if explicit else ({t, v}, t if t == v else None)


def _premise_ok(sent, f, roles):
    scope_single = any(r in ("single", "valid_single") for r in roles) and not any(r in ("total", "valid") for r in roles)
    if ALL_VALID.search(sent) and f.get("valid") != f.get("total") and not scope_single:
        return False
    if ALL_SINGLE.search(sent) and not scope_single and f.get("single_total") != f.get("total"):
        return False
    return True


def _licnum(s, m):
    """數字是許可證張數：前後幾個字內有許可證名詞，或是句中講許可證的「(N من M)」括號比數"""
    a, b = m.start(), m.end()
    near = s[max(0, a - 22):a] + " " + s[b:b + 22]
    if LICENSE.search(near):
        return True
    return bool(re.match(r"^\s*من\s+(?:أصل\s+)?\d", s[b:])) or bool(re.search(r"(?<!\w)من\s+(?:أصل\s+)?$", s[max(0, a - 12):a]))


def rewrite_sentence(sent, f, market=False):
    """回傳 (新句子, 跳過理由或 None)。比對在去掉變音符號的字串上做，改寫只換數字本身（變音符號不影響數字位置以外的字）。"""
    plain = DIAC.sub("", sent)
    if not (LICENSE.search(plain) or market) or NOT_LICENSE.search(plain):
        return sent, None
    nums = [m for m in NUM.finditer(plain) if _licnum(plain, m)]
    if not nums:
        ws = [] if re.search(r"(عرضت|يعرض|تعرض|أدرج|أبرز|أول|أهم|أدناه|أعلاه|الجدول|المذكورة|المدرجة)", plain) else _wvals(plain)
        if ws and not HEDGED.search(plain):
            ok = {f.get("total"), f.get("valid"), f.get("_shown")}
            if any(w not in ok for w in ws if w != 1) and not re.search(r"الوحيد|واحد", plain):
                return sent, "numeral-word"
        return sent, None
    if HEDGED.search(plain) or any(SUBSET.search(_clause(plain, m.start(), m.end())) for m in nums):
        return sent, "hedged/subset"
    found = []
    for m in nums:
        role = _role(plain, m.start(), m.end())
        po = PART_OF.match(plain[m.end():])
        if po and int(po.group(1)) != int(m.group(1)):
            role = "display"  # 「5 من أصل 12」的 5：表上列出的筆數
        found.append((m, role))
    roles = [r for _, r in found if r != "display"]
    explicit = any(r in ("valid", "cancelled") for r in roles)
    subs = []
    for m, role in found:
        if role == "display":
            continue
        old = int(m.group(1))
        ok, v = _readings(role, f, explicit)
        if None in ok and len(ok) == 1:
            return sent, "no-fact"
        if old in ok:
            continue
        if role in ("single", "combo", "valid_single", "valid_combo"):
            return sent, "single-combo"
        if v is None:
            return sent, "ambiguous"
        if old == 0:
            return sent, "zero-premise"
        if v == 0:
            return sent, "to-zero"
        if re.match(r"^\s*" + NOUN, plain[m.end():]) and (_klass(old) is None or _klass(old) != _klass(v)):
            return sent, "agreement"
        subs.append((m, v))
    if not subs:
        return sent, None
    if _wvals(plain):
        return sent, "numeral-word"
    if not _premise_ok(plain, f, roles):
        return sent, "premise"
    # 數字在原句與去變音符號字串裡的位置不同（變音符號不是數字）：依序對到原句裡的第 k 個數字
    orig_nums = list(re.finditer(r"(?<![\d/])(?<!\d[.,])\d{1,4}(?!\d|[.,]\d|/)", sent))
    plain_nums = list(re.finditer(r"(?<![\d/])(?<!\d[.,])\d{1,4}(?!\d|[.,]\d|/)", plain))
    if len(orig_nums) != len(plain_nums):
        return sent, "ambiguous"
    idx = {pm.start(): k for k, pm in enumerate(plain_nums)}
    out, last = [], 0
    for m, v in subs:
        k = idx.get(m.start(1))
        if k is None:
            return sent, "ambiguous"
        om = orig_nums[k]
        out.append(sent[last:om.start()])
        out.append(str(v))
        last = om.end()
    out.append(sent[last:])
    return "".join(out), None


def _line(ln, f, protect, skipped, market=False):
    if ln.startswith(("|", "#", ">", "<!--")) or not ln.strip():
        return ln
    parts = SENT_SPLIT.split(ln)
    new, held = [], False
    for s in parts:
        if s.strip() and any(p and (p in s or s.strip() in p) for p in protect):
            new.append(s)
            continue
        ns, why = rewrite_sentence(s, f, market)
        if why:
            skipped.append((why, s.strip()))
            held = True
        new.append(ns)
    if held:
        return ln
    out = "".join(new)
    if out != ln and LINE_HOLD.search(DIAC.sub("", ln)):
        skipped.append(("ambiguous", ln.strip()))  # 同一行另講「其餘／另外幾張」或用文字數詞講張數：改了數字會對不上
        return ln
    return out


def merged(facts, mix):
    f = dict(facts or {})
    if mix:
        f.update(mix)
    return f


def rewrite(text, facts, mix=None, protect=()):
    """text：整頁 markdown。回傳 (新內容, skipped)。front matter、查核框、程式區塊、表格、標題不動。"""
    skipped = []
    if not facts or facts.get("partial") or facts.get("total") is None:
        return text, skipped
    f = merged(facts, mix)
    pb = re.search(r"<!-- licenses:begin -->(.*?)<!-- licenses:end -->", text, re.S)
    f["_shown"] = max(0, len(re.findall(r"^\|", pb.group(1), re.M)) - 2) if pb else None
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines, market, mlv = [], False, 0
    for ln in body.split("\n"):
        h = re.match(r"^(#{1,6}) (.+?)\s*$", ln)
        if h:
            lv = len(h.group(1))
            if h.group(2) in C.MARKET_SECTIONS:
                market, mlv = True, lv
            elif market and lv <= mlv:
                market = False
        lines.append(ln if "\x00" in ln else _line(ln, f, protect, skipped, market))
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
