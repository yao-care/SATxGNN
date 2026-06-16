---
layout: default
title: Diflunisal
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 10
---

# Diflunisal
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

# Diflunisal: From Pain and Inflammation to Ankylosing Spondylitis

## One-Sentence Summary

Diflunisal is a salicylate-derived non-steroidal anti-inflammatory drug (NSAID) established for pain relief and musculoskeletal inflammation.
The TxGNN model predicts it may be effective for **Ankylosing Spondylitis** (TxGNN rank #5 among 10 candidates; ranks #1–4 are all Hold/L5 with no clinical evidence), with **0 registered clinical trials** and **3 directly relevant publications** (plus 4 NSAID class-effect reviews) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain and musculoskeletal inflammation (NSAID class; no Saudi Arabia regulatory record available) |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.98% (rank #5; top 4 predictions are congenital skeletal dysplasias with no evidence) |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, diflunisal is a difluorophenyl salicylate — an NSAID belonging to the salicylate class — whose analgesic and anti-inflammatory efficacy in musculoskeletal and rheumatic pain has been demonstrated in clinical use. Like other NSAIDs, it is understood to act through cyclooxygenase (COX) inhibition, reducing prostaglandin biosynthesis and thereby suppressing inflammation and pain signalling.

Ankylosing spondylitis (AS) is a chronic immune-mediated inflammatory arthropathy of the axial skeleton driven by aberrant prostaglandin and cytokine signalling. NSAIDs are the established, guideline-recommended first-line pharmacological treatment for AS — reducing spinal pain and stiffness, and potentially slowing radiographic progression in continuous use. Diflunisal's COX-inhibitory mechanism maps directly onto the predominant pathophysiological driver of AS symptoms.

Critically, this prediction is not purely algorithmic: a 12-week double-blind randomised trial (PMID 3524970, 1986) directly compared diflunisal 500 mg twice daily against phenylbutazone in 38 active AS patients, finding both agents effective in improving symptom severity, with diflunisal showing a more rapid early analgesic onset. A 48-week prospective extension from the same cohort (PMID 4062389) further examined disease-activity biomarkers under diflunisal treatment. These studies constitute L3 direct clinical evidence for diflunisal in AS, elevating this prediction above the majority of TxGNN-ranked candidates in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3524970](https://pubmed.ncbi.nlm.nih.gov/3524970/) | 1986 | Controlled Comparative Trial | Clinical Rheumatology | 12-week double-blind RCT in 38 male AS patients: diflunisal 500 mg BID vs phenylbutazone 200 mg BID; both drugs effective in improving symptom severity throughout 48-week follow-up; diflunisal showed more pronounced and rapid early analgesia |
| [4062389](https://pubmed.ncbi.nlm.nih.gov/4062389/) | 1985 | Prospective Cohort | Annals of the Rheumatic Diseases | 48-week longitudinal study in 38 AS patients on diflunisal or phenylbutazone; serum IgA correlated most frequently with chest expansion and lumbar flexion index, and tracked disease activity under treatment — providing a biomarker framework for monitoring diflunisal response |
| [3546687](https://pubmed.ncbi.nlm.nih.gov/3546687/) | 1986 | Observational | The Journal of Rheumatology | Spirometric study in 33 AS patients treated 12 weeks double-blind then 36 weeks open with diflunisal or phenylbutazone; assessed restrictive pulmonary function impairment caused by progressive thoracic ankylosis — provides safety-relevant functional endpoint data |
| [2670397](https://pubmed.ncbi.nlm.nih.gov/2670397/) | 1989 | Narrative Review (other drug) | Clinical Pharmacy | Comprehensive review of diclofenac pharmacology and efficacy in rheumatic diseases including AS; contextualises COX inhibition and prostaglandin reduction as the shared NSAID class mechanism relevant to AS management |
| [6772422](https://pubmed.ncbi.nlm.nih.gov/6772422/) | 1980 | Narrative Review (other drug) | Drugs | Diclofenac review advocating NSAID class for RA, degenerative joint disease, and AS; establishes comparability benchmarks (aspirin, indomethacin) applicable to positioning diflunisal within the NSAID class for AS |
| [387372](https://pubmed.ncbi.nlm.nih.gov/387372/) | 1979 | Narrative Review (other drug) | Drugs | Naproxen class review in rheumatic diseases including AS; demonstrates superiority of propionic acid NSAIDs over aspirin in tolerability — NSAID class context for interpreting diflunisal's position |
| [3539573](https://pubmed.ncbi.nlm.nih.gov/3539573/) | 1986 | Narrative Review (other drug) | Drugs | Pirprofen review demonstrating interchangeability of multiple NSAIDs in AS, osteoarthritis, and musculoskeletal disorders; reinforces class-level treatment equivalence relevant to diflunisal repurposing rationale |

---

## Saudi Arabia Market Information

Diflunisal holds no regulatory authorizations in Saudi Arabia and is currently not marketed. No license records are available for tabulation.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A 1986 double-blind controlled trial directly demonstrated diflunisal's clinical efficacy in active ankylosing spondylitis, and NSAIDs are the established first-line pharmacological class for this indication — making the mechanistic and clinical rationale for repurposing both clear and well-grounded, despite the evidence predating modern trial design standards.

**To proceed, the following is needed:**

- **Regulatory pathway**: Diflunisal is not marketed in Saudi Arabia; market entry or named-patient access pathway must be established before any clinical use
- **Safety documentation**: Full package insert review required — key warnings, contraindications, renal/GI/cardiovascular risks (standard NSAID class concerns), and drug interaction profile must be formally assessed before safety gating (DG001, DG002 data gaps)
- **MOA documentation**: Formal pharmacological dossier to confirm COX-1/2 selectivity profile and distinguish diflunisal from other NSAIDs (DG002)
- **Comparative positioning**: Evaluate whether diflunisal offers advantages over currently available, better-studied NSAIDs for AS (indomethacin, naproxen, celecoxib, etoricoxib) — the existing evidence is from 1985–1986 and pre-dates biological therapy era
- **Trial modernisation**: Consider whether a prospective head-to-head comparison with a current standard-of-care NSAID in AS would be feasible and add value, particularly given the absence of any registered clinical trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

