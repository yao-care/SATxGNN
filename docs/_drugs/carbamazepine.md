---
layout: default
title: Carbamazepine
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
---

# Carbamazepine
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

# Carbamazepine: From Epilepsy / Trigeminal Neuralgia to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Carbamazepine (CBZ) is a classic antiepileptic and analgesic drug with established global use for epilepsy, trigeminal neuralgia, and neuropathic pain, though it is not currently registered in Saudi Arabia.
The TxGNN model predicts it may be relevant for **Trigeminal Nerve Neoplasm** with a score of **99.9976%**, but this prediction likely reflects a knowledge graph overlap between trigeminal nerve tumor and trigeminal neuralgia rather than a direct antitumor effect.
Current evidence includes **1 observational imaging study** and **20 publications**, though the substantive literature addresses secondary trigeminal neuralgia caused by tumors — not the neoplasm itself.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Saudi Arabia; globally established for epilepsy and trigeminal neuralgia |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.9976% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

> ⚠️ **Critical Conceptual Warning**: "Trigeminal Nerve Neoplasm" ≠ "Trigeminal Neuralgia." The high TxGNN score most likely arises from a knowledge graph artifact: tumors of the trigeminal nerve and trigeminal neuralgia share the same anatomical node in the graph, creating a spurious association.

Formal mechanism of action data was not retrievable from DrugBank in this evidence pack. However, based on the pharmacological references cited throughout the literature, carbamazepine acts as a **voltage-gated sodium channel (Nav) blocker**, suppressing high-frequency repetitive neuronal firing. This mechanism underlies its well-established efficacy in epilepsy and classical trigeminal neuralgia.

Trigeminal nerve neoplasms (primary lymphoma, schwannoma, meningioma, granuloma, etc.) can compress or invade the trigeminal nerve, generating secondary trigeminal neuralgia (TN) through focal demyelination and ectopic nerve discharges. In this specific clinical context, CBZ may provide **symptomatic pain relief** by suppressing those ectopic discharges. PMID 3181365 provides the only direct mechanistic data in this direction: intravenous CBZ immediately inhibited spontaneous discharges in experimental saphenous neuromas in rats, confirming CBZ's ability to silence aberrant firing from injured peripheral nerve tissue. Case reports (PMID 30741017, 25142539) further confirm that CBZ is routinely prescribed as a first-line symptomatic agent when tumor-related TN is initially suspected or confirmed.

**The critical boundary**: CBZ does not treat the tumor itself — it addresses the neuropathic pain symptom only. Any application in trigeminal nerve neoplasm must be framed as adjunct symptomatic management, not disease-modifying therapy. Once the diagnosis of malignancy is established, surgical or oncological intervention takes precedence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06853119](https://clinicaltrials.gov/study/NCT06853119) | N/A | Not Yet Recruiting | 120 | MRI-based observational study examining brain network dynamics and microstructural plasticity in trigeminal neuralgia patients; no CBZ intervention arm; disease target is TN not trigeminal neoplasm |

No clinical trials specifically evaluating CBZ for trigeminal nerve neoplasm were identified. The single trial found studies trigeminal neuralgia (a related but distinct condition) and includes no drug intervention.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | Animal/Lab | Experimental Neurology | **Only direct mechanistic evidence**: IV CBZ immediately suppressed spontaneous A-fibre discharges in rat saphenous neuromas at clinical dose ranges |
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Review | Acta Clinica Croatica | Treatment overview for TN; notes tumor compression as a recognised cause of secondary TN amenable to CBZ |
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | Case Report | British Journal of Neurosurgery | Primary trigeminal nerve lymphoma initially treated with CBZ; lack of improvement prompted MRI and correct diagnosis — illustrates CBZ's diagnostic role |
| [25142539](https://pubmed.ncbi.nlm.nih.gov/25142539/) | 2014 | Case Report | Clinical Neurology | Malignant lymphoma spreading along trigeminal nerve; CBZ initially improved neuralgic pain, then failed when non-neuralgic tumour pain developed |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Review of Neurotherapeutics | Comprehensive TN treatment review; CBZ is first-line medical therapy; vascular and mass compression cause focal demyelination and aberrant firing |
| [33989821](https://pubmed.ncbi.nlm.nih.gov/33989821/) | 2021 | Case Report | World Neurosurgery | Petroclival meningioma encasing the fifth cranial nerve causing TN; surgical resection via Kawase approach |
| [9109911](https://pubmed.ncbi.nlm.nih.gov/9109911/) | 1997 | Case Report | Neurology | Post-irradiation neuromyotonia in bilateral facial and trigeminal distribution responded to CBZ therapy — supports CBZ efficacy in radiation-damaged trigeminal nerve |
| [22647513](https://pubmed.ncbi.nlm.nih.gov/22647513/) | 2012 | Case Report | No Shinkei Geka | Combined glossopharyngeal and trigeminal neuralgia; CBZ is standard initial medical treatment before microvascular decompression |
| [12590697](https://pubmed.ncbi.nlm.nih.gov/12590697/) | 2003 | Case Report | Neurosurgery | Trigeminal nerve sarcoid granuloma (a benign mass lesion) mimicking schwannoma; granulomatous compression can cause secondary TN |
| [26768887](https://pubmed.ncbi.nlm.nih.gov/26768887/) | 2016 | Case Report | Turkish Neurosurgery | Pituitary adenoma causing isolated trigeminal neuralgia via cavernous sinus invasion; CBZ may provide transient symptomatic relief pending surgical planning |

---

## Saudi Arabia Market Information

Carbamazepine is **not currently registered in Saudi Arabia**. The regulatory query returned zero product licenses. Clinical use would require either compassionate use authorisation or an import permit under Saudi Food and Drug Authority (SFDA) regulations.

---

## Safety Considerations

Please refer to the package insert for safety information. No safety data (key warnings, contraindications, or drug interactions) was retrievable from the available data sources for this report. Formal SFDA package insert review is required before any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for "trigeminal nerve neoplasm" most likely reflects a knowledge graph artifact rather than a genuine novel repurposing signal. CBZ has no antitumour activity, and the available evidence supports only **symptomatic pain management** for secondary TN arising from nerve compression — a use that already falls within CBZ's established neuropathic pain indication. With zero clinical trials targeting this specific disease entity, no formal safety data on file, and no Saudi Arabia registration, advancement as a repurposing candidate is premature.

**To proceed, the following is needed:**
- **Clarify the clinical question**: Is the target (a) antitumour therapy, or (b) adjunct pain management in trigeminal nerve neoplasm patients? Only (b) has any mechanistic basis.
- **Reclassify if (b)**: Frame as "CBZ for secondary TN in trigeminal nerve neoplasm" — this would likely be considered an extension of the existing neuropathic pain indication rather than true repurposing.
- **Retrieve formal MOA data** from DrugBank API to document the Nav-blocking mechanism in the evidence dossier.
- **Obtain full safety data**: Package insert warnings, contraindications, and DDI profile are currently unavailable and are mandatory before any clinical use.
- **SFDA registration pathway**: Establish import or registration route for Saudi Arabia if clinical use is planned.
- **Consider rank-2 indication (startle epilepsy, L3)** as a more scientifically coherent repurposing candidate: case series (PMID 6465864) show direct CBZ efficacy, and the mechanistic link to Nav-dependent reflex seizures is substantially stronger.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

