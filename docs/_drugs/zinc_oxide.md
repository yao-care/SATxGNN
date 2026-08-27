---
layout: default
title: Zinc Oxide
parent: 僅模型預測 (L5)
nav_order: 675
evidence_level: L5
indication_count: 5
---

# Zinc Oxide
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

# Zinc Oxide: From No Registered Indication to Acne

## One-Sentence Summary

Zinc oxide (DrugBank DB09321) currently has no approved indication on record and is not marketed under this entry. The TxGNN model predicts it may be effective for **Acne**, with **0 clinical trials** but **7 supporting publications** (mostly reviews and preclinical studies) currently identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on record (this DrugBank entry is currently not marketed) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for zinc oxide in this dataset. Based on general pharmacological knowledge, zinc ions have anti-inflammatory, antibacterial (including inhibitory activity against *Cutibacterium acnes*), and sebum-regulating properties, and zinc oxide is a common ingredient in topical dermatologic formulations (antibacterial, astringent, physical UV-blocking agent).

Acne vulgaris pathology involves inflammation, bacterial overgrowth, and excess sebum production — all mechanistic targets that zinc compounds are known to act on. This provides a plausible biological rationale for the TxGNN prediction linking zinc oxide to acne.

However, this specific DrugBank entry (DB09321) has no original indication or regulatory approval on record, so the "repurposing" framing here is more accurately a novel-use hypothesis grounded in the general pharmacology of zinc, rather than an extension from an already-approved use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29193602](https://pubmed.ncbi.nlm.nih.gov/29193602/) | 2018 | Review | Dermatologic Therapy | Reviews zinc's therapeutic potential in acne vulgaris, covering topical/systemic use and limitations of current standard-of-care therapies |
| [21342155](https://pubmed.ncbi.nlm.nih.gov/21342155/) | 2011 | Review | International Journal of Dermatology | Reviews unique physical properties of zinc oxide/titanium dioxide nanoparticles; notes nano-preparations under investigation as novel acne treatments |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Cohort (small clinical, split-face) | Skin Research and Technology | Split-face clinical and bioinstrumental assessment of management of mild inflammatory catamenial acne |
| [36888703](https://pubmed.ncbi.nlm.nih.gov/36888703/) | 2023 | Preclinical (microneedle/material engineering) | Science Advances | Ultrasound-triggered zinc-porphyrin metal-organic-framework microneedle patch developed for transdermal treatment of bacterial (P. acnes) acne |
| [31322532](https://pubmed.ncbi.nlm.nih.gov/31322532/) | 2019 | Preclinical (formulation development) | Georgian Medical News | Development of cosmetic powder formulations for acne treatment |
| [29284390](https://pubmed.ncbi.nlm.nih.gov/29284390/) | 2018 | Preclinical (material/textile application) | Current Medicinal Chemistry | Reviews ultrasonic functionalization of textiles with nanoparticle (including zinc-based) coatings for antimicrobial wound and acne skin care |
| [41033952](https://pubmed.ncbi.nlm.nih.gov/41033952/) | 2025 | Preclinical (piezoelectric/photocatalytic mechanism) | Science Bulletin | ZnO-based piezo-phototronic heterojunction material developed to selectively modulate skin microbiota by responding to *C. acnes* respiration activity |

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Retrieval of the TFDA/manufacturer package insert (warnings and contraindications) is flagged as a Blocking data gap (DG001) — this must be resolved before a formal safety pre-assessment (S1) can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.86%) and plausible mechanistic rationale (zinc's antibacterial/anti-inflammatory activity relevant to acne pathology), the evidence base consists only of reviews and preclinical/materials-science studies with no completed clinical trials — placing this candidate at evidence level L3, decision stage S1 ("Research Question"). Critically, this drug entry has no on-record original indication, is not currently marketed, and safety data (warnings/contraindications) is a Blocking data gap, preventing formal safety pre-assessment.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert data (warnings, contraindications) — Blocking gap (DG001)
- Confirmed mechanism of action (MOA) documentation — High-priority gap (DG002)
- Clarification of any original approved indication(s) for this DrugBank entry
- Design of early-phase clinical studies evaluating topical zinc oxide specifically for acne vulgaris
- No further action recommended on the remaining candidate indications (anorectal stricture, anal polyp, papillary conjunctivitis, postinfectious vasculitis) — all rated L5/S0/Hold with no supporting literature or clinical trials, most likely reflecting knowledge-graph topological noise rather than genuine biological signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

