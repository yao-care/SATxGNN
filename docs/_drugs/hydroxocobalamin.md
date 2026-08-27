---
layout: default
title: Hydroxocobalamin
parent: 僅模型預測 (L5)
nav_order: 311
evidence_level: L5
indication_count: 2
---

# Hydroxocobalamin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Hydroxocobalamin: From Cyanide Poisoning / Vasoplegic Shock to Esophageal Varices with Bleeding

## One-Sentence Summary

> Hydroxocobalamin is a vitamin B12 precursor whose established clinical uses are cyanide poisoning antidote and nitric oxide (NO) scavenging in vasoplegic shock; it is not currently marketed in Taiwan.
> The TxGNN model predicts it may be effective for **Esophageal Varices with Bleeding**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-score-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Taiwan (no licenses on file); known clinical uses are cyanide poisoning antidote and NO-scavenging for vasoplegic shock |
| Predicted New Indication | Esophageal Varices with Bleeding |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (original_moa is a data gap, and no Taiwan license/indication record exists for this drug). Based on the known pharmacology captured in this evidence pack, hydroxocobalamin's two established clinical mechanisms are (1) binding cyanide ions to form cyanocobalamin (cyanide detoxification) and (2) scavenging nitric oxide, which is used therapeutically to raise blood pressure in vasoplegic shock.

The rationale for the esophageal varices prediction rests entirely on this NO-scavenging mechanism: bleeding esophageal varices arise from portal hypertension, which is driven in part by NO-mediated splanchnic vasodilation. In theory, hydroxocobalamin's NO-scavenging effect could constrict splanchnic vasculature and lower portal pressure — a mechanistic direction analogous to established vasoactive agents such as terlipressin or octreotide.

However, this is a pharmacological inference only. No preclinical or clinical data link hydroxocobalamin to portal hypertension or variceal bleeding, and hydroxocobalamin's real-world use is limited to acute, short-duration dosing (cyanide poisoning, vasoplegic shock) — quite different from the acute-hemostasis-then-secondary-prophylaxis pattern needed for variceal disease. (TxGNN separately assigns an identical score to "esophageal varices without bleeding," rank 10996, which would require chronic dosing and has even weaker mechanistic support given the drug's short-term-use profile.) The mechanistic link should be regarded as low-strength until independent evidence emerges.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

Hydroxocobalamin is not marketed in Taiwan (0 authorizations on file); no product/license data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is evidence level L5 (model score only, no clinical trials, no literature, no preclinical data), and the drug has no Taiwan regulatory footprint or safety profile on file. There is nothing beyond a theoretical mechanistic argument to support advancing this candidate.

**To proceed, the following is needed:**
- TFDA package insert / label warnings and contraindications (currently blocking — DG001)
- Verified mechanism of action from DrugBank (currently data gap — DG002)
- Any preclinical or in-vivo evidence connecting NO-scavenging activity to portal pressure reduction
- Safety data for repeated/chronic dosing, since variceal disease management is not a single-dose scenario like cyanide poisoning
- Confirmation of whether this signal should be pursued given the identical, equally unsupported score on the related "without bleeding" indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

