---
layout: default
title: Ticagrelor
parent: 僅模型預測 (L5)
nav_order: 619
evidence_level: L5
indication_count: 10
---

# Ticagrelor
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

# Ticagrelor: From Acute Coronary Syndrome (Antiplatelet Therapy) to Intracranial Arteriosclerosis

## One-Sentence Summary

Ticagrelor is a P2Y12 receptor antagonist whose established clinical role, per the evidence pack's own mechanistic notes, is antiplatelet therapy for ischemic cardiovascular events after acute coronary syndrome (ACS) or PCI. The TxGNN model predicts it may also be effective for **Intracranial Arteriosclerosis**, currently supported by **11 clinical trials** and **3 publications**, though the most directly relevant trial (CAPTIVA) is still ongoing.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Intracranial Arteriosclerosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question (Hold pending confirmatory data) |

*Note: Original (approved) indication text could not be extracted — no Saudi Arabia license records exist in this pack, and the TFDA package insert has not yet been retrieved (see Data Gap DG001, blocking).*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available (Data Gap DG002). Based on the information present in this evidence pack, Ticagrelor is a reversible P2Y12 receptor antagonist and part of the modern antiplatelet drug class; its efficacy in preventing ischemic cardiovascular events after ACS/PCI is described in this pack as a core, well-established mechanism (see the rationale for the "ischemic disease" candidate below), and mechanistically this platelet-inhibition effect may extend to other atherothrombotic conditions.

Intracranial arteriosclerosis causes ischemic events through platelet-dependent thrombus formation on stenotic intracranial vessels — the same underlying process (platelet activation and aggregation) that P2Y12 inhibition targets in coronary and peripheral arterial disease. This gives the prediction biological plausibility.

However, the evidence pack explicitly flags an important caveat: intracranial vascular anatomy and bleeding risk (including hemorrhagic transformation) differ meaningfully from the coronary system, so the mechanism cannot simply be extrapolated — it requires validation in a dedicated intracranial-disease population rather than relying on cardiac/PAD trial data alone.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Phase 3 | Active, not recruiting | 1,683 | CAPTIVA — directly compares rivaroxaban/ticagrelor/both vs. clopidogrel for reducing 1-year ischemic stroke, ICH, or vascular death in intracranial atherosclerotic stenosis; results pending. |
| [NCT04948749](https://clinicaltrials.gov/study/NCT04948749) | N/A | Recruiting | 792 | DREAM-PRIDE — drug-eluting stent + aggressive medical therapy (incl. antiplatelet) vs. standard medical therapy for symptomatic intracranial atherosclerotic disease. |
| [NCT01732822](https://clinicaltrials.gov/study/NCT01732822) | Phase 3b | Completed | 13,885 | EUCLID — compares ticagrelor vs. clopidogrel on cardiovascular death, MI, and ischemic stroke risk in peripheral artery disease. |
| [NCT01813435](https://clinicaltrials.gov/study/NCT01813435) | Phase 3 | Completed | 15,991 | GLOBAL LEADERS — ticagrelor-based antiplatelet strategy vs. standard DAPT after stent implantation. |
| [NCT06058130](https://clinicaltrials.gov/study/NCT06058130) | N/A | Unknown | 2,171 | Anticoagulation vs. anticoagulation + antiplatelet in acute ischemic stroke with concomitant AF and extracranial/intracranial artery stenosis. |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | N/A | Recruiting | 100 | Genotype-guided P2Y12 inhibitor selection vs. conventional clopidogrel in symptomatic intracranial atherosclerotic disease (pilot). |
| [NCT07164859](https://clinicaltrials.gov/study/NCT07164859) | Phase 3 | Not yet recruiting | 1,700 | SOLOPCI — short DAPT followed by P2Y12 monotherapy in older PCI patients. |
| [NCT07354828](https://clinicaltrials.gov/study/NCT07354828) | N/A | Not yet recruiting | 3,500 | Quality-control standard system for coronary revascularization based on DAPT. |
| [NCT02605447](https://clinicaltrials.gov/study/NCT02605447) | Phase 4 | Completed | 2,009 | EVOLVE Short DAPT — 3-month DAPT safety in high-bleeding-risk PCI patients. |
| [NCT03620760](https://clinicaltrials.gov/study/NCT03620760) | Phase 4 | Unknown | 2,036 | Low-dose vs. standard-dose ticagrelor after DES implantation for unstable angina. |

*(1 additional trial, NCT06857045, was withdrawn with 0 enrollment and is omitted.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | RCT (design paper) | Int J Stroke | Describes the CAPTIVA trial design, testing whether other dual antithrombotic combinations (incl. ticagrelor) outperform clopidogrel+aspirin for symptomatic intracranial atherosclerotic stenosis. |
| [38252758](https://pubmed.ncbi.nlm.nih.gov/38252758/) | 2024 | Review | Stroke | Focused update on intracranial atherosclerosis, summarizing knowledge gaps in antithrombotic management. |
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohort | J Neurointerv Surg | Reports experience with lower-dose ticagrelor (60 mg BID) + aspirin vs. standard aspirin/clopidogrel for neurointerventional (intracranial) stenting. |

---

## Saudi Arabia Market Information

Ticagrelor currently holds **no marketing authorization records** in this dataset (market status: Not Marketed; total licenses: 0). No product/dosage-form information is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all currently unavailable — TFDA package insert extraction is flagged as a **Blocking** data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold (Research Question stage)**

**Rationale:**
The mechanistic rationale is biologically plausible and one directly relevant Phase 3 trial (CAPTIVA, NCT05047172) is underway, but it has not yet reported results, and no completed trial specifically targets intracranial arteriosclerosis outcomes. Evidence level is L2 — insufficient to move past a research question into active development, particularly given the distinct hemorrhagic risk profile of intracranial vasculature.

**To proceed, the following is needed:**
- CAPTIVA (NCT05047172) and DREAM-PRIDE (NCT04948749) primary results (expected ~2026–2027)
- TFDA package insert data — warnings, contraindications (DG001, Blocking)
- Confirmed mechanism-of-action data via DrugBank (DG002, High)
- Formal original-indication/regulatory text, since no license records exist in this pack

**Cross-reference note:** This evidence pack also contains a separate candidate indication, **"ischemic disease"** (rank 4), with substantially stronger evidence (Evidence Level L1, decision stage S3, "Proceed with Guardrails") — reflecting ticagrelor's core, already-substantiated use in post-ACS/PCI ischemic event prevention. If a nearer-term repurposing decision is needed, that candidate warrants separate prioritized review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

