---
layout: default
title: Avelumab
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
---

# Avelumab
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

# Avelumab: From Urothelial Carcinoma to Human Herpesvirus 8-Related Tumor

## One-Sentence Summary

Avelumab (Bavencio) is a fully human anti-PD-L1 IgG1 monoclonal antibody checkpoint inhibitor, FDA-approved for the maintenance treatment of locally advanced or metastatic urothelial carcinoma and Merkel cell carcinoma. The TxGNN model predicts it may be effective for **Human Herpesvirus 8-Related Tumor** (encompassing Kaposi's sarcoma and primary effusion lymphoma), with a prediction score of 99.97% — however, **no clinical trials or published literature** currently support this specific repurposing direction, and a critical mechanistic caveat applies: HHV-8-related tumors disproportionately arise in immunocompromised hosts where T cell effectors are severely depleted, raising a fundamental paradox for a T cell-restoring agent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Urothelial carcinoma (locally advanced / metastatic, first-line maintenance); Merkel cell carcinoma (FDA-approved) |
| Predicted New Indication | Human Herpesvirus 8-Related Tumor |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Avelumab blocks the interaction between PD-L1 and its receptors (PD-1 and B7.1), restoring T cell-mediated anti-tumor immunity. Uniquely among PD-L1 inhibitors, its IgG1 Fc domain retains antibody-dependent cellular cytotoxicity (ADCC) activity, meaning it can directly engage NK cells to kill PD-L1-expressing tumor cells independent of the T cell axis. Its proven clinical activity in Merkel cell carcinoma — itself a virus-associated (Merkel cell polyomavirus) malignancy — establishes a conceptual precedent for efficacy in virally driven tumors.

Human herpesvirus 8 (HHV-8) drives tumor formation through a well-described immune evasion mechanism: viral latency proteins upregulate PD-L1 on infected cells, suppressing T cell recognition and creating an immunosuppressive tumor microenvironment. This makes PD-L1 blockade mechanistically coherent for HHV-8-associated malignancies such as Kaposi's sarcoma and primary effusion lymphoma. The fact that Avelumab's ADCC activity could additionally target PD-L1-overexpressing HHV-8-infected cells through NK cell recruitment adds a second mechanistic rationale beyond T cell restoration.

However, the critical clinical complication is population-level immune status. The vast majority of HHV-8-related tumor patients are immunocompromised — HIV-positive individuals with AIDS-related Kaposi's sarcoma, or solid organ transplant recipients. In these patients, functional T cells are severely depleted or pharmacologically suppressed. PD-L1 blockade requires intact T cell effectors to exert its primary effect; without them, therapeutic benefit is uncertain. Worse, checkpoint inhibitor-induced irAEs (immune pneumonitis, colitis, hepatitis) may be unpredictable or amplified in the setting of pre-existing immune dysregulation. Any clinical development plan must rigorously stratify by immune status before proceeding.

---

## Clinical Trial Evidence

Currently no clinical trials registered for avelumab in human herpesvirus 8-related tumor.

---

## Literature Evidence

Currently no related literature available for avelumab in human herpesvirus 8-related tumor.

---

## Saudi Arabia Market Information

Avelumab has no registered authorizations in Saudi Arabia (0 licenses on record). The drug is not currently marketed in the Saudi Arabia market.

---

## Cytotoxicity

Avelumab is an anti-cancer monoclonal antibody (checkpoint immunotherapy) used for malignant indications, and is classified under antineoplastic agents.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — Anti-PD-L1 checkpoint inhibitor (fully human IgG1 monoclonal antibody with ADCC activity) |
| Myelosuppression Risk | Low (not conventionally myelosuppressive; immune-related hematologic events such as hemolytic anemia and thrombocytopenia are rare but reported) |
| Emetogenicity Classification | Minimal to low (infusion-related reactions are the primary acute concern, rather than nausea/vomiting) |
| Monitoring Items | Liver function tests (immune hepatitis), TSH / free T4 (immune thyroiditis), CBC with differential, serum creatinine (immune nephritis), fasting glucose / HbA1c (immune-related diabetes mellitus), chest imaging (immune pneumonitis), infusion reaction observation during and post-infusion |
| Handling Protection | Standard biologic / monoclonal antibody handling protocols; cytotoxic drug containment facilities not required |

---

## Safety Considerations

No SFDA package insert warnings or contraindications are available in the current dataset (data gap). No drug-drug interaction data was retrieved.

Based on the established pharmacological class (anti-PD-L1 checkpoint inhibitor), the following safety considerations are clinically relevant and should be reviewed against the originator's package insert (Bavencio® prescribing information):

- **Immune-Related Adverse Events (irAEs):** Pneumonitis, hepatitis, colitis, endocrinopathies (thyroiditis, adrenal insufficiency, type 1 diabetes mellitus), nephritis, and dermatitis may occur and require early recognition, corticosteroid management, and potential permanent discontinuation.
- **Infusion Reactions:** Premedication with antihistamine and acetaminophen is required prior to the first 4 infusions; severe infusion reactions mandate permanent discontinuation.
- **Special Population Concern (HHV-8 context):** Use in immunocompromised patients (HIV-positive, transplant recipients) has not been formally studied; irAE behavior in pre-existing immune dysregulation is unpredictable and may be severe.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the TxGNN prediction score is high (99.97%) and a plausible mechanistic link exists through PD-L1 upregulation in HHV-8-driven tumor microenvironments, this remains a pure model prediction (Evidence Level L5) with zero supporting clinical trials or published literature. More critically, the paradox between avelumab's T cell-dependent mechanism and the T cell-deficient host environment that characterizes most HHV-8-related tumor patients constitutes a patient-safety concern that must be systematically addressed before any clinical development is proposed.

**To proceed, the following is needed:**

- **Biomarker profiling:** PD-L1 IHC and TMB characterization of HHV-8-related tumor specimens, stratified by host immune status (HIV+ vs. HIV−, CD4 count ≥ or < 200 cells/μL)
- **Safety precedent review:** Systematic literature search for published case reports or retrospective series of any PD-1/PD-L1 inhibitor use in AIDS-related Kaposi's sarcoma or PEL
- **Preclinical feasibility:** In vitro cytotoxicity data (ADCC assay) of avelumab against HHV-8-positive cell lines (e.g., BC-1, BCBL-1 for PEL; SLK for KS)
- **MOA data gap:** Full DrugBank MOA extraction to confirm ADCC mechanism and its potential relevance in ADCC-competent vs. ADCC-deficient immune environments
- **Package insert data gap:** Retrieve SFDA/TFDA-approved package insert warnings and contraindications to complete S1 safety screening
- **Clinical framework:** If evidence supports proceeding, design as a biomarker-selected basket trial with mandatory HIV/immunosuppression stratification and enhanced irAE monitoring protocol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

