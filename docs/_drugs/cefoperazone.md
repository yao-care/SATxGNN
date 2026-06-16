---
layout: default
title: Cefoperazone
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Cefoperazone
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

# Cefoperazone: From Bacterial Infections to Sclerosing Cholangitis

## One-Sentence Summary

Cefoperazone is a third-generation cephalosporin antibiotic with broad-spectrum antibacterial activity, widely recognized for treating serious bacterial infections across multiple organ systems.
The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**,
however, there are currently **0 clinical trials** and **0 publications** directly supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (no Saudi Arabia regulatory authorization on record) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the source database. Based on established pharmacological knowledge, Cefoperazone is a third-generation cephalosporin belonging to the β-lactam antibiotic class. It exerts antibacterial effects by binding to penicillin-binding proteins (PBPs) — in particular PBP3 and PBP1b — thereby disrupting bacterial cell wall synthesis and triggering bacterial lysis. Its spectrum covers many Gram-positive organisms, a broad range of Gram-negative Enterobacteriaceae, and notably Pseudomonas aeruginosa, which distinguishes it from earlier cephalosporins.

Primary sclerosing cholangitis (PSC) is a chronic, progressive, fibroinflammatory disease of the bile ducts driven by autoimmune and multifactorial mechanisms, with strong associations to gut microbiome dysbiosis and intestinal immune dysregulation. The theoretical basis for TxGNN's prediction may lie in the gut-liver axis hypothesis: antibiotics capable of reshaping intestinal microbial communities could, in principle, reduce the pro-inflammatory signals reaching the biliary tract. Cefoperazone's broad anaerobic and Gram-negative coverage might theoretically alter gut microbial composition.

However, this mechanistic link is highly speculative and remains entirely unsupported by evidence. Cefoperazone has no known direct immunomodulatory activity, no anti-fibrotic properties, and no capacity to interrupt the IgG- or T-cell-mediated biliary inflammation that drives PSC progression. The high TxGNN score almost certainly reflects node co-occurrence patterns in the underlying knowledge graph rather than a validated biological relationship, and should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN model score (99.98%), sclerosing cholangitis lacks any clinical or preclinical evidence connecting Cefoperazone to this indication, and no plausible direct mechanistic pathway has been established between a cell-wall-synthesis-inhibiting antibiotic and an autoimmune fibroinflammatory biliary disease.

**To proceed, the following is needed:**
- Preclinical studies (in vitro or animal models of PSC) demonstrating any effect of Cefoperazone on biliary inflammation or hepatic fibrosis
- Evidence specifically linking Cefoperazone's antibacterial spectrum to gut microbiome shifts that are clinically meaningful in PSC
- MOA data retrieval from DrugBank (currently a data gap) to formally assess indirect immunological activities, if any
- Package insert review to identify safety warnings and contraindications before any further evaluation

> **Advisory note:** Among all ten TxGNN-predicted indications evaluated for Cefoperazone, **pneumonia (rank 3)** is by far the most clinically credible repurposing signal. It is backed by 2 registered clinical trials — including an open-label randomized comparative Phase III trial (NCT01280461, n=142) and a Phase 1/2 nebulization trial (NCT02060149) — plus 20 publications including two RCTs. The evidence level is **L2** with a recommendation of **Proceed with Guardrails**. A dedicated evaluation report for the pneumonia indication is strongly recommended as a higher-priority next step.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

