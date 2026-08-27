---
layout: default
title: Griseofulvin
parent: 僅模型預測 (L5)
nav_order: 301
evidence_level: L5
indication_count: 5
---

# Griseofulvin
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

# Griseofulvin: From Dermatophyte Infection to Myiasis

## One-Sentence Summary

> Griseofulvin is a long-established oral antifungal historically used for dermatophyte (ringworm-type) infections of skin, hair, and nails.
> The TxGNN model predicts it may be effective for **Myiasis** (a parasitic skin infestation by fly larvae),
> but this prediction is currently supported by **0 clinical trials** and only **1 loosely related publication**, with no mechanistic or experimental confirmation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Taiwan license/indication records in the evidence pack (see MOA note below) |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, griseofulvin is an oral antifungal agent that binds fungal microtubule protein and disrupts mitotic spindle formation, inhibiting fungal cell division — its established use is for dermatophyte infections of skin, hair, and nails.

Myiasis, however, is not a fungal disease. It is an entomological condition caused by fly (Diptera) larvae infesting skin or wounds, and griseofulvin has no known insecticidal or larvicidal activity. The only theoretical bridge between the two is that some antiparasitic agents (e.g., benzimidazoles such as albendazole/mebendazole) also act via tubulin binding — but this is a class-level analogy, not evidence specific to griseofulvin itself.

The repurposing rationale supplied with this evidence pack explicitly flags this as a purely model-derived association: there is no experimental or clinical data showing griseofulvin has activity against fly larvae or related parasites (this same caveat applies to the other four predicted indications — creeping myiasis, furuncular myiasis, wound myiasis, and echinococcosis — all of which share the same unsupported mechanistic gap).

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4098614](https://pubmed.ncbi.nlm.nih.gov/4098614/) | 1970 | Review | The Veterinary Record | General review of parasitic skin diseases in dogs and cats; abstract not available, relevance to griseofulvin-myiasis link not yet assessed |

---

## Taiwan Market Information

Griseofulvin currently has no marketing authorization or license records in Taiwan.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN similarity score, none of the top-5 predicted indications (myiasis subtypes and echinococcosis) have any clinical trials or drug-specific literature support, and the proposed mechanistic link relies on a broad tubulin-binding class analogy rather than evidence for griseofulvin itself. The drug is also unmarketed in Taiwan and lacks basic safety documentation.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action data from DrugBank or primary literature (DG002)
- In vitro/in vivo evidence of griseofulvin activity against myiasis-causing larvae or *Echinococcus granulosus*
- Dedicated clinical or case-report evidence before any further evaluation stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

