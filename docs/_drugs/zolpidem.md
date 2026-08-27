---
layout: default
title: Zolpidem
parent: 僅模型預測 (L5)
nav_order: 676
evidence_level: L5
indication_count: 3
---

# Zolpidem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Zolpidem: From Insomnia to Sleep Disorder, Initiating and Maintaining Sleep

## One-Sentence Summary

> Zolpidem is a non-benzodiazepine ("Z-drug") hypnotic already established worldwide as first-line pharmacotherapy for insomnia. The TxGNN model's top prediction, **"sleep disorder, initiating and maintaining sleep,"** is clinically synonymous with insomnia — meaning this result largely **confirms Zolpidem's already-known indication** rather than surfacing a genuinely new one, and it is backed by **20 publications**, including several randomized controlled trials and network meta-analyses, though **zero registered clinical trials appear in this evidence pack**. Two additional, lower-confidence candidates (benign paroxysmal torticollis of infancy; agoraphobia) were also flagged by the model but carry no clinical or mechanistic support and are already scored **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from local licensing records (0 licenses on file); internationally, Zolpidem is approved for short-term treatment of insomnia |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep (i.e., insomnia) |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L1 (supported by long-standing, extensive completed Phase 2/3 RCT and meta-analytic literature on Zolpidem in insomnia) |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured evidence pack (original_moa flagged as a data gap). Based on information contained in the supporting literature, Zolpidem is an imidazopyridine-class, non-benzodiazepine hypnotic that acts as a positive allosteric modulator selective for the α1 subunit of the GABA-A receptor, which underlies its sedative/sleep-promoting effect (Greenblatt & Roth, 2012, PMID 22424586; Sun et al., 2023, PMID 37730991).

The predicted indication — "sleep disorder, initiating and maintaining sleep" — describes the same clinical entity (insomnia) that Zolpidem has been prescribed for since its original approval decades ago. In this sense, the model's top-ranked prediction is best interpreted as a **validation signal** (the model correctly re-derives a drug's known use from the knowledge graph) rather than evidence of true repurposing potential. This is mechanistically unsurprising and expected, given Zolpidem's α1-selective GABAergic action is the established basis for its hypnotic effect (Atkin et al., 2018, PMID 29487083).

The two other model-flagged candidates are materially different: benign paroxysmal torticollis of infancy (rank 2) and agoraphobia (rank 3) have no supporting clinical trials or literature in this pack. As already annotated in the evidence pack itself, neither has a plausible mechanistic link to Zolpidem's α1-selective sedative action — agoraphobia is more associated with α2/α3 GABA-A subunits (anxiolysis), and torticollis of infancy has no established GABAergic basis — so both remain **Hold / L5 (model prediction only)**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Phase 3) | JAMA Network Open | Compared lemborexant vs. placebo vs. zolpidem tartrate ER in older adults with insomnia disorder |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | RCT | JAMA Internal Medicine | Randomized trial of masked benzodiazepine-receptor-agonist taper plus CBT-I for discontinuing hypnotics such as zolpidem |
| [31859791](https://pubmed.ncbi.nlm.nih.gov/31859791/) | 2020 | RCT | Rev Bras Psiquiatr | 3-month randomized trial comparing sublingual (5 mg) vs. oral (10 mg) zolpidem for insomnia, including as-needed middle-of-night dosing |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Systematic Review / Network Meta-analysis | Lancet | Comparative effectiveness of pharmacological insomnia treatments (acute and long-term), including zolpidem, across the drug class |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Systematic Review / Network Meta-analysis | J Manag Care Spec Pharm | Compared efficacy/safety of lemborexant against other insomnia treatments including zolpidem |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Review | Pharmacological Reviews | Reviews pharmacology of Z-drugs (zolpidem, zopiclone, zaleplon) as FDA-approved GABAergic insomnia treatments and their side-effect profile |
| [37549414](https://pubmed.ncbi.nlm.nih.gov/37549414/) | 2023 | Review | J Fam Pract | Update on insomnia management in primary care, including pharmacologic options |
| [38551874](https://pubmed.ncbi.nlm.nih.gov/38551874/) | 2024 | Review | La Revue du Praticien | Reviews pharmacotherapies for insomnia; notes Z-drugs (zolpidem, zopiclone) promote sleep initiation with fewer deleterious effects than long-acting benzodiazepines |
| [22424586](https://pubmed.ncbi.nlm.nih.gov/22424586/) | 2012 | Review | Expert Opin Pharmacother | Reviews zolpidem as the most widely prescribed hypnotic in the US, acting via benzodiazepine-receptor agonism |
| [36472134](https://pubmed.ncbi.nlm.nih.gov/36472134/) | 2023 | Comparative Study | J Clin Sleep Med | Compared treatment response between lemborexant and zolpidem tartrate ER across polysomnography-defined insomnia subtypes |

---

## Saudi Arabia Market Information

Zolpidem currently has **no product authorizations on file** (total_licenses = 0; market_status: 未上市/Not Marketed). No authorization or product-level data is available to tabulate.

---

## Safety Considerations

Structured safety data (key warnings, contraindications, and drug–drug interactions) has not been collected for this candidate — please refer to the official package insert for safety information.

For context only, literature included in this evidence pack (Atkin et al., 2018, PMID 29487083) notes that Z-drugs such as zolpidem carry known risks of cognitive impairment, tolerance, rebound insomnia on discontinuation, falls/motor-vehicle accidents, and abuse/dependence liability — these should be formally verified against official labeling once obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction largely reconfirms Zolpidem's already-known indication (insomnia) rather than identifying a novel repurposing opportunity, and a **blocking data gap** (missing TFDA/SFDA package-insert warnings and contraindications, DG001) currently prevents any formal safety (S1) evaluation. The drug also has zero current market authorization in Saudi Arabia. The two other model-flagged candidates (benign paroxysmal torticollis of infancy; agoraphobia) remain L5/Hold with no clinical, literature, or mechanistic support.

**To proceed, the following is needed:**
- Obtain official package insert (warnings/contraindications) to close DG001 (Blocking)
- Confirm mechanism of action via DrugBank API to close DG002 (High)
- Clarify local regulatory/licensing pathway given current "not marketed" status
- If pursuing rank 2/3 candidates further, generate preclinical/mechanistic rationale before any clinical evidence-gathering, as none currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

