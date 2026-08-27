---
layout: default
title: Telbivudine
parent: 僅模型預測 (L5)
nav_order: 599
evidence_level: L5
indication_count: 10
---

# Telbivudine
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

# Telbivudine: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Telbivudine (DrugBank DB01265) is an L-nucleoside antiviral known clinically as an HBV DNA polymerase inhibitor (marketed elsewhere as Tyzeka/Sebivo for chronic hepatitis B) — though this original indication is not actually captured in this Evidence Pack (`original_indications` and `original_moa` are both data gaps). The TxGNN model's top-ranked prediction is **Chronic Hepatitis C Virus Infection**, nominally supported by **10 clinical trials** and **10 publications**, but on inspection nearly all of this "evidence" is actually about hepatitis B, not C — telbivudine has no established antiviral activity against HCV. This looks like a knowledge-graph co-occurrence artifact rather than a genuine repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in Evidence Pack (Data Gap — `original_indications: []`); telbivudine is a known HBV DNA polymerase inhibitor (chronic hepatitis B) |
| Predicted New Indication | Chronic Hepatitis C Virus Infection |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (`original_moa: "[Data Gap]"`). Based on known pharmacology, telbivudine is the unmodified L-enantiomer of thymidine, acting as a highly selective inhibitor of hepatitis B virus (HBV) DNA polymerase — it preferentially blocks HBV second-strand (DNA-dependent) synthesis. It has no known target overlap with hepatitis C virus, which is an RNA virus replicated by an RNA-dependent RNA polymerase (NS5B), not a DNA polymerase.

Reviewing the supporting evidence in this pack confirms the mechanism does not transfer: of the 10 "chronic hepatitis C" clinical trials listed, essentially all are titled and described as **chronic hepatitis B** studies (e.g., NCT00142298 "Telbivudine in Adults With Chronic Hepatitis B," NCT00412529 "Kinetics of Hepatitis B Virus (HBV) DNA," NCT03181607/NCT05466071 on HBV mother-to-child transmission). The literature is dominated by review articles that discuss hepatitis B *and* C jointly (e.g., "Perspectives on the management of chronic hepatitis B and C," PMID 19344237), not primary evidence of anti-HCV efficacy.

This pattern — HBV-specific trials and joint B/C reviews being pulled in under an HCV query — is consistent with **knowledge-graph co-occurrence bias**: HBV and HCV are frequently discussed together in the literature (comparative reviews, coinfection studies, shared guideline documents), which can inflate a GNN's predicted association without any real pharmacological basis. The evidence pack's own rationale field for this candidate concurs: *"telbivudine acts specifically on HBV DNA polymerase... no known inhibitory activity against HCV (RNA virus, RdRp target); listed trials are in fact all HBV-indication trials."*

## Clinical Trial Evidence

*(as tagged to "chronic hepatitis C virus infection" in the Evidence Pack — flagged where the trial is actually an HBV study)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02956850](https://clinicaltrials.gov/study/NCT02956850) | Phase 1 | Completed | 160 | RO7020531 PK/safety study — target population is **chronic hepatitis B**, not C |
| [NCT00412529](https://clinicaltrials.gov/study/NCT00412529) | Phase 3 | Completed | 44 | Telbivudine vs. entecavir viral kinetics in **HBeAg-positive chronic hepatitis B** |
| [NCT00142298](https://clinicaltrials.gov/study/NCT00142298) | Phase 3 | Completed | 1869 | Open-label extension of telbivudine in **chronic hepatitis B** patients |
| [NCT03181607](https://clinicaltrials.gov/study/NCT03181607) | N/A | Unknown | 300 | Telbivudine/tenofovir to reduce **HBV** mother-to-child transmission |
| [NCT05466071](https://clinicaltrials.gov/study/NCT05466071) | N/A | Unknown | 200 | Tenofovir alafenamide to prevent **HBV** mother-to-child transmission |
| [NCT02058108](https://clinicaltrials.gov/study/NCT02058108) | Phase 3 | Terminated | 53 | Pediatric telbivudine oral solution/tablets in **chronic hepatitis B** |
| [NCT01925820](https://clinicaltrials.gov/study/NCT01925820) | Phase 4 | Unknown | 540 | Pegasys + entecavir vs. entecavir vs. Pegasys for **HBeAg-negative chronic hepatitis B** |
| [NCT01083251](https://clinicaltrials.gov/study/NCT01083251) | N/A | Unknown | 120 | Vitamin D adjunct to Peg-IFN/telbivudine in **chronic HBV** infection |
| [NCT00805675](https://clinicaltrials.gov/study/NCT00805675) | Phase 3 | Completed | 83 | Telbivudine + tenofovir DF combination kinetics in **HBeAg-positive compensated CHB** |
| [NCT00810524](https://clinicaltrials.gov/study/NCT00810524) | Phase 4 | Unknown | 600 | Long-term prognosis of antiviral treatment in **chronic HBV** infection |

**None of these trials studied telbivudine for hepatitis C.** This table reflects a data-tagging artifact in the evidence pack rather than genuine HCV trial support.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19344237](https://pubmed.ncbi.nlm.nih.gov/19344237/) | 2009 | Review | Expert Rev Anti Infect Ther | Joint management perspective on chronic hepatitis B **and** C — not telbivudine-specific HCV data |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Current/future therapy overview for hepatitis B **and** C; telbivudine discussed only in the HBV context |
| [18340426](https://pubmed.ncbi.nlm.nih.gov/18340426/) | 2008 | Review | Der Internist | German guideline update on antiviral therapy for hepatitis B **and** C; telbivudine listed only among HBV agents |
| [25233195](https://pubmed.ncbi.nlm.nih.gov/25233195/) | 2014 | Review | J Perinatol | Review of HBV/HCV in pregnancy and mother-to-child transmission; not an HCV efficacy study of telbivudine |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antiviral medications for HBV and HCV and renal effects; telbivudine listed as an HBV agent only |
| [28845882](https://pubmed.ncbi.nlm.nih.gov/28845882/) | 2018 | Cohort | J Viral Hepat | HBV reactivation during direct-acting antiviral (DAA) therapy **for HCV** — DAAs, not telbivudine, are the study drug |
| [18330099](https://pubmed.ncbi.nlm.nih.gov/18330099/) | 2007 | Guideline | Acta Gastroenterol Belg | Belgian guidelines for management of chronic **hepatitis B** |
| [23697556](https://pubmed.ncbi.nlm.nih.gov/23697556/) | 2013 | Cohort | J Interferon Cytokine Res | IL-37 and HBeAg seroconversion during telbivudine treatment in **HBV** patients |
| [21964179](https://pubmed.ncbi.nlm.nih.gov/21964179/) | 2011 | Review | Mayo Clin Proc | General antiviral drug class review (herpes/hepatitis/influenza); not HCV-specific telbivudine data |
| [21999649](https://pubmed.ncbi.nlm.nih.gov/21999649/) | 2011 | Review | Paediatr Drugs | Pediatric chronic liver disease management overview; not telbivudine-HCV specific |

**No literature in this pack demonstrates anti-HCV activity for telbivudine.**

## Saudi Arabia Market Information

Telbivudine is **not marketed** in Saudi Arabia (`market_status: 未上市`, `total_licenses: 0`). No product authorizations are on file in this Evidence Pack.

## Safety Considerations

Please refer to the package insert for safety information. (`key_warnings`, `contraindications`, and DDI data are all flagged as Data Gaps in this pack — notably, DG001 marks the missing SFDA/TFDA package insert as a **Blocking** gap that prevents any S1 safety pre-assessment.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (chronic hepatitis C) is not mechanistically plausible and is not actually supported by its own cited evidence — the linked trials and most literature describe hepatitis B, not C, indicating a knowledge-graph co-occurrence artifact. The next two ranked candidates fare no better: "hepatitis B virus infection" (rank 2) is not a repurposing opportunity at all — it is telbivudine's own known original indication, misfiled here due to the `original_indications` data gap — and "HIV infectious disease" (rank 3) is directly contradicted by in vitro/clinical evidence (PMID 22024528, PMID 20308377) showing telbivudine has no anti-HIV-1 activity. Ranks 5–10 (phenylalanine/tyrosine metabolism disorders, SIV, feline AIDS, rare neurodevelopmental disorder) have zero trials or literature and are almost certainly high-degree-node model noise.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain the SFDA/TFDA package insert for telbivudine to enable any safety pre-assessment
- Resolve DG002 (High): backfill confirmed mechanism of action and original-indication data from DrugBank/FDA label — this will also correct the mislabeling that makes HBV appear as a "new" prediction
- If HBV re-confirmation is of interest, evaluate it separately as a market-entry/line-extension question, not as a TxGNN repurposing candidate
- No further action recommended on the HCV, HIV, or metabolic-disorder predictions absent new mechanistic or clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

