---
layout: default
title: Lorazepam
parent: 僅模型預測 (L5)
nav_order: 386
evidence_level: L5
indication_count: 10
---

# Lorazepam
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

# Lorazepam: From Benzodiazepine Anxiolytic/Sedative Use to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Lorazepam is a classic benzodiazepine used clinically for anxiety, sedation, and seizure control (specific Taiwan-approved indication text is not on file, as the drug is currently not marketed here). The TxGNN model's top-ranked prediction for this drug is **Trigeminal Nerve Neoplasm**, but this candidate currently has **0 clinical trials** and **0 publications** supporting it, and the model's own rationale flags a lack of biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — drug is not marketed in Taiwan and no approved indication text is recorded |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (drug-level MOA is flagged as a data gap). Based on well-established pharmacology, Lorazepam is a benzodiazepine that acts as a positive allosteric modulator of the GABA-A receptor, producing central nervous system depression, anxiolysis, sedation, and anticonvulsant effects.

There is no known mechanistic pathway connecting GABA-A receptor modulation to trigeminal nerve neoplasm pathology, which involves neural/Schwann cell proliferation and tumor microenvironment processes unrelated to GABAergic signaling. The evidence pack's own repurposing rationale is explicit on this point: the high TxGNN score appears to reflect network-topology similarity rather than biological plausibility, and no clinical trials or literature exist to bridge this gap.

For context, this drug's other TxGNN-ranked candidates include several with much stronger support — notably **insomnia** (rank 2, evidence level L2, 23 clinical trials and 18 publications identified, including lorazepam-specific RCTs), which reflects a well-known, already-established clinical use of benzodiazepines rather than a novel repurposing hypothesis. If the goal is to identify an actionable near-term candidate for this drug, that indication warrants separate evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Lorazepam is not currently marketed in Taiwan — there are no product licenses on file (0 total authorizations), so no dosage form or approved-indication data can be reported.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack — TFDA package insert retrieval is flagged as a blocking data gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature evidence, and the drug's core pharmacology (GABA-A modulation → CNS depression) has no established mechanistic link to trigeminal nerve tumor pathology. The prediction score alone does not justify advancement.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a blocking data gap for any safety screening
- Confirmed mechanism of action (MOA) data from DrugBank — currently a data gap
- Preclinical or mechanistic studies establishing a plausible pathway between GABAergic modulation and trigeminal nerve neoplasm before further investment
- Alternatively, consider re-scoping this evaluation to the drug's rank-2 predicted indication (insomnia), which has substantially stronger clinical trial and literature support (L2, "Proceed with Guardrails")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

