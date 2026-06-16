---
layout: default
title: Capecitabine
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine: From Colorectal Cancer to Gastric Tubular Adenocarcinoma

> **Report Scope Note:** The TxGNN model's top-ranked prediction (Rank 1) is gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS)—an ultra-rare hereditary syndrome with zero supporting clinical evidence for capecitabine. This report focuses on Rank 2 (**Gastric Tubular Adenocarcinoma**, L1 evidence, Proceed with Guardrails) as the primary actionable prediction. GAPPS is addressed in the Conclusion.

---

## One-Sentence Summary

Capecitabine is an orally administered fluoropyrimidine prodrug of 5-FU, widely approved globally for colorectal and breast cancer treatment, but currently not registered in Saudi Arabia.
The TxGNN model predicts it may be effective for **Gastric Tubular Adenocarcinoma**—the most common histological subtype of gastric cancer, accounting for over 60% of cases—with **0 registered clinical trials** under this specific subtype label and **20 publications**, including at least 6 landmark Phase 3 RCTs directly incorporating capecitabine as a backbone chemotherapy agent, currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Colorectal cancer, breast cancer (globally approved; not registered in Saudi Arabia) |
| Predicted New Indication | Gastric Tubular Adenocarcinoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank regulatory source. Based on established pharmacological knowledge, Capecitabine is an oral fluoropyrimidine carbamate that functions as a tumor-activated prodrug of 5-fluorouracil (5-FU). It undergoes sequential enzymatic conversion—first in the liver by carboxylesterase and cytidine deaminase, then finally and preferentially within tumor tissue by thymidine phosphorylase (TP). The resulting intratumoral 5-FU inhibits thymidylate synthase (TS), blocking nucleotide synthesis and DNA replication, and is incorporated into RNA and DNA to disrupt cancer cell proliferation. This selectivity for tumor tissue is the key pharmacological advantage over intravenous 5-FU infusion.

Gastric tubular adenocarcinoma, classified as the Lauren intestinal type, characteristically overexpresses TP relative to surrounding normal gastric mucosa. This creates a favorable intratumoral pharmacokinetic environment that enhances local 5-FU concentrations, providing a direct mechanistic rationale for capecitabine's predicted activity in this subtype. The tumor-to-normal tissue ratio of active 5-FU generation is higher than in other gastric cancer subtypes, making tubular adenocarcinoma a biologically well-matched target for capecitabine.

The clinical evidence base is exceptionally robust. The landmark CLASSIC trial (PMID 22226517, Lancet 2012) directly established adjuvant CAPOX (capecitabine + oxaliplatin) as a global standard of care following D2 gastrectomy in Stage II–IIIB gastric cancer. The RESOLVE trial (PMID 34252374; final OS PMID 39952264) further validated CAPOX in the perioperative and postoperative settings. Critically, the absence of registered clinical trials carrying the specific diagnostic label "gastric tubular adenocarcinoma" reflects database classification practice rather than lack of clinical evidence: tubular adenocarcinoma constitutes the majority histological subtype in all major Phase 3 gastric cancer trials that use CAPOX as their chemotherapy backbone (CheckMate 649, KEYNOTE-859, ORIENT-16, GLOW, RATIONALE-305).

---

## Clinical Trial Evidence

Currently no clinical trials are registered under the specific diagnostic label "gastric tubular adenocarcinoma" in combination with capecitabine. This is a known database indexing limitation: gastric tubular adenocarcinoma accounts for the majority of patients enrolled in Phase 3 trials that enroll "gastric or gastroesophageal junction adenocarcinoma" broadly—including the CAPOX-backbone trials documented in the Literature Evidence section below.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22226517](https://pubmed.ncbi.nlm.nih.gov/22226517/) | 2012 | Phase 3 RCT | Lancet | CLASSIC trial: Adjuvant CAPOX after D2 gastrectomy significantly improved DFS vs. surgery alone (68% vs. 53% at 3 years) in Stage II–IIIB gastric cancer — direct foundational L1 evidence for capecitabine in gastric adenocarcinoma |
| [34252374](https://pubmed.ncbi.nlm.nih.gov/34252374/) | 2021 | Phase 3 RCT | Lancet Oncology | RESOLVE trial: Perioperative SOX vs. postoperative CAPOX in D2-resected gastric/GEJ adenocarcinoma — CAPOX confirmed as effective standard arm; superiority and non-inferiority endpoints both evaluated |
| [39952264](https://pubmed.ncbi.nlm.nih.gov/39952264/) | 2025 | Phase 3 RCT | Lancet Oncology | RESOLVE final OS report: Updated long-term survival data confirming durable CAPOX efficacy in locally advanced gastric/GEJ adenocarcinoma after D2 gastrectomy |
| [37524953](https://pubmed.ncbi.nlm.nih.gov/37524953/) | 2023 | Phase 3 RCT | Nature Medicine | GLOW trial: Zolbetuximab + CAPOX vs. CAPOX alone in CLDN18.2+, HER2-negative advanced gastric/GEJ adenocarcinoma — CAPOX used as the standard-of-care control backbone |
| [34102137](https://pubmed.ncbi.nlm.nih.gov/34102137/) | 2021 | Phase 3 RCT | Lancet | CheckMate 649: Nivolumab + chemotherapy (CAPOX or FOLFOX) vs. chemotherapy alone as first-line for HER2-negative gastric/GEJ/esophageal adenocarcinoma — capecitabine arm included |
| [38806195](https://pubmed.ncbi.nlm.nih.gov/38806195/) | 2024 | Phase 3 RCT | BMJ | RATIONALE-305: Tislelizumab + chemotherapy (including CAPOX) vs. placebo + chemotherapy as first-line in advanced gastric/GEJ adenocarcinoma — confirmed survival benefit |
| [37875143](https://pubmed.ncbi.nlm.nih.gov/37875143/) | 2023 | Phase 3 RCT | Lancet Oncology | KEYNOTE-859: Pembrolizumab + chemotherapy (CAPOX or FP) vs. placebo + chemotherapy in HER2-negative advanced gastric/GEJ adenocarcinoma |
| [38051328](https://pubmed.ncbi.nlm.nih.gov/38051328/) | 2023 | Phase 3 RCT | JAMA | ORIENT-16: Sintilimab + CAPOX vs. CAPOX alone in advanced gastric/GEJ adenocarcinoma — CAPOX established as the standard comparator arm |
| [30982686](https://pubmed.ncbi.nlm.nih.gov/30982686/) | 2019 | Phase 3 RCT | Lancet | FLOT4: Perioperative FLOT vs. ECF/ECX (capecitabine-containing) in locally advanced resectable gastric/GEJ adenocarcinoma — capecitabine arm validated against novel regimen |
| [33610734](https://pubmed.ncbi.nlm.nih.gov/33610734/) | 2021 | Phase 2 RCT | Ann Oncol | FAST trial: Zolbetuximab + EOX (epirubicin, oxaliplatin, capecitabine) vs. EOX alone in CLDN18.2+ gastric/GEJ adenocarcinoma — direct capecitabine combination use confirmed feasible |

---

## Saudi Arabia Market Information

Capecitabine is currently **not registered** in Saudi Arabia. No product licenses, approved indications, or dosage form records were found in the SFDA regulatory database. Patients in Saudi Arabia requiring capecitabine must currently access it through import pathways or exceptional access programs.

---

## Cytotoxicity

Capecitabine meets the criteria for inclusion of this section: it belongs to the fluoropyrimidine class of conventional cytotoxic chemotherapy, and its predicted indication is a malignant condition.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Fluoropyrimidine class (oral prodrug of 5-FU) |
| Myelosuppression Risk | Moderate — neutropenia and thrombocytopenia are reported adverse effects; overall myelosuppression risk is generally lower than continuous-infusion IV 5-FU |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (every cycle), liver function tests (ALT/AST/bilirubin), renal function (serum creatinine/CrCl — dose reduction required for CrCl 30–50 mL/min; use contraindicated below 30 mL/min), hand-foot syndrome (palmar-plantar erythrodysesthesia) grading at each visit |
| Handling Protection | Must follow cytotoxic drug handling and disposal regulations — oral cytotoxic agent requiring caregiver exposure precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. No SFDA-specific safety warnings, contraindications, or drug interaction data were retrievable from the available regulatory sources.

**Key considerations based on known pharmacology (to be verified against package insert):**
- **DPD Deficiency Risk:** Capecitabine is contraindicated in patients with known dihydropyrimidine dehydrogenase (DPD) deficiency. Pre-treatment DPYD genotyping is recommended per current international oncology guidelines. Prevalence of DPD-deficient alleles may vary in the Saudi population.
- **Renal Impairment:** Dose adjustment required for moderate renal impairment; contraindicated in severe impairment.
- **Drug Interactions:** Significant interactions known with warfarin (INR elevation risk), phenytoin, and leucovorin (potentiates 5-FU toxicity).

---

## Conclusion and Next Steps

### Decision: Proceed with Guardrails
*(Applicable to Gastric Tubular Adenocarcinoma, Rank 2, L1)*

---

### Note on Rank 1 TxGNN Prediction — GAPPS: **Hold**

The model's highest-scoring prediction is gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS, score 99.94%), a hereditary syndrome caused by APC gene promoter point mutations with fewer than 100 documented families worldwide. There are zero clinical trials, zero publications, and no mechanistic basis supporting capecitabine use in this ultra-rare subtype. The TxGNN score reflects model extrapolation from the broader gastric adenocarcinoma category, not direct support for GAPPS. This prediction should be treated as a probable false positive. **Decision: Hold.**

---

**Rationale (Gastric Tubular Adenocarcinoma):**
Capecitabine as part of the CAPOX regimen is supported by multiple Phase 3 RCTs as a global standard of care for gastric adenocarcinoma. The CLASSIC trial provides direct L1 evidence for adjuvant capecitabine following D2 gastrectomy. Gastric tubular adenocarcinoma—the dominant histological subtype in all these trials—high-expresses thymidine phosphorylase, providing a biologically sound mechanistic rationale. Evidence strength is sufficient to move forward, contingent on regulatory registration in Saudi Arabia.

**To proceed, the following is needed:**
- Submission of SFDA registration dossier or import permit application for capecitabine in Saudi Arabia
- Resolution of data gaps DG001 and DG002: download and parse the drug package insert for warnings/contraindications; retrieve MOA data from DrugBank API
- Establishment of pre-treatment DPYD genotyping protocol for the Saudi patient population
- Safety monitoring plan covering hand-foot syndrome (Grade ≥2 management algorithm), myelosuppression thresholds, and renal function surveillance
- Saudi Arabia gastric cancer burden and treatment gap analysis to quantify the target patient population
- Consultation with local oncology centers (e.g., KFMC, KFSH&RC) on feasibility of CAPOX regimen adoption
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

