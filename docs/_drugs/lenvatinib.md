---
layout: default
title: Lenvatinib
parent: 中證據等級 (L3-L4)
nav_order: 367
evidence_level: L3
indication_count: 10
---

# Lenvatinib
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Lenvatinib：從已核准腫瘤適應症 到 Liposarcoma（脂肪肉瘤）

> ⚠️ 本證據包 `drug.original_indications` 為空、`original_moa` 標記為 Data Gap，且當地（Saudi Arabia/TFDA）許可資料 `licenses` 為空（`market_status: 未上市`）。以下「原始適應症」為 Lenvatinib（Lenvima）公開已知核准資訊（甲狀腺癌、肝細胞癌、腎細胞癌等），非本證據包來源，僅供背景參考。

## 一句話摘要

Lenvatinib 是已核准用於甲狀腺癌、肝細胞癌、腎細胞癌等多種實體腫瘤的多重酪氨酸激酶抑制劑（VEGFR/FGFR/PDGFR）。TxGNN 模型預測其可能對 **Liposarcoma（脂肪肉瘤）** 有效，目前有 **1 篇已完成臨床試驗**與 **4 篇文獻**支持，但證據集中於「Lenvatinib + Eribulin 併用療法」而非 Lenvatinib 單藥證據。

## 總覽表

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料包未提供（licenses 為空）；一般已知核准適應症包含甲狀腺癌、肝細胞癌、腎細胞癌等 |
| 預測新適應症 | Liposarcoma（脂肪肉瘤） |
| TxGNN 預測分數 | 99.51%（rank 7787） |
| 證據等級 | L3 |
| 當地市場狀態 | 未上市 |
| 許可證數量 | 0 |
| 建議決策 | Research Question（S2 階段） |

## 為什麼這個預測合理？

目前 `drug.original_moa` 標記為 Data Gap，缺乏藥品層級的正式機轉資料。但本證據包在 rank1 的 `repurposing_rationale` 中已提供機轉關聯說明：Lenvatinib 具抗血管新生機轉（抑制 VEGFR/FGFR/PDGFR），與 eribulin（微管抑制劑，已核准用於脂肪肉瘤/平滑肌肉瘤）併用時，具潛在協同細胞毒性效果。

去分化型脂肪肉瘤（dedifferentiated liposarcoma）具高度血管依賴性，因此抗血管新生藥物理論上可提供治療效益。**需特別注意**：現有支持證據（LEADER study, NCT03526679）評估的是 Lenvatinib+Eribulin 併用方案，而非 Lenvatinib 單藥療效，機轉合理但屬於併用療法的證據延伸，非 Lenvatinib 獨立作用證據。

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案人數 | 重點發現 |
|---------|------|------|------|---------|
| [NCT03526679](https://clinicaltrials.gov/study/NCT03526679) | Phase 1/2 | 已完成 | 30 | 單臂試驗，評估 Lenvatinib+Eribulin 於無法手術或轉移性脂肪細胞肉瘤及平滑肌肉瘤之安全性與療效 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 重點發現 |
|------|-----|------|------|---------|
| [36129471](https://pubmed.ncbi.nlm.nih.gov/36129471/) | 2022 | Phase1/2 單臂試驗 | Clinical Cancer Research | LEADER study（NCT03526679）正式發表：Lenvatinib+Eribulin 於晚期脂肪肉瘤/平滑肌肉瘤之安全性與療效 |
| [39103896](https://pubmed.ncbi.nlm.nih.gov/39103896/) | 2024 | 臨床前/生物標記 | Experimental Hematology & Oncology | 探討 CDK4 作為軟組織肉瘤預後生物標記，及其抑制劑於去分化型脂肪肉瘤序貫治療之協同效果 |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | 臨床前 | Anticancer Research | Eribulin 與多種不同機轉抗癌藥物併用之廣譜臨床前抗腫瘤活性評估 |
| [34326745](https://pubmed.ncbi.nlm.nih.gov/34326745/) | 2021 | 病例報告 | Case Reports in Oncology | 個案報告：肺轉移之去分化型脂肪肉瘤患者接受個別化治療（含標靶治療）後腫瘤明顯縮小 |

## 當地市場資訊

目前未在當地上市，無許可證資料（`total_licenses: 0`）。

## 細胞毒性資訊（抗腫瘤藥物專屬）

Lenvatinib 屬多重酪氨酸激酶抑制劑（targeted therapy），符合抗腫瘤藥物認定，故列出本節。惟本證據包未提供 DrugBank 毒性資料或當地仿單（`meta.data_gaps` DG001 標記為 Blocking：TFDA 仿單警語/禁忌缺失），以下為 TKI 藥物類別之一般已知風險，非本地仿單來源：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | Targeted therapy（多重酪氨酸激酶抑制劑，VEGFR1-3/FGFR1-4/PDGFRα/KIT/RET） |
| 骨髓抑制風險 | 請參照仿單警語與注意事項（本證據包無毒性資料） |
| 致吐性分類 | 請參照仿單警語與注意事項（本證據包無毒性資料） |
| 監測項目 | 一般 TKI 類別建議監測：血壓、心臟功能、肝腎功能、蛋白尿、甲狀腺功能、QT 間期（非本地仿單來源，僅供參考） |
| 處理防護 | 請依當地細胞毒性藥品處理規範辦理，實際規定需以當地仿單為準 |

## 安全性考量

請參照仿單以取得安全性資訊。

## 結論與下一步

**決策：Research Question（S2 階段）**

**理由：**
現有證據僅來自 1 篇已完成 Phase 1/2 單臂試驗（n=30）及其延伸文獻，且核心證據為 Lenvatinib+Eribulin 併用方案而非 Lenvatinib 單藥，尚不足以支持進入更高信心的決策階段。值得注意的是，本證據包中排序第 7 的「renal carcinoma」適應症證據等級達 L1（多個 Phase 3 RCT，含 CLEAR 試驗），但該適應症實質上是 Lenvatinib+Pembrolizumab 一線治療晚期腎細胞癌之**既有核准用途延伸**，而非真正的新適應症訊號；相較之下 liposarcoma 訊號證據較弱但屬於較新穎的老藥新用方向。

**後續需要補齊：**
- TFDA/當地仿單警語與禁忌資料（`DG001`，Blocking，目前無法進入 S1 安全性初評）
- Lenvatinib 作用機轉（MOA）正式資料（`DG002`）
- Lenvatinib 單藥（非併用 Eribulin）於脂肪肉瘤之獨立療效證據
- 藥物交互作用（DDI）查詢目前為 not_found，需另行查證
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

