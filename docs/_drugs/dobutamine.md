---
layout: default
title: Dobutamine
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 10
---

# Dobutamine
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

# Dobutamine: From Acute Heart Failure to Alopecia

## One-Sentence Summary

Dobutamine is a synthetic catecholamine and selective β₁-adrenergic receptor agonist, widely used clinically for acute heart failure and cardiogenic shock — though no regulatory records were found in the Saudi Arabia licensing database for this review.
The TxGNN model predicts it may be effective for **Alopecia**, with **0 clinical trials** and **2 publications** currently retrieved for this indication.
However, neither publication directly supports dobutamine as a treatment for hair loss; the evidence base is purely model-derived.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute heart failure / cardiogenic shock (established clinical use; no Saudi Arabia regulatory record found) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dobutamine is a synthetic catecholamine that acts primarily as a β₁-adrenergic receptor agonist, increasing cardiac contractility and output. It is used intravenously in acute settings — cardiogenic shock, acute decompensated heart failure, and dobutamine stress echocardiography. Its mechanism of action data was not available in the linked DrugBank record at the time of this review, but its pharmacological class and clinical role are well established.

The KG (Knowledge Graph) prediction path reconstructed from the evidence is: **minoxidil (a hair-loss treatment drug) → cardiovascular side effects → dobutamine (supportive inotropic therapy for those side effects)**. This is an indirect, triangulated graph link — it reflects the fact that minoxidil intoxication can cause heart failure requiring dobutamine support, not that dobutamine itself acts on hair follicles.

No direct biological mechanism links β₁-adrenergic stimulation to hair follicle biology. The β-adrenergic system does interact with dermal papilla cells to some degree, but the evidence for β₁ agonism as a driver of hair growth is absent from the literature. The prediction is most likely a graph artifact from disease-node co-clustering rather than a pharmacologically meaningful signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Case Report (Veterinary) | Journal of Veterinary Cardiology | Cat with minoxidil intoxication-induced congestive heart failure; dobutamine used for hemodynamic support, not for alopecia treatment |
| [17505274](https://pubmed.ncbi.nlm.nih.gov/17505274/) | 2007 | Case Report | Pediatric Emergency Care | Pediatric colchicine poisoning; hair loss described as a phase-3 recovery symptom, dobutamine not mentioned as a hair treatment |

> ⚠️ **Note:** Neither publication supports dobutamine as a treatment for alopecia. Both were retrieved incidentally due to co-occurrence of hair-related terms and dobutamine in the context of toxicological emergencies.

---

## Saudi Arabia Market Information

No registered products found in the Saudi Arabia licensing database for Dobutamine.

> Dobutamine is nonetheless used clinically worldwide as an intravenous inotropic agent, typically dispensed in hospital/ICU settings under generic formulations. The absence of a formal Saudi Arabia license record may reflect that registration was not pursued or that it is supplied via hospital procurement channels without retail registration.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction records were available in this Evidence Pack.

> ⚠️ **Known clinical context (for reviewer reference):** Dobutamine is a potent cardiovascular agent. Common risks include tachyarrhythmia, hypertension, and increased myocardial oxygen demand. It is contraindicated in hypertrophic obstructive cardiomyopathy and should be used with caution in patients with atrial fibrillation. Detailed package insert review is essential before any repurposing evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for dobutamine → alopecia is a spurious Knowledge Graph artifact, arising from an indirect path through minoxidil's cardiovascular side effects rather than any direct mechanistic link between dobutamine and hair follicle biology. No clinical trials, no disease-relevant literature, and no pharmacological rationale support this repurposing candidate. Furthermore, the β₁-agonist mechanism of dobutamine is theoretically antagonistic to the vasodilatory mechanism by which minoxidil is thought to promote hair growth.

**To proceed (if further evaluation is desired despite Hold recommendation):**
- Obtain DrugBank MOA data to confirm absence of any hair follicle receptor interactions
- Search primary literature for any β-adrenergic agonist effects on dermal papilla or hair cycle regulation
- Review the full KG edge path in the TxGNN model to confirm and document the indirect minoxidil → dobutamine routing as a model limitation
- Consider flagging this candidate as a **KG false positive** in the pipeline's triage log, to improve future prediction filtering
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

