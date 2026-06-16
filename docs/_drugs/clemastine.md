---
layout: default
title: Clemastine
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 6
---

# Clemastine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

The `txgnn-pipeline` skill covers pipeline management and deployment — not directly applicable to report generation here. Proceeding with the Evidence Pack report.

---

# Clemastine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Clemastine (Tavegyl®) is a first-generation H₁-receptor antihistamine classically used for allergic rhinitis and hypersensitivity reactions.
The TxGNN model predicts it may be effective for **Allergic Urticaria** with a near-perfect confidence score,
supported by **1 completed Phase 2 clinical trial** and **13 publications** in this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis and hypersensitivity reactions (no Saudi Arabia authorization on record) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank query. Based on known information, clemastine is a first-generation H₁-receptor competitive antagonist — it directly blocks histamine binding to H₁ receptors on vascular endothelium and sensory nerve endings, inhibiting the downstream cascade of mast cell degranulation that produces vasodilation, increased vascular permeability, pruritus, and wheal formation. This is the core pharmacological pathway through which all antihistamines act in urticaria.

Allergic urticaria is driven by IgE-mediated (or occasionally non-immunological) mast cell activation that releases histamine as its primary mediator. The mechanistic link between H₁ antagonism and urticaria symptom control is one of the most well-established relationships in clinical pharmacology, validated across five decades of comparative trials. Clemastine consistently served as the active reference comparator in head-to-head studies against loratadine, acrivastine, astemizole, and terfenadine — confirming it as a benchmark standard of care, not a new experimental agent.

A 2025 review (Soni & Kaur, *Naunyn-Schmiedeberg's Archives of Pharmacology*) further underscores that clemastine is gaining renewed research interest beyond antihistaminergic properties — including remyelination via M1 muscarinic receptor antagonism and potential anti-tumor activity — but for urticaria specifically, the mechanistic rationale is direct, strong, and fully validated by existing literature.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01154361](https://clinicaltrials.gov/study/NCT01154361) | Phase 2 | Completed | N/A | Multicenter, randomized, double-blind proof-of-concept study comparing subcutaneous icatibant versus a historical standard-therapy cohort treated with methylprednisolone 250 mg + **clemastine 2 mg** in ACE inhibitor–induced angioedema with urticaria. Clemastine formed the core of the active standard-of-care comparator arm, directly confirming its frontline clinical role in acute allergic angioedema/urticaria. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [40055203](https://pubmed.ncbi.nlm.nih.gov/40055203/) | 2025 | Review | Naunyn-Schmiedeberg's Arch Pharmacol | Patent landscape review (2015–2024) confirming clemastine's established use in allergic rhinitis and urticaria while identifying emerging therapeutic frontiers in neurodegeneration and oncology |
| [6119852](https://pubmed.ncbi.nlm.nih.gov/6119852/) | 1981 | Clinical / Comparative | Wisconsin Medical Journal | Direct patient evaluation of clemastine fumarate in allergic diseases; comparative assessment against other antihistamines |
| [2873823](https://pubmed.ncbi.nlm.nih.gov/2873823/) | 1986 | Observational / Cohort | Asian Pac J Allergy Immunol | 142 paediatric urticaria patients; 56.3% had prior urticaria history; antihistamines including clemastine used as standard treatment; half had associated angioedema |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review | Drugs | Acrivastine vs. clemastine RCT data in seasonal allergic rhinitis and chronic urticaria — acrivastine found similar in efficacy to clemastine, confirming clemastine as active benchmark |
| [7528133](https://pubmed.ncbi.nlm.nih.gov/7528133/) | 1994 | Review | Drugs | Large controlled trials of loratadine vs. clemastine in urticaria; loratadine shown as effective as clemastine — further validates clemastine's established efficacy standard |
| [2523301](https://pubmed.ncbi.nlm.nih.gov/2523301/) | 1989 | Review | Drugs | Preliminary loratadine review; loratadine (10 mg once daily) found superior to placebo and comparable to clemastine in chronic urticaria |
| [2859711](https://pubmed.ncbi.nlm.nih.gov/2859711/) | 1985 | Review | Z Hautkrankheiten | 39-trial analysis (>2,300 patients) showing astemizole superior to classical antihistamines including clemastine, terfenadine, and ketotifen in chronic urticaria — positions clemastine within the urticaria antihistamine hierarchy |
| [30838475](https://pubmed.ncbi.nlm.nih.gov/30838475/) | 2019 | Case Report | Drug Safety - Case Reports | Anaphylactic reaction with systemic urticaria and facial oedema — patient treated with **clemastine + prednisone**, full recovery documented; confirms clemastine's real-world frontline use |
| [4152119](https://pubmed.ncbi.nlm.nih.gov/4152119/) | 1971 | Clinical Study | Therapia Hungarica | Early clinical evaluation of clemastine (Tavegyl®) in allergic diseases; one of the foundational efficacy studies |
| [40456207](https://pubmed.ncbi.nlm.nih.gov/40456207/) | 2025 | Case Report | J Neurosurg Case Lessons | Intraoperative anaphylaxis managed with clemastine; illustrates continued frontline clinical use in acute allergic emergencies as of 2025 |

---

## Saudi Arabia Market Information

Clemastine is currently **not marketed** in Saudi Arabia. No SFDA authorizations are on record as of the data cutoff (2026-06-16). This report therefore evaluates the feasibility of pursuing an initial SFDA registration, with allergic urticaria as the primary target indication.

---

## Safety Considerations

Please refer to the package insert for safety information. SFDA label warnings and contraindication data were not retrievable in this data cycle, representing a blocking gap that must be resolved before a formal safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clemastine has a direct, well-validated mechanistic link to allergic urticaria through H₁ receptor antagonism, confirmed over five decades of comparative clinical trials that consistently used clemastine as the active reference standard. The completed Phase 2 trial (NCT01154361) further documents its use in acute allergic angioedema/urticaria management. While not currently registered in Saudi Arabia, the global efficacy and safety record is extensive.

**To proceed, the following is needed:**
- **Resolve blocking data gap**: Obtain full SFDA (or equivalent EMA/FDA) package insert to extract warnings, contraindications, and drug–drug interactions
- **Confirm MOA from DrugBank API**: Retrieve full pharmacodynamic and pharmacokinetic profile to complete mechanism-of-action analysis
- **Regulatory pathway scoping**: Determine whether an abbreviated SFDA registration pathway is available based on existing EMA/FDA approvals
- **Market positioning analysis**: Map the second-generation antihistamine landscape in Saudi Arabia (loratadine, cetirizine, fexofenadine) to define the clinical niche for a first-generation agent
- **Sedation risk assessment**: Evaluate the CNS sedation profile of first-generation antihistamines in the context of Saudi Arabia prescribing practices and occupational driving guidelines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

