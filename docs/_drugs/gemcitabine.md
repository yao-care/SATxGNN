---
layout: default
title: Gemcitabine
parent: 高證據等級 (L1-L2)
nav_order: 290
evidence_level: L1
indication_count: 10
---

# Gemcitabine
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Gemcitabine: From Established Cytotoxic Chemotherapy to Female Breast Carcinoma

## 一句話摘要

Gemcitabine（健擇）是廣泛使用於多種實體腫瘤的細胞毒性化療藥物；本次 Evidence Pack 未提供其台灣核准原始適應症清單。TxGNN 模型預測其對**乳癌（Female Breast Carcinoma）**具高度相關性，目前有 **50 篇臨床試驗**與 **20 篇文獻**支持此方向，其中包含一項已完成的關鍵第三期 RCT（gemcitabine+paclitaxel vs. paclitaxel）。

---

## 總覽表

| 項目 | 內容 |
|------|------|
| 原始適應症 | Evidence Pack 未提供台灣核准適應症資料（本品目前未於台灣上市，無許可證紀錄） |
| 預測新適應症 | Female Breast Carcinoma（乳癌） |
| TxGNN 預測分數 | 99.98%（rank 683） |
| 證據等級 | L1 |
| 台灣市場狀態 | 未上市 |
| 許可證數量 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為何此預測合理？

目前 DrugBank 詳細作用機轉（MOA）欄位為空值缺口（DG002，High severity）。根據本次分析附帶的機轉關聯性資料，gemcitabine 為去氧胞苷（deoxycytidine）核苷類似物，主要透過抑制核糖核苷酸還原酶（ribonucleotide reductase）並嵌入 DNA 造成鏈終止，達到細胞毒殺作用，屬廣效型抗代謝化療藥物。

Evidence Pack 未收錄本品的台灣原始核准適應症，但由收錄的臨床試驗可見，gemcitabine 早已廣泛用於乳癌治療：一項已完成的第三期隨機對照試驗（NCT00006459）直接比較 gemcitabine+paclitaxel 與 paclitaxel 單用於轉移性乳癌，另有一項納入 4,894 名患者的大型輔助治療第三期試驗（NCT00093795）將 gemcitabine 納入其中一組治療臂（AC→PG）。乳癌屬高增殖性實體腫瘤，此類病理特性與 gemcitabine 已建立療效之其他實體瘤（如胰臟癌、非小細胞肺癌）具共同的藥理學基礎。

多項第二期試驗亦顯示 gemcitabine 併用 trastuzumab／pertuzumab（HER2 陽性乳癌）、docetaxel（新輔助治療）等組合具臨床活性，顯示此機轉延伸至乳癌治療具有充分的臨床實務基礎，而非僅為模型的抽象關聯。

---

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案人數 | 關鍵發現 |
|---------|------|------|------|---------|
| [NCT00193063](https://clinicaltrials.gov/study/NCT00193063) | Phase 2 | Completed | 41 | HER2 過表現轉移性乳癌，gemcitabine + trastuzumab 併用療效評估 |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Phase 3 | Unknown | 1206 | 可觸診/可手術乳癌新輔助治療，比較加入 capecitabine 或 gemcitabine 於 docetaxel 對病理完全緩解（pCR）之影響 |
| [NCT01352494](https://clinicaltrials.gov/study/NCT01352494) | Phase 2 | Unknown | 99 | 多中心試驗，docetaxel+gemcitabine 用於局部晚期乳癌新輔助化療 |
| [NCT00244933](https://clinicaltrials.gov/study/NCT00244933) | Phase 2 | Completed | 19 | 轉移性乳癌，gemcitabine+genistein 併用及生物標記分析 |
| [NCT07528768](https://clinicaltrials.gov/study/NCT07528768) | Phase 2 | Not yet recruiting | 750 | 加勒比海非裔女性三陰性轉移性乳癌，gemcitabine 作為一線治療對比 paclitaxel |
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | Completed | N/A | 隨機分派 RCT：paclitaxel 併用或不併用 gemcitabine，用於無法切除、局部復發或轉移性乳癌 |
| [NCT00093795](https://clinicaltrials.gov/study/NCT00093795) | Phase 3 | Completed | 4894 | 大型輔助治療 RCT，比較三種化療方案（含 AC→劑量密集 paclitaxel+gemcitabine 臂），淋巴結陽性乳癌 |
| [NCT00440622](https://clinicaltrials.gov/study/NCT00440622) | Phase 3 | Terminated | 90 | HER-2 陽性轉移性乳癌，gemcitabine+Herceptin 對比 capecitabine+Herceptin |
| [NCT02252887](https://clinicaltrials.gov/study/NCT02252887) | Phase 2 | Completed | 45 | 曾接受 trastuzumab/pertuzumab 治療之 HER2 陽性轉移性乳癌，gemcitabine+trastuzumab+pertuzumab 療效與安全性 |
| [NCT02139358](https://clinicaltrials.gov/study/NCT02139358) | Phase 1/2 | Completed | 15 | 曾治療之 HER2 陽性轉移性乳癌，gemcitabine+trastuzumab+pertuzumab 安全性與活性評估 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 關鍵發現 |
|------|-----|------|------|---------|
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase1 Cohort | Breast Cancer Res Treat | Carboplatin+gemcitabine+mifepristone 第一期試驗，用於晚期乳癌及復發/持續性卵巢上皮癌 |
| [38262235](https://pubmed.ncbi.nlm.nih.gov/38262235/) | 2024 | Phase1 | Gynecologic Oncology | Mirvetuximab soravtansine+gemcitabine 第一期試驗，含三陰性乳癌族群，測定最大耐受劑量 |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Phase1/2 Cohort | Tumori | Docetaxel+gemcitabine 劑量探索研究，用於蒽環類藥物治療後之轉移性乳癌 |
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Review | Oncology (Williston Park) | Gemcitabine+paclitaxel 於轉移性乳癌之療效回顧，第二/三期試驗緩解率達52% |
| [15685821](https://pubmed.ncbi.nlm.nih.gov/15685821/) | 2004 | Review | Oncology (Williston Park) | Gemcitabine 併用鉑類藥物於轉移性乳癌之臨床效益回顧 |
| [15685820](https://pubmed.ncbi.nlm.nih.gov/15685820/) | 2004 | Review | Oncology (Williston Park) | Gemcitabine+docetaxel 於轉移性乳癌，機轉互補與毒性側寫部分重疊 |
| [14768404](https://pubmed.ncbi.nlm.nih.gov/14768404/) | 2003 | Review | Oncology (Williston Park) | Gemcitabine 併用蒽環類/紫杉類藥物組合於晚期乳癌之療效綜述 |
| [12722022](https://pubmed.ncbi.nlm.nih.gov/12722022/) | 2003 | Review | Seminars in Oncology | Gemcitabine+trastuzumab 第二期試驗背景與初步結果，重度預治療轉移性乳癌 |
| [12138397](https://pubmed.ncbi.nlm.nih.gov/12138397/) | 2002 | Review | Seminars in Oncology | Gemcitabine 單藥及合併標靶治療於轉移性乳癌，緩解率16%-37% |
| [24295415](https://pubmed.ncbi.nlm.nih.gov/24295415/) | 2013 | Review | Future Oncology | 微脂體化療藥物綜述，以 gemcitabine 與 paclitaxel 為例說明微脂體劑型優勢 |

---

## Cytotoxicity（細胞毒性資訊）

Gemcitabine 屬於已知的傳統細胞毒性化療藥物（去氧胞苷類似物/抗代謝物），符合本項目納入標準，說明如下：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | Conventional cytotoxic（抗代謝物 / 核苷類似物，Deoxycytidine analogue） |
| 骨髓抑制風險 | 請參考仿單警語與注意事項（本 Evidence Pack 未提供具體毒性數據） |
| 致吐性分類 | 請參考仿單警語與注意事項 |
| 監測項目 | 全血球計數（含白血球分類）、肝腎功能，依常規細胞毒性化療監測原則進行 |
| 處理防護 | 屬細胞毒性化療藥品，調配與給藥應依機構細胞毒性藥品處理規範辦理 |

---

## 安全性考量

請參考仿單警語與注意事項以取得完整安全性資訊（本 Evidence Pack 之關鍵警語、禁忌症與藥物交互作用資料均為缺口，DG001 為 Blocking 等級）。

---

## 結論與後續步驟

**決策：Proceed with Guardrails**

**理由：**
多項第二/三期臨床試驗（含一項已完成之關鍵第三期 RCT NCT00006459，以及納入 4,894 名患者的大型輔助治療試驗 NCT00093795）支持 gemcitabine 於乳癌治療之臨床活性，證據等級達 L1；但台灣仿單警語/禁忌症資料（DG001，Blocking）尚未取得，無法完成 S1 安全性初評，故不宜逕行放行，須於補齊安全性資料後方可推進。

**推進前需補齊：**
- TFDA 官網仿單警語與禁忌症資料（DG001，Blocking）
- DrugBank 完整 MOA 資料確認（DG002）
- 藥物交互作用（DDI）資料庫查詢結果（目前 query_status 為 not_found）
- 台灣上市/引進評估（本品目前於台灣未上市，0 張許可證）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

