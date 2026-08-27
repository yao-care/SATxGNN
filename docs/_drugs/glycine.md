---
layout: default
title: Glycine
parent: 僅模型預測 (L5)
nav_order: 297
evidence_level: L5
indication_count: 2
---

# Glycine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Glycine: From No Established Indication to Nasal Cavity Disease

## One-Sentence Summary

Glycine currently has no recorded original indication or approved product in this evidence pack — it is an amino acid known pharmacologically as an inhibitory neurotransmitter and NMDA receptor co-agonist. The TxGNN model predicts potential efficacy for **Nasal Cavity Disease**, but the supporting evidence is weak: the single clinical trial and both literature records were independently graded as irrelevant or only tangentially related to this drug-disease pair.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No original indication data available |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for glycine. Based on known pharmacology, glycine acts as an inhibitory neurotransmitter and as a co-agonist at the NMDA receptor; no established anti-inflammatory or mucosal-repair mechanism is documented that would plausibly connect it to nasal cavity disease.

No original indication is recorded for this drug in the current evidence pack, so a mechanistic bridge between "original use" and "predicted new indication" cannot be constructed. The high TxGNN score (99.85%) reflects graph-embedding similarity within the knowledge graph rather than a validated pharmacological or clinical rationale.

Reviewer annotations on the supporting evidence reinforce this caution: the one retrieved clinical trial was graded "C" relevance (an unrelated PET-imaging biomarker study in cancer patients, only coincidentally touching head-and-neck anatomy), and both literature records were classified as low-tier, off-target findings (bovine nasal mucosa histochemistry; polymer-based mucosal vaccine adjuvants). Neither line of evidence actually studies glycine's effect on nasal cavity disease.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1/2 | Completed | 25 | Evaluated the 18F-FPPRGD2 PET radiopharmaceutical for imaging αvβ3 integrin/angiogenesis in GBM, gynecological cancer, and renal cell carcinoma patients under antiangiogenic therapy. Not a glycine or nasal-disease study; flagged as irrelevant (Grade C), likely surfaced only via incidental head/neck cancer enrollment. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | Preclinical | Chemical & Pharmaceutical Bulletin | Investigated oligoarginine-polymer conjugates as nasal mucosal vaccine adjuvants in mice; unrelated to glycine. |
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Other (histochemistry) | Veterinary Pathology | Lectin histochemistry of normal vs. herpesvirus-infected bovine nasal mucosa; a basic veterinary pathology study, not a glycine or human-disease study. |

## Saudi Arabia Market Information

Glycine is not currently marketed in Saudi Arabia; no product authorizations are on record.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack — this is flagged as a blocking data gap, DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN similarity score, none of the retrieved clinical trial or literature evidence actually supports glycine's use in nasal cavity disease — both were independently graded as off-target. Combined with the absence of MOA and original-indication data, there is no mechanistic or clinical basis to advance this candidate at this time.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (blocking gap, DG001)
- Verified mechanism of action data for glycine (DG002)
- Literature or trial evidence that directly studies glycine (not incidental keyword matches) in nasal or upper-airway conditions

*Note: A second, similarly weak candidate was also predicted — **acute laryngopharyngitis** (TxGNN score 99.84%, rank 3409, Evidence Level L5). Its only supporting literature record (PMID 21617577) studies sivelestat, an unrelated neutrophil elastase inhibitor, in acute lung injury — not glycine. This candidate carries the same "Hold" recommendation for the same reasons.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

