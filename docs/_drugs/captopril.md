---
layout: default
title: Captopril
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L5
indication_count: 4
---

# Captopril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Captopril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Captopril is the first oral ACE (angiotensin-converting enzyme) inhibitor, globally established for the treatment of hypertension and heart failure, but currently carrying no registered product license in Saudi Arabia.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease** (rank 1) and **Malignant Renovascular Hypertension** (rank 2), with **0 clinical trials** but **1 and 20 publications** respectively supporting these directions.
Evidence quality is limited (L4 for rank 1, L3 for rank 2), and two data gaps — including a Blocking gap on safety data — prevent advancement to full evaluation at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, heart failure (globally established; no Saudi Arabia product registration found) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L4 (rank 1: malignant hypertensive renal disease) / L3 (rank 2: malignant renovascular hypertension) |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Captopril is the first clinically approved ACE inhibitor. Although detailed MOA data is not available in this Evidence Pack, Captopril's mechanism is well-established in the pharmacological literature: it competitively inhibits angiotensin-converting enzyme, blocking the conversion of Angiotensin I to Angiotensin II. This lowers systemic vascular resistance, reduces aldosterone secretion, and decreases efferent arteriolar tone in the kidney — directly targeting the renin-angiotensin-aldosterone system (RAAS).

For **malignant hypertensive renal disease** (rank 1), the RAAS is typically hyperactivated, driving severe end-organ damage including hypertensive nephropathy. Blocking Angiotensin II production has direct mechanistic relevance. However, the single literature citation retrieved (PMID 28902735) describes captopril renography as a **diagnostic procedure** rather than a therapeutic intervention, and does not constitute efficacy evidence for treatment. This is an important distinction: the TxGNN model appears to have matched on the term "captopril" in a diagnostic context, not a therapeutic one.

For **malignant renovascular hypertension** (rank 2), the mechanistic link is far stronger and clinically well-recognized. Renovascular hypertension arises when renal artery stenosis reduces renal perfusion, triggering excess renin release and downstream Angiotensin II elevation — exactly the pathway that Captopril blocks. Multiple observational studies and cohort data (see Literature Evidence below) support this use. One critical safety constraint applies: Captopril is pharmacologically contraindicated in **bilateral renal artery stenosis or stenosis of a solitary functioning kidney**, where ACE inhibition eliminates the efferent arteriolar tone needed to maintain glomerular filtration, risking acute renal failure. Vascular imaging to exclude bilateral stenosis must precede any clinical use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Captopril in Malignant Hypertensive Renal Disease.

---

## Literature Evidence

The single paper retrieved for rank 1 describes captopril renography as a diagnostic tool, not a treatment. Because it offers no therapeutic evidence, the more substantive literature base for rank 2 (**Malignant Renovascular Hypertension**, L3) is presented below as the primary evidence table.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [232024](https://pubmed.ncbi.nlm.nih.gov/232024/) | 1979 | Clinical Study | Clinical Science | Captopril and saralasin induced PRA increases >14 ng/h/ml in 43/44 patients with renovascular hypertension; response absent in normal-renin essential hypertension — establishes captopril as a pharmacological probe and antihypertensive in renin-dependent states |
| [6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/) | 1984 | Clinical Observational Study | Bulletin of All-Union Cardiology Centre | Direct clinical use of captopril in arterial hypertension with both stable and malignant course |
| [3894732](https://pubmed.ncbi.nlm.nih.gov/3894732/) | 1985 | Cohort Study | Japanese Journal of Medicine | Evaluated captopril challenge test in diagnosis of renovascular hypertension; emphasized role of sodium balance; supports captopril's pivotal RAAS-targeting role |
| [2887673](https://pubmed.ncbi.nlm.nih.gov/2887673/) | 1987 | Experimental/Mechanistic Study | Japanese Heart Journal | Characterized neurohormonal changes (PRA, Ang I/II, catecholamines) in benign and malignant phases of Goldblatt (2K2C) hypertension; confirms RAAS hyperactivation in malignant phase |
| [2040938](https://pubmed.ncbi.nlm.nih.gov/2040938/) | 1991 | Review | Journal of Pediatrics | Review of malignant hypertension including pathophysiology and treatment options in pediatric context |
| [8070421](https://pubmed.ncbi.nlm.nih.gov/8070421/) | 1994 | Review | Endocrinology & Metabolism Clinics of North America | Renin-secreting (JGC) tumors cause severe hypertension and hypokalemia; blood pressure drops with ACE inhibition (captopril), demonstrating renin-dependence |
| [10955932](https://pubmed.ncbi.nlm.nih.gov/10955932/) | 2000 | Case Series | Pediatric Nephrology | 27 NF1 patients; captopril challenge test used to assess renovascular involvement; secondary hypertension profile documented |
| [11334320](https://pubmed.ncbi.nlm.nih.gov/11334320/) | 2001 | Case Report + Review | Clinical Nephrology | Two cases of renovascular hypertension with NF1; captopril stimulation test showed marked PRA rise (2.8 → 12.6 ng/ml/h), confirming renin-mediated mechanism |
| [17008836](https://pubmed.ncbi.nlm.nih.gov/17008836/) | 2006 | Review | Minerva Medica | Clinical concepts of renovascular hypertension; treatment strategies targeting renal ischemia including RAAS blockade |
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Case Report | Clinical Nuclear Medicine | Positive captopril renography in a patient with chromophobe renal cell carcinoma (no renal artery stenosis); renin-dependent hypertension resolved after nephrectomy — illustrates renin-dependency mechanism but is diagnostic, not therapeutic evidence |

---

## Saudi Arabia Market Information

Captopril is currently **not registered** with the Saudi Food and Drug Authority (SFDA). No product licenses, approved dosage forms, or indication texts were found in the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical clinical note from mechanistic knowledge**: ACE inhibitors including captopril carry a well-established contraindication in bilateral renal artery stenosis or stenosis of a solitary functioning kidney — conditions that are directly relevant given the two primary predicted indications. Use in these scenarios can precipitate acute renal failure by abolishing angiotensin II-mediated efferent arteriolar tone. Renal vascular imaging to exclude bilateral stenosis is mandatory before any clinical application. This concern must be formally captured once the SFDA package insert is retrieved (Data Gap DG001, Blocking severity).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking data gap (SFDA/TFDA package insert and formal contraindication data, DG001) prevents entry into S1 safety pre-screening, and the primary TxGNN-predicted indication (malignant hypertensive renal disease, rank 1) is supported by only one publication describing a diagnostic procedure rather than a therapeutic effect. The mechanistically stronger indication (malignant renovascular hypertension, rank 2) has observational support (L3) and sound pharmacological rationale, but also carries a critical safety constraint — bilateral renal artery stenosis contraindication — that cannot be formally evaluated without the full package insert.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Retrieve SFDA or TFDA package insert to capture formal contraindications, warnings, and special population data before advancing to S1 safety evaluation
- **[DG002 — High]** Confirm mechanism of action details via DrugBank API to support mechanistic linkage analysis
- Bilateral renal artery stenosis exclusion protocol must be defined before any clinical use in renovascular indications
- Dedicated prospective registry or controlled study data for Captopril in malignant hypertensive renal disease is needed to elevate rank 1 beyond L4
- Evaluate SFDA registration pathway for Captopril — currently unregistered, requiring a full market authorization application before any Saudi Arabia deployment
- Renal function monitoring protocol (serum creatinine, serum potassium, GFR) to be specified for the target population
- Indications ranked 3 and 4 (pulmonary hypertension, both L5, S0) are **not recommended for further investigation**: current ESC/ERS 2022 guidelines do not support ACE inhibitor use in any pulmonary arterial hypertension category, and the retrieved literature for these indications contains no captopril-specific therapeutic evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

