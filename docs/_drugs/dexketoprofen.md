---
layout: default
title: Dexketoprofen
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
---

# Dexketoprofen
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

# Dexketoprofen: From Acute Musculoskeletal Pain to Tendinitis

## One-Sentence Summary

Dexketoprofen is a COX-inhibiting NSAID analgesic used internationally for acute pain and musculoskeletal conditions, though it carries no current Saudi Arabia regulatory approval.
The TxGNN model predicts it may be effective for **Tendinitis**, with **0 clinical trials** and **1 publication** directly supporting this specific direction.
The mechanistic rationale is sound, but indication-specific clinical evidence remains insufficient at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Saudi Arabia authorization; used internationally as an NSAID analgesic for acute pain |
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (mechanism-level; no indication-specific RCT) |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question — indication-specific evidence required) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the dataset. Based on known pharmacological information, dexketoprofen belongs to the NSAID (non-steroidal anti-inflammatory drug) class and acts as a cyclooxygenase (COX) inhibitor. By blocking COX enzymes, it suppresses prostaglandin synthesis, thereby reducing both inflammation and pain — a well-established class effect across musculoskeletal conditions.

Tendinitis is driven by localized prostaglandin-mediated inflammation within the tendon sheath. This is precisely the pathway targeted by COX inhibition, making the TxGNN prediction mechanistically coherent. NSAIDs as a class are widely used as first-line symptomatic treatment for tendinitis in clinical practice, and dexketoprofen's notable bioavailability and rapid onset of action offer a pharmacokinetic advantage within the class.

That said, no dexketoprofen-specific randomized controlled trial has been registered or published for tendinitis as a primary endpoint. The sole supporting publication addresses broad non-traumatic musculoskeletal pain in the emergency department — a category that includes tendinitis but does not study it as an isolated indication. This limits the evidence level to L4, and a "Hold" decision is appropriate until indication-specific data is generated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for dexketoprofen in tendinitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30744914](https://pubmed.ncbi.nlm.nih.gov/30744914/) | 2019 | RCT | The American Journal of Emergency Medicine | IV dexketoprofen vs. IV paracetamol for non-traumatic musculoskeletal pain in the ED (causes ranged from tendinitis to muscle spasm and joint injuries); compared analgesic effectiveness between NSAID and paracetamol in an acute setting |

---

## Saudi Arabia Market Information

Dexketoprofen has no registered authorizations in Saudi Arabia. No product listings, dosage forms, or approved indications are available in the SFDA database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between dexketoprofen's COX-inhibitory action and tendinitis is plausible, but the single supporting publication covers a broad musculoskeletal pain category without tendinitis-specific outcomes — insufficient to meet the L3 threshold needed to advance to a "Proceed" recommendation.

**To proceed, the following is needed:**

- At least one Phase 2 RCT specifically enrolling tendinitis patients, comparing dexketoprofen against placebo or an active NSAID comparator
- MOA data retrieval from DrugBank (DB09214) to complete mechanistic analysis and document COX-1/COX-2 selectivity profile
- Safety data from the package insert (warnings, contraindications) — currently a blocking data gap
- SFDA registration strategy assessment if Saudi Arabia market entry is planned
- Note: Migraine disorder (TxGNN rank #6) and headache disorder (rank #7) carry substantially stronger evidence for dexketoprofen (8 and 12 completed clinical trials respectively, plus meta-analyses) and may represent higher-priority repurposing targets for near-term development decisions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

