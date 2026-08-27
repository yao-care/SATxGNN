---
layout: default
title: Simeprevir
parent: 僅模型預測 (L5)
nav_order: 574
evidence_level: L5
indication_count: 10
---

# Simeprevir
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

# Simeprevir: From Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Simeprevir is an oral NS3/4A protease inhibitor developed for chronic hepatitis C virus (HCV) infection (inferred from the trial evidence in this pack, since no formal regulatory indication record exists). The TxGNN model predicts potential efficacy for **Hepatitis B Virus Infection**, and while **19 clinical trials** and **20 publications** were retrieved for this pairing, evidence review finds these are overwhelmingly HCV-focused studies — several documenting **HBV reactivation as an adverse event during HCV treatment**, not HBV efficacy data — so the prediction currently lacks mechanistic or clinical support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C virus (HCV) infection (inferred from trial evidence; not confirmed via regulatory license data — no license records exist) |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 (per evidence-pack scoring; underlying trials are HCV-specific, not HBV-specific — see rationale below) |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for simeprevir is formally listed as a data gap in this pack (DG002). Based on the trial and literature evidence retrieved, simeprevir is an NS3/4A serine protease inhibitor whose target is specific to *Hepatitis C virus* (Flaviviridae). Hepatitis B virus is a *Hepadnaviridae* (reverse-transcribing DNA virus) with no homologous NS3/4A-type protease target, so there is no direct mechanistic pathway by which simeprevir would inhibit HBV replication.

Of the 19 clinical trials returned for this disease pairing, the large majority are HCV genotype 1/4 efficacy, pharmacokinetic-interaction, or safety studies (e.g., simeprevir + sofosbuvir, simeprevir + daclatasvir); none were designed to test antiviral activity against HBV. The apparent link to hepatitis B appears to arise from a real and clinically important — but mechanistically unrelated — signal: **HBV reactivation occurring in HCV/HBV-coinfected patients during interferon-free simeprevir-based HCV treatment**, an immune-mediated phenomenon (loss of HCV-driven immune suppression of HBV) rather than any antiviral effect of simeprevir on HBV itself. Several of the literature citations below describe exactly this reactivation risk, which argues for caution in coinfected patients rather than supporting simeprevir as an HBV therapy.

Given this, the reasoning for repurposing simeprevir toward HBV is not supported by the assembled evidence; the score reflects TxGNN's embedding-space similarity (viral hepatitis / antiviral drug space) rather than a validated pharmacological hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01290679](https://clinicaltrials.gov/study/NCT01290679) | Phase 3 | Completed | 393 | Placebo-controlled TMC435 (simeprevir) + peginterferon/ribavirin in treatment-naive genotype 1 HCV; HCV efficacy trial, not HBV-specific (relevance grade C) |
| [NCT03423641](https://clinicaltrials.gov/study/NCT03423641) | N/A | Completed | 33,808 | Large real-world safety comparison of DAA-treated vs. untreated HCV patients; no HBV endpoint |
| [NCT02765490](https://clinicaltrials.gov/study/NCT02765490) | Phase 2 | Completed | 365 | AL-335 + odalasvir + simeprevir regimens across HCV genotypes 1/2/4/5/6; no HBV endpoint |
| [NCT01852604](https://clinicaltrials.gov/study/NCT01852604) | Phase 2 | Completed | 143 | Samatasvir + simeprevir ± ritonavir in HCV genotype 1b/4/6; no HBV endpoint |
| [NCT02349048](https://clinicaltrials.gov/study/NCT02349048) | Phase 2 | Completed | 68 | Simeprevir + daclatasvir + sofosbuvir, 6–8 weeks, in HCV genotype 1; HCV efficacy trial (relevance grade C) |
| [NCT02278419](https://clinicaltrials.gov/study/NCT02278419) | Phase 2 | Completed | 63 | Simeprevir + sofosbuvir, 8/12 weeks, HCV genotype 4; no HBV endpoint |
| [NCT00561353](https://clinicaltrials.gov/study/NCT00561353) | Phase 2 | Completed | 121 | TMC435350 ± peginterferon/ribavirin in genotype 1 HCV; no HBV endpoint |
| [NCT01323257](https://clinicaltrials.gov/study/NCT01323257) | Phase 1 | Completed | 49 | Healthy-subject PK interaction study (TMC435 with erythromycin/darunavir-ritonavir); disease-nonspecific (relevance grade C) |
| [NCT03099135](https://clinicaltrials.gov/study/NCT03099135) | Phase 3 | Terminated | 24 | 3-year SVR durability follow-up in HCV patients previously on odalasvir/AL-335 ± simeprevir; no HBV endpoint |
| [NCT02118597](https://clinicaltrials.gov/study/NCT02118597) | N/A | Terminated | 19 | Non-interventional study of boceprevir/simeprevir triple therapy retreatment for chronic HCV in Hungary; no HBV endpoint |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26082511](https://pubmed.ncbi.nlm.nih.gov/26082511/) | 2015 | Case Series | Clin Infect Dis | Two cases of HBV reactivation during interferon-free simeprevir + sofosbuvir treatment for HCV; a safety signal, not HBV efficacy evidence |
| [26215390](https://pubmed.ncbi.nlm.nih.gov/26215390/) | 2015 | Case Report | J Med Case Rep | Fulminant HBV reactivation requiring liver transplantation in a chronic HCV patient treated with simeprevir + sofosbuvir |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Reviews approved HBV therapies (interferon, nucleos(t)ide analogues) and HCV therapies separately; does not identify simeprevir as an HBV agent |
| [26558143](https://pubmed.ncbi.nlm.nih.gov/26558143/) | 2015 | Review | World J Gastrointest Pharmacol Ther | HBV prophylaxis in transplant recipients relies on immune globulin + entecavir/tenofovir, not simeprevir |
| [26967675](https://pubmed.ncbi.nlm.nih.gov/26967675/) | 2016 | Review | J Clin Virol | Discusses HBV reactivation as a challenge during DAA treatment of HCV-infected adults |
| [27621502](https://pubmed.ncbi.nlm.nih.gov/27621502/) | 2015 | ADR Report | Hospital Pharmacy | Case feature: hepatitis B reactivation occurring during hepatitis C treatment with simeprevir and sofosbuvir |
| [26082512](https://pubmed.ncbi.nlm.nih.gov/26082512/) | 2015 | Editorial | Clin Infect Dis | Editorial commentary calling for renewed efforts to cure hepatitis B (companion piece to the reactivation case series above) |
| [24631495](https://pubmed.ncbi.nlm.nih.gov/24631495/) | 2014 | Review | Gastroenterology | Reviews new HCV therapies including simeprevir; no HBV efficacy claim |
| [26904396](https://pubmed.ncbi.nlm.nih.gov/26904396/) | 2016 | Review | Acta Pharm Sin B | Notes that, unlike HIV and HBV, HCV is curable with DAAs such as simeprevir — explicitly distinguishes simeprevir's HCV-specific mechanism from HBV |
| [24782255](https://pubmed.ncbi.nlm.nih.gov/24782255/) | 2014 | Review | Semin Liver Dis | Reviews new anti-HCV drug development concepts; not related to HBV |

---

## Saudi Arabia Market Information

Simeprevir is **not currently marketed** in Saudi Arabia (market status: 未上市 / Not Marketed; 0 authorizations on file). No product license records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information — key warnings, contraindications, and DDI data are not available in this pack (TFDA/SFDA package insert retrieval is a Blocking data gap, DG001).

One relevant safety signal did emerge from the literature review above: multiple case reports describe **HBV reactivation in HCV/HBV-coinfected patients** during simeprevir-based HCV treatment. This should be treated as a caution flag for any coinfected population, independent of the (unsupported) HBV-efficacy hypothesis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Simeprevir's NS3/4A protease target is HCV-specific with no HBV homolog, so there is no mechanistic basis for the predicted indication. All 19 retrieved trials and the majority of the 20 publications are HCV-focused; the only genuinely HBV-related literature describes reactivation risk during HCV treatment, an adverse safety signal rather than efficacy evidence. The drug is also not marketed in Saudi Arabia and TFDA/SFDA label data are unavailable (Blocking gap).

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action data from DrugBank — currently a data gap (DG002)
- Preclinical/in vitro evidence of any direct simeprevir activity against HBV targets (polymerase, core, or X protein) — none currently exists
- Any dedicated HBV-specific clinical trial data (the current 19 trials are HCV trials with incidental HBV-coinfection mentions)
- If pursuing any coinfected-population use case, a formal safety review of HBV reactivation risk during simeprevir-based HCV therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

