---
layout: default
title: Omalizumab
parent: 僅模型預測 (L5)
nav_order: 462
evidence_level: L5
indication_count: 10
---

# Omalizumab
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

# Omalizumab: From Allergic Asthma to Bronchitis

## One-Sentence Summary

Omalizumab (DB00043) is an anti-IgE monoclonal antibody originally developed and clinically established for **moderate-to-severe allergic asthma** (and, separately, chronic spontaneous urticaria). The TxGNN model predicts it may be effective for **Bronchitis**, but this ranks as the model's top-scoring prediction (rank 43 overall, score 99.9992%) rather than the strongest-evidenced one — supporting data consist of only **2 clinical trials** and **8 publications**, nearly all of which studied asthma populations where "bronchitis" appeared as a comorbid term rather than the primary indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic Asthma (widely documented across the supporting literature/trials in this pack; no formal license record available) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.9992% (rank 43) |
| Evidence Level | L4 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002 — [Data Gap], flagged High severity). Based on known information reflected throughout the supporting literature in this pack, omalizumab binds free IgE and reduces FcεRI expression on mast cells and basophils, reducing airway inflammation — a mechanism validated in moderate-to-severe persistent allergic asthma and later extended to chronic spontaneous urticaria.

The link to bronchitis is mechanistically indirect. Bronchitis (acute or chronic) is predominantly a non-IgE-mediated inflammatory pathology, and the anti-IgE mechanism does not map cleanly onto its core pathophysiology. Consistent with this, the pack's own repurposing rationale flags that the supporting trials and publications largely originate from asthma or COPD research where "bronchitis" appears as a comorbidity or keyword, rather than studies designed with bronchitis as the primary indication. The single trial evaluating a steroid-sparing effect in eosinophilic bronchitis (NCT02049294) enrolled only 11 patients and was graded "B" relevance (indirect) rather than a direct, adequately powered bronchitis trial — hence the L4 (mechanism/preclinical-level) evidence classification and "Hold" recommendation, despite the very high TxGNN score.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Completed | 11 | Randomized, double-blind, placebo-controlled, 3-center trial testing whether add-on omalizumab allows a reduction in prednisone dose in patients with asthma and persistent eosinophilic bronchitis (steroid-sparing effect). Relevance graded "B" — indirect, very small sample. |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2b | Completed | 382 | Dose-finding study of **QGE031 (ligelizumab)**, a different anti-IgE antibody — not omalizumab — as add-on therapy in Chronic Spontaneous Urticaria. No direct link to bronchitis; relevance graded "C" (low). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui (Jpn J Anesthesiology) | Preoperative management review for patients with bronchial asthma or chronic bronchitis; notes omalizumab availability for severe allergic asthma per Japanese guidelines. |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clin Rev Allergy Immunol | Omalizumab approval and post-approval experience; efficacy shown for moderate-to-severe persistent asthma. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case Report | J Investig Allergol Clin Immunol | A rare case of plastic bronchitis following bronchial thermoplasty (procedural complication case, not an omalizumab efficacy study). |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Not yet classified | Curr Med Res Opin | Pooled safety/tolerability analysis of omalizumab in children with allergic (IgE-mediated) asthma. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Not yet classified | Expert Opin Pharmacother | Discusses smoking-induced airway diseases (chronic bronchitis, emphysema, ACO) contributing to chronic respiratory symptoms in asthma; notes uncertainty in drug treatment due to trial exclusions. |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Not yet classified | Allergol Immunopathol | General update on monoclonal antibodies in pediatrics, including allergic disease use. |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Not yet classified | Postepy Dermatol Alergol | Omalizumab in middle-aged/older patients with severe allergic asthma-COPD overlap. |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | Not yet classified | Rev Mal Respir | French working-party review on definitions/treatment of adult asthma exacerbations. |

## Saudi Arabia Market Information

Omalizumab is currently **not marketed** in Saudi Arabia (market status: 未上市), and no product license records are available (total licenses: 0).

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all recorded as data gaps in this evidence pack — DG001, flagged Blocking severity, requires retrieval of the TFDA/regulator package insert before any S1 safety assessment can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but the underlying evidence is thin and largely indirect — only one small (n=11), non-bronchitis-specific trial and no literature designed around bronchitis as a primary endpoint. The mechanistic case is also weak, since bronchitis is not primarily an IgE-mediated condition. This does not meet the bar to proceed past S0.

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Detailed mechanism-of-action documentation from DrugBank — currently a High-severity data gap (DG002)
- A dedicated, adequately powered clinical trial in a well-defined bronchitis population (the current small, indirect trial is insufficient)
- Consider prioritizing other candidates in this evidence pack with stronger direct support — notably **atopic eczema** (Evidence Level L2, direct Phase 4 RCT NCT02300701 in severe pediatric eczema) — before further investment in the bronchitis hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

