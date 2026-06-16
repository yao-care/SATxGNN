---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
---

# Durvalumab
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

# Durvalumab: From Urothelial Carcinoma to Prostatic Urethra Urothelial Carcinoma and Beyond

---

## One-Sentence Summary

Durvalumab (IMFINZI) is an anti-PD-L1 monoclonal antibody checkpoint inhibitor approved in multiple markets for urothelial carcinoma and non-small cell lung cancer, though not currently registered in Saudi Arabia.
The TxGNN model predicts it may be effective for **10 rare urothelial and gynecological cancer subtypes** — the highest TxGNN score goes to **Prostatic Urethra Urothelial Carcinoma** (99.98%), while **Endocervical Carcinoma** (Rank #6) carries the strongest clinical evidence with **2 clinical trials and 1 publication**.
Evidence levels range from **L2 to L5** across predicted indications; most require further investigation before clinical translation, with endocervical carcinoma as the one actionable candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Urothelial carcinoma, NSCLC, biliary tract cancer (approved in other markets; original indication data not captured in this Evidence Pack) |
| Predicted New Indication (Top TxGNN Score) | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% (Rank #746) |
| Evidence Level (Rank #1 Indication) | L5 — Model prediction only |
| Best-Evidenced Indication | Endocervical Carcinoma (Rank #6, L2) |
| Saudi Arabia Market Status | ✗ Not Marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (7 indications) · Research Question (2 indications) · Proceed with Guardrails (Endocervical Carcinoma) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack (Data Gap DG002). Based on known pharmacological information, Durvalumab is a human IgG1 monoclonal antibody that selectively blocks PD-L1 from binding its receptors PD-1 and CD80, thereby restoring T-cell-mediated immune surveillance against tumors. This mechanism — immune checkpoint blockade at the PD-L1 node — has proven effective across multiple solid tumors where PD-L1 upregulation enables immune evasion.

The 10 predicted indications cluster around two biological themes. The first group comprises **urothelial/transitional cell carcinoma subtypes** (prostatic urethra, kidney pelvis sarcomatoid, bladder sarcomatoid variant, renal pelvis papillary), where PD-L1 expression is documented at 30–60% in conventional urothelial carcinoma and is notably higher (>60% in some studies) in sarcomatoid variants due to epithelial-mesenchymal transition (EMT) activation and elevated tumor mutational burden (TMB). The second group comprises **gynecological adenocarcinoma subtypes** (endocervical, uterine ligament variants, cervical mucinous variants), where HPV-driven immune evasion — including PD-L1 upregulation — creates a theoretical basis for checkpoint inhibition. Importantly, the related anti-PD-1 agent pembrolizumab is already FDA-approved for cervical cancer, validating the PD-1/PD-L1 axis as a clinically meaningful target in this tumor class.

The mechanistic rationale is strongest for **sarcomatoid urothelial variants** (EMT, high PD-L1, high TMB) and **HPV-positive endocervical carcinoma** (PD-L1 upregulation in ~30–60% of cases). It is weakest for adenoid cystic carcinoma of the cervix (typically immunologically cold, TMB-low) and signet ring cell/intestinal mucinous cervical variants (immunosuppressive tumor microenvironment unless MSI-H).

---

## All Predicted Indications — Summary

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|----------------|----------|
| 1 | Prostatic Urethra Urothelial Carcinoma | 99.98% | L5 | Hold |
| 2 | Kidney Pelvis Sarcomatoid TCC | 99.98% | L4 | Research Question |
| 3 | Infiltrating Bladder UC Sarcomatoid Variant | 99.98% | L3 | Research Question |
| 4 | Renal Pelvis Papillary UC | 99.98% | L5 | Hold |
| 5 | Uterine Ligament Adenocarcinoma | 99.92% | L5 | Hold |
| **6** | **Endocervical Carcinoma** | **99.91%** | **L2** | **Proceed with Guardrails** |
| 7 | Adenoid Cystic Carcinoma of Cervix Uteri | 99.91% | L5 | Hold |
| 8 | Uterine Ligament Serous Adenocarcinoma | 99.91% | L5 | Hold |
| 9 | Signet Ring Cell Variant Cervical Mucinous Adenocarcinoma | 99.90% | L5 | Hold |
| 10 | Intestinal Variant Cervical Mucinous Adenocarcinoma | 99.90% | L5 | Hold |

---

## Clinical Trial Evidence

Clinical trial evidence exists for Indications #2, #3, and #6 only. Indications #1, #4, #5, #7, #8, #9, and #10 have no registered clinical trials.

### For Indication #3 — Infiltrating Bladder UC Sarcomatoid Variant

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03912818](https://clinicaltrials.gov/study/NCT03912818) | Phase 2 | Terminated | 7 | Durvalumab + neoadjuvant chemotherapy in variant histology bladder cancer. **Critical signal**: terminated after enrolling only 7 patients (far below target). Termination reason must be clarified — if due to insufficient efficacy, this is a significant negative signal; if due to accrual/funding difficulties, the indication may warrant re-evaluation. |
| [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) | Early Phase 1 | Active, Not Recruiting | 54 | Durvalumab + Tremelimumab (dual checkpoint: anti-PD-L1 + anti-CTLA-4) pre-surgical in muscle-invasive, cisplatin-ineligible high-risk urothelial carcinoma. Covers the broader urothelial population including bladder; dual checkpoint blockade may offer additional synergy for sarcomatoid variants. Indirect relevance only. |

### For Indication #2 — Kidney Pelvis Sarcomatoid TCC

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) | Early Phase 1 | Active, Not Recruiting | 54 | Same trial as above — the urothelial carcinoma population may include upper tract (renal pelvis) cases. Not designed for sarcomatoid TCC of the kidney pelvis. Indirect relevance; supports the broader concept of durvalumab in urothelial disease. |

### For Indication #6 — Endocervical Carcinoma

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04065269](https://clinicaltrials.gov/study/NCT04065269) | Phase 2 | Active, Not Recruiting | 174 | **ATARI trial**: ceralasertib (ATR inhibitor) alone or combined with olaparib or durvalumab in relapsed gynecological cancers, stratified by ARID1A loss. Largest available dataset (n=174). Key limitation: three-drug combination arms make it difficult to isolate durvalumab's independent contribution; patient selection is biomarker-driven (DDR deficiency). Expected completion August 2026. |
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | Completed | 20 | Hypofractionated radiotherapy + durvalumab + tremelimumab in recurrent/metastatic cervical, vaginal, or vulvar cancers. **Completed** — safety profile of durvalumab in the cervical cancer population has been established. Publication status of results should be confirmed. |

---

## Literature Evidence

Literature was found for Indication #6 (Endocervical Carcinoma) only. Indications #1–5 and #7–10 have no related publications in the Evidence Pack search.

### For Indication #6 — Endocervical Carcinoma

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Review | Biomedical Journal | Molecular basis and therapeutic advances in small cell neuroendocrine carcinoma of the cervix (SCNECC). Discusses HPV association, evidence gaps in rare cervical subtypes, and immunotherapy potential. Indirectly informs PD-L1 pathway rationale for endocervical carcinoma; direct evidence for durvalumab not addressed. |

---

## Saudi Arabia Market Information

Durvalumab has no registered authorizations in Saudi Arabia (0 licenses, not marketed). No authorization records to display.

---

## Cytotoxicity

Durvalumab is an antineoplastic drug (immune checkpoint inhibitor targeting PD-L1 in solid tumors). This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted immunotherapy — Immune Checkpoint Inhibitor (anti-PD-L1 IgG1 monoclonal antibody); not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Low — mechanism does not directly suppress bone marrow; immune-mediated cytopenias (e.g., immune thrombocytopenia, hemolytic anemia) are rare but recognized immune-related adverse events (irAEs) |
| Emetogenicity Classification | Minimal — IV biologic; emetogenic risk is negligible compared to conventional chemotherapy |
| Monitoring Items | CBC with differential (baseline and periodic), liver function (ALT/AST — immune hepatitis), thyroid function (TSH/fT4 — thyroiditis), creatinine/BUN (immune nephritis), blood glucose (immune endocrinopathy), pulmonary assessment (chest imaging if pneumonitis symptoms) |
| Handling Protection | Standard biohazard precautions for injectable biologics; specialized cytotoxic handling protocols (closed system, double glove, negative pressure) are **not** required for monoclonal antibodies under most institutional guidelines — verify against local pharmacy SOPs |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data were not available in this Evidence Pack. TFDA package insert retrieval is flagged as a **Blocking** data gap [DG001] and must be resolved before safety screening can proceed. No drug-drug interactions were identified in the DDI database query.)*

---

## Conclusion and Next Steps

### Endocervical Carcinoma (Rank #6) — **Proceed with Guardrails**

**Rationale:**
The PD-1/PD-L1 axis is clinically validated in cervical cancer (pembrolizumab holds FDA approval), HPV-driven PD-L1 upregulation provides a strong mechanistic basis, and durvalumab specifically is under active investigation in gynecological cancer clinical trials (Phase 1 completed, Phase 2 active with n=174), placing this indication at evidence Level L2.

**To proceed, the following is needed:**
- Confirm endocervical carcinoma representation within NCT04065269 and obtain interim efficacy readouts
- Retrieve published results from completed NCT03452332 (Phase 1 safety data)
- Define biomarker strategy: PD-L1 IHC (CPS ≥1 or ≥10), HPV status, MSI/MMR, TMB
- Initiate Saudi Arabia regulatory pathway: durvalumab requires full NDA/BLA submission or compassionate use framework (0 current authorizations)
- Resolve Blocking data gap DG001: retrieve SFDA/TFDA package insert for safety screening

---

### Urothelial Sarcomatoid Variants — Indications #2 and #3 — **Research Question**

**Rationale:**
Sarcomatoid variants carry elevated PD-L1 expression and strong immunological rationale, but NCT03912818 (the only Phase 2 trial directly targeting variant histology bladder cancer with durvalumab) was terminated with only 7 patients enrolled — a critical negative signal. The cause of termination is unknown and determines whether this indication warrants further investment.

**To proceed, the following is needed:**
- Investigate and document termination reason for NCT03912818
- Biomarker characterization of sarcomatoid TCC: PD-L1 expression, TMB, EMT marker profile
- Explore basket trial inclusion or investigator-initiated study design for rare sarcomatoid urothelial subtypes

---

### All Other Indications (#1, #4, #5, #7, #8, #9, #10) — **Hold**

**Rationale:**
These 7 indications have no clinical trials or literature support. TxGNN scores reflect knowledge-graph topological proximity to adjacent cancer nodes — not clinical validation. Specific mechanistic concerns include: adenoid cystic carcinoma of the cervix is typically immunologically cold (TMB-low, PD-L1 negative, poor historical response to ICIs); signet ring cell and intestinal variants respond poorly to ICI unless MSI-H/dMMR; uterine ligament adenocarcinomas have near-zero PD-L1 characterization data.

**Minimum requirements before reconsideration:**
- Subtype-specific PD-L1 expression and TMB data
- At least preclinical evidence (cell line or patient-derived xenograft) for direct mechanistic support
- Biomarker-selected patient identification criteria (MSI-H, TMB-H, PD-L1 CPS) before any prospective study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

