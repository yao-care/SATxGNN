---
layout: default
title: Nitrazepam
parent: 僅模型預測 (L5)
nav_order: 445
evidence_level: L5
indication_count: 3
---

# Nitrazepam
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

# Nitrazepam: From an Undocumented Original Indication to Insomnia (Sleep Initiation and Maintenance Disorder)

## One-Sentence Summary

Nitrazepam is a classic benzodiazepine hypnotic; this Evidence Pack does not carry a documented original indication or formal mechanism-of-action record for it locally. The TxGNN model predicts it may be effective for **Insomnia (sleep disorder, initiating and maintaining sleep)** — which in practice reproduces nitrazepam's well-known worldwide clinical role rather than uncovering a novel use — supported by **20 publications**, including several head-to-head randomized trials, though **no registered clinical trials** currently exist for this pairing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this Evidence Pack (see note below) |
| Predicted New Indication | Insomnia (Sleep Disorder, Initiating and Maintaining Sleep) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

This Evidence Pack flags detailed mechanism-of-action data as a data gap, and no original indication is recorded for nitrazepam in the local regulatory data. However, the model's own repurposing rationale supplies the pharmacological link: nitrazepam is a classic benzodiazepine that potentiates GABA-A receptor chloride-channel conductance, producing sedative/hypnotic effects — a direct, well-established pharmacological action rather than an indirect inference.

Consistent with this, nitrazepam was originally marketed internationally under the brand name **Mogadon** specifically as a hypnotic for insomnia. In that sense, the TxGNN prediction largely reconstructs an already-known clinical use of the drug rather than proposing a genuinely novel indication — which strengthens confidence in the prediction's face validity, even though local original-indication documentation is currently absent.

Because the mechanistic link (GABA-A potentiation → sedation/sleep induction) is direct and well characterized pharmacologically, the main open questions for this candidate are regulatory (local licensing status) and safety-documentation (label data), not mechanistic plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6135296](https://pubmed.ncbi.nlm.nih.gov/6135296/) | 1983 | RCT | Acta Psychiatrica Scandinavica | Double-blind cross-over in 26 geriatric inpatients: nitrazepam 5mg vs triazolam 0.25mg — similar sleep quantity/quality, no significant psychomotor differences |
| [1743245](https://pubmed.ncbi.nlm.nih.gov/1743245/) | 1991 | RCT | European Journal of Clinical Pharmacology | Double-blind crossover (n=28): nitrazepam 5mg/d vs oxazepam 25mg/d vs placebo — both effective for sleep induction and quality, no adverse dream effects |
| [6669629](https://pubmed.ncbi.nlm.nih.gov/6669629/) | 1983 | RCT | Pharmacology | Double-blind, parallel-group randomized polysomnography study: zopiclone 7.5mg vs nitrazepam 5mg — both immediately and lastingly effective; slight rebound insomnia with nitrazepam |
| [6661386](https://pubmed.ncbi.nlm.nih.gov/6661386/) | 1983 | RCT | British Journal of Clinical Pharmacology | Brotizolam 0.25mg vs nitrazepam 5mg vs placebo in general-practice insomnia — equally effective, no residual next-day effects with either |
| [7037262](https://pubmed.ncbi.nlm.nih.gov/7037262/) | 1981 | Cohort | Clinical Pharmacokinetics | Clinical pharmacokinetic profile of nitrazepam underpinning its dosing and use as a hypnotic |
| [14960254](https://pubmed.ncbi.nlm.nih.gov/14960254/) | 2004 | Cohort | Health Technology Assessment | Evaluated CBT vs continued long-term hypnotic (incl. nitrazepam) use in general practice; assessed clinical and cost impact |
| [4892037](https://pubmed.ncbi.nlm.nih.gov/4892037/) | 1969 | Clinical study | British Medical Journal | 27 patients with acute nitrazepam overdose showed only drowsiness; double-blind trial found nitrazepam as effective as butobarbitone as a hypnotic, and safe |
| [10804040](https://pubmed.ncbi.nlm.nih.gov/10804040/) | 2000 | Review | Drugs | Zolpidem review noting hypnotic efficacy generally comparable to benzodiazepines including nitrazepam, flurazepam, temazepam, and triazolam |
| [3281819](https://pubmed.ncbi.nlm.nih.gov/3281819/) | 1988 | Review | Drugs | Brotizolam pharmacology review showing efficacy comparable to nitrazepam 2.5–5mg, flunitrazepam 2mg, and triazolam 0.25mg |
| [19450355](https://pubmed.ncbi.nlm.nih.gov/19450355/) | 2007 | Review | BMJ Clinical Evidence | Overview of insomnia management in the elderly, contextualizing benzodiazepine hypnotic use as prevalence rises with age |

---

## Saudi Arabia Market Information

Nitrazepam currently holds no marketing authorizations on file (0 licenses; market status: **Not Marketed**).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Local TFDA warnings/contraindications and DDI data are currently unavailable for nitrazepam (flagged as a Blocking data gap — DG001), and this prevents completion of the initial safety review (S1) stage.*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction score is very high (99.89%), the mechanistic link (GABA-A potentiation → sedation) is direct rather than inferred, and multiple head-to-head RCTs support nitrazepam's hypnotic efficacy against comparator agents — yielding an L2 evidence level. However, the drug is not currently marketed locally, and safety-label data needed for a full S1 review is missing.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (DG001, Blocking — required before S1 safety review can proceed)
- Confirmed original indication and regulatory history for nitrazepam locally (currently absent from the data pack)
- Drug-drug interaction data (current query returned no results)
- Assessment of controlled-substance/dependence-liability regulatory pathway, given nitrazepam's benzodiazepine class and no existing local marketing authorization

*Note: TxGNN also surfaced acute encephalopathy with biphasic seizures and late reduced diffusion (AESD) and Wernicke-Korsakoff syndrome as lower-ranked pattern matches, but with no supporting trials or literature (L5, Hold) — these are not pursued further here.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

