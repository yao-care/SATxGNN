---
layout: default
title: Cyclopentolate
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 3
---

# Cyclopentolate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# CYCLOPENTOLATE: From Ophthalmic Use to Cauda Equina Syndrome

## One-Sentence Summary

Cyclopentolate is an antimuscarinic agent used in ophthalmology to induce mydriasis (pupil dilation) and cycloplegia (ciliary muscle paralysis) during eye examinations and procedures.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, with **0 clinical trials** and **0 publications** currently supporting this direction.
Evidence across all three predicted indications remains at the earliest exploratory stage (L5 — model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ophthalmic use (mydriasis and cycloplegia) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacological knowledge, Cyclopentolate is an antimuscarinic (anticholinergic) agent that competitively blocks muscarinic acetylcholine receptors. Its primary clinical use is ophthalmic — applied topically to produce pupil dilation and temporarily paralyze the ciliary muscle for refraction testing and intraocular examinations. It belongs to the same receptor class as systemic antimuscarinics (oxybutynin, solifenacin, dicyclomine) that treat bladder and gastrointestinal conditions.

Cauda equina syndrome (CES) is a compressive neurological emergency caused by damage to the bundle of nerve roots at the terminal end of the spinal cord. Its hallmark features are lower limb weakness, saddle anaesthesia, and loss of bladder and bowel control. The TxGNN model's high prediction score for this pairing most likely reflects shared knowledge graph nodes between CES-associated autonomic complications (neurogenic bladder, bowel dysfunction) and the antimuscarinic drug class — rather than a direct mechanistic link to CES itself.

Critically, CES is a mechanical compression injury that requires urgent surgical decompression. The underlying pathology is not driven by muscarinic receptor overactivation and cannot be addressed pharmacologically with antimuscarinics. While CES patients frequently develop secondary neurogenic bladder — a condition where antimuscarinics do have an established role — this does not constitute a repurposing rationale for CES as the primary target. The mechanistic connection is indirect and the clinical plausibility is low.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or published literature evidence supporting Cyclopentolate use in Cauda Equina Syndrome, and the mechanistic link is indirect — CES is a compressive mechanical emergency requiring surgery, not a condition driven by the muscarinic pathway that Cyclopentolate targets.

**To proceed, the following is needed:**
- Retrieve and confirm the full mechanism of action (MOA) from DrugBank (DG002)
- Retrieve package insert warnings and contraindications to complete the safety profile (DG001)
- Clarify whether the TxGNN signal is targeting CES itself or its secondary autonomic sequelae (e.g., neurogenic bladder)
- If interest pivots to the **#2 predicted indication (neurogenic bladder)**, note that established oral antimuscarinics (oxybutynin, solifenacin, tolterodine) already occupy this space with strong clinical evidence; a differentiated formulation or delivery strategy would be required to justify further development
- If interest pivots to the **#3 predicted indication (irritable bowel syndrome)**, note that oral antispasmodics (dicyclomine, hyoscine) are already available; Cyclopentolate's lack of an oral dosage form is a practical barrier requiring formulation development before any clinical study is feasible
- Consider de-prioritizing this candidate unless a novel administration route or unique selectivity advantage can be identified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

