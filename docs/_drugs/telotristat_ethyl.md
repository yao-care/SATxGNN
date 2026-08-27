---
layout: default
title: Telotristat Ethyl
parent: 僅模型預測 (L5)
nav_order: 602
evidence_level: L5
indication_count: 2
---

# Telotristat Ethyl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Telotristat Ethyl: From Carcinoid Syndrome Diarrhea to Cauda Equina Syndrome

*Note: The evidence pack itself does not contain an "original indication" field (empty `original_indications`, MOA marked `[Data Gap]`). The original indication above is based on publicly available drug information (Telotristat ethyl / Xermelo®, a peripheral TPH1 inhibitor used for carcinoid syndrome–associated diarrhea), not on data confirmed within this evidence pack.*

## One-Sentence Summary

Telotristat ethyl is a peripheral tryptophan hydroxylase-1 (TPH1) inhibitor; its confirmed original indication is not documented in this evidence pack. The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags the prediction as likely a knowledge-graph artifact rather than a genuine pharmacological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (data gap); publicly known use is carcinoid syndrome–associated diarrhea |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, telotristat ethyl is a peripheral TPH1 inhibitor that reduces serotonin synthesis in enterochromaffin cells of the gut; its action is largely confined to the periphery, and the drug does not readily cross the blood-brain barrier.

Cauda equina syndrome is a neurosurgical emergency caused by mechanical compression of the lumbosacral nerve roots, with acute neural injury as the core pathology. There is no established causal or therapeutic pathway linking serotonin-synthesis inhibition to nerve root decompression or recovery.

The evidence pack's own repurposing rationale is explicit on this point: the high TxGNN score (0.994) likely reflects noise from serotonin–gut–nerve comorbidity associations embedded in the knowledge graph, rather than a real pharmacological connection. A second, lower-ranked prediction (obsolete neurogenic bladder, score 0.991) has a somewhat more plausible mechanistic thread — central serotonergic pathways do modulate the voiding reflex — but is undermined by the drug's low systemic bioavailability and by the disease term itself being flagged as an obsolete ontology entry, indicating an underlying data-quality issue rather than a genuine signal.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Saudi Arabia Market Information

Not marketed — no product authorizations are on record for this evidence pack (total_licenses = 0).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 (model prediction only) with zero supporting clinical trials or literature, and the evidence pack's own mechanistic review argues the top-ranked signal (cauda equina syndrome) is likely graph noise rather than a real drug-disease relationship. Combined with a blocking data gap on the TFDA/local package insert, this candidate does not meet the bar to advance.

**To proceed, the following is needed:**
- TFDA (or equivalent) package insert / labeling data — currently blocking (DG001)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Confirmation of the drug's actual original indication (not present in this evidence pack)
- Any preclinical or mechanistic study directly linking TPH1/serotonin inhibition to cauda equina syndrome pathology, to move beyond model-only prediction
- Ontology cleanup on the secondary candidate ("obsolete neurogenic bladder") before it can be meaningfully re-evaluated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

