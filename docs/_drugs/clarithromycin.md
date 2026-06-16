---
layout: default
title: Clarithromycin
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 5
---

# Clarithromycin
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

# Clarithromycin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Clarithromycin is a macrolide antibiotic widely used for respiratory tract infections, skin and soft tissue infections, and *Mycobacterium avium* complex (MAC) disease, as well as *Helicobacter pylori* eradication regimens.
The TxGNN model predicts a potential association with **Hyperamylasemia**,
with **0 clinical trials** and **1 case report** currently available — suggesting the connection is mechanistically indirect rather than a direct therapeutic application.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (macrolide antibiotic; no Saudi Arabia authorizations on record) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, clarithromycin is a macrolide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit. It is a cornerstone agent in treating *Mycobacterium avium* complex (MAC) and *Mycobacterium abscessus* pulmonary infections, and also exerts immunomodulatory effects by downregulating pro-inflammatory cytokines (IL-6, IL-8, TNF-α).

The predicted link to hyperamylasemia is **indirect and secondary**, not a direct therapeutic effect on serum amylase. TxGNN most likely constructed this connection through a knowledge graph path: clarithromycin → treats MAC/*M. abscessus* infection → mycobacterial infection can trigger infectious pancreatitis → pancreatitis elevates serum amylase (hyperamylasemia). A secondary pathway also exists: clarithromycin itself has been reported in very rare cases to cause drug-induced pancreatitis, which would also produce hyperamylasemia.

The sole supporting publication (PMID 15228140) describes a case of *M. abscessus* pulmonary infection complicated by primary macroamylasemia — illustrating co-occurrence of mycobacterial disease and elevated amylase, not a clarithromycin treatment effect directed at amylase levels. Hyperamylasemia is a laboratory finding rather than a primary disease target, and no evidence supports clarithromycin as a treatment for hyperamylasemia independent of its antimicrobial indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15228140](https://pubmed.ncbi.nlm.nih.gov/15228140/) | 2004 | Case Report | Nihon Kokyuki Gakkai zasshi (Japanese Respiratory Society) | *M. abscessus* pulmonary infection in a 76-year-old man complicated with primary macroamylasemia; illustrates co-occurrence of mycobacterial infection and elevated amylase — not a direct clarithromycin treatment effect on amylase levels |

---

## Saudi Arabia Market Information

Clarithromycin is **not currently marketed in Saudi Arabia**. No SFDA product authorizations were found in the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted link between clarithromycin and hyperamylasemia is mechanistically indirect (MAC infection → secondary pancreatitis → elevated amylase) and supported only by a single 2004 case report describing co-occurrence rather than therapeutic benefit. Hyperamylasemia is a laboratory marker, not an actionable treatment target in its own right, making this a low-priority repurposing candidate.

**To proceed, the following is needed:**
- Clarify the clinical question: if the goal is to treat hyperamylasemia *caused by* MAC/*M. abscessus* infection, clarithromycin's role as the primary antimicrobial is already well-established and no new repurposing study is required; if the goal is to treat hyperamylasemia of *other* etiologies, a mechanistic rationale must first be established
- Mechanism of action data (MOA) from DrugBank to complete mechanistic gap analysis (DG002)
- Saudi Arabia package insert and SFDA label data for safety screening (DG001)
- If this indication is to be pursued further, a systematic literature review covering macrolide effects on pancreatic amylase secretion is needed as a prerequisite to any research protocol design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

