---
layout: default
title: Oxcarbazepine
parent: 僅模型預測 (L5)
nav_order: 467
evidence_level: L5
indication_count: 10
---

# Oxcarbazepine
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

# Oxcarbazepine: From Epilepsy to Visual Epilepsy

## One-Sentence Summary

Oxcarbazepine is a well-established antiepileptic drug for partial-onset seizures, though it is not currently registered or marketed in Saudi Arabia. The TxGNN model predicts it may be effective for **Visual Epilepsy**, a reflex epilepsy subtype, with **1 clinical trial** and **19 publications** currently associated with this direction — though none specifically designed for visual/photosensitive epilepsy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Saudi Arabia regulatory data (no license on file); known pharmacological class: antiepileptic (partial-onset seizures) |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the structured data source. Based on known information, oxcarbazepine is a voltage-gated sodium channel blocker, a mechanism shared by the broader class of antiepileptic drugs (AEDs). Its efficacy in partial-onset (focal) epilepsy is well-proven and long-established in clinical practice.

Visual epilepsy is a reflex epilepsy subtype in which seizures are triggered by visual stimuli (e.g., flashing lights, patterns). Rather than representing a wholly new disease category, it falls within the same broad epilepsy spectrum that oxcarbazepine already treats — sharing the underlying pathology of abnormal neuronal hyperexcitability and hypersynchronous discharge.

Because sodium channel blockade dampens neuronal hyperexcitability broadly rather than targeting a stimulus-specific trigger, the mechanism is plausible across seizure subtypes, including reflex/stimulus-induced forms such as visual epilepsy. This is consistent with existing evidence that oxcarbazepine is effective as first-choice combination therapy across multiple focal epilepsy presentations.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Prospective observational (Liceo) study assessing new AEDs — including oxcarbazepine — used as first-choice bitherapy in daily clinical practice for focal epilepsy. Not specific to visually-induced seizures; population overlap only (Relevance grade B). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32129501](https://pubmed.ncbi.nlm.nih.gov/32129501/) | 2020 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Cochrane review of oxcarbazepine as add-on therapy for drug-resistant focal epilepsy. |
| [35429132](https://pubmed.ncbi.nlm.nih.gov/35429132/) | 2022 | RCT | CNS Neurosci Ther | Multicenter, open-label, randomized study comparing oxcarbazepine vs. levetiracetam monotherapy in newly diagnosed focal epilepsy. |
| [35380580](https://pubmed.ncbi.nlm.nih.gov/35380580/) | 2022 | Review | JAMA | Review of antiseizure medications for adults with epilepsy, including oxcarbazepine's role. |
| [33334546](https://pubmed.ncbi.nlm.nih.gov/33334546/) | 2020 | Review | Seizure | Current role of carbamazepine and oxcarbazepine in epilepsy management. |
| [1379159](https://pubmed.ncbi.nlm.nih.gov/1379159/) | 1992 | Review | Drugs | Pharmacology and therapeutic potential of oxcarbazepine in epilepsy, trigeminal neuralgia, and affective disorders. |
| [10530693](https://pubmed.ncbi.nlm.nih.gov/10530693/) | 1999 | Review | Epilepsia | Review of oxcarbazepine, including comparative profile to carbamazepine. |
| [26844734](https://pubmed.ncbi.nlm.nih.gov/26844734/) | 2016 | Review | Continuum (Minneap Minn) | Overview of antiepileptic drugs including oxcarbazepine's clinical pharmacology and modes of use. |
| [39899099](https://pubmed.ncbi.nlm.nih.gov/39899099/) | 2025 | Review | Continuum (Minneap Minn) | 2025 update on antiseizure medications, covering pharmacokinetics, indications and use. |
| [22091603](https://pubmed.ncbi.nlm.nih.gov/22091603/) | 2012 | Clinical Study | Epilepsia | Efficacy, tolerability, and pharmacokinetics of oxcarbazepine oral loading in patients with recurrent seizures. |
| [12697143](https://pubmed.ncbi.nlm.nih.gov/12697143/) | 2003 | Cohort | Epilepsy & Behavior | Safety and tolerability of oxcarbazepine in elderly patients with epilepsy. |

Note: none of the above literature directly studies visual/photosensitive epilepsy specifically — evidence is drawn from oxcarbazepine's general efficacy and safety in focal/generalized epilepsy, extrapolated to the reflex-epilepsy subtype.

---

## Saudi Arabia Market Information

Oxcarbazepine currently holds **no registered marketing authorization in Saudi Arabia** (0 licenses on file; market status: 未上市/Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is direct — oxcarbazepine's sodium channel-blocking action is already proven across the broader epilepsy spectrum, and visual epilepsy is a reflex subtype rather than a novel disease category. However, evidence remains at the observational/review level (L3) with no clinical trial specifically designed for visually-induced seizures, so guardrails around indication-specific evidence gaps are warranted.

**To proceed, the following is needed:**
- TFDA/SFDA-equivalent package insert data (warnings, contraindications) — currently a Blocking data gap
- Detailed mechanism of action (MOA) documentation from DrugBank — currently a High-severity data gap
- Disease-specific clinical evidence (trial or case series) for visual/photosensitive epilepsy, rather than general focal epilepsy extrapolation
- Drug-drug interaction (DDI) data, currently unavailable (query status: not found)
- Regulatory pathway assessment, since the drug is not currently marketed in Saudi Arabia (0 licenses)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

