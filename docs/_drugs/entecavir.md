---
layout: default
title: Entecavir
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Entecavir
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

# Entecavir: From Chronic Hepatitis B Virus Infection to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir is a nucleoside analogue whose established, well-documented use is suppressing hepatitis B virus (HBV) replication; the source drug record for this candidate is missing that original-indication field (data gap), but it is recoverable from the evidence pack itself (see rank‑2 finding below). The TxGNN model's top-ranked prediction is **Chronic Hepatitis C Virus Infection**, but after reviewing the underlying **~40 clinical trials** and **20 publications**, this specific prediction appears to be a knowledge-graph artifact (HBV/HCV entity confusion) rather than a genuine pharmacological signal, and the evidence pack's own scoring places it at the lowest confidence tier (L5, Hold).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis B Virus Infection *(not recorded in `original_indications` — this is a data gap; inferred from the evidence pack's own rank‑2 rationale, which identifies entecavir as an existing first-line approved HBV drug)* |
| Predicted New Indication | Chronic Hepatitis C Virus Infection |
| TxGNN Prediction Score | 99.98% (rank 813 of all disease predictions) |
| Evidence Level | L5 (model prediction only; no supporting studies) |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

**It is not.** The evidence pack's own mechanistic analysis concludes this prediction lacks pharmacological plausibility, and this report agrees with that assessment.

Entecavir is a guanosine nucleoside analogue that selectively inhibits **HBV reverse transcriptase** — blocking priming of the polymerase, reverse transcription of the pregenomic RNA, and second-strand DNA synthesis. This mechanism is specific to viruses that replicate through a reverse-transcription step. Hepatitis C virus, by contrast, is a positive-strand RNA virus that replicates entirely through its own **RNA-dependent RNA polymerase (RdRp)** and never uses a reverse-transcription intermediate. Entecavir has no known activity against HCV RdRp.

The apparent "supporting" trials and literature in this evidence pack are almost entirely studies of **HBV monotherapy or HBV/HCV co-infection management** (e.g., HBV reactivation risk during anti-HCV DAA therapy, viral load kinetics in dual-infected patients). These co-occur with the term "hepatitis C" in the literature because HBV and HCV share transmission routes and are frequently discussed together in coinfection contexts — not because entecavir treats HCV. This is a textbook case of **knowledge-graph entity confusion**: TxGNN's embedding space picked up co-occurrence signal, not efficacy signal.

The evidence pack's own `repurposing_rationale` for this entry states this explicitly, and duplicate rank‑4 entry ("hepatitis C virus infection") shows the identical pattern — the two should likely be merged/deduplicated at the database level.

## Clinical Trial Evidence

None of the identified trials provide direct evidence for entecavir's efficacy in HCV. All graded trials were classified as **not relevant (Grade C)** — they are HBV trials that were mismatched to this HCV entity.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04157257](https://clinicaltrials.gov/study/NCT04157257) | Phase 2 | Unknown | 60 | QL-007 + entecavir/tenofovir in chronic hepatitis **B** (not C) — knowledge-graph mismatch |
| [NCT01179594](https://clinicaltrials.gov/study/NCT01179594) | Phase 4 | Withdrawn | 0 | Pegasys ± entecavir in HBeAg-negative chronic hepatitis B; withdrawn, unrelated to HCV |
| [NCT05005507](https://clinicaltrials.gov/study/NCT05005507) | Phase 2 | Terminated | 1 | Terminated after 1 enrollee; HBV-focused, no HCV evidence |
| [NCT01022801](https://clinicaltrials.gov/study/NCT01022801) | Phase 2 | Completed | 120 | Entecavir vs. lamivudine in Japanese chronic hepatitis B patients — HBV trial |
| [NCT00597259](https://clinicaltrials.gov/study/NCT00597259) | Phase 4 | Unknown | 294 | Pegasys + entecavir vs. entecavir alone, HBeAg-positive chronic hepatitis B — unrelated to HCV |
| [NCT01848743](https://clinicaltrials.gov/study/NCT01848743) | Phase 3 | Unknown | 120 | Tenofovir vs. lamivudine for severe HBV exacerbation — not entecavir-led, not HCV |
| [NCT02956850](https://clinicaltrials.gov/study/NCT02956850) | Phase 1 | Completed | 160 | Safety/PK study, presumed HBV population — insufficient detail to confirm any HCV relevance |
| [NCT00096785](https://clinicaltrials.gov/study/NCT00096785) | Phase 3 | Completed | 69 | Early viral kinetics of entecavir vs. adefovir in nucleoside-naive chronic hepatitis B |
| [NCT02589652](https://clinicaltrials.gov/study/NCT02589652) | N/A | Unknown | 294 | Peg-IFN sequential therapy after long-term entecavir in chronic hepatitis B — not HCV |
| [NCT00412529](https://clinicaltrials.gov/study/NCT00412529) | Phase 3 | Completed | 44 | Telbivudine vs. entecavir kinetics in HBeAg-positive chronic hepatitis B — exploratory HBV trial |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | Examines HCV reactivation/viral load evolution in anti-HCV-antibody-positive chronic hepatitis B patients undergoing nucleos(t)ide (entecavir-class) therapy — a coinfection-monitoring study, not an HCV treatment trial |
| [28487602](https://pubmed.ncbi.nlm.nih.gov/28487602/) | 2017 | Review | World J Gastroenterol | Reviews HBV, HCV, and alcohol as causes of HCC; notes HCV is now largely curable via DAAs, unrelated to entecavir |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | General review of chronic hepatitis B and C treatment landscape; entecavir discussed only in the HBV context |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Review | Clin Res Hepatol Gastroenterol | Pediatric management of HBV and HCV infections; no entecavir-HCV efficacy data |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | Advances in treating HBV/HCV coinfection; entecavir covered only as an HBV agent |
| [32527114](https://pubmed.ncbi.nlm.nih.gov/32527114/) | 2021 | Review | Chin Clin Oncol | Timing/management of HBV and HCV in hepatocellular carcinoma patients; not an entecavir efficacy study |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Reviews antiviral drugs (including entecavir) for HBV and separately for HCV — the two are distinct drug classes in this review, not combined therapy |
| [39351520](https://pubmed.ncbi.nlm.nih.gov/39351520/) | 2024 | Editorial | World J Hepatol | General commentary on metabolomics in liver disease; not entecavir- or HCV-specific |
| [38631661](https://pubmed.ncbi.nlm.nih.gov/38631661/) | 2024 | Basic Science | Antiviral Research | Studies transcription factor YY1 and HBV replication; unrelated to HCV |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Review | World J Hepatol | Management of HBV and HCV patients around liver/kidney transplantation; entecavir referenced only for HBV |

## Saudi Arabia Market Information

Entecavir is currently **not marketed** in Saudi Arabia under this candidate record, and no product license entries are available (0 authorizations on file). No dosage form, brand name, or approved-indication text could be extracted from the regulatory data.

## Safety Considerations

No structured safety data (warnings, contraindications, or drug-drug interactions) is available for this candidate — all three fields returned only data gaps, and the TFDA/SFDA package insert has not yet been retrieved (flagged as a **Blocking** data gap, DG001, in the source record). Please refer to the package insert for safety information once it becomes available.

**One evidence-derived safety signal is worth flagging**, even though it did not come from the formal safety fields: literature identified elsewhere in this evidence pack (in the HIV-co-infection prediction branch, not shown above) reports that entecavir has partial, sub-therapeutic anti-HIV-1 activity and can select for the HIV reverse-transcriptase resistance mutation M184V in HIV/HBV-coinfected patients who are not on antiretroviral therapy. This is a known clinical caution for entecavir use in that population and should be confirmed against the official label once available — it is unrelated to the HCV prediction itself but is directly relevant to safe use of this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (Chronic Hepatitis C Virus Infection) has no mechanistic basis — entecavir inhibits HBV reverse transcriptase, a replication step HCV does not use — and every supporting trial/publication reviewed is actually about HBV or HBV/HCV coinfection management rather than HCV treatment efficacy. The evidence level is L5 (model score only), consistent with the source scoring's own "Hold" recommendation.
- This candidate record also has two blocking data problems: `original_indications` is empty (entecavir's real, well-established original indication — chronic hepatitis B — is missing from the record) and the TFDA/SFDA package insert has not been retrieved, which by itself blocks any safety-tier review (DG001).

**To proceed, the following is needed:**
- Correct the drug record's `original_indications` field to reflect entecavir's actual approved use (chronic hepatitis B virus infection), so future TxGNN predictions are not mistaken for a "novel" finding when they merely restate the known indication.
- Retrieve the TFDA/SFDA package insert (warnings, contraindications, interactions) to unblock the S1 safety pre-screen (DG001).
- Retrieve confirmed mechanism-of-action documentation from DrugBank (DG002) to formally support future mechanistic-plausibility scoring rather than relying on inference from trial/literature rationale text.
- If this candidate pipeline is re-run, apply an entity-disambiguation step for "hepatitis B" vs. "hepatitis C" search terms to prevent recurrence of this knowledge-graph confusion (also affecting the duplicate rank‑4 "hepatitis C virus infection" entry).
- This candidate should **not** advance to clinical evaluation for HCV. If a genuine repurposing signal exists in this evidence pack, it is the correction of the HBV indication record (rank 2), not a new therapeutic use.

*This report is for research reference only and does not constitute medical advice. Any repurposing candidate requires full clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

