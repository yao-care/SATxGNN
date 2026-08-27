---
layout: default
title: Tinidazole
parent: 僅模型預測 (L5)
nav_order: 621
evidence_level: L5
indication_count: 10
---

# Tinidazole
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

# Tinidazole: From Protozoal & Anaerobic Infections to AIDS (HIV Acquisition-Risk Reduction)

## One-Sentence Summary

> Tinidazole is a second-generation 5-nitroimidazole antimicrobial, established for anaerobic bacterial and protozoal infections (trichomoniasis, bacterial vaginosis, amebiasis, giardiasis). The TxGNN model's top-scored predictions (postmenopausal atrophic vaginitis, vulvar ulceration, vulvar/breast lesions) show no supporting evidence and are most likely knowledge-graph embedding artifacts. The one indication with real supporting data — **AIDS** — is supported not by direct antiretroviral activity, but by **1 clinical trial** and **17 publications** on treating genital-tract infections that increase HIV susceptibility, making it the only candidate in this evidence pack worth carrying forward.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anaerobic bacterial & protozoal infections (trichomoniasis, bacterial vaginosis, amebiasis, giardiasis) |
| Predicted New Indication | AIDS (via indirect infection-control pathway, not direct antiretroviral effect) |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for tinidazole is not available in this evidence pack (MOA: Data Gap). Based on the information that is available, tinidazole belongs to the 5-nitroimidazole class and is clinically used for trichomonal vaginitis, bacterial vaginosis, amebiasis, and giardiasis — efficacy that is well established.

The mechanistic link to AIDS is **not** a direct antiviral or antiretroviral effect — tinidazole has no known anti-HIV activity. Instead, the rationale is indirect: infections such as *Trichomonas vaginalis* and bacterial vaginosis-related dysbiosis are known to increase mucosal permeability and inflammation, which in turn raises the risk of HIV acquisition and transmission. By treating these underlying infections, tinidazole may plausibly reduce HIV susceptibility as part of a combined infection-control strategy — not as a treatment for AIDS itself. This is reflected in the supporting literature, which centers on trichomoniasis/amebiasis management in HIV-positive or HIV-at-risk populations rather than on antiretroviral endpoints.

**Note on other predicted indications:** Nine of the ten TxGNN-predicted indications in this evidence pack (postmenopausal atrophic vaginitis, vulvar ulceration, vulvar neoplasm, breast fibrocystic disease, blunt duct/apocrine adenosis of breast, AIDS-related complex, congenital HIV, benign mammary dysplasia) returned **zero clinical trials and zero literature hits** across ClinicalTrials.gov, ICTRP, and PubMed. Their own rationale text flags them as likely token-level embedding proximity artifacts (e.g. "vaginitis" clustering) with no plausible biological mechanism. These are excluded from further evaluation (Evidence Level L5, Hold, Decision Stage S0) and are not carried into the sections below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03412071](https://clinicaltrials.gov/study/NCT03412071) | NA | Unknown | 125 | Pilot study assessing four antimicrobial products (3 topical, 1 systemic) on foreskin microbiome and HIV susceptibility of foreskin-derived CD4+ T cells in HIV-uninfected Ugandan men undergoing elective circumcision. Tinidazole is not explicitly named as the study drug and the endpoint is HIV susceptibility, not AIDS treatment — relevance graded C (indirect, low certainty). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31996095](https://pubmed.ncbi.nlm.nih.gov/31996095/) | 2020 | Cohort/Screening | Int J STD AIDS | Prenatal screening for chlamydia, gonorrhea, and trichomonas in DR Congo; trichomonas treatment relevant to reducing adverse birth/transmission outcomes. |
| [21931875](https://pubmed.ncbi.nlm.nih.gov/21931875/) | 2011 | Cohort | PLoS Negl Trop Dis | Retrospective analysis of 170 HIV-1/amebiasis co-infected Japanese men; describes clinical features and treatment response in this high-risk population. |
| [34794678](https://pubmed.ncbi.nlm.nih.gov/34794678/) | 2022 | Review | Pediatr Clin North Am | Review of amebiasis/amebic liver abscess; notes people with AIDS/HIV as a high-risk group requiring heightened suspicion. |
| [19632225](https://pubmed.ncbi.nlm.nih.gov/19632225/) | 2010 | Review | Exp Parasitol | Review of Cryptosporidium/Giardia treatment options, including nitroimidazole-class drugs, with focus on immunocompromised/HIV-positive patients. |
| [30789955](https://pubmed.ncbi.nlm.nih.gov/30789955/) | 2019 | Review | PLoS One | Epidemiological and clinical review of amoebic colitis in a non-endemic (Barcelona) setting. |
| [35863010](https://pubmed.ncbi.nlm.nih.gov/35863010/) | 2022 | In vitro | Microbiol Spectr | Comparative in vitro anti-trichomonal activity of tinidazole and other 5-nitroimidazoles against clinical *T. vaginalis* isolates. |
| [31324206](https://pubmed.ncbi.nlm.nih.gov/31324206/) | 2019 | Trial Protocol | Trials | Protocol for the RCT (matches NCT03412071) examining systemic/topical antimicrobial effects on penile microbiota and HIV susceptibility in Ugandan men. |
| [8442923](https://pubmed.ncbi.nlm.nih.gov/8442923/) | 1993 | Preliminary study | AIDS (London) | Study of combined tinidazole + thiabendazole + cotrimoxazole vs. placebo for AIDS-related diarrhea in Zambia — most direct tinidazole/AIDS link in this dataset. |
| [29393008](https://pubmed.ncbi.nlm.nih.gov/29393008/) | 2018 | Case report | Int J STD AIDS | Refractory *T. vaginalis* infection treated with combined IV metronidazole, oral tinidazole, and intravaginal boric acid after gastric bypass surgery. |
| [21097745](https://pubmed.ncbi.nlm.nih.gov/21097745/) | 2010 | Case report | Int J STD AIDS | *T. vaginalis* presenting atypically as vulval ulceration, resolved with oral tinidazole. |

---

## Saudi Arabia Market Information

Tinidazole currently has **no marketing authorization on record in Saudi Arabia** (market status: not marketed; 0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were not retrievable for this evaluation — see Conclusion for remediation.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The AIDS-related evidence is exploratory (Evidence Level L3: cohort/review-grade only, no completed RCT with a HIV/AIDS endpoint, and one Phase NA trial of unknown status). More importantly, the mechanistic link is indirect (infection control lowering HIV acquisition risk) rather than a treatment effect on AIDS itself, and a **Blocking** data gap (no TFDA/SFDA package insert or safety data) currently prevents this candidate from clearing the S1 safety screen at all.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — required before any S1 safety review can proceed
- Confirmed mechanism-of-action data from DrugBank
- A completed, adequately powered trial with an HIV-acquisition or AIDS-related endpoint (the current NCT03412071 is status "Unknown" and only indirectly linked to tinidazole)
- Clarification of the drug-interaction profile (currently "not found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

