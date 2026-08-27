---
layout: default
title: Perampanel
parent: 中證據等級 (L3-L4)
nav_order: 489
evidence_level: L4
indication_count: 10
---

# Perampanel
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Perampanel: From Focal Epilepsy to Visual Epilepsy

## 一句話摘要

> Perampanel 目前尚未在沙烏地阿拉伯上市，其官方原始適應症資料（TFDA 仿單、MOA 結構化欄位）為資料缺口，但根據本證據包內大量文獻可確認其為選擇性 AMPA 受體拮抗劑，已在其他國家核准用於局部性（partial-onset）癲癇。
> TxGNN 模型將其預測擴及多種反射性癲癇亞型，排名第一的是 **Visual Epilepsy（視覺誘發性癲癇）**，預測分數 **99.92%**，目前有 **3 篇臨床試驗**與 **19 篇文獻**支持此方向，但均非該亞型專屬設計。
> 本證據包同時列出另外 9 個候選適應症（見文末總覽表），其中 **Status Epilepticus（癲癇重積狀態）** 證據強度最高（L3，已有專屬 Phase 2 試驗招募中）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 局部性（partial-onset）癲癇，含續發性全身性發作之輔助治療 — 依文獻確認（非沙烏地監管資料，該藥物目前未在當地上市） |
| 預測新適應症 | Visual Epilepsy（視覺誘發性癲癇） |
| TxGNN 預測分數 | 99.92%（rank 1794） |
| 證據等級 | L4 |
| 沙烏地阿拉伯市場狀態 | 未上市 |
| 授權數量 | 0 |
| 建議決策 | Research Question（研究待啟階段，尚不足以進入 Go/Hold 二選一判斷） |

---

## 為何此預測合理？

本證據包的 `original_moa` 結構化欄位標記為資料缺口，DrugBank API 尚待補齊。但根據本包內多篇文獻的一致描述（如 PMID 21635236、24559052、29953584），perampanel 是一種**選擇性、非競爭性 AMPA（α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid）受體拮抗劑**，透過阻斷麩胺酸（glutamate）介導的突觸後興奮性傳導發揮廣效型抗癲癇作用，已在超過 35 個國家核准作為局部性癲癇（partial-onset seizures）及原發性全身強直陣攣發作（PGTC seizures）之輔助治療。

視覺誘發性癲癇（visual/photosensitive reflex epilepsy）的病理機轉涉及枕葉皮質對視覺刺激的過度興奮反應，同樣以 AMPA 受體介導的快速興奮性傳導為核心路徑。因此廣效型 AMPA 拮抗劑理論上可抑制此類反射性發作，此為 TxGNN 預測的機轉基礎。

然而，目前所有相關臨床試驗（3 篇）皆為一般癲癇族群或 PK/耐受性/認知功能研究，並未鎖定視覺誘發亞型患者；文獻證據同樣以廣泛性癲癇治療為主，尚無專屬視覺誘發性癲癇的介入性研究直接驗證此適應症。

---

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03780907](https://clinicaltrials.gov/study/NCT03780907) | Phase 2 | Completed | 18 | 評估 perampanel（E2007）於局部性與全身性難治性癲癇患者之耐受性、安全性與藥動學，非視覺誘發亞型專屬 |
| [NCT02900755](https://clinicaltrials.gov/study/NCT02900755) | Phase 4 | Completed | 30 | 評估 perampanel 對癲癇患者認知功能與 EEG 之影響，一般癲癇族群 |
| [NCT03653741](https://clinicaltrials.gov/study/NCT03653741) | Phase 4 | Completed | 12 | 評估 perampanel 對神經生理學檢測（EEG、SEP、BAEP、VEP）參數之影響，含視覺誘發電位但非治療效果試驗 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Guideline | Neurology | AAN/AES 更新新發癲癇之第二/三代 AED 治療指引 |
| [36150304](https://pubmed.ncbi.nlm.nih.gov/36150304/) | 2022 | Review (real-world) | Epilepsy & Behavior | Perampanel 單藥治療之臨床試驗與真實世界證據回顧 |
| [36206645](https://pubmed.ncbi.nlm.nih.gov/36206645/) | 2022 | Systematic Review/Meta-analysis | Seizure | Perampanel 治療癲癇之隨機對照試驗系統性回顧與統合分析 |
| [37684052](https://pubmed.ncbi.nlm.nih.gov/37684052/) | 2023 | Review | BMJ | 妊娠與哺乳期癲癇管理，含抗癲癇藥物安全性概述 |
| [36218253](https://pubmed.ncbi.nlm.nih.gov/36218253/) | 2022 | Review | Revista de neurologia | 兒童癲癇重積狀態之處置回顧 |
| [24559052](https://pubmed.ncbi.nlm.nih.gov/24559052/) | 2014 | Review | Expert Opinion on Drug Discovery | Perampanel 的發現與開發歷程回顧 |
| [37329172](https://pubmed.ncbi.nlm.nih.gov/37329172/) | 2023 | Cohort | Annals of Clinical and Translational Neurology | Perampanel 於已知/疑似基因型病因之兒童癲癇療效 |
| [37292124](https://pubmed.ncbi.nlm.nih.gov/37292124/) | 2023 | Cohort | Frontiers in Neurology | Perampanel 單藥治療新診斷局部性癲癇兒童之療效與耐受性 |
| [36034267](https://pubmed.ncbi.nlm.nih.gov/36034267/) | 2022 | Observational | Frontiers in Neurology | Perampanel 治療兒童失神性癲癇之真實世界經驗 |
| [37775491](https://pubmed.ncbi.nlm.nih.gov/37775491/) | 2023 | Observational | The Medical Journal of Malaysia | Perampanel 輔助治療癲癇患者之療效與安全性 |

---

## 沙烏地阿拉伯市場資訊

Perampanel 目前**未在沙烏地阿拉伯上市**，查無任何有效藥證授權（0 筆），故無產品名稱、劑型或核准適應症資料可列表。

---

## 安全性考量

請參考藥品仿單以取得安全性資訊。

*（TFDA 仿單警語/禁忌屬 Blocking 級資料缺口，DDI 查詢亦無結果，需先補齊方能進行 S1 安全性初評。）*

---

## 結論與下一步

**決策：Research Question（研究待啟階段）**

**理由：**
視覺誘發性癲癇的 AMPA 受體機轉合理性存在，但現有 3 篇臨床試驗與 19 篇文獻皆非該亞型專屬設計，證據等級僅達 L4，尚不足以支持 Go 或明確 Hold 之二元決策，應先以研究問題形式推進。

**若要繼續推進，需要補齊：**
- TFDA/SFDA 官方仿單之警語與禁忌資料（Blocking 級缺口）
- DrugBank MOA 結構化資料（High 級缺口）
- 針對視覺誘發性癲癇亞型的專屬前瞻性研究設計
- 藥物交互作用（DDI）資料庫查詢結果

---

## 附錄：本證據包其他候選適應症總覽

本證據包（TW-DB08883-multi）共列出 10 個 TxGNN 預測適應症，以下為排名第 2–10 名之總覽：

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 | 備註 |
|------|------|------|------|------|------|------|
| 2 | Startle epilepsy | 99.86% | L5 | S0 | Hold | 僅 1 篇弱相關文獻（基因關聯研究），無直接機轉或療效證據 |
| 3 | Thinking seizures | 99.86% | L4 | S1 | Research Question | 機轉推論與視覺/閱讀誘發癲癇相近，尚無專屬試驗 |
| 4 | Micturition-induced seizures | 99.86% | pending | pending | pending | 評分未完成 |
| 5 | Orgasm-induced seizures | 99.86% | L5 | S0 | Hold | 無任何試驗或文獻支持，判定為模型雜訊 |
| 6 | Audiogenic seizures | 99.86% | L4 | S1 | Research Question | 動物模型（DBA/2 小鼠）前臨床證據明確，缺人體試驗 |
| 7 | Eating seizures | 99.86% | L4 | S0 | Hold | 現有文獻方向相反（perampanel 誘發食慾減退之不良反應） |
| 8 | Reading seizures | 99.83% | L4 | S1 | Research Question | 典型反射性癲癇亞型，機轉合理但無專屬試驗 |
| 9 | Beta-ketothiolase deficiency | 99.79% | L5 | S0 | Hold | 代謝疾病，與 AMPA/癲癇路徑無直接機轉關聯，判定為雜訊 |
| **10** | **Status epilepticus** | **99.77%** | **L3** | **S2** | **Proceed with Guardrails** | **證據最強：已有專屬 Phase 2 試驗（NCT06401707，心跳停止後重積狀態預防）招募中，加上多篇系統性回顧與世代研究支持** |

**特別提示：** 排名第 10 的 Status Epilepticus 雖 TxGNN 分數略低，但實證強度（L3、S2、Proceed with Guardrails）明顯優於排名第一的 Visual Epilepsy，建議後續資源投入優先評估此候選適應症。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

