---
layout: default
title: Gilteritinib
parent: 僅模型預測 (L5)
nav_order: 292
evidence_level: L5
indication_count: 1
---

# Gilteritinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Gilteritinib: From FLT3-Mutated Acute Myeloid Leukemia to Bulbar Polio

## One-Sentence Summary

Gilteritinib is a FLT3/AXL tyrosine kinase inhibitor whose established use is in FLT3-mutated acute myeloid leukemia (AML); it is not currently marketed in Saudi Arabia and no local approved-indication data exists. The TxGNN model assigns a 99.10% score to **Bulbar Polio** as a novel indication, but this direction is supported by **zero clinical trials** and **zero publications**, and the evidence pack's own mechanistic review flags the pairing as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | FLT3-mutated Acute Myeloid Leukemia (AML) — not locally registered in Saudi Arabia; no formal approved-indication text on file |
| Predicted New Indication | Bulbar polio |
| TxGNN Prediction Score | 99.10% |
| Evidence Level | L5 (model prediction only — no trials, no literature) |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (`original_moa`) is marked as a data gap and could not be retrieved from DrugBank in this pull. Based on the rationale text accompanying this prediction, gilteritinib is known to act as a FLT3/AXL tyrosine kinase inhibitor, approved for FLT3-mutated AML. AXL has been reported in some literature as playing a role in cell-entry mechanisms for certain enveloped viruses (e.g., Ebola, Dengue).

However, bulbar polio is caused by poliovirus, a picornavirus that enters motor neurons via the CD155 receptor — a pathway with no known connection to FLT3/AXL signaling. The evidence pack's own mechanistic assessment explicitly concludes that this pairing **lacks a credible biological basis**, and is more likely attributable to model-level noise or a spurious rare-disease pairing rather than a genuine repurposing signal.

**This prediction should be treated with skepticism rather than presented as a promising lead.** No clinical trials, ICTRP registrations, or PubMed literature were found linking gilteritinib to poliovirus-related disease (confirmed via three independent queries on 2026-04-21), which is consistent with the mechanistic implausibility noted above.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Gilteritinib is an antineoplastic agent (approved for FLT3-mutated AML), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FLT3/AXL tyrosine kinase inhibitor) — based on rationale text; formal DrugBank MOA/category data not yet retrieved |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 (model prediction only), with no clinical trials, ICTRP registrations, or literature support, and the pack's own mechanistic analysis assesses the FLT3/AXL–poliovirus pairing as biologically implausible, likely a false-positive signal. A blocking data gap on official (e.g., TFDA/label) warnings and contraindications also prevents this candidate from entering the S1 safety pre-screen stage.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): official package insert warnings/contraindications
- Resolve DG002: confirmed DrugBank MOA and drug category data
- Independent biological plausibility evidence (e.g., in vitro data on AXL's role, if any, in poliovirus/CD155-mediated neuronal entry) before further pursuit
- If no such evidence emerges, this candidate-indication pair should be deprioritized rather than advanced
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

