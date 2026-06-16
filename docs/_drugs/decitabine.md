---
layout: default
title: Decitabine
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 1
---

# Decitabine
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

# Decitabine: From Myelodysplastic Syndrome to Refractory Cytopenia of Childhood

## One-Sentence Summary

Decitabine is a DNA hypomethylating agent (DNMTi) used to treat myelodysplastic syndrome (MDS) in adults, acting by inhibiting DNA methyltransferases to reactivate epigenetically silenced hematopoietic differentiation genes.
The TxGNN model predicts it may be effective for **Refractory Cytopenia of Childhood (RCC)** — a rare pediatric MDS subtype driven by the same epigenetic pathophysiology —
with **0 registered clinical trials** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myelodysplastic Syndrome (MDS) in adults |
| Predicted New Indication | Refractory Cytopenia of Childhood (RCC) |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Decitabine is a DNA methyltransferase inhibitor (DNMTi) that incorporates into replicating DNA and traps DNMT enzymes, leading to progressive hypomethylation of previously silenced genomic regions. In adult MDS, this mechanism reactivates differentiation-promoting genes suppressed by aberrant epigenetic silencing — restoring partial hematopoietic output and delaying disease progression. Currently, detailed mechanism of action data from DrugBank is not available in this Evidence Pack, but decitabine's DNMTi mechanism is well-established in the published literature and underpins its regulatory approval for adult MDS.

Refractory Cytopenia of Childhood (RCC) is a distinct pediatric MDS subtype defined by chronic peripheral cytopenias with hypocellular marrow and minimal blasts. Its core pathology is epigenetic dysregulation of hematopoietic stem and progenitor cells — the same target pathway as decitabine's mechanism of action. This makes the TxGNN prediction mechanistically direct rather than analogical: both conditions share the DNMTi-targetable epigenetic axis driving ineffective hematopoiesis.

Clinically, decitabine has already been used in pediatric MDS settings as part of a low-intensity bridging regimen (DAC + minimally myelosuppressive regimen) prior to allogeneic hematopoietic stem cell transplantation (allo-HSCT), which is currently the only curative therapy for RCC. This real-world clinical precedent in the overlapping pediatric MDS population supports the biological plausibility of this repurposing prediction, even in the absence of RCC-specific trial data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35624441](https://pubmed.ncbi.nlm.nih.gov/35624441/) | 2022 | Retrospective Cohort | BMC Pediatrics | Single-center 10-year experience using decitabine combined with a minimally myelosuppressive regimen (DAC + MMR) as a bridge to allo-HSCT in children with MDS; reports feasibility and clinical outcomes of this hypomethylating bridge strategy in the pediatric population |

---

## Saudi Arabia Market Information

Decitabine is currently not marketed in Saudi Arabia. No product authorizations are on record.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted epigenetic therapy — DNA hypomethylating agent (nucleoside analogue / DNMTi class) |
| Myelosuppression Risk | High — neutropenia, thrombocytopenia, and anemia are dose-limiting toxicities; of particular concern in pediatric RCC patients who present with pre-existing cytopenias at baseline |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (before each cycle and as clinically indicated), serum creatinine and BUN, liver function tests (AST, ALT, total bilirubin), serum electrolytes |
| Handling Protection | Must follow cytotoxic drug handling regulations — closed-system drug transfer devices (CSTD) and appropriate personal protective equipment (PPE) required |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for using decitabine in RCC is scientifically direct — both conditions share the DNMTi-targetable epigenetic dysregulation of hematopoiesis — but the current evidence consists of a single retrospective pediatric MDS study with no RCC-specific data and zero registered clinical trials for this indication. The absence of Saudi Arabia market authorization further constrains near-term clinical deployment.

**To proceed, the following is needed:**
- RCC-specific efficacy and safety data, or a subgroup analysis from existing pediatric MDS cohort studies
- Formal MOA documentation via DrugBank API (Data Gap DG002)
- Regulatory pathway assessment for decitabine market authorization in Saudi Arabia
- Pediatric pharmacokinetic and dosing data specific to the RCC patient population (lower body weight, pre-existing cytopenias)
- A prospective safety monitoring protocol addressing high myelosuppression risk in children with baseline cytopenias
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

