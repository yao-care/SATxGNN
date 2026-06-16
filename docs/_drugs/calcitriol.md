---
layout: default
title: Calcitriol
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 7
---

# Calcitriol
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

# Calcitriol: From Metabolic Bone Disease to Hereditary Hypophosphatemic Rickets

## One-Sentence Summary

Calcitriol (1,25-dihydroxyvitamin D3) is the biologically active hormonal form of vitamin D, traditionally used for hypocalcemia management in chronic kidney disease, hypoparathyroidism, and renal osteodystrophy.
The TxGNN model's highest-evidenced actionable prediction is **Hereditary Hypophosphatemic Rickets** (Rank #7), supported by **7 clinical trials** and **20 publications** — including an active Phase 4 dose-optimization study (NCT03820518, n=100) and a Lancet 2024 disease review.

> **Note on ranking:** The top-ranked prediction (#1, "obsolete vitamin D deficiency") uses a deprecated disease ontology term no longer recognized by Orphanet/OMIM, carries no supporting trials or literature (L5, Hold), and represents a direct indication rather than a repurposing opportunity. This report therefore focuses on the highest-evidence, clinically actionable prediction: **Hereditary Hypophosphatemic Rickets** (Rank #7, L2, Proceed with Guardrails).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypocalcemia, hypoparathyroidism, renal osteodystrophy (traditional use; no SFDA authorization on record) |
| Predicted New Indication (Focus) | Hereditary Hypophosphatemic Rickets (TxGNN Rank #7) |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Predicted Indication Overview (All Ranks)

| Rank | Disease | TxGNN Score | Evidence | Recommendation |
|------|---------|-------------|----------|----------------|
| 1 | Obsolete vitamin D deficiency *(deprecated term)* | 99.9955% | L5 | Hold |
| 2 | Renal Tubular Acidosis | 99.93% | L4 | Research Question |
| 3 | Familial Isolated Hypoparathyroidism (impaired PTH secretion) | 99.81% | L4 | Research Question |
| 4 | Acromesomelic Dysplasia, Campailla Martinelli Type | 99.79% | L5 | Hold |
| 5 | Craniofacial Conodysplasia | 99.78% | L5 | Hold |
| 6 | Dahlberg-Borer-Newcomer Syndrome | 99.76% | L4 | Research Question |
| **7** | **Hereditary Hypophosphatemic Rickets** | **99.28%** | **L2** | **Proceed with Guardrails** |

---

## Why is This Prediction Reasonable?

Calcitriol is the final active metabolite in the vitamin D activation cascade: dietary/sun-derived vitamin D3 is hydroxylated first in the liver (to 25-OH-D3) and then in the kidney by CYP27B1 (25-hydroxyvitamin D-1α-hydroxylase) to produce 1,25-dihydroxyvitamin D3 (calcitriol). Calcitriol binds to the vitamin D receptor (VDR), a nuclear transcription factor expressed in the intestine, kidney, bone, parathyroid gland, and numerous other tissues. Its core physiological actions include stimulating intestinal calcium and phosphate absorption, facilitating renal calcium reabsorption, and regulating bone mineralization through osteoblast differentiation.

In **hereditary hypophosphatemic rickets** — most commonly X-linked hypophosphatemia (XLH), caused by loss-of-function mutations in the *PHEX* gene — excess production of the phosphaturic hormone FGF23 by osteocytes actively suppresses renal CYP27B1 activity. This creates a dual deficit: renal phosphate wasting (leading to hypophosphatemia) combined with inappropriately low calcitriol synthesis, which further impairs intestinal phosphate absorption. The result is defective growth plate and bone mineralization, presenting as rickets in children and osteomalacia in adults. Supplementing exogenous calcitriol directly bypasses FGF23-mediated suppression of CYP27B1 and restores the intestinal calcium/phosphate absorptive capacity, while oral phosphate supplementation corrects the renal wasting component.

This dual-therapy approach (calcitriol + phosphate) has been the standard of care for XLH for over four decades, confirmed by a Phase 4 dose-optimization study (NCT03820518, n=100) and documented in major clinical guidelines including a 2024 Lancet review and a 2025 Calcified Tissue International clinical guideline. It is worth noting that the newer anti-FGF23 biologic burosumab (Crysvita) has demonstrated superior efficacy by targeting the upstream hormonal driver and is now the preferred first-line therapy where available. Calcitriol retains a clinically relevant role in resource-limited or burosumab-contraindicated settings, and as adjunctive therapy in ENPP1 and ADHR subtypes.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | Active, Not Recruiting | 20 | **Calcitriol monotherapy for XLH** — evaluates calcitriol alone (without phosphate) over 12 months with dose escalation in first 3 months; primary endpoint: serum phosphate and skeletal mineralization without increasing nephrocalcinosis |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | Unknown | 100 | **High vs. low-dose calcitriol + neutral phosphate in children with XLH** — dose-optimization study to establish evidence-based weight-adjusted calcitriol dosing in pediatric XLH |
| [NCT04846647](https://clinicaltrials.gov/study/NCT04846647) | N/A (observational) | Completed | 260 | FGF23 hypersecretion characterization in hypophosphatemia — provides mechanistic basis for why calcitriol levels are insufficient in XLH and FGF23-excess conditions |
| [NCT06046820](https://clinicaltrials.gov/study/NCT06046820) | Phase 3 | Active, Not Recruiting | 27 | INZ-701 in children with ENPP1 deficiency — evaluates emerging alternative for phosphate dysregulation disorders in the XLH disease family |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A | Not Yet Recruiting | 65 | ATP 31P-NMR spectroscopy in phosphate diabetes (XLH and acquired forms) — diagnostic biomarker study |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Clinical Guideline | *Calcified Tissue Int.* | Current XLH diagnosis and therapy; calcitriol + phosphate as established first-line therapy; burosumab as preferred option where available |
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Review | *Lancet* | Comprehensive XLH review: PHEX mutations → FGF23 excess → renal phosphate wasting + reduced calcitriol synthesis; traditional therapy and burosumab comparative outcomes |
| [38044258](https://pubmed.ncbi.nlm.nih.gov/38044258/) | 2024 | Review | *Best Pract Res Clin Endocrinol Metab* | Inherited FGF23 excess syndromes including XLH, ADHR, ARHR; calcitriol's therapeutic role across all FGF23-mediated subtypes |
| [36446330](https://pubmed.ncbi.nlm.nih.gov/36446330/) | 2022 | Review | *Hormone Res Paediatrics* | History of rickets treatment; vitamin D activation pathway and calcitriol's role in correcting defective mineralization |
| [35226335](https://pubmed.ncbi.nlm.nih.gov/35226335/) | 2022 | Retrospective Cohort | *J Endocrinol Invest* | Growth and body proportion from birth to adulthood in hereditary hypophosphatemic rickets — documents long-term outcomes of treated vs. untreated patients |
| [31863781](https://pubmed.ncbi.nlm.nih.gov/31863781/) | 2020 | Review | *Metabolism* | XLH management in adults: calcitriol + phosphate for osteomalacia, bone pain, enthesopathy, pseudofractures, and dental anomalies |
| [29292875](https://pubmed.ncbi.nlm.nih.gov/29292875/) | 2017 | Multicenter Study | *Pediatr Endocrinol Rev* | Early calcitriol + phosphate therapy effects on spontaneous growth in 127 XLH patients from 49 centres across multiple countries |
| [17117305](https://pubmed.ncbi.nlm.nih.gov/17117305/) | 2006 | Review | *Arq Bras Endocrinol Metab* | All hereditary hypophosphatemic conditions cause inappropriately normal or low calcitriol; calcitriol supplementation rationale across subtypes |
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Clinical Study | *J Clin Investigation* | High-dose calcitriol (68 ng/kg/day) heals XLH-associated osteomalacia in 5 patients where conventional vitamin D alone failed |
| [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) | 1980 | Clinical Study | *NEJM* | Calcitriol + phosphate vs. phosphate alone vs. ergocalciferol in 11 children with vitamin D-resistant rickets; calcitriol increased intestinal phosphate absorption and reduced phosphate requirements |

---

## Safety Considerations

Detailed safety data (package insert warnings, contraindications, and drug interaction profile) were not available in this evidence pack. Key risks known from calcitriol's mechanism include:

- **Hypercalcemia and hypercalciuria**: The most important monitoring parameters; excess calcitriol drives increased intestinal calcium absorption that can lead to hypercalciuria, nephrocalcinosis, and renal stones — particularly relevant in XLH where calcitriol is used at relatively high doses combined with phosphate
- **Nephrocalcinosis**: A recognized long-term complication of calcitriol + phosphate therapy in XLH, requiring periodic renal ultrasound monitoring

Please refer to the full package insert and treating specialist guidance for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Calcitriol combined with phosphate supplementation represents the established, four-decade standard of care for hereditary hypophosphatemic rickets, supported by Phase 1 and Phase 4 clinical trials, multiple high-quality reviews, and 2024–2025 international clinical guidelines. The mechanistic rationale — bypassing FGF23-mediated CYP27B1 suppression — is well-understood and directly supported by calcitriol's pharmacology. Evidence level L2 is sufficient to support a regulated, monitored repurposing pathway.

**To proceed, the following is needed:**

- **Regulatory filing**: Calcitriol has no SFDA authorization in Saudi Arabia; a new marketing authorization application (MAA) or bibliographic/well-established use application is required before clinical deployment
- **MOA documentation**: A formal mechanism-of-action dossier is needed for regulatory submission (currently flagged as a data gap)
- **Competitive positioning vs. burosumab**: Define the patient population where calcitriol offers a viable alternative — e.g., cost constraints, burosumab unavailability, ENPP1/ADHR subtypes, or adjunctive use — and document this in the clinical development rationale
- **Safety monitoring protocol**: Standardize monitoring for hypercalcemia, hypercalciuria, urinary calcium/creatinine ratio, and nephrocalcinosis (renal ultrasound at 6–12 month intervals) before initiating any clinical program
- **Dose optimization data**: Await or obtain results from NCT03820518 (Phase 4, n=100) to establish evidence-based weight-adjusted dosing; monitor NCT03748966 for calcitriol monotherapy data
- **Pediatric formulation**: XLH primarily affects children; age-appropriate oral formulation (solution or dispersible tablet) and pediatric pharmacokinetic data are required
- **Genetic subtype stratification**: Confirm applicability across all hereditary hypophosphatemic rickets subtypes (XLH, ADHR, ARHR, HHRH) and document response variability by mutation type
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

