---
layout: default
title: Pirfenidone
parent: 僅模型預測 (L5)
nav_order: 498
evidence_level: L5
indication_count: 10
---

# Pirfenidone
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

# Pirfenidone: From Idiopathic Pulmonary Fibrosis to Fibroblastic Neoplasm

## One-Sentence Summary

Pirfenidone is an antifibrotic agent generally known for treating idiopathic pulmonary fibrosis (IPF) by inhibiting TGF-β1-driven fibroblast proliferation and collagen synthesis — though this evidence pack itself has a data gap for the drug's original indication and MOA. TxGNN's top 10 predictions for this drug are dominated by fibrous- and mast-cell-tumor names, but only **fibroblastic neoplasm** (rank 9) has any supporting literature — **6 publications, 0 clinical trials** — and that literature includes two case reports of sarcoma/dermatofibroma worsening after pirfenidone exposure. The other 9 top-ranked predictions, including the #1-scored "extracutaneous mastocytoma," have **zero** clinical trials or publications and are explicitly flagged in the evidence pack as likely knowledge-graph noise.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (data gap). Commonly known (external knowledge, not from this pack): idiopathic pulmonary fibrosis (IPF) |
| Predicted New Indication | Fibroblastic neoplasm *(rank 9/10 — see note below on selection)* |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L4 (preclinical / mechanistic studies only) |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

**Note on prediction selection:** The evidence pack's own top-ranked hit (extracutaneous mastocytoma, score 99.71%) has zero trials, zero publications, and its own mechanistic-rationale field states it is "judged to be knowledge-graph noise." Presenting it as the headline finding would misrepresent the evidence. Fibroblastic neoplasm is the only one of the 10 predictions with any literature support, so it is used here as the substantive candidate; all other predictions are summarized separately below.

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is not available in this evidence pack (data gap). Based on the literature retrieved for this drug, pirfenidone is described as inhibiting TGF-β1, PDGF, and EGF/FGF-driven fibroblast proliferation and collagen synthesis — the mechanism underlying its established antifibrotic use. TxGNN's prediction cluster (fibrosarcoma variants, dermatofibrosarcoma protuberans, fibroblastic neoplasm) plausibly reflects this same TGF-β/fibroblast-proliferation signal in the knowledge graph, since these entities are all fibroblast-lineage.

The mechanistic plausibility is real but narrow: it applies best to **benign fibroproliferative disease** (e.g., Dupuytren's contracture, where in vitro studies below show PFD blocking TGF-β1-mediated myofibroblast activity), not to **neoplastic/malignant fibrous tumors**. Extrapolating an anti-proliferative mechanism from benign fibrosis to cancer is not automatically valid — malignant transformation involves additional oncogenic drivers that a TGF-β-inhibition mechanism does not obviously address, and as the safety literature below shows, the opposite effect (tumor emergence/aggravation) has been observed clinically.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12907346](https://pubmed.ncbi.nlm.nih.gov/12907346/) | 2003 | Pilot study (desmoid tumor; drug identity as pirfenidone needs verification) | Am J Gastroenterol | Pilot evaluation of pirfenidone in desmoid tumors (FAP patients); described as blocking TGF-β1, PDGF, EGF, FGF signaling |
| [27835939](https://pubmed.ncbi.nlm.nih.gov/27835939/) | 2016 | In vitro | BMC Musculoskelet Disord | Pirfenidone inhibits TGF-β1-mediated myofibroblast activity in Dupuytren's disease-derived fibroblasts |
| [30927912](https://pubmed.ncbi.nlm.nih.gov/30927912/) | 2019 | In vitro (mechanistic) | BMC Musculoskelet Disord | Pirfenidone affects TGF-β1-stimulated non-SMAD signaling in Dupuytren's disease fibroblasts |
| [35129055](https://pubmed.ncbi.nlm.nih.gov/35129055/) | 2022 | Preclinical/translational | Pharm Dev Technol | Local injectable pirfenidone delivery proposed to prevent Dupuytren's nodule-to-cord progression |
| [29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/) | 2018 | Case report — **adverse safety signal** | The Permanente Journal | Undifferentiated pleomorphic sarcoma diagnosed after pirfenidone use for IPF |
| [32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/) | 2020 | Case report — **adverse safety signal** | Rheumatology (Oxford) | Multiple eruptive dermatofibromas aggravated by mycophenolate mofetil + pirfenidone in systemic sclerosis |

## Saudi Arabia Market Information

Pirfenidone has **no registered authorizations** and is **not marketed** in Saudi Arabia per this evidence pack (0 licenses).

## Safety Considerations

- **Formal safety data (warnings, contraindications, DDI):** not available in this evidence pack — TFDA/manufacturer package insert has not been retrieved (flagged as a Blocking data gap, DG001). Please refer to the package insert for safety information.
- **Literature-derived safety signal (not from the formal safety fields, but material to this indication):** two case reports directly relevant to the fibroblastic-neoplasm hypothesis describe (1) an undifferentiated pleomorphic sarcoma diagnosed after pirfenidone treatment, and (2) worsening of existing dermatofibromas under pirfenidone co-therapy. Both run counter to the repurposing rationale and should be treated as a safety concern, not just an evidence gap.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial evidence exists for any of the 10 TxGNN-predicted indications. The single indication with any literature support (fibroblastic neoplasm) is backed only by in vitro/preclinical mechanistic studies (L4) plus two case reports describing tumor emergence or aggravation after pirfenidone exposure — evidence that argues against, not for, pursuing this indication. The remaining 9 predictions, including the top-ranked score, have no clinical or literature evidence at all and are assessed as likely graph artifacts.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed DrugBank mechanism-of-action data (DG002)
- Verification that the 2003 desmoid-tumor pilot study used pirfenidone (brand "Deskar") and not a related compound
- If this indication is still considered, a dedicated preclinical tumor-model study addressing the sarcoma/dermatofibroma-aggravation signal before any clinical exploration
- Independent mechanistic review of the 9 evidence-free predictions before treating any of them as viable leads
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

