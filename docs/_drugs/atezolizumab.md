---
layout: default
title: Atezolizumab
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
---

# Atezolizumab
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

# Atezolizumab: From Urothelial Carcinoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Atezolizumab (Tecentriq) is an anti-PD-L1 monoclonal antibody immunotherapy with established efficacy against urothelial carcinoma and multiple solid tumors at the international level, though it has not obtained SFDA registration in Saudi Arabia.
The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma** — a urothelial carcinoma subtype arising from the prostatic urethra — with a prediction score of **99.98%**.
Currently **2 clinical trials** support this direction (no dedicated published literature identified), and the mechanistic rationale is strong given the shared PD-L1 overexpression biology across urothelial carcinoma subsites.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no SFDA registration; internationally approved for urothelial carcinoma, NSCLC, TNBC, HCC) |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not marketed (0 SFDA licenses) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the system. Based on well-established pharmacological knowledge, atezolizumab is a humanized IgG1 monoclonal antibody that selectively binds to **PD-L1 (Programmed Death-Ligand 1)**, blocking its interactions with both PD-1 and B7.1 receptors. This blockade restores cytotoxic T-cell activity within the tumor microenvironment, allowing the immune system to recognize and destroy tumor cells that have evaded immune surveillance via the PD-L1/PD-1 axis.

Urothelial carcinomas — regardless of anatomical subsite (bladder, renal pelvis, ureter, or prostatic urethra) — share a common molecular signature: high PD-L1 expression on tumor cells and tumor-infiltrating immune cells, elevated tumor mutational burden (TMB), and a characteristically immunogenic microenvironment. The prostatic urethra is lined with transitional (urothelial) epithelium, making prostatic urethra urothelial carcinoma biologically equivalent to bladder urothelial carcinoma at the molecular level. The same immune evasion mechanism that makes bladder cancer responsive to atezolizumab is present in this subsite.

Atezolizumab's efficacy in bladder/urothelial carcinoma is well established internationally (FDA-approved for locally advanced or metastatic urothelial carcinoma), and Phase 2 clinical trial data in BCG-unresponsive non-muscle invasive bladder cancer (NCT02844816, n=172) directly validates the drug's activity against urothelial carcinomas that have evaded first-line treatment. The extension to the prostatic urethral subsite represents an anatomical extrapolation with strong mechanistic justification, consistent with how checkpoint inhibitors are generally applied across urothelial subsites in clinical practice.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02844816](https://clinicaltrials.gov/study/NCT02844816) | Phase 2 | Completed | 172 | Atezolizumab monotherapy in BCG-unresponsive non-muscle invasive bladder cancer (NMIBC); immunotherapy targeting PD-L1 to inhibit tumor growth in recurrent/refractory urothelial carcinoma |
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1b | Active, not recruiting | 914 | Cabozantinib ± atezolizumab in multiple solid tumors, explicitly including advanced urothelial carcinoma (bladder, renal pelvis, ureter, urethra), CRPC, RCC, NSCLC, TNBC; provides safety and PK data for combination use |

---

## Saudi Arabia Market Information

No SFDA marketing authorizations found for atezolizumab. The drug is not currently registered or marketed in Saudi Arabia.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — PD-L1 checkpoint inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Low (immune-related cytopenias possible but uncommon; primary risk is immune-mediated adverse events, not direct myelosuppression) |
| Emetogenicity Classification | Minimal (infusion-related reactions are the main acute concern, not emetogenicity) |
| Monitoring Items | CBC with differential, liver function tests (AST/ALT/bilirubin), thyroid function (TSH/free T4), renal function (creatinine), blood glucose, adrenal function; monitor for immune-related adverse events (irAEs) at each cycle |
| Handling Protection | Standard biologic/monoclonal antibody handling precautions apply; not classified as a traditional cytotoxic — closed-system drug transfer devices not mandated, but institutional biologic handling policies must be followed |

---

## Safety Considerations

Detailed SFDA-specific warnings and contraindications are not available (no local registration). Please refer to the international prescribing information (FDA label or EMA SmPC) for full safety information, including:

- Immune-related adverse events (pneumonitis, hepatitis, colitis, endocrinopathies, nephritis) requiring corticosteroid management or permanent discontinuation
- Infusion-related reactions
- Embryo-fetal toxicity (contraindicated in pregnancy)
- No drug-drug interaction data was identified in the current query

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Atezolizumab has a completed Phase 2 trial in BCG-unresponsive urothelial carcinoma (NCT02844816, n=172) and a large Phase 1b safety dataset in broad urothelial carcinoma (NCT03170960, n=914), with a strong and well-understood mechanistic rationale that directly extends to the prostatic urethral subsite. The absence of SFDA registration represents a regulatory, not a scientific, barrier.

**To proceed, the following is needed:**
- SFDA registration pathway assessment for atezolizumab in Saudi Arabia (or compassionate use / import license options)
- Subsite-specific efficacy data for prostatic urethra urothelial carcinoma (ideally from retrospective cohort or case series within NCT03170960's urothelial cohort)
- Full mechanism of action and safety data retrieval via DrugBank API (DG002 remediation)
- SFDA/local package insert review for Saudi Arabia-specific contraindications and warnings (DG001 remediation)
- Patient selection criteria based on PD-L1 expression testing (SP142 assay) and tumor mutational burden profiling
- Pharmacovigilance and monitoring plan aligned with Saudi Arabia SFDA post-marketing requirements
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

