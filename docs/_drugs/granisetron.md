---
layout: default
title: Granisetron
parent: 僅模型預測 (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
---

# Granisetron
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

# Granisetron: From Chemotherapy-Induced Nausea and Vomiting to Manic Bipolar Affective Disorder

## One-Sentence Summary

Granisetron is a 5-HT3 receptor antagonist, originally used to prevent chemotherapy- and radiotherapy-induced nausea and vomiting (CINV/RINV). The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags no known direct pharmacological mechanism connecting 5-HT3 antagonism to mania.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chemotherapy/radiotherapy-induced nausea and vomiting (inferred from drug class in evidence pack; no Saudi Arabia license record on file) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a data gap in the evidence pack). Based on known pharmacology, granisetron is a 5-HT3 (serotonin) receptor antagonist that acts on peripheral vagal afferents and the chemoreceptor trigger zone (CTZ) to block chemotherapy-induced emesis. Its efficacy in this original indication is well established.

For the top-ranked prediction, manic bipolar affective disorder, the model's own repurposing rationale is explicitly cautious: while the serotonergic system is theoretically linked to mood regulation, the primary pharmacological targets for mania are dopaminergic, glutamatergic, and ion-channel pathways (e.g., lithium, anticonvulsants, antipsychotics). No established direct mechanism connects 5-HT3 receptor antagonism to bipolar mania — this association is described as a knowledge-graph-derived inference rather than an evidence-backed hypothesis.

Among the other nine candidates, two show comparatively more plausible (though still unproven) theoretical links: **Tourette syndrome** (rank 2) — central 5-HT3 receptors modulate striatal dopamine release, and the related drug ondansetron has been explored in small tic-symptom trials — and **trichotillomania** (rank 7), an OCD-spectrum disorder where 5-HT3 antagonists have been theoretically discussed as adjuncts to impulse-control treatment. The remaining candidates (conjunctivitis, urticaria, angioedema, bronchitis, NSIAD) are flagged in the source rationale as likely spurious correlations in the embedding space, with no plausible mechanistic basis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications sit at evidence level L5 (model prediction only) with zero clinical trials or literature identified, and the top-ranked candidate (manic bipolar affective disorder) lacks a plausible pharmacological mechanism per the model's own rationale. This is compounded by a **Blocking** data gap (DG001: TFDA/local package insert warnings and contraindications not yet retrieved), which prevents even an initial S1 safety screen, and the drug currently has zero registrations in Saudi Arabia.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve and parse official package insert warnings/contraindications before any S1 safety evaluation
- Resolve DG002 (High): obtain confirmed mechanism-of-action data from DrugBank/literature to properly assess mechanistic plausibility
- Targeted literature/clinical trial search for the mechanistically better-supported candidates (Tourette syndrome, trichotillomania) rather than the top-ranked but mechanistically unsupported manic bipolar affective disorder
- Preclinical or observational evidence before advancing any candidate past decision stage S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

