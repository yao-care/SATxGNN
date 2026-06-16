---
layout: default
title: Bupivacaine
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 4
---

# Bupivacaine
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

# Bupivacaine: From Local Anesthesia to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Bupivacaine is a long-acting amide-type local anesthetic, widely used for regional nerve blocks, epidural anesthesia, and surgical pain management via sodium channel blockade.
The TxGNN model predicts it may be effective for **Acrodermatitis Chronica Atrophicans** — a late-stage Lyme disease–associated chronic skin atrophy —
however, this prediction is currently supported by **0 clinical trials** and **0 publications**, representing the weakest possible evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Local/regional anesthesia and perioperative pain management |
| Predicted New Indication | Acrodermatitis Chronica Atrophicans |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Registered |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on well-established pharmacological knowledge, bupivacaine is a voltage-gated sodium channel (Nav) blocker belonging to the amide class of local anesthetics. By preventing Na⁺ influx, it interrupts action potential propagation in sensory and motor nerves, producing reversible local anesthesia. Secondary to this primary mechanism, in vitro studies have documented weak anti-inflammatory activity — including inhibition of NF-κB signalling and suppression of pro-inflammatory cytokines such as IL-6 — though these effects occur at concentrations far exceeding clinically relevant levels.

Acrodermatitis chronica atrophicans (ACA) is a dermatological manifestation of late disseminated *Borrelia burgdorferi* infection (Lyme disease), characterised by progressive skin atrophy and chronic low-grade inflammation. The hypothesised mechanistic link relies on bupivacaine's incidental anti-inflammatory properties reducing local cutaneous inflammation — not on any antibacterial or spirochaetal activity. This indirect chain (Na⁺ channel blockade → anti-inflammatory → Borrelia-driven skin atrophy) is pharmacologically tenuous at best.

The repurposing rationale documented in the Evidence Pack itself flags a high likelihood of **knowledge graph artefact**: TxGNN's high prediction score may stem from co-occurrence bias between "skin inflammation" nodes in the training graph rather than a genuine drug–disease pharmacological signal. With zero supporting clinical or preclinical evidence in the direct indication space, this prediction should be treated as a hypothesis-generating signal only, not a viable repurposing candidate at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Bupivacaine is **not currently registered with the Taiwan Food and Drug Administration (TFDA)**. No marketing authorizations or approved products were found in the regulatory database query conducted on 2026-03-29.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** TFDA package insert data and formal contraindication/warning records were not retrievable from the data pipeline at the time of this report (Data Gap: DG001). Before any preclinical or clinical investigation proceeds, a full safety profile review from the originator label (e.g., Marcaine®/AstraZeneca) and TFDA database must be completed. Key known class-level concerns include cardiac toxicity (QRS widening, ventricular arrhythmia) and **direct myotoxicity** — the latter is particularly relevant given the dermatomyositis-spectrum predictions in ranks 2 and 4.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predicted indications carry L5 evidence (model prediction only, no supporting clinical trials or literature), and the mechanistic link between bupivacaine's sodium channel blockade and Borrelia-driven chronic skin atrophy is indirect and unvalidated. Additionally, the simultaneous appearance of two dermatomyositis-spectrum predictions at high scores raises a credible concern that TxGNN's output reflects graph topology clustering artefacts rather than true pharmacological signals.

**To proceed, the following is needed:**

- **Complete safety data retrieval:** Download and parse the TFDA package insert PDF for bupivacaine to populate contraindications, boxed warnings, and drug interaction profiles (DG001 — Blocking severity)
- **MOA confirmation:** Retrieve full DrugBank MOA entry to formally document sodium channel subtype selectivity and anti-inflammatory evidence thresholds (DG002 — High severity)
- **Knowledge graph audit:** Evaluate whether TxGNN's high scores for all four indications reflect true pharmacological signal or systematic over-scoring of "skin/connective tissue inflammation" node clusters
- **Preclinical literature sweep:** Conduct a broader PubMed search using MeSH terms for "bupivacaine + anti-inflammatory" and "local anesthetic + dermatitis" to identify any foundational mechanistic evidence before considering in vitro work
- **Route compatibility assessment:** Even if mechanistic plausibility were established, an appropriate delivery route for a chronic skin condition (topical formulation? intradermal depot?) would need to be defined, as systemic bupivacaine carries unacceptable cardiac risk for non-surgical indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

