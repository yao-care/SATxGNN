---
layout: default
title: Cyproterone Acetate
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 10
---

# Cyproterone Acetate
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

# Cyproterone Acetate: From Hyperandrogenism to Migraine Disorder

## One-Sentence Summary

Cyproterone Acetate (CPA) is an internationally established synthetic antiandrogen and progestogen, primarily used for hyperandrogenism conditions such as hirsutism, acne, and polycystic ovary syndrome (PCOS) — though it currently holds no marketing authorization in Saudi Arabia.
The TxGNN model predicts it may be effective for **Migraine Disorder**, with **0 clinical trials** and **3 publications** currently supporting this direction.
The mechanistic link is indirect and theoretical; evidence sits at Level L4, and the recommended decision is **Hold** pending further preclinical and clinical investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperandrogenism (hirsutism, acne, PCOS); hormonal therapy for prostate cancer — not registered in Saudi Arabia |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Cyproterone Acetate is not available in this Evidence Pack. Based on known pharmacological information, CPA is a synthetic C21-steroid progestogen with potent anti-androgenic properties. It functions primarily by competitively blocking androgen receptors and centrally suppressing LH and FSH secretion through anti-gonadotropic effects. As a progestogen, CPA also engages neurosteroid pathways: C21-steroids have been shown to act as activators of GABA-A receptor subtypes, stimulate dopamine release in striatal tissue, and modulate opioid receptor binding (PMID 14670648).

The theoretical connection to migraine builds on this neurosteroid-GABAergic framework. Progesterone-related neurosteroids are known to influence cortical excitability and migraine threshold, and a 2002 clinical study (PMID 12390622) observed that different progestogen regimens in hormone replacement therapy differentially affect migraine frequency in postmenopausal women — suggesting that progestogenic pharmacology, which CPA shares, may intersect with migraine biology.

However, no study has directly evaluated CPA as a migraine treatment. The TxGNN prediction reflects knowledge graph topological proximity between CPA's pharmacological nodes and migraine disease nodes, not a validated clinical relationship. A critical countervailing safety signal must also be noted: migraine with aura — a closely related phenotype — is explicitly contraindicated in CPA-containing products (Diane-35) under European clinical guidelines due to elevated cerebrovascular risk. This substantially limits the realistic scope of any repurposing effort targeting migraine.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cyproterone Acetate in migraine disorder.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12390622](https://pubmed.ncbi.nlm.nih.gov/12390622/) | 2002 | Clinical Study | Headache | Three oral HRT regimens evaluated for migraine course in postmenopausal women; progestogen type and delivery scheme differentially affect migraine frequency — indirect basis for progestogen-migraine interaction |
| [14670648](https://pubmed.ncbi.nlm.nih.gov/14670648/) | 2003 | Review | Maturitas | Mechanistic review of progestin-brain interactions; CPA specifically demonstrated to increase dopaminergic responses, bind opiate receptors, and activate GABA-A receptors via C21-steroid mechanism — theoretical neurological basis for migraine threshold modulation |
| [10857213](https://pubmed.ncbi.nlm.nih.gov/10857213/) | 2000 | Observational | Zentralblatt für Gynäkologie | Multicentre safety cohort (2,506 patients, 7,971 patient-years) on long-term CPA-containing therapy; addresses mutagenicity concerns but not migraine efficacy — peripherally relevant to safety profile only |

---

## Saudi Arabia Market Information

Cyproterone Acetate currently holds **no marketing authorization** in Saudi Arabia (SFDA). There are no approved products, registered dosage forms, or licensed indications on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Critical signals identified across the broader evidence review for this drug:**

- **Thromboembolism Risk**: Multiple cohort and case-control studies consistently document that CPA-containing combined oral contraceptives significantly elevate venous thromboembolism (VTE) risk, including deep vein thrombosis (DVT), pulmonary embolism (PE), and cerebral venous sinus thrombosis (CVST). Risk is amplified in patients with inherited thrombophilias such as Factor V Leiden mutation, protein S deficiency, and antithrombin deficiency — conditions that appear as separate TxGNN-predicted "indications" in this pack but are in fact documented contraindications.

- **Contraindication in Migraine with Aura**: European clinical guidelines (CNGOF 2018, PMID 30389542) explicitly list migraine with brainstem aura as a contraindication to Diane-35 (CPA + ethinyl estradiol) due to elevated stroke risk. Any repurposing effort in migraine must rigorously stratify by subtype and exclude aura-positive patients.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for CPA in migraine disorder is limited to three publications describing indirect mechanistic connections via GABA-A receptor modulation and progestogen-HRT interactions — none of which directly evaluate CPA as a migraine therapy. More critically, the closely related indication "migraine with brainstem aura" (TxGNN rank 2) is an established contraindication for CPA-containing products under major clinical guidelines, and CPA's well-documented prothrombotic profile adds further safety complexity to any potential migraine development program.

**To proceed, the following is needed:**

- Preclinical evidence directly evaluating CPA's effect on cortical spreading depression or migraine threshold in validated animal models
- Migraine subtype stratification plan: explicit exclusion of migraine with aura before any clinical protocol is designed
- MOA documentation from DrugBank (currently a data gap) to validate or refute the GABA-A/neurosteroid hypothesis
- Comprehensive thrombovascular risk-benefit analysis addressing CPA's known VTE risk in the migraine patient population
- Saudi Arabia regulatory pathway assessment for a compound with no current SFDA authorization

---

> **Note on Secondary Indication — Amenorrhea (Rank 8):**
> While this report focuses on the TxGNN top-ranked prediction, Amenorrhea (rank 8, TxGNN score 99.28%, Evidence Level L3) represents a substantially more actionable repurposing candidate. It is supported by **4 registered clinical trials** (including a Phase 4 randomized double-blind study, NCT01103518, directly evaluating CPA+EE for menstrual irregularity of hyperandrogenic origin) and **14 publications**. CPA+EE (Diane-35) is an internationally established treatment for PCOS-related menstrual disorders with a well-characterized pharmacological rationale. If SFDA registration is being considered, the amenorrhea/PCOS pathway carries a **"Proceed with Guardrails"** recommendation and should be evaluated as a priority track.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

