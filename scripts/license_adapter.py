"""SA（SFDA 開放資料：已註冊人用藥清單）下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：https://www.sfda.gov.sa/en/open-data 頁面上的「قائمة الأدوية البشرية ... المسجلة」（已註冊人用藥，本地與非本地兩份 xlsx，免金鑰）。
2026-10-30 頁面上已不列人用藥清單，2023 年版原網址仍可下載（FALLBACK）；頁面若出現較新的人用藥清單會優先採用，SFDA 更新後自動跟上（用戶 2026-10-30 選「沿用現有來源排程」）。
清單只列已註冊品項、沒有許可證號與狀態欄：站上原本以 TradeName 當 license_id、status 一律 Registered。
在列＝Registered；新清單查不到的品名保留原狀態、列在 summary（不推定為撤銷）。
"""
import io
import re
import time
from urllib.parse import unquote, urljoin

import openpyxl
import requests

RAW_FILE = "raw/sfda_registered_tradenames.json"
PAGE = "https://www.sfda.gov.sa/en/open-data"
FALLBACK = {
    "المحلية": "https://www.sfda.gov.sa/sites/default/files/2023-10/قائمة-الأدوية-البشرية-المحلية-المسجلة-2023م.xlsx",
    "الغير-محلية": "https://www.sfda.gov.sa/sites/default/files/2023-10/قائمة-الأدوية-البشرية-الغير-محلية-المسجلة-2023م.xlsx",
}
HUMAN = re.compile(r"قائمة-الأدوية-البشرية-(المحلية|الغير-محلية)-المسجلة-(\d{4})")


def _get(url):
    for attempt in range(4):
        try:
            r = requests.get(url, timeout=180, headers={"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"})
            r.raise_for_status()
            return r
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))


def fetch():
    page = _get(PAGE)
    links = {}
    for href in re.findall(r'href="([^"]+\.xlsx)"', page.text):
        m = HUMAN.search(unquote(href))
        if m and (m.group(1) not in links or m.group(2) > links[m.group(1)][0]):
            links[m.group(1)] = (m.group(2), urljoin(PAGE, href))
    for kind, url in FALLBACK.items():  # 2026-10-30 開放資料頁已不再列出人用藥清單（只剩獸用），原網址仍可下載
        links.setdefault(kind, ("2023", url))
    out = []
    for kind, (year, url) in links.items():
        ws = openpyxl.load_workbook(io.BytesIO(_get(url).content), read_only=True).active
        ws.reset_dimensions()
        rows = ws.iter_rows(values_only=True)
        head = [str(x or "").strip() for x in next(rows)]
        if "TradeName" not in head:
            raise RuntimeError(f"{kind} 欄位改變：{head}")
        for row in rows:
            t = str(dict(zip(head, row)).get("TradeName") or "").strip()
            if t:
                out.append({"trade": t, "year": year, "kind": kind})
    return out


def validate(new, old):
    p = []
    if len(new) < 5000:
        p.append(f"只解析出 {len(new)} 筆，疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    return {r["trade"].upper(): "Registered" for r in new}


def record_id(rec):
    return str(rec.get("license_id") or "").strip().upper()


def update(rec, new):
    if rec.get("status") == new:
        return False
    rec["status"] = new
    return True


# 2026-11-24（用戶決定）：「معلومات السوق في السعودية」的許可證表改由 scripts/sync_license_tables.py 依證據包產生（程式區塊 <!-- licenses:begin/end -->）。
# 每週排程（license_refresh_20261029.py 的 sync_tables 掛鉤）全站重排：品項或狀態變了，表格列與表下說明句都跟著變；
# 只重排表格內容，表以外的正文不動（正文張數由 build_license_snapshot.py／apply_drug_reviews.py 結尾的 rewrite_license_counts.py 依快照改寫）。
# PAGE_NOTE：表格列以外、程式寫的行（說明句、區塊標記、沒有任何品項時的一句、證據包只收部分品項時的一句）。
# 2026-11-24 第三輪起含 add_section 補的市場段落標題。
PAGE_NOTE = (r"^(## معلومات السوق في السعودية|يعرض الجدول أعلاه \d+ من أصل \d+ من المنتجات المسجلة في البيانات\.|<!-- licenses:(begin|end) -->|"
             r"تتضمن البيانات جزءاً فقط من التراخيص؛ قد تكون القائمة غير مكتملة\.|"
             r"لا تتضمن قائمة الأدوية المسجلة لدى الهيئة العامة للغذاء والدواء \(البيانات المستخدمة في هذا التقرير\) أي منتج يحتوي على مكوّن هذا الدواء\.)$")


def sync_tables(site_dir, bundles):
    import importlib.util
    s = importlib.util.spec_from_file_location("sa_slt", site_dir / "scripts/sync_license_tables.py")
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return [(pg, "許可證表", "", "依證據包重排") for pg in m.run()]
