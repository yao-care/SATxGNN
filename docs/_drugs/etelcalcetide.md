---
layout: default
title: Etelcalcetide
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 4
---

# Etelcalcetide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Etelcalcetide: From Secondary Hyperparathyroidism to Hyperphosphatemia

## One-Sentence Summary

Etelcalcetide is an intravenous calcimimetic used in the management of secondary hyperparathyroidism (SHPT) in hemodialysis patients with chronic kidney disease (CKD-MBD).
The TxGNN model predicts it may also be effective for **Hyperphosphatemia**,
with **1 clinical trial** and **3 publications** (including one RCT) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Secondary hyperparathyroidism (SHPT) in hemodialysis patients — based on known pharmacological class information; a formally documented approved-indication text was not available in this evidence pack (TFDA package insert parsing pending, see Blocking gap) |
| Predicted New Indication | Hyperphosphatemia |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation for etelcalcetide was not available in this evidence pack (High-severity gap, remediation pending via DrugBank API query). Based on established pharmacological knowledge, etelcalcetide is a calcimimetic that allosterically activates the calcium-sensing receptor (CaSR) on parathyroid chief cells, suppressing parathyroid hormone (PTH) secretion. This is the mechanism through which the drug is used clinically to control SHPT in dialysis patients.

Secondary hyperparathyroidism and hyperphosphatemia are both components of chronic kidney disease–mineral and bone disorder (CKD-MBD), a single interconnected pathophysiological syndrome. Suppressing PTH reduces osteoclast-mediated bone resorption, which in turn lowers the release of calcium and phosphate from bone into circulation. Phosphate lowering is therefore a recognized downstream pharmacodynamic effect of calcimimetics in the SHPT treatment context, rather than a speculative new mechanism — which supports the biological plausibility of the TxGNN prediction.

This mechanistic link is directly reflected in the supporting evidence: a completed trial evaluating etelcalcetide's effect on osteoclasts in CKD patients, and literature describing etelcalcetide's role in managing CKD-MBD abnormalities (including hyperphosphatemia) alongside PTH control. Taken together, the prediction is grounded in an established physiological pathway rather than an unexplained model association.

*Note on other predicted indications:* Three additional TxGNN candidates for this drug — esophageal varices with bleeding, esophageal varices without bleeding, and varicose disease — carry no supporting clinical trial or literature evidence (Evidence Level L5, Decision Stage S0, recommendation **Hold**). Their near-identical prediction scores and shared "varices/varicose" wording, combined with the absence of any known biological link between CaSR activation and venous wall integrity or portal pressure, suggest these are likely artifacts of semantic clustering in the model's disease embeddings rather than genuine pharmacological signals. They are not pursued further in this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03527511](https://clinicaltrials.gov/study/NCT03527511) | N/A | Completed | 21 | Evaluated the effect of active vitamin D plus etelcalcetide on osteoclasts in CKD patients; addresses CKD-MBD abnormalities including hypocalcemia, hyperphosphatemia, and hyperparathyroidism. Mechanistic study, not primarily designed with hyperphosphatemia as the endpoint. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33305109](https://pubmed.ncbi.nlm.nih.gov/33305109/) | 2020 | RCT | Kidney International Reports | The DUET trial — a prospective, randomized study of etelcalcetide in hemodialysis patients with SHPT, assessing control of CKD-MBD parameters. |
| [29440923](https://pubmed.ncbi.nlm.nih.gov/29440923/) | 2018 | Review | International Journal of Nephrology and Renovascular Disease | Reviews management of SHPT in hemodialysis, describing etelcalcetide's role in reducing PTH and its relationship to phosphate control alongside oral binders and vitamin D analogs. |
| [33211001](https://pubmed.ncbi.nlm.nih.gov/33211001/) | 2021 | Case Report | Clinical Nephrology | Describes a case of metastatic pulmonary calcification in a dialysis patient with hyperparathyroidism, illustrating downstream consequences of CKD-MBD mineral dysregulation. |

---

## Saudi Arabia Market Information

Etelcalcetide is currently **not marketed** in Saudi Arabia — no authorization records are available (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The prediction is supported by a coherent, well-established physiological pathway (PTH suppression → reduced bone resorption → lower serum phosphate) and by one completed RCT (DUET trial) plus a supportive mechanistic trial, yielding an L2 evidence level with a very high TxGNN score (99.42%). However, formal MOA documentation and TFDA/manufacturer safety labeling data are currently missing, including one Blocking-severity gap, so the candidate cannot yet clear a full safety pre-assessment (S1) and should proceed only under guardrails.

**To proceed, the following is needed:**
- TFDA package insert (warnings and contraindications) — Blocking data gap, requires PDF retrieval and parsing
- Formal mechanism-of-action documentation via DrugBank API query
- Drug-drug interaction (DDI) profile — current query returned no results
- Additional clinical data with hyperphosphatemia as a primary (rather than secondary/mechanistic) endpoint
- Route-of-administration compatibility assessment (currently marked pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

