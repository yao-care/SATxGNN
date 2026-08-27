---
layout: default
title: Levonorgestrel
parent: 僅模型預測 (L5)
nav_order: 374
evidence_level: L5
indication_count: 6
---

# Levonorgestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Levonorgestrel: From Contraception to Acne

## One-Sentence Summary

Levonorgestrel is a synthetic progestin widely used in hormonal contraceptives (oral pills, IUS, implants). The TxGNN model predicts it may be effective for **Acne (disease)**, with **5 clinical trials** and **20 publications** returned in the evidence search — but on closer reading, most of this evidence is indirect (acne recorded as a side-effect signal in contraception studies) rather than direct treatment evidence, and the drug's own pharmacology raises a caution flag against this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from regulatory data (no Saudi Arabia licenses on file); levonorgestrel is generally known as a contraceptive progestin |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on known information, levonorgestrel is a 19-nortestosterone-derived progestin used in combined oral contraceptives, progestin-only pills, IUS (e.g., Mirena), and subdermal implants (e.g., Norplant). Its contraceptive efficacy is well established through inhibition of ovulation, thickening of cervical mucus, and endometrial changes.

The link to acne is mechanistically ambiguous rather than straightforwardly supportive. Combined oral contraceptives (estrogen + progestin) are a recognized acne treatment because estrogen suppresses ovarian androgen production and raises sex hormone-binding globulin, lowering free androgen levels. However, levonorgestrel itself is one of the more androgenic progestins in clinical use (literature PMID 7825629 explicitly notes its androgenic activity), and androgenic progestins are generally understood to counteract, not enhance, the anti-acne effect of the estrogen component. One retrieved study (PMID 15025547) directly reports that an anti-androgenic progestin combination (EE/chlormadinone acetate) was **more effective** than EE/levonorgestrel for treating papulopustular acne — evidence pointing against levonorgestrel's own contribution to acne improvement.

Taken together, the TxGNN score likely reflects levonorgestrel's frequent co-occurrence with "acne" in contraception literature (where acne appears mainly as an adverse-event or comparator marker), rather than a genuine causal treatment relationship. This should be treated as a weak/uncertain signal, not a validated repurposing lead.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00161226](https://clinicaltrials.gov/study/NCT00161226) | N/A | Terminated | 44 | LNG-IUS studied for endometrial cancer prevention in obese women; acne is only referenced as a known side effect of oral progestins, not a study endpoint |
| [NCT01650168](https://clinicaltrials.gov/study/NCT01650168) | N/A | Completed | 101,498 | Large post-marketing safety cohort comparing nomegestrol acetate/estradiol vs. LNG-containing combined oral contraceptives; acne only tracked as an adverse event |
| [NCT00480532](https://clinicaltrials.gov/study/NCT00480532) | N/A | Completed | 131 | Continuous oral contraceptive + doxycycline for bleeding control; the acne-relevant agent is doxycycline, not levonorgestrel |
| [NCT05570786](https://clinicaltrials.gov/study/NCT05570786) | Phase 2 | Completed | 100 | Gestrinone implant for endometriosis pelvic pain; drug and indication unrelated to levonorgestrel/acne |
| [NCT05492487](https://clinicaltrials.gov/study/NCT05492487) | Phase 2 | Unknown | 60 | Mirena (LNG-IUS) vs. megestrol acetate for atypical endometrial hyperplasia fertility preservation; unrelated to acne |

None of these trials directly test levonorgestrel as an acne treatment; all are indirect associations.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12196750](https://pubmed.ncbi.nlm.nih.gov/12196750/) | 2002 | RCT | J Am Acad Dermatol | Low-dose EE/LNG (20mcg/100mcg) oral contraceptive improved biochemical androgen markers and moderate acne vs. placebo |
| [10717776](https://pubmed.ncbi.nlm.nih.gov/10717776/) | 1999 | RCT | Contraception | Multicenter randomized comparison of low-dose OCs with different progestins on androgenic markers and acne outcomes |
| [15025547](https://pubmed.ncbi.nlm.nih.gov/15025547/) | 2004 | Comparative trial review | Drugs | EE/chlormadinone acetate was significantly more effective than EE/levonorgestrel for mild-to-moderate papulopustular acne |
| [21895044](https://pubmed.ncbi.nlm.nih.gov/21895044/) | 2011 | Review | Am J Clin Dermatol | Reviews androgen-driven pilosebaceous unit disorders (acne, hirsutism); anti-androgenic progestins favored over androgenic ones |
| [16796485](https://pubmed.ncbi.nlm.nih.gov/16796485/) | 2006 | Review | J Womens Health | Drospirenone contrasted with MPA, levonorgestrel, and micronized progesterone; androgenic progestins linked to acne occurrence, not reduction |
| [7825629](https://pubmed.ncbi.nlm.nih.gov/7825629/) | 1995 | Review | Am J Med | Establishes levonorgestrel's relatively high androgenic activity among clinically used progestins — the mechanistic basis for caution here |

The remaining literature returned by the search (contraception method reviews, VTE/cardiovascular studies, endometrial hyperplasia trials) mentions levonorgestrel but is not substantively about acne and was excluded as noise.

## Saudi Arabia Market Information

Levonorgestrel is currently **not marketed** in Saudi Arabia per the available regulatory data (0 licenses on file). No product, dosage form, or approved indication text is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The strongest available evidence (PMID 15025547) suggests levonorgestrel's androgenic activity makes it a *weaker* choice for acne compared with anti-androgenic progestins, and no trial directly tests levonorgestrel monotherapy against acne. Combined with the absence of Saudi Arabia market presence and blocking safety data gaps, the evidence does not support advancing this candidate. (Note: the other TxGNN-predicted indications for this drug — Worth syndrome, pregnancy-associated osteoporosis, ADNIV, and two breast adenosis subtypes — returned zero clinical trials or literature and lack any plausible mechanistic link; they are excluded from this report as unsupported model-only predictions, L5.)

**To proceed, the following is needed:**
- TFDA/SFDA package insert data (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- A direct comparative trial isolating levonorgestrel's contribution to acne outcomes (vs. estrogen component or vs. anti-androgenic progestins)
- Reassessment of the TxGNN signal given the reversed-direction mechanistic concern identified above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

