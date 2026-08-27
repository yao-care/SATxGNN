---
layout: default
title: Minoxidil
parent: 僅模型預測 (L5)
nav_order: 424
evidence_level: L5
indication_count: 10
---

# Minoxidil
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

# Minoxidil: From Hypertension to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Minoxidil is best known as an oral vasodilator for severe hypertension, later repurposed into a topical treatment for androgenetic alopecia (a use not captured in this Taiwan evidence pack, where the drug is currently unmarketed). The TxGNN model's top prediction is efficacy in **hypotrichosis simplex of the scalp**, a rare hereditary non-scarring hair disorder, currently supported by **0 clinical trials** and **3 case-report publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Taiwan licensing data (0 licenses on file); internationally, minoxidil's original approved use is oral treatment of severe/refractory hypertension |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.9999% |
| Evidence Level | L4 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for minoxidil was not retrievable from DrugBank in this pack (marked as a data gap). However, the evidence pack's own mechanistic assessment for this candidate provides the relevant rationale: hypotrichosis simplex of the scalp is a hereditary non-scarring hair disorder in which hair follicles are structurally present but the growth cycle is disrupted. It shares a core pathological feature with androgenetic alopecia — prolonged telogen (resting) phase and shortened anagen (growth) phase.

Minoxidil's established mechanism in hair disorders is to prolong the anagen phase and promote vascularization of the dermal papilla. Because this mechanism acts on the hair cycle itself rather than on a specific etiology, it is plausible that it extends to hypotrichosis simplex, even though the underlying cause (mutations in the *CDSN* gene, encoding corneodesmosin) differs from androgenetic alopecia.

This theoretical basis is supported, at a preliminary level, by three case reports in which oral or topical minoxidil — usually combined with other therapies (growth factors, botanic extracts, or platelet-rich plasma) — produced clinical improvement in patients with hereditary hypotrichosis simplex.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | Case Report | Dermatologic Therapy | Treatment of hereditary hypotrichosis simplex of the scalp with oral minoxidil combined with growth factors |
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | Case Report | Frontiers in Genetics | Familial case (8-year-old male, *CDSN* mutation) treated with a combination of botanic extracts and minoxidil; notes lack of definitive effective treatments for this rare monogenic disorder |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | Case Report | Journal of Dermatological Treatment | 14-year-old patient with hypotrichosis simplex successfully treated with combined platelet-rich plasma injection and topical minoxidil 2% |

## Taiwan Market Information

Minoxidil is not currently marketed in Taiwan, and no product authorizations are on file (0 licenses).

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: DG001 — TFDA package insert warnings/contraindications — is flagged as a **Blocking** data gap in the evidence pack, meaning safety review (S1) cannot formally proceed until this is resolved.)*

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic rationale is plausible and internally consistent (anagen-phase prolongation applies regardless of the underlying cause of follicular dysfunction), but the supporting evidence base is limited to three low-tier case reports (Tier 3) with no registered clinical trials. This corresponds to Evidence Level L4 — sufficient to justify a formal research question, not yet a development or guardrailed-use decision.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications data (DG001, Blocking — required before any S1 safety screening)
- DrugBank mechanism-of-action data (DG002, High priority)
- A prospective case series or small trial in genetically confirmed hypotrichosis simplex patients, rather than reliance on case reports
- Taiwan regulatory pathway assessment, since the drug currently holds no local marketing authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

