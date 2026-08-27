---
layout: default
title: Sofosbuvir
parent: 僅模型預測 (L5)
nav_order: 579
evidence_level: L5
indication_count: 8
---

# Sofosbuvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Sofosbuvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Sofosbuvir (DrugBank DB08934) is an NS5B RNA-dependent RNA polymerase (RdRp) inhibitor originally developed and marketed for chronic hepatitis C virus (HCV) infection. The TxGNN model's top prediction for this compound is **Hepatitis B Virus Infection**, drawing on **50 clinical trial records and 19 publications** retrieved for this pairing — but on closer reading, the strongest and most consistent signal in that evidence is not therapeutic benefit, it is **HBV reactivation as an adverse event** during HCV treatment, which points the opposite direction from the predicted indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C Virus (HCV) infection |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action data was not returned for this compound (data gap, severity: High). Based on the pharmacological information present throughout the evidence pack itself, sofosbuvir is a nucleotide analogue prodrug that is metabolized intracellularly to its active triphosphate and inhibits the HCV NS5B RNA-dependent RNA polymerase (RdRp), terminating viral RNA chain synthesis. This mechanism is well validated for HCV, a positive-strand ssRNA virus that depends on RdRp for genome replication.

Hepatitis B virus, however, is a partially double-stranded DNA virus that replicates via an RNA intermediate using a viral reverse transcriptase, not an RdRp. Sofosbuvir's validated target is therefore not directly present in the HBV replication cycle, which weakens the mechanistic rationale for repurposing relative to other TxGNN candidates in this evidence pack (e.g., HEV, which — like HCV — is a (+)ssRNA RdRp-dependent virus and shows better mechanistic alignment).

The evidence base for this specific ranking is dominated by studies of **HCV/HBV-coinfected patients receiving sofosbuvir for their HCV infection**, in which HBV virological activity was monitored as a secondary safety outcome rather than a treatment target. Several of these reports describe HBV reactivation following sofosbuvir-based DAA therapy — a safety signal, not an efficacy signal. The one genuine efficacy hypothesis in this evidence set (a modest HBsAg decline observed in coinfected patients, explored prospectively in a small HBV-monoinfection pilot study) is real but very preliminary (n=21).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Open-label pilot in HBV-monoinfected subjects testing whether ledipasvir/sofosbuvir (12 weeks) reduces HBsAg and HBV DNA, based on a retrospective signal of modest HBsAg decline seen in HBV/HCV-coinfected patients previously treated for HCV. |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3 | Completed | 111 | Evaluated antiviral efficacy and safety of ledipasvir/sofosbuvir in Taiwanese patients with genotype 1/2 HCV and HBV coinfection; primary endpoint was HCV clearance, HBV status monitored as safety outcome. |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study of incidence, morbidity, mortality and predisposing factors for HBV reactivation during direct-acting antiviral treatment of HCV in HCV/HBV coinfected patients — a safety/reactivation study, not an HBV efficacy trial. |

*Note: The remaining trials returned for this query (mostly HCV monoinfection genotype/regimen studies) were graded low relevance (TxGNN co-occurrence artifacts) and are excluded from this table.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | RCT (Phase 2) | Journal of Medical Virology | Open-label pilot of ledipasvir/sofosbuvir (12 weeks) in HBV-monoinfected subjects; primary/secondary endpoints were decline in HBsAg and HBV DNA at Week 12 — the main prospective efficacy evidence for this indication. |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Cohort | Trans. R. Soc. Trop. Med. Hyg. | Sofosbuvir/daclatasvir-based therapy in chronic HCV and HCV/HBV-coinfected patients in Egypt; describes generic DAA efficacy and safety in the coinfected subgroup. |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Case report (safety signal) | Medicine | HBV reactivation following successful HCV treatment with sofosbuvir and ribavirin — reported as a rare but clinically significant adverse event. |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohort/case series | Journal of Clinical Gastroenterology | Examined risk of HBV reactivation among patients treated with ledipasvir-sofosbuvir for HCV in actively infected or previously exposed individuals. |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Cohort | Infection and Drug Resistance | Management of HBV reactivation post-DAA treatment of HCV in HCV/HBV coinfected patients with pretreatment HBeAg seroconversion. |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case report | Journal of Medical Case Reports | HBV reactivation sustained by an HBsAg immune-escape mutant in an anti-HBc-positive patient during sofosbuvir/velpatasvir treatment for HCV. |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Cohort | Journal of Viral Hepatitis | Prospective observational study of HBV reactivation in cancer patients receiving DAAs (including sofosbuvir-based regimens) for HCV, in HBV/HCV coinfection. |
| [27621502](https://pubmed.ncbi.nlm.nih.gov/27621502/) | 2015 | Review (ADR surveillance) | Hospital Pharmacy | Includes a reported case of hepatitis B reactivation associated with HCV treatment using simeprevir and sofosbuvir. |
| [37517414](https://pubmed.ncbi.nlm.nih.gov/37517414/) | 2023 | Modelling study | Lancet Gastroenterology & Hepatology | Global prevalence, care cascade, and prophylaxis coverage of HBV — background epidemiological context, not drug-specific. |
| [39914746](https://pubmed.ncbi.nlm.nih.gov/39914746/) | 2025 | Review | Journal of Hepatology | Reviews HCV treatment scale-up (2014–2023) and draws applicable lessons for the rollout of future HBV and HDV therapies. |

---

## Saudi Arabia Market Information

Sofosbuvir currently has **no marketing authorization on record** for this market (market status: Not Marketed; 0 authorizations). No product license data is available to summarize in table form.

---

## Safety Considerations

No formal package-insert warnings, contraindications, or drug-interaction records were returned for this compound in the safety database (query status: not found).

However, the evidence review for this specific repurposing candidate surfaced a recurring **safety signal not captured in the formal safety fields**: multiple case reports and cohort studies describe **HBV reactivation** in HBV/HCV-coinfected patients during or after sofosbuvir-based direct-acting antiviral therapy for HCV (PMIDs 33031326, 29334502, 31632097, 31542053, 33523503, 27621502). This is a clinically important consideration specifically *because* it runs counter to the predicted new indication, and should be treated as a screening/monitoring flag — not a therapeutic rationale — for any HBV-related use of this drug.

For all other safety information, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis is weak — sofosbuvir's validated target (HCV RdRp) is not the primary replication enzyme of HBV (reverse transcriptase) — and the bulk of the retrieved evidence describes HBV reactivation as an *adverse* event during HCV treatment rather than therapeutic effect on HBV. The one direct efficacy signal (a Phase 2 pilot, n=21, testing HBsAg/HBV DNA decline) is real but far too small and preliminary to support advancement, consistent with the assigned evidence level (L3) and decision stage (S1).

**To proceed, the following is needed:**
- Full published results of NCT03312023 (currently only pilot-level data via PMID 36045503)
- A dedicated, adequately powered RCT in HBV-monoinfected patients to confirm or refute the HBsAg-reduction signal
- Formal DrugBank/TFDA mechanism-of-action and package-insert data (currently blocking gaps DG001/DG002)
- A structured pharmacovigilance review specifically weighing the HBV reactivation signal against any purported antiviral benefit before any S1 safety review proceeds
- Confirmation of local (Saudi Arabia) regulatory and market status, given the drug is currently unmarketed with zero authorizations on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

