---
layout: default
title: Hyoscyamine
parent: 僅模型預測 (L5)
nav_order: 314
evidence_level: L5
indication_count: 1
---

# Hyoscyamine
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

# Hyoscyamine: From Antispasmodic Use to Gastroduodenitis

## One-Sentence Summary

Hyoscyamine is a muscarinic acetylcholine receptor antagonist (antispasmodic) commonly used for gastrointestinal and genitourinary smooth muscle spasm; its specific Saudi-approved indication text is not available because the drug is currently not marketed in Saudi Arabia. The TxGNN model predicts it may be effective for **Gastroduodenitis**, but this is currently supported by **0 clinical trials** and only **1 tangentially related publication**, so the evidence base is essentially prediction-only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the Saudi regulatory dataset (drug not marketed); generally known as a GI/GU antispasmodic |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for hyoscyamine in this Evidence Pack (DrugBank MOA query returned a data gap). Based on general pharmacological knowledge, hyoscyamine is a muscarinic acetylcholine receptor antagonist (anticholinergic/antispasmodic) that reduces gastrointestinal smooth muscle spasm and secretion.

The predicted new indication, gastroduodenitis, involves gastric/duodenal mucosal inflammation (e.g., from H. pylori infection or other irritant causes) that is often accompanied by spasmodic abdominal pain. Hyoscyamine's antispasmodic action could theoretically relieve the pain component of gastroduodenitis, but this is a symptomatic/mechanistic inference rather than evidence of a disease-modifying effect on the underlying mucosal inflammation itself.

The single retrieved publication (a 2000 review on endoscopy premedication and sedation practice) does not directly address hyoscyamine's efficacy in gastroduodenitis — it is only broadly related to gastrointestinal endoscopic procedures. Combined with the absence of any clinical trials, the prediction currently rests on TxGNN's model score and a plausible but unproven mechanistic rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10696836](https://pubmed.ncbi.nlm.nih.gov/10696836/) | 2000 | Review | Endoscopy | General review of endoscopy premedication and IV sedation practice (e.g., propofol use); does not specifically evaluate hyoscyamine in gastroduodenitis |

## Saudi Arabia Market Information

Hyoscyamine is currently **not marketed** in Saudi Arabia (0 authorizations on record), so no product/authorization data is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is currently supported only by a TxGNN model score and a plausible but unconfirmed mechanistic rationale (L5, evidence stage S0) — there are no clinical trials and the single literature hit is not directly relevant to hyoscyamine's use in gastroduodenitis. In addition, TFDA package insert warnings/contraindications are a **blocking** data gap that prevents even a preliminary safety assessment (S1).

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) to unblock the S1 safety review
- Confirmed mechanism of action (MOA) data from DrugBank
- Confirmed original approved indication text (currently absent, as the drug is not marketed in Saudi Arabia)
- Targeted clinical or preclinical evidence directly evaluating hyoscyamine (or antispasmodics of its class) in gastroduodenitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

