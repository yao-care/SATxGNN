---
layout: default
title: Fidaxomicin
parent: 僅模型預測 (L5)
nav_order: 262
evidence_level: L5
indication_count: 9
---

# Fidaxomicin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Fidaxomicin: From Clostridioides difficile Infection to Staphylococcal Scalded Skin Syndrome

## One-Sentence Summary

Fidaxomicin is a narrow-spectrum macrocyclic antibiotic used clinically for *Clostridioides difficile* infection (CDI). The TxGNN model predicts possible efficacy in **Staphylococcal Scalded Skin Syndrome (SSSS)**, but this prediction is currently supported by **zero clinical trials** and **zero publications** — it is a model-only signal, and the drug's own antibacterial spectrum and pharmacokinetics argue against plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in evidence pack — `original_indications` and `licenses` are empty. Fidaxomicin's established clinical use is *Clostridioides difficile* infection (general pharmacological knowledge, not evidence-pack data) |
| Predicted New Indication | Staphylococcal Scalded Skin Syndrome (SSSS) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for fidaxomicin is not available in this evidence pack (flagged as data gap **DG002**, High severity). Based on general pharmacological knowledge, fidaxomicin inhibits bacterial RNA polymerase and is approved specifically for CDI because of its near-zero systemic absorption after oral dosing — the drug stays concentrated in the gut lumen, which is exactly what CDI treatment requires.

That same property is the core problem for this prediction. The evidence pack's own mechanistic assessment states that SSSS is caused by exfoliative toxins from *Staphylococcus aureus* and requires systemic anti-staphylococcal therapy. Fidaxomicin's antibacterial spectrum does not cover *S. aureus*, and its negligible oral bioavailability means it cannot reach the systemic concentrations a skin/soft-tissue toxin-mediated disease would require.

In short, the high TxGNN similarity score does not correspond to a plausible pharmacological pathway here — it more likely reflects graph-embedding proximity between infection-related disease nodes than an actual antimicrobial match. This assessment is consistent with the other 8 candidates in this batch (bullous impetigo, impetigo, botulism variants, vulvovaginal candidiasis, hordeolum, *S. aureus* pneumonia, punctate epithelial keratoconjunctivitis), all of which carry the same L5/S0/Hold status and, per the evidence pack's own rationale, similar mechanistic mismatches.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Fidaxomicin is currently **not marketed** in Saudi Arabia — 0 active SFDA authorizations, no licensed products on record.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests entirely on a TxGNN similarity score (L5, no clinical or literature support), and fidaxomicin's known antibacterial spectrum and pharmacokinetics are mechanistically incompatible with a staphylococcal toxin-mediated skin disease. All 9 predictions in this evidence pack share the same Hold/L5/S0 status, and several are explicitly flagged in the pack's own rationale as implausible (e.g., an antibacterial drug predicted for the fungal infection vulvovaginal candidiasis) — suggesting this candidate set largely reflects embedding-space artifacts rather than genuine repurposing signals.

**To proceed, the following is needed:**
- TFDA/SFDA package insert data (warnings, contraindications) — currently Blocking gap DG001
- Verified mechanism of action from DrugBank API — currently High severity gap DG002
- Any in-vitro or preclinical susceptibility data for fidaxomicin against *S. aureus*, if this specific indication is still to be pursued
- Independent pharmacological review of the full 9-candidate batch before committing further evaluation resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

