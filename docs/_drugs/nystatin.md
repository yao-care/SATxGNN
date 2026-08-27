---
layout: default
title: Nystatin
parent: 僅模型預測 (L5)
nav_order: 452
evidence_level: L5
indication_count: 10
---

# Nystatin
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

# Nystatin: From Fungal Infections (Candidiasis) to Vulvovaginitis

## One-Sentence Summary

Nystatin is a polyene antifungal antibiotic historically used to treat *Candida* infections; Taiwan-specific approved-indication text is not currently on file, and the drug holds **no marketing authorization in Taiwan** (0 licenses, market status: not marketed). The TxGNN model predicts it may be effective for **Vulvovaginitis**, with **no registered clinical trials** but **20 supporting publications** currently available, giving a moderate (L3) evidence base built on observational and review-level data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal infections (Candidiasis) — no Taiwan-specific approved-indication text on file (drug not marketed) |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed drug-level mechanism-of-action data (DrugBank `original_moa`) is currently a data gap (flagged as High severity in this Evidence Pack, remediation pending via DrugBank API query). However, the evidence pack's repurposing rationale supplies pharmacologically grounded reasoning: Nystatin is a polyene-class antifungal that binds ergosterol in the fungal cell membrane, forming pores that cause cell death, giving it direct fungicidal/fungistatic activity against *Candida* species.

Vulvovaginitis is frequently caused by *Candida albicans* (vulvovaginal candidiasis accounts for an estimated 85–90% of *Candida*-related vaginitis per the literature below), which is mechanistically identical to the target organism Nystatin was originally developed against. Nystatin has, in fact, been used topically (vaginal tablets/creams) for decades as a first- or second-line agent for vulvovaginal candidiasis before azoles became dominant — this is corroborated by multiple historical and recent reviews in the literature table below (e.g., PMID 1436934, PMID 39771534).

Because the causative pathogen (Candida) and the drug's mechanism (membrane disruption via ergosterol binding) map directly onto this indication, the TxGNN prediction is biologically plausible and is further supported by a substantial, if largely observational/review-level, published literature base — rather than being a purely graph-distance-driven prediction (contrast with several other ranked predictions in this pack, e.g., "disease of orbital region," which have no mechanistic or evidentiary support).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | Reviews current management of fluconazole-resistant vulvovaginal candidiasis (FRVVC); identifies nystatin, boric acid, oteseconazole, and ibrexafungerp as alternative antifungal options for resistant cases |
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Cohort | Mycoses | 287 *Candida* isolates from 283 patients with complicated VVC tested for fluconazole and nystatin susceptibility; correlated in vitro susceptibility with clinical treatment outcome |
| [16047929](https://pubmed.ncbi.nlm.nih.gov/16047929/) | 2005 | Cohort | Ceska gynekologie | Evaluated combined/miscellaneous vulvovaginal infections and their treatment with vaginal nystatin + nifuratel combination products |
| [30359236](https://pubmed.ncbi.nlm.nih.gov/30359236/) | 2018 | Preclinical (rat model) | BMC Microbiology | Nystatin enhanced mucosal immune response against *C. albicans* and protected vaginal epithelial ultrastructure in a rat VVC model |
| [1436934](https://pubmed.ncbi.nlm.nih.gov/1436934/) | 1992 | Review | Obstetrics and Gynecology Clinics of North America | Reviews topical antifungal agents; notes nystatin was the original 1950s treatment for VVC before being surpassed by imidazoles/triazoles |
| [37023426](https://pubmed.ncbi.nlm.nih.gov/37023426/) | 2023 | Comparative in vitro study | J Infection in Developing Countries | Compared inhibition zones of tea tree oil (5%, 10%) vs. nystatin against vaginal *Candida* isolates from pregnant women |
| [32104010](https://pubmed.ncbi.nlm.nih.gov/32104010/) | 2020 | Laboratory study | Infection and Drug Resistance | Compared antifungal activity of ZnO nanoparticles and nystatin, and their effect on virulence gene (SAP1-3) expression in fluconazole-resistant *C. albicans* from VVC |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | Journal of Women's Health | Reviews boric acid for recurrent VVC in the context of rising azole resistance, positioning nystatin among alternative therapies |
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Review | BMJ Clinical Evidence | Overview of vulvovaginal candidiasis; *C. albicans* accounts for 85–90% of cases, establishing the fungal pathophysiology nystatin targets |
| [12228137](https://pubmed.ncbi.nlm.nih.gov/12228137/) | 2002 | Review | BMJ | General clinical review of vulvovaginal candidiasis diagnosis and management |

---

## Taiwan Market Information

Nystatin currently has no marketing authorization on file in Taiwan (0 licenses; market status: not marketed). No product/authorization data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: this Evidence Pack flags TFDA package-insert warnings/contraindications as a Blocking data gap (DG001) — this must be resolved before any Stage 1 safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong (direct antifungal activity against the likely causative organism) and is backed by 20 publications, including a sizeable susceptibility/outcome cohort (n=283) and an animal mechanistic study — sufficient to warrant continued interest (L3, evidence level). However, there are no registered clinical trials testing nystatin specifically for vulvovaginitis, and the drug currently has no marketing authorization in Taiwan, so guardrails (formulation/route confirmation, safety data completion) are required before advancing further.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001: obtain TFDA/manufacturer package-insert warnings and contraindications
- Resolve High-severity data gap DG002: confirm detailed mechanism of action via DrugBank API
- Confirm route/formulation availability (vaginal tablet/cream) since the drug is not currently marketed in Taiwan
- Consider a prospective RCT comparing vaginal nystatin against azole therapy specifically for vulvovaginitis/VVC to upgrade the evidence level beyond L3
- Complete drug-interaction (DDI) query, currently returning "not found"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

