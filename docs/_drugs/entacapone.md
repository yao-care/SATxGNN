---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
---

# Entacapone
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

# Entacapone: From Parkinson's Disease to Lewy Body Dementia

## One-Sentence Summary

> Entacapone is a peripheral COMT (catechol-O-methyltransferase) inhibitor used as adjunct therapy to levodopa/carbidopa in **Parkinson's disease**, extending the duration of dopaminergic response.
> Across 10 TxGNN-predicted indications for this molecule, the strongest candidate is **Lewy Body Dementia**, supported by **1 early-phase clinical trial** and **3 publications**, though none directly test entacapone's efficacy in this population.
> Overall evidence remains preclinical/mechanistic (**L3 at best**), and a Blocking data gap on package-insert safety information prevents formal safety screening — the recommended decision is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (adjunct to levodopa/carbidopa) — based on known pharmacology; formal regulatory indication text and MOA record are a data gap (DG002) |
| Predicted New Indication | Lewy Body Dementia (best-evidenced of 10 candidates screened; see note below) |
| TxGNN Prediction Score | 99.25% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

**Important note on indication selection:** TxGNN's single highest-ranked prediction for entacapone was *PLA2G6-associated neurodegeneration* (score 99.76%), but the model's own rationale explicitly states this has **no mechanistic linkage and no supporting trials or literature** — it is a pure embedding-similarity artifact. Of the 10 predicted indications reviewed, only two reached decision-stage **S1 ("Research Question")**: *Lewy Body Dementia* (L3, has real trial/literature evidence) and *paralysis agitans, juvenile, of Hunt* (L4, mechanistically strong but with zero direct evidence). This report features Lewy Body Dementia as the headline candidate because it is the only one with actual empirical support; the full screening results are summarized below.

### All Screened Indications (Ranked by TxGNN Score)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | PLA2G6-associated neurodegeneration | 99.76% | L5 | S0 | Hold |
| 2 | Rasmussen subacute encephalitis | 99.73% | L5 | S0 | Hold |
| 3 | Myelitis | 99.63% | L5 | S0 | Hold |
| 4 | Paralysis agitans, juvenile, of Hunt (early-onset Parkinson's) | 99.60% | L4 | S1 | Research Question |
| 5 | Transaldolase deficiency | 99.43% | L5 | S0 | Hold |
| 6 | Lethal infantile mitochondrial myopathy | 99.28% | L5 | S0 | Hold |
| 7 | **Lewy Body Dementia** | 99.25% | L3 | S1 | Research Question |
| 8 | Fructose-1,6-bisphosphatase deficiency | 99.22% | L5 | S0 | Hold |
| 9 | Polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 99.06% | L5 | S0 | Hold |
| 10 | Progressive supranuclear palsy-corticobasal syndrome | 99.04% | L4 | S0 | Hold |

Ranks 1, 2, 3, 5, 6, 8, and 9 (7 of 10 candidates) have no clinical trials, no literature, and no plausible mechanistic link to entacapone's known pharmacology — these are model-similarity artifacts and are not discussed further.

---

## Why is This Prediction Reasonable?

Currently, detailed formal mechanism-of-action documentation is not available in this evidence pack (data gap DG002). Based on known pharmacology, entacapone is a peripheral, reversible COMT inhibitor used as an adjunct to levodopa/carbidopa in Parkinson's disease — it blocks peripheral metabolism of levodopa, prolonging its central dopaminergic effect.

Lewy Body Dementia (LBD) and Parkinson's disease sit on the same pathological spectrum: both are alpha-synucleinopathies, characterized by aggregation of α-synuclein in neurons and progressive nigrostriatal dopaminergic neuron loss. Many LBD patients develop parkinsonian motor symptoms and are, in clinical practice, treated with levodopa (often combined with a COMT inhibitor such as entacapone) to manage these symptoms. This shared pathophysiology is the basis of the TxGNN prediction.

Mechanistically, the supporting literature strengthens this link at two levels: PMID 23913715 directly tested antiparkinsonian agents' effects on α-synuclein oligomer formation in vitro, providing mechanism-level evidence relevant to disease-modifying potential; PMID 39259788 used iPSC-derived cortical organoids to model Lewy body pathology, offering preclinical biological context. The one registered trial (NCT04246437) does not test entacapone directly — it is an [18F]F-DOPA imaging study in autonomic failure patients — but it establishes that dopaminergic pathway imaging in synucleinopathy populations is an active area of investigation. Notably, none of this evidence directly evaluates entacapone's efficacy in LBD; all current support is indirect (shared disease mechanism, drug-class effects, or imaging methodology in adjacent populations), which is why the evidence level remains L3 rather than higher.

The secondary candidate, "paralysis agitans, juvenile, of Hunt," is an archaic term for juvenile/early-onset Parkinson's disease — essentially the same disease entity for which entacapone's use is already well established. Its mechanistic plausibility is arguably higher than LBD's, but zero direct trials or literature exist for this specific naming, so it remains an unverified extrapolation (L4) pending clinician input on pediatric/early-onset dosing safety.

---

## Clinical Trial Evidence

*(For Lewy Body Dementia — the featured candidate)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04246437](https://clinicaltrials.gov/study/NCT04246437) | Phase 1 | Recruiting | 40 | [18F]F-DOPA imaging study characterizing dopaminergic pathway integrity in patients with autonomic failure/synucleinopathies (Parkinson's disease, Multiple System Atrophy, Dementia with Lewy Bodies). Not an entacapone-interventional trial; provides background imaging context for the alpha-synucleinopathy spectrum. Graded "C" relevance — indirect. |

No entacapone-interventional trials for Lewy Body Dementia are currently registered.

---

## Literature Evidence

*(For Lewy Body Dementia — the featured candidate)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23913715](https://pubmed.ncbi.nlm.nih.gov/23913715/) | 2013 | In vitro mechanistic study | Journal of Neuroscience Research | Examined effects of antiparkinsonian agents on β-amyloid and α-synuclein oligomer formation in vitro — direct mechanism-level relevance to LBD pathology. |
| [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) | 2024 | Preclinical (iPSC model) | Science Advances | Modeled Lewy body disease using SNCA-triplication iPSC-derived cortical organoids to identify candidate therapeutic drugs. |
| [11268898](https://pubmed.ncbi.nlm.nih.gov/11268898/) | 2001 | Review | Presse Médicale | General review of Parkinson's disease; background reference only, no LBD- or entacapone-specific data (abstract not available). |

---

## Saudi Arabia Market Information

Entacapone currently has **no registered product license and is not marketed** in Saudi Arabia (0 authorizations on file). No dosage form, brand name, or approved indication text is available from the regulatory dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: this is a Blocking data gap — DG001 — not merely an absence of findings. Key warnings, contraindications, and drug-drug interaction data could not be retrieved from any source, which by itself is sufficient to prevent this candidate from advancing past initial safety screening, independent of the indication-level evidence discussed above.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No predicted indication for entacapone currently has direct clinical trial or controlled-study evidence of efficacy — the best-supported candidate (Lewy Body Dementia) rests on shared-mechanism and preclinical data only (L3), and a Blocking gap in basic package-insert safety data (DG001) prevents even a preliminary safety assessment. The drug is also not currently marketed in Saudi Arabia, removing any existing local safety/utilization track record to draw on.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications, DDI) — Blocking gap, must be resolved before any S1→S2 progression
- Formal DrugBank mechanism-of-action and original-indication record for entacapone
- If pursuing Lewy Body Dementia or early-onset Parkinson's further: a targeted literature/trial search specifically combining "entacapone" with these terms (rather than relying on general antiparkinsonian-agent studies), and clinical input on dosing/safety in early-onset or dementia populations
- Re-screening of the 7 lowest-evidence candidates (ranks 1, 2, 3, 5, 6, 8, 9) is not recommended — they show no mechanistic or empirical support and should remain deprioritized unless new evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

