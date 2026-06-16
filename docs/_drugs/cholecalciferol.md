---
layout: default
title: Cholecalciferol
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 7
---

# Cholecalciferol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cholecalciferol: From Vitamin D Deficiency to Renal Osteodystrophy

## One-Sentence Summary

Cholecalciferol (Vitamin D3) is a fat-soluble prohormone essential for calcium and phosphorus homeostasis, classically used to prevent and treat vitamin D deficiency, nutritional rickets, and bone demineralisation disorders. The TxGNN model identified 7 candidate new indications; among these, **Renal Osteodystrophy** carries the strongest clinical evidence (L2, 32 clinical trials, 20 publications) and is the primary actionable target, while **Hypophosphatemic Rickets** (L3) offers a compelling secondary mechanistic case. The top 4 TxGNN-ranked predictions all score above 99.7% yet carry no disease-specific clinical evidence (L5), reflecting knowledge graph topology artefacts rather than genuine drug–disease relationships.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin D deficiency; nutritional rickets; bone metabolism support |
| Predicted New Indication (Primary) | Renal Osteodystrophy |
| TxGNN Prediction Score | 99.11% (Rank 6; highest-evidence among 7 predictions) |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## All TxGNN Predictions at a Glance

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|---------------------|-------------|----------------|---------|
| 1 | Familial isolated hypoparathyroidism (PTH secretion defect) | 99.79% | L5 | Hold |
| 2 | Acromesomelic dysplasia, Campailla-Martinelli type | 99.78% | L5 | Hold |
| 3 | Craniofacial conodysplasia | 99.75% | L5 | Hold |
| 4 | Dahlberg-Borer-Newcomer syndrome | 99.73% | L5 | Hold |
| 5 | Hypophosphatemic Rickets | 99.20% | L3 | Research Question |
| 6 | Renal Osteodystrophy | 99.11% | **L2** | **Proceed with Guardrails** |
| 7 | Renal Tubular Acidosis | 99.06% | L4 | Research Question |

> **Note on ranks 1–4:** All four are scored L5 with zero disease-specific clinical trials or literature. The rationale documents indicate these predictions originate from shared "calcium metabolism" or "skeletal dysplasia" nodes in the knowledge graph, not from biological plausibility. They are retained here for completeness but warrant no further short-term action.

---

## Why Is This Prediction Reasonable?

Cholecalciferol is activated in two sequential steps: hepatic hydroxylation to 25-hydroxyvitamin D3 (calcidiol, the circulating storage form), followed by renal 1α-hydroxylation to 1,25-dihydroxyvitamin D3 (calcitriol), the biologically active hormone. Calcitriol binds the nuclear Vitamin D Receptor (VDR) to upregulate intestinal calcium and phosphate absorption, suppress PTH gene transcription, and promote osteoblast mineralisation. Detailed DrugBank MOA data is currently unavailable for this report; the mechanistic reasoning below is drawn from published endocrinology literature.

In chronic kidney disease (CKD), progressive nephron loss reduces renal 1α-hydroxylase activity, leading to calcitriol deficiency. The resulting hypocalcaemia stimulates PTH secretion (secondary hyperparathyroidism), driving bone resorption and impaired mineralisation — the constellation of pathologies termed renal osteodystrophy. Cholecalciferol supplementation replenishes the 25-OH-D3 substrate pool, enabling partial calcitriol synthesis through extrarenal 1α-hydroxylase expressed in macrophages, osteoblasts, and parathyroid glands. This extrarenal pathway is operative even when renal capacity is substantially compromised. In early-to-moderate CKD (Stages G1–G3), cholecalciferol supplementation has clinical-trial support for reducing PTH and improving bone mineral markers. In advanced CKD and ESRD, active analogues (calcitriol, paricalcitol, doxercalciferol) are the clinical standard because they bypass the impaired renal activation step entirely.

For hypophosphatemic rickets (Rank 5), the relationship is more complex: XLH is characterised by elevated FGF23, which actively suppresses renal 1α-hydroxylase — effectively blocking cholecalciferol → calcitriol conversion. The historical treatment included phosphate salts combined with active Vitamin D analogues (not cholecalciferol itself), and the current standard has shifted to burosumab (anti-FGF23 antibody). Cholecalciferol's role here is adjunctive substrate replenishment, and its efficacy as a primary agent is limited by the FGF23-mediated block.

---

## Clinical Trial Evidence

*The following tables focus on the two clinically actionable indications: Renal Osteodystrophy (Rank 6, L2) and Hypophosphatemic Rickets (Rank 5, L3).*

### Renal Osteodystrophy

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00656032](https://clinicaltrials.gov/study/NCT00656032) | Phase 2 | Completed | 12 | Most directly relevant trial: evaluates Vitamin D receptor activation effects on insulin resistance and inflammation in ESRD; tests hypothesis that Vitamin D3 analogue restores insulin sensitivity and reduces inflammatory markers in end-stage kidney disease |
| [NCT00285467](https://clinicaltrials.gov/study/NCT00285467) | N/A | Completed | 55 | Head-to-head comparison of **Cholecalciferol vs. Doxercalciferol** for secondary hyperparathyroidism in CKD stages 3–4; directly tests cholecalciferol's ability to control PTH in moderate CKD |
| [NCT00752401](https://clinicaltrials.gov/study/NCT00752401) | Phase 3 | Unknown | 200 | VITA-D trial: **Cholecalciferol** substitution in Vitamin D-deficient kidney transplant recipients; evaluates GFR, acute rejection episodes, infection rates, and CRP at 1 year post-transplant |
| [NCT00001242](https://clinicaltrials.gov/study/NCT00001242) | N/A | Completed | 70 | NIH longitudinal study on states of Vitamin D and PTH resistance (hypocalcaemia, rickets, osteomalacia, pseudohypoparathyroidism); directly addresses Vitamin D resistance mechanisms relevant to CKD |
| [NCT00108394](https://clinicaltrials.gov/study/NCT00108394) | Phase 4 | Completed | N/A | Evaluation and management of osteopenia and renal osteodystrophy; assesses pamidronate for adynamic bone disease in the context of comprehensive CKD mineral management |
| [NCT00560300](https://clinicaltrials.gov/study/NCT00560300) | Phase 2 | Completed | 61 | Comparison of calcitriol vs. doxercalciferol and two phosphate binders on bone disease in children with kidney failure; characterises the differential effects of Vitamin D analogues in paediatric CKD-MBD |
| [NCT03960437](https://clinicaltrials.gov/study/NCT03960437) | Phase 2 | Completed | 22 | Etelcalcetide (calcimimetic) effects on bone tissue properties and calcification propensity in ESKD with hyperparathyroidism; provides comparative context for Vitamin D pathway vs. calcimimetic interventions |
| [NCT03202407](https://clinicaltrials.gov/study/NCT03202407) | Phase 3 | Unknown | 40 | Non-calcium vs. calcium-based phosphate binders in paediatric haemodialysis patients with CKD-MBD; disease context directly relevant to Vitamin D metabolism abnormalities in dialysis patients |
| [NCT00527085](https://clinicaltrials.gov/study/NCT00527085) | Phase 2 | Completed | 45 | 12-month randomised, double-blind, placebo-controlled study of cinacalcet (calcimimetic) in haemodialysis patients with secondary hyperparathyroidism and renal osteodystrophy; includes bone biopsy endpoints |
| [NCT01149291](https://clinicaltrials.gov/study/NCT01149291) | N/A | Completed | 511 | 18-month post-marketing observational study of selective Vitamin D Receptor Activators (sVDRA) for secondary hyperparathyroidism in haemodialysis patients in Turkey; real-world efficacy and safety of VDR-targeting agents in ESRD |

### Hypophosphatemic Rickets

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02915705](https://clinicaltrials.gov/study/NCT02915705) | Phase 3 | Completed | 61 | Burosumab vs. oral phosphate + **active Vitamin D** (control arm) in paediatric XLH; establishes conventional Vitamin D-based treatment as the clinical comparator and provides quantitative efficacy benchmarks |
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | Active, Not Recruiting | 20 | **Calcitriol monotherapy** (without phosphate) in children and adults with XLH; tests whether Vitamin D metabolite alone improves serum phosphate and skeletal mineralisation without increasing nephrocalcinosis |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | Unknown | 100 | High-dose vs. standard-dose calcitriol combined with neutral phosphate in children with XLH; establishes optimal dosing for active Vitamin D analogues in hypophosphatemic rickets |
| [NCT03920072](https://clinicaltrials.gov/study/NCT03920072) | Phase 3 | Completed | 35 | Long-term safety and efficacy of burosumab (anti-FGF23) in adult XLH; provides comparative context showing outcomes achievable beyond the conventional Vitamin D + phosphate paradigm |
| [NCT01652573](https://clinicaltrials.gov/study/NCT01652573) | N/A | Completed | 21 | Nasal calcitonin to reduce circulating FGF23 and phosphate wasting in XLH; complementary treatment strategy addressing the upstream FGF23 block that limits cholecalciferol activation |

---

## Literature Evidence

### Renal Osteodystrophy

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9684690](https://pubmed.ncbi.nlm.nih.gov/9684690/) | 1998 | Review | Artificial Organs | Comprehensive diagnostic and treatment review of renal osteodystrophy subtypes (osteitis fibrosa, osteomalacia, adynamic bone); identifies native Vitamin D deficiency as a distinct cause of osteomalacia in CKD patients |
| [12944733](https://pubmed.ncbi.nlm.nih.gov/12944733/) | 2003 | Review | Blood Purification | Pathogenesis and treatment of ROD; documents calcitriol deficiency from impaired renal 1α-hydroxylase as a primary driver of secondary hyperparathyroidism and high-turnover bone disease |
| [12386262](https://pubmed.ncbi.nlm.nih.gov/12386262/) | 2002 | Review | Nephrol Dial Transplant | Secondary hyperparathyroidism in renal osteodystrophy; describes decreased calcitriol and calcium-sensing receptor density as key mechanisms; relevant to cholecalciferol's substrate-replacement rationale |
| [3909812](https://pubmed.ncbi.nlm.nih.gov/3909812/) | 1985 | Review | Am J Med Sci | Foundational review on altered Vitamin D, calcium, phosphorus, and PTH metabolism in renal failure; establishes theoretical basis for Vitamin D supplementation in CKD bone disease |
| [16970258](https://pubmed.ncbi.nlm.nih.gov/16970258/) | 2006 | Review | Saudi J Kidney Dis Transplant | Renal osteodystrophy review from a Saudi-published journal; discusses shift from high-turnover to low-turnover bone disease and implications for treatment strategy in dialysis populations — directly relevant to Saudi Arabia clinical context |
| [3518448](https://pubmed.ncbi.nlm.nih.gov/3518448/) | 1986 | Review | Am J Med Sci | Updated review on ROD pathogenesis and treatment; discusses Vitamin D metabolite deficiency and its correction as part of management |
| [8512774](https://pubmed.ncbi.nlm.nih.gov/8512774/) | 1993 | Case Series | Curr Opin Rheumatol | Aluminium-related bone disease and adynamic bone disease in uraemic patients; discusses phosphate binder optimisation and residual bone disease; relevant to distinguishing ROD subtypes amenable to Vitamin D intervention |

### Hypophosphatemic Rickets

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Review | Nutrients | Types of rickets and treatment with Vitamin D and analogues; explicitly addresses cholecalciferol, ergocalciferol, calcitriol, and alfacalcidol in different rickets subtypes including XLH; most current and comprehensive treatment review |
| [31392510](https://pubmed.ncbi.nlm.nih.gov/31392510/) | 2020 | Review | Pediatr Nephrol | Mineralised tissues in hypophosphatemic rickets; details PHEX mutation → elevated FGF23 → phosphate wasting → growth plate and bone mineralisation defects; explains why cholecalciferol's activation is mechanistically constrained |
| [26813507](https://pubmed.ncbi.nlm.nih.gov/26813507/) | 2016 | Review | Clinical Calcium | FGF23-related hypophosphatemic rickets: current therapy and unresolved issues; reviews active Vitamin D + phosphate combination and its limitations including nephrocalcinosis and secondary HPT complications |
| [35226335](https://pubmed.ncbi.nlm.nih.gov/35226335/) | 2022 | Cohort | J Endocrinol Invest | Retrospective cohort study of growth trajectories in hereditary hypophosphatemic rickets from birth to adulthood; quantifies the disease burden that Vitamin D-based treatment is expected to ameliorate |
| [29292875](https://pubmed.ncbi.nlm.nih.gov/29292875/) | 2017 | Review | Pediatr Endocrinol Rev | Early calcitriol and phosphate therapy in XLH: height data from 127 patients across 49 centres; documents the effect of early Vitamin D-based treatment initiation on final height outcomes |

---

## Saudi Arabia Market Information

Cholecalciferol (Vitamin D3) is currently **not registered** in the Saudi Arabia regulatory database — 0 authorisations on record in this dataset. As a widely available nutritional supplement and WHO Essential Medicine globally, it is likely accessible through international channels or as an unregistered imported product; however, formal regulatory approval in Saudi Arabia is not documented here.

*No authorisation records to display.*

> If pursuing a formal indication in Saudi Arabia, a full regulatory submission to the Saudi Food & Drug Authority (SFDA) would be required, including Vitamin D3 being registered as a pharmaceutical product rather than a supplement.

---

## Safety Considerations

Please refer to the package insert for safety information.

In the absence of Saudi Arabia regulatory filing data, the following general pharmacological safety signals are noted from the published literature (not from a regulatory dossier):

- **Hypercalcaemia risk**: High-dose or prolonged cholecalciferol supplementation can cause hypercalcaemia and hypercalciuria, particularly in patients with impaired renal regulation of calcium homeostasis (directly relevant to CKD and renal osteodystrophy populations)
- **Metastatic calcification in CKD**: In dialysis and advanced CKD patients, excessive Vitamin D supplementation may worsen vascular calcification; PMID 10910456 specifically flags Vitamin D-associated nephrocalcinosis in patients with renal tubular acidosis and hypercalciuria
- **Monitoring**: Serum 25-OH-D3, serum calcium, serum phosphate, and renal function (eGFR) monitoring are indicated during supplementation in all CKD patients

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(for Renal Osteodystrophy, Rank 6)*

**Rationale:**
Cholecalciferol has an established mechanistic role as the substrate precursor of the Vitamin D endocrine axis, and calcitriol deficiency from impaired renal 1α-hydroxylase is a well-documented, central driver of renal osteodystrophy. Two trials directly testing cholecalciferol in CKD patients exist (NCT00285467, NCT00752401), and the broader Vitamin D intervention literature in this disease context reaches L2 evidence. Ranks 1–4 (all L5, no disease-specific data) should not proceed. Hypophosphatemic Rickets (Rank 5) and Renal Tubular Acidosis (Rank 7) are appropriate for investigator-initiated research question framing.

**To proceed, the following is needed:**
- DrugBank MOA data retrieval to formally document VDR-mediated mechanisms and complete regulatory submission pharmacology sections
- Saudi Arabia SFDA regulatory pathway assessment: determine whether a supplement registration or pharmaceutical New Drug Application is required
- Safety monitoring protocol: serum calcium, serum phosphate, 25-OH-D3, PTH, and eGFR measurement schedule stratified by CKD stage
- CKD stage-stratified treatment positioning: define cholecalciferol's role in early CKD (G1–G3, primary supplementation) vs. late CKD/ESRD (adjunctive to calcitriol/paricalcitol)
- For hypophosphatemic rickets (Rank 5): clarify adjunctive vs. primary role in the burosumab era; a Research Question protocol comparing cholecalciferol + phosphate vs. burosumab monotherapy as adjunct would be the appropriate framing
- Package insert review from an approved market (EU or Japan) to extract formal contraindications and dosing recommendations for renal impairment populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

