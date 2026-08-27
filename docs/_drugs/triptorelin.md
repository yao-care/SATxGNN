---
layout: default
title: Triptorelin
parent: 僅模型預測 (L5)
nav_order: 643
evidence_level: L5
indication_count: 10
---

# Triptorelin
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

Using the given report prompt template directly (no additional skill applies — this is a self-contained content-generation task per explicit spec already provided).

# Triptorelin: From Central Precocious Puberty (Inferred) to Hypertrichosis

## One-Sentence Summary

Triptorelin is a long-acting GnRH agonist; this evidence pack does not record its original approved indication(s), but the pack's own analysis of a lower-ranked prediction (precocious puberty, L1 evidence) strongly suggests central precocious puberty is its actual core, already-approved use — a data gap that should be corrected upstream. The TxGNN model's top-ranked new prediction is **Hypertrichosis (disease)**, but this is currently supported by only **1 incidental case report** and **no clinical trials**, where triptorelin was a background medication rather than the studied intervention.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in source data. The pack's rank-8 analysis (precocious puberty, L1 evidence) indicates this is likely triptorelin's true core indication — flagged as an upstream data gap needing correction, not a confirmed label. |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, triptorelin is a GnRH agonist that, through continuous receptor stimulation, desensitizes pituitary GnRH receptors and suppresses downstream gonadotropin (LH/FSH) and sex-steroid output. This axis-suppression mechanism is the basis for its well-established, heavily trial-supported use in conditions like central precocious puberty (see rank 8 in this same pack).

Hair growth is partly androgen-dependent, so in theory suppressing testosterone via triptorelin could reduce androgen-driven hair growth — the rationale behind ranking hypertrichosis highly. However, the only literature identified (PMID 41822646) is a case report of a transgender woman on testosterone-blocking therapy (including triptorelin) who developed generalised hypertrichosis attributed specifically to **concurrent ciclosporin**, not to triptorelin or androgen suppression. Triptorelin appears only as background/unrelated concomitant medication, and the direction of any real triptorelin effect on hypertrichosis (protective, neutral, or irrelevant) is not established. This is indirect, non-designed evidence and does not constitute mechanistic validation of the prediction.

Separately, note that the original_indications field is empty in the source data — a data gap, not a "no indications" finding. The pack's own rank-8 rationale explicitly flags that precocious puberty is likely triptorelin's existing core indication (supported by 9 clinical trials, several completed Phase 3, and 20 literature items) rather than a true repurposing opportunity, and recommends the upstream data pipeline be corrected accordingly.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41822646](https://pubmed.ncbi.nlm.nih.gov/41822646/) | 2026 | Case report (adverse effect of a different drug) | Cureus | Transgender woman on testosterone-blocking therapy (incl. triptorelin) developed generalised hypertrichosis attributed to concurrent ciclosporin, not to triptorelin or androgen suppression; triptorelin was background medication only, not the studied intervention. |

---

## Saudi Arabia Market Information

No marketing authorizations recorded. Per this evidence pack, triptorelin is not currently marketed in Saudi Arabia (0 authorizations).

---

## Safety Considerations

Key safety data (warnings, contraindications, DDI) are unavailable in this evidence pack. Notably, the TFDA package insert lookup is flagged as a **Blocking**-severity data gap — safety data cannot be resolved by internal query and requires manual retrieval (download and parse the TFDA package insert PDF) before this candidate can enter S1 safety pre-assessment.

Please refer to the package insert for safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rank-1 prediction (hypertrichosis) rests on a single incidental case report in which triptorelin was not the intervention under study, with no supporting clinical trials — evidence level L4 at best, insufficient for progression. A Blocking-severity safety data gap (no TFDA label available) also prevents even an initial safety screen (S1).

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently Blocking; requires manual PDF retrieval and parsing
- Confirmed mechanism of action documentation from DrugBank (currently a data gap)
- Correction of the original_indications field upstream — this pack's own rank-8 evidence (9 trials, 20 publications, L1) strongly suggests central precocious puberty is triptorelin's actual core indication, misrecorded as empty
- Purpose-designed studies evaluating triptorelin specifically for hypertrichosis (none currently exist); the current single case report does not support this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

