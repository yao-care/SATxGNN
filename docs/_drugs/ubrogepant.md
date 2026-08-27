---
layout: default
title: Ubrogepant
parent: 僅模型預測 (L5)
nav_order: 649
evidence_level: L5
indication_count: 3
---

# Ubrogepant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using no specific skill — this is a direct report-generation task fully specified by the prompt template; skills like txgnn-pipeline cover pipeline engineering, not report authoring, so I'll follow the template as given.

# Ubrogepant: From Acute Migraine Treatment to Migraine with Brainstem Aura

## One-Sentence Summary

Ubrogepant is an oral CGRP receptor antagonist originally approved (US, 2019) for acute treatment of migraine with or without aura. The TxGNN model predicts it may also be effective for **migraine with brainstem aura**, a rare migraine subtype historically excluded from triptan trials due to vasoconstriction concerns, but current evidence is drawn from general migraine studies rather than trials targeting this specific subtype — **0 clinical trials** and **20 publications** were found, none of which studied the brainstem-aura subtype directly.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute treatment of migraine, with or without aura (FDA-approved; no regulatory record in Saudi Arabia) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Ubrogepant is a small-molecule calcitonin gene-related peptide (CGRP) receptor antagonist — a "gepant" — that blocks CGRP, a key mediator of migraine pain signaling. It received its first global (US) approval in December 2019 for acute treatment of migraine with or without aura, based on the ACHIEVE I and ACHIEVE II Phase 3 randomized trials.

The predicted new indication, migraine with brainstem aura (formerly "basilar-type migraine"), is a rare migraine subtype defined by brainstem-origin aura symptoms. Because this subtype was historically thought to involve intracranial vasoconstriction, patients with brainstem aura were typically excluded from triptan (5-HT1B/1D agonist) trials, which carry vasoconstrictive risk. Gepants such as ubrogepant act through CGRP receptor blockade rather than vasoconstriction, so they are mechanistically plausible for use in this excluded population — this is the core logic behind the TxGNN prediction.

However, this is largely a mechanistic extrapolation rather than a directly confirmed finding: none of the retrieved literature or trials specifically enrolled or analyzed a "migraine with brainstem aura" subgroup. The evidence base instead consists of general acute-migraine efficacy/safety data (including cardiovascular-risk subgroup analyses), which supports the *plausibility* of use in a vasoconstriction-sensitive population but does not directly demonstrate efficacy in brainstem aura specifically.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37979595](https://pubmed.ncbi.nlm.nih.gov/37979595/) | 2023 | RCT (Phase 3) | Lancet | Ubrogepant 100 mg outperformed placebo when taken during the migraine prodrome (before headache onset), supporting early intervention potential. |
| [31742631](https://pubmed.ncbi.nlm.nih.gov/31742631/) | 2019 | RCT (ACHIEVE II) | JAMA | Confirmed superiority of ubrogepant vs. placebo for pain freedom and relief of the most bothersome migraine symptom at 2 hours. |
| [31913519](https://pubmed.ncbi.nlm.nih.gov/31913519/) | 2020 | RCT (52-week extension) | Headache | Long-term safety and tolerability of ubrogepant confirmed under repeated intermittent use over 52 weeks. |
| [33874756](https://pubmed.ncbi.nlm.nih.gov/33874756/) | 2021 | RCT post-hoc analysis | Cephalalgia | Efficacy and safety maintained across cardiovascular risk categories in pooled ACHIEVE I/II data — relevant given gepants' lack of vasoconstrictive effect. |
| [35790906](https://pubmed.ncbi.nlm.nih.gov/35790906/) | 2022 | Network meta-analysis | J Headache Pain | Compared relative efficacy/speed of onset of lasmiditan, rimegepant, and ubrogepant for acute migraine treatment. |
| [32020557](https://pubmed.ncbi.nlm.nih.gov/32020557/) | 2020 | Review | Drugs | Summarizes ubrogepant's first global approval (US, Dec 2019) as an oral CGRP antagonist for acute migraine with or without aura. |
| [32011192](https://pubmed.ncbi.nlm.nih.gov/32011192/) | 2020 | Review | Expert Opin Pharmacother | Reviews CGRP pathway biology and ubrogepant's development as a migraine-specific abortive treatment. |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Review | Neurology International | Overview of ubrogepant's role in acute migraine treatment in adults, including dosing and safety profile. |
| [39569702](https://pubmed.ncbi.nlm.nih.gov/39569702/) | 2025 | Cohort (TANDEM study) | Headache | Evaluated safety/tolerability of ubrogepant for acute attacks in patients already on atogepant for prevention — no unexpected safety signal. |
| [39262541](https://pubmed.ncbi.nlm.nih.gov/39262541/) | 2024 | Case Report | Cureus | Single case of treatment-resistant migraine (without aura) showing substantial improvement with ubrogepant. |

## Saudi Arabia Market Information

Not marketed in Saudi Arabia; no authorization records available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ubrogepant has a well-established Phase 3 efficacy/safety record for acute migraine in general, and its non-vasoconstrictive mechanism is mechanistically consistent with use in brainstem aura, a subtype where vasoconstrictive agents are avoided. However, no trial or publication has directly studied this subtype, so evidence is extrapolated rather than confirmed (L2).

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (currently a blocking data gap — DG001)
- Formal DrugBank/MOA verification (DG002)
- A dedicated trial or registry analysis in patients with migraine with brainstem aura to confirm efficacy and rule out any residual vasoconstrictive risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

