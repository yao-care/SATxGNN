---
layout: default
title: Amoxicillin
parent: 僅模型預測 (L5)
nav_order: 46
evidence_level: L5
indication_count: 8
---

# Amoxicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# AMOXICILLIN: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Amoxicillin is a broad-spectrum β-lactam antibiotic widely used for treating common bacterial infections including respiratory, urinary tract, and skin infections.
The TxGNN model predicts it may be effective for **Polyclonal Hyperviscosity Syndrome** as its highest-ranked novel indication,
but currently **0 clinical trials** and **0 publications** directly support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (broad-spectrum aminopenicillin antibiotic; no authorizations found in this market) |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacological knowledge, amoxicillin is an aminopenicillin antibiotic that inhibits bacterial cell wall synthesis by irreversibly binding to penicillin-binding proteins (PBPs), preventing peptidoglycan cross-linking, and ultimately causing osmotic lysis of susceptible Gram-positive and selected Gram-negative bacteria.

Polyclonal hyperviscosity syndrome results from the excessive and dysregulated production of immunoglobulins across multiple immunoglobulin classes — an immune-mediated process with no mechanistic intersection with bacterial cell wall inhibition. The underlying pathophysiology (e.g., reactive polyclonal gammopathy from chronic inflammation or autoimmune disease) is wholly unrelated to the antibacterial targets of β-lactam agents.

The high TxGNN prediction score (99.63%) reflects graph-based proximity in the drug-disease knowledge network, not clinical plausibility. Without a demonstrable infectious etiology driving polyclonal immunoglobulin overproduction in a specific clinical context, there is no pharmacological rationale for repurposing amoxicillin in this indication. This prediction is likely a graph topology artefact rather than a genuine therapeutic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Amoxicillin has no registered marketing authorizations in this market based on available data. No authorization table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Polyclonal hyperviscosity syndrome is an immune-driven condition with no mechanistic link to amoxicillin's antibacterial activity, and the complete absence of supporting clinical trials or published literature means this prediction cannot advance beyond model output.

**Predicted Indications Overview — All 8 Candidates**

| Rank | Indication | TxGNN Score | Evidence Level | Decision | Key Note |
|------|-----------|-------------|----------------|----------|----------|
| 1 | Polyclonal Hyperviscosity Syndrome | 99.63% | L5 | Hold | No mechanistic link; immune-mediated |
| 2 | Hyperamylasemia | 99.63% | L5 | Hold | Amoxicillin is a *cause* of drug-induced pancreatitis — opposite direction |
| 3 | Congenital Analbuminemia | 99.59% | L5 | Hold | Genetic disease (ALB mutation); no connection to antibiotics |
| 4 | Blood Group Incompatibility | 99.40% | L5 | Hold | Single case report (PMID [40350274](https://pubmed.ncbi.nlm.nih.gov/40350274/)) describes amoxicillin treating a comorbid infection, not the incompatibility |
| 5 | Premalignant Hematological Disease | 99.29% | L5 | Hold | Category too broad; no evidence or mechanistic link |
| **6** | **Monoclonal Gammopathy** | **99.22%** | **L3** | **Research Question** | **Mechanistic rationale exists for IPSID subtype via H. pylori eradication** |
| 7 | Hematological Disease with Acquired Peripheral Neuropathy | 99.14% | L5 | Hold | Immune-mediated neuropathy; no antibiotic rationale |
| 8 | Septicemic Plague | 99.13% | L4 | Hold | In vitro β-lactam activity shown but clinical standard-of-care is aminoglycosides/doxycycline; β-lactamase resistance limits amoxicillin |

**Most Actionable Finding — Rank 6: Monoclonal Gammopathy (IPSID Subtype)**

Among all 8 predictions, **rank 6 (monoclonal gammopathy, L3)** contains the only clinically grounded repurposing signal. A specific subtype — Immunoproliferative Small Intestinal Disease (IPSID, also known as Mediterranean lymphoma or alpha heavy-chain disease) — is a *Helicobacter pylori*-driven B-cell marginal zone lymphoma that secretes monoclonal IgA heavy chains, satisfying the definition of monoclonal gammopathy. Multiple retrospective studies and case series demonstrate that H. pylori eradication therapy containing amoxicillin can induce complete remission by removing the antigenic stimulus that drives B-cell clonal proliferation (PMID [20300878](https://pubmed.ncbi.nlm.nih.gov/20300878/), PMID [8988128](https://pubmed.ncbi.nlm.nih.gov/8988128/), PMID [9030995](https://pubmed.ncbi.nlm.nih.gov/9030995/)). **This mechanism does not apply to MGUS, multiple myeloma, or other non-IPSID monoclonal gammopathies.**

**To proceed, the following is needed:**

- **MOA data**: Retrieve amoxicillin pharmacodynamics from DrugBank API (currently a blocking data gap)
- **Safety data**: Download and parse TFDA/SFDA package insert PDF to obtain warnings and contraindications
- **For monoclonal gammopathy / IPSID**: Design a prospective study evaluating amoxicillin-containing H. pylori eradication regimens in biopsy-confirmed early-stage IPSID
- **Regulatory pathway assessment**: Determine whether an antibacterial agent can receive an oncology/haematology indication under applicable regulatory frameworks
- **Resistance profiling**: In the context of septicemic plague (rank 8), document regional *Y. pestis* β-lactamase prevalence before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

