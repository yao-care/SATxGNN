---
layout: default
title: Acarbose
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 9
---

# Acarbose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Acarbose: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Acarbose is an intestinal α-glucosidase inhibitor used to manage postprandial blood glucose in type 2 diabetes mellitus by slowing carbohydrate absorption in the small intestine.
The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome**, a rare focal variant of Stiff Person Spectrum Disorder;
however, **no clinical trials** and **no publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (postprandial blood glucose management) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory record. Based on established pharmacology, acarbose is an intestinal α-glucosidase inhibitor that competitively and reversibly blocks the enzymes responsible for breaking down oligosaccharides and disaccharides into absorbable monosaccharides in the gut brush border. This delays carbohydrate absorption and blunts postprandial glucose excursions. Acarbose has no known activity on the central nervous system, GABAergic neurotransmission, or immune modulation.

Focal Stiff Limb Syndrome is a focal variant of Stiff Person Spectrum Disorder, characterized by pathological anti-GAD65 antibody-mediated dysfunction of GABAergic inhibitory interneurons, leading to segmental muscle rigidity and spasms. The postulated TxGNN graph reasoning path runs through a shared molecular node: GAD65 (glutamic acid decarboxylase 65) is a target autoantigen in both Stiff Person Spectrum Disorder and Type 1 Diabetes Mellitus, creating an indirect graph linkage through autoimmune co-occurrence. The model likely traverses the path: Acarbose → blood glucose regulation → GAD65 autoimmunity → Focal Stiff Limb Syndrome.

However, acarbose acts solely on intestinal carbohydrate absorption and has no established pharmacological effect on GAD65 autoantibody production, GABAergic neurotransmission, or neuroimmune regulation. The mechanistic chain is indirect, multi-hop, and entirely unsupported by experimental or clinical data. This prediction most likely represents a non-specific graph traversal artifact rather than a biologically meaningful drug-disease relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, preclinical, or mechanistic evidence connecting acarbose to focal stiff limb syndrome; the TxGNN prediction is classified as L5 (model prediction only) and is most likely an artifact of indirect GAD65 graph linkage, with no clinically meaningful basis for further development in this indication.

**To proceed, the following is needed:**
- Basic preclinical studies (in vitro / in vivo) to explore whether α-glucosidase inhibition exerts any effect on GABAergic function or anti-GAD65 autoimmunity
- Complete MOA data from DrugBank (DG002) to fill the mechanistic gap and enable proper target overlap analysis
- Package insert safety data (DG001) from TFDA or equivalent authority to enable full contraindication and warning review
- Consideration of higher-ranked predictions with stronger mechanistic plausibility (e.g., Rank 9 — Pancreatic Agenesis, Evidence Level L4) for prioritized follow-up
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

