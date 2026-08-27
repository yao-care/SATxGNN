---
layout: default
title: Trabectedin
parent: 僅模型預測 (L5)
nav_order: 630
evidence_level: L5
indication_count: 1
---

# Trabectedin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Trabectedin: From Soft Tissue Sarcoma / Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

> Trabectedin is a DNA minor-groove-binding cytotoxic agent originally developed for soft tissue sarcoma and, in combination with pegylated liposomal doxorubicin (PLD), relapsed platinum-sensitive ovarian cancer.
> The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**, with **2 clinical trials** (neither directly in breast cancer) and **no dedicated literature** currently supporting this direction — evidence rests mainly on a mechanistic/synthetic-lethality rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Soft tissue sarcoma; relapsed platinum-sensitive ovarian cancer (combination therapy) — not confirmed against a Saudi Arabia label since the product is not marketed there |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data was not returned by DrugBank for this candidate ([Data Gap]), but the repurposing rationale supplied with the evidence pack describes the relevant biology directly: Trabectedin is a DNA minor-groove-binding alkylator that traps and degrades the RNA polymerase II complex during transcription-coupled nucleotide excision repair (TC-NER), producing DNA double-strand breaks. In tumors with homologous recombination (HR) deficiency — most notably BRCA1/2-mutated tumors — this damage is poorly repaired, and combination with a PARP inhibitor (e.g., olaparib) can produce a synthetic-lethal effect.

This mechanism is already clinically exploited in ovarian cancer, where trabectedin + PLD is an established option in the platinum-sensitive relapsed, BRCA-associated setting. Breast and ovarian cancer share a substantial overlap in BRCA1/2-driven tumor biology, which gives a plausible mechanistic bridge to female breast carcinoma, particularly BRCA-mutated or HR-deficient subtypes.

However, the supporting evidence for breast cancer specifically is currently limited to an in vitro cell-line observation (trabectedin + olaparib synergy) cited in the rationale narrative — no clinical trial or published study in human breast cancer patients was identified in this evidence pack. The prediction should therefore be read as a mechanism-driven hypothesis rather than a clinically validated signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03470805](https://clinicaltrials.gov/study/NCT03470805) | Phase 2 | Completed | 9 | Olaparib maintenance after response to trabectedin + PLD in recurrent, BRCA-associated ovarian cancer (EMA-approved PARPi maintenance setting). Small single-arm study; population is ovarian, not breast, cancer — relevance is via BRCA/HR-deficiency mechanism analogy only. |
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Phase 2 | Completed | 76 | Single-dose QTc/ECG safety study of trabectedin in advanced solid tumors (general oncology population, not breast-cancer specific). Provides systemic cardiac-safety context only, no efficacy signal for breast cancer. |

*Note: Neither trial directly studies trabectedin in female breast carcinoma; both are included because they were the top-ranked evidence returned for this prediction, graded "C" relevance in the source evidence pack.*

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Trabectedin is not currently marketed in Saudi Arabia (0 authorizations on record).

---

## Cytotoxicity

Trabectedin is a marine-derived antineoplastic agent (ecteinascidin class, DNA minor-groove-binding alkylator), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA minor-groove-binding alkylating agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Cytotoxic drug handling precautions required (hazardous drug) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is currently mechanistic/preclinical only (L4) — the two available trials do not directly study breast cancer, and no breast-cancer literature was found. A Blocking data gap on TFDA package insert warnings/contraindications also prevents any S1 safety evaluation, and the drug is not marketed in Saudi Arabia.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed original MOA and indication data from DrugBank (DG002)
- Direct clinical or in vivo preclinical evidence of trabectedin activity in female breast carcinoma (current support is limited to an in vitro cell-line observation)
- Drug-drug interaction (DDI) data, currently not found
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

