---
layout: default
title: Dabigatran Etexilate
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 5
---

# Dabigatran Etexilate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Dabigatran Etexilate: From Anticoagulation to Sclerosing Cholangitis

## One-Sentence Summary

Dabigatran etexilate is an oral direct thrombin inhibitor (DTI) prodrug, approved globally (as Pradaxa) for prevention of stroke in non-valvular atrial fibrillation and treatment/prevention of venous thromboembolism, though it is currently not registered in Taiwan.
The TxGNN model predicts it may be effective for **Sclerosing Cholangitis** (TxGNN rank #1 among 5 predicted indications), with **0 clinical trials** and **1 tangentially related publication** currently available to support this direction.
Evidence is limited to model prediction level only, and a **Hold** decision is recommended pending mechanistic and clinical validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Taiwan regulatory database; globally approved for stroke prevention in atrial fibrillation and VTE treatment/prevention |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacology, dabigatran etexilate is a prodrug converted in vivo to dabigatran — a potent, competitive, and reversible direct inhibitor of thrombin (Factor IIa). Beyond its role in coagulation, thrombin also activates protease-activated receptors (PARs), particularly PAR-1 and PAR-2, which are expressed on hepatic stellate cells and cholangiocytes.

The TxGNN prediction for sclerosing cholangitis appears to be grounded in the thrombin–PAR-2–stellate cell fibrosis axis: thrombin signaling through PAR-2 may accelerate collagen deposition and biliary fibrosis, which is the defining pathological feature of primary sclerosing cholangitis (PSC) and secondary sclerosing cholangitis (SSC). By blocking thrombin, dabigatran could theoretically interrupt this pro-fibrotic cascade and slow disease progression.

However, this mechanistic link remains entirely hypothetical. No published preclinical or clinical studies have directly investigated dabigatran in any form of sclerosing cholangitis. The only retrieved literature item relates to cilofexor — an FXR agonist being developed for PSC — and was retrieved due to pharmacokinetic DDI methodology rather than any shared mechanism with dabigatran. The TxGNN model likely captured an indirect knowledge-graph path between the DTI class and biliary fibrosis nodes, but biological plausibility at the treatment level is currently unestablished.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | DDI Pharmacokinetic Study | Clinical Pharmacokinetics | Evaluated cilofexor (a selective FXR agonist under development for PSC and NASH) as a DDI victim and perpetrator via CYP450 and transporter pathways; not directly relevant to dabigatran efficacy in sclerosing cholangitis |

---

## Saudi Arabia Market Information

Dabigatran etexilate is not currently registered or marketed. No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited exclusively to TxGNN model prediction (L5); no clinical trials, no preclinical mechanistic studies, and no direct clinical literature support dabigatran in sclerosing cholangitis. While the thrombin → PAR-2 → biliary fibrosis hypothesis provides a conceptually accessible rationale, it has not been tested in any PSC/SSC model system, and the drug carries known bleeding risk that would require careful benefit–risk assessment in a hepatic disease context.

**To proceed, the following is needed:**
- Preclinical validation in bile duct ligation or Mdr2-knockout mouse models to test whether DTI treatment reduces biliary fibrosis markers
- Mechanism of action profile retrieval from DrugBank (DG002) to formally document PAR signaling and off-target interactions
- Complete safety data acquisition: TFDA package insert warnings and contraindications (DG001) and a DDI assessment against ursodeoxycholic acid, immunosuppressants, and biologics commonly co-prescribed in cholangitis
- Regulatory pathway assessment — dabigatran is marketed globally as Pradaxa but holds zero Taiwan registrations; market entry feasibility must be evaluated before any indication expansion
- Clarification on whether the sclerosing cholangitis target is PSC (autoimmune/idiopathic, high unmet need) or SSC (secondary, potentially preventable) — the mechanistic and clinical development pathway differs substantially between the two subtypes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

