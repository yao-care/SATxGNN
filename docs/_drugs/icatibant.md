---
layout: default
title: Icatibant
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 7
---

# Icatibant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Icatibant: From No Registered Indication in Saudi Arabia to C1 Inhibitor Deficiency (Hereditary Angioedema)

## One-Sentence Summary

Icatibant is not currently marketed in Saudi Arabia, and no approved original indication is on file for it there. The TxGNN model predicts it may be effective for **C1 inhibitor deficiency** (hereditary angioedema, HAE), a use already extensively supported worldwide, with **23 clinical trials** and **20 publications** currently backing this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Icatibant is not marketed in Saudi Arabia and no approved indication is on file |
| Predicted New Indication | C1 inhibitor deficiency (Hereditary Angioedema) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data was not returned for this evidence pack, but the mechanism can be reconstructed directly from the clinical trial descriptions included here: Icatibant is a selective **bradykinin B2 receptor antagonist**. It blocks the B2 receptor, counteracting the vascular permeability and tissue swelling caused by excess bradykinin — the effector molecule that accumulates when C1 esterase inhibitor (C1-INH, gene *SERPING1*) is deficient or dysfunctional. This bradykinin excess is the core pathophysiology of hereditary angioedema.

Importantly, the "predicted" indication here is not a novel disease association discovered by the model — it is icatibant's own long-established, globally approved indication. Multiple trials in this evidence pack (e.g., NCT00097695, NCT00912093) explicitly describe icatibant as an existing treatment for acute HAE attacks, and the drug is marketed elsewhere under brand names including Firazyr and Icanticure. The gap is regulatory, not scientific: icatibant simply has no market authorization in Saudi Arabia yet.

Because the predicted indication and the drug's real-world mechanism are directly aligned (B2 receptor blockade ↔ bradykinin-driven angioedema), the extremely high TxGNN score (99.99%) is consistent with a model correctly recovering a well-validated drug-disease relationship rather than proposing a speculative new use. This strengthens confidence in the prediction but also reframes the decision as one of **market registration/access** rather than novel repurposing risk.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00097695](https://clinicaltrials.gov/study/NCT00097695) | Phase 3 | Completed | 84 | Pivotal double-blind, placebo-controlled RCT of subcutaneous icatibant for acute cutaneous/abdominal HAE attacks |
| [NCT00912093](https://clinicaltrials.gov/study/NCT00912093) | Phase 3 | Completed | 98 | Randomized, double-blind, placebo-controlled RCT confirming efficacy/safety of icatibant in acute HAE attacks |
| [NCT00500656](https://clinicaltrials.gov/study/NCT00500656) | Phase 3 | Completed | 85 | RCT comparing subcutaneous icatibant vs. oral tranexamic acid for HAE attacks |
| [NCT00997204](https://clinicaltrials.gov/study/NCT00997204) | Phase 3 | Completed | 151 | Open-label study of self-administered subcutaneous icatibant — safety, tolerability, convenience |
| [NCT01034969](https://clinicaltrials.gov/study/NCT01034969) | N/A | Completed | 1761 | Icatibant Outcome Survey (IOS) — large prospective observational registry of real-world icatibant/C1-INH use |
| [NCT03888755](https://clinicaltrials.gov/study/NCT03888755) | Phase 3 | Completed | 8 | Open-label study of icatibant efficacy, PK, and safety in Japanese HAE patients |
| [NCT01386658](https://clinicaltrials.gov/study/NCT01386658) | Phase 3 | Completed | 32 | PK, tolerability, and safety of single-dose icatibant in children and adolescents with HAE |
| [NCT04654351](https://clinicaltrials.gov/study/NCT04654351) | Phase 3 | Completed | 2 | Safety, efficacy, and PK of subcutaneous icatibant in Japanese children/adolescents with HAE |
| [NCT04057131](https://clinicaltrials.gov/study/NCT04057131) | N/A | Completed | 179 | FIRAZYR post-marketing drug-use survey in Japan — real-world safety/efficacy |
| [NCT06346899](https://clinicaltrials.gov/study/NCT06346899) | N/A | Completed | 115 | Real-world observational study of icatibant (and lanadelumab) effectiveness/safety in China |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23420425](https://pubmed.ncbi.nlm.nih.gov/23420425/) | 2013 | Systematic Review | Pneumonologia i Alergologia Polska | Comparative clinical effectiveness of conestat alfa, C1-INH, and icatibant for acute HAE attacks |
| [35662289](https://pubmed.ncbi.nlm.nih.gov/35662289/) | 2022 | Registry Analysis | Clin Exp Allergy | Registry-based analysis of icatibant and C1-inhibitor use for laryngeal HAE attacks |
| [22686628](https://pubmed.ncbi.nlm.nih.gov/22686628/) | 2012 | Observational | Allergy | Real-world use of icatibant in acquired C1-inhibitor deficiency (off-label) |
| [34965883](https://pubmed.ncbi.nlm.nih.gov/34965883/) | 2021 | Observational (IOS Registry) | Allergy Asthma Clin Immunol | Real-world icatibant outcomes in Spanish HAE patients from the IOS registry |
| [35871284](https://pubmed.ncbi.nlm.nih.gov/35871284/) | 2023 | Retrospective Study | J Clin Pharmacol | Off-label prescribing patterns of C1-INH concentrates and icatibant in real-life practice |
| [30280305](https://pubmed.ncbi.nlm.nih.gov/30280305/) | 2018 | Case Series | J Clin Immunol | Treatment of HAE attacks with icatibant and recombinant C1 inhibitor during pregnancy |
| [29757016](https://pubmed.ncbi.nlm.nih.gov/29757016/) | 2018 | Review | Expert Rev Clin Immunol | Icatibant use in adolescents and children over 2 years with C1-INH-HAE |
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Review | J Investig Allergol Clin Immunol | Overview of current and emerging therapies for C1-INH-HAE, including icatibant |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Review | J Allergy Clin Immunol | Disease burden and treatment access for C1-INH-HAE in the Asia-Pacific region |
| [20496014](https://pubmed.ncbi.nlm.nih.gov/20496014/) | 2010 | Review | Intern Emerg Med | Overview of angioedema due to C1 inhibitor deficiency and treatment options |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The efficacy evidence for icatibant in C1 inhibitor deficiency (HAE) is exceptionally strong — this is icatibant's own established global indication, supported by multiple completed Phase 3 RCTs and a large multinational outcomes registry (>1,700 patients). However, a blocking data gap exists: no SFDA package insert/warnings data is available (DG001), and the drug currently holds no market authorization in Saudi Arabia, so a formal safety review cannot yet be completed.

**To proceed, the following is needed:**
- SFDA package insert warnings, precautions, and contraindications for icatibant (blocking gap, DG001)
- Confirmed DrugBank mechanism-of-action record (DG002)
- Saudi Arabia market registration/authorization pathway assessment, since the drug is not currently marketed there
- Local drug-drug interaction data, as none were found in the current query
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

