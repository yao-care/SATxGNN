---
layout: default
title: Vasopressin
parent: 僅模型預測 (L5)
nav_order: 658
evidence_level: L5
indication_count: 2
---

# Vasopressin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Vasopressin: From Diabetes Insipidus to Congenital Prothrombin Deficiency

## One-Sentence Summary

Vasopressin is a peptide hormone classically used for diabetes insipidus and as a vasopressor/antidiuretic agent; it currently holds **no marketing authorization in Saudi Arabia**, so a locally-confirmed original indication cannot be cited. The TxGNN model predicts a possible role in **Congenital Prothrombin Deficiency**, but this is supported only by **0 clinical trials** and **3 tangentially related publications** — none of which actually study prothrombin deficiency.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed for Saudi Arabia (no license on file); classically diabetes insipidus / vasopressor support based on general pharmacological knowledge |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on the drug's known pharmacology, vasopressin and its analogue DDAVP act through the **V2 receptor** on vascular endothelial cells, triggering release of **von Willebrand factor (vWF)** and **Factor VIII** stored in Weibel-Palade bodies. This mechanism is specific to the vWF/Factor VIII axis.

Prothrombin (Factor II) is a vitamin K–dependent clotting factor synthesized in the liver through an entirely separate pathway. There is **no direct mechanistic link** between vasopressin's V2-receptor-mediated vWF/FVIII release and prothrombin synthesis or activity. The three supporting publications discuss combined Factor V/VIII deficiency, acquired hemophilia A (Factor VIII inhibitors), and DDAVP use in Factor VIII replacement — none address prothrombin deficiency specifically. The TxGNN score therefore reflects a broad "coagulation factor / hemostasis" knowledge-graph association rather than a disease-specific mechanistic rationale, and the connection should be treated as indirect and unproven.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | Reviews acquired hemophilia A (autoantibodies against Factor VIII); does not address prothrombin deficiency |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case Report | Rinsho Ketsueki | Cesarean delivery in a patient with combined Factor V/VIII deficiency managed with FVIII concentrate replacement |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case Report | Rinsho Ketsueki | DDAVP administration in a patient with congenital combined Factor V and Factor VIII deficiency |

**Note:** None of the retrieved literature directly studies congenital prothrombin (Factor II) deficiency; all relate to Factor V/VIII pathways, which is a different coagulation axis.

---

## Saudi Arabia Market Information

Vasopressin currently has no marketing authorization on file in Saudi Arabia (market status: 未上市 / Not marketed, 0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA warnings and contraindications are listed as a **Blocking** data gap — DG001 — and could not be retrieved for this evaluation; drug interaction query returned no results.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by mechanism-level evidence (L4) with no clinical trials and no literature directly studying the predicted indication; the drug also lacks Saudi Arabia market authorization and has a **Blocking** safety data gap (missing TFDA warnings/contraindications) that prevents an S1 safety pre-assessment.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (DG001, blocking — must be resolved before any safety review)
- Confirmed mechanism of action data (DG002)
- Literature or preclinical studies specifically addressing prothrombin deficiency (current evidence only covers Factor V/VIII pathways)
- Saudi Arabia regulatory/licensing pathway assessment, given the drug is not currently marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

