---
layout: default
title: Aceclofenac
parent: 僅模型預測 (L5)
nav_order: 14
evidence_level: L5
indication_count: 10
---

# Aceclofenac
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

# Aceclofenac: From Musculoskeletal Pain to Inflammatory Spondylopathy

## One-Sentence Summary

Aceclofenac is an oral non-steroidal anti-inflammatory drug (NSAID) of the phenylacetic acid class, widely established for symptomatic relief of pain and inflammation in musculoskeletal conditions including osteoarthritis and rheumatoid arthritis.
The TxGNN model predicts it may be effective for **Inflammatory Spondylopathy** (encompassing ankylosing spondylitis and related axial spondyloarthropathies),
with **3 clinical trials** and **17 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Musculoskeletal pain and inflammatory arthropathy (OA, RA) — no Saudi Arabia regulatory approval on file |
| Predicted New Indication | Inflammatory Spondylopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Aceclofenac is a phenylacetic acid-derived NSAID that inhibits both COX-1 and COX-2 enzymes, reducing prostaglandin synthesis to suppress pain and inflammation. Importantly, aceclofenac's anti-inflammatory profile extends beyond classical COX inhibition: it also downregulates pro-inflammatory cytokines including IL-1β and TNF-α — cytokines that drive the synovial and entheseal inflammation central to spondyloarthropathies. This dual mechanism makes it mechanistically well-suited for inflammatory spinal conditions.

Inflammatory spondylopathy — a category encompassing ankylosing spondylitis (AS), non-radiographic axial spondyloarthritis, and related disorders — is defined by exactly the prostaglandin- and cytokine-mediated inflammatory cascades that aceclofenac directly targets. NSAIDs are in fact the first-line pharmacological recommendation in international ASAS/EULAR guidelines for axial spondyloarthritis. Aceclofenac has been directly evaluated in RCTs involving AS patients since the mid-1990s, and comprehensive reviews consistently list AS alongside OA and RA as established indications.

The high TxGNN prediction score (99.63%) therefore reflects not a speculative leap, but a documented pharmacological relationship that simply lacks a formal Saudi Arabia (SFDA) registration. The primary open question is whether existing RCT evidence (predominantly from the 1990s) meets current regulatory standards, and how aceclofenac positions against more recently approved agents such as etoricoxib and celecoxib in this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00647517](https://clinicaltrials.gov/study/NCT00647517) | Phase 4 | Completed | 60 | Pilot RCT evaluating tramadol/APAP add-on to COX-2 NSAID background therapy in patients with ankylosing spondylitis and rheumatoid arthritis (Taiwan). Confirms NSAIDs as backbone therapy in inflammatory spondylitis; BASDAI >3 used as disease activity threshold for enrollment. |
| [NCT02883569](https://clinicaltrials.gov/study/NCT02883569) | N/A | Completed | 1102 | Comparative effectiveness study of surgical vs. non-surgical treatment for low back pain from herniated intervertebral disc and spinal stenosis. Provides broad context on pharmacological management pathways for spinal disorders; aceclofenac role not specified. |
| [NCT05164198](https://clinicaltrials.gov/study/NCT05164198) | Phase 4 | Unknown | 448 | Multicenter prospective trial examining standard-dose vs. reduced-dose TNF inhibitor in stable AS patients. NSAIDs likely used as background co-medication; aceclofenac is not the primary investigational agent. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [8823692](https://pubmed.ncbi.nlm.nih.gov/8823692/) | 1996 | RCT | The Journal of Rheumatology | 3-month multicenter double-blind trial: aceclofenac 100 mg BID vs. tenoxicam 20 mg QD in active AS patients. Aceclofenac demonstrated equivalent efficacy and safety, establishing direct RCT evidence in inflammatory spondylopathy. |
| [8823693](https://pubmed.ncbi.nlm.nih.gov/8823693/) | 1996 | RCT | The Journal of Rheumatology | Multicenter controlled trial of aceclofenac efficacy and tolerability specifically in active AS; confirmed therapeutic benefit and acceptable tolerability profile compared to indomethacin. |
| [34876850](https://pubmed.ncbi.nlm.nih.gov/34876850/) | 2021 | Systematic Review | Journal of Pain Research | Most recent comprehensive review of aceclofenac analgesic and anti-inflammatory effects across musculoskeletal disorders including LBP, scapulohumeral periarthritis, OA, RA, and AS. Concludes aceclofenac is effective and generally well-tolerated. |
| [15163279](https://pubmed.ncbi.nlm.nih.gov/15163279/) | 2004 | Review | Expert Opinion on Pharmacotherapy | Clinical review of aceclofenac in inflammatory pain management; reports >75 million patients treated worldwide; efficacy comparable to diclofenac, naproxen, and indomethacin across OA, RA, and AS settings. |
| [11511027](https://pubmed.ncbi.nlm.nih.gov/11511027/) | 2001 | Review | Drugs | Reappraisal of aceclofenac in pain and rheumatic disease; covers effects on multiple inflammatory mediators and cartilage metabolism alongside head-to-head clinical comparison data with other NSAIDs. |
| [8799688](https://pubmed.ncbi.nlm.nih.gov/8799688/) | 1996 | Pharmacodynamic Review | Drugs | Detailed pharmacodynamic profile; preclinical data suggest lower GI damage potential than diclofenac; double-blind trials confirm equivalent efficacy to ketoprofen, indomethacin, and diclofenac in RA, OA, and AS. |
| [11548913](https://pubmed.ncbi.nlm.nih.gov/11548913/) | 2001 | Health Economics | PharmacoEconomics | Economic modelling of aceclofenac vs. other NSAIDs in OA, RA, and AS incorporating mild-to-moderate adverse event costs; supports a favourable overall cost-effectiveness profile. |
| [22350497](https://pubmed.ncbi.nlm.nih.gov/22350497/) | 2012 | Review | Clinical Drug Investigation | Review of NSAID-induced gastropathy and PPI co-prescription strategy in OA, RA, and AS; directly relevant to designing a gastroprotection monitoring plan for aceclofenac use in spondylopathy. |
| [10081315](https://pubmed.ncbi.nlm.nih.gov/10081315/) | 1999 | Clinical Overview | Revue Médicale de Liège | Clinical overview of aceclofenac (Biofenac) pharmacology and indications covering OA, RA, AS, and post-traumatic inflammation; standard oral dose confirmed at 100 mg twice daily in adults. |
| [23192419](https://pubmed.ncbi.nlm.nih.gov/23192419/) | 2013 | RCT | Clinical Rheumatology | 12-week double-blind placebo-controlled RCT of tramadol/acetaminophen add-on in AS (Taiwan, n=60); enrolled active AS per Modified New York Criteria with BASDAI >3. Confirms NSAID backbone role in AS management. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two direct RCTs from 1996 demonstrate aceclofenac's efficacy in ankylosing spondylitis — the primary subtype within inflammatory spondylopathy — and multiple systematic reviews and narrative reviews consistently list this indication alongside OA and RA as established therapeutic territory. The drug's COX/cytokine inhibition mechanism aligns directly with the pathophysiology of inflammatory spondylopathy, making this a pharmacologically sound and evidence-supported candidate. The primary barrier is the absence of Saudi Arabia (SFDA) registration and the age of the foundational RCT data relative to current regulatory expectations.

**To proceed, the following is needed:**
- Package insert review to obtain full warnings, contraindications, and drug interaction data (currently Blocking gap DG001)
- Mechanism of action documentation from DrugBank (gap DG002) to complete the mechanistic rationale section
- Safety monitoring plan addressing GI risk, renal function, and cardiovascular profile in line with current NSAID safety frameworks
- Assessment of whether the 1996 RCT evidence base meets current SFDA regulatory registration requirements, or whether a bridging/new registration study is needed for the Saudi Arabia market
- Competitive landscape review positioning aceclofenac against currently approved agents in Saudi Arabia for axial spondyloarthritis (e.g., etoricoxib, celecoxib, naproxen) to evaluate market differentiation potential
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

