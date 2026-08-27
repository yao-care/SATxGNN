---
layout: default
title: Palbociclib
parent: 僅模型預測 (L5)
nav_order: 471
evidence_level: L5
indication_count: 4
---

# Palbociclib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Palbociclib：從乳癌治療到四項 TxGNN 預測新適應症的初步評估

## 一句話摘要

Palbociclib（DB09073）為 CDK4/6 抑制劑，原始適應症資料在本證據包中缺失，但依公開藥理學已知用於 HR+/HER2- 乳癌治療。TxGNN 模型針對此藥提出 4 項候選新適應症（甲狀腺機能亢進、類風濕性關節炎、血栓性疾病、甲狀腺素受體β突變抗性），其中僅**類風濕性關節炎**有機轉性文獻與個案報告支持（L4），其餘 3 項要嘛完全無證據（L5），要嘛證據方向與預測相反——**血栓性疾病**的文獻反而顯示 CDK4/6 抑制劑會「誘發」而非治療血栓事件，應視為安全性警訊而非治療候選。

---

## 快速總覽

### 藥物基本資訊

| 項目 | 內容 |
|------|------|
| 原始適應症 | 證據包未提供結構化資料（`original_indications` 為空）；依已知藥理分類為 CDK4/6 抑制劑，用於乳癌治療 |
| 作用機轉 (MOA) | [Data Gap] — DrugBank 查詢未取得 |
| 沙烏地阿拉伯市場狀態 | 未上市 |
| 授權許可數 | 0 |
| 資料缺口（阻斷性） | TFDA 仿單警語/禁忌缺失 → **無法進入 S1 安全性初評**（DG001, Blocking） |

### 四項預測適應症比較

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|-----------|-----------|---------|---------|------|
| 1 | Hyperthyroidism（甲狀腺機能亢進） | 99.44% | L5 | S0 | Hold |
| 2 | Rheumatoid arthritis（類風濕性關節炎） | 99.36% | L4 | S1 | Research Question |
| 3 | Thrombotic disease（血栓性疾病） | 99.32% | L5 | S0 | Hold（證據方向相反，應視為安全性警訊） |
| 4 | 甲狀腺素受體β突變抗性 | 99.30% | L5 | S0 | Hold |

**整體建議決策：Hold**（因 DG001 為阻斷性資料缺口，任何候選皆無法進入安全性初評；類風濕性關節炎方向可列為研究問題持續追蹤）

---

## 為什麼這些預測合理／不合理？

目前無詳細作用機轉資料。依已知資訊，palbociclib 為 CDK4/6 抑制劑（cyclin-dependent kinase 4/6 inhibitor），其乳癌治療效果已獲證實，機轉上可能適用於其他細胞週期調控相關疾病。

**類風濕性關節炎（唯一有支持性證據的方向）**：CDK4/6 調控滑膜纖維母細胞（synovial fibroblast）的細胞週期進程，是 RA 血管翳（pannus）形成與滑膜增生的關鍵驅動因子之一。2025 年小鼠模型研究證實 CDK6 依賴（CDK4 非依賴）路徑驅動關節炎滑膜增生，2016 年臨床前研究顯示細胞週期調控合併細胞激素阻斷可增強抗關節炎效果。人類端有一例乳癌病人使用 palbociclib 後 RA 症狀改善之個案報告。證據方向一致，但完全缺乏對照性臨床試驗，僅為個案報告＋臨床前機轉等級。

**血栓性疾病（證據方向與預測相反）**：文獻反覆顯示 CDK4/6 抑制劑（此藥物類別）在真實世界藥物流行病學資料中會**誘發**而非治療血栓事件——FAERS 不成比例分析、真實世界世代研究均顯示與靜脈血栓栓塞風險上升相關，同類藥 ribociclib 甚至有腦靜脈竇血栓個案報告。兩筆臨床試驗（Belzutifan 併用試驗、COVID-19 試驗-已撤回）皆非以「治療血栓疾病」為適應症設計。此為 TxGNN 分數與實際證據方向相反的個案。

**甲狀腺機能亢進、甲狀腺素受體β突變抗性**：無任何臨床試驗或文獻支持，亦無已知 CDK4/6 抑制與甲狀腺路徑之機轉關聯，純屬模型預測，缺乏生物學合理性論述基礎。

---

## 臨床試驗證據

### 血栓性疾病（唯一有試驗登記的方向）

| 試驗編號 | 期別 | 狀態 | 收案人數 | 重點發現 |
|---------|------|------|------|---------|
| [NCT05468697](https://clinicaltrials.gov/study/NCT05468697) | Phase 1/2 | Active, not recruiting | 60 | Belzutifan 併用 palbociclib 治療晚期腎細胞癌，非以血栓疾病為適應症，相關性低（Grade C） |
| [NCT05371275](https://clinicaltrials.gov/study/NCT05371275) | Phase 2 | Withdrawn（已撤回，收案 0 人） | 0 | 評估 palbociclib 於住院中重度 COVID-19 病人預防血栓發炎（thromboinflammation）之安全性，已撤回無法提供證據 |

### 其他三項適應症

目前無相關臨床試驗登記。

---

## 文獻證據

### 類風濕性關節炎

| PMID | 年份 | 類型 | 期刊 | 重點發現 |
|------|-----|------|------|---------|
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Review | The Oncologist | 探討 HR+/HER2- 乳癌病人接受 CDK4/6i 治療時既有及新發自體免疫疾病之盛行率與影響 |
| [39940918](https://pubmed.ncbi.nlm.nih.gov/39940918/) | 2025 | Preclinical Mechanistic Study | Int J Mol Sci | CDK6 依賴（CDK4 非依賴）路徑驅動關節炎小鼠滑膜增生；提及 palbociclib 曾被探索用於 RA，但臨床前研究觀察到骨髓抑制 |
| [33587021](https://pubmed.ncbi.nlm.nih.gov/33587021/) | 2021 | Case Report | Mod Rheumatol Case Rep | 一名乳癌合併 RA 病人使用 palbociclib 後，關節炎症狀獲得改善 |
| [25165034](https://pubmed.ncbi.nlm.nih.gov/25165034/) | 2016 | Preclinical (Animal Model) | Ann Rheum Dis | 細胞週期調控（CDK 抑制劑）合併細胞激素阻斷，在 RA 動物模型中增強抗關節炎效果且不增加免疫抑制 |

### 血栓性疾病

| PMID | 年份 | 類型 | 期刊 | 重點發現 |
|------|-----|------|------|---------|
| [39302147](https://pubmed.ncbi.nlm.nih.gov/39302147/) | 2025 | Basic Science | Cardiovascular Research | dsDNA 經 cGAS 路徑增強血小板活化與血栓形成（與 palbociclib 無直接關聯之基礎研究） |
| [37994878](https://pubmed.ncbi.nlm.nih.gov/37994878/) | 2023 | Review | Expert Opin Drug Saf | CDK4/6 抑制劑用於乳癌治療時的間質性肺病與骨髓抑制、腸胃道毒性等已知不良反應回顧 |
| [39123221](https://pubmed.ncbi.nlm.nih.gov/39123221/) | 2024 | Pharmacovigilance (FAERS) | BMC Pharmacol Toxicol | 比較三種 CDK4/6 抑制劑（palbociclib/abemaciclib/ribociclib）不良反應差異 |
| [39083396](https://pubmed.ncbi.nlm.nih.gov/39083396/) | 2025 | Pharmacovigilance (FAERS) | Expert Opin Drug Saf | FAERS 不成比例分析評估 CDK4/6 抑制劑相關不良事件 |
| [41496429](https://pubmed.ncbi.nlm.nih.gov/41496429/) | 2026 | Pharmacovigilance (FAERS) | Breast (Edinburgh) | 高齡乳癌病人使用 CDK4/6 抑制劑之年齡分層毒性分析 |
| [35300061](https://pubmed.ncbi.nlm.nih.gov/35300061/) | 2022 | Cohort (Real-world) | Cancer Manag Res | Ribociclib 併用 letrozole/fulvestrant 治療 HR+/HER2- 轉移性乳癌病人之血栓栓塞事件真實世界資料 |
| [36794339](https://pubmed.ncbi.nlm.nih.gov/36794339/) | 2023 | Pharmacovigilance Cohort | Expert Opin Drug Saf | 真實世界藥物流行病學研究＋系統性回顧，評估 CDK4/6 抑制劑與血栓形成之關聯 |
| [38390439](https://pubmed.ncbi.nlm.nih.gov/38390439/) | 2024 | Case Report（ribociclib，非 palbociclib） | SAGE Open Med Case Rep | 使用 ribociclib 治療轉移性乳癌病人發生腦靜脈竇血栓之個案報告 |
| [27098250](https://pubmed.ncbi.nlm.nih.gov/27098250/) | 2016 | Preclinical (Animal Model) | Circ Cardiovasc Genet | 高膽固醇血症合併 Cdkn2a 缺失小鼠之巨核細胞生成與血小板活性增強（與 CDK 路徑相關之基礎研究） |
| [40623899](https://pubmed.ncbi.nlm.nih.gov/40623899/) | 2025 | Guideline（不相關主題） | Zhonghua Xue Ye Xue Za Zhi | B型血友病基因治療臨床應用指引，主題與血栓疾病治療無直接相關 |

### 甲狀腺機能亢進、甲狀腺素受體β突變抗性

目前無相關文獻可供參考。

---

## 沙烏地阿拉伯市場資訊

目前 palbociclib 於沙烏地阿拉伯**未上市**，無任何上市許可紀錄（`total_licenses = 0`）。

---

## 細胞毒性資訊

Palbociclib 屬 CDK4/6 抑制劑，依已知藥理分類為腫瘤標靶治療藥物（原始適應症為乳癌治療，DrugBank 結構化毒理資料未取得）。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶治療（Targeted therapy）— CDK4/6 抑制劑，非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 偏高 — 本證據包文獻（PMID 39940918、37994878）提及 palbociclib/CDK4/6i 類已知會造成骨髓抑制，屬乳癌治療族群常見不良反應 |
| 致吐性分類 | 請參考仿單警語與注意事項 |
| 監測項目 | 全血球計數（CBC，含分類計數）、肝腎功能 |
| 處理防護 | 請依細胞毒性藥品處理規範辦理 |

---

## 安全性考量

請參考仿單以取得完整安全性資訊。

（`safety.key_warnings`、`safety.contraindications`、`safety.ddi` 於本證據包中均為資料缺口；DG001 已標記為阻斷性缺口，使本候選無法進入 S1 安全性初評。）

---

## 結論與後續步驟

**決策：Hold**（類風濕性關節炎方向可列為 Research Question 持續追蹤）

**理由：**
- 阻斷性資料缺口 DG001（TFDA 仿單警語/禁忌缺失）使本候選目前無法進入 S1 安全性初評，任一適應症皆無法往下推進決策階段。
- 4 項預測中僅類風濕性關節炎有機轉一致的臨床前與個案證據（L4），其餘 3 項證據等級為 L5（純模型預測，無實證支持），其中血栓性疾病方向的既有證據甚至與預測相反，應視為安全性警訊而非治療機會。

**若要繼續推進，需要補充：**
- TFDA/原廠仿單完整警語與禁忌資料（DG001，阻斷性，優先處理）
- DrugBank 作用機轉（MOA）與藥物分類完整資料（DG002）
- 藥物交互作用（DDI）查詢結果
- 若欲推進類風濕性關節炎方向：需設計對照性臨床試驗（目前僅個案報告與動物模型等級證據）
- 若繼續評估血栓性疾病方向：應轉為安全性監測議題，而非療效候選
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

