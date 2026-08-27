---
layout: default
title: Emedastine
parent: 僅模型預測 (L5)
nav_order: 222
evidence_level: L5
indication_count: 2
---

# Emedastine
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

Using the evidence pack provided, here is the drug repurposing evaluation report for Emedastine's top-ranked predicted indication (allergic urticaria), with the second candidate (cold urticaria) noted separately as a lower-confidence signal.

---

# Emedastine: From Antihistamine Therapy to Allergic Urticaria

## One-Sentence Summary

> Emedastine is a selective H1-histamine receptor antagonist used as an antiallergic agent; formal original-indication and mechanism-of-action records for this market are currently on file as data gaps, but published literature consistently describes its use across allergic rhinitis, allergic conjunctivitis, urticaria, and allergic dermatitis.
> The TxGNN model predicts it may be effective for **Allergic Urticaria**,
> with **0 registered clinical trials** but **4 supporting publications** — including one head-to-head RCT — currently backing this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (drug is not marketed in this jurisdiction; per literature, emedastine is used as an H1-antihistamine for allergic rhinitis, conjunctivitis, urticaria, and dermatitis) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.96% (rank 1,165) |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed, source-verified mechanism-of-action data for emedastine is currently flagged as a data gap in this evidence pack (High severity — DG002). However, the supporting literature itself is informative: a 2009 review (PMID 19558341) describes emedastine difumarate as "a selective histamine-H1 receptor antagonist and effective antiallergic agent" that inhibits clinical symptoms across allergic rhinitis, allergic conjunctivitis, **urticaria**, allergic dermatitis, pruritus cutaneous, and prurigo — with the added note that it produces minimal anticholinergic activity and no adverse cardiovascular effects relative to other antihistamines.

This is mechanistically direct, not a novel hypothesis: H1-receptor antagonism is the established pharmacological basis for treating urticaria, since mast-cell/basophil-released histamine acting on H1 receptors drives the wheal-and-flare (vascular permeability and pruritus) response that defines the condition. Emedastine's known antiallergic activity therefore maps onto allergic urticaria through the same mechanism already used for its other approved allergic indications.

One caveat worth flagging for downstream review: the strongest human evidence (the RCT below) was conducted in **chronic idiopathic urticaria**, not a strictly-defined "allergic urticaria" subtype. The two conditions share substantial pathophysiological overlap (mast-cell/histamine-mediated), but are not clinically identical, so indication naming should be clarified before advancing to formal clinical planning.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17229605](https://pubmed.ncbi.nlm.nih.gov/17229605/) | 2006 | RCT | European Journal of Dermatology | Randomized, double-blind, multicentre trial (n=192) comparing emedastine difumarate (2mg BID) vs. loratadine (10mg QD) in chronic idiopathic urticaria; emedastine produced significantly greater reduction in body skin involvement (57.1% vs. 38.2% reaching 0–10% involvement, p=0.0019) and total urticaria symptom score (83.3% vs. 64.5% reaching score 0–1, p=0.0134) after 4 weeks. |
| [19558341](https://pubmed.ncbi.nlm.nih.gov/19558341/) | 2009 | Review | Expert Opinion on Pharmacotherapy | Reviews emedastine difumarate as a selective H1-antihistamine effective against allergic rhinitis, allergic conjunctivitis, urticaria, allergic dermatitis, and pruritus; highlights greater efficacy vs. other antihistamines, minimal anticholinergic activity, no adverse cardiovascular effects, and a possible additional effect on tissue remodeling in allergic disease. |
| [24720119](https://pubmed.ncbi.nlm.nih.gov/24720119/) | 2013 | Review | Przeglad Lekarski | Polish-language analysis of discrepancies between urticaria treatment guidelines, official drug label indications (SPCs), and the evidence base for antihistamines following 2012 Polish reimbursement policy changes affecting urticaria pharmacotherapy. |
| [14499249](https://pubmed.ncbi.nlm.nih.gov/14499249/) | 2003 | Other (murine model) | Clinical Immunology | Murine contact-sensitivity study primarily evaluating suplatast tosilate's effect on eosinophil recruitment; emedastine difumarate is included only as a comparator antihistamine, so direct relevance to human urticaria efficacy is limited. |

---

## Saudi Arabia Market Information

No marketed products are currently on file for this drug (market status: Not Marketed; 0 authorizations recorded).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Retrieval of the official local package insert (warnings/contraindications) is currently listed as a Blocking data gap (DG001), meaning this candidate cannot yet complete the S1 safety pre-screen. This should be resolved before any clinical advancement.*

---

## Additional Predicted Indication (Lower Priority)

A second TxGNN-predicted indication was identified for the same drug and is noted here for completeness, though it does not currently meet the evidentiary bar for active progression:

| Item | Content |
|------|------|
| Predicted Indication | Cold Urticaria |
| TxGNN Prediction Score | 99.82% (rank 3,649) |
| Evidence Level | L5 (model prediction only) |
| Supporting Trials / Literature | 0 / 0 |
| Recommended Decision | Hold |

Cold urticaria is mechanistically plausible for an H1-antihistamine by analogy with other agents in the same class (e.g., cetirizine, desloratadine) already used clinically for this condition, but there is currently zero drug-specific clinical or literature evidence for emedastine in this indication — it should remain in monitoring only.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- One controlled RCT plus a supportive mechanistic review provide plausible, direct evidence for emedastine in urticaria (L2), but the drug's safety documentation for this market (package insert warnings/contraindications) is a Blocking data gap, and the strongest RCT evidence is in chronic idiopathic urticaria rather than the specific "allergic urticaria" label — both must be resolved before this candidate can move past the current safety pre-screen.

**To proceed, the following is needed:**
- Retrieve the official package insert (warnings, contraindications, DDI) to close the Blocking data gap (DG001) and complete the S1 safety pre-screen
- Obtain verified mechanism-of-action documentation (e.g., via DrugBank API) to close the High-severity MOA data gap (DG002)
- Clarify clinical definition alignment between "chronic idiopathic urticaria" (trial population) and "allergic urticaria" (predicted indication)
- Continue monitoring for emerging trial/literature evidence on the lower-priority cold urticaria candidate before any action is taken there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

