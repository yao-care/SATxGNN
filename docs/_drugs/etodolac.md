---
layout: default
title: Etodolac
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
---

# Etodolac
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

# Etodolac: From NSAID Pain/Inflammation Control to Ankylosing Spondylitis

## One-Sentence Summary

Etodolac is a COX-inhibiting NSAID whose formally recorded original indication is not available in this evidence pack (drug is not marketed in Saudi Arabia). Among 10 TxGNN-predicted indications, most are top-ranked but mechanistically implausible graph artifacts (e.g., rare skeletal dysplasias) with no supporting evidence; the one indication with real supporting data is **Ankylosing Spondylitis**, backed by **1 clinical trial** and **10 publications**, though the literature largely reflects etodolac's already-established use in axial spondyloarthritis rather than a genuinely novel signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this pack (drug not marketed in Saudi Arabia; no license/label data). Literature evidence (PMID 1717225) confirms etodolac as an NSAID established for rheumatoid arthritis and osteoarthritis pain/inflammation. |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on known information, etodolac belongs to the NSAID (non-steroidal anti-inflammatory drug) class and acts through COX enzyme inhibition — literature in this pack (PMID 17694363) further describes it as having a relatively selective COX-2 effect. Its efficacy in inflammatory/degenerative joint pain (osteoarthritis, rheumatoid arthritis) is well documented.

Ankylosing spondylitis (AS) is, like RA and OA, a condition where NSAIDs are standard symptomatic therapy for pain and inflammation control. The repurposing rationale attached to this candidate explicitly notes that NSAIDs are already the first-line standard treatment for AS symptom control — meaning the TxGNN high score largely reflects an **already-known pharmacological association** rather than a newly discovered mechanism. Several of the cited publications (e.g., PMID 1717225, PMID 2146130) directly state etodolac's efficacy was studied in AS alongside RA/OA as early as the late 1980s–1990s.

It is worth noting that among the 10 TxGNN-ranked candidates in this pack, the four highest-scoring ones (acromesomelic dysplasia, brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, spondyloarthropathy susceptibility, brachyolmia, pseudoachondroplasia, rheumatoid vasculitis, hypermobility of coccyx) are rare genetic skeletal/structural disorders or conditions where the pack's own mechanistic review flags no plausible NSAID relevance and no supporting trials or literature — these are held (L5/S0/Hold) and are likely graph-embedding artifacts around skeletal-related nodes rather than genuine pharmacological signals. AS (rank 6) is the only candidate with meaningful clinical/literature support and is the focus of this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05164198](https://clinicaltrials.gov/study/NCT05164198) | Phase 4 | Unknown | 448 | Evaluates TNF-inhibitor dose reduction vs. standard dose in AS patients with stable disease activity. **Does not test etodolac directly** — relevance graded "C" (population/indication overlap only, not direct drug evidence). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2525800](https://pubmed.ncbi.nlm.nih.gov/2525800/) | 1989 | Cohort/Open-label | La Revue de medecine interne | Open trial in 4,947 patients with RA, AS, and OA of the lower limbs; etodolac 400–600mg/day showed efficacy and tolerability across these rheumatic conditions. |
| [2150569](https://pubmed.ncbi.nlm.nih.gov/2150569/) | 1990 | Cohort/Open-label (safety) | Rheumatology International | Two large French open-label studies (n=4,947 and n=51,355) confirming efficacy/safety of etodolac in RA, AS, and OA. |
| [2150568](https://pubmed.ncbi.nlm.nih.gov/2150568/) | 1990 | Cohort (postmarketing surveillance) | Rheumatology International | Four postmarketing surveillance studies (n=8,334) across Italy, Switzerland, UK, France; one study included AS patients, confirming favorable safety profile. |
| [2146130](https://pubmed.ncbi.nlm.nih.gov/2146130/) | 1990 | Review | European Journal of Rheumatology and Inflammation | Randomized, double-blind, parallel-group studies comparing etodolac to naproxen/piroxicam and placebo in RA, OA, and AS; etodolac found comparable to standard NSAIDs. |
| [1717225](https://pubmed.ncbi.nlm.nih.gov/1717225/) | 1991 | Review | Drugs | Pharmacology reappraisal: etodolac effective in RA, OA, and AS, and in postoperative/gouty/traumatic pain; adverse effect profile similar to other NSAIDs. |
| [17694363](https://pubmed.ncbi.nlm.nih.gov/17694363/) | 1997 | Review | Inflammopharmacology | Clinical review of etodolac as a multipurpose analgesic; primary anti-inflammatory mechanism via relatively selective COX-2 inhibition; widely applied in RA, AS, and gout. |
| [22071858](https://pubmed.ncbi.nlm.nih.gov/22071858/) | 2011 | Review (safety, Cochrane) | Cochrane Database of Systematic Reviews | Safety of NSAIDs (including aspirin/paracetamol) combined with methotrexate in inflammatory arthritis including AS. |
| [20829199](https://pubmed.ncbi.nlm.nih.gov/20829199/) | 2011 | Review/Guideline | Annals of the Rheumatic Diseases | ASAS recommendations for standardized collection/reporting of NSAID intake as an outcome measure in axial spondyloarthritis trials. |
| [21140116](https://pubmed.ncbi.nlm.nih.gov/21140116/) | 2010 | Cohort (non-etodolac comparator) | Singapore Medical Journal | Open prospective trial of IV pamidronate in NSAID-refractory/intolerant AS patients — supports NSAID as standard first-line comparator, not direct etodolac evidence. |
| [24449987](https://pubmed.ncbi.nlm.nih.gov/24449987/) | 2013 | Review | The Israel Medical Association Journal | Discussion of diagnostic uncertainty in axial spondyloarthritis (indemonstrable axial SpA); no abstract available. |

---

## Saudi Arabia Market Information

Etodolac is not currently marketed in Saudi Arabia; no marketing authorization records are available in this evidence pack (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Etodolac's use in ankylosing spondylitis is supported by decades of open-label/cohort evidence and consistent mechanistic plausibility as an NSAID, but no completed randomized controlled trial specifically evaluates etodolac in AS, and the one registered trial in this pack does not test etodolac directly (TNF-inhibitor dosing study). This is an evidence-consistent but not novel signal, warranting cautious, guarded progression rather than a full Go.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (currently a **Blocking** data gap — required before any S1 safety review)
- Confirmed mechanism of action (MOA) data from DrugBank (currently a **High**-severity data gap)
- Formal drug-drug interaction (DDI) data (current query returned not_found)
- A dedicated etodolac-in-AS clinical trial or comparative effectiveness study, since existing evidence is largely legacy open-label/cohort data from the late 1980s–1990s
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

