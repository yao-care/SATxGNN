---
layout: default
title: Lanadelumab
parent: 僅模型預測 (L5)
nav_order: 358
evidence_level: L5
indication_count: 10
---

# Lanadelumab
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

# Lanadelumab: From No Registered Indication to C1 Inhibitor Deficiency (Hereditary Angioedema)

## One-Sentence Summary

Lanadelumab (DrugBank DB14597) has no recorded original indication or market authorization on file for this jurisdiction — it is currently **not marketed** here. The TxGNN model's top-ranked prediction is **C1 Inhibitor Deficiency** (the molecular basis of Hereditary Angioedema Type I/II), the condition lanadelumab is already approved for internationally, supported by **22 clinical trials** and **20 publications**, including one pivotal placebo-controlled Phase 3 RCT.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no approved indication or license record exists locally for this drug |
| Predicted New Indication | C1 Inhibitor Deficiency (Hereditary Angioedema Type I/II) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (1 completed pivotal Phase 3 RCT — HELP Study, NCT02586805) |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the drug-level record for this evidence pack (DrugBank MOA field flagged as a data gap). However, the literature evidence attached to the top prediction does describe the mechanism: lanadelumab is a fully human monoclonal antibody that inhibits plasma kallikrein (PMID 30267321). In hereditary angioedema, mutations in the *SERPING1* gene cause a deficiency or dysfunction of C1-esterase inhibitor (C1-INH), which normally restrains plasma kallikrein activity. Loss of this restraint drives excessive bradykinin production, the vasodilator responsible for HAE's characteristic swelling attacks. By directly inhibiting plasma kallikrein downstream of the C1-INH defect, lanadelumab addresses the disease mechanism regardless of the specific C1-INH mutation.

This is not a conventional "repurposing" signal in the usual sense: C1 Inhibitor Deficiency is not a new indication distinct from the drug's known mechanism — it is the disease lanadelumab (Takhzyro) is already approved to treat in numerous other markets (US, EU, Japan, China, South Korea, etc.), as reflected by the extensive multinational trial and real-world evidence portfolio. Because this evidence pack's regulatory record shows zero local licenses and no original indication, the practical interpretation is that TxGNN has correctly identified the drug's established therapeutic use, but local registration and safety documentation are absent. Notably, one Phase 3 trial (NCT04444895) also explored lanadelumab in a mechanistically related but distinct condition — non-histaminergic angioedema with *normal* C1-INH — indicating the kallikrein-inhibition mechanism may have utility beyond classic C1-INH deficiency as well.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Phase 3 | Completed | 125 | Pivotal double-blind, placebo-controlled trial (HELP Study) establishing lanadelumab's efficacy and safety for long-term prophylaxis against HAE attacks |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Phase 3 | Completed | 212 | Open-label extension (HELP Study Extension) confirming long-term safety and efficacy of continued prophylaxis |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | Completed | 12 | Open-label study confirming efficacy and safety in Japanese HAE Type I/II patients, supporting Japan approval |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | Completed | 20 | Open-label study of safety, PK and efficacy in Chinese HAE patients over 26 weeks |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | Completed | 21 | SPRING Study: open-label PK/PD and prophylactic efficacy in pediatric patients aged 2 to <12 years |
| [NCT04444895](https://clinicaltrials.gov/study/NCT04444895) | Phase 3 | Completed | 73 | Long-term safety/efficacy in non-histaminergic angioedema with normal C1-inhibitor — a distinct but mechanistically related condition |
| [NCT07263685](https://clinicaltrials.gov/study/NCT07263685) | N/A | Not yet recruiting | 50 | REFLEQT-KSA: retrospective chart review of real-world effectiveness and quality-of-life impact of lanadelumab prophylaxis specifically in the Kingdom of Saudi Arabia |
| [NCT04130191](https://clinicaltrials.gov/study/NCT04130191) | N/A | Completed | 140 | ENABLE: 3-year prospective real-world study comparing HAE attack rates before and after lanadelumab initiation |
| [NCT03845400](https://clinicaltrials.gov/study/NCT03845400) | N/A | Completed | 168 | EMPOWER: US/Canada observational study comparing HAE attack rates pre- and post-lanadelumab treatment |
| [NCT04687137](https://clinicaltrials.gov/study/NCT04687137) | Phase 3 | Completed | 12 | Japan expanded access program providing lanadelumab to Japanese HAE patients ahead of local licensure |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Pivotal randomized, placebo-controlled trial (HELP Study) showing lanadelumab significantly reduces HAE attack rates vs placebo |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Drug Review | Drugs | First global approval profile: fully human mAb inhibiting plasma kallikrein; describes SERPING1/C1-INH deficiency mechanism |
| [32187470](https://pubmed.ncbi.nlm.nih.gov/32187470/) | 2020 | Review | New England Journal of Medicine | Overview of HAE pathophysiology, diagnosis, and treatment |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Systematic Review | Clinical Reviews in Allergy & Immunology | Review of breakthrough HAE attacks occurring in patients already on long-term prophylaxis |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Network Meta-Analysis | Drugs in R&D | Indirect comparison of efficacy, safety, and QoL impact across HAE prophylactic therapies (lanadelumab, garadacimab, C1INH, berotralstat) |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Open-label Extension Study | Allergy | HELP OLE: long-term effectiveness and safety follow-up in patients ≥12 years old |
| [39701274](https://pubmed.ncbi.nlm.nih.gov/39701274/) | 2025 | Observational Study | J Allergy Clin Immunol Pract | INTEGRATED multicountry real-world study of lanadelumab effectiveness in reducing HAE attack rates |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Review | BioDrugs | Review of preclinical and Phase I data supporting the prophylactic mechanism in C1-INH-HAE |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Review | Journal of Allergy and Clinical Immunology | Review of HAE disease burden and treatment access across the Asia-Pacific region |
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Review | J Investig Allergol Clin Immunol | Review of current and emerging treatments for C1-esterase inhibitor deficiency HAE |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence is strong (L2: a pivotal double-blind, placebo-controlled Phase 3 RCT plus a broad multinational Phase 3/real-world program, including a Saudi Arabia–specific study already underway), and the predicted "new" indication is in fact the drug's established global use. However, the local safety data gap (DG001, marked *Blocking*) means the drug cannot yet clear an S1 safety pre-assessment, and there is no local regulatory record (0 authorizations, not marketed).

**To proceed, the following is needed:**
- Obtain the SFDA/local package insert (warnings, contraindications, DDI) to close DG001 before any safety pre-assessment
- Retrieve confirmed mechanism-of-action data from DrugBank to close DG002 and formally validate the mechanistic rationale
- Pursue local regulatory registration, since this is a market-entry decision for an internationally approved therapy rather than a novel disease-target pairing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

