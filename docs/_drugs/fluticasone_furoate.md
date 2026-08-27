---
layout: default
title: Fluticasone Furoate
parent: 僅模型預測 (L5)
nav_order: 276
evidence_level: L5
indication_count: 8
---

# Fluticasone Furoate
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

# Fluticasone Furoate: From Asthma to Atopic Eczema

## One-Sentence Summary

Fluticasone furoate is a corticosteroid whose furoate monotherapy (Arnuity Ellipta) is globally approved for asthma, with combination products (Relvar/Breo Ellipta, +vilanterol) approved for COPD; it is not currently marketed in Saudi Arabia. The TxGNN model predicts it may be effective for **Atopic Eczema**, with **12 clinical trials** and **2 publications** currently associated with this direction — though most of the trial evidence involves fluticasone **propionate**, not furoate itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (global approval, e.g. Arnuity Ellipta; not marketed in Saudi Arabia) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for fluticasone furoate is not available in this evidence pack. Based on known information, fluticasone furoate is a synthetic trifluorinated corticosteroid in the same pharmacological class as fluticasone propionate. It acts as a glucocorticoid receptor agonist, producing potent local anti-inflammatory and anti-allergic effects. Its efficacy in asthma (as furoate monotherapy, Arnuity Ellipta) and in COPD (combined with vilanterol, Relvar/Breo Ellipta) has been established, which supports a plausible mechanistic extension to other corticosteroid-responsive inflammatory conditions.

Atopic eczema is a chronic, corticosteroid-responsive inflammatory skin disease, and topical corticosteroids are standard first-line therapy. This makes a class-level mechanistic link between fluticasone furoate and atopic eczema reasonable.

However, the supporting evidence in this pack has an important caveat: nearly all identified trials use fluticasone **propionate** formulations (e.g., Cutivate cream/lotion 0.05%) rather than furoate. Furoate currently lacks a dedicated topical dermatological formulation and has no direct clinical trials in atopic eczema — the evidence here should be read as same-class inference, not molecule-specific proof.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01772056](https://clinicaltrials.gov/study/NCT01772056) | Phase 3 | Terminated | 54 | Twice-weekly topical fluticasone propionate 0.05% maintenance vs. emollient alone to prevent AD relapse in children; terminated early. |
| [NCT00546000](https://clinicaltrials.gov/study/NCT00546000) | Phase 4 | Completed | 56 | Open-label study of Cutivate (fluticasone propionate) lotion 0.05% and its effect on the HPA axis in pediatric AD. |
| [NCT00616538](https://clinicaltrials.gov/study/NCT00616538) | Phase 4 | Completed | 121 | Pilot RCT comparing non-steroidal EpiCeram device vs. mid-strength fluticasone propionate 0.05% in pediatric moderate-to-severe AD. |
| [NCT00426283](https://clinicaltrials.gov/study/NCT00426283) | Phase 2 | Completed | 42 | Double-blind RCT of swallowed high-dose fluticasone propionate vs. placebo in eosinophilic esophagitis (allergic/eosinophilic mechanism, not skin AD). |
| [NCT01915914](https://clinicaltrials.gov/study/NCT01915914) | Phase 4 | Completed | 107 | Open-label RCT of intermittent twice-weekly fluticasone propionate 0.05% cream plus moisturizer to reduce AD relapse risk in children. |
| [NCT00689832](https://clinicaltrials.gov/study/NCT00689832) | Phase 4 | Completed | 487 | RCT comparing tacrolimus 0.03% vs. fluticasone 0.005% ointment in children ≥2 years with moderate-to-severe AD. |
| [NCT07537751](https://clinicaltrials.gov/study/NCT07537751) | N/A | Completed | 40 | Double-blind RCT comparing topical crisaborole 2% vs. fluticasone propionate 0.05% in children with mild-to-moderate AD (SCORAD/ISGA endpoints). |
| [NCT00690105](https://clinicaltrials.gov/study/NCT00690105) | Phase 4 | Completed | 577 | RCT comparing tacrolimus 0.1% vs. fluticasone 0.005% ointment in adults with facial ("red face") AD lesions. |
| [NCT03742414](https://clinicaltrials.gov/study/NCT03742414) | Phase 2 | Active, not recruiting | 398 | Proactive skin-barrier care (including proactive fluticasone propionate cream) vs. reactive therapy to reduce AD onset/severity and prevent food allergy in infants. |
| [NCT00119158](https://clinicaltrials.gov/study/NCT00119158) | Phase 4 | Completed | 90 | Vehicle-controlled paired study of pimecrolimus (Elidel) 1% combined with fluticasone propionate (Cutivate) 0.05% in severe AD lesions. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40066386](https://pubmed.ncbi.nlm.nih.gov/40066386/) | 2025 | Cohort (case study) | Indian J Otolaryngol Head Neck Surg | Discusses allergen immunotherapy use in patients with autoimmune disease, including relevance to atopic dermatitis management. |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Reviews intranasal corticosteroids and HPA-axis/adrenal suppression risk in allergic conditions that coexist with atopic dermatitis. |

## Saudi Arabia Market Information

Fluticasone furoate currently holds no marketing authorization in Saudi Arabia (market status: not marketed; 0 licenses on record), so no product-level authorization table is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L3, and the supporting trials predominantly use fluticasone **propionate**, not furoate — furoate has no dedicated topical dermatological formulation or direct atopic eczema trial, and the one directly relevant Phase 3 trial (NCT01772056) was terminated. This is class-level, not molecule-specific, evidence, so a Go/Guardrails decision is not yet supportable.

**To proceed, the following is needed:**
- Furoate-specific topical formulation and at least one dedicated clinical trial in atopic eczema
- Detailed mechanism of action (MOA) data from DrugBank
- TFDA/SFDA package insert warnings, contraindications, and DDI data (currently unavailable)
- Note: within this same evidence pack, the "bronchitis" (COPD-spectrum) indication (rank 2, evidence level L2, "Proceed with Guardrails") is directly supported by fluticasone furoate/vilanterol trial data (e.g., NCT02989935, RELVAR) and may warrant separate, more advanced evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

