---
layout: default
title: Pefloxacin
parent: 僅模型預測 (L5)
nav_order: 479
evidence_level: L5
indication_count: 10
---

# Pefloxacin
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

# 培氟沙星（Pefloxacin）：從抗菌適應症到心臟傳導疾病（訊號存疑）

## 一句話摘要

Pefloxacin 為 fluoroquinolone 類抗生素，原始適應症資料目前缺失（DrugBank 未提供）。
TxGNN 模型預測其可能對 **Heart Conduction Disease（心臟傳導疾病）** 有效，預測分數高達 **99.90%**，
但**目前無任何臨床試驗或文獻支持**，證據等級僅 **L5**。更關鍵的是，fluoroquinolone 類藥物已知具有 QT 間期延長等心臟傳導相關不良反應的類別效應，此高分很可能是模型將「藥物－不良事件」共現訊號誤判為「藥物－適應症」關聯，而非真正治療潛力。

---

## 總覽表

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料缺失（DrugBank 原始適應症未提供；已知屬 fluoroquinolone 類抗生素） |
| 預測新適應症 | Heart Conduction Disease（心臟傳導疾病） |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L5（純模型預測，無試驗或文獻） |
| 台灣市場狀態 | 未上市 |
| 核准案數量 | 0 |
| 建議決策 | Hold |

---

## 此預測是否合理？

目前作用機轉（MOA）資料缺失，無法建立 pefloxacin 與心臟傳導系統之間的正向治療機轉關聯。

從證據包本身的分析可知，pefloxacin 屬 fluoroquinolone 類抗生素，此藥物類別已有明確記載的類別性不良反應（class effect）——QT 間期延長與心臟傳導異常。TxGNN 的高預測分數，很可能反映的是訓練資料中「藥物與此類不良事件共同出現」的訊號，被模型誤判為治療關聯，而非藥物對該疾病具有正向療效。

換言之，此項預測應被理解為**安全性警訊**，而非老藥新用機會。在缺乏機轉支持、無臨床試驗、無文獻佐證的情況下，不建議將其視為具開發價值的適應症候選。

---

## 臨床試驗證據

目前尚無相關臨床試驗登記

---

## 文獻證據

目前尚無相關文獻資料

---

## 台灣市場資訊

Pefloxacin 目前於台灣**未上市**，無核准案號紀錄（核准案數量：0）。

---

## 安全性考量

請參考仿單所載安全性資訊。

（註：TFDA 仿單警語/禁忌與藥物交互作用資料目前均為缺口，已列為 Blocking 等級資料缺口 DG001，阻礙進入 S1 安全性初評。）

---

## 結論與後續建議

**決策：Hold**

**理由：**
此候選適應症（heart conduction disease）證據等級僅 L5，無任何臨床試驗或文獻支持，且證據包分析指出高分很可能源自「藥物－不良事件」訊號被誤判為療效關聯，而非真正機轉支持。此外，本候選藥物排名 2–10 的其他預測適應症（heart neoplasm、heart valve disease、congenital anomaly of ventricular septum 等）同樣證據等級為 L4–L5、建議均為 Hold，顯示這批預測整體缺乏可操作的臨床證據基礎。

**若要繼續推進，需要補充：**
- TFDA 仿單警語與禁忌資料（DG001，Blocking，阻礙 S1 安全性初評）
- 作用機轉（MOA）資料，以釐清是否存在生物學合理性（DG002）
- 針對 QT 間期延長／心臟傳導不良反應之類別效應，進行獨立文獻查證，排除「不良事件訊號被誤判為適應症」的可能性後，才可重新評估此候選是否值得進一步觀察
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

