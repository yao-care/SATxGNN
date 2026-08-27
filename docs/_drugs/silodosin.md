---
layout: default
title: Silodosin
parent: 僅模型預測 (L5)
nav_order: 573
evidence_level: L5
indication_count: 6
---

# Silodosin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Silodosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Silodosin is a selective α1A-adrenergic receptor antagonist used clinically for benign prostatic hyperplasia (BPH); this specific detail is general clinical knowledge and is **not** contained in the evidence pack (`original_indications` and `original_moa` are both empty/Data Gap here). The TxGNN model's top prediction is **Ambras type hypertrichosis universalis congenita** (score 99.99%), but this is supported by **zero clinical trials and zero literature**, and the evidence pack's own mechanistic-rationale field explicitly flags the score as likely knowledge-graph noise from a sparsely-connected rare-disease node rather than a real biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign Prostatic Hyperplasia (general clinical knowledge — not present in evidence pack) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (`original_moa: "[Data Gap]"`). Based on well-established public pharmacology, silodosin is a uroselective α1A-adrenoceptor antagonist that relaxes smooth muscle in the bladder neck/prostate to relieve BPH symptoms.

For the top-ranked prediction, however, the pack's own `repurposing_rationale` concludes there is **no plausible mechanistic link**: Ambras syndrome is a rare autosomal-dominant condition tied to 8q22 chromosomal rearrangements and hair-follicle growth-cycle regulatory genes, with no known intersection with α1A-adrenoceptor blockade. The rationale explicitly states the high TxGNN score is likely an artifact of sparse graph connectivity around this rare-disease node rather than a genuine biological signal.

The same pattern repeats across all six predicted indications in this pack — hypertrichosis, a periodontal/odontal malformation syndrome (whose 20 literature hits are all general periodontitis background papers with no mention of silodosin or α1-blockers), Dandy-Walker malformation, hair-shaft abnormality, and familial trichomegaly — every one is scored L5 (model prediction only) with a "Hold" recommendation and an explicit statement of no mechanistic plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: rank-3 candidate, "malformation syndrome with odontal and/or periodontal component," returned 20 PubMed hits, but all are general periodontitis pathophysiology/treatment-guideline papers unrelated to silodosin — they do not constitute drug-disease evidence and are therefore not listed here.)*

---

## Saudi Arabia Market Information

Silodosin is not marketed in Saudi Arabia (`total_licenses = 0`, no license records available).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every predicted indication in this pack is L5 (model score only), with no clinical trials, no drug-relevant literature, and no plausible mechanistic link — the evidence pack itself assesses the top signal as likely knowledge-graph noise rather than a real biological effect. Silodosin is also unmarketed in Saudi Arabia, and a **Blocking** data gap (TFDA package insert / warnings & contraindications) prevents even entering the S1 safety pre-assessment stage.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently Blocking (DG001)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- Confirmed original indication/label text (currently absent from this evidence pack)
- A rerun of literature/trial searches specifically pairing "silodosin" with each candidate disease term, since existing hits are background disease literature rather than drug-linked evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

