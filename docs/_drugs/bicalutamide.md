---
layout: default
title: Bicalutamide
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
---

# Bicalutamide
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

# Bicalutamide: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Bicalutamide is a non-steroidal androgen receptor (AR) antagonist widely used for prostate cancer, blocking testosterone and DHT from binding to AR across tissues.
The TxGNN model ranks **Hypertrichosis** as its top predicted new indication (score 99.69%), currently supported by only **1 publication** (a letter/comment).
Importantly, among all 10 evaluated indications, **Female Breast Carcinoma** (rank 9) carries far stronger clinical evidence — 1 ongoing Phase 2 trial and 20 publications — and is the most actionable repurposing candidate in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (non-steroidal antiandrogen; not marketed in Saudi Arabia) |
| Predicted New Indication (Top) | Hypertrichosis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Hypertrichosis) / Proceed with Guardrails (Female Breast Carcinoma) |

---

## Why Is This Prediction Reasonable?

Bicalutamide is a competitive AR antagonist that blocks binding of testosterone and dihydrotestosterone (DHT) to the androgen receptor. By occupying AR without activating it, bicalutamide suppresses androgen-driven cellular proliferation and differentiation across a wide range of tissues — this is the basis of its established use in prostate cancer, where tumor growth is androgen-dependent.

The connection to hypertrichosis rests on the known role of androgens in promoting hair follicle activity. In androgen-sensitive follicles (such as those on the face and body in women with hyperandrogenism), excess androgen signaling drives excessive hair growth. AR blockade is therefore mechanistically plausible for reducing androgen-dependent hypertrichosis. The sole supporting publication (PMID 35304167) is a letter specifically commenting on bicalutamide's ability to counter **minoxidil-induced hypertrichosis** — a pharmacological side-effect scenario rather than treatment of primary hypertrichosis — which may explain the high TxGNN score via a specific knowledge-graph sub-path.

It is critical to note that hypertrichosis encompasses both androgen-dependent forms (where AR antagonism is theoretically active) and purely genetic forms such as Ambras syndrome (chromosome 8q22-24 rearrangement) and isolated hair shaft abnormalities, where AR blockade would have no effect. The current evidence does not differentiate between these subtypes.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Hypertrichosis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35304167](https://pubmed.ncbi.nlm.nih.gov/35304167/) | 2022 | Letter/Comment | Journal of the American Academy of Dermatology | Commentary on bicalutamide's role in improving minoxidil-induced hypertrichosis in female pattern hair loss patients (n=35 retrospective review); supports AR antagonism as a management strategy for drug-induced excess hair growth |

---

## Saudi Arabia Market Information

Bicalutamide currently holds **no regulatory authorizations in Saudi Arabia** (market status: not marketed). No product-level information is available from local regulatory databases. Any future introduction would require SFDA new drug application.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — non-steroidal AR antagonist (antiandrogen); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low (not associated with significant bone marrow suppression) |
| Emetogenicity Classification | Minimal to low |
| Monitoring Items | Liver function tests (LFTs: AST, ALT, bilirubin), serum testosterone/PSA (in oncology use), CBC |
| Handling Protection | Standard pharmaceutical handling; not classified under cytotoxic chemotherapy handling regulations |

---

## Safety Considerations

Detailed local safety data (warnings, contraindications) was not retrievable for the Saudi Arabia market due to the absence of approved product labels. Based on international prescribing information, the following are known:

- **Hepatotoxicity**: Rare but serious liver injury (including fatal cases) has been reported. Baseline LFTs and periodic monitoring are recommended; discontinue if ALT rises >2× ULN.
- **Gynecomastia / breast tenderness**: Common in male patients on prolonged therapy due to peripheral AR blockade with relative estrogen excess.
- **Cardiovascular**: Androgen deprivation may prolong QT interval; cardiac monitoring warranted in at-risk patients.
- **Warfarin interaction**: Bicalutamide can potentiate anticoagulant effect of warfarin (CYP-mediated displacement); INR monitoring required if co-administered.

No DDI data was returned by the local drug interaction query system. Refer to the current international package insert for full prescribing information.

---

## Conclusion and Next Steps

**Decision: Hold (Hypertrichosis) | Proceed with Guardrails (Female Breast Carcinoma)**

**Rationale:**

For **Hypertrichosis** (TxGNN rank 1): Despite the high model score, evidence is limited to a single letter/comment with no clinical trials. The mechanistic case applies only to androgen-dependent subtypes, and the specific context in the publication (minoxidil-induced hypertrichosis) is a niche scenario unlikely to justify a broad repurposing program. Holding pending prospective case series or pilot data.

For **Female Breast Carcinoma** (TxGNN rank 9): This is the most clinically significant finding in the pack. AR is expressed in 10–35% of triple-negative breast cancers (TNBC), particularly the LAR (luminal androgen receptor) subtype. Bicalutamide has demonstrated activity in vitro (proliferation and invasion inhibition in MDA-MB-231 cells), mechanistic studies confirm AR/β-catenin and AR/ERK/FOXC2 pathway involvement, and Phase 2 trial NCT03650894 (nivolumab + bicalutamide + ipilimumab, n=30, completion expected December 2026) is actively running. Multiple reviews (2018–2025) confirm bicalutamide as a lead agent in AR+ TNBC. Evidence level L2 supports advancing to structured evaluation.

---

**To proceed with Hypertrichosis, the following is needed:**
- Prospective case series or pilot study data in androgen-dependent hypertrichosis patients
- Subtype differentiation: confirm only androgen-sensitive forms are targeted
- Full safety and MOA documentation (Saudi Arabia package insert or international label)

**To proceed with Female Breast Carcinoma (recommended path), the following is needed:**
- Monitor NCT03650894 primary results (expected end of 2026)
- Establish AR expression (IHC) as companion diagnostic for LAR-TNBC patient selection
- Obtain bicalutamide SFDA registration in Saudi Arabia (currently no local authorization)
- Design a safety monitoring plan including liver function surveillance and cardiac monitoring
- Evaluate combination strategy: bicalutamide + immune checkpoint inhibitor vs. monotherapy based on trial results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

