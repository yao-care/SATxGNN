---
layout: default
title: Cabergoline
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 5
---

# Cabergoline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cabergoline: From Hyperprolactinemia/Prolactinoma to Pituitary Adenocarcinoma

## One-Sentence Summary

Cabergoline is a selective dopamine D2 receptor agonist established as the first-line medical treatment for hyperprolactinemia and prolactin-secreting pituitary adenomas (prolactinomas).
The TxGNN model predicts it may be effective for **Pituitary Adenocarcinoma** (malignant pituitary tumor with distant metastases), with **no registered clinical trials** and **3 case-report-level publications** providing only indirect supporting evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperprolactinemia / Prolactinoma (established clinical use; not approved in Saudi Arabia) |
| Predicted New Indication | Pituitary Adenocarcinoma |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cabergoline is a long-acting ergoline derivative that selectively activates dopamine D2 receptors expressed on pituitary adenohypophyseal cells—particularly lactotrophs (prolactin-producing cells). By stimulating D2 receptors, cabergoline suppresses prolactin secretion, inhibits tumor cell proliferation, and induces apoptosis, producing the clinically observed tumor shrinkage characteristic of prolactinoma treatment. Beyond this established mechanism, recent research has revealed additional anti-tumor pathways: cabergoline can trigger autophagy-mediated cell death, and in non-functioning pituitary adenomas the HTR2B receptor pathway may sensitize tumor cells to cabergoline treatment (PMID 38989697).

Pituitary adenocarcinoma is the rare malignant end of the pituitary tumor spectrum, defined strictly by the presence of craniospinal or systemic metastases, with fewer than 500 confirmed cases reported globally. Since pituitary adenocarcinoma arises from the same adenohypophyseal cell lineages as benign adenomas—which are the well-established targets of cabergoline's D2 agonism—the mechanistic extrapolation is biologically plausible. If malignant cells retain functional D2 receptor expression, the same anti-proliferative and pro-apoptotic pathways exploited in adenoma treatment could theoretically apply.

In practice, this extrapolation faces a major clinical hurdle: dopamine agonist resistance is common in pituitary carcinomas and may itself be a contributing factor in malignant transformation. D2 receptor expression tends to be lower or functionally impaired in carcinomas compared to adenomas. Scattered case reports document only transient or partial responses to cabergoline in confirmed pituitary carcinomas, with no sustained disease control demonstrated. The overall prognosis for pituitary carcinoma remains poor regardless of treatment, and the distinction from the benign adenoma—where cabergoline has well-established efficacy—must be maintained rigorously.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for pituitary adenocarcinoma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [41760078](https://pubmed.ncbi.nlm.nih.gov/41760078/) | 2026 | Case Report | Medicine | MEN1 patient with atypical multi-gland neoplasia and a MEN1 variant of uncertain pathogenicity; pituitary tumor was part of the presentation, illustrating the overlap of hereditary neoplasia syndromes with pituitary malignancy risk—not a direct cabergoline efficacy study |
| [20497940](https://pubmed.ncbi.nlm.nih.gov/20497940/) | 2010 | Case Report | Endocrine Practice | Patient with ectopic ACTH hypersecretion managed long-term with octreotide or cabergoline following bilateral adrenalectomy; cabergoline demonstrated utility in corticotroph-related ectopic secretion, an adjacent indication to corticotroph carcinoma, though ectopic ACTH is not pituitary adenocarcinoma |
| [33569966](https://pubmed.ncbi.nlm.nih.gov/33569966/) | 2021 | Case Report | Rev Esp Enferm Dig | Patient with known pituitary adenoma receiving cabergoline developed duodenal lymphangiectasias as the first presenting sign of pancreatic adenocarcinoma; cabergoline was incidental background therapy and was not being evaluated as anticancer treatment |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Pituitary adenocarcinoma is an ultra-rare condition (globally <500 reported cases), and the available evidence for cabergoline consists solely of incidental case observations rather than any direct therapeutic studies. Frequent dopamine agonist resistance in carcinomas—often more pronounced than in adenomas—and the absence of D2 receptor expression data in malignant tissue further weaken the immediate clinical case.

**To proceed, the following is needed:**
- **Systematic case registry data:** Collection of confirmed pituitary carcinoma cases treated with dopamine agonists to establish a minimal evidence base before any prospective study design
- **D2 receptor expression profiling:** Tumor tissue studies to confirm whether pituitary carcinomas retain sufficient D2 receptor density and function to be therapeutically targeted by cabergoline
- **MOA documentation:** Formal characterization of cabergoline's mechanism of action (currently a data gap) is required to support any regulatory or clinical development rationale
- **Safety profile review:** Package insert analysis and Saudi Arabia-specific safety assessment, including evaluation of the known long-term valvular regurgitation risk
- **Broaden evaluation scope:** The broader **pituitary cancer** category (TxGNN Rank 3, evidence level L2, 20 registered clinical trials including one completed Phase 3 RCT and a 880-patient multi-center trial) represents a substantially more clinically actionable target and warrants a separate, higher-priority evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

