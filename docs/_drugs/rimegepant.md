---
layout: default
title: Rimegepant
parent: 僅模型預測 (L5)
nav_order: 547
evidence_level: L5
indication_count: 6
---

# Rimegepant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Rimegepant: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

> Rimegepant is a CGRP receptor antagonist originally developed and marketed globally (as Nurtec® ODT / Vydura®) for the acute and preventive treatment of migraine.
> The TxGNN model predicts it may also be effective for **migraine with brainstem aura**, a subtype in which vasoconstrictive triptans are typically avoided,
> with **0 clinical trials** but **14 supporting publications** currently available — all on general migraine populations rather than this specific subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine — acute treatment (with or without aura) and preventive treatment of episodic migraine (based on literature/known global approval; no formal local license record found) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

No structured mechanism-of-action record is available in the drug database (DrugBank MOA field flagged as a data gap). Based on the literature reviewed below, however, rimegepant is a small-molecule, highly-selective calcitonin gene-related peptide (CGRP) receptor antagonist. It blocks CGRP-mediated vasodilation and neurogenic inflammation — the core pathological mechanism of migraine — and is already approved for both acute and preventive treatment of migraine.

Migraine with brainstem aura (formerly "basilar-type migraine") is a subtype of migraine, not a distinct disease, so the pharmacological rationale carries over directly from the approved indication. What makes this subtype distinct clinically is that triptans — the conventional acute treatment, which act via vasoconstriction — are generally avoided in this population due to concerns about ischemic risk in brainstem/posterior-circulation territory. Because rimegepant's mechanism is non-vasoconstrictive, it is theoretically well-suited as an alternative for exactly this population. A 2026 longitudinal MRA study (PMID 41574090) supports this by directly characterizing rimegepant's effect on cerebral and extracerebral arteries during migraine attacks.

The key caveat is that all 14 publications identified concern the general migraine population; none specifically enrolled or analyzed patients with the brainstem aura subtype. The mechanistic case is sound, but subtype-specific clinical evidence is currently absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32270407](https://pubmed.ncbi.nlm.nih.gov/32270407/) | 2020 | Regulatory Approval Summary | Drugs | FDA approval summary for rimegepant ODT as acute migraine treatment; conventional tablet under review for acute treatment/prevention and trigeminal neuralgia |
| [35790906](https://pubmed.ncbi.nlm.nih.gov/35790906/) | 2022 | Network meta-analysis | The Journal of Headache and Pain | Compares onset of efficacy of lasmiditan vs. rimegepant vs. ubrogepant for acute migraine treatment |
| [41574090](https://pubmed.ncbi.nlm.nih.gov/41574090/) | 2026 | Longitudinal MRA study | Brain Communications | Prospective study of rimegepant's effect on cerebral/extracerebral arteries during spontaneous migraine attacks; supports non-vasoconstrictive mechanism (directly relevant to brainstem aura's triptan-avoidance rationale) |
| [41366286](https://pubmed.ncbi.nlm.nih.gov/41366286/) | 2025 | Phase 4 open-label safety/tolerability study | The Journal of Headache and Pain | 24-week study of once-daily 75mg rimegepant for episodic migraine prevention; evaluates long-term safety/tolerability |
| [41066271](https://pubmed.ncbi.nlm.nih.gov/41066271/) | 2025 | Phase 3 open-label long-term safety study | Cephalalgia | Long-term safety, tolerability and effectiveness of rimegepant ODT for acute migraine treatment in Chinese adults |
| [36739335](https://pubmed.ncbi.nlm.nih.gov/36739335/) | 2023 | Review | CNS Drugs | Comprehensive review of rimegepant in acute and preventive migraine treatment; phase III trials show superiority over placebo |
| [38307667](https://pubmed.ncbi.nlm.nih.gov/38307667/) | 2024 | Review | Handbook of Clinical Neurology | Review of second-generation gepants (rimegepant, ubrogepant) as CGRP-mediated antimigraine drugs |
| [33550872](https://pubmed.ncbi.nlm.nih.gov/33550872/) | 2021 | Review | Pain Management | Review of rimegepant within the broader landscape of new acute/preventive migraine treatments |
| [41652664](https://pubmed.ncbi.nlm.nih.gov/41652664/) | 2026 | Retrospective cohort | Headache | Tolerability and effectiveness of off-label rimegepant use for acute migraine treatment in adolescents |
| [41133671](https://pubmed.ncbi.nlm.nih.gov/41133671/) | 2026 | Phase 1 PK study | Headache | Pharmacokinetics, safety and tolerability of single-dose rimegepant in children aged 6–<12 with migraine history |

---

## Saudi Arabia Market Information

Not marketed; no product authorizations on file (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-interaction data are marked as a Blocking data gap — see Next Steps.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic case is strong — rimegepant's non-vasoconstrictive CGRP antagonism is plausible for the brainstem aura subtype specifically because it avoids the triptan-related ischemic concern — and it is supported by an extensive general-migraine evidence base (14 publications, including Phase 3/4 studies and a vascular-mechanism MRA study). However, zero trials or publications directly address the brainstem aura subtype, and a Blocking-severity data gap exists on local package-insert warnings/contraindications, so this cannot proceed to full evaluation without guardrails.

**To proceed, the following is needed:**
- Local package insert / label data (warnings, contraindications, DDI) — currently a Blocking gap preventing S1 safety review
- Detailed original mechanism-of-action documentation from DrugBank (currently a data gap)
- Subtype-specific clinical evidence (trial or observational data) for migraine with brainstem aura, rather than general migraine extrapolation
- Local regulatory pathway assessment, since the drug is not currently marketed/licensed in this jurisdiction

*Note: TxGNN also flagged five additional candidate indications (atrophoderma vermiculata, ulerythema ophryogenesis, heparin cofactor 2 deficiency, antithrombin deficiency type 2, factor V excess) for rimegepant. All were held (L5, no mechanistic or evidentiary support) and are not discussed further here.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

