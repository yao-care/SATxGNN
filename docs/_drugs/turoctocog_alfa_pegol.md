---
layout: default
title: Turoctocog Alfa Pegol
parent: 僅模型預測 (L5)
nav_order: 648
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa Pegol
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

# Turoctocog Alfa Pegol：從 A 型血友病到原發性血小板釋放障礙（Primary Release Disorder of Platelets）

## 一句話摘要

Turoctocog alfa pegol 為聚乙二醇化重組人類 Factor VIII 替代藥物，原始用途為 A 型血友病（先天性 FVIII 缺乏症）之出血預防與治療。TxGNN 模型預測其可能對 **原發性血小板釋放障礙** 有效（電腦運算分數 **99.9966%**），但目前 **無任何臨床試驗** 與 **無任何文獻** 支持此方向，且模型自身的機轉評估亦指出該關聯性薄弱。

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | A 型血友病（先天性 Factor VIII 缺乏症）※見下方說明 |
| Predicted New Indication | Primary release disorder of platelets（原發性血小板釋放障礙） |
| TxGNN Prediction Score | 99.9966%（全域排名 130） |
| Evidence Level | L5（僅模型預測，無臨床試驗或文獻） |
| Saudi Arabia Market Status | ✗ 未上市 |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

※ 來源資料中 `original_indications` 與 `taiwan_regulatory.licenses` 均為空值，無法從結構化欄位直接萃取原始適應症。上表原始適應症係依 Evidence Pack 內 `repurposing_rationale` 反覆提及之「FVIII 替代品」「凝血瀑布中 FVIII 角色」「acquired hemophilia A」等機轉描述，回推其藥物類別（重組 FVIII）之已知公開藥理分類所得，非正式法規登記資料。

---

## 為什麼這個預測合理？

目前尚無詳細作用機轉（MOA）資料可用（DrugBank 查詢結果為資料缺口，優先級 High）。根據 Evidence Pack 中各候選適應症之機轉描述可推知，turoctocog alfa pegol 屬於 PEGylated 重組 Factor VIII 替代品，其藥理作用為補充內源性凝血路徑中的 FVIII，作為 FIXa 之輔因子加速 FXa 生成，用於矯正 FVIII 濃度或活性不足所致之出血傾向。

然而，本報告主要標的「原發性血小板釋放障礙」屬於血小板顆粒釋放機制異常，病因在血小板本身的訊息傳導與顆粒分泌，並非凝血因子濃度或活性問題。Evidence Pack 自身的 `repurposing_rationale` 明確指出：「與凝血瀑布中 FVIII 角色（活化 FIXa 輔因子）無直接機轉重疊，補充 FVIII 無法矯正血小板釋放缺陷」。也就是說，儘管 TxGNN 運算分數極高，此排名很可能來自知識圖譜中的間接共現關係（如同屬「出血傾向」節點群），而非具因果基礎的生物學機轉，這也是該候選被評為 L5／Hold 的主因。

值得留意的是，Evidence Pack 中排名第 4 的候選適應症「acquired coagulation factor deficiency（後天性凝血因子缺乏）」機轉合理性明顯較強——FVIII 替代品理論上可直接補充後天性 FVIII 缺乏，唯臨床上此類病人常合併抑制物，實務多改用 rFVIIa/aPCC，故該候選被列為 S1「Research Question」而非直接進入安全性評估。若要在本藥物的十個預測適應症中挑選機轉最站得住腳的方向，建議優先關注此候選而非本報告標的排名第一者。

---

## Clinical Trial Evidence

目前無相關臨床試驗登記

---

## Literature Evidence

目前無相關文獻

---

## 沙烏地阿拉伯市場資訊

本藥物目前**未於沙烏地阿拉伯上市**，`taiwan_regulatory.licenses` 無任何授權紀錄（總授權數：0），無可列示之產品資訊。

---

## 安全性考量

安全性相關欄位（`key_warnings`、`contraindications`、DDI 查詢）均為資料缺口或查無結果，其中「TFDA 仿單警語/禁忌」已被標記為 **Blocking** 等級缺口，直接阻擋進入 S1 安全性初評階段。

請參閱藥品仿單以獲取安全性資訊。

---

## 結論與下一步

**決策：Hold**

**理由：**
本候選適應症（原發性血小板釋放障礙）僅有 TxGNN 電腦運算分數支持，無任何臨床試驗或文獻佐證（L5），且模型自身機轉分析已指出生物學關聯性薄弱；同時安全性資料存在 Blocking 等級缺口（TFDA 仿單警語/禁忌未取得），藥物也尚未於沙烏地阿拉伯上市，現階段不具備推進條件。

**若要推進，需要補齊：**
- TFDA／原廠仿單警語與禁忌資料（Blocking，DG001）
- DrugBank 作用機轉（MOA）詳細資料（High，DG002）
- 針對「原發性血小板釋放障礙」之機轉關聯性重新評估，或改列為低優先觀察項目
- 若仍欲推進此藥物之老藥新用，建議轉向機轉合理性較強的候選適應症（如排名第 4「後天性凝血因子缺乏」）並補充其臨床實證
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

