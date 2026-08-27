---
layout: default
title: Erenumab
parent: 僅模型預測 (L5)
nav_order: 233
evidence_level: L5
indication_count: 1
---

# Erenumab
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

# Erenumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Erenumab is a CGRP-receptor monoclonal antibody used for migraine prevention in the general migraine population. The TxGNN model predicts it may also be effective for **Migraine with Brainstem Aura**, a subtype that has historically been excluded from pivotal Phase 3 trials. Currently **0 dedicated clinical trials** and **20 supporting publications** (mostly post-hoc analyses and real-world cohorts) back this direction, corresponding to Evidence Level **L3**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack — no Saudi Arabia license or `original_indications` data on file (drug is globally known as a migraine-prevention agent, but this is not confirmed by the source data) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.89% (rank #2610) |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism-of-action text is not available (flagged as a High-severity data gap). However, the evidence pack's own repurposing rationale provides a working mechanistic description: Erenumab is a monoclonal antibody that binds the CGRP receptor, blocking calcitonin gene-related peptide (CGRP) signaling and thereby inhibiting activation of the trigeminovascular system — the core pathogenic pathway believed to drive migraine, including its aura variants.

Migraine with brainstem aura (formerly "basilar-type migraine") shares the same downstream trigeminovascular activation pathway as the migraine subtypes for which erenumab is already used, which is the mechanistic basis for this prediction. However, CGRP is also an important vasodilatory mediator in cerebral and posterior-circulation blood flow, and brainstem aura is thought to involve posterior-circulation vascular regulation. Blocking CGRP could theoretically remove a protective vasodilatory compensation mechanism in this specific subgroup — an additional theoretical safety concern.

Critically, the major Phase 3 RCTs that established erenumab's efficacy (e.g., STRIVE, ARISE) routinely excluded patients with hemiplegic migraine and brainstem aura. As a result, the current evidence base is "reasonable mechanistic extrapolation," not "confirmed efficacy within the target population" — this distinction is central to the evidence-level rating below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for migraine with brainstem aura. (ClinicalTrials.gov and ICTRP searches on 2026-04-21 both returned 0 results; existing pivotal RCTs for erenumab excluded this subgroup.)

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30360965](https://pubmed.ncbi.nlm.nih.gov/30360965/) | 2018 | RCT (Phase 3b) | Lancet | Randomized, double-blind, placebo-controlled trial establishing erenumab efficacy/tolerability in episodic migraine patients who failed 2–4 prior preventives (core pivotal evidence, general migraine population) |
| [34928306](https://pubmed.ncbi.nlm.nih.gov/34928306/) | 2022 | RCT (secondary/post-hoc analysis) | JAMA Neurology | Secondary analysis of RCT data assessing erenumab safety/efficacy specifically in migraine with vs. without aura, given elevated vascular risk in the aura subgroup |
| [37012858](https://pubmed.ncbi.nlm.nih.gov/37012858/) | 2023 | Systematic Review | International Immunopharmacology | Systematic review of erenumab's preventive efficacy across episodic and chronic migraine |
| [36942409](https://pubmed.ncbi.nlm.nih.gov/36942409/) | 2023 | Cohort (post-hoc, pooled trial data) | Headache | Post-hoc cardiovascular safety analysis of erenumab stratified by baseline vascular risk in patients with/without aura |
| [41888647](https://pubmed.ncbi.nlm.nih.gov/41888647/) | 2026 | Cohort (REFORM study) | The Journal of Headache and Pain | Longitudinal characterization of migraine aura frequency changes during and after erenumab treatment in patients with confirmed frequent aura |
| [40275185](https://pubmed.ncbi.nlm.nih.gov/40275185/) | 2025 | Cohort (biomarker, REFORM study) | The Journal of Headache and Pain | Plasma suPAR (inflammation biomarker elevated in migraine with aura) evaluated as a predictor of erenumab therapeutic response |
| [35151970](https://pubmed.ncbi.nlm.nih.gov/35151970/) | 2022 | Cohort (real-world) | Clinical Neurology and Neurosurgery | Real-world 6-month effectiveness and safety of erenumab in treatment-resistant chronic migraine (Croatian cohort) |
| [35538414](https://pubmed.ncbi.nlm.nih.gov/35538414/) | 2022 | Cohort (real-world, 12-month) | The Journal of Headache and Pain | 12-month real-world safety/tolerability data and predictors of adverse events during erenumab prophylaxis |
| [38071464](https://pubmed.ncbi.nlm.nih.gov/38071464/) | 2024 | Cohort (retrospective, clinical/genetic) | Headache | Real-world community cohort identifying clinical and genetic characteristics associated with response to anti-CGRP monoclonal antibodies |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review (mechanistic) | Handbook of Experimental Pharmacology | Foundational review of CGRP's role in migraine pathophysiology, underpinning the mechanistic rationale for CGRP-targeted therapy |

---

## Saudi Arabia Market Information

Erenumab is currently **not marketed in Saudi Arabia** — 0 authorizations are on file, so no product/license table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were available in this evidence pack (all flagged as data gaps). Notably, retrieval of the TFDA/SFDA package insert (warnings and contraindications) is flagged as a **Blocking** data gap (DG001) — this evidence pack cannot currently support a formal S1 safety pre-assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The pivotal Phase 3 trials that support erenumab's general migraine-prevention efficacy explicitly excluded brainstem-aura patients, so the current evidence (L3: post-hoc analyses and real-world cohorts) is mechanistic extrapolation rather than population-specific confirmation, and there is a theoretical vascular safety concern specific to this subgroup.
- A Blocking data gap (missing TFDA/SFDA package insert — warnings and contraindications) prevents this candidate from entering a formal safety pre-assessment (S1) at all.

**To proceed, the following is needed:**
- Retrieve the TFDA/SFDA package insert (warnings, contraindications) to resolve the Blocking data gap (DG001)
- Confirm detailed mechanism-of-action data via the DrugBank API to resolve the High-severity data gap (DG002)
- Seek or commission trial data specifically enrolling patients with confirmed brainstem/basilar-type aura (or at minimum hemiplegic migraine, given shared exclusion criteria), given the theoretical posterior-circulation vascular risk raised in the mechanistic rationale
- Obtain confirmed original-indication and licensing data, since none were available in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

