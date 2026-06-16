---
layout: default
title: Clofarabine
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 10
---

# Clofarabine
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

# Clofarabine: From Pediatric ALL to Myeloid Leukemia

## One-Sentence Summary

Clofarabine (Clolar/Evoltra) is a second-generation purine nucleoside analog first approved by the FDA in 2004 for the treatment of relapsed or refractory acute lymphoblastic leukemia (ALL) in pediatric patients, marking the first new drug for pediatric leukemia approved in over a decade.
The TxGNN model predicts it may be effective for **myeloid leukemia**,
with **50 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsed/refractory pediatric ALL (FDA 2004 / EMA 2006 approved; not registered in Saudi Arabia) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Although formal DrugBank mechanism-of-action data was not retrieved for this report, published literature provides a well-characterized pharmacological profile. Clofarabine is a second-generation purine nucleoside analog engineered to combine the best properties of cladribine and fludarabine while overcoming their limitations (such as enzymatic deamination). It acts through three converging mechanisms: (1) inhibition of ribonucleotide reductase (RNR), depleting the intracellular deoxyribonucleoside triphosphate (dNTP) pool; (2) direct incorporation into DNA, causing strand termination; and (3) disruption of mitochondrial membrane integrity, triggering the intrinsic apoptosis pathway. These mechanisms are selectively potent in rapidly proliferating cells with high nucleotide demand — precisely the biology of leukemic blasts, whether lymphoid or myeloid in origin.

Clofarabine's original approval in pediatric ALL reflects the high sensitivity of lymphoid precursor cells to nucleotide synthesis disruption. Acute myeloid leukemia (AML) shares this fundamental dependency: rapidly cycling myeloid blasts rely heavily on de novo nucleotide biosynthesis, making them equally vulnerable to RNR inhibition and DNA chain termination. This mechanistic overlap explains why researchers began evaluating clofarabine in AML almost simultaneously with its ALL development — NCT00044889 (Phase 2 in adult AML) opened in May 2002, the same period as the pivotal pediatric ALL pivotal trials. The drug's strong immunosuppressive properties, which reduce the risk of graft rejection, also make it a particularly attractive component of reduced-intensity conditioning regimens prior to allogeneic stem cell transplantation in AML.

The TxGNN prediction is further grounded in an extensive body of published evidence. A 2019 Phase 3 sub-analysis (AML08, PMID 31246522) demonstrated that clofarabine can replace conventional anthracycline-etoposide induction in pediatric AML without sacrificing efficacy. Multiple completed Phase 2 trials — including randomized designs (NCT01423175, NCT00932412) and large single-arm salvage studies (NCT01295307, n=86; NCT00373529, n=116) — have consistently shown antileukemic activity across AML subtypes, from newly diagnosed elderly patients to relapsed/refractory disease. A Lancet Oncology systematic review (PMID 31281098, 2019) consolidates these findings into a coherent evidentiary framework, making myeloid leukemia one of the best-supported predicted new indications for clofarabine.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00044889](https://clinicaltrials.gov/study/NCT00044889) | Phase 2 | Completed | 40 | Single-arm open-label study of clofarabine monotherapy in adult relapsed/refractory AML; established proof of concept for single-agent activity in AML |
| [NCT01423175](https://clinicaltrials.gov/study/NCT01423175) | Phase 2 | Unknown | 60 | Randomized multicenter trial comparing ClAraC (clofarabine + Ara-C × 5 days) vs FLAMSA in high-risk AML/advanced MDS before allogeneic SCT; primary endpoint event-free survival |
| [NCT00932412](https://clinicaltrials.gov/study/NCT00932412) | Phase 2 | Completed | 735 | Randomized comparison of clofarabine/intermediate-dose Ara-C (CLARA) vs high-dose Ara-C (HDAC) as consolidation in younger newly diagnosed AML patients not receiving allogeneic SCT |
| [NCT00454480](https://clinicaltrials.gov/study/NCT00454480) | Phase 2/3 | Completed | 2000 | Large treatment development programme for older AML and high-risk MDS; evaluated multiple combinations including clofarabine alongside gemtuzumab ozogamicin and other agents |
| [NCT01295307](https://clinicaltrials.gov/study/NCT01295307) | Phase 2 | Completed | 86 | Clofarabine salvage therapy in relapsed/refractory AML; assessed rate of achieving remission sufficient to bridge to allogeneic HCT |
| [NCT02686593](https://clinicaltrials.gov/study/NCT02686593) | Phase 2 | Completed | 50 | CLAM regimen (clofarabine 30 mg/m²/day + cytarabine 750 mg/m²/day + mitoxantrone 12 mg/m²/day) as first salvage in AML refractory/relapsed after 3+7 induction |
| [NCT01794702](https://clinicaltrials.gov/study/NCT01794702) | Phase 1/2 | Completed | 65 | Decitabine followed by CIA (clofarabine + idarubicin + cytarabine) in acute leukemia; Phase I determined MTD, Phase II assessed disease control rate and safety |
| [NCT01188174](https://clinicaltrials.gov/study/NCT01188174) | Phase 2 | Completed | 26 | Prospective sequential strategy combining clofarabine/Ara-C salvage chemotherapy with subsequent reduced-intensity allogeneic SCT for AML in primary treatment failure |
| [NCT00373529](https://clinicaltrials.gov/study/NCT00373529) | Phase 2 | Completed | 116 | Single-agent clofarabine in previously untreated older AML patients unlikely to benefit from intensive standard chemotherapy; evaluated overall response rate and tolerability |
| [NCT01101880](https://clinicaltrials.gov/study/NCT01101880) | Phase 2 | Completed | 50 | Clofarabine combined with high-dose cytarabine and G-CSF priming in adults under 65 with newly diagnosed AML or advanced MDS/myeloproliferative neoplasm |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31246522](https://pubmed.ncbi.nlm.nih.gov/31246522/) | 2019 | Phase 3 RCT sub-analysis | J Clin Oncol | AML08 multicenter randomized trial: clofarabine can replace anthracyclines and etoposide in pediatric AML remission induction with comparable efficacy and potentially reduced late cardiotoxicity |
| [32187883](https://pubmed.ncbi.nlm.nih.gov/32187883/) | 2020 | Retrospective Cohort | Cancer Medicine | CLAM regimen (Phase 2, n=50) in relapsed/refractory AML: high complete remission rates with effective bridge to allogeneic HSCT in patients aged 18–65 |
| [36336258](https://pubmed.ncbi.nlm.nih.gov/36336258/) | 2023 | Prospective Cohort | Transplant Cell Ther | Clofarabine/busulfan myeloablative conditioning (Clo/Bu4) for active myeloid malignancies: antileukemic activity with acceptable non-relapse mortality in patients ≤70 years |
| [31281098](https://pubmed.ncbi.nlm.nih.gov/31281098/) | 2019 | Systematic Review | Lancet Oncol | Systematic review confirming the clinical utility of clofarabine + cytarabine combination regimens in AML across induction and salvage settings |
| [31905904](https://pubmed.ncbi.nlm.nih.gov/31905904/) | 2019 | Cohort Analysis | Cancers | CLARA vs HDAC consolidation in younger AML: clofarabine-based CLARA significantly improves relapse-free survival in patients with micro-complex karyotype AML |
| [27621503](https://pubmed.ncbi.nlm.nih.gov/27621503/) | 2015 | Clinical Study | Hosp Pharmacy | Pharmacist-focused review of the clofarabine + cytarabine regimen — preparation, dispensing, administration protocols, and clinical use in AML |
| [22957815](https://pubmed.ncbi.nlm.nih.gov/22957815/) | 2013 | Review | Leuk Lymphoma | Comprehensive review of clofarabine's mechanism (RNR inhibition, DNA polymerase inhibition), pharmacokinetics, and evolving clinical role in AML as monotherapy and in combinations |
| [25457773](https://pubmed.ncbi.nlm.nih.gov/25457773/) | 2015 | Review | Crit Rev Oncol Hematol | Critical appraisal of clofarabine's development in adult AML across first-line and salvage settings; reviews combination strategies and identifies subgroups most likely to benefit |
| [23526416](https://pubmed.ncbi.nlm.nih.gov/23526416/) | 2013 | Guidelines Review | Am J Hematol | AML 2013 update on risk stratification and management; contextualizes novel nucleoside analogs including clofarabine within contemporary treatment algorithms |
| [17852710](https://pubmed.ncbi.nlm.nih.gov/17852710/) | 2007 | Review | Leuk Lymphoma | Foundational review of clofarabine's design rationale, pharmacology, and early clinical development in acute leukemias including AML; establishes the scientific basis for current use |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — second-generation purine nucleoside analog (deoxyadenosine analog class) |
| Myelosuppression Risk | High — clofarabine consistently causes profound bone marrow suppression; febrile neutropenia, severe thrombocytopenia, and anemia are expected consequences of treatment at therapeutic doses |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (at least weekly during active treatment), liver function tests (ALT/AST/bilirubin), renal function (serum creatinine), and fluid balance monitoring (capillary leak syndrome and systemic inflammatory response have been reported) |
| Handling Protection | Must follow cytotoxic drug handling regulations; intravenous formulation requires preparation in a certified biological safety cabinet with standard chemotherapy PPE; disposal per hazardous waste protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2 trials — including two randomized designs — consistently demonstrate clofarabine's antileukemic activity across AML subtypes, backed by a Phase 3 RCT sub-analysis (AML08) and a Lancet Oncology systematic review (2019); the evidence base is sufficient to justify structured clinical use in myeloid leukemia, provided appropriate monitoring safeguards are in place. However, the drug is not currently registered in Saudi Arabia, and complete local safety data (package insert warnings, contraindications, drug interactions) remain unavailable in this evidence pack.

**To proceed, the following is needed:**
- Pursue Saudi Arabia (SFDA) regulatory registration or establish a compassionate use / named-patient access pathway
- Retrieve complete package insert safety data including key warnings, contraindications, and drug interaction profile
- Obtain formal DrugBank API mechanistic data (DrugBank ID: DB00631) to complete the pharmacological profile
- Define the specific AML treatment setting (induction in newly diagnosed patients, salvage for relapsed/refractory disease, or bridge-to-transplant conditioning) to align with the most relevant evidence tier
- Develop an institutional monitoring protocol addressing myelosuppression management, capillary leak syndrome surveillance, hepatotoxicity monitoring, and infection prophylaxis
- Evaluate pharmacogenomic factors (e.g., cytarabine sensitivity scores, karyotype risk stratification) where applicable to optimize patient selection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

