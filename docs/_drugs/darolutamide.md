---
layout: default
title: Darolutamide
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 3
---

# Darolutamide
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

# Darolutamide: From Prostate Cancer to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Darolutamide is an androgen receptor (AR) antagonist established for the treatment of castration-resistant prostate cancer.
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)** with a score of **99.11%**,
however, **no clinical trials and no published literature** currently support this direction — this prediction rests entirely on computational network analysis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (AR antagonist; no Taiwan TFDA record available) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 |
| Taiwan (TFDA) Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological classification, Darolutamide is a potent androgen receptor (AR) antagonist with minimal CNS penetration. Its efficacy in non-metastatic castration-resistant prostate cancer has been established in the pivotal ARAMIS Phase 3 trial.

The mechanistic rationale for HoFH is indirect but theoretically coherent. AR signaling is known to upregulate hepatic PCSK9 expression and simultaneously downregulate LDL receptor (LDLR) activity. In principle, AR antagonism could increase LDLR expression on hepatocyte surfaces and enhance LDL particle clearance from circulation — directly relevant to HoFH, a disease defined by severely impaired LDL clearance due to biallelic mutations in *LDLR*, *APOB*, or *PCSK9* genes.

However, this chain of reasoning has not been validated at any level — cellular, animal, or clinical. HoFH patients carry loss-of-function mutations that may render residual LDLR activity largely unresponsive to transcriptional upregulation signals. The TxGNN high score likely reflects topological proximity between the AR signaling network and lipid metabolism nodes in the knowledge graph, rather than a direct biological effect. The gap between network plausibility and clinical relevance remains very wide for this prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Darolutamide in Homozygous Familial Hypercholesterolemia.

---

## Literature Evidence

Currently no related literature available for Darolutamide in Homozygous Familial Hypercholesterolemia.

---

## Taiwan (TFDA) Market Information

Darolutamide has no approved marketing authorization in Taiwan (TFDA). No license records are available.

---

## Cytotoxicity

Darolutamide is an antineoplastic agent (indicated for prostate cancer). The following applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Androgen Receptor Antagonist (non-cytotoxic mechanism) |
| Myelosuppression Risk | Low (AR antagonists do not cause direct bone marrow suppression) |
| Emetogenicity Classification | Low (oral agent; minimal emetogenic potential per class) |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Standard oral oncology agent handling; no specialized cytotoxic precautions required |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score (99.11%), the mechanistic link between AR antagonism and HoFH is indirect, speculative, and unvalidated at any experimental level. With zero supporting clinical trials, zero published literature, and no preclinical data, the evidence level is L5 — model prediction only. HoFH also has a crowded approved-therapy landscape (statins, ezetimibe, PCSK9 inhibitors, lomitapide, evinacumab), making the differentiation hurdle significant.

**To proceed, the following is needed:**

- **Mechanistic proof-of-concept**: In vitro experiments in hepatocyte models (HepG2, primary human hepatocytes) or LDLR-deficient cell lines to quantify whether Darolutamide modulates LDLR surface expression or LDL uptake at clinically achievable concentrations
- **Animal validation**: Testing in LDLR-knockout or PCSK9 gain-of-function mouse models used as HoFH surrogates to confirm lipid-lowering effect in vivo
- **MOA and safety data**: Formal mechanism of action documentation and complete safety profile (currently absent from this evidence pack)
- **Differentiation rationale**: Given multiple approved HoFH therapies, a clinical unmet need analysis is required before committing to preclinical investment
- **Network hypothesis clarification**: Determine whether TxGNN's high score is driven by a true PCSK9/LDLR pathway signal or by non-specific AR–lipid metabolism graph adjacency
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

