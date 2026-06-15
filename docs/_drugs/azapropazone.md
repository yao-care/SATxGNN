---
layout: default
title: Azapropazone
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
---

# Azapropazone
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

# Azapropazone: From Inflammatory Arthritis to Inflammatory Spondylopathy

## One-Sentence Summary

Azapropazone is a non-steroidal anti-inflammatory drug (NSAID) with additional uricosuric properties, historically used for conditions including rheumatoid arthritis, ankylosing spondylitis (AS), and psoriatic arthritis before being withdrawn from most markets due to safety concerns.
Among 10 TxGNN-predicted indications, **Inflammatory Spondylopathy** carries the strongest supporting evidence with **2 historical RCTs** and **4 additional publications** — making it the only prediction to reach decision stage S2.
The top-ranked predictions (Ranks 1–5) are all genetic skeletal dysplasias where COX inhibition has no disease-modifying rationale; Rank 10 (inflammatory spondylopathy, score **99.52%**) represents the clinically actionable signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved license in this region (historically: inflammatory arthritis, AS, gout) |
| Predicted New Indication | Inflammatory Spondylopathy |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Azapropazone is a non-selective COX (cyclooxygenase) inhibitor — an NSAID class drug — with an additional uricosuric effect that distinguishes it from most other NSAIDs. While detailed DrugBank MOA records are currently unavailable, azapropazone's pharmacological action follows the established NSAID pathway: inhibition of prostaglandin synthesis via COX-1 and COX-2 blockade, reducing the downstream inflammatory cascade that drives pain, swelling, and structural joint damage.

Inflammatory spondylopathy — covering ankylosing spondylitis, psoriatic arthritis, and Reiter's disease — is fundamentally driven by prostaglandin-mediated axial and peripheral joint inflammation. NSAIDs are recognized as first-line pharmacological therapy for these conditions in all major rheumatology guidelines. Azapropazone's COX inhibition maps directly onto the principal disease mechanism, making this prediction mechanistically sound rather than speculative.

Crucially, this is not merely a model prediction: azapropazone was in active clinical use for ankylosing spondylitis during the 1970s–1980s, with at least two randomized controlled trials demonstrating efficacy comparable to indomethacin. The drug was withdrawn from most markets (notably the UK in the 1990s) due to a less favorable gastrointestinal and renal safety profile relative to newer NSAIDs — not due to lack of efficacy. The TxGNN model is therefore identifying a historically validated, mechanistically grounded use case, with the caveat that the drug's safety record creates a meaningful regulatory obstacle.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [4604141](https://pubmed.ncbi.nlm.nih.gov/4604141/) | 1974 | RCT | Rheumatology and Rehabilitation | Controlled clinical trial of azapropazone in ankylosing spondylitis; earliest formal RCT establishing efficacy in AS |
| [7282105](https://pubmed.ncbi.nlm.nih.gov/7282105/) | 1980 | RCT | Zeitschrift für Rheumatologie | Double-blind RCT (n=60): azapropazone vs indomethacin in AS over 3 weeks; comparable therapeutic effect, with azapropazone marginally favoured on chest expansion and patient global assessment |
| [770082](https://pubmed.ncbi.nlm.nih.gov/770082/) | 1976 | Pilot Comparative Study | Current Medical Research and Opinion | Double-blind crossover study (n=50): azapropazone 1200 mg/day vs indomethacin 100 mg/day in psoriatic arthritis and Reiter's disease; no overall efficacy difference; some withdrawals due to side effects on both arms |
| [369020](https://pubmed.ncbi.nlm.nih.gov/369020/) | 1978 | Narrative Review | Terapevticheskii Arkhiv | Review of drug therapy for ankylosing spondylitis (Bechterew's disease) including azapropazone in historical treatment context |
| [11208503](https://pubmed.ncbi.nlm.nih.gov/11208503/) | 2001 | Case Series | Medical Science Monitor | AS patient with peripheral arthritis unresponsive to conventional NSAID therapy, successfully managed with cyclosporin; contextualizes the limits of NSAID monotherapy in refractory AS |
| [6999577](https://pubmed.ncbi.nlm.nih.gov/6999577/) | 1980 | Clinical Trial | Reumatologia | Clinical evaluation of sulindac (another NSAID) in RA and AS; provides comparative class context for NSAID efficacy in inflammatory spondylopathy |

---

## Saudi Arabia Market Information

Azapropazone has **no approved authorizations** in Saudi Arabia and is not currently marketed in this region. No license table is available.

---

## Safety Considerations

**Key Regulatory History (Critical Constraint):**
Azapropazone was withdrawn from the UK market in the 1990s following post-marketing evidence of a disproportionately high rate of serious gastrointestinal adverse events (bleeding, perforation) compared to other NSAIDs available at the time. Its interaction with warfarin (displacement from plasma protein binding, leading to elevated anticoagulant effect) was identified as a particularly serious drug–drug interaction.

Specific safety data from the DrugBank and TFDA records is not currently available in this Evidence Pack. Please refer to the original package insert and regulatory withdrawal documentation for complete warnings, contraindications, and interaction profiles before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Azapropazone has direct, historical randomized controlled trial evidence specifically in inflammatory spondylopathy (ankylosing spondylitis and psoriatic arthritis), with efficacy comparable to indomethacin established in two RCTs. The mechanistic rationale (COX inhibition as NSAID first-line therapy for AS) is unambiguous. However, the drug's market withdrawal history due to GI toxicity and warfarin interaction creates a high evidentiary bar for any repurposing or market re-entry pathway — these safety concerns must be formally re-assessed against contemporary standards and currently available alternatives.

**To proceed, the following is needed:**
- **Safety re-evaluation package:** Full GI toxicity, renal toxicity, and warfarin DDI profile benchmarked against currently approved NSAIDs (naproxen, diclofenac, celecoxib) and AS biologics (TNF-α inhibitors, IL-17 inhibitors)
- **Regulatory pathway assessment:** Whether Saudi Arabia SFDA would consider a previously withdrawn compound for re-approval, compassionate use, or named-patient access
- **MOA documentation:** Formal DrugBank record retrieval to confirm COX selectivity profile (COX-1 vs COX-2 ratio) and uricosuric mechanism
- **Unmet need analysis:** Whether a clinical scenario exists where azapropazone would offer advantages over currently available and safer NSAID alternatives — particularly in gout complicating AS, given the uricosuric property
- **Updated PK/PD data** and contemporary monitoring protocol design if clinical re-evaluation is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

