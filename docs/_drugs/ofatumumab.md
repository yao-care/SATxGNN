---
layout: default
title: Ofatumumab
parent: 僅模型預測 (L5)
nav_order: 456
evidence_level: L5
indication_count: 8
---

# Ofatumumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Ofatumumab: From Chronic Lymphocytic Leukemia (CLL/SLL) to an IGHV-Mutated CLL/SLL Subtype

## One-Sentence Summary

Ofatumumab is a fully human anti-CD20 monoclonal antibody whose established indication is chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL) — this is documented within the evidence pack itself, not in the Saudi regulatory dataset, since the product currently holds **zero SFDA licenses** and is **not marketed** in Saudi Arabia. TxGNN's top-ranked prediction is not a new disease but a biomarker-defined refinement of that same indication — **CLL/SLL with IGHV somatic hypermutation** — and currently has **no dedicated clinical trials or literature** of its own. The prediction is therefore best read as a research question about biomarker-stratified efficacy rather than a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma (CLL/SLL) — noted in evidence-pack rationale text as ofatumumab's original approved indication (e.g., Arzerra); not present in the Saudi Arabia license database because the product is not currently marketed there |
| Predicted New Indication | Chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene (IGHV) somatic hypermutation |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 (model prediction only — 0 clinical trials, 0 publications specific to this IGHV-defined subgroup) |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The `original_moa` field in this evidence pack is a documented data gap (DG002), so no formal mechanism-of-action statement is available from DrugBank. However, the literature captured elsewhere in this same pack (e.g., PMID 20068404, 20481657, 18535937) consistently describes ofatumumab as a fully human IgG1κ monoclonal antibody that binds a membrane-proximal epitope on CD20 and depletes CD20⁺ B cells via complement-dependent cytotoxicity (CDC) and antibody-dependent cellular cytotoxicity (ADCC).

The predicted "new" indication is not a distinct disease — it is CLL/SLL stratified by IGHV mutation status, a well-established prognostic biomarker that separates patients into pre-germinal-center (IGHV-unmutated, generally worse prognosis) and post-germinal-center (IGHV-mutated, generally better prognosis) subgroups. Both this candidate (rank 1) and its counterpart "pregerminal center CLL/SLL" (rank 2) share the exact same CD20-targeting mechanism as ofatumumab's core, already-supported indication for unstratified CLL/SLL, which appears elsewhere in this same evidence pack (rank 5) backed by **34 clinical trials, 20 publications, and L1-level evidence** (multiple completed Phase 3 RCTs, including RESONATE and DUO).

Mechanistically, there is no reason CD20 expression or ofatumumab's cytotoxic activity would differ systematically by IGHV status — the open question is whether efficacy, response depth, or duration differs across the biomarker-defined subgroup, which would require a dedicated subgroup analysis or prospective biomarker-stratified trial rather than a new mechanistic hypothesis. In this sense, the prediction functions as a research question about existing therapy rather than a novel repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Ofatumumab currently holds no marketing authorizations in Saudi Arabia (0 licenses on file; market status: Not Marketed). No product/dosage-form/indication records are available to tabulate.

---

## Cytotoxicity

Chronic lymphocytic leukemia/small lymphocytic lymphoma is a hematologic malignancy, so this section applies even though ofatumumab is a targeted biologic rather than a conventional cytotoxic agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy (anti-CD20 monoclonal antibody; not a conventional cytotoxic chemotherapeutic) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction is a biomarker-defined subtype of ofatumumab's own established indication rather than an independent disease target, and it currently has zero direct clinical trials or publications of its own — it is a research question about existing therapy, not a validated repurposing opportunity. Separately, ofatumumab has no SFDA marketing authorization in Saudi Arabia today, and two blocking-severity data gaps (package insert warnings/contraindications, and DrugBank mechanism-of-action data) prevent a safety pre-screen from being completed.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/SFDA package insert warnings and contraindications) — currently Blocking severity
- Resolve DG002 (formal DrugBank mechanism-of-action data) — currently High severity
- IGHV-status subgroup analyses or a prospective biomarker-stratified trial drawing on the existing CLL/SLL evidence base (rank 5: L1, 34 trials, 20 publications) to test whether this specific prediction adds actionable information beyond the parent indication
- A Saudi Arabia regulatory pathway assessment, given the product currently holds zero local authorizations
- For context, two other candidates in this same evidence pack carry materially stronger direct evidence and may warrant separate evaluation: follicular lymphoma (rank 3, L2, multiple completed Phase 2 trials) and unstratified CLL/SLL itself (rank 5, L1)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

