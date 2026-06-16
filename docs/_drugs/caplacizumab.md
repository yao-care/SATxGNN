---
layout: default
title: Caplacizumab
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
---

# Caplacizumab
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

# Caplacizumab: From Anti-vWF Nanobody to Thrombotic Thrombocytopenic Purpura

## One-Sentence Summary

Caplacizumab is a humanized bivalent anti-von Willebrand factor (vWF) nanobody, globally approved as the first targeted therapy for acquired thrombotic thrombocytopenic purpura (aTTP), but currently not marketed in Saudi Arabia.
The TxGNN model predicts it may be effective for **Thrombotic Thrombocytopenic Purpura (TTP)** — confirming its established mechanism and positioning it as a priority candidate for Saudi Arabia market introduction — with **14 clinical trials** and **20 publications** currently supporting this direction.
While TxGNN's highest-scored novel prediction is "primary release disorder of platelets," the most clinically actionable and evidence-supported indication remains TTP, where the mechanistic fit is near-perfect.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acquired TTP (aTTP) — inferred from global approval context; no Saudi Arabia registration on record |
| Predicted New Indication | Thrombotic Thrombocytopenic Purpura (TTP) |
| TxGNN Prediction Score | 99.9965% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the DrugBank record for this report. Based on information embedded in the clinical evidence and repurposing rationale, caplacizumab is a bivalent variable-domain-only immunoglobulin fragment (nanobody) that directly targets the **A1 domain of von Willebrand factor (vWF)**, blocking the interaction between ultra-large vWF multimers and the platelet surface receptor GPIbα. This mechanistically interrupts the pathological platelet adhesion step that initiates microvascular thrombosis.

In acquired TTP, an immune-mediated deficiency of ADAMTS13 — the specific vWF-cleaving protease — allows uncleaved ultra-large vWF multimers to accumulate in the circulation. These multimers trigger unrestrained platelet binding, resulting in disseminated microvascular thrombosis, severe thrombocytopenia, microangiopathic hemolytic anemia, and potentially fatal ischemic end-organ damage involving the brain, heart, and kidneys. The mechanistic alignment between caplacizumab's target and TTP's core pathophysiology is direct and well-characterized: the drug specifically neutralizes the triggering event (vWF–GPIbα adhesion) upstream of downstream organ injury.

Caplacizumab (Cablivi®) has been approved in the European Union (2018), United States (2019), Japan (2021), and multiple other jurisdictions as the first targeted anti-adhesive therapy for aTTP, used in combination with plasma exchange and immunosuppression. The absence of any Saudi Arabia regulatory registration represents a gap in access to what international guidelines (ISTH 2020, 2025) now describe as an essential component of standard of care. TxGNN's prediction score of 99.9965% reflects high network-level connectivity between caplacizumab and the TTP disease node in the biomedical knowledge graph.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01151423](https://clinicaltrials.gov/study/NCT01151423) | Phase 2 | Completed | 75 | TITAN trial: Single-blind, placebo-controlled RCT in aTTP patients; directly validated efficacy with reduced time to platelet response and fewer exacerbations versus placebo on top of standard plasma exchange |
| [NCT02553317](https://clinicaltrials.gov/study/NCT02553317) | Phase 3 | Completed | 145 | HERCULES trial: Double-blind, placebo-controlled RCT; evaluated caplacizumab in more rapidly restoring normal platelet counts and preventing further microvascular thrombosis — pivotal registration study |
| [NCT05468320](https://clinicaltrials.gov/study/NCT05468320) | Phase 3 | Completed | 51 | Open-label single-arm multicenter study confirming efficacy and safety of caplacizumab + immunosuppression WITHOUT first-line therapeutic plasma exchange in iTTP; extends treatment options |
| [NCT04074187](https://clinicaltrials.gov/study/NCT04074187) | Phase 2/3 | Completed | 21 | Japanese bridging study evaluating caplacizumab for prevention of aTTP recurrence in Asian patients; directly supports regional/local approval pathways |
| [NCT02878603](https://clinicaltrials.gov/study/NCT02878603) | Phase 3 | Completed | 104 | Post-HERCULES long-term follow-up; evaluated sustained safety, repeated-use efficacy, and long-term disease impact of caplacizumab |
| [NCT05876221](https://clinicaltrials.gov/study/NCT05876221) | N/A (Observational) | Completed | 223 | Real-world study of platelet response dynamics under caplacizumab in iTTP; 223 patients, provides insights on platelet count interpretation and treatment pitfalls |
| [NCT06291025](https://clinicaltrials.gov/study/NCT06291025) | N/A (Single-arm) | Recruiting | 131 | Multicenter prospective study evaluating caplacizumab + immunosuppression + plasma infusion without therapeutic plasma exchange; may further expand treatment pathway accessibility |
| [NCT04720261](https://clinicaltrials.gov/study/NCT04720261) | Phase 2 | Terminated | 58 | Personalized caplacizumab regimen guided by ADAMTS13 activity monitoring; terminated early, provides interim data on biomarker-guided dosing strategy |
| [NCT04985318](https://clinicaltrials.gov/study/NCT04985318) | N/A (Observational) | Recruiting | 350 | German national prospective real-world registry; describes prescription patterns, outcome predictors, and treatment algorithms in iTTP |
| [NCT05262881](https://clinicaltrials.gov/study/NCT05262881) | N/A (Retrospective) | Unknown | 50 | ROSCAPLI Italian experience: retrospective multicenter study of aTTP patients treated with caplacizumab + plasma exchange + immunosuppression |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [30625070](https://pubmed.ncbi.nlm.nih.gov/30625070/) | 2019 | Phase 3 RCT | N Engl J Med | HERCULES trial: Caplacizumab significantly reduced time to platelet count response, TTP-related mortality composite, and rate of exacerbation/major thromboembolic events versus placebo |
| [26863353](https://pubmed.ncbi.nlm.nih.gov/26863353/) | 2016 | Phase 2 RCT | N Engl J Med | TITAN trial: Caplacizumab reduced platelet-count response time and exacerbation rate in aTTP; established the mechanistic proof-of-concept for vWF blockade |
| [40533296](https://pubmed.ncbi.nlm.nih.gov/40533296/) | 2025 | Clinical Practice Guideline Update | J Thromb Haemost | 2025 ISTH focused update on TTP management; incorporates latest evidence and updates caplacizumab use recommendations |
| [32914526](https://pubmed.ncbi.nlm.nih.gov/32914526/) | 2020 | Clinical Practice Guideline | J Thromb Haemost | ISTH 2020 treatment guidelines for TTP; evidence-based framework recommending caplacizumab as standard of care |
| [32914582](https://pubmed.ncbi.nlm.nih.gov/32914582/) | 2020 | Clinical Practice Guideline | J Thromb Haemost | ISTH 2020 diagnostic guidelines for TTP; defines ADAMTS13 activity thresholds and diagnostic workup |
| [36053773](https://pubmed.ncbi.nlm.nih.gov/36053773/) | 2023 | Systematic Review & Meta-analysis | Blood Advances | Pooled analysis of RCTs and real-world studies of caplacizumab added to standard of care; confirms benefit across diverse populations and study designs |
| [37045600](https://pubmed.ncbi.nlm.nih.gov/37045600/) | 2023 | Systematic Review & Meta-analysis | Expert Rev Hematol | Comprehensive meta-analysis of caplacizumab efficacy and safety in TTP across multiple populations |
| [40235949](https://pubmed.ncbi.nlm.nih.gov/40235949/) | 2025 | International Multicenter Cohort | EClinicalMedicine | Capla 1000+ project: large international real-world cohort (>1,000 patients) evaluating mortality impact and optimal timing of caplacizumab initiation |
| [34266669](https://pubmed.ncbi.nlm.nih.gov/34266669/) | 2022 | Expert Consensus | Medicina Clinica | Spanish expert recommendations on TTP diagnosis and treatment; includes practical caplacizumab use guidance |
| [40388146](https://pubmed.ncbi.nlm.nih.gov/40388146/) | 2025 | Narrative Review | JAMA | Comprehensive 2025 JAMA review of iTTP covering pathophysiology, diagnosis, and treatment; reflects current clinical consensus |

---

## Saudi Arabia Market Information

Caplacizumab currently holds **no registered licenses in Saudi Arabia**. There are no approved products, dosage forms, or authorized indications on record. The drug is entirely absent from the local market.

---

## Safety Considerations

Safety data from a Saudi Arabia (SFDA) package insert is unavailable as the drug has not been registered locally. Based on the globally published evidence:

- **Bleeding risk**: Caplacizumab inhibits vWF-mediated platelet adhesion, which may increase bleeding tendency. Caution is required when co-administered with anticoagulants or antiplatelet agents.
- **No drug-drug interaction data** was identified in the DDI database query for this report.

Please refer to the approved package inserts from the EU (EMA), US (FDA), or Japan (PMDA) for complete safety information including full warnings, precautions, and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Caplacizumab has robust L1 evidence supporting its use in TTP, anchored by two pivotal randomized controlled trials (TITAN Phase 2, HERCULES Phase 3), a completed Phase 3 single-arm study, an Asian bridging study, multiple systematic meta-analyses, and definitive international clinical guidelines (ISTH 2020 and 2025 update) that now position it as a cornerstone of standard care. The drug's absence from Saudi Arabia represents a critical unmet access need for a proven life-saving therapy in a rare, rapidly fatal disease.

**To proceed, the following is needed:**

- **Regulatory dossier submission**: File an SFDA market authorization application leveraging the existing EU/FDA/PMDA approved dossiers under mutual recognition or abridged pathways
- **Safety package**: Obtain and translate the full package insert (warnings, contraindications, special populations) from approved markets for SFDA review
- **MOA documentation**: Compile formal mechanism of action data from DrugBank and published pharmacology literature to complete regulatory submission requirements
- **Local clinical network**: Identify Saudi Arabia hematology centers with TTP patient populations and ADAMTS13 testing capability
- **Pharmacovigilance plan**: Develop a post-marketing surveillance plan compliant with SFDA requirements for rare disease biologics
- **Access bridge**: Explore compassionate use or named-patient access program while formal approval is pending, given the life-threatening nature of TTP
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

