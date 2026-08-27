---
layout: default
title: Potassium Acetate
parent: 僅模型預測 (L5)
nav_order: 507
evidence_level: L5
indication_count: 1
---

# Potassium Acetate
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

# Potassium Acetate: From Electrolyte/Alkalinizing Agent to Renal Tubular Acidosis

## One-Sentence Summary

Potassium acetate is a potassium salt used clinically as an electrolyte replacement and alkalinizing agent, most commonly added to IV fluids or parenteral nutrition; no formal indication record exists in the current dataset. The TxGNN model predicts it may be effective for **Renal Tubular Acidosis (RTA)**, with **0 registered clinical trials** and **9 publications** currently identified — most of which are case reports or preclinical studies, and several describe a physiologically opposite RTA subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally documented — general use as electrolyte/alkalinizing agent (IV fluids, parenteral nutrition) |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on known pharmacology, potassium acetate supplies potassium ions and acetate, which the liver converts to bicarbonate — giving it a dual role as a potassium replacement and an alkalinizing agent. This is the same basic mechanism used in already-established RTA therapies such as potassium citrate and potassium bicarbonate.

Hypokalemic RTA (Type 1 distal and Type 2 proximal) is defined by concurrent hypokalemia and normal-anion-gap metabolic acidosis, so combined potassium-and-alkali replacement is mechanistically plausible and consistent with current standard-of-care agents for these subtypes.

However, the supporting literature set is mechanistically mixed: several of the identified papers (PMIDs 4015282, 2973296, 637641, 3398981, 6758113) describe **hyperkalemic** Type 4 RTA (hyporeninemic hypoaldosteronism, Gordon syndrome), a subtype where potassium supplementation is contraindicated rather than indicated. This subtype heterogeneity means the evidence base does not cleanly support the prediction without RTA-subtype stratification, and should be treated as a material caveat rather than confirmatory evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33771116](https://pubmed.ncbi.nlm.nih.gov/33771116/) | 2021 | RCT | BMC Nephrology | Randomized trial comparing 0.9% NaCl vs. Plasma-Lyte on kidney injury biomarkers and tubular transport proteins after hip replacement; isotonic saline linked to hyperchloremic acidosis risk relevant to chloride/acetate balance. |
| [6758113](https://pubmed.ncbi.nlm.nih.gov/6758113/) | 1982 | Review | Schweizerische medizinische Wochenschrift | Review of hyporeninemic hypoaldosteronism as a cause of hyperkalemic, hyperchloremic acidosis (Type 4 RTA) — opposite-direction subtype, potassium supplementation not indicated. |
| [3398981](https://pubmed.ncbi.nlm.nih.gov/3398981/) | 1988 | Cohort/Clinical Study | Nephron | Case study showing hyperkalemia drives acidosis in hyporeninemic hypoaldosteronism; fludrocortisone (not potassium) corrected both hyperkalemia and acidosis. |
| [2973296](https://pubmed.ncbi.nlm.nih.gov/2973296/) | 1988 | Case Report/Review | Archives des maladies du coeur et des vaisseaux | Case of hyperkalemia with proximal tubular acidosis and normal renal function (Gordon syndrome / pseudohypoaldosteronism type II) — hyperkalemic subtype. |
| [37224266](https://pubmed.ncbi.nlm.nih.gov/37224266/) | 2023 | Case Report | Veterinary medicine and science | Transient distal RTA with hypokalemia and hyperchloremic metabolic acidosis after general anaesthesia in a dog — hypokalemic subtype consistent with predicted use. |
| [4015282](https://pubmed.ncbi.nlm.nih.gov/4015282/) | 1985 | Case Report | Archives of internal medicine | Hyperkalemic distal RTA combined with selective aldosterone deficiency in a patient with lead nephropathy; fludrocortisone did not resolve acidosis or potassium excretion. |
| [637641](https://pubmed.ncbi.nlm.nih.gov/637641/) | 1978 | Case Report | Archives of internal medicine | Familial hyperkalemia, hypertension, and hyporeninemia with a tubular potassium-handling defect — hyperkalemic subtype. |
| [34442051](https://pubmed.ncbi.nlm.nih.gov/34442051/) | 2021 | Case Report | Journal of clinical medicine | Patiromer-induced hypercalcemia, metabolic alkalosis, and hypokalemia in a CKD patient — indirect relevance to potassium/acid-base handling. |
| [239022](https://pubmed.ncbi.nlm.nih.gov/239022/) | 1975 | Preclinical (Animal) | The Journal of clinical investigation | Rat model of KCl deficiency examining renal citrate and ammonia metabolism and effects of volume expansion on metabolic alkalosis correction. |

---

## Saudi Arabia Market Information

No authorization records — potassium acetate is currently not marketed in Saudi Arabia (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L4 (preclinical/mechanistic only), no clinical trials support this indication, and most identified literature consists of case reports. Critically, several key references describe hyperkalemic RTA subtypes where potassium supplementation would be contraindicated, directly conflicting with the proposed rationale — this subtype mismatch must be resolved before advancing.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (blocking gap, DG001) to complete the S1 safety screen
- Confirmed mechanism of action data from DrugBank (DG002)
- RTA subtype-stratified evidence (specifically hypokalemic Type 1/2 RTA) rather than mixed hyper-/hypokalemic case series
- Prospective or controlled clinical evidence in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

