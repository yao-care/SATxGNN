---
layout: default
title: Topiramate
parent: 僅模型預測 (L5)
nav_order: 628
evidence_level: L5
indication_count: 9
---

# Topiramate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Topiramate: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Topiramate is a broad-spectrum antiepileptic drug (AED) with an established pharmacological role in epilepsy and migraine prophylaxis. The TxGNN model's top-ranked prediction for this candidate is **Trigeminal Nerve Neoplasm**, but this signal is currently backed by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale flags it as a likely knowledge-graph artifact rather than a genuine pharmacological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (partial-onset and generalized seizures); migraine prophylaxis — established uses per the literature evidence in this pack, though no formal Saudi Arabia regulatory record is on file |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal DrugBank MOA data is not on file for this candidate, but the model's own mechanistic rationale describes topiramate's known pharmacology: sodium/calcium channel blockade, GABA-A receptor potentiation, AMPA/kainate glutamate receptor antagonism, and carbonic anhydrase inhibition. Collectively, these mechanisms dampen neuronal excitability — the pharmacological basis for topiramate's established use in seizure disorders.

Trigeminal nerve neoplasm, however, is a structural and proliferative pathology (a tumor), not a disorder of neuronal excitability. There is no known mechanistic pathway by which excitability-modulating or anticonvulsant action would influence tumor growth, and the evidence search returned zero clinical trials and zero publications connecting topiramate to this indication.

The model's own rationale states this directly: the high prediction score most likely arises from the knowledge graph placing "trigeminal neuralgia" and "seizure"-related nodes in close proximity to "trigeminal nerve neoplasm," producing a structural inference bias rather than a real pharmacological signal. This top-ranked prediction should therefore be treated as a hypothesis-generation artifact, not a validated repurposing lead. Notably, within this same prediction batch, rank 2 ("visual epilepsy") is mechanistically coherent — it is simply an extension of topiramate's existing antiepileptic use into a reflex-epilepsy subtype — and is supported by a completed Phase 3 monotherapy RCT (n=750) plus multiple Cochrane reviews, making it a substantially stronger candidate signal than rank 1.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information. Note: retrieval of the official TFDA/SFDA package insert (warnings/contraindications) is currently a **Blocking** data gap (DG001), which independently prevents this candidate from entering a formal S1 safety pre-assessment regardless of the efficacy evidence above.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (trigeminal nerve neoplasm) has zero direct clinical or literature evidence (Evidence Level L5), and the model's own mechanistic reasoning identifies it as a probable knowledge-graph proximity artifact rather than a genuine pharmacological hypothesis. Combined with a Blocking gap on package-insert safety data, there is no basis to advance this specific indication.

**To proceed, the following is needed:**
- Resolve DG001 — obtain the official package insert (warnings, contraindications) before any safety pre-assessment can begin
- Resolve DG002 — obtain a formal DrugBank/structured MOA record for this drug
- Independent pharmacological or preclinical validation of any topiramate–neoplasm mechanism, if this specific signal is to be pursued further
- Consider redirecting evaluation effort within this same candidate batch toward rank 2 ("visual epilepsy" — L1 evidence, Phase 3 RCT n=750, multiple Cochrane systematic reviews, Recommendation: Proceed with Guardrails), which represents a mechanistically coherent extension of topiramate's existing antiepileptic use and a far stronger repurposing lead than the top-ranked score alone suggests
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

