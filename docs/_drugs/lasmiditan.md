---
layout: default
title: Lasmiditan
parent: 僅模型預測 (L5)
nav_order: 363
evidence_level: L5
indication_count: 3
---

# Lasmiditan
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

# Lasmiditan：從偏頭痛急性治療到腦幹型先兆偏頭痛

## 一句話摘要

> Lasmiditan（DB11732）為選擇性 5-HT1F 受體致效劑，原用於偏頭痛急性治療（此為外部藥理學已知資訊，本資料集內 `original_indications` 為空、屬待補資料）。
> TxGNN 模型預測其可能對 **Migraine with Brainstem Aura（腦幹型先兆偏頭痛）** 有效，
> 惟本資料集中該適應症目前**無臨床試驗、無文獻**佐證，僅有機轉推論支持。

---

## 總覽表

| 項目 | 內容 |
|------|------|
| 原始適應症 | 偏頭痛急性治療（外部藥理學知識；本資料集無沙烏地阿拉伯核准適應症資料） |
| 預測新適應症 | Migraine with Brainstem Aura |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L4（機轉推論，無臨床試驗/文獻佐證） |
| 沙烏地阿拉伯市場狀態 | 未上市 |
| 核准許可證數量 | 0 |
| 建議決策 | Hold |

---

## 為何此預測具合理性？

目前無法取得完整的作用機轉（MOA）資料，本資料集中 `original_moa` 標示為待補資料。根據已知的外部藥理學資訊，Lasmiditan 為選擇性 5-HT1F 受體致效劑，與 triptan 類藥物（5-HT1B/1D 致效劑）不同，其不具明顯血管收縮作用，機轉聚焦於抑制三叉神經血管系統活化與 CGRP 釋放調控。

Migraine with Brainstem Aura（舊稱 basilar-type migraine）在臨床上因涉及腦幹／後循環血流特徵，過去 triptan 類藥物因血管收縮疑慮常被列為相對禁忌。5-HT1F 致效劑不具血管收縮效應，機轉上可能較適合此亞型病人，這是 TxGNN 給出高分預測的合理生物學基礎。

然而，此推論目前**僅止於機轉層次**——本資料集查詢結果顯示，clinicaltrials.gov、ICTRP、PubMed 針對「Lasmiditan + migraine with brainstem aura」皆為 0 筆結果，尚無直接臨床證據支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

目前無相關文獻資料

---

## 沙烏地阿拉伯市場資訊

Lasmiditan 目前在沙烏地阿拉伯**未上市**，無核准許可證資料（`total_licenses = 0`）。

---

## 安全性考量

請參閱藥品仿單以獲取安全性資訊。

（本資料集中之關鍵警語、禁忌症及藥物交互作用查詢結果均為待補資料，TFDA 仿單解析為 Blocking 等級缺口，尚未完成 S1 安全性初評所需資料蒐集。）

---

## 結論與後續步驟

**決策：Hold**

**理由：**
本適應症的證據等級僅為 L4（機轉推論），無任何臨床試驗或文獻直接支持，且藥品在沙烏地阿拉伯尚未上市、仿單安全性資料為 Blocking 等級缺口，尚不足以進入 S1 安全性初評，故暫不建議推進。

**後續需補充：**
- TFDA／原廠仿單警語與禁忌症資料（DG001，Blocking，阻擋 S1 安全性初評）
- 完整作用機轉（MOA）資料，供機轉關聯性分析（DG002，High）
- 針對 migraine with brainstem aura 的直接臨床試驗或文獻證據（目前為 0 筆）
- 若無法取得直接證據，建議改以既有偏頭痛適應症之臨床數據作間接佐證來源
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

