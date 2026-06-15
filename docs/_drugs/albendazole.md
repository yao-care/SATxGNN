---
layout: default
title: Albendazole
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 3
---

# Albendazole
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

# Albendazole: From Helminth Infections to Alveolar Echinococcosis

## One-Sentence Summary

Albendazole is a broad-spectrum benzimidazole antiparasitic drug with established global efficacy against a wide range of helminth infections, currently not registered in Saudi Arabia.
The TxGNN model predicts it may be effective for **Alveolar Echinococcosis** with a confidence score of 99.97%,
supported by **5 clinical trials** and **20 publications** — including a completed Phase 2 RCT (n=194) directly testing albendazole in early-stage alveolar echinococcosis — making this the highest-priority repurposing candidate in the current dataset.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Helminth infections (broad-spectrum antiparasitic; no Saudi Arabia market authorization on record) |
| Predicted New Indication | Alveolar Echinococcosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Albendazole belongs to the benzimidazole class of anthelmintics. It acts by selectively binding to parasite β-tubulin with high affinity — an interaction far more potent than binding to human tubulin — thereby inhibiting microtubule polymerization. This disrupts the parasite's cytoskeletal integrity and blocks GLUT-mediated glucose uptake, leading to progressive glycogen depletion and energy starvation that ultimately paralyzes and kills the worm. The active metabolite, albendazole sulfoxide, is able to penetrate alveolar echinococcal cyst walls, ensuring therapeutic concentrations reach the *Echinococcus multilocularis* metacestode directly.

Alveolar echinococcosis (AE) is caused by the larval stage of *E. multilocularis*, a tapeworm (class Cestoda) that invades the liver with a pseudotumoral, infiltrative growth pattern. Without treatment, AE is nearly universally fatal within 10–15 years. Because *E. multilocularis* shares the same β-tubulin vulnerability as other cestode species, the mechanistic rationale for albendazole's anti-AE activity is well-founded. Albendazole functions as a **parasitostatic** agent in this context — it halts disease progression and suppresses cyst viability but does not achieve complete parasiticidal eradication — which is why surgical resection combined with long-term albendazole chemotherapy remains the standard of care.

Critically, the WHO has already listed albendazole as the **first-line continuous chemotherapy for inoperable AE** (administered in 28-day on / 14-day off cycles), and this use is endorsed by the WHO Informal Working Group on Echinococcosis (WHO-IWGE) expert consensus guidelines. This is therefore an **established, guideline-supported use** rather than a speculative repurposing hypothesis. However, since albendazole is not currently marketed in Saudi Arabia, accessing this treatment requires a formal import authorization or compassionate-use pathway — making the TxGNN prediction clinically and regulatorily actionable in this market context.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Phase 2 | Completed | 194 | Direct RCT testing albendazole for early-stage AE in an endemic region of Kyrgyzstan (Osh province). Most prior evidence focused on late or inoperable cases; this trial specifically addresses early-stage intervention. Highest-quality direct clinical evidence for this indication to date. |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | N/A | Completed | 50 | Prospective observational cohort (EchinoVISTA) of AE patients on albendazole, evaluating parasite viability markers and imaging-based criteria to guide treatment withdrawal decisions. Supports development of a structured monitoring framework for long-term therapy. |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | N/A | Unknown | 24 | RCT evaluating adjuvant albendazole vs. placebo after pulmonary hydatid cyst (cystic echinococcosis, CE) surgical resection to reduce 6-month recurrence. CE and AE share the same drug mechanism; findings can be indirectly extrapolated to adjuvant AE scenarios. |
| [NCT05824442](https://clinicaltrials.gov/study/NCT05824442) | N/A | Recruiting | 43 | Evaluation of a new multiplex qPCR diagnostic technique for echinococcosis. Not a treatment efficacy trial; albendazole is mentioned as the standard of care backdrop. No direct contribution to albendazole efficacy assessment. |
| [NCT07176598](https://clinicaltrials.gov/study/NCT07176598) | N/A | Completed | 1 | Case report of a rare intramuscular (deltoid) hydatid cyst initially misdiagnosed as a synovial cyst. Lowest-grade evidence; useful only for reference in rare extra-hepatic anatomical presentations. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Expert Consensus Guidelines | *Acta Tropica* | WHO-IWGE consensus on diagnosis and treatment of cystic and alveolar echinococcosis; formally establishes albendazole as the standard of care for inoperable AE with 28-day on/14-day off cycling regimen. Foundational reference for all clinical practice. |
| [39254012](https://pubmed.ncbi.nlm.nih.gov/39254012/) | 2024 | Review | *Tidsskrift for Den Norske Lægeforening* | Contemporary review of AE epidemiology, diagnosis, and management; highlights the pseudotumoral liver presentation, the role of prolonged albendazole therapy, and emerging risk in previously non-endemic regions, relevant to Saudi Arabia import risk assessment. |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Review | *Clinical Microbiology Reviews* | Comprehensive overview of 21st-century advances in echinococcosis including genetics, diagnostics, and treatment. Discusses albendazole bioavailability limitations, resistance concerns, and emerging alternatives. Widely cited benchmark review. |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Review | *World Journal of Gastroenterology* | Current management of hepatic echinococcosis; emphasizes surgery as the cornerstone with albendazole chemotherapy as adjuvant or sole option when surgical cure is not achievable. Affirms continued dependence on albendazole in 2025. |
| [34161992](https://pubmed.ncbi.nlm.nih.gov/34161992/) | 2021 | Review | *Seminars in Liver Disease* | Focused review of hepatic AE: pathophysiology, staging, and treatment outcomes. Reports that the combination of earlier diagnosis, improved surgery, and prolonged albendazole use has transformed the AE prognosis since the 1990s. |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Review | *Parasite (Paris)* | Status review of chemotherapy for AE: identifies that benzimidazoles remain the only recommended class but highlights limitations — parasitostatic only, potential hepatotoxicity with prolonged use, and variable bioavailability. Points to unmet need for parasiticidal options. |
| [39508157](https://pubmed.ncbi.nlm.nih.gov/39508157/) | 2024 | Drug Repurposing Review | *Parasitology* | Identifies pyronaridine (an approved antimalarial) via drug repurposing as a promising candidate to supplement or replace albendazole in hard-to-treat AE. Confirms that albendazole is currently the **exclusive** standard pharmacological treatment, underscoring the therapeutic gap. |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | Pharmacological Study | *Antimicrobial Agents and Chemotherapy* | Develops and evaluates bioavailability-enhancing albendazole formulations (crystalline dispersion, hydrochloride, and hydroxyethyl sulfonate composites) in a hepatic AE rat model. Addresses low oral bioavailability as a key barrier to optimal therapeutic outcomes. |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Review | *Acta Tropica* | Review of novel treatment options for CE and AE; confirms that no licensed non-surgical alternative to albendazole or mebendazole currently exists, reinforcing the continued clinical necessity of albendazole access. |
| [36974024](https://pubmed.ncbi.nlm.nih.gov/36974024/) | 2022 | Review | *Chinese Journal of Schistosomiasis Control* | Progress summary of albendazole use for AE treatment; documents the parasitostatic mechanism, long-term treatment outcomes, and emerging research on improved dosing strategies and potential combination therapies to overcome treatment failure in >20% of patients. |

---

## Saudi Arabia Market Information

Albendazole currently has **no registered authorizations with the Saudi Food and Drug Authority (SFDA)**. There are no licensed products available on the Saudi market. Patients in Saudi Arabia who require albendazole therapy for alveolar echinococcosis must access the drug through one of the following pathways:

- **Compassionate use / named-patient import** from a country where the drug is registered (e.g., United Kingdom, France, United States)
- **Unlicensed import authorization** via SFDA Special Access Scheme
- **Procurement through international humanitarian/WHO channels** (albendazole is on the WHO Essential Medicines List)

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Notice:** Formal safety data including specific warnings, contraindications, and drug interaction profiles were not available in the current dataset. Albendazole has an established global safety profile and is a WHO Essential Medicine; however, prolonged high-dose use (as required for AE) carries hepatotoxicity risk. Clinicians should consult the manufacturer's current prescribing information, WHO treatment guidelines, and the WHO-IWGE expert consensus before initiating therapy. Baseline and periodic liver function monitoring is standard practice in AE treatment protocols.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 RCT (NCT07182305, n=194) directly testing albendazole in early-stage alveolar echinococcosis, combined with WHO designation as first-line therapy for inoperable AE, robust mechanistic evidence (selective β-tubulin binding → parasite energy depletion), and broad international guideline support, constitutes L2-level evidence sufficient to support use. The primary barrier in Saudi Arabia is not efficacy or safety uncertainty — both are well-characterized globally — but rather **regulatory access**, since the drug is not currently marketed in the Kingdom.

**To proceed, the following is needed:**

- **Regulatory pathway**: Initiate SFDA special access or compassionate use application; identify a registered-country supplier for importation
- **Safety data package**: Obtain the current manufacturer's package insert to formally document warnings, contraindications, and drug-drug interactions (particularly with CYP enzyme inducers/inhibitors that affect albendazole sulfoxide plasma levels)
- **Long-term monitoring plan**: Establish a protocol for liver function tests (ALT/AST, total bilirubin), CBC (including differential), and renal function at baseline and at regular intervals throughout extended therapy — AE typically requires months to years of continuous treatment
- **Multidisciplinary team**: Engage hepatology, infectious disease, and/or parasitology specialists for staging, treatment decision-making, and surgical consultation (R0 resection with adjuvant albendazole offers the best outcome when feasible)
- **Imaging infrastructure**: Confirm access to MRI/CT (and ideally PET-CT) for baseline staging and treatment response assessment per WHO-IWGE criteria (PNM staging system)
- **Patient counseling**: Inform patients that albendazole is parasitostatic — not parasiticidal — in AE; indefinite or lifelong therapy may be required in inoperable cases
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

