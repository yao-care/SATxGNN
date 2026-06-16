---
layout: default
title: Clotrimazole
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 3
---

# Clotrimazole
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

# Clotrimazole: From Topical Antifungal to Vulvovaginitis

## One-Sentence Summary

Clotrimazole is a broad-spectrum azole antifungal widely used globally for superficial fungal and yeast infections, including vulvovaginal candidiasis.
The TxGNN model predicts it may be effective for **Vulvovaginitis** (ranked #2 by score; ranked #1 by actionable evidence), supported by **22 clinical trials** and **20 publications** — making it the most evidence-backed repurposing candidate in this pack.
A secondary prediction for **Acne** (ranked #1 by TxGNN score) and **Postmenopausal Atrophic Vaginitis** (ranked #3) carry insufficient evidence at this time and are both recommended **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Topical antifungal (tinea, oropharyngeal candidiasis, vulvovaginal candidiasis — established global use; not yet registered in Saudi Arabia) |
| Predicted New Indication | Vulvovaginitis (Vulvovaginal Candidiasis) |
| TxGNN Prediction Score | 99.59% (rank #6790 among all disease–drug pairs) |
| Evidence Level | L1 (multiple completed Phase 3/4 RCTs) |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Clotrimazole is a synthetic imidazole antifungal that inhibits the fungal enzyme **CYP51A1 (lanosterol 14α-demethylase)**, blocking ergosterol biosynthesis. Without ergosterol, the fungal cell membrane loses structural integrity and becomes permeable, leading to cell death. This mechanism is direct and well-established against *Candida* species — including *C. albicans*, *C. glabrata*, and *C. tropicalis* — which are responsible for the overwhelming majority of vulvovaginal candidiasis (VVC) cases.

Vulvovaginitis is not a new predicted use in the true sense: vulvovaginal candidiasis accounts for 20–25% of all vulvovaginitis and is one of the most important globally approved indications for clotrimazole. The TxGNN model correctly identifies this mechanistic alignment, and the evidence base (multiple Phase 4 RCTs, a post-marketing study of 1,033 patients, and >20 publications) confirms that this prediction is well-grounded in established pharmacology.

The key repurposing opportunity here is not mechanism discovery but **market authorization**: clotrimazole carries a decades-long global safety record for vulvovaginal candidiasis and is currently absent from the Saudi Arabian (SFDA) market. Registering it would fill an existing therapeutic gap in gynecological fungal infection management.

---

## Clinical Trial Evidence

*Primary indication: Vulvovaginitis / Vulvovaginal Candidiasis — top 10 trials by relevance and quality*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02180828](https://clinicaltrials.gov/study/NCT02180828) | Phase 4 | Completed | 240 | Head-to-head RCT: Clotrimazole vaginal tablet vs Fluconazole oral for severe vulvovaginal candidiasis — core direct efficacy and safety evidence |
| [NCT03599323](https://clinicaltrials.gov/study/NCT03599323) | N/A | Completed | 1,033 | Post-marketing non-interventional safety study of Empecid L Cream (Clotrimazole 1%) in vaginal yeast infection under pharmacist guidance; large real-world safety dataset |
| [NCT00755053](https://clinicaltrials.gov/study/NCT00755053) | Phase 3 | Completed | 466 | Investigator-blinded active-controlled study: Clotrimazole ovule 500 mg vs Clotrimazole vaginal tablet 500 mg; demonstrated non-inferiority of new formulation |
| [NCT00313131](https://clinicaltrials.gov/study/NCT00313131) | Phase 3 | Completed | 1,524 | Large RCT in West Africa comparing single-dose tinidazole + fluconazole vs metronidazole + vaginal clotrimazole (3 days) for syndromic vaginal discharge management |
| [NCT03562156](https://clinicaltrials.gov/study/NCT03562156) | Phase 3 | Completed | 438 | Double-blind, placebo-controlled Phase 3 evaluating oteseconazole for recurrent VVC; large-scale, rigorous design confirming the burden of RVVC and standard of care context |
| [NCT04699240](https://clinicaltrials.gov/study/NCT04699240) | Phase 4 | Completed | 140 | RCT: Clotrimazole vaginal tablets ± oral Lactobacillus for prevention of recurrent VVC; Clotrimazole used as active comparator/backbone treatment |
| [NCT02242695](https://clinicaltrials.gov/study/NCT02242695) | Phase 4 | Completed | 150 | Head-to-head: 10 mg dequalinium chloride vs 100 mg clotrimazole vaginal tablet in VVC; evaluated clinical efficacy, safety, and patient satisfaction |
| [NCT06835361](https://clinicaltrials.gov/study/NCT06835361) | Phase 2/3 | Recruiting | 264 | International open-label RCT comparing Clotrimazole + Lactulose vaginal suppositories vs Clotrimazole monotherapy (Canesten®) in candidal vulvovaginitis |
| [NCT01230814](https://clinicaltrials.gov/study/NCT01230814) | Phase 2 | Completed | 234 | Double-blind RCT of monthly metronidazole + miconazole suppositories vs placebo for preventing recurrent VVC; same-class comparator context |
| [NCT04292704](https://clinicaltrials.gov/study/NCT04292704) | N/A | Unknown | 205 | Protocol for RCT of fractional CO2 laser as consolidation treatment in recurrent VVC; antifungal treatment (including azoles) serves as standard backbone |

---

## Literature Evidence

*Top 10 publications by study type priority — RCT first, then reviews, then mechanistic*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [2644595](https://pubmed.ncbi.nlm.nih.gov/2644595/) | 1989 | RCT | Obstetrics and Gynecology | Prospective double-blind RCT (n=42): Clotrimazole 500 mg vaginal suppositories once weekly × 2 weeks achieved 90.4% clinical remission in recurrent VVC; monthly prophylaxis thereafter significantly reduced recurrence |
| [3895960](https://pubmed.ncbi.nlm.nih.gov/3895960/) | 1985 | RCT | Am J Obstet Gynecol | Open randomized study (n=199): single vaginal tablet 500 mg vs 6-day 100 mg clotrimazole in candidal vulvovaginitis; both regimens achieved equivalent mycologic cure rates |
| [39824974](https://pubmed.ncbi.nlm.nih.gov/39824974/) | 2025 | RCT | Scientific Reports | Triple-blinded equivalence RCT (n=126): Mycozin vs Clotrimazole 1% cream for vaginal candidiasis; confirmed clotrimazole as effective standard comparator for symptom relief |
| [41765149](https://pubmed.ncbi.nlm.nih.gov/41765149/) | 2026 | RCT | Complementary Therapies in Medicine | RCT comparing Prangos ferulacea vaginal cream vs clotrimazole for VVC; clotrimazole arm demonstrated robust clinical and laboratory cure — used as active gold-standard comparator |
| [30565745](https://pubmed.ncbi.nlm.nih.gov/30565745/) | 2019 | RCT | Mycoses | Randomised trial in recurrent VVC: probiotics + lactoferrin vs maintenance clotrimazole; supports clotrimazole's role as maintenance therapy standard in RVVC management |
| [24863842](https://pubmed.ncbi.nlm.nih.gov/24863842/) | 2014 | Review | J Applied Microbiology | Comprehensive review: "Clotrimazole as a pharmaceutical — past, present and future." Covers antifungal mechanism (ergosterol pathway), established indications (tinea, VVC, oropharyngeal candidiasis), and emerging pharmacological targets (IK1 potassium channel) |
| [39362128](https://pubmed.ncbi.nlm.nih.gov/39362128/) | 2024 | Meta-analysis | Eur J Obstet Gynecol Reprod Biol | Bayesian network meta-analysis of pharmacological maintenance therapy for RVVC; synthesizes evidence for oral/topical agents including clotrimazole at 24- and 48-week endpoints |
| [39419780](https://pubmed.ncbi.nlm.nih.gov/39419780/) | 2024 | Cohort/Mechanistic | J Applied Microbiology | Prospective study: clotrimazole treatment of VVC shifts vaginal bacteriome and lipid metabolism; mechanistic insight into how clotrimazole restores vaginal microecological balance |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Women's Health | Review of boric acid for recurrent VVC (resistant to azoles including clotrimazole); contextualizes non-albicans Candida resistance as a gap where clotrimazole alone may be insufficient |
| [7482105](https://pubmed.ncbi.nlm.nih.gov/7482105/) | 1995 | Clinical Trial | Sexually Transmitted Diseases | Comparative study: fluconazole vs clotrimazole for VVC; addresses compliance advantage of oral route, while confirming comparable antifungal efficacy of topical clotrimazole |

---

## Saudi Arabia Market Information

Clotrimazole is currently **not registered** with the Saudi Food and Drug Authority (SFDA). No licenses or approved products are on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | Not applicable | — | No registered products in Saudi Arabia |

> **Note:** Clotrimazole holds regulatory approvals in over 100 countries, including multiple formulations (vaginal tablets, creams, ovules, topical cream) for vulvovaginal candidiasis and dermatophyte infections. The absence of SFDA registration represents a market gap rather than a safety or efficacy concern.

---

## Safety Considerations

Detailed package insert data (warnings, contraindications) was not available through the data sources queried for this Evidence Pack. Please refer to the package insert for full safety information.

> **Known drug class context (from published literature):** Clotrimazole is a topically applied agent with minimal systemic absorption, contributing to its favorable safety profile. The Empecid L post-marketing study (n=1,033; NCT03599323) confirmed no unexpected safety signals in real-world community use. Azole-class resistance in non-*albicans Candida* species (e.g., *C. glabrata*) is an acknowledged clinical limitation.

---

## Additional TxGNN Predictions — Supporting Information

### Prediction #1 (TxGNN Rank): Acne — **Hold**

| Item | Detail |
|------|--------|
| TxGNN Score | 99.86% |
| Evidence Level | L4 (preclinical/mechanistic only) |
| Clinical Trials | 1 (SUSPENDED, combination product, no usable data) |
| Literature | 0 publications identified |
| Mechanistic Link | Indirect: Clotrimazole may suppress *Malassezia furfur* (a comorbid pathogen in some acne presentations) and has minor anti-inflammatory activity via IK1 potassium channel blockade. However, the primary drivers of acne (*P. acnes* infection, sebaceous gland obstruction, androgens) are outside Clotrimazole's pharmacological target range. |

### Prediction #3 (TxGNN Rank): Postmenopausal Atrophic Vaginitis — **Hold**

| Item | Detail |
|------|--------|
| TxGNN Score | 99.46% |
| Evidence Level | L5 (model prediction only) |
| Clinical Trials | 1 (UNKNOWN status, unrelated CO2 laser study) |
| Literature | 0 publications identified |
| Mechanistic Link | Very weak: Postmenopausal atrophic vaginitis (GSM) is driven by estrogen deficiency, not fungal overgrowth. Clotrimazole cannot address the root cause. High TxGNN score likely reflects disease feature overlap with vulvovaginitis. |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(for Vulvovaginitis / Vulvovaginal Candidiasis)*

**Rationale:**
Clotrimazole has one of the most robust evidence bases among azole antifungals for vulvovaginal candidiasis, backed by multiple completed Phase 3/4 RCTs (including head-to-head comparisons with fluconazole), a 1,033-patient post-marketing safety study, and over 35 years of published clinical trial literature — fully meeting L1 criteria. Its absence from the Saudi Arabian market represents a registration gap, not a safety or efficacy unknown.

**To proceed, the following is needed:**

- **SFDA registration dossier:** Compile CMC data, clinical efficacy dossier (existing global RCTs are sufficient), and local pharmacovigilance plan for submission
- **Package insert localization:** Obtain and translate official warnings, contraindications, and dosing information for Saudi patient population (data gap DG001)
- **Formulation decision:** Confirm preferred registration route — vaginal tablet (500 mg single dose or 100 mg × 6 days), cream (1%), or ovule (500 mg) — based on SFDA preference and supply chain considerations
- **Resistance monitoring plan:** Establish surveillance for non-*albicans Candida* species resistant to azoles, as these represent the main clinical limitation of clotrimazole therapy
- **MOA documentation (DG002):** Formally document CYP51A1 inhibition mechanism in submission package for SFDA scientific review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

