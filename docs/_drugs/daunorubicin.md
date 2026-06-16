---
layout: default
title: Daunorubicin
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
---

# Daunorubicin
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

# Daunorubicin: From Acute Leukemia to Hodgkin's Lymphoma

## One-Sentence Summary

Daunorubicin is a first-generation anthracycline antibiotic primarily used in the treatment of acute myeloid leukemia (AML) and acute lymphoblastic leukemia (ALL).
The TxGNN model predicts it may be effective for **Hodgkin's Lymphoma**, with **multiple Phase 2/3 trials** demonstrating strong efficacy of the mechanistically analogous doxorubicin in ABVD-based regimens, and **1 early-phase clinical study directly evaluating liposomal daunorubicin** in relapsed/refractory lymphoma (PMID 9387047) providing proof-of-concept.
Overall evidence is rated **L3**, reflecting the gap between the well-established doxorubicin evidence base and the limited direct daunorubicin clinical data in Hodgkin's Lymphoma.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute leukemia (AML/ALL) — detailed regulatory data not available in this evidence pack |
| Predicted New Indication | Hodgkin's Lymphoma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, daunorubicin is a first-generation anthracycline antibiotic that acts as a **DNA intercalating agent and topoisomerase II inhibitor** — the same core mechanism shared by doxorubicin, the "A" component of ABVD (doxorubicin, bleomycin, vinblastine, dacarbazine), which has been the global standard of care for Hodgkin's Lymphoma for decades. Both agents generate cytotoxic double-strand DNA breaks by stabilizing the topoisomerase II cleavage complex, triggering apoptosis preferentially in rapidly proliferating tumour cells.

The biological rationale linking daunorubicin to Hodgkin's Lymphoma is mechanistically sound. Reed-Sternberg cells — the malignant hallmark of classical HL and derived from germinal centre B cells — are known to overexpress topoisomerase IIα, rendering them intrinsically sensitive to the anthracycline drug class. The success of doxorubicin across multiple Phase 3 HL trials (including NCT00005584, n=1,649 and NCT00041210, n=850) therefore constitutes strong indirect evidence for daunorubicin's potential activity. While doxorubicin exhibits modestly superior tissue penetration in solid tumours compared to daunorubicin, liposomal formulations (DaunoXome) can partially compensate for this pharmacokinetic difference.

Critically, a direct early-phase clinical signal already exists: a 1997 study (PMID 9387047) evaluating liposomal daunorubicin at 120 mg/m² in 9 patients with relapsed or refractory lymphoma reported 1 complete response and 2 partial responses, with no patient showing clinically significant cardiac function deterioration. This proof-of-concept data, combined with the overwhelming mechanistic analogy to established doxorubicin-containing regimens across dozens of HL trials, provides a credible scientific foundation for further clinical investigation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00005584](https://clinicaltrials.gov/study/NCT00005584) | Phase 3 | Active, Not Recruiting | 1,649 | Large multinational HL trial comparing ABVD-based regimens with or without additional agents across clinical Stages I–II; provides the highest-quality efficacy benchmarks for anthracycline-containing chemotherapy in HL |
| [NCT00041210](https://clinicaltrials.gov/study/NCT00041210) | Phase 3 | Unknown | 850 | Head-to-head Stanford V vs. ABVD in advanced Hodgkin's Disease; directly benchmarks doxorubicin-based regimens, providing the strongest mechanistic analogy evidence for daunorubicin class |
| [NCT00025259](https://clinicaltrials.gov/study/NCT00025259) | Phase 3 | Completed | 1,734 | Pediatric intermediate-risk HL: response-based, dose-intensive chemotherapy ± radiation; establishes doxorubicin-containing regimen efficacy and late-effects data in a younger population |
| [NCT00002462](https://clinicaltrials.gov/study/NCT00002462) | Phase 3 | Active, Not Recruiting | 615 | MOPP/ABV hybrid chemotherapy ± adjuvant involved-field RT for Stage III/IV HL; long-term OS and PFS data with anthracycline-based consolidation |
| [NCT02797717](https://clinicaltrials.gov/study/NCT02797717) | RCT | Recruiting | 2,200 | International multicenter trial for classical HL in children and adolescents; investigates chemotherapy intensification while reducing RT — the largest ongoing paediatric HL platform trial |
| [NCT01569204](https://clinicaltrials.gov/study/NCT01569204) | Phase 2 | Completed | 100 | BEACOPP variants (containing epirubicin, an anthracycline analogue) in newly diagnosed advanced classical HL; complete response rate and final remission assessed after 6 cycles |
| [NCT00002987](https://clinicaltrials.gov/study/NCT00002987) | Phase 3 | Unknown | 400 | VAPEC-B plus involved-field RT vs. mantle RT alone for early supradiaphragmatic HL; established combined chemoradiotherapy role in early-stage disease |
| [NCT03331341](https://clinicaltrials.gov/study/NCT03331341) | Phase 1/2 | Completed | 50 | APVD (doxorubicin + pembrolizumab + vinblastine + dacarbazine) for untreated classical HL; demonstrates how doxorubicin backbones integrate with anti-PD-1 immunotherapy |
| [NCT03407144](https://clinicaltrials.gov/study/NCT03407144) | Phase 2 | Active, Not Recruiting | 340 | Pembrolizumab combined with chemotherapy for paediatric and young adult cHL slow early responders; explores immunotherapy addition to anthracycline-based frontline regimens |
| [NCT02191930](https://clinicaltrials.gov/study/NCT02191930) | Phase 2 | Completed | 70 | Brentuximab vedotin or B-CAP (bleomycin, cyclophosphamide, doxorubicin, prednisone) in older patients with newly diagnosed classical HL; evaluates objective response rate and PFS at 3 years in an age group where toxicity management is critical |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9387047](https://pubmed.ncbi.nlm.nih.gov/9387047/) | 1997 | Phase 1 / Early Phase | Investigational New Drugs | **Direct daunorubicin evidence**: Liposomal daunorubicin (DaunoXome) at 120 mg/m² q21d in 9 patients with relapsed/refractory lymphoma achieved 1 CR + 2 PR; no clinically significant cardiac deterioration — key proof-of-concept for daunorubicin in lymphoma |
| [39413375](https://pubmed.ncbi.nlm.nih.gov/39413375/) | 2024 | RCT (Phase 3) | New England Journal of Medicine | Nivolumab + AVD vs. BV + AVD in advanced-stage classical HL; demonstrates durability of doxorubicin-backbone regimens augmented by immunotherapy, defines current standard-of-care benchmark |
| [35830649](https://pubmed.ncbi.nlm.nih.gov/35830649/) | 2022 | RCT (Phase 3) | New England Journal of Medicine | 5-year OS follow-up: A+AVD (brentuximab vedotin + doxorubicin + vinblastine + dacarbazine) shows sustained PFS benefit over ABVD and a potential overall survival advantage in Stage III/IV cHL |
| [378369](https://pubmed.ncbi.nlm.nih.gov/378369/) | 1979 | Historical Review | Cancer Treatment Reports | Seminal head-to-head analysis of daunorubicin and doxorubicin (adriamycin) in cancer treatment; formally documents their mechanistic equivalence and specific clinical roles across tumour types |
| [36271128](https://pubmed.ncbi.nlm.nih.gov/36271128/) | 2022 | Observational | Scientific Reports | Interim FDG-PET/CT predictive value in 245 consecutive HL patients on ABVD; iPET2 negativity after 2 cycles strongly predicts long-term PFS and OS — relevant for response-adapted strategies |
| [28365830](https://pubmed.ncbi.nlm.nih.gov/28365830/) | 2017 | Review | Current Oncology Reports | Optimal therapy for early-stage HL: risk-adapted and response-adapted strategies; reviews role of anthracycline-based chemotherapy and evolving RT indications |
| [22147803](https://pubmed.ncbi.nlm.nih.gov/22147803/) | 2012 | Registry / Cohort | Japanese Journal of Clinical Oncology | JCOG Lymphoma Study Group: 30+ trials including 10 randomised trials in aggressive NHL and HL spanning 30 years; provides multi-decade anthracycline efficacy and safety dataset |
| [14584273](https://pubmed.ncbi.nlm.nih.gov/14584273/) | 2003 | Review | Cancer & Chemotherapy | Documents daunorubicin + cytarabine as the foundation of AML cure and ABVD as first-line HL standard; explicitly links both drugs within the anthracycline class context |
| [12736231](https://pubmed.ncbi.nlm.nih.gov/12736231/) | 2003 | Review | Annals of Oncology | IEV (ifosfamide, epirubicin, etoposide) salvage in NHL and Hodgkin's Disease — Italian experience; supports anthracycline class activity at relapse |
| [6085157](https://pubmed.ncbi.nlm.nih.gov/6085157/) | 1984 | Review | Pediatric Surgery | Paediatric HL outcomes over two decades: 5/10/15-year actuarial survival of 90%/80%/70%; establishes the long-term efficacy benchmark for combination chemotherapy regimens in HL |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Anthracycline class (DNA intercalator / Topoisomerase II inhibitor) |
| Myelosuppression Risk | **High** — Dose-dependent severe myelosuppression is expected; neutropenia nadir typically at days 10–14 post-infusion; thrombocytopenia and anaemia are common; febrile neutropenia risk is clinically significant |
| Emetogenicity Classification | Moderate to High |
| Monitoring Items | Complete blood count with differential (CBC-D) at each cycle and nadir; left ventricular ejection fraction (LVEF) by echocardiogram or MUGA scan at baseline, at cumulative dose thresholds (~400 mg/m² daunorubicin equivalent), and at end of treatment; liver function tests (AST/ALT/bilirubin); renal function (creatinine, eGFR) |
| Handling Protection | Must follow cytotoxic drug handling regulations — dedicated laminar-flow preparation area, double-glove technique, disposable gown and respiratory protection, and closed-system drug transfer devices (CSTDs) required for preparation and administration |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Daunorubicin shares the topoisomerase II inhibition mechanism with doxorubicin, the backbone of ABVD — the established gold standard for Hodgkin's Lymphoma supported by decades of Phase 3 evidence. A direct early-phase clinical signal in relapsed/refractory lymphoma (PMID 9387047) confirms the drug class is active, and the TxGNN prediction score of 99.81% reflects strong network-level biological support. However, daunorubicin has not been evaluated head-to-head against doxorubicin in an HL-specific randomised trial, and the drug currently holds no Saudi Arabia marketing authorization.

**To proceed, the following is needed:**
- A prospective Phase 1/2 study of daunorubicin (preferably liposomal formulation) specifically in Hodgkin's Lymphoma patients, with a pharmacokinetic sub-study comparing tissue exposure vs. liposomal doxorubicin
- Formal retrieval and review of DrugBank MOA and SFDA/SFDA-equivalent package insert to document key warnings, contraindications, and cumulative cardiac dose thresholds (data gaps DG001 and DG002 must be resolved before clinical development can proceed)
- A comprehensive cardiac safety monitoring protocol specifying baseline LVEF requirements, cycle-by-cycle monitoring intervals, and stopping rules for cumulative anthracycline exposure
- Drug-drug interaction profile assessment, particularly with bleomycin and other agents typically co-administered in HL regimens
- Saudi Arabia regulatory pathway evaluation for importation, compassionate use, or clinical trial import authorization, given zero current market approvals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

