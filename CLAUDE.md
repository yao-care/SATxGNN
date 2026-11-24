# SATxGNN 維護說明

各站共通的維護流程見母 repo（yao-care/txgnn）的 CLAUDE.md；本檔只記本站自己的機制。

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」「藥物頁許可證表與張數」兩節）；
UsTxGNN 是第一個試做站（做法見 UsTxGNN/CLAUDE.md 同名一節）。本站的規則與程式都在本 repo，頁面文字用阿拉伯文（由右至左、阿拉伯標點），依據是SFDA 開放資料的註冊藥品清單（只列已註冊品項；表格第一欄是產品註冊名，沒有獨立許可證號，所以只驗品牌名屬於本藥，site.py 的 ID_MATCH）。
本站的在地字樣、頁首規則細節、歷史刪改的提交清單集中在 `src/satxgnn/regulatory/site.py`。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、每頁在免責聲明前的查核紀錄表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/satxgnn/regulatory/page_format.py` | 頁首＝快速總覽「مستوى الدليل／مستوى الأدلة」格的**第一個**等級（主預測，不照 Tw 整格取最高）；頁首已是 N/A 的頁不重算。2026-11-12 實測有 6 頁頁首 L5 跟總覽格第一個等級不同（dasabuvir、favipiravir、quetiapine、ranibizumab、trifluoperazine、warfarin），2026-11-12 同日依 methodology 重審（`sa-rr-20261112-*`），HEADER_EXCEPTIONS 已清空、待查清單標 resolved |
| 撤回預測 | `src/satxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/sa_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/satxgnn/regulatory/licenses.py` | 快照存本藥許可證號與事實層；gate 依快照驗市場段落表格的許可證號屬於本藥、狀態列與張數列＝事實層寫法、表格列狀態不跟事實相反（本站沒有程式產生的許可證表，不驗表格列內容） |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依 git 前後版本（或改寫前後目錄）把正文刪改轉成 correct 紀錄 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證與待重審項目；證據包沒有許可證適應症文字時照實回報可比對 0 頁 |
| gate | `scripts/check_seo_docs.py` 最後 4 項 | 紀錄都已套用、許可證＝快照、頁首＝快速總覽等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、每週排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（每週排程會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 依新事實直接刪掉的矛盾子句，2026-11-12 已用 `scripts/reviews_from_edits.py --git` 轉成 657 筆紀錄（465 頁）。
`scripts/sync_notes_to_docs.py` 依 notes 重寫整頁後會重套紀錄，notes 裡的舊錯句會被紀錄再更正一次。
2026-11-12 頁首例外 6 頁的重審：總覽格「預測新適應症」是排名第一的預測，其中 4 頁（favipiravir、quetiapine、ranibizumab、warfarin）的等級格寫的卻是報告另外評估的適應症的等級。依總覽格的適應症重審（PubMed、ClinicalTrials.gov）：dasabuvir L3→L5、favipiravir L4→L5、quetiapine L4→L5、ranibizumab L1→L5（決策改 Hold）、warfarin L1→L4（決策改 Hold）、trifluoperazine 維持 L4；頁首隨總覽格（trifluoperazine、warfarin 由 L5 改 L4，記 header_level／description_level），衍生檔（drug_stats、drugs.json、FHIR、search-index、llms、README）已重產。
同日正文許可證張數對快照事實層的掃描：0 筆不符（正文的數字都是總數、有效數或「列出其中 N 張」，SFDA 清單只有已註冊品項）。
2026-11-12 許可證表格列狀態對事實層（母目錄 check_drug_page.py --row-status）：23 頁 33 列在 SFDA 註冊清單上（data-20261105 原始清單 Status 全為 Registered）的品項標成「ملغى」，以 33 筆 `sa-row-20261112-*` correct 紀錄改成本站既有寫法「ساري」。表格裡其他「ملغى」列的品項不在快照本藥名單（事實不明），這次不動。

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 168 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「لا تتوفر حالياً بيانات تفصيلية عن آلية عمل الدواء.」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `sa-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：本站語言（العربية）的出處句＋節錄的忠實翻譯（標明「非官方翻譯」）＋英文原文（照引、為準）＋DailyMed 連結、仿單版本、取用日期（用戶 2026-11-19 決定「當地語言摘要＋英文原文」）。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 翻譯：節錄的翻譯是 AI 輔助的忠實翻譯（不增不減，藥名、基因與受體符號、數字、「[…]」照原文），2026-11-19 批次產生，存在紀錄 sources 的 translation（translation_lang、translation_note 註明非官方、英文原文為準）；頁面上同時列英文原文。`--translations <檔>` 讀翻譯、`--need <檔>` 列出還沒翻的節錄（這些頁那次不寫紀錄，gate 會擋，翻好再跑）。
- 2026-11-19 結果：123 頁寫入紀錄（美國仿單 106、ChEMBL 17），45 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 21 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）；ChEMBL 譯文（詞組清單）後補句號 17 筆；「وفقًا لـقسم」改成規範寫法「وفقًا لقسم」106 筆；同 id 重發，前版 replacement 存 history。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；偵測漏抓的「不可得」句補 512 筆紀錄、100 頁列待查；同頁重複引用同一段節錄的 1 筆改成指向上方節錄的一句（附同一個來源連結）；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「الاستطباب الأصلي: غير مسجل في البيانات المحلية」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：SFDA 註冊品項。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：abatacept「الاستطباب الأصلي: غير مسجل في البيانات المحلية」→「المنتجات المسجلة لدى SFDA: 2 (السارية: 2)」；2026-11-19 改了 346 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site SATxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。

## 市場段落許可證表與正文張數改由程式維護（2026-11-24）

用戶 2026-11-24 決定（30 站「許可證張數與狀態不再每週過期」，本站做表＋B）：每週許可證排程只改得到概覽表狀態列／張數列，AI 寫的自由格式許可證表（表頭十幾種寫法，劑型、適應症欄多半寫「غير مسجّل」，
狀態寫在品名格「(ملغى)」或狀態欄；2026-11-12 就以 33 筆 sa-row 紀錄人工更正過）與正文寫死的張數，會跟主管機關資料矛盾、checker 擋頁。
- 量測（改前，公開藥物頁 882 頁，沒有 noindex 頁）：有市場段落 869 頁，其中 849 頁有 AI 許可證表、20 頁段落裡沒有表，13 頁沒有市場段落；正文含許可證數字的句子 336 句（非 partial 頁 293、partial 頁 43），
  跟事實層不符的 0 句（另 25 句是講表上列了幾筆）。本站事實層：SFDA 已註冊人用藥清單只列已註冊品項，有效數＝總數、註銷數＝0。
- A. `scripts/sync_license_tables.py`（照 HkTxGNN 同名檔）：市場段落（site.MARKET_SECTIONS）第一張表換成程式依證據包 tfda.records 產生的
  「| اسم المنتج المسجل (بالإنجليزية كما في SFDA) | المادة الفعالة (بالإنجليزية) | الشركة المصنّعة | الحالة |」：第一欄＝license_id（產品註冊名，SFDA 沒有獨立許可證號，同 site.ID_MATCH），
  成分、廠商照 SFDA 英文原文（不翻譯、表頭註明），狀態 ساري（license_status＝cancelled 才寫 مُلغى；目前沒有）。選列照換表當時報告原表依序列出的品項（`config/license_table_pins.json`，
  849 頁 2,513 列中 2,489 列對到證據包 license_id；對不到的 24 列是報告列了、SFDA 清單沒有的品項（例 dapoxetine 的 DEPOJOY、LEJAM、Elong，原表標 ملغى；正文沒有提到這些品名），不收），
  其餘依單一成分在前、品名排序；列數＝原表列數（最多 20）；總數較多時表下「يعرض الجدول أعلاه N من أصل M من المنتجات المسجلة في البيانات.」，證據包只收部分品項（55 頁）時加
  「تتضمن البيانات جزءاً فقط من التراخيص؛ قد تكون القائمة غير مكتملة.」；段落裡沒有表的 20 頁在標題下補 min(5, 總數) 列。單一成分／複方照成分欄「,」個數（事實層用「;;」切，本站每張都算單方，不能用）。
  換表時（`--migrate`）拿掉緊鄰舊表、只講表上筆數的說明行 19 行（例「(عُرضت 5 من أصل 7 تراخيص.)」；講其餘品名的說明句不動）。前後 `<!-- licenses:begin/end -->`。
  快照另存 rows／nrows／partial_line／mix（`scripts/build_license_snapshot.py`）；gate 第 18 項（`src/satxgnn/regulatory/licenses.py` 的 program_block_problems）擋程式區塊≠快照重算、市場段落有程式區塊以外的表。
  接進：每週排程 `scripts/license_adapter.py` 的 sync_tables（全站重排）與 PAGE_NOTE、`scripts/sync_notes_to_docs.py`（carry_block 移植舊頁程式區塊，寫完再跑 sync_license_tables）。
- B. `scripts/rewrite_license_counts.py`＋`src/satxgnn/regulatory/count_prose.py`（移植 Kr／My／Hk，阿拉伯文句型）：只改阿拉伯數字＋許可證名詞（ترخيص／تراخيص／ترخيصًا）或講許可證的「(N من M)」；
  有保留、相對數（آخر／أخرى／إضافي）、講資料或查詢、劑型或廠商子集（數字所在子句有英文字母也算）、顯示筆數（عُرضت／أبرز／أول／منها、「X من أصل Y」的 X）、partial 頁、查核紀錄 replacement／anchor 所在句不動；
  同一句用文字數詞（الأربعة、ترخيصان…）講張數、同一行另講「其餘幾張」時整行不動；數詞配合：數字後接許可證名詞而新舊數字不在同一組（3～10「تراخيص」、11～99「ترخيصًا」）就不改、列 agreement；
  單一成分／複方只驗不改；改成 0、原本 0 不改。`apply_drug_reviews.py`（非 --check）結尾與 `build_license_snapshot.py` 結尾自動跑（不帶 --ws 時只依現有快照改寫）；gate 第 22 項擋「再跑一次會變」。
  2026-11-24 全站跑：改寫 0 句（現行正文張數都跟事實層一致），判斷不了的 0 句；模擬事實變動（每頁總數＝有效數＋1）時改寫 148 行、107 頁，判斷不了的列出：文字數詞 134、ambiguous 8、premise 5、agreement 4、子集 4。
- 查核紀錄：錨在舊表列上的 33 筆 `sa-row-20261112-*` 標 `status: superseded`＋`superseded_by`；說明框寫死「عدد التراخيص في البيانات: N، منها سارية: V」的 642 筆、更正文字寫死張數／舊表筆數的 6 筆
  （amlodipine、diclofenac、everolimus、imipenem、insulin_lispro、pantoprazole）同 id 重發（共 645 筆，前版存 history），改成不寫數字、指向概覽表與程式表；site.py 的 FIGURES 同步改成不寫數字。
  獨立寬偵測另找到單一成分說法跟成分欄相反的 3 頁（diphenylpyraline、ginseng、polymyxin_b，實為全部複方）與決策理由寫唯一許可已註銷的 lonoctocog_alfa（Afstyla 在 SFDA 清單），以 4 筆 `sa-lic-20261124-*` 更正。
  「下一步」待辦條目以「許可證已全部註銷」為前提的 12 句（11 頁 partial 頁＋lonoctocog_alfa）照規則不改，列進待查清單。
- 驗證：checker 全量改前 0／改後 0；`--row-status` 0 列；gate exit 0；寬偵測（正文張數不在事實層總數／有效數／程式表列數裡、寫註銷、寫全部單方而成分欄是複方）剩：張數 11 句（劑量、「其餘 N 張」相對數、點名表外品項的說明，都跟事實一致）、待辦條目 11 句（已列待查）。
- 已知：母目錄 `.claude/license_labels/SATxGNN.json` 把「مُلغى」對到 valid（看起來應是 cancelled）；本站資料目前沒有註銷品項，程式表不會寫到，沒有改母目錄。
