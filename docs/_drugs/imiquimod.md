---
layout: default
title: Imiquimod
parent: 僅模型預測 (L5)
nav_order: 323
evidence_level: L5
indication_count: 10
---

# Imiquimod
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

# Imiquimod: From External Genital Warts to Pre-malignant Neoplasm

## One-Sentence Summary

Imiquimod is a topical Toll-like receptor 7 (TLR7) agonist internationally approved for external genital/perianal warts, superficial basal cell carcinoma, and actinic keratosis. The TxGNN model predicts it may also be effective for **Pre-malignant Neoplasm** (a broad category encompassing HPV-related intraepithelial lesions), with **19 clinical trials** and **9 publications** currently identified in support of this direction, though the drug is not currently marketed in Saudi Arabia.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in the Saudi Arabia regulatory dataset (drug unmarketed); internationally, imiquimod is approved for external genital/perianal warts, superficial basal cell carcinoma, and actinic keratosis |
| Predicted New Indication | Pre-malignant Neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed, formally sourced mechanism-of-action data for imiquimod is not available in this evidence pack. Based on well-established pharmacological knowledge, imiquimod is a TLR7 agonist that activates plasmacytoid dendritic cells and macrophages, inducing local secretion of IFN-α and TNF-α. This drives a Th1-skewed immune response that clears HPV-infected and dysplastic epithelial cells at the site of topical application.

The predicted indication, "pre-malignant neoplasm," is mechanistically continuous with imiquimod's already-established uses. HPV-driven intraepithelial dysplasias — including cervical intraepithelial neoplasia (CIN), vulvar intraepithelial neoplasia (VIN), anal intraepithelial neoplasia (AIN), actinic keratosis (AK), and Bowenoid papulosis — share the same underlying biology as external genital warts: localized epithelial proliferation susceptible to TLR7-mediated immune clearance. This class of premalignant lesion is already a recognized, widely used application area for imiquimod in clinical practice, which supports a high degree of mechanistic consistency for this prediction.

Where the evidence is weaker is in extrapolating this mechanism to anatomically distinct or deep-tissue sites (e.g., oral mucosa, salivary gland, inner ear) — these are addressed separately in lower-ranked predictions not covered by this lead indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | RCT of topical imiquimod for high-grade cervical intraepithelial neoplasia (CIN 2-3) as a non-invasive alternative to LLETZ excision; directly targets the predicted indication but stopped early, limiting statistical power |
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | Completed | 259 | Imiquimod as neoadjuvant treatment for lentigo maligna (a premalignant melanocytic lesion) to reduce surgical excision margins; largest completed Phase 3 trial directly on a premalignant lesion |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | Completed | 90 | Brazilian RCT evaluating topical imiquimod efficacy in high-grade cervical intraepithelial lesions caused by persistent HPV infection |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | Completed | 5 | Explorative study of immune escape mechanisms in HPV-associated VIN 2/3 and anogenital warts, and imiquimod treatment efficiency; small sample, mechanism-focused |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Phase 3 | Unknown | 145 | Non-inferiority RCT comparing surgical excision to curettage plus imiquimod for nodular basal cell carcinoma; related skin-tumor immunotherapy mechanism |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Phase 1 | Completed | 16 | Neoadjuvant TLR7 agonist (imiquimod/Aldara) immunotherapy pilot in early-stage oral squamous cell carcinoma |
| [NCT03057340](https://clinicaltrials.gov/study/NCT03057340) | Phase 1 | Unknown | 30 | Imiquimod used as a vaccine adjuvant in advanced lung cancer immunotherapy; disease setting differs substantially from premalignant lesions |
| [NCT01792505](https://clinicaltrials.gov/study/NCT01792505) | Phase 1 | Completed | 71 | Surgical resection followed by dendritic-cell vaccine plus imiquimod in malignant glioma; imiquimod plays an adjuvant, not primary, role |
| [NCT03872947](https://clinicaltrials.gov/study/NCT03872947) | Phase 1b | Active, not recruiting | 138 | Dose/safety/PK study combining multiple anticancer regimens (including imiquimod cream) in advanced solid tumors; imiquimod's specific role is not well defined |
| [NCT04072900](https://clinicaltrials.gov/study/NCT04072900) | Phase 1 | Unknown | 30 | Personalized neoantigen vaccine combined with anti-PD-1 in metastatic melanoma; metastatic setting, not premalignant disease |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Review of interventions, including imiquimod, for anal canal intraepithelial neoplasia (AIN), a premalignant HPV-associated condition |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Review of medical interventions, including imiquimod, for high-grade vulval intraepithelial neoplasia (VIN) |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | International Journal of Molecular Sciences | Overview of combined photodynamic therapy approaches for non-melanoma skin cancer, contextualizing topical immunomodulators like imiquimod |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Letter | Current management review of actinic keratosis, a premalignant cutaneous lesion, including topical imiquimod as a field therapy |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Seminars in Cutaneous Medicine and Surgery | Review of topical treatment strategies, including imiquimod, for non-melanoma skin cancer and precursor (premalignant) lesions |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical/Animal PK-PD | Urologic Oncology | Pharmacokinetic/pharmacodynamic comparison of TLR7 agonists (related class) for premalignant skin lesions and investigational bladder cancer use |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case Report | International Journal of STD & AIDS | Successful treatment of high-grade VIN with topical imiquimod 5% in an immunosuppressed renal transplant recipient |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Case Report/Imaging | Der Hautarzt | OCT imaging case of disseminated superficial actinic porokeratosis with coexisting premalignant actinic keratoses resistant to topical treatment |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case Report | International Journal of STD & AIDS | Bowenoid papulosis of the penis (a premalignant HPV-related condition) successfully treated with topical imiquimod 5% cream |

---

## Saudi Arabia Market Information

Imiquimod currently holds no market authorization in Saudi Arabia (0 licenses on file; market status: Not Marketed). No product listings are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two Phase 3 trials (one completed with n=259) and two Cochrane systematic reviews directly support imiquimod's use in HPV-related and other premalignant epithelial lesions, and this mechanism is already part of imiquimod's established, widely used clinical practice pattern outside this specific indication label. However, the drug is not currently marketed in Saudi Arabia, and two blocking/high-severity data gaps (formal safety labeling and MOA documentation) remain unresolved, so proceeding requires structured risk management rather than an unconditional go.

**To proceed, the following is needed:**
- Official SFDA/manufacturer package insert (warnings, precautions, and contraindications) — currently a blocking data gap for the safety pre-assessment (S1)
- Formal DrugBank/manufacturer-sourced mechanism of action documentation to confirm the mechanistic linkage used above
- Drug-drug interaction (DDI) data, which returned no results in the current query
- A market authorization pathway assessment, since imiquimod is not currently registered in Saudi Arabia
- Clarification on which specific premalignant subtype(s) (CIN, VIN, AIN, AK, Bowenoid papulosis) the label/protocol would target, since "pre-malignant neoplasm" is a broad TxGNN-predicted category
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

