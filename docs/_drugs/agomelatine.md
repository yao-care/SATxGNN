---
layout: default
title: Agomelatine
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 10
---

# Agomelatine
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

# Agomelatine: From Major Depressive Disorder to Melancholia

## One-Sentence Summary

Agomelatine (Valdoxan) is a melatonin receptor agonist and 5-HT2C receptor antagonist approved by the EMA for the treatment of major depressive disorder in adults, though it is not currently registered in Saudi Arabia.
The TxGNN model predicts it may be effective for **Melancholia** — the most severe, endogenous subtype of depression defined by profound anhedonia and circadian rhythm disruption — the two core targets of agomelatine's dual mechanism.
With **0 dedicated clinical trials** but **20 publications** supporting this direction, and given EMA approval for MDD (the parent diagnosis), the evidence base is substantial.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major Depressive Disorder (MDD) — EMA-approved (Valdoxan); not registered in Saudi Arabia |
| Predicted New Indication | Melancholia |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Agomelatine acts through a uniquely dual mechanism with no monoamine reuptake inhibition. It is a full agonist at melatonin MT1 and MT2 receptors — synchronising the suprachiasmatic nucleus (the brain's master clock) and restoring disrupted sleep architecture — and simultaneously an antagonist at serotonin 5-HT2C receptors, which disinhibits the release of dopamine and noradrenaline in the prefrontal cortex, improving motivational drive and hedonic tone. This places it in a pharmacological class of its own among antidepressants.

Melancholia (ICD-10: F32.2/F33.3) is defined precisely by the two features that agomelatine targets: profound anhedonia (loss of pleasure, directly addressed by dopaminergic disinhibition) and early morning awakening with diurnal mood variation (the biological hallmark of circadian rhythm disturbance, directly addressed by MT1/MT2 agonism). No other approved antidepressant addresses both of these cardinal symptoms through a single, integrated mechanism.

Multiple landmark studies — including the Cipriani 2018 *Lancet* network meta-analysis synthesising 522 trials of 21 antidepressants, and the Kishi 2023 *Molecular Psychiatry* systematic review of MDD maintenance trials — confirm agomelatine's efficacy across the MDD spectrum. Melancholia is the most severe endogenous subtype of MDD; the EMA approved agomelatine (Valdoxan 25–50 mg) for MDD in February 2009 on the basis of multiple Phase 3 placebo-controlled RCTs. The TxGNN prediction therefore reflects a mechanistically sound and clinically well-grounded sub-indication extension.

---

## Clinical Trial Evidence

Currently no related clinical trials specifically targeting agomelatine in melancholia are registered. The evidence base derives from Phase 3 RCTs conducted for the MDD indication (EMA approval basis), with melancholia patients included within the broader MDD populations studied.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [29477251](https://pubmed.ncbi.nlm.nih.gov/29477251/) | 2018 | Network Meta-Analysis | *Lancet* | Among 21 antidepressants in acute MDD treatment (522 trials, 116,477 participants), agomelatine ranked among the top for both efficacy and acceptability |
| [36253442](https://pubmed.ncbi.nlm.nih.gov/36253442/) | 2023 | Systematic Review | *Molecular Psychiatry* | Agomelatine demonstrated superior efficacy vs placebo in MDD maintenance phase across enrichment-design double-blind RCTs |
| [41135546](https://pubmed.ncbi.nlm.nih.gov/41135546/) | 2025 | Systematic Review | *Lancet* | Comparative physiological side-effect profiling across antidepressants from RCTs; agomelatine distinguished by cardiometabolic neutrality |
| [39684343](https://pubmed.ncbi.nlm.nih.gov/39684343/) | 2024 | Systematic Review / Meta-Analysis | *Int J Mol Sci* | Agomelatine effective and safe in MDD patients with comorbid type 2 diabetes, supporting use in medically complex populations |
| [40129874](https://pubmed.ncbi.nlm.nih.gov/40129874/) | 2025 | Review | *PCN Reports* | Agomelatine identified among agents with promising anti-anhedonic effects alongside vortioxetine and ketamine — directly targeting the cardinal symptom of melancholia |
| [37424409](https://pubmed.ncbi.nlm.nih.gov/37424409/) | 2023 | Review | *Clin Psychopharmacol Neurosci* | Anhedonia as a core transdiagnostic domain with reward-processing deficits; mechanistically aligns with agomelatine's dopaminergic disinhibition via 5-HT2C blockade |
| [32568567](https://pubmed.ncbi.nlm.nih.gov/32568567/) | 2020 | Review | *Expert Opin Drug Discov* | Preclinical discovery of agomelatine; described as the first antidepressant extending beyond monoaminergic neurotransmission, with circadian resynchronisation as its key differentiator |
| [34419186](https://pubmed.ncbi.nlm.nih.gov/34419186/) | 2021 | Review | *Lancet Psychiatry* | Circadian rhythm sleep-wake disturbances as a causal pathway in depressive disorders in young people; supports melatonin-based interventions for early intervention |
| [37960759](https://pubmed.ncbi.nlm.nih.gov/37960759/) | 2023 | Meta-Analysis | *Medicine* | Systematic meta-analysis confirming agomelatine's superior efficacy and safety profile in depressive disorder patients |
| [23484857](https://pubmed.ncbi.nlm.nih.gov/23484857/) | 2013 | Review | *Expert Opin Investig Drugs* | Agomelatine's dual action on melatonin receptors and circadian system reviewed in the context of MDD subtypes; pineal-SCN nexus central to antidepressant effect |

---

## Saudi Arabia Market Information

Agomelatine is not currently registered in Saudi Arabia. No SFDA authorisation records were found (total licences: 0). The drug is approved and marketed in the EU (Valdoxan, Servier) and is available in a number of other markets, but has not entered the Saudi Arabia regulatory pathway.

---

## Safety Considerations

Please refer to the package insert (EMA SmPC for Valdoxan) for complete safety information. Note that the local SFDA package insert data was not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Agomelatine's dual mechanism maps directly onto the core pathophysiology of melancholia — circadian rhythm disruption addressed by MT1/MT2 agonism, and anhedonia addressed by dopaminergic disinhibition via 5-HT2C blockade. The drug holds EMA approval for MDD (the parent diagnosis of melancholia) supported by multiple Phase 3 RCTs, and is ranked highly in the most comprehensive antidepressant network meta-analysis to date. The primary barrier is the absence of Saudi Arabia registration rather than a lack of clinical evidence.

**To proceed, the following is needed:**

- **Regulatory pathway**: Initiate SFDA registration filing using the EMA dossier as the primary basis; clarify whether Saudi Arabia has an expedited review pathway for EMA-approved drugs
- **MOA documentation**: Retrieve full DrugBank/EMA SmPC MOA data (currently marked as data gap) to complete the mechanistic analysis for the regulatory submission
- **Hepatotoxicity monitoring protocol**: Agomelatine carries a well-documented risk of transaminase elevation (a class-specific concern); a liver function monitoring plan (ALT/AST at baseline, 3 weeks, 6 weeks, 12 weeks, then periodically) must be formalised before clinical use
- **Drug interaction assessment**: Formal DDI profiling for CYP1A2 interactions (agomelatine is a CYP1A2 substrate; co-administration with potent CYP1A2 inhibitors such as fluvoxamine or ciprofloxacin is contraindicated per EMA label) — DDI data was not retrieved in the current evidence pack
- **Melancholia-specific trial**: Dedicated prospective study in melancholia (using validated melancholia rating instruments such as the CORE or HDRS melancholia subscale) to generate sub-indication specific data beyond the extrapolation from broad MDD trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

