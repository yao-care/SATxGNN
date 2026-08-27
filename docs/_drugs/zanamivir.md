---
layout: default
title: Zanamivir
parent: 僅模型預測 (L5)
nav_order: 672
evidence_level: L5
indication_count: 2
---

# Zanamivir
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

# Zanamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

Zanamivir is a neuraminidase inhibitor originally used to treat influenza A/B infection by blocking release of viral particles from infected cells. The TxGNN model predicts it may be effective for **Pyelonephritis**, with a **99.84%** prediction score but **zero supporting clinical trials and zero supporting literature**. Both the model's own linked rationale and the evidence search results indicate this is a low-confidence, purely graph-based association.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record in local regulatory licenses (drug not marketed); known mechanistically as an influenza antiviral |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Zanamivir is a neuraminidase inhibitor. Its mechanism of action is limited to blocking the neuraminidase enzyme on the surface of influenza virus particles, which prevents newly formed virions from being released from infected respiratory cells. This is a narrow, virus-specific antiviral mechanism.

Pyelonephritis is a bacterial infection of the renal pelvis, most commonly caused by gram-negative organisms such as *E. coli* ascending the urinary tract. There is no known biochemical or pharmacological pathway connecting neuraminidase inhibition to bacterial urinary tract pathogenesis.

Based on the evidence pack's own assessment, this prediction should be treated with caution: the high TxGNN score (0.9984) reflects a graph-embedding link with no corroborating clinical trial or literature evidence, and cannot currently be distinguished from knowledge-graph noise. No formal mechanism-of-action record is available at the drug level (data gap), which further limits confidence in this repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Zanamivir currently holds no marketing authorization in Saudi Arabia (market status: Not Marketed; 0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Additional Predicted Indication (Lower Rank, Low Confidence)

A second candidate indication, **disorder of tyrosine metabolism**, was also predicted (TxGNN score 99.02%, rank 13262). Three literature records were retrieved, but on review none are relevant to tyrosine metabolism: all three concern oseltamivir resistance mutations (H275Y/H274Y/N294S) and neuraminidase inhibition assay methodology in influenza virology. This appears to be a keyword/entity mismatch rather than genuine supporting evidence, and it is not recommended for further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications rely solely on TxGNN's graph score (L5, decision stage S0) with no clinical trial or relevant literature support, and no plausible mechanistic link has been established. The drug is also not currently marketed in Saudi Arabia, removing any near-term access pathway.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (currently a Blocking data gap — required before any S1 safety screening)
- Formal drug-level mechanism-of-action documentation from DrugBank (High-severity data gap)
- Targeted literature and preclinical search specifically on zanamivir/neuraminidase activity in urinary tract or renal infection models, to confirm or rule out mechanistic plausibility
- Reassessment of local regulatory pathway given current "not marketed" status in Saudi Arabia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

