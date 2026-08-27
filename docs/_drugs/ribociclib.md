---
layout: default
title: Ribociclib
parent: 僅模型預測 (L5)
nav_order: 544
evidence_level: L5
indication_count: 4
---

# Ribociclib
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

# Ribociclib: From HR+/HER2- Breast Cancer to Myeloid Leukemia

## One-Sentence Summary

Ribociclib (DrugBank DB11730) is a CDK4/6 inhibitor originally developed and marketed (as Kisqali) for HR+/HER2-negative advanced/metastatic breast cancer, based on repeated references across the included trial and literature evidence — no formal Saudi Arabia licensing or original-indication record exists in this evidence pack. The TxGNN model predicts potential activity in **myeloid leukemia**, but this is currently supported by **0 registered clinical trials** and only **3 publications**, one of which actually reports CDK4/6-inhibitor-induced AML rather than treatment benefit. Evidence is preliminary and largely preclinical/in vitro.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HR+/HER2-negative advanced/metastatic breast cancer *(inferred from trial/literature titles in this evidence pack; not confirmed via Saudi Arabia licensing data, which is empty)* |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 99.35% (model rank 9,631) |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for ribociclib is not available in this evidence pack (flagged as a High-severity data gap). Based on known information, ribociclib is an orally administered, highly selective CDK4/6 inhibitor whose efficacy in HR+/HER2-negative breast cancer is well established through multiple Phase 1–3 trials referenced in the underlying evidence.

The repurposing rationale for AML proposes that CDK4/6 pathway compensatory activation contributes to pharmacokinetic drug resistance in acute myeloid leukemia, and that in vitro CDK4/6 inhibition can partially reverse this resistance — providing a theoretical mechanistic basis. However, this rationale is supported by only one relevant in vitro study (PMID 32560251); a second AML-related publication (PMID 30575100) actually reports the **opposite** relationship — CDK4/6 inhibitor treatment triggering AML with eosinophilia via clonal hematopoiesis — and the third (PMID 41641105) is unrelated to AML entirely (a vulvar adenocarcinoma case report). This mix of supportive, contradictory, and irrelevant evidence substantially weakens confidence in the prediction.

Given the absence of any clinical trials for this indication and the cellular-level-only supportive evidence, this prediction should currently be treated as hypothesis-generating rather than actionable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32560251](https://pubmed.ncbi.nlm.nih.gov/32560251/) | 2020 | Preclinical/In vitro | Cancers | CDK4/6 inhibitors (including ribociclib) tested in AML cell lines to counteract ABCB1/ABCG2-transporter- and carbonyl-reductase-mediated drug resistance to anthracycline-based induction therapy |
| [30575100](https://pubmed.ncbi.nlm.nih.gov/30575100/) | 2019 | Case report (adverse event) | American Journal of Hematology | AML with eosinophilia arising after CDK4/6 inhibitor treatment, attributed to underlying clonal hematopoiesis of indeterminate potential — i.e., a drug-associated AML risk signal, not a treatment benefit signal |
| [41641105](https://pubmed.ncbi.nlm.nih.gov/41641105/) | 2026 | Case report (unrelated) | Frontiers in Oncology | Vulvar mammary-type adenocarcinoma with concomitant breast cancer; not related to AML or ribociclib's use in leukemia |

---

## Saudi Arabia Market Information

No Saudi Arabia licensing records are available — the evidence pack lists 0 authorizations and market status "Not marketed."

---

## Cytotoxicity

Ribociclib is an antineoplastic agent (CDK4/6 inhibitor used in breast cancer treatment).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | High — neutropenia, leukopenia, and thrombocytopenia are consistently reported as common hematological adverse events across the CDK4/6-inhibitor class in the supporting literature (e.g., PMID 38753541 hematological toxicity meta-analysis, PMID 29147869 systematic review/meta-analysis) |
| Emetogenicity Classification | Not explicitly characterized in the available evidence; consult product labeling for formal classification |
| Monitoring Items | CBC with differential (baseline and periodic during treatment), liver function tests, ECG/QTc (per class-associated cardiac signals noted in the literature) |
| Handling Protection | Oral antineoplastic agent — handle per institutional hazardous-drug handling policy |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all marked as data gaps in this evidence pack; the missing SFDA package insert is flagged as a Blocking-severity gap that prevents formal S1 safety screening.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for ribociclib in myeloid leukemia is limited to a single supportive in vitro study, with no registered clinical trials, and is undercut by a contradictory case report describing CDK4/6-inhibitor-induced AML. Combined with the Blocking-severity gap in TFDA/SFDA package insert data and the complete absence of Saudi Arabia market presence, there is insufficient evidence to proceed at this time.

**To proceed, the following is needed:**
- Confirmed mechanism of action and original approved indication (currently marked as data gaps)
- SFDA/TFDA package insert (warnings, contraindications, DDI) — Blocking gap
- Additional preclinical or early clinical evidence directly evaluating anti-leukemic efficacy of ribociclib, distinguishing a therapeutic signal from the drug's known myelosuppressive/AML-risk adverse-event profile
- Saudi Arabia regulatory and market status confirmation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

