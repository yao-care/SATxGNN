---
layout: default
title: Ciprofloxacin
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 10
---

# Ciprofloxacin
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

# Ciprofloxacin: From Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Ciprofloxacin is a broad-spectrum fluoroquinolone antibiotic widely used for treating bacterial infections including urinary tract, respiratory, gastrointestinal, and skin infections.
The TxGNN model predicts it may have utility in **Diffuse Scleroderma**, with **0 clinical trials** and **2 publications** currently supporting this direction.
Evidence for this repurposing direction remains exploratory, anchored by a single small-cohort pilot trial and one observational study on antibiotic management of scleroderma-associated gut complications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (fluoroquinolone antibiotic class) |
| Predicted New Indication | Diffuse Scleroderma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, ciprofloxacin is a fluoroquinolone antibiotic that exerts its primary bactericidal effect by inhibiting bacterial DNA gyrase (GyrA/GyrB subunits) and topoisomerase IV (ParC/ParE subunits) — essential enzymes for bacterial DNA replication and repair. This mechanism underpins its broad-spectrum coverage against gram-negative and selected gram-positive organisms.

Beyond its antibacterial role, ciprofloxacin has been reported to possess antifibrotic properties — potentially inhibiting fibroblast proliferation and collagen synthesis through mechanisms distinct from its classical antibacterial action. Diffuse scleroderma (systemic sclerosis) is an autoimmune connective tissue disorder defined by progressive skin and visceral fibrosis, microvascular injury, and immune dysregulation. No currently approved pharmacological treatment effectively halts fibrosis, creating an unmet therapeutic need. This antifibrotic mechanistic link forms the primary biological rationale for the TxGNN model's high prediction score.

A secondary pathway involves small intestinal bacterial overgrowth (SIBO), which affects a substantial proportion of systemic sclerosis patients and drives symptoms such as chronic diarrhoea, malabsorption, and weight loss. Ciprofloxacin, as a proven broad-spectrum antibiotic, can address SIBO directly, providing indirect symptom relief in scleroderma patients with gastrointestinal involvement. It is important to note, however, that this represents a symptomatic application rather than disease modification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Clinical Pilot (Small Cohort RCT) | The Journal of Dermatology | Controlled, double-blind pilot trial evaluating oral ciprofloxacin as an antifibrotic agent in scleroderma patients; assessed whether ciprofloxacin reduces disease severity, providing the most direct evidence for this repurposing direction |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Observational/Diagnostic | British Journal of Rheumatology | 24 systemic sclerosis patients (6 with diffuse form) investigated for SIBO via jejunal aspiration; describes antibiotic treatment outcomes for malabsorption, supporting ciprofloxacin's indirect role in managing a key scleroderma complication |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Notable safety signal identified within this evidence pack:** Ciprofloxacin carries an FDA Black Box Warning for the risk of causing or exacerbating **peripheral neuropathy**, which may be irreversible. This is a critical consideration for any chronic or repeated-course use in a non-infectious indication such as scleroderma, and must be weighed explicitly against any potential antifibrotic benefit.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.87%), the current evidence base for ciprofloxacin in diffuse scleroderma consists of only 2 early-phase or observational publications with no registered clinical trials, placing this at Evidence Level L4 — insufficient to support clinical repurposing without further validation. The antifibrotic hypothesis is mechanistically plausible but remains unconfirmed by adequately powered prospective data.

**To proceed, the following is needed:**
- A properly powered randomized controlled trial explicitly evaluating ciprofloxacin's antifibrotic efficacy in diffuse scleroderma (building on the 2010 pilot study at PMID 20507401)
- Retrieval of detailed MOA data from DrugBank (DG002) to characterize the molecular targets underlying the reported antifibrotic activity
- Retrieval of SFDA package insert safety warnings and contraindications (DG001) before any S1 safety evaluation can be completed
- Clarification of whether antifibrotic dosing and treatment duration differ from standard antibacterial regimens
- Formal benefit-risk assessment accounting for ciprofloxacin's FDA Black Box Warning on peripheral neuropathy and known risks of tendinopathy and QT prolongation, which are particularly concerning in the context of chronic use
- Regulatory pathway analysis given that ciprofloxacin is currently not marketed in Saudi Arabia (0 SFDA authorizations), requiring a de novo registration strategy if clinical development proceeds

> **Multi-indication note:** This evidence pack evaluated 10 predicted indications. While diffuse scleroderma ranks highest by TxGNN score, two other indications carry substantially stronger clinical evidence: **Septicemic Plague** (L2 — completed Phase 2 RCT + multiple human RCTs, FDA-approved under Animal Rule; recommended: Proceed with Guardrails) and **Monoclonal Gammopathy** (L3 — multiple retrospective cohorts supporting prophylactic use in haematopoietic stem cell transplantation; recommended: Proceed with Guardrails). These should be prioritized in any parallel repurposing development strategy.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

