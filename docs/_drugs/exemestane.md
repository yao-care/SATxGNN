---
layout: default
title: Exemestane
parent: 僅模型預測 (L5)
nav_order: 248
evidence_level: L5
indication_count: 7
---

# Exemestane
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Exemestane: From Breast Cancer to Antithrombin Deficiency Type 2

## One-Sentence Summary

Exemestane 是一種芳香酶抑制劑，原始適應症脈絡（依證據包內文獻上下文推斷）為停經後荷爾蒙受體陽性乳癌治療；TxGNN 模型將其最高分預測連結到 **Antithrombin Deficiency Type 2**（一種遺傳性抗凝血酶基因突變疾病），但目前**零臨床試驗、零文獻支持**，且證據包本身的機轉分析已明確指出此為圖譜結構性偽相關，缺乏生物學合理性。

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | 乳癌（依文獻上下文推斷為芳香酶抑制劑用於停經後荷爾蒙受體陽性乳癌；台灣/沙國正式核准適應症文字未取得） |
| Predicted New Indication | Antithrombin Deficiency Type 2 |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

目前尚無正式的作用機轉（MOA）資料來源（DrugBank 查詢缺口，DG002）。根據證據包內文獻脈絡可知，exemestane 屬於不可逆類固醇型芳香酶抑制劑，透過阻斷周邊組織雌激素合成、降低血中雌二醇濃度發揮療效，常見於停經後乳癌之荷爾蒙治療。

Antithrombin Deficiency Type 2 是一種因抗凝血酶（Antithrombin III）基因突變導致的遺傳性凝血因子異常疾病，其病理機轉與雌激素合成路徑之間**沒有已知的生物學關聯**。證據包中的機轉分析明確指出：此高分預測「無臨床或文獻支持」，且推測是 TxGNN 知識圖譜中「乳癌-抗凝治療共病節點」傳遞所造成的**結構性偽相關（spurious correlation）**，而非真實的因果治療關係。

換言之，這是一個純模型分數驅動的預測，沒有任何機轉、臨床或文獻證據支撐，方向性上也缺乏合理性基礎。

---

## Clinical Trial Evidence

目前沒有相關臨床試驗登記。

---

## Literature Evidence

目前沒有相關文獻。

---

## Saudi Arabia Market Information

Exemestane 目前於沙烏地阿拉伯**未上市**，無核准授權紀錄可供列表。

---

## Cytotoxicity

Exemestane 屬於抗腫瘤藥物（芳香酶抑制劑，用於乳癌荷爾蒙治療）。

| Item | Content |
|------|------|
| Cytotoxicity Classification | 標靶／荷爾蒙治療（芳香酶抑制劑），非傳統細胞毒性化療 |
| Myelosuppression Risk | 請參考仿單警語與注意事項 |
| Emetogenicity Classification | 請參考仿單警語與注意事項 |
| Monitoring Items | 請參考仿單警語與注意事項 |
| Handling Protection | 請參考仿單警語與注意事項 |

---

## Safety Considerations

請參考仿單以獲取安全性資訊。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
此預測證據等級為 L5（純模型分數，無臨床試驗、無文獻），且證據包內的機轉分析本身已判定為知識圖譜結構性偽相關，缺乏生物學合理性，不建議進入下一階段評估。

**To proceed, the following is needed:**
- TFDA/沙國仿單警語與禁忌資料（DG001，Blocking，目前無法進行 S1 安全性初評）
- Exemestane 正式作用機轉（MOA）資料（DG002，來源：DrugBank API）
- 若欲追蹤此藥物之老藥新用機會，證據包中排名第 2 之預測適應症 **Amenorrhea**（L4，5 篇文獻支持，decision_stage S1，建議 Research Question）具備較高的證據強度，值得優先於 Antithrombin Deficiency Type 2 進行後續研究規劃
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

