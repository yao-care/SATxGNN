---
layout: default
title: Doxazosin
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 2
---

# Doxazosin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Doxazosin: From Hypertension / Benign Prostatic Hyperplasia to Migraine Disorder

## One-Sentence Summary

Doxazosin is a selective alpha-1 adrenergic receptor blocker, widely used for hypertension and benign prostatic hyperplasia (BPH). The TxGNN model predicts it may be effective for **Migraine Disorder**, with **1 published literature source** currently supporting this direction and no registered clinical trials. Evidence remains at an exploratory stage, and this candidate is best treated as a research question pending further investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Benign Prostatic Hyperplasia (alpha-1 blocker class; original_indications field not populated in this Evidence Pack) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on available information from the repurposing rationale, Doxazosin is a selective alpha-1 adrenergic receptor blocker that inhibits catecholamine-induced (particularly norepinephrine-induced) vasoconstriction. Its efficacy in controlling hypertension and relieving BPH-related urinary symptoms has been well established clinically.

The theoretical mechanistic bridge to migraine is as follows: cerebral vasculature expresses alpha-1 adrenergic receptors, and blocking these receptors may reduce migraine-associated vascular reactivity. Additionally, sympathetic nervous system over-activation is considered a contributing factor in migraine triggering, and alpha-1 blockade could indirectly modulate this pathway. This is consistent with the one identified publication (Vatz 1997), which reported a decrease in migraine frequency or severity in most patients placed on either terazosin or doxazosin.

However, the mainstream pharmacological mechanisms for migraine prophylaxis centre on beta-blockade, calcium channel antagonism, 5-HT modulation, and anti-epileptic pathways. The alpha-1 adrenergic blockade pathway represents a peripheral hypothesis in migraine pharmacology, and systematic clinical evidence is lacking. The TxGNN prediction score is high (99.20%), suggesting a strong graph-level network association, but this must be interpreted cautiously given the absence of randomised controlled data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Review/Commentary | Headache | Small case series (n=10) in a general neurology practice: patients with migraine placed on terazosin or doxazosin. All but 1 patient showed a decrease in migraine frequency or severity or both. However, 5 of 10 patients discontinued due to side effects (e.g. orthostatic hypotension). No serious adverse reactions reported. |

---

## Saudi Arabia Market Information

Doxazosin is currently **not marketed** in Saudi Arabia. No authorisation records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data (key warnings, contraindications, and drug-drug interactions) were not retrievable for this Evidence Pack. Clinicians should consult the full prescribing information before any clinical use. Known class-effect concerns for alpha-1 blockers include orthostatic hypotension (especially first-dose effect), syncope, dizziness, and caution in patients with hepatic impairment. The 1997 Vatz publication noted that 50% of patients discontinued doxazosin/terazosin due to side effects in the migraine context.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for doxazosin in migraine is limited to a single 1997 review/commentary with a 10-patient informal case series — there are no registered clinical trials and no controlled studies. While the TxGNN prediction score is high and the mechanistic hypothesis is biologically plausible, the evidence base is insufficient to justify further investment without additional research.

**To proceed, the following is needed:**

- **Mechanism of action confirmation:** Retrieve full MOA data from DrugBank to substantiate the alpha-1 → cerebrovascular reactivity hypothesis
- **Safety data retrieval:** Download and parse the package insert (SFDA/TFDA source) to complete the contraindications and key warnings sections (currently blocking for S1 safety evaluation)
- **Systematic literature search expansion:** Search for additional evidence on alpha-1 adrenergic blockers as a drug class in migraine prophylaxis (terazosin, prazosin, alfuzosin), not limited to doxazosin alone
- **Proof-of-concept study:** A small prospective observational study or retrospective database analysis (e.g. hypertensive patients on doxazosin vs. comparators, migraine incidence as secondary endpoint) would constitute minimum required evidence for escalation to L3
- **Re-evaluate migraine with brainstem aura (Rank #2):** This predicted sub-indication (TxGNN score 99.19%, L5) currently has zero supporting evidence. It should remain on hold pending any development in the broader migraine indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

