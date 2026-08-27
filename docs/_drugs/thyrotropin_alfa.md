---
layout: default
title: Thyrotropin Alfa
parent: 僅模型預測 (L5)
nav_order: 616
evidence_level: L5
indication_count: 10
---

# Thyrotropin Alfa
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

# Thyrotropin Alfa: From No Registered Local Indication to Migraine Disorder

## One-Sentence Summary

Thyrotropin alfa (rhTSH) is not currently marketed in this jurisdiction, and no original approved indication or license data is on file for it locally.
The TxGNN model predicts it may be effective for **Migraine Disorder**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure computational signal with no corroborating real-world evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no local license or approved-indication record on file (drug not marketed) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for thyrotropin alfa is not available in the current dataset (data gap DG002). Based on other information captured in this evidence pack, thyrotropin alfa is a recombinant human thyroid-stimulating hormone (rhTSH) analogue whose known pharmacology is to stimulate thyroid follicular cells to synthesize and release thyroid hormone.

No original approved indication is on record locally (0 licenses, market status "未上市"), so no relationship between an original indication and migraine can be established from local regulatory data.

Importantly, the evidence pack's own rationale for this prediction states there is **no known direct physiological mechanism** linking TSH signaling to migraine pathophysiology. The high TxGNN score (99.98%) appears to reflect knowledge-graph embedding similarity rather than a biologically grounded hypothesis, and should be treated as a pure hypothesis pending independent validation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

This product is not currently marketed in this jurisdiction — 0 authorizations are on file, so no product/authorization table is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (migraine disorder, L5) has zero clinical trial or literature support and no established mechanistic rationale — it is a model-only signal. Notably, even the pack's best-evidenced candidate (hyperthyroidism, rank 10, L4) is mechanistically contradictory — rhTSH would be expected to stimulate rather than suppress thyroid hormone release — and its supporting literature discusses interferon-alfa–induced thyroid dysfunction, a different drug entity, suggesting a likely knowledge-graph false-positive rather than genuine repurposing evidence. There is currently no candidate in this set that meets a bar for further investment.

**To proceed, the following is needed:**
- Original indication and mechanism-of-action data for thyrotropin alfa (DrugBank/registration source)
- TFDA/local package insert warnings and contraindications (blocking gap DG001) before any S1 safety evaluation can begin
- Independent mechanistic or preclinical rationale for a TSH–migraine link before further evidence collection is warranted
- Verification of the hyperthyroidism literature set to rule out drug-entity confusion (interferon-alfa vs. thyrotropin alfa) before treating it as supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

