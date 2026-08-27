---
layout: default
title: Tiotropium
parent: 僅模型預測 (L5)
nav_order: 622
evidence_level: L5
indication_count: 10
---

# Tiotropium
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

Using the report template you provided as direct task instructions (no additional skill needed — this is a self-contained content-generation spec). One flag before the report: the evidence pack's own `repurposing_rationale` for rank 1 explicitly states "obstructive lung disease" is the *superset term* for tiotropium's already-established COPD indication, not a novel hypothesis — I've kept that caveat visible rather than glossing over it.

---

# Tiotropium: From Chronic Obstructive Pulmonary Disease to Obstructive Lung Disease

## One-Sentence Summary

> Tiotropium is a long-acting muscarinic antagonist (LAMA) bronchodilator whose established use is maintenance treatment of chronic obstructive pulmonary disease (COPD).
> The TxGNN model's top prediction, **obstructive lung disease**, is the broader diagnostic category that already contains COPD — so this is best read as the model correctly re-identifying tiotropium's known therapeutic class rather than surfacing a genuinely new indication.
> The signal is nonetheless backed by an unusually large evidence base — **50 clinical trials** and **20 publications** — reflecting decades of accumulated COPD/asthma data rather than new repurposing evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Obstructive Pulmonary Disease (COPD) — well-established global indication; not captured in the local license record (0 authorizations on file) |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action record is not available for this drug (flagged as a data gap). Based on the literature evidence collected, tiotropium is a long-acting muscarinic (M1/M2/M3) receptor antagonist that dissociates especially slowly from M3 receptors on bronchial smooth muscle, producing sustained bronchodilation with once-daily dosing (PMID 12010082, 11281822, 10069510).

"Obstructive lung disease" is not a distinct new disease — it is the umbrella category under which COPD (and, in this evidence set, asthma) already sits. The mechanistic link is therefore not a novel hypothesis: it is the same M3-antagonism/bronchodilation pathway that underlies tiotropium's existing COPD indication, extended in the evidence pack to include LAMA use in asthma (e.g., add-on therapy in severe persistent asthma, pediatric/adolescent asthma trials).

Practically, this means the "repurposing candidate" should be interpreted as a **confirmatory signal for an already-known drug class use**, not a discovery. Its value lies in consolidating the strength of existing evidence (useful for a formulary or label-expansion decision), not in opening a new therapeutic avenue.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01012765](https://clinicaltrials.gov/study/NCT01012765) | Phase 3 | Completed | 173 | Crossover RCT using open-label tiotropium (18µg) as active comparator to assess indacaterol's effect on inspiratory capacity in moderate COPD |
| [NCT00274521](https://clinicaltrials.gov/study/NCT00274521) | Phase 3 | Completed | 108 | 25-week placebo-controlled RCT: tiotropium improved exercise tolerance and dyspnea in COPD patients undergoing pulmonary rehabilitation |
| [NCT01233284](https://clinicaltrials.gov/study/NCT01233284) | Phase 2 | Completed | 149 | Crossover dose-ranging trial of tiotropium Respimat (1.25–5.0 µg) vs placebo in moderate persistent asthma inadequately controlled on ICS |
| [NCT01120691](https://clinicaltrials.gov/study/NCT01120691) | Phase 3 | Completed | 2,224 | 64-week RCT comparing QVA149 vs glycopyrronium vs open-label tiotropium on COPD exacerbations in severe/very severe COPD |
| [NCT03158311](https://clinicaltrials.gov/study/NCT03158311) | Phase 3 | Completed | 1,426 | 24-week non-inferiority RCT of QVM149 vs free combination salmeterol/fluticasone + tiotropium in uncontrolled asthma |
| [NCT01634139](https://clinicaltrials.gov/study/NCT01634139) | Phase 3 | Completed | 403 | 48-week placebo-controlled RCT of tiotropium Respimat in children (6–11y) with moderate persistent asthma |
| [NCT00776984](https://clinicaltrials.gov/study/NCT00776984) | Phase 3 | Completed | 453 | 48-week RCT: tiotropium Respimat (5µg) as add-on controller therapy in severe persistent asthma on top of usual care |
| [NCT04184297](https://clinicaltrials.gov/study/NCT04184297) | N/A | Completed | 27,190 | Large real-world comparative-effectiveness study: tiotropium+olodaterol vs ICS/LABA/LAMA combinations across COPD exacerbation-risk subgroups |
| [NCT05402020](https://clinicaltrials.gov/study/NCT05402020) | N/A | Completed | 17,018 | Taiwan NHI claims-based real-world study comparing tiotropium/olodaterol vs ICS/LABA effectiveness and safety in COPD |
| [NCT04208581](https://clinicaltrials.gov/study/NCT04208581) | Phase 3 | Unknown | 372 | RCT of Chinese herbal granule + standard care (including LAMA) for mortality reduction in COPD with chronic respiratory failure; status unknown, indirect evidence only |

*50 trials were returned in the source search; the 10 above were prioritized for design quality (RCTs), sample size, and coverage of both COPD and asthma populations.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25046211](https://pubmed.ncbi.nlm.nih.gov/25046211/) | 2014 | Systematic Review | Cochrane Database Syst Rev | Cochrane review confirming tiotropium's efficacy vs placebo across multiple COPD trials, including soft-mist inhaler formulations |
| [29605624](https://pubmed.ncbi.nlm.nih.gov/29605624/) | 2018 | RCT | Lancet Respir Med | DYNAGITO trial: tiotropium+olodaterol vs tiotropium alone for COPD exacerbation prevention |
| [28877027](https://pubmed.ncbi.nlm.nih.gov/28877027/) | 2017 | RCT | N Engl J Med | Long-term tiotropium in mild/moderate early-stage COPD improved lung function and slowed decline |
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Systematic Review | Cochrane Database Syst Rev | Comparative review of tiotropium vs ipratropium bromide in stable COPD |
| [27271056](https://pubmed.ncbi.nlm.nih.gov/27271056/) | 2016 | Systematic Review | Cochrane Database Syst Rev | ICS/LABA plus tiotropium vs tiotropium or ICS/LABA alone in COPD maintenance |
| [12010082](https://pubmed.ncbi.nlm.nih.gov/12010082/) | 2002 | Review | Drugs | Pharmacology review: tiotropium's slow M3-receptor dissociation underlies once-daily dosing and sustained bronchodilation |
| [10069510](https://pubmed.ncbi.nlm.nih.gov/10069510/) | 1999 | Review | Life Sciences | Mechanistic profile of tiotropium as a kinetically M3/M1-selective muscarinic antagonist |
| [33095662](https://pubmed.ncbi.nlm.nih.gov/33095662/) | 2021 | Review | Curr Med Res Opin | Review of tiotropium+olodaterol fixed-dose combination for reducing COPD exacerbations per GOLD 2020 |
| [35510163](https://pubmed.ncbi.nlm.nih.gov/35510163/) | 2022 | Cohort | Int J Chron Obstruct Pulmon Dis | Taiwan multicenter real-world cohort comparing tiotropium/olodaterol, umeclidinium/vilanterol, and indacaterol/glycopyrronium in COPD |
| [27724909](https://pubmed.ncbi.nlm.nih.gov/27724909/) | 2016 | Systematic Review | BMC Pulm Med | Systematic review of tiotropium Respimat® vs HandiHaler® comparative studies in COPD |

*20 publications were returned in the source search; the 10 above prioritize RCTs and systematic reviews over case reports and narrative commentary.*

---

## Saudi Arabia Market Information

TIOTROPIUM currently has **no marketing authorization on file** for Saudi Arabia (market status: Not Marketed; total licenses: 0). No product name, dosage form, or approved-indication text is available to tabulate.

---

## Safety Considerations

The structured safety fields for this drug (key warnings, contraindications, drug–drug interactions) are all data gaps — the query for TFDA/package-insert warnings and DDI records returned no results (DG001, flagged **Blocking**: this gap alone is sufficient to prevent a formal S1 safety pre-assessment).

Separately, the literature evidence collected for tiotropium's COPD indication surfaces two safety signals worth carrying forward even though they sit outside the formal `safety` data block:
- **Possible dementia risk**: a 2025 cohort study (PMID 40388132, *JAMA Intern Med*) examined whether LAMA initiation, including tiotropium, is associated with increased dementia risk via central anticholinergic effects.
- **Cardiovascular and mortality signals**: a meta-analysis (PMID 32274526) evaluated tiotropium and adverse cardiovascular events, and an earlier BMJ meta-analysis (PMID 21672999) raised a mortality signal specifically tied to the Respimat mist-inhaler formulation (subsequently the subject of further large-scale safety trials in the literature, not captured in this pack).

> Please refer to the package insert for authoritative safety information; the signals above are literature-derived and not a substitute for formal label review.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The evidence base is extensive (L1, 50 trials/20 publications) and consistent with tiotropium's long-established role as a first-line LAMA bronchodilator — but because "obstructive lung disease" largely restates the existing COPD indication, this should be treated as **evidence consolidation, not novel repurposing**, and weighted accordingly in any repurposing pipeline scoring.
- The Blocking data gap (DG001: no TFDA/package-insert warnings or contraindications on file) means a genuine safety pre-assessment (S1) cannot yet be completed, regardless of the strength of efficacy evidence — this is a hard prerequisite before any Go decision, not merely a guardrail.

**To proceed, the following is needed:**
- Retrieve and parse the official package insert for warnings, contraindications, and precautions (DG001, Blocking)
- Obtain a structured mechanism-of-action record from DrugBank or equivalent (DG002, High)
- Confirm Saudi Arabia registration status/pathway given the current 0-license, not-marketed status
- If repurposing scoring is the goal, re-run ranking with rank-1 excluded or down-weighted as a non-novel signal, and evaluate rank 4 ("COPD, severe early onset", L3/S1/Research Question) as the more genuinely differentiated candidate in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

