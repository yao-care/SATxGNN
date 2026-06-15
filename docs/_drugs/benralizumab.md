---
layout: default
title: Benralizumab
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 5
---

# Benralizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Benralizumab: From Severe Eosinophilic Asthma to Thrombocytopenia Due to Immune Destruction

## One-Sentence Summary

Benralizumab is a humanized anti-IL-5Rα monoclonal antibody globally approved for severe eosinophilic asthma, achieving near-complete eosinophil and basophil depletion via antibody-dependent cellular cytotoxicity (ADCC).
The TxGNN model predicts it may be effective for **Thrombocytopenia Due to Immune Destruction (ITP)**,
however this prediction is currently supported by **0 clinical trials** and **0 publications** — making it a model-only signal with no empirical backing.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe eosinophilic asthma (globally approved; not registered in Saudi Arabia) |
| Predicted New Indication | Thrombocytopenia Due to Immune Destruction |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Benralizumab is a fully humanized IgG1κ monoclonal antibody that binds directly to the alpha subunit of the IL-5 receptor (IL-5Rα) expressed on eosinophils and basophils. Unlike mepolizumab and reslizumab — which block the IL-5 ligand — benralizumab acts at the receptor level and recruits natural killer cells to eliminate IL-5Rα-bearing cells via ADCC, achieving near-complete peripheral and tissue eosinophil depletion within weeks. This mechanism is well-validated in severe eosinophilic asthma, where eosinophilic airway inflammation is the central pathological driver.

The mechanistic link to immune thrombocytopenia (ITP), however, is tenuous. ITP is primarily mediated by anti-platelet autoantibodies (targeting GPIIb/IIIa, GPIb/IX) and macrophage-driven platelet phagocytosis in the spleen, with underlying immune dysregulation centered on Th1 overactivation and Treg deficiency — not the Th2/eosinophilic axis that benralizumab targets. While eosinophil depletion can modestly reshape the broader immune microenvironment, this indirect effect is unlikely to meaningfully correct the Th1-dominant autoimmune mechanism of ITP.

The high TxGNN score (99.34%) most likely reflects a **graph-proximity artefact**: benralizumab's node in the drug-disease knowledge graph sits close to immune/inflammatory disease clusters, and ITP shares network neighbors with IL-5-associated conditions such as atopic dermatitis and eosinophilic disorders. This is a recognized limitation of graph neural network repurposing models when mechanistic plausibility is not explicitly encoded as a graph constraint.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Benralizumab is currently not registered or marketed in Saudi Arabia. No regulatory authorizations are on file (total licenses: 0). The drug holds approvals in the United States (FDA, 2017), European Union (EMA), Japan, and other jurisdictions for severe eosinophilic asthma, but none of these extend to Saudi Arabia's SFDA at the time of this report.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a purely model-driven prediction (L5) with zero supporting clinical trials or published literature for benralizumab in immune thrombocytopenia. The IL-5Rα/eosinophil mechanism has no established relevance to ITP pathophysiology, and the high TxGNN rank is likely attributable to knowledge-graph neighborhood effects rather than a true mechanistic signal.

**To proceed, the following is needed:**

- **Mechanistic evidence:** Preclinical studies or case reports demonstrating that IL-5Rα depletion influences platelet autoimmunity or modifies Th1/Treg balance in ITP models
- **Hypothesis-generating data:** Case series or retrospective analyses of ITP incidence in eosinophilic asthma patients treated with benralizumab
- **MOA clarification:** Full DrugBank mechanism-of-action data (currently a data gap) to better assess off-target immunomodulatory potential
- **Saudi Arabia registration:** Benralizumab requires SFDA registration before any local clinical development or use is possible
- **Priority redirect:** Evidence for the rank-2 prediction (dermatitis) is substantially richer — 6 clinical trials and 20 publications exist, including a completed Phase 2 RCT (HILLIER; PMID 37178404) that returned a **negative primary endpoint** for atopic dermatitis, and an ongoing Phase 2 trial in DRESS (NCT06734884, a highly eosinophilic skin disease subtype) that merits closer monitoring as a mechanistically better-fit indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

