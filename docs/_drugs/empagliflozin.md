---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 3
---

# Empagliflozin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Empagliflozin：原始適應症資料缺失，預測信號指向 Focal Stiff Limb Syndrome

## 一句話總結

Empagliflozin（DrugBank ID: DB09038）目前在沙烏地阿拉伯**未上市**（0 筆許可證），本證據包中亦未提供其原始核准適應症與作用機轉（MOA）資料。TxGNN 模型預測其可能與 **Focal Stiff Limb Syndrome** 相關，預測分數 **99.06%**，但目前**沒有任何臨床試驗、也沒有任何文獻**支持這個方向，證據等級為最低的 **L5（純模型預測）**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料未提供（藥品在沙烏地阿拉伯未上市，無許可證紀錄可供擷取） |
| 預測新適應症 | Focal Stiff Limb Syndrome |
| TxGNN 預測分數 | 99.06% |
| 證據等級 | L5 |
| 沙烏地阿拉伯市場狀態 | ✗ 未上市 |
| 許可證數量 | 0 |
| 建議決策 | Hold |

> 補充：同批次另有 2 個高度相近分數的預測適應症（見下方「同批次其他預測適應症」），三者證據等級與建議決策相同，均為 L5 / Hold。

---

## 為什麼這個預測合理？

目前尚無詳細作用機轉（MOA）資料——DrugBank 查詢雖已成功執行，但本證據包中 `original_moa` 標記為資料缺口，無法交叉驗證藥理路徑，也無法確認藥品的原始核准適應症。

根據證據包內附的機轉關聯性分析（repurposing rationale），Focal Stiff Limb Syndrome 屬於 stiff person syndrome 譜系的局部型，其病理機轉是抗 GAD65 抗體導致脊髓/皮質 GABA 能抑制訊號缺損，屬自體免疫神經肌肉疾病。而 Empagliflozin 作為 SGLT2 抑制劑，作用於腎近曲小管的鈉-葡萄糖共轉運，與 GABA 能傳導或自體免疫抗體生成路徑**沒有已知的直接機轉重疊**。

分析同時指出，這個高分預測很可能是 TxGNN 知識圖譜透過共病節點（例如糖尿病神經病變）或代謝相關節點間接連結所致，而非反映真實的藥理機轉關聯——換言之，這應被視為**假說產生（hypothesis generation）**，而不是具生物學合理性的候選。在缺乏 MOA 資料可供交叉驗證的情況下，此預測的可信度需進一步下修。

---

## 臨床試驗證據

Currently no related clinical trials registered.

（`clinicaltrials` 與 `ictrp` 兩個來源皆於 2026-04-21 查詢，針對 Empagliflozin + Focal Stiff Limb Syndrome 結果數皆為 0。）

---

## 文獻證據

Currently no related literature available.

（`pubmed` 於 2026-04-21 查詢 Empagliflozin + Focal Stiff Limb Syndrome，結果數為 0。）

---

## 同批次其他預測適應症

除首位預測外，同批次還有兩個機轉合理性同樣偏低、且完全無臨床試驗與文獻支持的候選：

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 建議決策 | 機轉關聯性摘要 |
|------|------|-----------|---------|---------|----------------|
| 2 | Classic Stiff Person Syndrome | 99.06% | L5 | Hold | 核心病理為抗 GAD65 抗體攻擊 GABA 合成酶，與 SGLT2 抑制機轉無實證關聯，無動物或體外研究支持 |
| 3 | Opsismodysplasia | 99.03% | L5 | Hold | 罕見骨骼發育不良疾病，主因 INPPL1（SHIP2）基因突變；與 SGLT2 抑制作用無已知分子路徑連結，零臨床零文獻支持 |

三者分數高度接近，且皆查無臨床試驗、文獻或 ICTRP 登錄紀錄，顯示此批預測可能反映知識圖譜嵌入相似性，而非獨立驗證過的藥理假說。

---

## 安全性考量

Please refer to the package insert for safety information.

（本證據包中之警語、禁忌症、藥物交互作用皆標記為資料缺口或查無資料；`ddi` 查詢狀態為 `not_found`。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 三個預測適應症皆為 L5（純模型預測），無任何臨床試驗或文獻佐證，且證據包本身的機轉分析已指出生物學合理性偏低，更可能是知識圖譜間接連結所致的假說，而非藥理機轉。
- 存在一個 Blocking 等級資料缺口（DG001：TFDA/SFDA 仿單警語與禁忌症未取得），依規定無法進入安全性初評（S1）階段。

**若要繼續推進，需要補充：**
- TFDA/SFDA 官網仿單 PDF（警語、禁忌症）— Blocking，須優先解決
- 透過 DrugBank API 補齊作用機轉（MOA）資料 — High 優先
- 藥品原始核准適應症之完整清單（目前為空）
- 藥物交互作用（DDI）資料庫查詢結果
- 若後續要推進 Focal Stiff Limb Syndrome / Classic Stiff Person Syndrome 方向，建議另行檢索是否有病例報告（case report）等級的文獻，目前 PubMed 查詢完全無結果
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

