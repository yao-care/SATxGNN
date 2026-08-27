---
layout: default
title: Ribavirin
parent: 僅模型預測 (L5)
nav_order: 543
evidence_level: L5
indication_count: 10
---

# Ribavirin
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

# Ribavirin: From Antiviral Therapy to Chronic Hepatitis B Virus Infection

## One-Sentence Summary

Ribavirin is a guanosine nucleoside analog historically used in combination antiviral regimens (e.g., with peginterferon) against RNA viral infections such as hepatitis C. The TxGNN model predicts it may be effective for **Chronic Hepatitis B Virus Infection**, but the supporting evidence base is weak: the drug is not currently marketed in Saudi Arabia, its original approved indication is not on record, and the clinical trials/literature retrieved are predominantly about hepatitis C or HBV/HCV co-infection rather than HBV monotherapy efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved-indication record on file (drug is unmarketed; regulatory/label data not available) |
| Predicted New Indication | Chronic Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, sourced mechanism-of-action data is not currently available for ribavirin in this evidence pack (flagged as a High-severity data gap). Based on the repurposing rationale generated alongside the prediction, ribavirin is a guanosine nucleoside analog that acts mainly through IMPDH inhibition and RNA mutagenesis, mechanisms that target **RNA viruses** such as hepatitis C virus (HCV).

Hepatitis B virus (HBV), by contrast, is a partially double-stranded DNA virus that replicates via reverse transcription. Direct mechanistic support for ribavirin's antiviral activity against HBV is weak. The very high TxGNN score most likely reflects the extensive literature and knowledge-graph co-occurrence of HBV and HCV in "dual infection" / "co-infection" contexts — where ribavirin is a standard component of anti-HCV therapy administered to patients who also carry HBV — rather than evidence that ribavirin directly suppresses HBV replication.

In other words, the prediction is plausible as a graph-embedding artifact of shared clinical contexts (HBV/HCV co-infection management, shared risk populations, shared literature) rather than as a direct pharmacological signal. This distinction matters for interpreting the clinical trial and literature evidence below, most of which addresses ribavirin's role in treating HCV in patients who happen to also have HBV, not ribavirin's efficacy against HBV itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Phase 3 | Completed | 138 | PARC Study: peginterferon alfa-2a + ribavirin vs. peginterferon monotherapy in HBeAg-negative chronic HBV — tested whether adding ribavirin enhances virologic response (HBV DNA suppression) over interferon alone. Most directly relevant trial to this indication hypothesis. |
| [NCT01401400](https://clinicaltrials.gov/study/NCT01401400) | N/A | Completed | 1350 | GIANT-B Study: genetic determinants of response to peginterferon-based treatment in chronic hepatitis B patients; background antiviral context, not a ribavirin efficacy trial per se. |
| [NCT02339337](https://clinicaltrials.gov/study/NCT02339337) | Phase 4 | Completed | 203 | Pioneer pilot study: tailored peginterferon alfa + ribavirin regimen in patients with chronic hepatitis C/hepatitis B co-infection (HBeAg-negative), guided by viral kinetics — evaluates HCV response, not HBV efficacy directly. |
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Phase 3 | Unknown | 320 | Peginterferon alfa-2a + ribavirin in HCV/HBV co-infected vs. HCV mono-infected patients — designed around treating the HCV component in co-infected patients. |
| [NCT00630084](https://clinicaltrials.gov/study/NCT00630084) | Phase 4 | Completed | 120 | Peginterferon + ribavirin outcomes in chronic hepatitis C patients with concomitant malignancy — graded as possibly relevant but title/summary center on HCV, not HBV; relevance uncertain. |

**Note:** The full evidence pack returned 50 clinical trials for this indication query, but the large majority (graded "C" — indirect/possibly mislabeled) are standard peginterferon + ribavirin trials for chronic hepatitis C, HCV-related conditions, or unrelated antivirals, not HBV-specific studies. Only the trials above have a title/summary directly referencing hepatitis B. No trial tests ribavirin as HBV monotherapy or against an HBV-specific endpoint as a primary objective.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10832679](https://pubmed.ncbi.nlm.nih.gov/10832679/) | 2000 | Commentary | Journal of Gastroenterology | "Is ribavirin treatment really effective for chronic hepatitis B?" — directly interrogates the efficacy question underlying this prediction. |
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | Reviews HCV/HBV co-infection management, including peginterferon + ribavirin regimens for the HCV component. |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World Journal of Gastroenterology | Updates on treatment and outcomes of dual chronic HCV/HBV infection. |
| [19669238](https://pubmed.ncbi.nlm.nih.gov/19669238/) | 2009 | Review | Hepatology International | Dual chronic HBV and HCV infection — viral interaction dynamics and treatment considerations. |
| [27433078](https://pubmed.ncbi.nlm.nih.gov/27433078/) | 2016 | — | World Journal of Gastroenterology | Notes that while HCV can be eliminated with combination DAA therapy, HBV persists even after treatment and requires lifelong therapy — underscores that interferon/ribavirin-based regimens are not curative for HBV. |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | — | Annual Review of Medicine | Current treatment strategies for chronic hepatitis B and C — describes interferon and lamivudine (not ribavirin) as HBV treatment mainstays. |
| [18804888](https://pubmed.ncbi.nlm.nih.gov/18804888/) | 2008 | Review | Journal of Hepatology | Treatment of HBV/HCV co-infection — still a challenge for the hepatologist. |
| [21538279](https://pubmed.ncbi.nlm.nih.gov/21538279/) | 2011 | Review | Seminars in Liver Disease | Host genetics of chronic hepatitis B and C outcomes. |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | — | World Journal of Gastroenterology | IL28B genetic polymorphism and its association with peginterferon/ribavirin response in HCV, and its uncertain relationship to HBV outcomes. |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | — | Expert Review of Anti-infective Therapy | Treatment options for chronic hepatitis B and C infection in children. |

**Note:** None of the retrieved literature is a randomized controlled trial specifically testing ribavirin efficacy against HBV. The most directly on-topic item (Kakumu 2000) poses the efficacy question rather than demonstrating a positive result.

---

## Saudi Arabia Market Information

Ribavirin currently has no marketing authorization on record (market status: **Not Marketed**, 0 licenses). No product, dosage form, or approved-indication data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available in this evidence pack (TFDA package insert retrieval is flagged as a Blocking data gap, DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the mechanistic basis is weak — ribavirin's known antiviral activity targets RNA viruses, while HBV is a DNA virus, and the retrieved trials/literature are almost entirely about ribavirin's established role in HCV treatment (including in HBV/HCV co-infected patients) rather than direct evidence of anti-HBV efficacy. The one directly relevant Phase 3 trial (PARC) tested ribavirin as an *add-on* to interferon rather than as a therapy in its own right, and no literature confirms a positive HBV-specific outcome. Combined with the Blocking data gap on safety labeling and the drug's unmarketed status in Saudi Arabia, this candidate does not meet the bar to proceed at this time.

**To proceed, the following is needed:**
- TFDA/local package insert with warnings and contraindications (DG001 — Blocking)
- Verified mechanism-of-action data from DrugBank (DG002 — High)
- Full-text review of the PARC study (NCT00114361) results to confirm whether ribavirin add-on therapy showed a genuine HBV-specific benefit
- Clarification of whether the high TxGNN score reflects a true mechanistic signal or a graph co-occurrence artifact from HBV/HCV co-infection literature, before further evidence collection is prioritized
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

