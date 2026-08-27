---
layout: default
title: Pralatrexate
parent: 僅模型預測 (L5)
nav_order: 512
evidence_level: L5
indication_count: 10
---

# Pralatrexate
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

# Pralatrexate: An Antifolate Chemotherapy Explored for Malignant Pleural Mesothelioma

## One-Sentence Summary

> Pralatrexate is a dihydrofolate reductase (DHFR) inhibitor (antifolate); this evidence pack contains no confirmed original indication or approved-label data, and the drug is currently **not marketed in Saudi Arabia**.
> Among 10 TxGNN-predicted indications (mostly mesothelioma-family tumours), **Malignant Pleural Mesothelioma** has the strongest supporting evidence — a direct Phase II single-arm trial plus 2 supporting publications — even though its TxGNN score ranks 10th of the 10 candidates presented.
> Other top-scoring predictions (e.g., pleural adenomatoid tumor, relapsing-remitting multiple sclerosis) have no clinical trial or literature support and are explicitly flagged by the model rationale as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `original_indications` is empty and no Saudi Arabia license record exists in this evidence pack |
| Predicted New Indication | Pleural (Malignant) Mesothelioma |
| TxGNN Prediction Score | 99.85% (rank 3273 of full candidate list) |
| Evidence Level | L3 (observational/Phase II single-arm + review) |
| Saudi Arabia Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in this pack (`original_moa: [Data Gap]`), and no original indication is recorded. Based on the information that is available, pralatrexate (10-propargyl-10-deazaaminopterin) is a DHFR-inhibiting antifolate, pharmacologically related to methotrexate and to pemetrexed — the antifolate already approved for malignant pleural mesothelioma. This shared drug-class mechanism is the basis for the TxGNN prediction and is corroborated by direct experimental data: PMID 11595715 reports pralatrexate had 25–30× greater in vitro cytotoxic potency than methotrexate against mesothelioma cell lines, and PMID 17409804 reports a completed Phase II clinical trial of pralatrexate specifically in unresectable malignant pleural mesothelioma.

Nine of the ten TxGNN-predicted indications in this pack belong to the mesothelioma/pericardial-tumour family, which is internally consistent with an antifolate mechanism plausible for mesothelial tumours. Two subtypes — malignant pleural mesothelioma (rank 10) and pleural epithelioid mesothelioma (rank 4) — are supported by the same Phase II trial evidence and reach evidence level L3/decision stage S1 ("Research Question"), while the remaining subtypes (biphasic, sarcomatoid, lymphohistiocytoid, peritoneal, well-differentiated papillary, pericardial) have no direct evidence and are held at L4 (mechanistic inference only).

It is worth noting the model's single highest-scoring prediction, pleural adenomatoid tumor, is **not** supported by this analysis: the rationale explicitly notes adenomatoid tumors are typically benign and do not require cytotoxic chemotherapy, and no clinical or literature evidence exists. Similarly, relapsing-remitting multiple sclerosis has no mechanistic or empirical support — pralatrexate's cytotoxic antifolate action is not equivalent to the immunomodulatory mechanism of low-dose methotrexate in autoimmune disease. For these reasons, malignant pleural mesothelioma — not the top TxGNN-scored candidate — is the indication carried forward in this report as the most defensible repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant pleural mesothelioma (no matching entries in `clinical_trials` or `ictrp_trials`; the supporting Phase II study below is captured only as a literature record, not a registered trial entry).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17409804](https://pubmed.ncbi.nlm.nih.gov/17409804/) | 2007 | Phase 2 Trial (single-arm) | Journal of Thoracic Oncology | Phase II trial of pralatrexate in unresectable malignant pleural mesothelioma; favorable toxicity profile (mainly stomatitis), demonstrated antitumor activity in mesothelioma cell lines/xenografts and in NSCLC patients |
| [21301589](https://pubmed.ncbi.nlm.nih.gov/21301589/) | 2010 | Review | Cancer Management and Research | Review of antifolate chemotherapy targeting folate synthesis (DHFR and related enzymes); positions pralatrexate within the broader antifolate drug class |
| [11595715](https://pubmed.ncbi.nlm.nih.gov/11595715/) | 2001 | Preclinical (animal/in vitro) | Clinical Cancer Research | Pralatrexate (PDX) showed 25–30× greater in vitro cytotoxic potency than methotrexate against human mesothelioma cell lines (VAMT-1, JMN), including combination activity with platinum agents |

---

## Saudi Arabia Market Information

Pralatrexate currently holds **no marketing authorization in Saudi Arabia** (`market_status: 未上市 / Not Marketed`, `total_licenses: 0`). No license, product, or approved-indication records are available in this evidence pack.

---

## Cytotoxicity

Pralatrexate is a cytotoxic antifolate/antimetabolite (DHFR inhibitor), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate/antimetabolite class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC (with differential), renal and hepatic function, mucositis/stomatitis monitoring (reported dose-limiting toxicity in PMID 17409804) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug–drug interaction data are all flagged as data gaps in this evidence pack — `safety.key_warnings`, `safety.contraindications` are unfilled, and the DDI query returned no results.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- TFDA/label-level safety data (warnings, contraindications) is a **Blocking** data gap (DG001) that explicitly prevents entry into the S1 safety pre-assessment stage; without it no repurposing candidate from this drug can advance regardless of efficacy evidence.
- Even for the best-supported indication (malignant pleural mesothelioma), evidence is limited to one completed Phase II single-arm trial plus supportive preclinical/review literature (L3) — insufficient on its own to justify "Go," but sufficient to justify further investigation rather than outright rejection.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications) — required to clear the Blocking data gap (DG001)
- Confirmed mechanism-of-action and original approved-indication data (DG002)
- DDI profile (current query returned no results)
- If pursuing malignant/epithelioid pleural mesothelioma specifically: updated search for any newer randomized trials beyond the single 2007 Phase II study, and confirmation of activity by histologic subtype (the existing trial did not stratify results by subtype)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

