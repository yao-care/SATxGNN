---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 39
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan: From Pulmonary Arterial Hypertension to Pulmonary Arteriovenous Malformation

## One-Sentence Summary

Ambrisentan is a selective endothelin A (ETA) receptor antagonist approved in the US and EU for pulmonary arterial hypertension (PAH), though it currently holds no regulatory authorizations in Saudi Arabia.
The TxGNN model predicts it may be effective for **Pulmonary Arteriovenous Malformation (PAVM)**,
with **no clinical trials** and **1 case report** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Idiopathic / Hereditary Pulmonary Arterial Hypertension (approved in US/EU; not registered in Saudi Arabia) |
| Predicted New Indication | Pulmonary Arteriovenous Malformation |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, ambrisentan is a selective ETA receptor antagonist that blocks the effects of endothelin-1 (ET-1) — a potent vasoconstrictor and smooth muscle mitogen — on pulmonary arterial cells, thereby reducing pulmonary vascular resistance and inhibiting vascular remodeling. This is the mechanism by which it treats idiopathic PAH.

Pulmonary arteriovenous malformation (PAVM) most commonly arises in patients with hereditary hemorrhagic telangiectasia (HHT), a rare autosomal dominant condition. A small subset of HHT patients develop concurrent PAH, and ET-1 pathway dysregulation has been implicated in HHT-related pulmonary vascular remodeling. In this subpopulation, ETA antagonism could theoretically reduce pulmonary vascular resistance and slow vasculopathy progression.

However, the mechanistic link is indirect. PAVM is fundamentally a structural arteriovenous fistula — an abnormal direct communication between pulmonary arteries and veins — whose core pathophysiology (intrapulmonary right-to-left shunting) has no established causal relationship with ET-1 signaling. The TxGNN prediction likely reflects the HHT ↔ PAH ↔ ET-1 graph path rather than a tractable pharmacological target for PAVM itself. This connection is considered an indirect inference and does not constitute a validated therapeutic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Case Report | World Journal of Clinical Cases | A case of HHT with concurrent PAH; clinical course and treatment described; family genetic analysis performed. Highlights the rare comorbidity of HHT and PAH, but does not evaluate ambrisentan specifically in the setting of PAVM |

---

## Saudi Arabia Market Information

Ambrisentan currently holds no registered authorizations in Saudi Arabia. There are no approved products, dosage forms, or licensed indications available in the local regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for ambrisentan in pulmonary arteriovenous malformation consists of a single case report with no direct pharmacological link between ETA antagonism and PAVM pathology. The structural and hemodynamic nature of PAVM (fixed arteriovenous shunting) is not addressable by vasodilatory therapy alone, and no clinical trials have evaluated this indication.

> **Note on broader indication landscape:** While PAVM represents the highest-ranked TxGNN prediction by score, other predicted indications in this evidence pack carry substantially stronger clinical support. PAH associated with congenital heart disease (CHD-PAH, Rank 2) is rated **L1** with a completed Phase 3 study and 18 publications; PAH associated with connective tissue disease (CTD-PAH, Rank 4) is rated **L2** with 3 trials including a completed Phase 4 study; and PAH associated with HIV infection (Rank 6) is rated **L1** with a completed Phase 3 crossover RCT. These three indications carry a **"Proceed with Guardrails"** recommendation and may represent higher-priority candidates for regulatory submission or formulary consideration in Saudi Arabia.

**To proceed with PAVM, the following is needed:**
- Preclinical or mechanistic studies establishing a direct role for ET-1/ETA signaling in PAVM formation or progression (not merely in HHT-associated PAH)
- Case series or registry data specifically documenting outcomes of PAH-targeted therapies in HHT patients with confirmed PAVM
- Full mechanism of action documentation and pharmacokinetic profile for the relevant patient population
- Drug-drug interaction assessment, particularly for patients on concurrent HHT-related treatments
- Review of the package insert for contraindications relevant to patients with right-to-left shunting physiology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

