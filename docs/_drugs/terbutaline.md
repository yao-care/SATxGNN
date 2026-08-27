---
layout: default
title: Terbutaline
parent: 僅模型預測 (L5)
nav_order: 610
evidence_level: L5
indication_count: 3
---

# Terbutaline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Terbutaline: From Asthma Bronchodilator Therapy to Obstructive Lung Disease

## One-Sentence Summary

> Terbutaline is a short-acting β2-adrenergic bronchodilator whose long-standing clinical role has been relief of asthma-related bronchospasm.
> The TxGNN model predicts it may also be broadly relevant to **Obstructive Lung Disease** (a category spanning asthma and COPD),
> with **48 clinical trials** and **20 publications** currently supporting this direction — though much of this evidence reflects terbutaline's already-established use rather than a wholly novel therapeutic hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No locally-approved indication text available (drug not marketed here, 0 licenses); general pharmacological classification is a short-acting β2-adrenergic bronchodilator used for asthma-related bronchospasm |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, terbutaline is a short-acting β2-adrenergic receptor agonist (SABA) — the same drug class as salbutamol — that relaxes bronchial smooth muscle to relieve bronchospasm. TxGNN's very high-confidence prediction (99.96%) linking terbutaline to "Obstructive Lung Disease" is therefore mechanistically plausible, since β2-agonist-mediated bronchodilation is a core, first-line mechanism for both asthma and COPD, which together make up the majority of the obstructive lung disease category.

It is worth noting explicitly, however, that this is not a novel repurposing hypothesis in the traditional sense: the large body of supporting evidence (48 trials, 20 publications) largely reflects terbutaline's existing, decades-long role as a reliever/rescue bronchodilator in asthma (e.g., the Symbicort SMART trial series, which repeatedly uses terbutaline as the "as-needed" comparator) and its investigational use in acute COPD exacerbations. The prediction is best interpreted as reinforcing and consolidating an already-recognized clinical application, with some signal pointing toward formalizing or extending COPD-specific use in markets where that indication is not yet explicitly authorized.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Phase 3 | Completed | 24 | Terbutaline Turbuhaler 0.4 mg showed comparable relative efficacy/safety to salbutamol pMDI 200 μg in Japanese adult asthma patients (single-blind crossover) |
| [NCT02322788](https://clinicaltrials.gov/study/NCT02322788) | Phase 3 | Completed | 95 | Bricanyl (terbutaline) Turbuhaler M3 vs M2 compared for protective effect against methacholine-induced bronchoconstriction in stable mild-moderate asthma |
| [NCT00837967](https://clinicaltrials.gov/study/NCT00837967) | Phase 3 | Completed | 25 | Compared tolerability of high cumulative doses of Symbicort Turbuhaler vs Terbutaline Turbuhaler on top of maintenance Symbicort in Japanese adult asthma patients |
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Phase 3 | Completed | 3850 | Large trial testing Symbicort "as needed" vs Terbutaline "as needed" vs Pulmicort+Terbutaline "as needed" in mild-moderate persistent asthma |
| [NCT02224157](https://clinicaltrials.gov/study/NCT02224157) | Phase 3 | Completed | 4215 | Very large trial (n=4215) comparing Symbicort "as needed" vs Pulmicort + Terbutaline "as needed" in adult/adolescent asthma |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Phase 3 | Completed | 2091 | 12-month trial comparing Symbicort SMART vs Symbicort maintenance + Terbutaline as-needed reliever in asthma patients ≥16 years |
| [NCT00849095](https://clinicaltrials.gov/study/NCT00849095) | Phase 3 | Completed | 860 | As-needed Budesonide/Formoterol vs regular Budesonide/Formoterol + as-needed Terbutaline in mild-moderate persistent asthma (AIFA-sponsored) |
| [NCT00259766](https://clinicaltrials.gov/study/NCT00259766) | Phase 3 | Completed | 1970 | SHARE study: compared Symbicort regimens vs Pulmicort + Bricanyl (terbutaline) as-needed on asthma-related healthcare costs and control over 12 months |
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Phase 3 | Completed | 120 | Recent (2024) RCT comparing IV magnesium sulfate vs terbutaline for management of acute pediatric asthma exacerbations in the ED |
| [NCT01944033](https://clinicaltrials.gov/study/NCT01944033) | Phase 3 | Completed | 250 | RCT comparing β2-agonist alone vs β2-agonist + ipratropium bromide nebulization for acute COPD exacerbation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30156361](https://pubmed.ncbi.nlm.nih.gov/30156361/) | 2019 | RCT | Academic Emergency Medicine | Double-blind RCT in AECOPD patients requiring non-invasive ventilation; evaluated nebulized terbutaline + ipratropium vs terbutaline alone |
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | RCT | British Journal of Diseases of the Chest | Double-blind crossover trial: oral terbutaline significantly increased diaphragmatic contractile force (peak inspiratory and transdiaphragmatic pressure) vs placebo in COPD |
| [6988343](https://pubmed.ncbi.nlm.nih.gov/6988343/) | 1980 | RCT | Int J Clin Pharmacol Ther Toxicol | Double-blind 2-week study: oral terbutaline and clenbuterol both produced significant bronchodilation (FEV1, sRaw, V50%VC) in chronic obstructive lung disease |
| [1615190](https://pubmed.ncbi.nlm.nih.gov/1615190/) | 1992 | RCT | Respiratory Medicine | Double-blind placebo-controlled crossover study: inhaled terbutaline via Turbuhaler improved spirometry and exercise dyspnoea/walking distance in COLD |
| [2031046](https://pubmed.ncbi.nlm.nih.gov/2031046/) | 1991 | RCT | Pneumologie | Randomized crossover study: nebulized terbutaline combined with positive expiratory pressure (PEP) improved symptom score and peak expiratory flow in COPD |
| [10384064](https://pubmed.ncbi.nlm.nih.gov/10384064/) | 1999 | RCT | Lung | Double-blind placebo-controlled crossover RCT: single-dose terbutaline improved resting lung function and exercise capacity in COPD outpatients |
| [3044105](https://pubmed.ncbi.nlm.nih.gov/3044105/) | 1988 | RCT | American Journal of the Medical Sciences | Double-blind randomized crossover placebo-controlled trial: oral terbutaline augmented right/left ventricular ejection fraction (cardiac performance) in COPD |
| [6620518](https://pubmed.ncbi.nlm.nih.gov/6620518/) | 1983 | Clinical Study | JAMA | Radionuclide ventriculography study: terbutaline 0.25 mg decreased RVEF/LVEF in most stable severe COPD patients — a cardiac safety signal relevant to monitoring |
| [2951811](https://pubmed.ncbi.nlm.nih.gov/2951811/) | 1986 | RCT | Respiration | Randomized single-blind intra-individual study comparing fenoterol-ipratropium combination vs terbutaline alone on ventilatory response and tolerance in COLD |
| [8296260](https://pubmed.ncbi.nlm.nih.gov/8296260/) | 1993 | Comparative Study | Thorax | Compared bronchodilator reversibility response to low- and high-dose terbutaline and ipratropium bromide in COPD, informing reversibility-testing methodology |

---

## Saudi Arabia Market Information

Currently not marketed in this jurisdiction — no local authorization records are available (market status: 未上市, 0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite strong, extensive efficacy evidence (Evidence Level L1) supporting terbutaline's role in obstructive lung disease, this evidence pack has a **Blocking**-severity gap in local safety data (warnings, contraindications, DDI) that prevents even a preliminary S1 safety assessment, and the drug currently holds zero local market authorizations. Repurposing cannot proceed responsibly until baseline safety and regulatory documentation is secured.

**To proceed, the following is needed:**
- Official package insert / TFDA-equivalent safety documentation (warnings, contraindications, DDI) — currently Blocking (DG001)
- Confirmed mechanism-of-action / pharmacology documentation from DrugBank or manufacturer — currently High severity (DG002)
- Clarification of local regulatory/registration pathway given the drug is not currently marketed
- Note: the two lower-ranked candidate indications in this pack — "respiratory malformation" (L4, weak mechanistic link, Research Question stage) and "Rienhoff syndrome" (L5, no supporting evidence, Hold) — are substantially weaker and should remain deprioritized pending further evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

