---
layout: default
title: Raloxifene
parent: 僅模型預測 (L5)
nav_order: 532
evidence_level: L5
indication_count: 4
---

# Raloxifene
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

# Raloxifene：原始適應症資料缺失 → Duodenal Ulcer（十二指腸潰瘍，模型預測）

## 一句話摘要

本證據包中 Raloxifene（DrugBank DB00481）的**原始核准適應症與作用機轉皆為資料缺口**，僅知其為既有上市藥品。TxGNN 模型預測其對 **Duodenal Ulcer（十二指腸潰瘍）** 可能有效，預測分數 99.72%，但**目前無任何臨床試驗或文獻佐證**，屬純模型預測（L5），證據包本身亦註記此機轉關聯「未見確立文獻支持」。

## 概覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料未提供（`original_indications` 為空、台灣核准許可證亦為 0 筆） |
| 預測新適應症 | Duodenal ulcer（十二指腸潰瘍） |
| TxGNN 預測分數 | 99.72%（模型排名第 5094 位） |
| 證據等級 | L5（僅模型預測，無臨床試驗、無文獻） |
| 台灣市場狀態 | 未上市 |
| 核准許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前尚無詳細作用機轉（MOA）資料，也沒有原始適應症紀錄可供比對——這兩項均列為證據包的資料缺口（DG002 為 High 等級缺口）。因此無法依照標準流程分析原始適應症與新適應症之間的機轉連結。

證據包對此候選項目的機轉評述為：「SERM 對胃十二指腸黏膜保護的機轉未見確立文獻支持；雌激素路徑與潰瘍修復雖有零星理論，但無資料佐證此連結，且無任何試驗或文獻紀錄。」換言之，即使是排名第一的預測，其機轉合理性本身也相當薄弱。

值得注意的是，證據包內部對第 2 名候選項目（hypoalphalipoproteinemia，低α脂蛋白血症）的機轉評述反而較正面：「Raloxifene 為 SERM，臨床已知對脂質代謝有輕度影響……此適應症在藥理機轉上具備一定合理性，優於其他三項。」但同樣缺乏原始 MOA 資料與任何試驗/文獻佐證。第 3 名候選項目（duodenal obstruction）證據包更直接註記「高度疑似 TxGNN 預測偽陽性」。

### 本輪四項預測候選一覽

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 | 備註 |
|------|-----------|-----------|---------|------|------|
| 1 | Duodenal ulcer | 99.72% | L5 | Hold | 機轉未見確立文獻支持 |
| 2 | Hypoalphalipoproteinemia | 99.65% | L5 | Hold | 機轉相對合理，仍無試驗/文獻佐證 |
| 3 | Duodenal obstruction | 99.64% | L5 | Hold | 結構性病變，疑似模型偽陽性 |
| 4 | Duodenogastric reflux | 99.59% | L5 | Hold | 機轉關聯薄弱 |

## 臨床試驗證據

目前無相關已註冊臨床試驗（ClinicalTrials.gov 與 ICTRP 查詢均為 0 筆，查詢日期 2026-04-21）。

## 文獻證據

目前無相關文獻（PubMed 查詢為 0 筆，查詢日期 2026-04-21）。

## 台灣市場資訊

Raloxifene 目前**未在台灣上市**，無核准許可證資料（`total_licenses` = 0）。

## 安全性考量

請參考仿單所載安全性資訊。

補充說明：TFDA 仿單警語/禁忌資料為**阻斷性（Blocking）資料缺口**（DG001），目前無法進入 S1 安全性初評；DDI 查詢亦無結果（`not_found`）。此缺口須優先補齊才能進行後續安全性評估。

## 結論與後續步驟

**決策：Hold**

**理由：**
四項預測候選皆為 L5（純模型預測），無任何臨床試驗或文獻佐證；且安全性初評所需的 TFDA 仿單資料為阻斷性缺口，尚無法進行 S1 安全性評估。證據包本身也對第 1、3 名候選的機轉合理性提出保留。

**若要推進，需要補齊：**
- TFDA 仿單警語/禁忌資料（DG001，阻斷性，需下載並解析原廠仿單 PDF）
- 作用機轉（MOA）資料（DG002，查詢 DrugBank API）
- 原始核准適應症資料（目前完全空缺，無法建立原始–新適應症的比對基礎）
- 針對排名第 2（hypoalphalipoproteinemia）候選項目優先執行文獻與臨床試驗檢索，其機轉合理性在證據包內部評述中相對較高
- 排名第 3（duodenal obstruction）建議進一步確認是否為模型偽陽性，必要時自候選清單中排除
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

