---
layout: default
title: Streptokinase
parent: 僅模型預測 (L5)
nav_order: 584
evidence_level: L5
indication_count: 10
---

# Streptokinase
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

# Streptokinase: From Not Marketed in Saudi Arabia to Myocardial Infarction

## One-Sentence Summary

Streptokinase is a bacterial plasminogen activator whose original indications and mechanism-of-action data are not on file for this evidence pack (Data Gap), and the drug currently holds **no market authorization in Saudi Arabia**. The TxGNN model's top-ranked prediction is **Myocardial Infarction**, supported by **34 clinical trials** and **20 publications**, but this is notable mainly because MI is streptokinase's classic, already-established global indication rather than a genuinely novel repurposing signal — the model appears to have rediscovered known pharmacology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no registered indication text in Saudi Arabia (drug not marketed; original_indications field empty) |
| Predicted New Indication | Myocardial Infarction |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (`original_moa`) is not available in this evidence pack (Data Gap). However, the evidence pack's repurposing rationale for this candidate does describe the mechanism: Streptokinase is a non-enzymatic protein of streptococcal origin that binds plasma plasminogen to form an activator complex, which converts circulating plasminogen to plasmin. Plasmin then degrades the fibrin network of coronary artery thrombi, restoring reperfusion.

This mechanism maps directly onto myocardial infarction, where thrombotic coronary occlusion is the core pathology — dissolving the clot is the therapeutic goal. Importantly, the evidence pack itself flags that this is **"the classic, already-established mechanism for AMI, not a predictive association"** — meaning the TxGNN model has effectively surfaced the drug's known, historical use (streptokinase was one of the first thrombolytics approved for AMI decades ago) rather than an unexpected new indication. This should temper how "novel" this repurposing candidate is treated, even though the supporting evidence base is strong.

A second complicating factor: this candidate has **no registered Saudi Arabia market presence** (0 licenses, "Not Marketed"), and the original indication text field is empty. So while the mechanistic and clinical-trial case for MI is very strong globally, the actual regulatory starting point in this market is essentially a blank slate rather than a label-expansion scenario.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000505](https://clinicaltrials.gov/study/NCT00000505) | Phase 3 | Completed | N/A | TIMI I/II — landmark trial comparing IV rt-PA vs IV streptokinase for thrombolysis in AMI, and post-thrombolysis PTCA strategy |
| [NCT00245648](https://clinicaltrials.gov/study/NCT00245648) | Phase 3 | Completed | N/A | GUSTO-V — analyzed sex-based differences in death/bleeding outcomes among fibrinolytic (including streptokinase)-treated AMI patients |
| [NCT00000503](https://clinicaltrials.gov/study/NCT00000503) | Phase 3 | Completed | N/A | Randomized trial of non-surgical coronary reperfusion effect on infarct size in AMI (streptokinase-era core trial design) |
| [NCT00627809](https://clinicaltrials.gov/study/NCT00627809) | Phase 4 | Completed | 53 | Intracoronary low-dose streptokinase as adjunct to primary PCI in STEMI; evaluated late LV infarct size/volume |
| [NCT01930682](https://clinicaltrials.gov/study/NCT01930682) | Phase 4 | Completed | 344 | EARLY-MYO — early routine catheterization after alteplase fibrinolysis vs primary PCI in STEMI (same fibrinolytic drug class) |
| [NCT03328156](https://clinicaltrials.gov/study/NCT03328156) | N/A | Unknown | 300 | Compared erectile dysfunction incidence after PCI vs thrombolytic therapy in STEMI reperfusion strategies |
| [NCT02943785](https://clinicaltrials.gov/study/NCT02943785) | Phase 3 | Completed | 1426 | Edoxaban vs standard of care in atrial fibrillation patients post-TAVI; background cardiovascular context, different mechanism |
| [NCT01087723](https://clinicaltrials.gov/study/NCT01087723) | Phase 3 | Completed | 2198 | Bivalirudin vs standard of care in STE-ACS patients undergoing primary PCI; overlapping population, non-thrombolytic mechanism |
| [NCT03465644](https://clinicaltrials.gov/study/NCT03465644) | Phase 4 | Completed | 2018 | Tailored antiplatelet escalation/de-escalation vs standard DAPT after complex high-risk PCI |
| [NCT04609111](https://clinicaltrials.gov/study/NCT04609111) | Phase 4 | Active, not recruiting | 6002 | Prasugrel monotherapy vs 1-month DAPT after PCI with cobalt-chromium everolimus-eluting stents in high-bleeding-risk/ACS patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10172727](https://pubmed.ncbi.nlm.nih.gov/10172727/) | 1995 | RCT | Journal of Interventional Cardiology | European Working Party streptokinase trial and European Cooperative Study alteplase trial in AMI patients |
| [8028463](https://pubmed.ncbi.nlm.nih.gov/8028463/) | 1994 | Meta-analysis | Medical Decision Making | Combined meta-analysis/decision analysis of IV streptokinase cost-effectiveness for suspected AMI, by infarct location and likelihood |
| [21070617](https://pubmed.ncbi.nlm.nih.gov/21070617/) | 2012 | Review | Cardiovascular Therapeutics | History and comparative efficacy of thrombolytics (streptokinase and newer tPA agents) in reducing AMI mortality |
| [2868343](https://pubmed.ncbi.nlm.nih.gov/2868343/) | 1986 | Review | Lancet | Review of streptokinase in acute myocardial infarction |
| [8242906](https://pubmed.ncbi.nlm.nih.gov/8242906/) | 1993 | Review | Clinical Cardiology | Discussion of thrombolytic therapy economics in MI, including streptokinase |
| [2955892](https://pubmed.ncbi.nlm.nih.gov/2955892/) | 1987 | Review | Cardiovascular Clinics | Review of thrombolysis with streptokinase and TPA in AMI treatment |
| [8005961](https://pubmed.ncbi.nlm.nih.gov/8005961/) | 1993 | Review | Journal of the Association of Physicians of India | Review of streptokinase use in acute myocardial infarction |
| [481517](https://pubmed.ncbi.nlm.nih.gov/481517/) | 1979 | Review | New England Journal of Medicine | Early review discussing streptokinase and myocardial infarction |
| [5134571](https://pubmed.ncbi.nlm.nih.gov/5134571/) | 1971 | Review | British Medical Journal | Early review on streptokinase and myocardial infarction |
| [3139173](https://pubmed.ncbi.nlm.nih.gov/3139173/) | 1988 | Commentary | BMJ | Commentary characterizing streptokinase thrombolysis as "a milestone for myocardial infarction" |

---

## Saudi Arabia Market Information

Streptokinase currently has **no registered market authorization in Saudi Arabia** (0 licenses on file, market status: Not Marketed). No product name, dosage form, or approved indication text is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. All safety fields in this evidence pack (key warnings, contraindications, drug-drug interactions) are Data Gaps, and the DDI query returned no results.

**Note:** the accompanying data-gap log flags this as a **Blocking** gap (TFDA/local package insert warnings and contraindications not yet obtained), which by definition prevents this candidate from entering the S1 safety pre-assessment stage.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic and clinical-trial case for streptokinase in myocardial infarction is very strong (L1 evidence, 4 completed Phase 3 trials directly or closely relevant) — but this reflects the drug's long-established historical use rather than a novel finding. The path forward is gated by a **Blocking** safety data gap (no TFDA/local package insert data) and the fact that the drug has zero existing market presence in Saudi Arabia, so this is effectively a new-registration effort, not a label expansion.

**To proceed, the following is needed:**
- TFDA/Saudi package insert (warnings, contraindications) — currently Blocking (DG001)
- Formal mechanism-of-action documentation from DrugBank or manufacturer labeling — currently High-severity gap (DG002)
- Original indication and regulatory history data, since none is on file for this market
- A market-entry/registration assessment, given the drug has no existing Saudi Arabia authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

