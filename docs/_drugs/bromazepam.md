---
layout: default
title: Bromazepam
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 1
---

# Bromazepam
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

# Bromazepam: From Anxiety Disorders to Migraine Disorder

## One-Sentence Summary

Bromazepam is a 1,4-benzodiazepine, primarily used for anxiety and sedation.
The TxGNN model predicts it may be effective for **Migraine Disorder** (rank #12,910),
however **the sole identified clinical trial represents a negative signal** — bromazepam appears as a drug being *withdrawn* in a medication overuse headache (MOH) study, not as a therapeutic agent. There is **0 supportive literature** for this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiety disorders (benzodiazepine class; no local authorization on file) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Bromazepam belongs to the 1,4-benzodiazepine class. It acts as a positive allosteric modulator of GABA-A receptors, enhancing GABAergic inhibitory neurotransmission. In theory, augmenting GABA-mediated inhibition could modulate trigeminal nociceptive pathways involved in migraine pathophysiology — this is the mechanistic basis on which the TxGNN model likely assigns a high prediction score.

However, the theoretical mechanistic link does not translate into a plausible therapeutic relationship in this case. Benzodiazepines — including bromazepam — are among the **highest-risk drug classes for inducing medication overuse headache (MOH)**, a debilitating secondary headache disorder that affects approximately 2% of migraine patients. Chronic benzodiazepine use can paradoxically worsen headache frequency and severity, creating a cycle of dependency and rebound headache. The mechanistic link here is **adverse rather than therapeutic**.

Crucially, the only clinical trial retrieved in the evidence search (NCT04410536) investigates a **home-withdrawal program** for MOH patients — a context in which bromazepam is plausibly one of the *drugs being withdrawn*, not the intervention being tested. This represents an inverted evidence signal: existing clinical research activity around bromazepam and headache disorders points toward harm reduction, not therapeutic repurposing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04410536](https://clinicaltrials.gov/study/NCT04410536) | Phase 4 | Completed | 25 | ⚠️ **Adverse signal** — Home-withdrawal program combined with behavioural therapy for medication overuse headache (MOH) during COVID-19. Bromazepam's likely role is as one of the *overused drugs being withdrawn*, not as the therapeutic agent. This trial does **not** support repurposing; it is evidence of harm potential. |

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Bromazepam has no registered authorizations in Saudi Arabia. No license data to display.

---

## Safety Considerations

Detailed safety data (package insert warnings, contraindications) were not available in this evidence pack. Based on drug class knowledge, the following class-level considerations apply:

- **Benzodiazepine class risks**: dependence, tolerance, withdrawal syndrome, CNS depression, respiratory depression in combination with opioids or alcohol
- **Specific relevance to migraine**: chronic use is a well-established risk factor for **medication overuse headache (MOH)** — this is a **contraindication to repurposing**, not a manageable side effect
- **Elderly population**: falls, cognitive impairment, and paradoxical agitation are known risks

Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score, but the mechanistic basis is counterproductive — benzodiazepines including bromazepam are a recognised cause of medication overuse headache, the opposite of the intended therapeutic effect. The single identified clinical trial reinforces this concern. With zero supportive literature, zero Saudi Arabia authorizations, and an adverse mechanistic profile in the target indication, this candidate does not meet the threshold for further development.

**To proceed, the following would be needed:**
- A credible mechanistic hypothesis that separates GABA-A modulation from MOH induction risk (e.g., evidence that short-term or specific dosing regimens avoid headache chronification)
- At least one positive clinical signal — a prospective study or case series showing bromazepam *reducing* migraine frequency, not causing rebound headache
- Full MOA data from DrugBank to identify any off-target effects (e.g., calcium channel modulation) that might independently support migraine prophylaxis
- Re-evaluation of the TxGNN training data to determine whether the migraine prediction is driven by co-occurrence in headache-disorder patient records (confounding) rather than a true therapeutic signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

