---
layout: default
title: Tolvaptan
parent: 僅模型預測 (L5)
nav_order: 627
evidence_level: L5
indication_count: 10
---

# Tolvaptan
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

# Tolvaptan: Original Indication Not on File — Evaluated for Autosomal Dominant Polycystic Kidney Disease (ADPKD)

## One-Sentence Summary

This evidence pack does not record tolvaptan's original approved indication (data gap). The TxGNN model's top prediction is **polycystic kidney disease 3 with or without polycystic liver disease (ADPKD/PLD spectrum)**, and the evidence pack itself notes this is not a novel repurposing — tolvaptan, a selective vasopressin V2-receptor antagonist, is already an established treatment for ADPKD elsewhere, supported here by **2 pivotal Phase 3 RCTs** and **20 publications**, though it remains unmarketed in this jurisdiction (Taiwan, 0 authorizations on file).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license records or original indication text on file |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease (ADPKD/PLD) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed formal MOA documentation (DrugBank field) is flagged as a data gap. However, the repurposing rationale attached to this prediction supplies the mechanistic basis: tolvaptan is a selective vasopressin V2-receptor (AVPR2) antagonist that blocks cAMP signaling, thereby inhibiting renal tubular epithelial proliferation and cyst fluid secretion — a mechanism that maps directly onto ADPKD's cystogenesis pathway.

Importantly, the evidence pack explicitly flags this as **not a novel repurposing signal**: ADPKD is tolvaptan's known, already-approved indication in other markets, and the high TxGNN score reflects a correct recovery of a known positive association rather than a new hypothesis. The clinical value of this report is therefore less about mechanistic plausibility and more about **local market-entry status** — tolvaptan is not currently marketed or authorized in this jurisdiction (0 licenses on file), so this candidate represents a registration/access opportunity rather than a discovery.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov/ICTRP queries for this indication returned zero results; the pivotal trials below are captured only as published literature).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT | New England Journal of Medicine | TEMPO 3:4: tolvaptan slowed total kidney volume growth and eGFR decline vs. placebo in early ADPKD |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT | New England Journal of Medicine | REPRISE: tolvaptan preserved kidney function in later-stage ADPKD but caused more aminotransferase/bilirubin elevations |
| [38091246](https://pubmed.ncbi.nlm.nih.gov/38091246/) | 2024 | RCT | Pediatric Nephrology | Randomized trial (NCT02964273) of tolvaptan safety/pharmacodynamics in children (5–17y) with ADPKD |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Consensus Statement | Nephrology Dialysis Transplantation | ERA/ERKNet/PKD International consensus on when and how to initiate tolvaptan in ADPKD |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Systematic Review/Meta-analysis | Nefrologia | Confirms efficacy and summarizes safety profile of tolvaptan across pooled ADPKD trials |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Evaluates disease-modifying agents, including tolvaptan, for slowing ADPKD progression |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Guideline (EASL) | Journal of Hepatology | Clinical practice guideline on cystic liver disease management, covering PLD treatment |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | Comprehensive review of ADPKD epidemiology, genetics, and disease-modifying treatment |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clinics in Liver Disease | Reviews ADPKD/PLD; notes tolvaptan slows renal function deterioration and cyst growth |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Current Opinion in Nephrology and Hypertension | Reviews emerging ADPKD therapies; confirms tolvaptan as the only currently approved disease-modifying agent |

## Taiwan Market Information

No authorization records are on file. `taiwan_regulatory` reports 0 licenses and market status "未上市" (not marketed) — tolvaptan currently has no registered product in this jurisdiction.

## Safety Considerations

No structured safety data (warnings, contraindications, DDI) is on file for this jurisdiction. Please refer to the package insert for safety information.

For context, one of the pivotal trials captured in the literature evidence above (REPRISE, PMID 29105594) reports that tolvaptan use was associated with more elevations in aminotransferase and bilirubin levels than placebo — a hepatotoxicity signal that should inform any local safety monitoring plan even though it is not sourced from this pack's dedicated safety fields.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence strength is high (L1: two completed Phase 3 RCTs plus multi-society consensus guidance), but this reflects confirmation of tolvaptan's already-established ADPKD indication elsewhere rather than a novel discovery, and the drug has zero market presence or regulatory documentation in this jurisdiction.

**To proceed, the following is needed:**
- TFDA/local package insert (warnings, contraindications) — currently a **blocking** data gap (DG001) preventing S1 safety pre-assessment
- Verified DrugBank mechanism-of-action record (DG002)
- Local registration/market-entry pathway assessment, given 0 current authorizations
- A hepatic-monitoring protocol addressing the aminotransferase/bilirubin signal observed in REPRISE
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

