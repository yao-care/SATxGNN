---
layout: default
title: Potassium Gluconate
parent: 僅模型預測 (L5)
nav_order: 509
evidence_level: L5
indication_count: 1
---

# Potassium Gluconate
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

# Potassium Gluconate: From Hypokalemia to Renal Tubular Acidosis

## One-Sentence Summary

Potassium gluconate is a potassium salt used for oral potassium repletion in hypokalemia; no formal indication record is available in this evidence pack, and detailed mechanism-of-action data has not yet been retrieved.
The TxGNN model predicts it may be effective for **Renal Tubular Acidosis**, with **0 clinical trials** and **8 publications** currently identified — evidence is preclinical/mechanistic and includes a subtype-mismatch risk described below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no Saudi license text available); based on known pharmacology, used as an oral potassium supplement for hypokalemia |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, potassium gluconate is a potassium salt used for oral potassium supplementation, and its efficacy in correcting hypokalemia/potassium deficiency is well established; mechanistically this may be applicable to renal tubular acidosis (RTA), where potassium status is central to the disease process.

The link is plausible for one specific RTA subtype: in hypokalemic RTA (classically Type 1/distal RTA), potassium supplementation (typically as potassium citrate, though potassium gluconate has been used in case reports) is a recognized adjunct to alkali therapy. However, RTA is pathophysiologically heterogeneous — Type 4 RTA is **hyperkalemic**, and potassium supplementation is contraindicated in that subtype. The literature set retrieved for this prediction includes a case report of severe hyperkalemic Type 4 RTA, confirming this subtype conflict is real and not captured by the TxGNN score. This means the prediction is directionally reasonable only for a subset of RTA patients, and requires manual clinical triage by subtype before any further development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33771116](https://pubmed.ncbi.nlm.nih.gov/33771116/) | 2021 | RCT | BMC Nephrology | RCT comparing 0.9% NaCl vs. Plasma-Lyte on kidney injury biomarkers, sodium excretion, and tubular transport proteins after hip replacement; relevant to chloride-induced acidosis mechanisms, not RTA treatment directly |
| [18031562](https://pubmed.ncbi.nlm.nih.gov/18031562/) | 2008 | Review | Acta Neurologica Scandinavica | Review of primary periodic paralyses, which overlap clinically with potassium/RTA-related muscle weakness syndromes |
| [4990462](https://pubmed.ncbi.nlm.nih.gov/4990462/) | 1970 | Review | Wiener Klinische Wochenschrift | German-language review of clinically important water and electrolyte regulation disorders (abstract not available) |
| [2352031](https://pubmed.ncbi.nlm.nih.gov/2352031/) | 1990 | Cohort (animal) | The Journal of Nutrition | Dietary potassium restriction/acidification study in cats; potassium gluconate used to restore dietary potassium and assess renal function/mineral metabolism |
| [24659721](https://pubmed.ncbi.nlm.nih.gov/24659721/) | 2014 | Case Report (animal) | Journal of the American Animal Hospital Association | Dog with distal RTA secondary to leptospirosis, treated with sodium bicarbonate and potassium gluconate |
| [17112912](https://pubmed.ncbi.nlm.nih.gov/17112912/) | 2006 | Case Report | Transplantation Proceedings | Severe **hyperkalemic** Type 4 RTA after kidney transplantation — illustrates a subtype where potassium supplementation would be contraindicated |
| [8009183](https://pubmed.ncbi.nlm.nih.gov/8009183/) | 1994 | Case Report | Scandinavian Journal of Urology and Nephrology | Type 1 RTA with nephrocalcinosis managed long-term with sodium bicarbonate, potassium gluconate, and sodium thiosulphate; stable renal function over 9 years |
| [3014162](https://pubmed.ncbi.nlm.nih.gov/3014162/) | 1986 | Case Series | Journal of Toxicology. Clinical Toxicology | Toluene-inhalation-associated distal RTA with hypokalemia and quadriparesis |

---

## Saudi Arabia Market Information

Currently not marketed in Saudi Arabia; no license records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but supporting evidence is limited to preclinical/case-level literature (no clinical trials) and includes a direct subtype conflict — potassium supplementation is appropriate for hypokalemic RTA but contraindicated in hyperkalemic Type 4 RTA, which appears in the same literature set. Combined with the Blocking data gap on TFDA warnings/contraindications and the missing MOA data, this is not yet ready to advance past initial safety screening.

**To proceed, the following is needed:**
- TFDA package insert (warnings and contraindications) — currently a Blocking data gap for the S1 safety screen
- DrugBank mechanism-of-action data
- Subtype-stratified evidence distinguishing hypokalemic (Type 1/2) vs. hyperkalemic (Type 4) RTA, since the two require opposite potassium management
- Saudi Arabia regulatory/licensing pathway assessment, since the drug is not currently marketed there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

