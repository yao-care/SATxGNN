---
layout: default
title: Isoniazid
parent: 僅模型預測 (L5)
nav_order: 343
evidence_level: L5
indication_count: 1
---

# Isoniazid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Isoniazid: From Tuberculosis to Conjunctivitis

## One-Sentence Summary

Isoniazid is a first-line anti-tuberculosis agent, acting specifically against *Mycobacterium tuberculosis* by blocking mycolic acid synthesis. The TxGNN model predicts a possible new indication for **Conjunctivitis**, but the supporting evidence base — **1 clinical trial** and **20 publications** — consists almost entirely of cases where conjunctivitis is a *manifestation of tuberculosis itself*, not independent pharmacological evidence for treating conjunctivitis in general.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (latent and active TB infection treatment) — no formal indication text available in this evidence pack |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Isoniazid's mechanism of action is inhibition of mycolic acid synthesis in *Mycobacterium tuberculosis* (via KatG-mediated activation and InhA inhibition). This mechanism is narrowly targeted to mycobacteria and has no known anti-inflammatory, antiviral, or broad-spectrum antimicrobial activity that would explain efficacy against typical (allergic, viral, or bacterial) conjunctivitis.

Nearly all of the supporting literature reflects a different relationship: tuberculosis infection can itself present as conjunctivitis (e.g., TB conjunctivitis, phlyctenular keratoconjunctivitis). In these cases, isoniazid treats the underlying TB infection, and the conjunctivitis resolves as a downstream effect — not because isoniazid has a direct anti-inflammatory or ocular-surface effect. A smaller subset of cases involves isoniazid used to manage reactive arthritis/conjunctivitis following intravesical BCG therapy, which is again a TB-pathway-mediated context rather than a novel mechanism.

The TxGNN score of 99.36% most likely reflects a strong "isoniazid–TB–conjunctivitis" co-occurrence path in the underlying knowledge graph, rather than independent pharmacological evidence that isoniazid treats conjunctivitis outside the TB context. This distinction is critical for repurposing evaluation: it is an extension of the existing TB indication, not a genuinely new mechanistic signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Phase 3 | Completed | 490 | Compared systemic drug reaction rates between 3HP (rifapentine + isoniazid) and 1HP regimens for latent TB infection. This trial evaluated safety/tolerability of TB prophylaxis, not conjunctivitis as an efficacy endpoint — indirect relevance only (relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Case series | Annales d'oculistique | Local (topical) use of isoniazid in treatment of ocular tuberculosis — the most direct isoniazid-conjunctiva link in the evidence set |
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Prophylaxis study | American Review of Respiratory Disease | Isoniazid prophylaxis for phlyctenular keratoconjunctivitis among a TB-endemic population (Alaska) |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optometry Clinics | General review of ocular side effects of systemic drugs; conjunctivitis is linked to isotretinoin, sulfonamides, salicylates and antineoplastics, not isoniazid specifically |
| [25433746](https://pubmed.ncbi.nlm.nih.gov/25433746/) | 2014 | Case report | Canadian Journal of Ophthalmology | Conjunctival phlyctenulosis as a presenting sign of impending clinical tuberculosis |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case report | Medicine | Pediatric sinonasal tuberculosis presenting with phlyctenular keratoconjunctivitis |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | Case report | Middle East African Journal of Ophthalmology | Tuberculous conjunctivitis in an anophthalmic socket |
| [17133069](https://pubmed.ncbi.nlm.nih.gov/17133069/) | 2006 | Case report | Cornea | Mycobacterium tuberculosis presenting as chronic red eye/conjunctivitis |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Case series | Oftalmologia | 28 cases of tuberculous keratoconjunctivitis, mostly in children with primary TB |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case report | Archives of Ophthalmology | Primary tuberculosis of the conjunctiva |
| [32674602](https://pubmed.ncbi.nlm.nih.gov/32674602/) | 2020 | Case report | Clinical Pediatrics | Unexpected cause of conjunctivitis in an adolescent (TB-associated) |

---

## Saudi Arabia Market Information

Isoniazid currently has no marketing authorization on record in Saudi Arabia (0 licenses in the evidence pack).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not yet available for this evidence pack — TFDA/SFDA package insert data is flagged as a Blocking data gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The available evidence overwhelmingly describes conjunctivitis as a *manifestation of tuberculosis itself* rather than an independent indication treatable by isoniazid's known mechanism. The single clinical trial addresses TB prophylaxis safety, not conjunctivitis efficacy, and no RCT or controlled study directly tests isoniazid against conjunctivitis outside a TB context.

**To proceed, the following is needed:**
- TFDA/SFDA package insert data (warnings, contraindications) — currently a Blocking gap
- Confirmed drug mechanism of action documentation (DrugBank API query)
- Primary evidence separating isoniazid's effect on non-TB conjunctivitis from its established TB-treatment pathway
- Clarification of whether this candidate should instead be scoped as "isoniazid for TB-associated ocular manifestations" rather than "conjunctivitis" broadly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

