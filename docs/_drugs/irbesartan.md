---
layout: default
title: Irbesartan
parent: 僅模型預測 (L5)
nav_order: 340
evidence_level: L5
indication_count: 4
---

# Irbesartan
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

# Irbesartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Irbesartan is a well-known angiotensin II receptor blocker (ARB), whose established clinical use is hypertension and diabetic nephropathy — though this evidence pack itself contains no formal original-indication record (`original_indications` is empty and no local market licenses exist). TxGNN predicts four related indications — **malignant renovascular hypertension**, **malignant hypertensive renal disease**, and two subtypes of **pulmonary hypertension** — all at prediction scores around 99.3%. However, **none of the four are backed by any clinical trial**, and the only literature hits (20 papers, attached to the pulmonary hypertension/hypoxia prediction) are general hypoxia-biology papers unrelated to irbesartan itself. Evidence level is L5 (prediction-only) across the board.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (`original_indications` is empty). Irbesartan is generally known as an ARB antihypertensive — this is background pharmacological context, not sourced from the pack. |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available (`original_moa`: [Data Gap], DG002). Based on general pharmacological knowledge, irbesartan is an angiotensin II type 1 (AT1) receptor blocker that lowers blood pressure by inhibiting the renin-angiotensin system (RAS). This is mechanistically why TxGNN links it to hypertensive and renal-hypertensive disease phenotypes.

For the top two predictions — **malignant renovascular hypertension** and **malignant hypertensive renal disease** — the mechanistic direction is plausible on its face (RAS blockade lowering blood pressure and slowing hypertensive nephropathy), but the evidence pack's own rationale flags an important caveat: malignant renovascular hypertension frequently involves (often bilateral) renal artery stenosis, a setting where ARBs/ACE inhibitors carry a well-known risk of precipitating acute kidney injury by reducing glomerular perfusion pressure. In other words, this is a case where the mechanism could point toward benefit **or** harm depending on the underlying renal artery anatomy — it is not a straightforward "repurposing opportunity" signal.

For the two pulmonary hypertension predictions (WHO Group 3 and Group 5), the mechanistic case is much weaker. Current pulmonary hypertension treatment guidelines do not support systemic antihypertensive/RAS-blocking agents for these subtypes, and — as detailed below — the attached literature does not actually address irbesartan or ARBs in pulmonary hypertension; it reflects keyword co-occurrence with "hypoxia" rather than a drug-disease mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered — this applies to all four predicted indications (malignant renovascular hypertension, malignant hypertensive renal disease, pulmonary hypertension with unclear multifactorial mechanism, and pulmonary hypertension owing to lung disease and/or hypoxia).

---

## Literature Evidence

No literature is attached to the top three predicted indications. The fourth prediction (pulmonary hypertension owing to lung disease and/or hypoxia) has 20 PubMed hits, but on review **none of them study irbesartan, ARBs, or pulmonary hypertension treatment** — they are general hypoxia-biology papers (brain aging, cognitive impairment, cancer metabolism, altitude physiology) that matched on the keyword "hypoxia" alone. They are listed below for transparency, not as supporting evidence for repurposing:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respir Care Clin North Am | Overview of the mechanisms of hypoxemia (V/Q mismatch, shunt, hypoventilation); not drug-specific |
| [9446167](https://pubmed.ncbi.nlm.nih.gov/9446167/) | 1997 | Review | Rev Med Liege | Review of hepatopulmonary syndrome; no drug intervention data |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clin Oncol | Therapeutic modification of tumor hypoxia in oncology, unrelated to pulmonary hypertension |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Res Rev | Hypoxia and brain aging/neurodegeneration; neurology focus, not pulmonary/cardiovascular |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metab Brain Dis | Cognitive impairment from hypoxia; neurology focus |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biol | Hypoxia in multiple sclerosis pathology |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Review | Rev Med Inst Mex Seguro Soc | High-altitude hypoxia physiology and acclimatization |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | J Cell Biochem | General cellular hypoxia-sensing biology |
| [27146279](https://pubmed.ncbi.nlm.nih.gov/27146279/) | 2017 | Review | Cephalalgia | Hypoxic mechanisms in migraine/cluster headache |
| [8817697](https://pubmed.ncbi.nlm.nih.gov/8817697/) | 1996 | Review | Prog Neurobiol | Hypoxia and brain development |

---

## Safety Considerations

Formal safety data (key warnings, contraindications, DDI) is not available in this evidence pack — please refer to the package insert for safety information.

**Mechanism-based safety signal (not a formal DDI/contraindication record, derived from the repurposing rationale):** ARB use in the setting of malignant renovascular hypertension — particularly with bilateral renal artery stenosis — carries a known risk of acute kidney injury from reduced renal perfusion pressure. This should be treated as a specific red flag for the top-ranked prediction, not just a generic ARB caution.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predicted indications are supported only by a TxGNN score (L5), with zero clinical trials and no drug-specific literature. The drug is also not currently marketed in Saudi Arabia (0 authorizations), and the top prediction carries a plausible mechanism-based harm signal (AKI risk with renal artery stenosis) rather than a clean efficacy signal.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (DG001, blocking — required before any S1 safety screening)
- DrugBank-sourced mechanism of action detail (DG002)
- Targeted literature/clinical trial search using "irbesartan" or "ARB" combined with each specific indication term, rather than relying on the current keyword-matched hypoxia literature
- Clinical assessment of renal artery stenosis prevalence/risk in the malignant renovascular hypertension population before any translational consideration
- Confirmation of local market/registration pathway, given the drug is currently unmarketed in Saudi Arabia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

