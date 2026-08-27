---
layout: default
title: Salbutamol
parent: 僅模型預測 (L5)
nav_order: 564
evidence_level: L5
indication_count: 10
---

# Salbutamol
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

Using the report template from the system prompt (no additional skill needed — this is direct, fully-specified report generation from provided evidence pack). Note: `predicted_indications[0]` in this pack is **papillary conjunctivitis** (highest TxGNN score, rank 143), which is a pure L5/Hold prediction with zero trial/literature support — I'm following the template literally as specified.

# Salbutamol: From Bronchodilation (Asthma/COPD) to Papillary Conjunctivitis

## One-Sentence Summary

Salbutamol is a short-acting β2-adrenergic agonist bronchodilator; detailed original-indication and mechanism-of-action documentation for this market is currently a data gap (see DG001/DG002).
The TxGNN model predicts it may be effective for **Papillary Conjunctivitis**, its single highest-scoring prediction (99.99%),
but currently **0 clinical trials** and **0 publications** support this specific disease association.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no licensed indication text on file; MOA data gap — see DG001/DG002) |
| Predicted New Indication | Papillary Conjunctivitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity, DrugBank query pending). Based on known information, salbutamol is a short-acting β2-adrenoceptor agonist commonly used for reversible bronchospasm; its original indication text and regulatory documentation are not present in this evidence pack (DG001, Blocking severity — TFDA package insert not yet parsed), so no verifiable link between its established use and papillary conjunctivitis can be drawn at this time.

For papillary conjunctivitis specifically, the model's high score is not accompanied by any clinical trial or published literature — the TxGNN score stands alone, with no retrievable mechanistic or clinical evidence chain.

Notably, this same evidence pack contains a *related* ocular condition — atopic conjunctivitis (rank 8) — where two preclinical pharmacology studies are on file: salbutamol suppressed immediate allergic conjunctivitis in a guinea pig model (PMID 3666475), and topical β2-agonists showed anti-inflammatory activity in conjunctival tissue (PMID 2906082). Papillary conjunctivitis and atopic conjunctivitis are mechanistically adjacent (both involve conjunctival hypersensitivity/inflammation), so this indirect preclinical signal offers some biological plausibility — but it does not constitute direct evidence for papillary conjunctivitis itself, and no human trial in either condition exists.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Saudi Arabia Market Information

Salbutamol is not currently marketed in this jurisdiction (0 authorizations on file), so no product/authorization table is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests entirely on the TxGNN model score with no supporting clinical trials or literature for papillary conjunctivitis; per the evidence-level rubric this is L5 (model prediction only), which does not meet the bar for further development.

**To proceed, the following is needed:**
- TFDA/local package insert (warnings, contraindications) — currently Blocking (DG001)
- Mechanism-of-action data from DrugBank — currently High priority (DG002)
- Targeted preclinical or clinical evidence specifically in papillary conjunctivitis (the adjacent atopic conjunctivitis preclinical data, PMID 3666475 and PMID 2906082, could inform a hypothesis-generating study but is not substitute evidence)
- Consider that within this same evidence pack, **bronchitis** (rank 4, L2, decision stage S2, "Proceed with Guardrails") and **obstructive lung disease** (rank 10, L1, decision stage S3, "Proceed with Guardrails") have substantially stronger, mechanistically direct evidence and may be more actionable near-term repurposing candidates than papillary conjunctivitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

