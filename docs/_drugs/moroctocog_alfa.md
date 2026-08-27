---
layout: default
title: Moroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 428
evidence_level: L5
indication_count: 8
---

# Moroctocog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Moroctocog Alfa: From Hemophilia A (Factor VIII Deficiency) to Primary Release Disorder of Platelets

## One-Sentence Summary

Moroctocog alfa is a recombinant Factor VIII (BDD-rFVIII) replacement product, whose established mechanism corrects congenital Factor VIII deficiency (Hemophilia A). The TxGNN model's top-ranked prediction is **Primary Release Disorder of Platelets**, but the 7 supporting clinical trials are all graded "C" (low relevance) — they involve different drugs, different diseases, or unrelated coagulation topics — so **no genuine trial or literature evidence currently supports this specific indication.**

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Congenital Factor VIII deficiency (Hemophilia A) — inferred from repurposing rationale text; no formal Saudi Arabia license record exists (drug not marketed) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap: MOA). Based on the evidence pack's own repurposing rationale, moroctocog alfa is a B-domain-deleted recombinant Factor VIII, used to replace deficient Factor VIII in coagulation-factor–deficiency bleeding disorders such as Hemophilia A.

Primary release disorder of platelets, however, is caused by defective platelet granule secretion, not by a Factor VIII deficiency. The evidence pack's own rationale states that FVIII replacement therapy has **no corrective mechanism** for this condition. This is corroborated by the trial evidence: all 7 retrieved trials are graded "C" (low relevance) — most involve entirely different products (PEGylated rFVIII/BAX855, rFVIIIFc-VWF-XTEN/BIVV001) studied in Hemophilia A, not platelet release disorder, while others (artificial liver support, TIPS hemostasis, post-COVID vaccination syndrome, AML coagulation profiling) are unrelated coagulation-adjacent studies that appear to have been pulled in by disease-label matching rather than genuine relevance.

**Note:** Among the 8 TxGNN-predicted indications in this evidence pack, rank 4 ("acquired coagulation factor deficiency") shows a mechanistically more plausible link (congenital→acquired FVIII deficiency) and reached decision stage S1 ("Research Question") with L3 evidence, though the specific trials retrieved there were also confirmed to involve different FVIII products (Obizur/susoctocog alfa, TAK-672), not moroctocog alfa itself.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Phase 3 | Completed | 159 | BIVV001 (rFVIIIFc-VWF-XTEN) prophylaxis trial in severe Hemophilia A ≥12y — different drug and indication; disease-label mismatch |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Phase 3 | Completed | 30 | BAX 855 (PEGylated rFVIII) in severe Hemophilia A patients undergoing surgery — different drug and indication |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Phase 3 | Completed | 74 | BIVV001 safety trial in pediatric severe Hemophilia A <12y — different drug and indication |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/A | Recruiting | 25 | Artificial liver support system in acute-on-chronic liver failure, effect on coagulation — not specific to platelet release disorder |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/A | Recruiting | 45 | Systemic/portal hemostasis during TIPS placement — not specific to platelet release disorder |
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/A | Recruiting | 200 | Coagulation evaluation in Post-COVID-19-Vaccination Syndrome — unrelated |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/A | Not yet recruiting | 80 | Coagulation profile in newly diagnosed AML under induction chemotherapy — unrelated |

All 7 trials are graded "C" (low relevance) in the source data — none directly test moroctocog alfa in this indication.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Moroctocog alfa is not currently marketed in Saudi Arabia; no marketing authorizations are on record (total licenses: 0).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between Factor VIII replacement and a platelet granule-secretion defect is not supported, and every retrieved trial is graded low-relevance (wrong drug, wrong disease, or an unrelated coagulation topic). Combined with the drug's unmarketed status in Saudi Arabia and blocking data gaps on labeling and MOA, there is currently no basis to advance this indication.

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings, contraindications) — currently a Blocking data gap
- Verified mechanism of action data from DrugBank — currently a High-severity data gap
- A corrected disease-ontology query to rule out label mismatch, followed by a fresh trial/literature search specific to platelet release disorders
- If pursuing repurposing further, re-evaluate rank 4 ("acquired coagulation factor deficiency") instead, which shows stronger mechanistic plausibility and reached decision stage S1 in this same evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

