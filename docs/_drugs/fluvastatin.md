---
layout: default
title: Fluvastatin
parent: 僅模型預測 (L5)
nav_order: 277
evidence_level: L5
indication_count: 10
---

# Fluvastatin
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

# Fluvastatin: From Hypercholesterolemia to Hyperlipoproteinemia

## One-Sentence Summary

Fluvastatin is an HMG-CoA reductase inhibitor (statin) whose established pharmacological effect is lowering LDL and total cholesterol in hypercholesterolemia/dyslipidemia. The TxGNN model's top prediction is that it is effective for **Hyperlipoproteinemia** — essentially an extension of its already-known lipid-lowering effect rather than a novel mechanism — supported by **5 clinical trials** and **20 publications**, though the drug itself is currently **not marketed in Saudi Arabia**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / dyslipidemia (statin class; no Saudi Arabia license text available — drug not registered locally) |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (MOA) is not available from DrugBank in this evidence pack (data gap DG002). Based on known pharmacology, fluvastatin belongs to the HMG-CoA reductase inhibitor (statin) class: it blocks hepatic cholesterol synthesis and upregulates LDL receptor expression, lowering LDL-C and total cholesterol.

Hyperlipoproteinemia is a broader clinical descriptor of elevated lipoprotein/cholesterol levels that overlaps substantially with fluvastatin's already-established indication. The repurposing rationale in the evidence pack explicitly notes this is "not a re-purposing inference but an extension of an already-approved pharmacological effect" — the mechanism (HMG-CoA reductase inhibition → reduced LDL/total cholesterol) directly and causally addresses the target condition, rather than an indirect or speculative link.

This makes the prediction highly plausible mechanistically, but the practical question for Saudi Arabia is regulatory (the drug is not currently marketed there) rather than scientific — the evidence gap is one of local registration, not efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00726362](https://clinicaltrials.gov/study/NCT00726362) | N/A | Completed | 3270 | Large real-world survey comparing commercially available statins (including fluvastatin) for treating hyperlipidemia under local clinical practice; directly relevant, largest cohort (Grade A). |
| [NCT00532311](https://clinicaltrials.gov/study/NCT00532311) | Phase 3 | Terminated | 411 | Lapaquistat acetate (a different squalene synthase inhibitor, not fluvastatin) added to statins for hypercholesterolemia; terminated for hepatotoxicity — indication overlap only (Grade C). |
| [NCT04608474](https://clinicaltrials.gov/study/NCT04608474) | Phase 4 | Completed | 81 | Evolocumab (PCSK9 inhibitor) pilot in renal transplant recipients with hyperlipidemia; not a fluvastatin trial (Grade C). |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab in pediatric/adolescent homozygous familial hypercholesterolemia; not a fluvastatin trial (Grade C). |
| [NCT01634906](https://clinicaltrials.gov/study/NCT01634906) | N/A | Completed | 55 | Effect of statin withdrawal on erythrocyte-bound apolipoprotein B; may include fluvastatin-treated patients, indirect mechanistic support (Grade B). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10067240](https://pubmed.ncbi.nlm.nih.gov/10067240/) | 1998 | RCT | Terapevticheskii arkhiv | Compared hypolipidemic effects of simvastatin vs. fluvastatin in primary hyperlipoproteinemia, including lecithin-cholesterol acyltransferase activity and apoE changes. |
| [10856536](https://pubmed.ncbi.nlm.nih.gov/10856536/) | 2000 | RCT | Atherosclerosis | FACT study: fluvastatin + bezafibrate combination was effective and safe in patients with mixed hyperlipidaemia and coronary artery disease (n=333). |
| [11219479](https://pubmed.ncbi.nlm.nih.gov/11219479/) | 2001 | RCT | Clinical therapeutics | Extended-release fluvastatin 80 mg once-daily compared to immediate-release formulation in primary hypercholesterolemia. |
| [15598476](https://pubmed.ncbi.nlm.nih.gov/15598476/) | 2004 | RCT | Clinical therapeutics | 12-month RCT: fluvastatin + fenofibrate vs. fluvastatin monotherapy in combined hyperlipidemia with type 2 diabetes and coronary heart disease. |
| [7604789](https://pubmed.ncbi.nlm.nih.gov/7604789/) | 1995 | RCT | American Journal of Cardiology | Fluvastatin's effect on lipid profile and apolipoproteins in 31 Chinese patients with hypercholesterolemia. |
| [17062478](https://pubmed.ncbi.nlm.nih.gov/17062478/) | 2006 | RCT | Acta Paediatrica | Efficacy and safety of fluvastatin in children/adolescents with heterozygous familial hypercholesterolaemia. |
| [8157036](https://pubmed.ncbi.nlm.nih.gov/8157036/) | 1993 | RCT | European Journal of Clinical Pharmacology | Double-blind trial of high-dose fluvastatin (20 mg vs. 40 mg bid) in 52 patients with familial hypercholesterolaemia. |
| [9271817](https://pubmed.ncbi.nlm.nih.gov/9271817/) | 1997 | RCT | Thrombosis Research | Open-label study of fluvastatin's effect on tissue factor pathway inhibitor in type IIa/IIb hyperlipidemia and post-MI patients. |
| [11347136](https://pubmed.ncbi.nlm.nih.gov/11347136/) | 2001 | Review | Nihon Rinsho (Japanese J. Clinical Medicine) | General review of fluvastatin (abstract not available). |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clinical Therapeutics | Review of rosuvastatin in hyperlipidemia management, referencing the broader statin class context. |

---

## Saudi Arabia Market Information

Fluvastatin currently has **no marketing authorization in Saudi Arabia** (0 licenses on record) — it is not marketed in this market per the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence level is L1, with 7 tier-1 RCTs and a large real-world statin comparison cohort (N=3,270) directly involving fluvastatin, and the mechanistic link is direct rather than inferential (fluvastatin's approved lipid-lowering effect applies to hyperlipoproteinemia by definition). However, the drug is not currently marketed in Saudi Arabia, and key safety/regulatory data (TFDA-equivalent package insert warnings, MOA detail) are flagged as data gaps in this pack.

**To proceed, the following is needed:**
- Local package insert / regulatory label data (warnings, contraindications, DDI) — currently blocking (DG001)
- Confirmed DrugBank mechanism of action detail (DG002)
- Assessment of the regulatory pathway for market authorization in Saudi Arabia, since the drug is not currently registered there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

