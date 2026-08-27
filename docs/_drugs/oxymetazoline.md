---
layout: default
title: Oxymetazoline
parent: 僅模型預測 (L5)
nav_order: 468
evidence_level: L5
indication_count: 3
---

# Oxymetazoline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Oxymetazoline: From Undocumented Original Indication to Nasal Cavity Disease (Data-Gap Flag)

## One-Sentence Summary

> This evidence pack does not document oxymetazoline's original indication or Taiwan market status data (flagged as a data gap — see note below).
> The TxGNN model predicts efficacy for **Nasal Cavity Disease**, with **8 relevant clinical trials** and **5 publications** identified,
> including one directly relevant completed Phase 2 RCT. Note: the drug is pharmacologically a well-known topical nasal decongestant, so this may reflect a source-data gap rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (`original_indications` empty, `original_moa` unavailable) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not populated in this evidence pack's structured fields (`original_moa` is unavailable). Based on the pharmacological context recorded in the model's own repurposing rationale, oxymetazoline is a selective α1-adrenergic receptor agonist with partial α2 activity. It acts on nasal mucosal vascular smooth muscle to produce vasoconstriction, reducing mucosal congestion and swelling — the standard pharmacological basis for treating nasal congestion/obstruction.

**Important data-quality note:** this evidence pack records no original indication and a Taiwan market status of "未上市" (not marketed), yet oxymetazoline is a decades-old, globally marketed OTC topical nasal decongestant (e.g., Afrin). The model's own rationale explicitly flags this as likely a gap in the source database rather than a genuine drug-repurposing discovery — the "predicted" indication (nasal cavity disease / congestion) essentially overlaps with the drug's already-established real-world use. This should be corrected at the source-data level before this candidate is treated as a novel repurposing opportunity.

Setting the data-gap issue aside, the mechanistic rationale itself is sound: α1-agonist–driven vasoconstriction is a well-established treatment approach for nasal mucosal congestion/obstruction, which is consistent with the predicted indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Randomized, double-blind, double-dummy, placebo-controlled 4-way crossover testing an H3-receptor antagonist against nasal-allergen-induced congestion in seasonal allergic rhinitis; graded "A" relevance — high-quality efficacy-testing design directly applicable to nasal congestion indications. |
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Phase 4 | Completed | 20 | Directly compares topical 0.05% oxymetazoline vs. 1:1000 epinephrine for blood loss and surgical field visualization before endoscopic sinus surgery. |
| [NCT01411969](https://clinicaltrials.gov/study/NCT01411969) | N/A | Completed | 16 | Acoustic rhinometry study using 0.05% oxymetazoline aerosol spray for nasal decongestion to characterize rhinogram notches. |
| [NCT03962634](https://clinicaltrials.gov/study/NCT03962634) | Phase 2 | Terminated (N=3) | 3 | Kovanaze (tetracaine + oxymetazoline) nasal mist vs. articaine injection for maxillary dental pulpal anesthesia; graded "B" — uses the drug but endpoint is dental anesthesia, not nasal disease. |
| [NCT04104789](https://clinicaltrials.gov/study/NCT04104789) | Phase 2 | Withdrawn (N=0) | 0 | Same Kovanaze vs. articaine design as above; withdrawn before enrollment. |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Completed | 16 | Blinded triple-crossover comparing cocaine, lidocaine/xylometazoline (same decongestant class), and saline for intranasal analgesia before nasotracheal intubation; graded "C" — indirect drug-class support only. |
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | NA | Completed | 106 | Compares co-phenylcaine nasal spray (decongestant + local anesthetic) vs. nebulization before rigid nasoendoscopy; graded "C" — procedural use, not disease-treatment testing. |
| [NCT03620513](https://clinicaltrials.gov/study/NCT03620513) | Phase 4 | Completed | 160 | Double-blind study of topical anesthesia and/or decongestant pretreatment to reduce pain/discomfort during fiberoptic nasal pharyngoscopy and laryngoscopy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8615587](https://pubmed.ncbi.nlm.nih.gov/8615587/) | 1996 | Animal study (rabbit) | Ann Otol Rhinol Laryngol | Oxymetazoline nose drops evaluated for effect on early local tissue defense in an experimental bacterial maxillary sinus infection model. |
| [9929658](https://pubmed.ncbi.nlm.nih.gov/9929658/) | 1998 | Cohort/observational | Ann N Y Acad Sci | Assessed olfactory function and nasal volume (via acoustic rhinometry) in acute rhinitis. |
| [25496205](https://pubmed.ncbi.nlm.nih.gov/25496205/) | 2015 | Cohort | J Plast Surg Hand Surg | Evaluated nasal patency by acoustic rhinometry after repair of complete unilateral cleft lip and palate. |
| [28490409](https://pubmed.ncbi.nlm.nih.gov/28490409/) | 2017 | Case series/technique report | Am J Rhinol Allergy | Endoscopic-guided coblation treatment technique for nasal telangiectasias in hereditary hemorrhagic telangiectasia. |
| [38024464](https://pubmed.ncbi.nlm.nih.gov/38024464/) | 2023 | Case report | Global Pediatric Health | Rhinoscleroma in a 9-year-old boy presenting with nasal obstruction. |

---

## Taiwan Market Information

No authorizations are recorded for oxymetazoline in this evidence pack — `taiwan_regulatory.total_licenses` = 0 and `market_status` = "未上市" (not marketed). No license table can be produced from available data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top-ranked predicted indication (nasal cavity disease) has L2-level evidence — one completed Phase 2 RCT plus several trials directly using oxymetazoline for nasal/decongestant purposes — supporting mechanistic and clinical plausibility. However, this candidate is currently blocked from safety review (DG001, Blocking) due to missing TFDA label warnings/contraindications, and the drug's original indication and MOA are undocumented in the source data (DG002, High), which should be resolved before proceeding.

**To proceed, the following is needed:**
- Retrieve and reconcile the drug's actual original indication and regulatory history — the current "no original indication / not marketed" record conflicts with oxymetazoline's known long-standing OTC use and should be verified as a source-data gap rather than accepted as-is
- Obtain TFDA package insert warnings/contraindications (DG001) to complete the S1 safety pre-screen
- Obtain confirmed MOA data from DrugBank (DG002)
- Given the apparent overlap between "predicted" and real-world use, confirm with the source team whether this candidate should even be scored as a novel repurposing signal, or reclassified once original-indication data is corrected
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

