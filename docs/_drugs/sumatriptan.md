---
layout: default
title: Sumatriptan
parent: 僅模型預測 (L5)
nav_order: 592
evidence_level: L5
indication_count: 1
---

# Sumatriptan
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

Using the evidence pack as provided (no external lookups), here is the report:

---

# Sumatriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

> Sumatriptan is a 5-HT1B/1D receptor agonist originally used for acute migraine treatment.
> The TxGNN model predicts a possible link to **migraine with brainstem aura**, but this is currently supported only by **0 clinical trials** and **18 publications**, none of which directly studies this specific subtype.
> Critically, the drug's own proposed mechanism (cranial vasoconstriction) is a recognized **safety concern** — not a supportive rationale — for this particular indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute migraine treatment (without aura / typical aura) — inferred from the mechanistic rationale text; not confirmed by local license data (none on file) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (DrugBank MOA field) is marked as a data gap. Based on the mechanistic rationale available in the evidence pack, sumatriptan is a selective 5-HT1B/1D receptor agonist that constricts intracranial blood vessels and inhibits the release of vasoactive neuropeptides from perivascular trigeminal axons — a mechanism well established for typical migraine (with or without classic aura).

However, **migraine with brainstem aura** (formerly "basilar-type migraine") involves posterior-circulation/brainstem dysfunction. A vasoconstrictive agent is theoretically capable of *worsening* posterior-circulation ischemia in this subtype, which is why major headache societies (including AHS/IHS) have long listed it as a relative-to-absolute contraindication for triptans.

In other words, the mechanistic link here is a **warning signal**, not supportive evidence. The TxGNN prediction reflects a graph-level association between sumatriptan and this disease term, but it does not — and cannot — capture this well-documented directional safety concern. This is the central reason the evidence level is capped at L4 (mechanism-only) and the recommendation defaults to Hold rather than any form of proceed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23657930](https://pubmed.ncbi.nlm.nih.gov/23657930/) | 2014 | RCT | Phytotherapy Research | Double-blind RCT comparing ginger powder vs. sumatriptan in acute treatment of common migraine (without aura) — not aura-specific |
| [33567890](https://pubmed.ncbi.nlm.nih.gov/33567890/) | 2021 | RCT | Cephalalgia | Early sumatriptan treatment tested for preventing PACAP38-induced migraine attacks |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review/Guideline | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies, including triptans |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort/Comparative | Neurology | Found reduced efficacy of sumatriptan in migraine **with aura** compared to migraine without aura |
| [1313746](https://pubmed.ncbi.nlm.nih.gov/1313746/) | 1992 | RCT (double-blind, placebo-controlled) | Cephalalgia | Assessed oral sumatriptan (200mg) efficacy specifically in acute migraine **with aura** |
| [31135819](https://pubmed.ncbi.nlm.nih.gov/31135819/) | 2019 | Mechanistic study | JAMA Neurology | Investigated whether sumatriptan crosses into CNS and binds central 5-HT1B receptors during an attack |
| [21469920](https://pubmed.ncbi.nlm.nih.gov/21469920/) | 2011 | Regulatory note | Expert Rev Neurother | Needle-free subcutaneous sumatriptan approved for migraine with or without aura, and cluster headache |
| [8536293](https://pubmed.ncbi.nlm.nih.gov/8536293/) | 1995 | Review | Cephalalgia | Critical review of clinical experience managing migraine and cluster headache with sumatriptan |
| [11801805](https://pubmed.ncbi.nlm.nih.gov/11801805/) | 2001 | Review/Case | Clinical Neuropharmacology | Case-based review of a patient with classic migraine with visual aura |
| [7816788](https://pubmed.ncbi.nlm.nih.gov/7816788/) | 1994 | Review | Pharmacology & Toxicology | Diagnostic criteria and pathophysiology of migraine with and without aura |

*Note: none of the 18 retrieved publications directly studies sumatriptan in "migraine with brainstem aura" specifically; the most relevant items (25841032, 1313746) address migraine with aura broadly, and one (25841032) reports **reduced** triptan efficacy in aura patients.*

---

## Safety Considerations

Please refer to the package insert for safety information (key warnings, contraindications, and drug interaction data are all currently unavailable — flagged as a **Blocking** data gap, DG001).

**Mechanism-based caution (from repurposing rationale, not formal safety data):** Vasoconstrictive 5-HT1 agonists are conventionally considered contraindicated or requiring caution in patients with brainstem/basilar-type aura due to theoretical risk of worsening posterior-circulation ischemia. This should be explicitly verified against the official package insert before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No clinical trials or disease-specific literature support this exact indication, evidence is mechanism-level only (L4), and the proposed mechanism itself raises a plausible safety concern (posterior-circulation vasoconstriction) rather than supporting efficacy — combined with a Blocking data gap on TFDA/SFDA warnings and contraindications, this candidate cannot pass initial (S1) safety screening.

**To proceed, the following is needed:**
- Official package insert data — key warnings and contraindications (DG001, Blocking)
- Confirmed drug-drug interaction (DDI) profile
- Confirmed original MOA and approved indication text from DrugBank/regulatory source (DG002)
- Targeted literature or trial search on triptan safety specifically in brainstem-aura/basilar-type migraine populations, given the known theoretical contraindication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

