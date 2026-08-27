---
layout: default
title: Vandetanib
parent: 僅模型預測 (L5)
nav_order: 656
evidence_level: L5
indication_count: 10
---

# Vandetanib
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

# Vandetanib: From Medullary Thyroid Cancer to Renal Cell Carcinoma

## One-Sentence Summary

Vandetanib is a multi-kinase inhibitor (RET/VEGFR/EGFR) whose established use, per the literature captured in this evidence pack, is advanced medullary thyroid cancer; it is not currently marketed in Saudi Arabia. The TxGNN model predicts it may be effective for **Renal Cell Carcinoma**, with **4 clinical trials** and **6 publications** currently supporting this direction, though most of the trial evidence is small or terminated early.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Medullary thyroid cancer (established via TKI-class literature in this pack; no Saudi Arabia authorization on record) |
| Predicted New Indication | Renal Cell Carcinoma (disease) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Vandetanib's formal mechanism-of-action record in DrugBank is currently a data gap (DG002). However, the literature returned in this evidence pack itself describes vandetanib as an orally bioavailable multi-kinase inhibitor targeting RET, VEGFR-1/2, and EGFR (PMID 24451769, PMID 30860683). One review states directly that vandetanib, alongside lenvatinib and cabozantinib, belongs to a TKI class "targeting VEGFR subtypes 1 and 2, EGFR and the RET-tyrosine kinase... already been approved for treating patients suffering from thyroid cancer and renal cell carcinoma" (PMID 30860683), and another confirms vandetanib's antiangiogenic activity against VEGF signaling specifically (PMID 26677336).

This VEGFR-driven antiangiogenic mechanism is directly relevant to renal cell carcinoma, since clear cell RCC and related hereditary subtypes (VHL, HLRCC/SDH-deficient, TFE3-associated) are strongly driven by angiogenic signaling — the same target class already exploited by approved RCC therapies such as sunitinib, pazopanib, and axitinib. This mechanistic overlap explains why several early-phase trials have tested vandetanib specifically in VHL-associated renal tumors (NCT00566995) and hereditary RCC subtypes (NCT02495103), even though none of these trials led to a formal RCC indication for vandetanib.

The supporting evidence is real but limited in strength: the one completed, reasonably-sized trial (NCT00566995, n=37) was single-arm in a rare VHL population, while the trial specifically enrolling advanced clear cell RCC (NCT01372813) was terminated after only 3 patients. This keeps the evidence at an early "research question" stage rather than supporting near-term clinical use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | Completed | 37 | Evaluated vandetanib (ZD6474) in Von Hippel-Lindau disease-associated renal tumors, targeting new blood vessel growth and direct tumor cell growth. |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | Terminated | 7 | Vandetanib + metformin combination in HLRCC/SDH-associated or sporadic papillary RCC — populations with no established treatment; ended early. |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | Completed | 82 | Randomized carboplatin/gemcitabine ± vandetanib in cisplatin-ineligible advanced urothelial cancer; population description suggests closer overlap with renal pelvis carcinoma than classic RCC. |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | Terminated | 3 | Vandetanib monotherapy in advanced clear cell RCC to assess tumor shrinkage/stabilization; terminated with only 3 patients enrolled. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Review | Clinical & Experimental Metastasis | Discusses targeted therapy combinations for the rare, aggressive fumarate hydratase-deficient RCC subtype, for which no standard regimen exists. |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Preclinical (mouse model) | Molecular Cancer Research | TFE3 Xp11.2-translocation RCC mouse model identifies novel therapeutic targets relevant to this molecularly distinct RCC subtype. |
| [36302175](https://pubmed.ncbi.nlm.nih.gov/36302175/) | 2023 | RCT (different drug) | Clinical Cancer Research | Phase 2 trial of guadecitabine in SDH-deficient tumors including HLRCC-associated RCC, a population resistant to standard targeted therapies. |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review (different drug) | OncoTargets and Therapy | Reviews antiangiogenic agents including vandetanib that target VEGF signaling pathways across solid tumors. |
| [28477875](https://pubmed.ncbi.nlm.nih.gov/28477875/) | 2017 | Review (different drug) | Bulletin du Cancer | Describes cabozantinib's VEGFR2/c-MET/RET mechanism as a comparator multi-kinase inhibitor relevant to the same drug class as vandetanib. |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Review | ASCO Educational Book | Confirms vandetanib as an orally bioavailable RET kinase inhibitor, FDA-approved in the systemic treatment of medullary thyroid cancer. |

---

## Saudi Arabia Market Information

Currently no market authorization records — vandetanib has 0 registered licenses and is not marketed in Saudi Arabia based on available regulatory data.

---

## Cytotoxicity

Vandetanib is antineoplastic (approved use in medullary thyroid cancer; multi-kinase inhibitor class per literature evidence above), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: RET / VEGFR-1,2 / EGFR) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The VEGFR-driven mechanism plausibly extends to RCC and is backed by one completed Phase 2 trial in a defined population (VHL-associated renal tumors, n=37), but the RCC-specific trial (NCT01372813) was terminated at n=3, and a Blocking-severity safety data gap (DG001, missing TFDA label/warnings) currently prevents a proper S1 safety review.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications data (DG001, Blocking — required before any S1 safety assessment)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- Larger, ideally randomized trial data in RCC, prioritizing the hereditary subtypes (VHL, HLRCC/SDH-associated) where the strongest signal exists
- A defined regulatory pathway for Saudi Arabia market entry, since vandetanib currently has zero local authorizations
- A safety monitoring plan for known TKI-class risks (e.g., QT prolongation, hepatic and renal function) given the absence of drug-specific safety data in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

