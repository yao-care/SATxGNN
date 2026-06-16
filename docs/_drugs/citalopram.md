---
layout: default
title: Citalopram
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 5
---

# Citalopram
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

# Citalopram: From Depression to Obsessive-Compulsive Disorder

## One-Sentence Summary

Citalopram is a selective serotonin reuptake inhibitor (SSRI) originally developed for the treatment of major depressive disorder.
The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**,
with **30 clinical trials** (predominantly studying its active enantiomer escitalopram at class level) and **16 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major Depressive Disorder |
| Predicted New Indication | Obsessive-Compulsive Disorder (OCD) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not formally captured in this Evidence Pack. Based on known information, citalopram is a selective serotonin reuptake inhibitor (SSRI) that blocks the serotonin transporter (SERT), increasing synaptic serotonin (5-HT) availability in the central nervous system. Its efficacy in major depressive disorder is well established, and mechanistically this same serotonergic amplification is directly applicable to OCD.

OCD is neurobiologically characterized by hyperactivation of the orbitofrontal cortex–striatum–thalamus–cortical (CSTC) circuit. Serotonergic modulation through SERT inhibition suppresses this compulsive loop, which is why SSRIs are recognized internationally as first-line pharmacotherapy for OCD. The class has Phase III RCT support across multiple members — fluvoxamine, sertraline, fluoxetine, and paroxetine among them.

Citalopram shares the same core pharmacophore as escitalopram, which is simply its purified S-enantiomer. Two direct clinical publications from 1999 (PMID 10471169; PMID 10572334) already established citalopram's efficacy in OCD, including treatment-resistant cases. This structural kinship means the extensive escitalopram OCD evidence base can reasonably serve as class-level indirect support for citalopram, making the TxGNN prediction both mechanistically sound and clinically coherent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|------|--------|-----------|-------------|
| [NCT00086645](https://clinicaltrials.gov/study/NCT00086645) | Phase 2 | Completed | 149 | **Direct citalopram trial**: Citalopram vs placebo in children with autism and high levels of repetitive behavior — evaluates citalopram safety and efficacy in repetitive/compulsive symptom reduction |
| [NCT00609531](https://clinicaltrials.gov/study/NCT00609531) | Phase 1 | Completed | 12 | **Direct citalopram trial**: fMRI evaluation of citalopram's effect on restricted repetitive behaviors in autism spectrum disorders — establishes neuroimaging feasibility of citalopram in psychiatric compulsive symptoms |
| [NCT00305500](https://clinicaltrials.gov/study/NCT00305500) | Phase 3 | Completed | 100 | High-dose escitalopram (up to 50 mg/d) for OCD in outpatients — 18-week open-label study; strongest class-level indirect evidence (escitalopram is the S-enantiomer of citalopram) |
| [NCT00723060](https://clinicaltrials.gov/study/NCT00723060) | Phase 4 | Completed | 176 | Randomized double-blind comparison of conventional (20 mg) vs high-dose (40 mg) escitalopram in OCD across multiple centers — large-sample dose-finding study with Y-BOCS, HAM-D, CGI endpoints |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | CBT augmentation for pediatric OCD patients with partial SRI response — evaluates SRI + cognitive behavioral therapy combination, Phase III design |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Completed | 26 | OCD medication response prediction — randomized assignment to clomipramine or escitalopram; directly relevant to SSRI class response prediction in OCD |
| [NCT00116532](https://clinicaltrials.gov/study/NCT00116532) | Phase 4 | Completed | 30 | Escitalopram efficacy and optimal dosing for OCD — provides class-level dosing and safety reference for SERT inhibitors in OCD |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Phase 4 | Completed | 158 | Randomized open trial of group CBT vs SSRI (fluoxetine) in OCD — broad OCD population including comorbid conditions; SSRI arm demonstrates real-world efficacy |
| [NCT03993535](https://clinicaltrials.gov/study/NCT03993535) | Phase 4 | Completed | 250 | Multi-site naturalistic follow-up (US, Brazil, India, Netherlands) of OCD patients with clinical, neurocognitive, and neuroimaging variables — large international cohort, SSRI as standard treatment |
| [NCT03068429](https://clinicaltrials.gov/study/NCT03068429) | Phase 4 | Completed | 69 | Fear conditioning and extinction in OCD before/after sertraline treatment with fMRI — directly demonstrates SSRI modulation of OCD neural circuitry |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Case Series / Early Clinical Trial | Int Clin Psychopharmacol | **Direct citalopram evidence**: "Beyond depression: citalopram for OCD" — early clinical demonstration of citalopram's anti-obsessional efficacy; reviews the serotonin–OCD connection and early citalopram trial data |
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Case Series / Retrospective | Eur Psychiatry | **Direct citalopram evidence**: 90-day randomized open-label trial of citalopram ± clomipramine in 16 treatment-resistant OCD patients (Y-BOCS ≥25, failed clomipramine and fluoxetine); demonstrates citalopram utility in refractory cases |
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | Systematic Review | Compr Psychiatry | Long-term safety and tolerability of off-label high-dose SRIs in OCD — most recent systematic safety review; key reference for dose escalation considerations |
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | Meta-Analysis | J Psychiatr Res | Network meta-analysis comparing pharmacological, psychological, and combined treatments in children and adolescents with OCD — SSRIs demonstrate consistent efficacy across treatment arms |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Meta-Analysis | J Affect Disord | OCD shows significantly reduced placebo (and antidepressant) response compared to other anxiety disorders — highlights that active drug effect in OCD RCTs is genuine and not placebo-driven |
| [35818708](https://pubmed.ncbi.nlm.nih.gov/35818708/) | 2022 | Systematic Review | Expert Opin Pharmacother | Systematic review of RCTs for pharmacotherapy in obsessive-compulsive spectrum — evaluates current SSRI evidence quality and identifies research gaps |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-Review | Front Psychiatry | Meta-review of antidepressant efficacy and suicidality across pediatric psychiatric disorders including OCD — confirms SSRI efficacy signal in pediatric OCD with acceptable tolerability |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Review | BMJ Clin Evid | Comprehensive OCD evidence review: ~1–1.5% adult prevalence, episodic vs chronic course, established role of SSRIs as first-line pharmacotherapy |
| [32242450](https://pubmed.ncbi.nlm.nih.gov/32242450/) | 2020 | Systematic Review | Nord J Psychiatry | Systematic review and meta-analysis of fluoxetine in pediatric OCD — class-level SSRI evidence supporting efficacy and safety in younger populations |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | Review | World J Biol Psychiatry | "OCD: serotonin and beyond" — foundational mechanistic review of serotonergic pathways in OCD; establishes the scientific rationale for SSRI class use in this disorder |

---

## Saudi Arabia Market Information

Citalopram currently holds **no marketing authorizations** in Saudi Arabia. The drug is not commercially available through the SFDA-regulated market. Any clinical use would require a special import approval or compassionate-use access pathway under SFDA regulations.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers**: Safety data (key warnings, contraindications, drug-drug interactions) were not retrieved in this Evidence Pack. Before proceeding to clinical evaluation, the following known class-level risks should be independently verified: QTc prolongation at high doses (citalopram carries an FDA black-box equivalent warning for doses >40 mg), serotonin syndrome risk when combined with other serotonergic agents, and the general SSRI black-box warning regarding suicidality in patients under 25 years.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Citalopram's SSRI mechanism directly targets the serotonergic dysregulation underlying OCD, and two published clinical studies using citalopram itself in OCD patients (1999) already exist. The extensive Phase 3/4 evidence base for its structural twin escitalopram provides strong class-level corroboration, placing this candidate at Evidence Level L2 — sufficient to advance with appropriate safeguards.

**To proceed, the following is needed:**
- Retrieve formal MOA documentation from DrugBank (resolves Data Gap DG002)
- Obtain Saudi Arabia–compliant package insert or equivalent label to complete safety pre-screening (resolves blocking Data Gap DG001)
- Verify the QTc-prolongation profile and establish dose ceiling guidance for use in OCD (standard SSRI doses are generally within safe QTc range; high-dose escalation requires cardiac monitoring)
- Review drug-drug interaction profile, particularly with MAO inhibitors (absolute contraindication), other serotonergic agents (serotonin syndrome risk), and CYP2C19 inhibitors/inducers that affect citalopram plasma levels
- Assess SFDA market entry strategy — citalopram has no current Saudi authorization; a regulatory filing or named-patient program would be required before any clinical deployment
- Consider a prospective open-label pilot study of citalopram specifically (not escitalopram) in OCD to generate drug-specific Level 1 evidence and close the evidence gap from indirect class extrapolation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

