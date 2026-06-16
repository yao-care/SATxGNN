---
layout: default
title: Deoxycholic Acid
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 3
---

# Deoxycholic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Deoxycholic Acid: From Submental Fat Reduction to Autosomal Dominant Familial Hematuria-Retinal Arteriolar Tortuosity-Contractures Syndrome

## One-Sentence Summary

Deoxycholic acid (DCA) is a secondary bile acid approved in the United States, Canada, and Europe as an injectable fat-dissolving treatment for submental contouring (brand name Kybella/Belkyra), and is not currently registered in Saudi Arabia.
The TxGNN model predicts it may be effective for **Autosomal Dominant Familial Hematuria-Retinal Arteriolar Tortuosity-Contractures Syndrome**, an ultra-rare inherited collagen disorder,
with **no clinical trials and no supporting publications** currently available for this drug-disease pair — making this a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Submental fat reduction (Kybella/Belkyra; not registered in Saudi Arabia) |
| Predicted New Indication | Autosomal Dominant Familial Hematuria-Retinal Arteriolar Tortuosity-Contractures Syndrome |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for deoxycholic acid is not available in this evidence pack. Based on known pharmacological information, DCA is a secondary bile acid synthesised by gut bacteria from primary bile acids. It acts through two main mechanisms: (1) direct cytolytic disruption of adipocyte cell membranes (the basis of its cosmetic use), and (2) agonism at bile acid receptors FXR (farnesoid X receptor) and TGR5, which regulate metabolic, inflammatory, and fibrotic pathways across multiple organ systems.

The predicted disease — autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome (OMIM #141200) — is an ultra-rare inherited connective tissue disorder caused by mutations in *COL4A3* or *COL4A4* genes encoding type IV collagen α-chains of the glomerular and retinal basement membranes. The clinical triad of glomerular hematuria, retinal arteriolar tortuosity, and joint contractures reflects a structural failure of basement membrane scaffolding throughout the body.

There is no identified mechanistic link between DCA's FXR/TGR5 bile acid signalling and the COL4A3/COL4A4 collagen defects underlying this syndrome. The high TxGNN score (0.9949) almost certainly reflects indirect graph proximity in the biomedical knowledge graph — shared vascular and renal node neighbourhood — rather than genuine biological relevance. This is a well-recognised false-positive pattern for ultra-rare Mendelian structural protein diseases, where graph-based models capture phenotypic node proximity but not therapeutic actionability.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for this drug-disease pair.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Formal safety data (key warnings, contraindications, drug interactions) could not be retrieved for this evidence pack. The SFDA/TFDA package insert was not available for automated parsing (Data Gap DG001). DCA is known to be cytolytic at higher concentrations; injection-site necrosis and nerve injury are documented adverse effects for the approved injectable formulation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a numerically high TxGNN score (99.49%), the prediction lacks any supporting clinical, preclinical, or mechanistic evidence connecting deoxycholic acid to a collagen IV basement membrane disorder. The high score is best explained by knowledge graph topology artefact rather than biological plausibility, a pattern seen systematically with ultra-rare structural protein Mendelian diseases.

**Additional context — higher-priority repurposing candidate identified:**
Among the top-3 TxGNN predictions for this drug, **diabetic nephropathy (rank 3, score 99.32%, evidence level L4)** presents a far more compelling opportunity: DCA activates FXR and TGR5, both of which have demonstrated renoprotective effects in animal models of diabetic kidney disease (PMID 29089371, 26655953), and the structurally related bile acid UDCA has shown benefit in multiple preclinical diabetic nephropathy studies (PMID 26999661, 27193377, 22429686). Twenty supporting publications and a developed mechanistic rationale place this on a "Research Question" track rather than a full Hold.

**To proceed with any indication, the following is needed:**
- Drug MOA data from DrugBank (Data Gap DG002) — required to complete mechanistic reasoning
- Saudi Arabia package insert or label text (Data Gap DG001) — required for safety pre-screening
- For diabetic nephropathy specifically: a dedicated *in vivo* study using DCA directly (not UDCA/TUDCA) in a diabetic kidney model, to confirm class-effect validity before clinical translation
- Safety risk assessment for DCA's cytolytic properties relative to its therapeutic window in any systemic indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

