---
layout: default
title: Guaifenesin
parent: 僅模型預測 (L5)
nav_order: 302
evidence_level: L5
indication_count: 5
---

# Guaifenesin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Guaifenesin: From Cough (Expectorant) to Nasal Cavity Disease

## One-Sentence Summary

> Guaifenesin is a widely used over-the-counter expectorant, traditionally indicated for cough and chest congestion associated with upper respiratory irritation.
> The TxGNN model predicts it may be effective for **Nasal Cavity Disease**,
> with **1 clinical trial** and **2 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cough / chest congestion (expectorant) — no formal indication text available in this evidence pack |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA query returned a data gap). Based on known information, guaifenesin is a classic mucolytic/expectorant; its efficacy in reducing cough and chest congestion by thinning respiratory secretions has long been established, and mechanistically this action may extend to conditions involving nasal mucus accumulation.

The proposed mechanistic link is that guaifenesin promotes serous secretion in the respiratory tract, lowers mucus viscosity, and increases mucociliary clearance efficiency. This provides a direct pharmacological rationale for diseases involving nasal mucosa/sinus mucus buildup, and guaifenesin is already commonly used clinically as an adjunct in sinusitis and rhinitis management — supporting the biological plausibility of this TxGNN prediction rather than treating it as a purely coincidental graph association.

By contrast, the model's lower-ranked predictions (acute laryngopharyngitis, faucial diphtheria, cervical disc degenerative disorder, papillary conjunctivitis) lack any supporting mechanistic or literature evidence and are assessed as likely knowledge-graph noise from anatomical proximity rather than genuine pharmacology — none are carried forward in this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01364467](https://clinicaltrials.gov/study/NCT01364467) | Phase 2 | Completed | 30 | 14-day randomized, placebo-controlled pilot trial of oral guaifenesin in pediatric chronic rhinitis (ages 7–18), assessing nasal symptom relief via SN-5 survey, nasal airway volume, and secretion biophysical properties. |

*Note: This is a small pilot study (n=30); statistical power and adult generalizability are limited.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9065342](https://pubmed.ncbi.nlm.nih.gov/9065342/) | 1997 | Review/Clinical | American Journal of Rhinology | Management experience in 22 adult cystic fibrosis patients with chronic sinusitis, discussing treatment approaches including mucolytic therapy. |
| [12487405](https://pubmed.ncbi.nlm.nih.gov/12487405/) | 2002 | Review | Logopedics, Phoniatrics, Vocology | Discusses guaifenesin-containing decongestants as a treatment strategy for hidden respiratory allergies affecting voice users. |

---

## Saudi Arabia Market Information

Guaifenesin currently has no marketing authorization on record in Saudi Arabia (0 licenses); no product listing is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 2 pilot RCT plus two supportive review-level publications establish a preliminary, mechanistically plausible case for guaifenesin's mucolytic effect on nasal mucosa, but the pilot's small sample size (n=30, pediatric only) and lack of adult data mean the evidence is not yet sufficient for an unconditional Go.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (currently blocking — required before any safety pre-assessment)
- Confirmed mechanism of action data from DrugBank
- A confirmatory trial in adults with nasal cavity disease, given the current evidence is limited to a pediatric pilot study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

