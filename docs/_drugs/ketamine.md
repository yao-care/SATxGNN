---
layout: default
title: Ketamine
parent: 僅模型預測 (L5)
nav_order: 351
evidence_level: L5
indication_count: 1
---

# Ketamine
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

# Ketamine: From General Anesthesia to Headache Disorder

## One-Sentence Summary

Ketamine is a dissociative anesthetic and non-competitive NMDA receptor antagonist, long used clinically for anesthesia induction and procedural analgesia.
The TxGNN model predicts it may be effective for **Headache Disorder**,
with **10 relevant clinical trials** (out of 40 screened) and **4 directly relevant publications** currently supporting this direction, alongside a large amount of unrelated evidence (depression, CRPS, other agents) that was excluded from this analysis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anesthesia (dissociative anesthetic) — no formal approved indication text available in the evidence pack |
| Predicted New Indication | Headache Disorder |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed, drug-level mechanism of action data for ketamine is currently marked as a data gap in this evidence pack. However, the repurposing rationale supplied for this specific prediction is substantive: ketamine acts as a non-competitive NMDA receptor antagonist, inhibiting glutamatergic transmission implicated in central sensitization and cortical spreading depression. Both processes are core pathological mechanisms in chronic migraine, cluster headache, and refractory headache disorders.

Ketamine's established clinical use is as a general anesthetic and, at sub-anesthetic doses, as an analgesic for acute and chronic pain. Headache disorders share glutamatergic and central-sensitization pathophysiology with the pain syndromes ketamine is already used for off-label (CRPS, refractory neuropathic pain), making the extension to headache mechanistically plausible.

It is worth noting that ketamine's antidepressant effect (via NMDA/AMPA signaling) is a related but mechanistically distinct pathway from its putative anti-headache effect. The two should not be conflated — the headache indication requires independent validation of dose-response relationship and long-term safety, which is not yet established.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04179266](https://clinicaltrials.gov/study/NCT04179266) | Phase 1/2 | Completed | 23 | Proof-of-concept: intranasal ketamine spray for chronic cluster headache; direct drug-indication match |
| [NCT05306899](https://clinicaltrials.gov/study/NCT05306899) | Phase 3 | Recruiting | 56 | Multi-center RCT (KetHead Study) of high-dose IV ketamine infusion for chronic daily headaches |
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | Completed | 80 | THINK Trial: intranasal ketamine vs. standard therapy for primary headache syndromes in the ED |
| [NCT02657031](https://clinicaltrials.gov/study/NCT02657031) | Phase 4 | Completed | 54 | Check Trial: low-dose ketamine vs. Compazine for ED headache control |
| [NCT02697071](https://clinicaltrials.gov/study/NCT02697071) | N/A | Completed | 34 | Placebo-controlled RCT of sub-dissociative ketamine for acute migraine-type headache in the ED |
| [NCT04814381](https://clinicaltrials.gov/study/NCT04814381) | Phase 4 | Recruiting | 90 | Single infusion of ketamine + magnesium sulfate for refractory chronic cluster headache |
| [NCT04860713](https://clinicaltrials.gov/study/NCT04860713) | Phase 4 | Completed | 5 | Oral ketamine + aspirin + rimegepant for acute ED headache; very small sample |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Unknown | 60 | Ketamine vs. ketorolac for acute tension-type headache |
| [NCT06608277](https://clinicaltrials.gov/study/NCT06608277) | Phase 2 | Recruiting | 175 | Ketamine and/or stellate ganglion block for TBI-associated headache and PTSD |
| [NCT05997134](https://clinicaltrials.gov/study/NCT05997134) | Phase 4 | Unknown | 75 | Ketamine infusion regimens for complex regional pain syndrome; supportive pain-mechanism evidence, not headache-specific |

Note: several trials in the raw dataset (e.g., NCT06180759/DMT, NCT06428838/Eptinezumab, NCT03921567/Lidocaine) were graded C — wrong drug matched to Ketamine — and are excluded above. Several depression- and ECT-related ketamine trials were also excluded as off-topic for this indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35356451](https://pubmed.ncbi.nlm.nih.gov/35356451/) | 2022 | Cohort | Frontiers in Neurology | Retrospective cohort on IV lidocaine and ketamine infusions for headache disorders — efficacy, duration, and safety |
| [34919214](https://pubmed.ncbi.nlm.nih.gov/34919214/) | 2022 | Review | Drugs | Cluster headache drug therapy review; contextualizes where ketamine fits among acute/prophylactic options |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | AHS 2025 update on parenteral pharmacotherapies for acute migraine in the ED |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Review of Neurotherapeutics | Trigeminal neuralgia pharmacotherapy update; notes ketamine as a possible adjuvant |

Note: additional literature in the dataset concerns esketamine for treatment-resistant depression and is not relevant to the headache indication; it was excluded from this table.

## Safety Considerations

Please refer to the package insert for safety information. (TFDA warnings/contraindications and DDI data are currently marked as data gaps — DG001 is flagged as a **Blocking** severity gap that prevents S1 safety pre-assessment.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic rationale (NMDA antagonism → central sensitization) is plausible and several completed trials (THINK, Check, NCT02697071) show direct signal for ketamine in ED headache/migraine settings, the pivotal Phase 3 RCT (KetHead Study, NCT05306899) is still recruiting, and TFDA safety labeling data is a Blocking gap — S1 safety pre-assessment cannot proceed without it. Ketamine is also not currently marketed in Saudi Arabia (0 authorizations), so no existing distribution pathway exists.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (resolves Blocking gap DG001)
- Formal DrugBank mechanism of action data (DG002)
- Completion and results of the KetHead Study (NCT05306899) and other ongoing Phase 2/3 trials
- Drug-drug interaction data (currently not found)
- A market entry / distribution assessment given current "not marketed" status in Saudi Arabia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

