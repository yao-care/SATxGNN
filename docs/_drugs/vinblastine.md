---
layout: default
title: Vinblastine
parent: 僅模型預測 (L5)
nav_order: 664
evidence_level: L5
indication_count: 10
---

# Vinblastine
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

# Vinblastine: From Cytotoxic Chemotherapy (Vinca Alkaloid) to Rhabdomyosarcoma

## One-Sentence Summary

> Vinblastine is a classic vinca-alkaloid cytotoxic chemotherapy agent; this evidence pack does not contain its documented original indication or formal MOA text.
> The TxGNN model predicts it may be effective for **Rhabdomyosarcoma**,
> with **no dedicated clinical trials** but **15 supporting publications** — mostly same-class (vinorelbine) and case-report level evidence — currently available.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this evidence pack (no `taiwan_regulatory.licenses` entries); vinblastine is generally documented as a cytotoxic vinca-alkaloid antineoplastic agent |
| Predicted New Indication | Rhabdomyosarcoma |
| TxGNN Prediction Score | 99.86% (rank #2967) |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on the literature retrieved in this evidence pack, vinblastine is a **vinca alkaloid microtubule/tubulin polymerization inhibitor** that arrests cells in mitosis (PMID 3329524, 6744266) — the same mechanistic class as vincristine and vinorelbine.

Rhabdomyosarcoma is a highly proliferative sarcoma of skeletal-muscle origin. The related vinca alkaloid **vincristine** is a backbone component of the current standard VAC/VAI chemotherapy regimens, and the closely related agent **vinorelbine** has demonstrated Phase 2 activity in relapsed/refractory pediatric rhabdomyosarcoma (PMID 22633624, 15378498, 12115359). Vinblastine itself appears as a combination-chemotherapy component in case reports of refractory prostatic rhabdomyosarcoma (PMID 2451411).

Mechanistically, this supports plausibility, but there is **no dedicated controlled trial of vinblastine itself** in rhabdomyosarcoma — the supporting evidence is largely indirect (same-class drug) or case-report level.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for rhabdomyosarcoma specifically (`clinical_trials: []`, `ictrp_trials: []`).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Phase 2 trial (vinorelbine, same-class evidence) | European Journal of Cancer | Vinorelbine + low-dose cyclophosphamide in relapsed/refractory pediatric solid tumors; good tolerance and efficacy signal specifically noted in rhabdomyosarcoma |
| [15378498](https://pubmed.ncbi.nlm.nih.gov/15378498/) | 2004 | Cohort/Pilot (vinorelbine, same-class evidence) | Cancer | Dose-finding pilot of vinorelbine + low-dose oral cyclophosphamide in pediatric sarcomas, informing the upcoming European Rhabdomyosarcoma Protocol |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Cohort (vinorelbine, same-class evidence) | Cancer | Vinorelbine showed activity in previously treated advanced childhood rhabdomyosarcoma |
| [38050209](https://pubmed.ncbi.nlm.nih.gov/38050209/) | 2023 | Case report (direct vinblastine use) | Medicine | Adult perianal rhabdomyosarcoma achieved partial response after nivolumab + dacarbazine + cisplatin + **vinblastine** (3 cycles), followed by surgical resection |
| [2451411](https://pubmed.ncbi.nlm.nih.gov/2451411/) | 1987 | Case report (direct vinblastine use) | Hinyokika Kiyo (Acta Urologica Japonica) | Refractory prostatic rhabdomyosarcoma responded to cisplatin + **vinblastine** + peplomycin (PVP) after failing vincristine/actinomycin-D/adriamycin |
| [3329524](https://pubmed.ncbi.nlm.nih.gov/3329524/) | 1987 | Mechanistic/preclinical review | Anti-Cancer Drug Design | Human rhabdomyosarcoma xenograft model used to characterize tubulin-targeting selectivity of vincristine/vinblastine |
| [26024389](https://pubmed.ncbi.nlm.nih.gov/26024389/) | 2015 | Preclinical | Cell Death and Differentiation | PLK1 inhibitors synergize with microtubule-destabilizing drugs (vinca-alkaloid class) to induce apoptosis in preclinical rhabdomyosarcoma models |
| [16302215](https://pubmed.ncbi.nlm.nih.gov/16302215/) | 2007 | Case series (vinorelbine, related regimen) | Pediatric Blood & Cancer | Vinorelbine/low-dose cyclophosphamide regimen (developed for rhabdomyosarcoma) showed activity in desmoplastic small round cell tumor |
| [22156656](https://pubmed.ncbi.nlm.nih.gov/22156656/) | 2011 | Pilot study | Oncotarget | Pediatric metronomic 4-drug regimen (sub-MTD continuous dosing) explored against resistant pediatric solid tumors including sarcomas |
| [41216926](https://pubmed.ncbi.nlm.nih.gov/41216926/) | 2026 | Prospective trial (broader soft-tissue sarcoma) | Pediatric Blood & Cancer | CWS-96/CWS-2002P trials establishing risk stratification and chemo/radiotherapy strategy for pediatric non-rhabdomyosarcoma soft tissue sarcoma; contextualizes sarcoma-family chemotherapy protocols |

---

## Saudi Arabia Market Information

Vinblastine is **not currently marketed** in this jurisdiction (`market_status: 未上市`, `total_licenses: 0`). No product authorization records are available.

---

## Cytotoxicity

Vinblastine is a conventional cytotoxic antineoplastic agent (vinca alkaloid), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — Vinca alkaloid, microtubule/tubulin polymerization inhibitor |
| Myelosuppression Risk | Known class effect; literature in this pack (PMID 7459846) discusses myelosuppressive effects of vinblastine directly. Specific grading/incidence data not available — please refer to the package insert |
| Emetogenicity Classification | Vinca alkaloids are classically low-to-moderate emetogenic risk agents; not confirmed by pack-specific data |
| Monitoring Items | CBC with differential, liver function (hepatically metabolized), neurologic exam (vinca-class peripheral neuropathy risk), IV site (vesicant — extravasation risk) |
| Handling Protection | Must follow cytotoxic/hazardous drug handling protocols; vesicant — requires central line or extravasation precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack flags the **SFDA/TFDA package insert (warnings, contraindications)** as a **Blocking** data gap (DG001) — it must be resolved before any S1 safety assessment can proceed. Drug-drug interaction data is also unavailable (`ddi.query_status: not_found`).

---

## Other Predicted Indications Observed (Context)

This is a multi-indication candidate pack; rhabdomyosarcoma ranked #1 by TxGNN score but is not the strongest by evidence level. Notably:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|------|------|------|------|
| 9 | Neuroblastoma | 99.14% | **L2** | **Proceed with Guardrails** | Phase 1 vinblastine+sirolimus trial (PMID 23956145), historical CVB (cisplatin/vinblastine/bleomycin) cohort, preclinical antiangiogenic synergy |
| 8 | Monocytic leukemia | 99.78% | L3 | Research Question | Historical case series (41% remission, pediatric, 1975) plus combination regimens |
| 5 | Prostate embryonal rhabdomyosarcoma | 99.83% | L4 | Research Question | 2 direct-vinblastine case reports |
| 7 | Liver sarcoma (heterogeneous label) | 99.81% | L4 | Research Question | Indirect — desmoid tumor MTX-vinblastine regimen, Kaposi's sarcoma use |
| 2, 3, 4, 6, 10 | Various RMS subtypes / ganglioneuroblastoma | ~99.1–99.8% | L5 | Hold | Score-only, no clinical or literature evidence |

Neuroblastoma carries materially stronger evidence than the top-ranked rhabdomyosarcoma prediction and may warrant its own evaluation track.

---

## Conclusion and Next Steps

**Decision: Hold** (for the rhabdomyosarcoma indication specifically)

**Rationale:**
- Evidence level is L4 — no vinblastine-specific clinical trials exist for rhabdomyosarcoma; supporting data is same-class (vinorelbine) cohort/Phase 2 evidence plus isolated case reports.
- The Blocking safety data gap (SFDA/TFDA package insert, DG001) prevents any S1 safety evaluation, independent of efficacy evidence strength.

**To proceed, the following is needed:**
- SFDA/TFDA package insert (warnings, contraindications) — resolve DG001 (Blocking)
- Detailed MOA data from DrugBank — resolve DG002
- Drug-drug interaction data (current query: not found)
- Vinblastine-specific (not vinorelbine/vincristine) preclinical or clinical evidence in rhabdomyosarcoma
- Separately, consider prioritizing the **neuroblastoma** indication (L2, Proceed with Guardrails) given its stronger existing evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

