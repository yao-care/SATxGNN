---
layout: default
title: Dienogest
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
---

# Dienogest
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

# Dienogest: From Endometriosis to Amenorrhea

## One-Sentence Summary

Dienogest is a fourth-generation progestin widely used for endometriosis treatment, exerting its effects through progesterone receptor agonism and suppression of the hypothalamic–pituitary–gonadal (HPG) axis.

The TxGNN model predicts it may be effective for **Amenorrhea**, with **4 clinical trials** and **6 publications** currently associated with this direction — however, a critical interpretive caveat applies: amenorrhea in this context is a well-documented **pharmacological side effect** of dienogest (occurring in 50–70% of users), not an established therapeutic target, suggesting the model may have captured a reversed causal relationship.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Endometriosis (established from clinical trial and literature context; no Saudi Arabia registration) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Dienogest acts as a selective progesterone receptor agonist with high oral bioavailability and minimal androgenic activity. Its primary mechanism involves suppression of the HPG axis — reducing LH and FSH secretion, lowering circulating estrogen, and directly inhibiting ectopic endometrial cell proliferation and survival. This makes it highly effective for endometriosis-associated pain and lesion control.

As a direct consequence of this HPG suppression, dienogest reliably induces amenorrhea in a substantial proportion of treated women. The 2026 mechanistic study (PMID 41329046) explicitly states that "inducing amenorrhoea and a hypoestrogenic environment" is the intended therapeutic objective of dienogest in endometriosis — confirming that amenorrhea is the pharmacological mechanism, not the target indication. TxGNN's biological knowledge graph almost certainly captured this strong co-occurrence between dienogest and amenorrhea and scored it as a repurposing signal.

Critically, the causal direction is reversed from a repurposing standpoint. Treating primary amenorrhea (hypothalamic, pituitary, or structural origin) or secondary amenorrhea with additional HPG suppression would be pharmacologically counterproductive in most etiologies. A narrow diagnostic use case exists — the progesterone challenge test for assessing estrogen priming in secondary amenorrhea workup — but this is a diagnostic tool, not a therapeutic indication. Before any further development consideration, the specific amenorrhea subtype and clinical context must be defined.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A | Completed | 968 | Real-world observational study of dienogest (Visanne) for endometriosis in routine clinical practice; amenorrhea tracked as a secondary safety endpoint, reflecting a known side effect rather than a therapeutic target |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A | Completed | 895 | Prospective cohort study in Asian women with endometriosis assessing quality-of-life improvement and long-term safety; amenorrhea rate reported as a tolerability finding |
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Phase 3 | Recruiting | 290 | Non-inferiority Phase 3 trial comparing Indinol Forto® 200 mg vs. Visanne 2 mg for endometriosis treatment; amenorrhea not a primary endpoint |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | Active, not recruiting | 138 | Comparison of transdermal estradiol add-back with dienogest vs. drospirenone for bone protection in endometriosis; designed to mitigate dienogest-induced hypoestrogenism, not to treat amenorrhea |

> **Important**: All 4 identified trials target endometriosis as the primary indication. Amenorrhea appears exclusively as a secondary safety or tolerability endpoint — reflecting a drug-induced side effect — in none of these trials is amenorrhea the therapeutic target being treated.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematic Review / Meta-analysis | BMC Pharmacology & Toxicology | Bayesian analysis of dienogest adverse effects; irregular bleeding and amenorrhea confirmed as among the most prevalent adverse events, quantifying their pharmacological — not therapeutic — role |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Narrative Review | Reviews in Endocrine & Metabolic Disorders | Comprehensive review of hormonal treatments for endometriosis; frames estrogen dependency and progesterone resistance as the core disease drivers, providing mechanistic context for dienogest's HPG suppression strategy |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Clinical / Mechanistic Study | European Journal of Contraception & Reproductive Health Care | Demonstrates high inhibition ratio and transformation index for 2 mg dienogest; explicitly identifies inducing amenorrhea and a hypoestrogenic environment as the treatment objective in endometriosis, confirming reversed causation relative to the TxGNN prediction |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Cohort Study | Reproductive Sciences | Retrospective cohort of 514 women with ovarian endometrioma on long-term dienogest (>12 months); amenorrhea and breakthrough bleeding patterns documented as key long-term tolerability outcomes |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Case Report | Medicine | Case report of ovarian granulosa cell tumor in a PCOS patient; tangential association with amenorrhea context, no direct relevance to dienogest repurposing |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Review | Journal of Pediatric and Adolescent Gynecology | Advanced visualization for Müllerian anomalies; relevant as obstructive anomalies are a structural cause of primary amenorrhea — where hormonal therapy such as dienogest would have no role |

## Saudi Arabia Market Information

Dienogest currently has **no approved product registrations** with the Saudi Food and Drug Authority (SFDA). No marketed formulations exist in Saudi Arabia at this time, and accordingly no authorized indication data is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model has identified a pharmacologically real — but directionally reversed — association: dienogest reliably *induces* amenorrhea as a high-incidence side effect (50–70%) through HPG axis suppression, rather than serving as a treatment *for* amenorrhea as a primary disease state. All 4 clinical trials and the 6 publications identified support the endometriosis indication, with amenorrhea appearing only as a secondary safety endpoint. There is no clinical trial or literature evidence supporting dienogest as a therapeutic agent for primary or secondary amenorrhea of other etiologies, and pharmacological reasoning suggests it would be counterproductive in most amenorrhea subtypes.

**To proceed, the following is needed:**
- Formal clarification of the clinical question: is there a specific amenorrhea subtype (e.g., progesterone challenge test in secondary amenorrhea diagnosis) where dienogest's HPG-suppressive effect could be used constructively?
- SFDA product registration and local package insert retrieval to complete safety evaluation (currently a blocking data gap)
- MOA documentation from DrugBank to support mechanistic plausibility analysis
- If the primary endometriosis indication is pursued first (as recommended), the amenorrhea repurposing signal can be reconsidered in the context of any future indication expansion after market entry is established
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

