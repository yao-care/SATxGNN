---
layout: default
title: Levofloxacin
parent: 僅模型預測 (L5)
nav_order: 373
evidence_level: L5
indication_count: 10
---

# Levofloxacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Levofloxacin：從細菌感染治療到 Punctate Epithelial Keratoconjunctivitis

## 一句話摘要

Levofloxacin 是廣效型第三代 fluoroquinolone 類抗生素，因目前未於沙烏地阿拉伯上市，當地仿單核准適應症資料暫缺。TxGNN 模型預測其可能對 **Punctate Epithelial Keratoconjunctivitis（點狀表層角結膜炎）** 具潛在效益，惟目前**僅有 1 篇相關文獻**支持、**無任何臨床試驗**，且該文獻本身描述的是微孢子蟲群聚感染事件而非療效研究，證據薄弱。

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | 無區域核准適應症紀錄（藥品未於沙烏地阿拉伯上市；一般已知 levofloxacin 屬廣效抗菌藥物，用於呼吸道、泌尿道等細菌感染） |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.92%（rank 1853） |
| Evidence Level | L4 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

目前尚無 levofloxacin 的詳細作用機轉（MOA）資料可供比對。根據已知資訊，levofloxacin 屬於 fluoroquinolone 類廣效抗生素，其抗菌活性已於多種細菌性感染中證實，眼用劑型 fluoroquinolone（含 levofloxacin）在細菌性結膜炎/角膜炎治療上機轉明確、應用成熟。

然而，本項預測所引用的唯一文獻（PMID 30055152）描述的是台灣某游泳池水污染導致的**微孢子蟲（microsporidial）**角結膜炎群聚感染事件，屬於描述性 outbreak/case series 報告，並非療效研究。微孢子蟲為原蟲類病原體，與細菌性病原機轉不同，fluoroquinolone 對微孢子蟲**缺乏已證實的抗蟲活性**。因此，儘管 TxGNN 預測分數極高，此預測的機轉關聯性薄弱，屬於模型統計關聯而非機轉驗證的支持證據。

---

## Clinical Trial Evidence

目前尚無相關臨床試驗登記

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Case Series（描述性 outbreak report） | American Journal of Ophthalmology | 報告台灣某游泳池水污染導致的微孢子蟲角結膜炎群聚感染事件；非療效研究，未評估 levofloxacin 治療效果 |

---

## Safety Considerations

請參考仿單獲取安全性資訊。

（註：TFDA 仿單警語/禁忌資料屬 **Blocking** 級數據缺口，目前無法完成安全性初評（S1）。）

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
唯一支持文獻為描述性群聚感染報告而非療效研究，且 fluoroquinolone 對微孢子蟲缺乏已證實的抗蟲機轉，證據等級僅達 L4；此外藥品目前未於沙烏地阿拉伯上市、仿單安全性資料為 Blocking 級數據缺口，無法進入 S1 安全性初評。

**To proceed, the following is needed:**
- TFDA/當地仿單警語與禁忌資料（Blocking，須優先補齊）
- Levofloxacin 詳細作用機轉（MOA）資料
- Levofloxacin 對微孢子蟲之體外/臨床抗蟲活性證據（現有文獻不足以支持機轉假說）
- 該適應症之前瞻性療效研究或病例對照研究

---

### 附註：本證據包內其他候選適應症（供比較）

此為 multi-indication 證據包，共含 10 個 TxGNN 預測適應症。以下兩項證據強度明顯優於本報告主題，供後續評估參考：

- **Monoclonal gammopathy**（rank 7，L1，S3，Proceed with Guardrails）：TEAMM 多中心雙盲 Phase 3 RCT（PMID 31668592）等 20 篇文獻支持 levofloxacin 用於新診斷多發性骨髓瘤患者之感染預防，惟本質為「感染預防」而非疾病修飾。
- **Septicemic plague**（rank 9，L2，S3，Proceed with Guardrails）：Levofloxacin 已透過 FDA Animal Rule 核准用於鼠疫治療/預防，機轉關聯明確且已有法規背書（16 篇文獻）。

若欲優先推進老藥新用候選，建議評估上述兩項適應症而非本報告之主題適應症。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

