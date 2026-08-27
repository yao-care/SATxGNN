---
layout: default
title: Obeticholic Acid
parent: 僅模型預測 (L5)
nav_order: 453
evidence_level: L5
indication_count: 6
---

# Obeticholic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using the evidence pack fields directly (drug identity, taiwan_regulatory, predicted_indications[0], safety) per the specified report template. Below is the report.

---

# Obeticholic Acid: From Primary Biliary Cholangitis to Rheumatoid Arthritis

*Note: this evidence pack contains no Saudi Arabia regulatory/license data for obeticholic acid (0 licenses on file — the drug is not currently marketed in Saudi Arabia). The original indication shown above reflects obeticholic acid's well-established global indication (cholestatic liver disease / primary biliary cholangitis) and is consistent with the FXR-agonist / PBC context referenced in this pack's own literature (PMID 32299307) — it is not itself sourced from a Saudi Arabia license record.*

## One-Sentence Summary

> Obeticholic acid (OCA) is a farnesoid X receptor (FXR) agonist whose established use is in cholestatic liver disease (primary biliary cholangitis); it is not currently licensed or marketed in Saudi Arabia.
> The TxGNN model predicts possible relevance to **Rheumatoid Arthritis**, but this is currently supported only by **0 clinical trials** and **3 indirect, non-RCT publications**, none of which directly studies OCA in RA patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (0 Saudi Arabia licenses); externally established indication is cholestatic liver disease (primary biliary cholangitis) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L4 (preclinical/mechanistic only) |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally documented in this evidence pack (data gap DG002, High severity). Based on the analytical context available within this pack, obeticholic acid is described as an **FXR (farnesoid X receptor) agonist** with anti-inflammatory and hepatoprotective properties, and its established use lies in cholestatic autoimmune/metabolic liver disease.

The link between this profile and rheumatoid arthritis is weak and indirect. The only literature reference with any substantive connection (PMID 33704005) shows that FXR activation *prevents liver injury caused by Tripterygium wilfordii preparations* — an herbal medicine commonly used in Traditional Chinese Medicine to treat RA. This demonstrates a hepatoprotective effect **against RA-therapy-induced toxicity**, not a direct anti-rheumatic effect of OCA itself. The remaining two references discuss primary biliary cholangitis diagnosis/treatment and animal models of autoimmune hepatitis — both concern autoimmune *liver* disease, not the synovial/joint pathology characteristic of RA.

Taken together, the high TxGNN score most likely reflects graph-embedding proximity between FXR/bile-acid signaling and general immune-modulation pathways in the knowledge graph, rather than an established pharmacological causal chain for RA treatment. No clinical trial or disease-specific mechanistic study currently supports repurposing OCA for RA.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32299307](https://pubmed.ncbi.nlm.nih.gov/32299307/) | 2020 | Review | United European Gastroenterology Journal | Overview of primary biliary cholangitis diagnosis and treatment; establishes OCA's known clinical context in cholestatic autoimmune liver disease — not RA-specific |
| [33704005](https://pubmed.ncbi.nlm.nih.gov/33704005/) | 2021 | Animal/mechanistic study | Xenobiotica | FXR activation prevents liver injury induced by Tripterygium wilfordii preparations (a herbal RA treatment) in mice — an indirect hepatoprotective link, not direct evidence of OCA treating RA |
| [35903109](https://pubmed.ncbi.nlm.nih.gov/35903109/) | 2022 | Review (animal models) | Frontiers in Immunology | Reviews animal models for autoimmune hepatitis and related autoimmune liver diseases; general autoimmune-liver context, no RA-specific data |

---

## Saudi Arabia Market Information

Obeticholic acid is not currently marketed in Saudi Arabia — no local product licenses are on file (0 authorizations).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: this evidence pack flags a Blocking-severity data gap — DG001, TFDA/SFDA package insert warnings and contraindications — meaning a formal safety screen (S1) cannot currently be completed for this drug.)*

---

## Other Candidate Indications Screened (Lower Priority)

Beyond rheumatoid arthritis, five additional TxGNN-predicted indications were reviewed and are **not** carried forward, as each lacks any credible mechanistic or literature support:

- **Conjunctivitis** (score 99.53%) — sole matched literature concerns NASH treated with an unrelated herbal alkaloid; likely a keyword/database mismatch.
- **Colobomatous microphthalmia-rhizomelic dysplasia syndrome** (score 99.30%) — no literature or trials; no known biological link to FXR/bile acid pathways.
- **Brachydactyly-syndactyly syndrome** (score 99.26%) — no literature or trials; a skeletal developmental disorder with no known FXR relevance.
- **Brain small vessel disease 1 with or without ocular anomalies** (score 99.04%) — 19 literature hits, but the 10 reviewed are all congenital ophthalmic/neurodevelopmental case reports unrelated to OCA or FXR signaling; high literature count reflects keyword co-occurrence, not relevance.
- **Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome** (score 99.03%) — no literature or trials; a rare COL4A1-related vascular/renal syndrome with no known link to bile acid metabolism.

These are assessed as low-confidence model artifacts and are excluded from further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence for the rheumatoid arthritis prediction is limited to preclinical/mechanistic and review literature (Evidence Level L4), with zero registered clinical trials and no study directly testing OCA in RA patients. Combined with a Blocking safety data gap, this candidate does not currently meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently a Blocking gap (DG001)
- Formal mechanism of action (MOA) documentation from DrugBank or equivalent source — currently a High-severity gap (DG002)
- A disease-specific mechanistic or preclinical study directly evaluating OCA/FXR agonism in an RA model, rather than the indirect hepatoprotective evidence currently available
- Reassessment if any Phase 2 or later clinical trial of OCA in RA is registered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

