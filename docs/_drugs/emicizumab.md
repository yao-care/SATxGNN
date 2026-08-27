---
layout: default
title: Emicizumab
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
---

# Emicizumab
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

Using the Evidence Pack for EMICIZUMAB (DB13923), I selected **"acquired coagulation factor deficiency"** (rank 5, index 4) as the lead candidate to report on rather than rank 1. Reasoning: rank 1–4 and 6–10 are all `decision_stage: S0`, `evidence_level: L5`, `recommendation: Hold`, with the rationale text for several (e.g. Glanzmann thrombasthenia, Scott syndrome, TTP) explicitly stating the mechanism does **not** support repurposing or is even contraindicated. Only rank 5 reached `S3` / `L2` / "Proceed with Guardrails" with real clinical trial and literature backing (this maps mechanistically, per the evidence pack's own rationale text, to Acquired Hemophilia A). Reporting on rank 1 (pseudo-von Willebrand disease) would produce a report with zero supporting evidence and an explicit "no plausible mechanism" statement, which is not useful for a Go/Hold decision. This substitution is noted transparently in the report below rather than silently done.

---

# Emicizumab: From Congenital Hemophilia A to Acquired Coagulation Factor Deficiency (Acquired Hemophilia A)

## One-Sentence Summary

> Emicizumab is a bispecific monoclonal antibody originally developed and approved for prophylactic bleeding control in **congenital Hemophilia A** (with or without Factor VIII inhibitors) — this original-indication context is inferred from the literature evidence in this pack, since the `original_indications` and `taiwan_regulatory.licenses` fields are both empty (data gap).
> The TxGNN model predicts it may also be effective for **Acquired Coagulation Factor Deficiency**, which the supporting literature identifies specifically as **Acquired Hemophilia A (AHA)** — a distinct autoimmune condition where autoantibodies neutralize endogenous Factor VIII.
> This is currently the only one of 10 TxGNN-ranked candidates for this drug with meaningful evidence: **1 registry-type clinical trial** and **20 publications**, including multiple prospective Phase 2/3 intervention studies, support this direction. The other 9 candidates (including pseudo-von Willebrand disease, Glanzmann thrombasthenia, and thrombotic thrombocytopenic purpura) remain at model-prediction-only level (L5) with no clinical evidence, and one (TTP) is flagged as a potential mechanistic **safety conflict**, not an opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Congenital Hemophilia A (inferred from literature context; not present in structured `original_indications`/`licenses` fields — data gap) |
| Predicted New Indication | Acquired Coagulation Factor Deficiency (Acquired Hemophilia A) |
| TxGNN Prediction Score | 99.90% (rank 2296 among model outputs) |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

*Note: Of the 10 TxGNN-predicted indications for this drug, 9 are rated Hold/L5 (model prediction only, no clinical evidence). This report covers only the evidence-supported lead candidate above.*

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data (`original_moa`) is flagged as a data gap in this pack (DG002, severity High). However, the literature evidence collected for this candidate consistently describes emicizumab's mechanism: it is a **bispecific antibody that binds both activated Factor IX (FIXa) and Factor X (FX)**, bridging them to reconstitute the cofactor function normally performed by activated Factor VIII (FVIIIa) — without being an FVIII molecule itself.

This mechanistic property is precisely why the repurposing signal is plausible. In **congenital Hemophilia A**, FVIII is genetically absent or deficient, and emicizumab restores hemostasis by replacing FVIII's cofactor *function* through an independent structural route. In **Acquired Hemophilia A**, the problem is different — FVIII is structurally present but neutralized by autoantibodies — yet the *functional* gap is the same: the FIXa-FX bridging step is missing. Because emicizumab does not depend on FVIII protein at all, it is structurally immune to anti-FVIII autoantibody inhibition, which multiple literature sources in this pack (e.g. PMID 37858328, 36696195, 39134043) confirm has been directly tested in prospective, multicenter, open-label trials with favorable outcomes.

By contrast, the other 9 TxGNN candidates for this drug involve mechanistically unrelated or opposing pathways (e.g. platelet receptor defects such as Glanzmann thrombasthenia and Scott syndrome, platelet count disorders, or ADAMTS13-deficient thrombotic disease), and the evidence pack's own rationale text explicitly notes these lack mechanistic support or, in the case of TTP, may represent a **safety conflict** since promoting thrombin generation is the opposite of the desired therapeutic direction in a microthrombotic disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398628](https://clinicaltrials.gov/study/NCT04398628) | N/A | Recruiting | 3000 | ATHN Transcends — a large natural history/registry cohort study covering non-neoplastic hematologic disorders (including acquired coagulation factor deficiencies). It is **not** an interventional emicizumab trial; relevance graded "C" — background epidemiological data only, not direct efficacy evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/) | 2023 | Phase 2, open-label, single-arm | The Lancet Haematology | GTH-AHA-EMI study: emicizumab prophylaxis protected AHA patients from bleeding and allowed immunosuppression to be deferred during the first 12 weeks. |
| [36696195](https://pubmed.ncbi.nlm.nih.gov/36696195/) | 2023 | Phase 3, prospective, multicenter, open-label | J Thromb Haemost | First prospective Phase 3 study of emicizumab specifically in acquired hemophilia A patients (previously untested prospectively in this population). |
| [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/) | 2025 | Phase 3, final analysis | Thrombosis and Haemostasis | AGEHA study final analysis: favorable benefit-risk profile for emicizumab prophylaxis in AHA, including data on immunosuppression-ineligible patients and long-term use. |
| [38049124](https://pubmed.ncbi.nlm.nih.gov/38049124/) | 2024 | Consensus recommendations | Hamostaseologie | GTH-AHA Working Group consensus: the GTH-AHA-EMI study demonstrated emicizumab prevents bleeds and allows postponement of immunosuppression in AHA. |
| [39361769](https://pubmed.ncbi.nlm.nih.gov/39361769/) | 2024 | Real-world retrospective cohort | Blood Advances | Multicenter US cohort (62 patients, 12 hemophilia treatment centers) treated off-label with emicizumab for AHA, evaluating real-world outcomes with/without immunosuppression. |
| [40795229](https://pubmed.ncbi.nlm.nih.gov/40795229/) | 2025 | Follow-up cohort | Blood Advances | 2-year follow-up of GTH-AHA-EMI patients showing sustained survival benefit and continued deferral of immunosuppressive therapy. |
| [39536818](https://pubmed.ncbi.nlm.nih.gov/39536818/) | 2025 | Narrative review | J Thromb Haemost | Overview of AHA epidemiology, pathophysiology, diagnosis, and management "in the emicizumab era." |
| [38562115](https://pubmed.ncbi.nlm.nih.gov/38562115/) | 2024 | Review | Haemophilia | Reviews recent advances in AHA, acquired von Willebrand syndrome, and chronic-liver-disease-related hemostatic abnormalities; notes AHA patients can now benefit from emicizumab prophylaxis. |
| [36795341](https://pubmed.ncbi.nlm.nih.gov/36795341/) | 2023 | Review/opinion | Blood Transfusion | Discusses pros and cons of emicizumab as a new approach to AHA bleeding prevention and treatment. |
| [38066859](https://pubmed.ncbi.nlm.nih.gov/38066859/) | 2023 | Review (education program) | Hematology Am Soc Hematol Educ Program | Reviews immunotherapy of AHA, including the role of emerging hemostatic agents alongside standard immunosuppression. |

*10 of 20 available publications shown, prioritized by study design (prospective/Phase trials and consensus statements first, followed by cohort studies and reviews).*

---

## Saudi Arabia Market Information

Emicizumab currently has **no marketing authorization in Saudi Arabia** (`market_status: 未上市`, `total_licenses: 0`). No product license records are available to summarize in this pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: This pack flags a **Blocking** data gap (DG001) for TFDA/SFDA package insert warnings and contraindications — this data must be obtained before this candidate can proceed to formal safety pre-assessment (S1). No DDI records were found in the queried database (`query_status: not_found`).*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Among 10 TxGNN-predicted indications for emicizumab, "acquired coagulation factor deficiency" (mapping to Acquired Hemophilia A) is the only one supported by real evidence — multiple prospective Phase 2/3 studies (GTH-AHA-EMI, AGEHA) and a working-group consensus statement — combined with a mechanistically strong rationale (FVIII-autoantibody-independent hemostatic bridging). However, the drug is not currently registered in Saudi Arabia, and formal safety/prescribing data (TFDA/SFDA package insert) is a **Blocking** data gap, so this cannot yet proceed to a formal safety pre-assessment stage.

**To proceed, the following is needed:**
- Obtain TFDA/SFDA-equivalent package insert with warnings and contraindications (DG001, Blocking — required before S1 safety pre-assessment)
- Obtain formal DrugBank/manufacturer mechanism-of-action documentation (DG002, High priority)
- Confirm registration pathway/status for Saudi Arabia market entry, since the drug is currently unmarketed (0 licenses)
- Complete a formal DDI profile (current query returned no data)
- Evaluate whether AHA use should be pursued as a formal labeled indication vs. continued off-label/consensus-guideline use, given real-world cohort data (PMID 39361769) already exists alongside prospective trial data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

