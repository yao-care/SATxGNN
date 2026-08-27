---
layout: default
title: Potassium Chloride
parent: 僅模型預測 (L5)
nav_order: 508
evidence_level: L5
indication_count: 1
---

# Potassium Chloride
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

# Potassium Chloride: From Potassium Replacement Therapy to Renal Tubular Acidosis

## One-Sentence Summary

> Potassium chloride is a basic electrolyte agent generally used for potassium replacement/hypokalemia correction; the evidence pack does not contain itemized original-indication or licensing records for this compound.
> The TxGNN model predicts it may be effective for **Renal Tubular Acidosis (RTA)**,
> with **9 clinical trials** and **19 publications** retrieved in the search, though most of this evidence is only indirectly related to the drug-disease pair.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not itemized in source data (potassium/electrolyte replacement is the general use of KCl; no `original_indications` or licence records were returned) |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug (data gap). Based on known pharmacology, potassium chloride acts as a direct source of potassium ion, and its general clinical role is correcting or preventing hypokalemia.

RTA (particularly distal Type 1 and proximal Type 2) is frequently accompanied by abnormal renal potassium handling and hypokalemia, so potassium supplementation is a genuine, recurring clinical need in RTA management — this is the mechanistic thread the model is likely picking up on.

However, the underlying pathology of RTA is a hyperchloremic, normal-anion-gap metabolic acidosis. Standard potassium repletion in RTA favors alkalinizing potassium salts (potassium citrate or potassium bicarbonate) rather than potassium chloride, because the additional chloride load from KCl can worsen the acidosis. In other words, the mechanistic link here is the generic "potassium supplementation" action of the drug rather than an RTA-specific mechanism, and the chloride counter-ion is potentially in tension with standard-of-care chemistry for this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06750172](https://clinicaltrials.gov/study/NCT06750172) | N/A | Recruiting | 33 | Diagnostic methodology study comparing 24-hour urinary aldosterone timing for primary aldosteronism; not an interventional/drug trial. |
| [NCT01894594](https://clinicaltrials.gov/study/NCT01894594) | Phase 1 | Terminated | 7 | Alkali therapy (oral sodium bicarbonate) for bicarbonate/potassium repletion in sickle cell disease with low serum bicarbonate — not KCl, not RTA. |
| [NCT01834768](https://clinicaltrials.gov/study/NCT01834768) | Phase 2 | Unknown | 31 | Safety of eplerenone (a potassium-*sparing* agent) in transplant recipients on cyclosporine — mechanistically opposite direction to KCl supplementation. |
| [NCT07273838](https://clinicaltrials.gov/study/NCT07273838) | Phase 2 | Recruiting | 130 | SGLT2 inhibitor for acute cardiorenal syndrome; overlaps only on "renal," no KCl/RTA link. |
| [NCT03354507](https://clinicaltrials.gov/study/NCT03354507) | N/A | Unknown | 40 | Oral sodium bicarbonate alkalinization for RTA occurring in pediatric patients on topiramate; mechanistically related (alkali therapy) but tests bicarbonate, not KCl. |
| [NCT03644706](https://clinicaltrials.gov/study/NCT03644706) | Phase 3 | Terminated | 3 | Randomized, placebo-controlled withdrawal study of ADV7103 for preventing metabolic acidosis in pediatric/adult distal RTA; terminated with only 3 enrolled, drug identity truncated in the title. |
| [NCT06867471](https://clinicaltrials.gov/study/NCT06867471) | N/A | Recruiting | 43 | Exogenous ketosis effect on proteinuria/renal function in CKD and polycystic kidney disease; no direct KCl/RTA relevance. |
| [NCT01843309](https://clinicaltrials.gov/study/NCT01843309) | Phase 4 | Terminated | 36 | Spironolactone for preventing electrolyte abnormalities from Amphotericin B; overlaps only on "electrolytes," not RTA. |
| [NCT00120731](https://clinicaltrials.gov/study/NCT00120731) | N/A | Withdrawn | 0 | Potassium *citrate* (same cation, different salt) for urinary chemistry/acid-base effects in pediatric hypercalciuria and urolithiasis — the conceptually closest trial, but not KCl, not RTA, and withdrawn with zero enrollment. |

**Note:** None of the retrieved trials directly test potassium chloride as a treatment for renal tubular acidosis. Relevance grading (provided in the evidence pack) rated all nine trials "C" except the potassium citrate trial ("B"), and that one enrolled zero subjects.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33459628](https://pubmed.ncbi.nlm.nih.gov/33459628/) | 2021 | Review | Archivos españoles de urología | Overview of RTA diagnosis and management, including calcium phosphate stone formation from impaired distal acid excretion. |
| [17297212](https://pubmed.ncbi.nlm.nih.gov/17297212/) | 2007 | Review | Acta Medica Indonesiana | General approach to hypokalemia, covering renal vs. extrarenal potassium loss. |
| [21314872](https://pubmed.ncbi.nlm.nih.gov/21314872/) | 2011 | Review | International Journal of Clinical Practice | Clinical approach to proximal (Type II) and distal (Type I/IV) RTA in adults. |
| [33769949](https://pubmed.ncbi.nlm.nih.gov/33769949/) | 2021 | Review | Journal of the American Society of Nephrology | Reassessment of urine anion gap as a surrogate for urinary ammonium excretion in metabolic acidosis. |
| [3518609](https://pubmed.ncbi.nlm.nih.gov/3518609/) | 1986 | Review | Annual Review of Medicine | Classic review defining proximal RTA and hypokalemic/hyperkalemic distal RTA subtypes. |
| [8694660](https://pubmed.ncbi.nlm.nih.gov/8694660/) | 1996 | Review | Archives of Internal Medicine | Pathophysiology and diagnostic workup of RTA using urinary pH, electrolytes, and serum potassium. |
| [14048071](https://pubmed.ncbi.nlm.nih.gov/14048071/) | 1963 | Review | Medical Bulletin (Ann Arbor) | Early historical review of renal tubular acidosis. |
| [38445406](https://pubmed.ncbi.nlm.nih.gov/38445406/) | 2023 | Cohort | La Tunisie Médicale | Genotype-phenotype correlation of distal RTA (SLC4A1, ATP6V0A1/ATP6V1B1 mutations) with hypokalemia and hypocitraturia. |
| [783200](https://pubmed.ncbi.nlm.nih.gov/783200/) | 1976 | Cohort | Journal of Clinical Investigation | In classic (Type 1) RTA patients corrected with oral **potassium bicarbonate** (not chloride), sodium conservation was impaired under restricted sodium intake in several patients — directly relevant to the citrate/bicarbonate-vs-chloride salt question. |
| [34748193](https://pubmed.ncbi.nlm.nih.gov/34748193/) | 2022 | Case Report | Journal of Nephrology | Case of distal RTA presenting with hypokalemic periodic paralysis during pregnancy. |

**Note:** No RCTs were retrieved for this pair; the literature base is exclusively reviews, one cohort study, and case reports, and none evaluate potassium chloride specifically.

---

## Market Information

No marketed products or license records are currently available for this compound (market status: Not Marketed, 0 authorizations on file).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all marked as data gaps in the evidence pack — notably DG001, a **Blocking**-severity gap on TFDA label warnings/contraindications, which prevents this candidate from entering the S1 safety pre-screen.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- DG001 (Blocking) — TFDA label warnings/contraindications are missing, so the candidate cannot yet pass initial safety screening (S1).
- No clinical trial or publication directly evaluates potassium chloride in RTA; the closest analog (potassium citrate) trial was withdrawn with zero enrollment, and the mechanistic rationale itself flags that standard RTA therapy favors citrate/bicarbonate potassium salts over chloride due to acid-load concerns.

**To proceed, the following is needed:**
- TFDA package insert with warnings/contraindications (resolves DG001)
- Confirmed mechanism of action and original-indication documentation from DrugBank (resolves DG002)
- A targeted literature/trial search specifically on potassium chloride (not citrate/bicarbonate) use in RTA, to test whether the chloride-load concern is clinically significant
- Market/licensing assessment if repurposing is pursued, since the product is currently unmarketed with no authorizations on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

