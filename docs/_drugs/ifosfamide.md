---
layout: default
title: Ifosfamide
parent: 僅模型預測 (L5)
nav_order: 319
evidence_level: L5
indication_count: 10
---

# Ifosfamide
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

# Ifosfamide: From Soft Tissue Sarcoma / Testicular Cancer to Female Breast Carcinoma

## One-Sentence Summary

Ifosfamide is an oxazaphosphorine alkylating agent long established in combination chemotherapy for soft tissue sarcoma and testicular carcinoma. The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**, with **8 clinical trials** and **20 publications** currently retrieved in support of this direction — though, as detailed below, several of these need closer scrutiny before the signal can be considered fully confirmed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Soft tissue sarcoma / testicular carcinoma *(derived from literature in the evidence pack — e.g., PMID 3286879; not a Saudi Arabia regulatory dossier text, since no formal indication text is on file)* |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L1 *(as classified in the evidence pack — see caveat below)* |
| Saudi Arabia Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Research Question** |

> **Note on Evidence Level:** The evidence pack labels this candidate "L1," but of the 8 registered trials, none is a *completed* Phase 3 RCT specifically in breast cancer — the single Phase 3 trial identified (NCT00954174) actually enrolled uterine/fallopian tube/ovarian carcinosarcoma, not breast carcinoma (see Clinical Trial Evidence below). The strongest genuine breast-cancer evidence consists of several completed Phase 1/2 single-arm trials and mechanistic/PK studies. Readers should treat the L1 label as provisional pending re-verification.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap DG002 — High severity). Based on known pharmacology, ifosfamide is a cyclophosphamide analog that requires hepatic and intratumoral bioactivation (via CYP3A4, CYP2C9, CYP2B6) to its active metabolite, 4-hydroxy-ifosfamide, which cross-links DNA and induces apoptosis in rapidly dividing cells. This is directly supported by literature in the evidence pack: PMID 14970873 confirms CYP3A4/2C9/2B6 expression and active ifosfamide turnover within breast cancer tissue microsomes themselves, and PMID 11138456 demonstrates measurable DNA damage in both breast tumor tissue and peripheral blood lymphocytes following ifosfamide exposure — i.e., the drug is pharmacologically active inside breast tumor tissue, not just theoretically.

Ifosfamide's original indications (sarcoma, testicular carcinoma) and breast carcinoma share the same underlying vulnerability to alkylating-agent cytotoxicity, and ifosfamide-based regimens have in fact been trialed clinically in breast cancer for decades — mostly as second-/third-line therapy after anthracycline/taxane failure, in combination with etoposide, vinorelbine, paclitaxel, or epirubicin (PMID 11932893, 9226029, 8918497, 8873839, 2347057, 2347053, 10602903). Response rates in these small trials range from modest to notable (e.g., PMID 8873839 reports a 50% overall response rate with ifosfamide/mesna/epirubicin in previously-treated advanced breast cancer), supporting biological plausibility even though ifosfamide is not currently a guideline-standard first-line breast cancer agent.

However, mechanistic plausibility and small historical trials are not equivalent to confirmatory Phase 3 evidence, and this prediction should be read as a *reasonable, literature-supported hypothesis* rather than an established therapeutic pathway.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00026078](https://clinicaltrials.gov/study/NCT00026078) | Phase 2 | Unknown | 42 | Docetaxel + ifosfamide as first-line chemotherapy in metastatic breast cancer — direct regimen test |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | N/A | TIME regimen (topotecan/ifosfamide-mesna/etoposide) with autologous stem cell rescue in metastatic breast cancer; terminated early |
| [NCT00002854](https://clinicaltrials.gov/study/NCT00002854) | Phase 1 | Completed | 33 | Sequential high-dose cisplatin/cyclophosphamide/etoposide and ifosfamide/carboplatin/taxol with autologous stem cell support — early-phase safety data |
| [NCT00020722](https://clinicaltrials.gov/study/NCT00020722) | Phase 2 | Terminated | 7 | Chemotherapy + peripheral stem cell transplant + activated T-cell therapy in stage IV breast cancer; ifosfamide likely used as conditioning agent, not the primary study variable (Grade C relevance, n=7) |
| [NCT00003086](https://clinicaltrials.gov/study/NCT00003086) | Phase 1/2 | Terminated | 12 | Samarium-153 as part of double sequential autologous bone marrow transplant for stage IV breast cancer |
| [NCT00012311](https://clinicaltrials.gov/study/NCT00012311) | Phase 2 | Unknown | N/A | Randomized comparison of multi-cycle high-dose vs. optimized conventional-dose chemotherapy in metastatic breast cancer |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown | 35 | Organoid-based high-throughput drug-screening platform (SCORE) to select chemotherapy for refractory solid tumors — tool-development study, not a direct efficacy trial |
| [NCT00954174](https://clinicaltrials.gov/study/NCT00954174) | Phase 3 | Unknown | 637 | ⚠ **Likely mismatch**: this RCT enrolls uterine/fallopian tube/peritoneal/ovarian **carcinosarcoma**, not breast carcinoma. It compares paclitaxel+carboplatin vs. ifosfamide+paclitaxel. Despite being graded "A" in the source evidence set, the disease population does not match "female breast carcinoma" and should be excluded from the breast-cancer-specific evidence tally pending confirmation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11932893](https://pubmed.ncbi.nlm.nih.gov/11932893/) | 2002 | Phase 2 trial | Cancer | Paclitaxel (24-hr infusion) + ifosfamide in anthracycline-resistant metastatic breast carcinoma |
| [9226029](https://pubmed.ncbi.nlm.nih.gov/9226029/) | 1997 | Phase 2 trial | Tumori | Ifosfamide + etoposide in previously treated advanced breast cancer; response and toxicity profile evaluated |
| [8918497](https://pubmed.ncbi.nlm.nih.gov/8918497/) | 1996 | Phase 2 trial | J Clin Oncol | Ifosfamide + vinorelbine as first-line chemotherapy for metastatic breast cancer |
| [8873839](https://pubmed.ncbi.nlm.nih.gov/8873839/) | 1996 | Phase 2 trial | J Chemother | Ifosfamide/mesna/epirubicin as second-line therapy — 6% CR, 44% PR (50% overall response rate) |
| [2112056](https://pubmed.ncbi.nlm.nih.gov/2112056/) | 1990 | Phase 2 trial | Cancer Chemother Pharmacol | Ifosfamide/etoposide with mesna uroprotection in 44 patients with advanced breast cancer |
| [2347057](https://pubmed.ncbi.nlm.nih.gov/2347057/) | 1990 | Phase 2 trial | Cancer Chemother Pharmacol | Ifosfamide substituted for cyclophosphamide in CMF regimen — effective in CMF-refractory/relapsed breast cancer |
| [2347053](https://pubmed.ncbi.nlm.nih.gov/2347053/) | 1990 | Phase 2 trial | Cancer Chemother Pharmacol | Epirubicin + ifosfamide in 58 patients with refractory breast cancer and other metastatic solid tumors |
| [10602903](https://pubmed.ncbi.nlm.nih.gov/10602903/) | 1999 | Phase 2 trial | Cancer Chemother Pharmacol | Ifosfamide + vinorelbine in metastatic breast cancer after prior anthracycline therapy |
| [7695982](https://pubmed.ncbi.nlm.nih.gov/7695982/) | 1995 | PK/Cohort | Eur J Cancer | Pharmacokinetics, metabolism, and clinical effect of ifosfamide in 15 breast cancer patients |
| [39306877](https://pubmed.ncbi.nlm.nih.gov/39306877/) | 2024 | Cohort | Curr Probl Cancer | Ifosfamide-based chemotherapy experience in metaplastic breast cancer, a chemo-resistant breast cancer subtype |

*Additional mechanistic support (not tabled above, used for the MOA discussion): PMID 14970873 (CYP-mediated ifosfamide bioactivation in breast tumor microsomes), PMID 11138456 (ifosfamide-induced DNA damage in breast tumor tissue), PMID 10907953 (preclinical activity of 4-OH-ifosfamide in breast cancer cell lines).*

*Excluded as likely off-topic/mismatched: PMID 39013199 (ovarian cancer consensus), PMID 23374944 (radiation-induced angiosarcoma), PMID 27710871 (trabectedin/sarcoma review), PMID 10084362 (gene therapy review) — these appear in the retrieval set via keyword co-occurrence rather than direct relevance to ifosfamide in breast carcinoma.*

---

## Saudi Arabia Market Information

Ifosfamide is **not currently marketed in Saudi Arabia** — the evidence pack records 0 authorizations and no license entries. There is no product/dosage-form/indication-text data available to tabulate.

---

## Cytotoxicity

Ifosfamide is a conventional cytotoxic chemotherapy agent (confirmed by original indications in sarcoma/testicular cancer and its DNA-alkylating mechanism), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — oxazaphosphorine alkylating agent (cyclophosphamide analog) |
| Myelosuppression Risk | High — multiple trials in this evidence pack required growth-factor/thrombopoietin support (e.g., NCT00003597, NCT00187109) specifically because of ifosfamide-regimen-induced neutropenia/thrombocytopenia |
| Emetogenicity Classification | Moderate to High (typical for alkylating-agent chemotherapy at oncologic doses; official Saudi labeling data unavailable — see Data Gap below) |
| Monitoring Items | CBC with differential, renal function (BUN/creatinine), urinalysis (hemorrhagic cystitis risk — mesna co-administration required), neurological status (encephalopathy risk, per PMID 41818182 in the wider ifosfamide literature), liver function |
| Handling Protection | Yes — must be handled under institutional hazardous/cytotoxic drug handling protocols (PPE, closed-system transfer devices) |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Outstanding data gap:** The evidence pack flags TFDA-equivalent warnings/contraindications for ifosfamide as a **Blocking** data gap (DG001) — this must be resolved (via official label retrieval) before any Stage 1 (S1) safety pre-assessment can be completed. A drug interaction (DDI) query also returned no results ("not_found") and should be re-run through an alternative source.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Ifosfamide shows a mechanistically plausible and literature-supported signal in breast cancer (direct intratumoral bioactivation, DNA damage, and multiple small Phase 1/2 trials with measurable response rates), but the evidence falls short of confirmatory Phase 3 data — the one registered Phase 3 RCT in this evidence set is very likely a disease-mismatch (gynecological carcinosarcoma, not breast carcinoma). Combined with the drug's absence from the Saudi Arabia market and a blocking gap in local safety labeling, this candidate should remain a research question rather than proceed to Go or Guardrailed deployment.

**To proceed, the following is needed:**
- TFDA/SFDA-equivalent package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Detailed DrugBank mechanism-of-action data (DG002)
- Confirmation/correction of the NCT00954174 disease-population mismatch, and a targeted search for genuinely breast-cancer-specific completed RCTs
- A fresh drug-drug interaction (DDI) query, since the current lookup returned no data
- A regulatory pathway assessment given zero existing Saudi Arabia market authorizations for ifosfamide
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

