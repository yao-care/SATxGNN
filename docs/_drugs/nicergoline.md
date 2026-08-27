---
layout: default
title: Nicergoline
parent: 僅模型預測 (L5)
nav_order: 438
evidence_level: L5
indication_count: 8
---

# Nicergoline
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

# Nicergoline: From Undocumented Original Indication to Migraine Disorder

## One-Sentence Summary

Nicergoline (DrugBank DB00699) currently has no recorded original indication or approved market presence in Taiwan, and its structured mechanism-of-action field is a data gap.
Among 7 TxGNN-predicted indications, **Migraine Disorder** is the only candidate with any corroborating evidence — **0 clinical trials** but **6 supporting publications** (mostly older mechanistic/preclinical studies, plus one 1984 clinical case series).
The other 6 predicted indications (e.g., hypertrichosis, BPH, Dandy-Walker syndrome) are model-score-only outputs with no literature or trial support and are explicitly flagged in the evidence pack as lacking any known mechanistic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication on file; drug is not marketed in Taiwan |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.12% |
| Evidence Level | L3 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the structured `original_moa` field (flagged as a Blocking/High data gap). However, the repurposing rationale attached to this prediction indicates nicergoline is an ergot alkaloid derivative with alpha‑1 adrenergic receptor antagonism, cerebral vasodilating activity, and serotonin (5‑HT) transport modulation.

These pharmacological properties mechanistically overlap with classical anti-migraine ergot alkaloids (e.g., ergotamine, methysergide), giving the TxGNN prediction some biological plausibility rather than being a purely arbitrary graph-similarity output.

This is also reflected in the literature: several preclinical/mechanistic studies from the 1980s–2000s directly tested nicergoline in migraine-relevant models (cerebral blood flow, serotonin transport/release), and one 1984 Polish-language publication explicitly describes clinical use of nicergoline ("Sermion") for migraine treatment — suggesting a historical, if outdated and thinly documented, precedent for this use.

Because `original_indications` is empty in this evidence pack, no direct comparison to a confirmed original indication can be made — this relationship should be treated as unverified until the drug's approved indication history is retrieved.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6385484](https://pubmed.ncbi.nlm.nih.gov/6385484/) | 1984 | Cohort/Case series | Wiadomości Lekarskie | Direct clinical report on use of nicergoline (Sermion) in migraine treatment; abstract text not available |
| [2622296](https://pubmed.ncbi.nlm.nih.gov/2622296/) | 1989 | Preclinical/Experimental | Methods Find Exp Clin Pharmacol | Nicergoline reduced cerebrovascular resistance and modulated serotonin (5-HT)-induced cerebral vessel constriction in animal models relevant to migraine pathogenesis |
| [8374139](https://pubmed.ncbi.nlm.nih.gov/8374139/) | 1993 | Mechanistic (in vitro) | Biull Eksp Biol Med | Nicergoline, alongside other antimigraine agents, affects serotonin transport in platelets from migraine patients and healthy controls |
| [2625145](https://pubmed.ncbi.nlm.nih.gov/2625145/) | 1989 | Mechanistic (in vitro) | Farmakologiia i Toksikologiia | Nicergoline acts as a competitive inhibitor of serotonin uptake and enhances serotonin release in rat brain synaptosomes, a proposed antimigraine mechanism |
| [2684591](https://pubmed.ncbi.nlm.nih.gov/2684591/) | 1989 | Review | Drugs | Review of flunarizine (a different drug class) for migraine prophylaxis; included as comparator context, does not directly study nicergoline |
| [12924226](https://pubmed.ncbi.nlm.nih.gov/12924226/) | 2003 | Mechanistic/Comparative | Eksp Klin Farmakol | Comparative study of antiserotonin cerebrovascular effects among antimigraine agents; nicergoline not explicitly named in the available abstract |

## Taiwan Market Information

Currently not marketed in Taiwan; no license records are on file (0 authorizations).

## Safety Considerations

Please refer to the package insert for safety information. (TFDA warnings, contraindications, and DDI data are all currently unavailable — TFDA package-insert retrieval is flagged as a **Blocking** data gap.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the migraine indication is limited to older (1980s–2000s) mechanistic/preclinical studies and a single undated-abstract clinical case series from 1984, with no completed or ongoing clinical trials. Combined with a Blocking data gap on TFDA safety warnings/contraindications, the candidate cannot yet proceed to an S1 safety evaluation.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently Blocking
- Confirmed original indication and structured MOA data (currently Data Gap)
- Full-text retrieval and modern re-evaluation of the 1984 case series (PMID 6385484)
- Updated literature/trial search for any recent (post-2003) migraine studies
- Formal drug-drug interaction (DDI) database query (current status: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

