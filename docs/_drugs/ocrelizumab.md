---
layout: default
title: Ocrelizumab
parent: 僅模型預測 (L5)
nav_order: 455
evidence_level: L5
indication_count: 5
---

# Ocrelizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Ocrelizumab: From B-Cell-Mediated Autoimmune Disease to HER2 Positive Breast Carcinoma

## One-Sentence Summary

Ocrelizumab is an anti-CD20 monoclonal antibody whose established mechanism is depletion of CD20-expressing B lymphocytes, used in B-cell-mediated autoimmune disease; this specific original indication and its formal mechanism-of-action record are themselves flagged as data gaps in this evidence pack. The TxGNN model predicts it may be effective for **HER2 positive breast carcinoma**, but this prediction is currently supported by **zero clinical trials** and **zero relevant publications**, and the model's own rationale text flags it as a probable false-positive signal from knowledge-graph embedding similarity rather than a genuine mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally confirmed in this evidence pack — described only narratively as "B-cell-mediated autoimmune disease" (MOA record itself is a High-severity data gap, DG002) |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for ocrelizumab is not available in this evidence pack (`original_moa: "[Data Gap]"`, tracked as DG002, High severity). The evidence pack's own repurposing-rationale narrative describes ocrelizumab as an anti-CD20 monoclonal antibody that depletes CD20-expressing B lymphocytes, used primarily for B-cell-mediated autoimmune disease — but this description has not been independently verified against DrugBank or a TFDA-equivalent source, and no original indication list was returned (`original_indications: []`).

HER2 positive breast carcinoma is driven by amplification/overexpression of the HER2 (ERBB2) receptor tyrosine kinase, activating proliferative signaling pathways that are biologically distinct from CD20+ B-cell depletion. There is no established pharmacological or immunological pathway connecting B-cell depletion to HER2-driven tumor proliferation, and no experimental, translational, or clinical data in this pack bridge the two.

Given the absence of a credible mechanistic bridge and the complete absence of clinical trial or literature support (see below), this prediction should be treated as a hypothesis generated purely from model embedding similarity — the evidence pack itself explicitly characterizes it as a **suspected false-positive signal** rather than a validated repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predicted Indications in This Evidence Pack

This evidence pack also lists four additional breast-cancer-related predictions (progesterone-receptor positive breast cancer, normal breast-like subtype, luminal A/B breast tumor, and progesterone-receptor negative breast cancer), all scored L5/Hold with no clinical trial support. One item deserves a specific caution:

- **Breast tumor luminal A or B (rank 4)** returned 19 PubMed hits, but the 10 titles retrieved (B-cell development/maturation, Hepatitis B vaccines, HLA-B allele typing, etc.) are unrelated to breast cancer or ocrelizumab's pharmacology. This pattern strongly suggests the literature query matched on the literal letter "B" rather than the intended "luminal B" breast cancer subtype, and should be treated as a **search false-positive**, not supporting evidence.

None of the five predicted indications in this pack currently has genuine trial or literature support.

---

## Saudi Arabia Market Information

Ocrelizumab is not currently marketed in Saudi Arabia (`market_status: 未上市`), and no product license records are available (`total_licenses: 0`). No dosage form or route information can be assessed at this time.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA-equivalent package insert warnings/contraindications are a Blocking data gap — DG001 — which per the evidence pack directly prevents entry into the S1 safety preliminary evaluation stage. Drug interaction data was queried but not found.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (HER2 positive breast carcinoma) has no clinical trial or literature support, no plausible mechanistic bridge from the drug's B-cell-depleting activity, and is explicitly flagged in the underlying rationale as a likely false-positive model artifact. In addition, a Blocking data gap (missing TFDA-equivalent warnings/contraindications) prevents even a preliminary safety assessment, and a High-severity gap (unverified MOA) prevents mechanistic validation.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the TFDA-equivalent/manufacturer package insert for warnings and contraindications
- Resolve DG002 (High): verify mechanism of action and original approved indication(s) via DrugBank API
- Independent pharmacological review of whether any plausible B-cell/immune-microenvironment link to HER2+ breast carcinoma exists, since none is established in current data
- Re-run the literature search for "luminal A/B breast tumor" with refined query terms to eliminate the "B" keyword false-positive matches before treating rank 4 as evidence-bearing
- Confirm whether any genuine clinical trials or case reports exist for ocrelizumab in oncology settings (e.g., off-label or investigational use) that were not captured by the current search parameters
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

