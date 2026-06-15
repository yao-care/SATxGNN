---
layout: default
title: Aminophylline
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 10
---

# Aminophylline
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

# Aminophylline: From Bronchospasm to Migraine Disorder

## One-Sentence Summary

Aminophylline is a methylxanthine derivative and adenosine receptor antagonist, historically established as a bronchodilator for asthma, COPD, and apnea of prematurity.
The TxGNN model predicts it may be effective for **Migraine Disorder**, with **0 clinical trials** and **6 publications** currently supporting this direction.
Evidence remains at the mechanistic and review level (L4), qualifying this as an emerging research hypothesis rather than a clinically validated indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No authorization data available; established pharmacological use as bronchodilator (asthma, COPD, apnea of prematurity) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on established pharmacology, aminophylline is a soluble salt of theophylline and ethylenediamine. Its primary actions are non-selective phosphodiesterase (PDE) inhibition — which elevates intracellular cAMP — and competitive antagonism at adenosine receptors (A1, A2A, A2B). It is this adenosine receptor antagonism that forms the mechanistic backbone of the migraine prediction.

Adenosine, particularly via A2A receptor activation, is known to cause selective intracranial vasodilation and sensitize trigeminal nociceptive fibers — two cardinal features of migraine pathophysiology. A 2023 clinical review (PMID 38059379) proposes that migraine may be partly driven by impaired brain energy metabolism in a context of pathologically elevated adenosine, and documents observational evidence of strong analgesic relief with aminophylline, including in post-dural puncture headache. An in vitro study (PMID 219563) further demonstrated that adenosine and adenine compounds markedly dilate feline and human pial arteries but not extracranial vessels, pointing to a selective intracranial vascular role.

Perhaps the most compelling evidence comes from reverse pharmacology: regadenoson, a selective A2A adenosine receptor agonist used during cardiac stress imaging, was shown to trigger a hemiplegic migraine episode (PMID 34308528) — and aminophylline is routinely used to reverse regadenoson's effects. If A2A agonism provokes migraine, then A2A antagonism by aminophylline may attenuate it. This indirect logic is mechanistically coherent, though not yet tested in a prospective migraine trial.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for aminophylline in migraine disorder.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38059379](https://pubmed.ncbi.nlm.nih.gov/38059379/) | 2023 | Review / Clinical Analysis | Pain Management | Proposes adenosine excess and impaired brain energy metabolism as migraine drivers; documents observational evidence that aminophylline provides strong therapeutic relief in pain and post-dural puncture headache — a closely related adenosine-mediated headache syndrome |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Case Report | Journal of Nuclear Cardiology | Hemiplegic migraine episode triggered by regadenoson (selective A2A agonist) during myocardial perfusion imaging; aminophylline used as reversal agent — provides reverse-pharmacology support for A2A antagonism as a migraine intervention strategy |
| [219563](https://pubmed.ncbi.nlm.nih.gov/219563/) | 1979 | In Vitro / Mechanistic | Stroke | Adenosine and adenine compounds markedly dilate feline and human pial arteries in vitro, with effect absent in extracranial vessels; supports adenosine's selective intracranial vascular role and the potential anti-vasodilatory effect of adenosine antagonists in migraine |
| [7728647](https://pubmed.ncbi.nlm.nih.gov/7728647/) | 1995 | Case Report | Canadian Journal of Cardiology | Patient with Syndrome X presenting adenosine-mediated cardiac pain ("myocardial migraine") triggered by dipyridamole; supports the broader concept that adenosine signaling drives episodic nociceptive events reversible by methylxanthines |
| [14168418](https://pubmed.ncbi.nlm.nih.gov/14168418/) | 1964 | Historical Review | Aggiornamenti Clinicoterapeutici | Historical Italian review of medical headache treatment including xanthine derivatives; provides early conceptual background for xanthine use in headache |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Drug interaction data was not found in the DDI database for aminophylline, and key warnings/contraindications were not retrievable in this evidence pack. Given that theophylline (the active moiety of aminophylline) has a **narrow therapeutic index**, serum level monitoring is standard practice. This is a clinically important safety consideration for any new indication development.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The adenosine receptor antagonism hypothesis linking aminophylline to migraine relief is biologically coherent and supported by one recent clinical review alongside compelling reverse-pharmacology case evidence — but the complete absence of registered clinical trials and reliance on L4 (mechanistic/review-level) evidence prevents recommendation for clinical deployment at this stage.

**To proceed, the following is needed:**

- **Clinical trial initiation**: A proof-of-concept Phase 1/2 study evaluating aminophylline in acute migraine treatment (IV or oral formulation), particularly in post-dural puncture headache as a bridging model
- **MOA documentation**: Formal retrieval of DrugBank pharmacology data (adenosine receptor binding affinities, PDE isoform selectivity) to strengthen mechanistic dossier
- **Safety package**: Retrieval of package insert warnings, contraindications, and key drug interactions — especially with triptans, ergotamines, NSAIDs, and other common migraine medications
- **Therapeutic index assessment**: Theophylline serum monitoring requirements must be evaluated for feasibility in a migraine outpatient setting, where narrow therapeutic windows may be a practical barrier
- **Formulation strategy**: Determine whether an oral sustained-release or IV route is appropriate for migraine (acute vs. prophylactic use case) given the pharmacokinetic profile of theophylline
- **Saudi Arabia regulatory pathway**: As aminophylline is currently not marketed in Saudi Arabia, a full new drug registration or compassionate use pathway would be required before any clinical program can proceed locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

