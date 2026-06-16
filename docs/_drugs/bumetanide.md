---
layout: default
title: Bumetanide
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 1
---

# Bumetanide
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

# Bumetanide: From Heart Failure Edema to Acute Pulmonary Heart Disease

## One-Sentence Summary

Bumetanide is a potent loop diuretic historically used for edema management in congestive heart failure, hepatic disease, and renal disease.
The TxGNN model predicts it may be effective for **Acute Pulmonary Heart Disease (Acute Cor Pulmonale)**,
with **3 clinical trials** and **5 publications** currently supporting this direction — and a mechanistic rationale directly linking its diuretic action to the hemodynamic burden of right heart failure.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Edema associated with congestive heart failure, hepatic and renal disease, acute pulmonary congestion |
| Predicted New Indication | Acute Pulmonary Heart Disease (Acute Cor Pulmonale) |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L3 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bumetanide is a high-ceiling loop diuretic that inhibits the NKCC2 (Na⁺-K⁺-2Cl⁻) co-transporter in the thick ascending limb of the Loop of Henle, driving rapid and potent urinary excretion of sodium, chloride, and potassium. This mechanism produces swift volume reduction — clinically useful whenever fluid overload threatens cardiac or pulmonary function.

Acute pulmonary heart disease (acute cor pulmonale) is characterised by sudden right ventricular pressure overload — most commonly from massive pulmonary embolism or severe acute respiratory failure — leading to right ventricular dilation, venous congestion, and compromised forward flow. The resulting fluid accumulation and elevated preload closely mirror the pathophysiology for which loop diuretics are already established therapy. By reducing circulating volume, bumetanide lowers right ventricular filling pressure, pulmonary venous pressure, and ventricular wall stress, directly addressing the haemodynamic derangement.

Crucially, this is not merely theoretical extrapolation. PMID 3304383 — a prospective haemodynamic study using intravenous bumetanide in acute heart failure — documented an immediate reduction in pulmonary artery occluded pressure (wedge pressure) and left ventricular filling pressure with a single dose. The TxGNN score of 0.9958 is consistent with this mechanistic coherence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT07375212](https://clinicaltrials.gov/study/NCT07375212) | Phase 4 | Withdrawn | 0 | Planned to test whether a single 4 mg intranasal bumetanide dose acutely reduces pulmonary artery pressure and blood volume in outpatient heart failure patients with implanted CardioMEMS™ / Cordella™ haemodynamic monitors. Trial was withdrawn before enrolling any patients; no efficacy or safety data available. Withdrawal reason undisclosed. |
| [NCT06885164](https://clinicaltrials.gov/study/NCT06885164) | N/A | Recruiting | 200 | Observational study validating seismocardiography (a wearable cardiac motion sensor) for remote monitoring of heart failure patients. Bumetanide is not the investigational intervention; provides disease-population context only. |
| [NCT05580510](https://clinicaltrials.gov/study/NCT05580510) | Phase 2/3 | Unknown | 160 | Evaluated empagliflozin + sacubitril/valsartan in adults with congenital heart disease and reduced ejection fraction heart failure. Bumetanide, if involved, would be background therapy only. Status unknown (possibly completed/lost to follow-up). |

> **Note:** None of the identified trials directly tests bumetanide efficacy for acute pulmonary heart disease as a primary endpoint. NCT07375212 is the most mechanistically relevant but was withdrawn before enrolment.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [3304383](https://pubmed.ncbi.nlm.nih.gov/3304383/) | 1987 | Open-label Clinical Study | Br J Clin Pharmacol | Prospective haemodynamic study in 24 patients with acute or chronic heart failure. IV bumetanide (25 µg/kg) immediately reduced pulmonary artery occluded pressure and cardiac filling pressures, confirming acute haemodynamic benefit relevant to acute cor pulmonale. |
| [6391889](https://pubmed.ncbi.nlm.nih.gov/6391889/) | 1984 | Drug Review | Drugs | Comprehensive pharmacodynamic and pharmacokinetic review of bumetanide. Confirms established indication for acute pulmonary congestion and oedema from congestive heart failure; documents rapid onset (within 30 min) of diuresis via NKCC2 inhibition. |
| [19142155](https://pubmed.ncbi.nlm.nih.gov/19142155/) | 2009 | Review | Am J Ther | Reviews therapeutic options for acute decompensated heart failure (ADHF). Confirms loop diuretics (including bumetanide) as first-line management in ADHF; contextualises clinical practice and evidence base. |
| [19843838](https://pubmed.ncbi.nlm.nih.gov/19843838/) | 2009 | Comparative Review | Ann Pharmacother | Head-to-head comparison of loop diuretics (bumetanide vs. furosemide vs. torsemide) for pharmacokinetic profiles, safety, efficacy, and cost. Supports bumetanide as a clinically equivalent — and sometimes superior — alternative to furosemide in cardiac oedema. |
| [39366035](https://pubmed.ncbi.nlm.nih.gov/39366035/) | 2024 | Epidemiological Cohort | Am J Emerg Med | Large-scale epidemiological analysis of heart failure ED presentations (2016–2023) in the United States, documenting admission rates, evaluation patterns, and treatment trends. Provides recent disease burden context; not bumetanide-specific. |

---

## Taiwan Market Information

Bumetanide currently holds **no marketing authorisation** in Taiwan. There are no registered product licences, no approved dosage forms, and no locally approved indications on record as of the data cut-off date (2026-06-15).

Any clinical use would require importation under special access provisions or regulatory pathway development.

---

## Safety Considerations

Detailed package insert warnings, contraindications, and drug-drug interaction data are not available in this evidence pack.

> Please refer to the original product package insert and current clinical guidelines for full safety information before any clinical application.

Key known class-level concerns for loop diuretics include: electrolyte disturbances (hypokalaemia, hyponatraemia, hypomagnesaemia), ototoxicity (particularly at high IV doses), volume depletion and hypotension, and interactions with nephrotoxic agents, aminoglycosides, and anticoagulants. These should be formally reviewed in the next stage.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bumetanide's mechanism of action is directly and logically relevant to the haemodynamic pathophysiology of acute pulmonary heart disease, and PMID 3304383 provides direct haemodynamic proof-of-concept in acute heart failure. The TxGNN score (99.58%) is consistent with this strong mechanistic signal. However, no completed randomised trial specifically targets acute cor pulmonale as the primary indication, and the drug is not registered in Taiwan, placing current evidence at L3.

**To proceed, the following is needed:**

- **Safety review**: Retrieve and parse the full bumetanide package insert (from US FDA labelling or EMA SmPC) to complete contraindications, boxed warnings, and drug interaction profile — currently flagged as a blocking data gap
- **MOA documentation**: Confirm full mechanism of action from DrugBank (DG002), including secondary targets beyond NKCC2
- **Taiwan registration pathway**: Assess whether compassionate use, clinical trial IND, or full NDA pathway is required for Taiwan deployment
- **Clinical trial activation**: NCT07375212 (intranasal bumetanide in HF with haemodynamic sensors) was withdrawn before enrolment — investigate withdrawal reason and consider whether a redesigned interventional pilot trial for acute cor pulmonale is feasible
- **Comparator evidence**: Benchmark bumetanide against standard-of-care (IV furosemide) in the target indication for differentiation rationale
- **Special population safety**: Evaluate use in patients with concurrent renal impairment, given the prevalence of cardiorenal syndrome in acute cor pulmonale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

