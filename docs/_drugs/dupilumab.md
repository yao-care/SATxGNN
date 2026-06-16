---
layout: default
title: Dupilumab
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab: From Atopic Dermatitis to Bronchitis

## One-Sentence Summary

Dupilumab is a fully human monoclonal antibody blocking the IL-4 receptor α subunit (IL-4Rα), globally established as standard of care for Type 2 inflammatory diseases including atopic dermatitis and asthma, though it has no current market authorization in Saudi Arabia.
The TxGNN model predicts it may be effective for **Bronchitis** — specifically eosinophilic and plastic bronchitis subtypes — with **1 clinical trial** (indirect, via the united airway disease concept) and **6 publications** currently supporting this direction.
The mechanistic rationale is biologically sound, but dedicated direct clinical evidence in bronchitis as a distinct diagnosis remains limited.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Atopic dermatitis (global approval; not registered in Saudi Arabia) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dupilumab is a fully human IgG4 monoclonal antibody that binds the shared IL-4 receptor α subunit (IL-4Rα), blocking downstream signaling of both IL-4 and IL-13 — the two master cytokines of Type 2 (Th2) immunity. Formal MOA records were not returned by the DrugBank query in this Evidence Pack; however, the mechanism is well-characterized across the literature: IL-4 drives naïve T cell polarization toward Th2 and class-switching to IgE, while IL-13 promotes goblet cell metaplasia, airway mucus hypersecretion, and tissue eosinophilia. Dupilumab interrupts this axis by blocking the shared receptor subunit expressed on both immune and structural (epithelial, endothelial) cells, reversing Type 2-driven tissue remodeling across multiple organ systems.

The mechanistic link to bronchitis centers on the eosinophilic airway disease spectrum. Eosinophilic bronchitis — chronic cough with sputum eosinophilia in the absence of variable airflow obstruction — and plastic bronchitis (particularly in pediatric patients, where thick fibrinous casts obstruct the airways) both display the hallmark IL-4/IL-13-driven Type 2 signature: eosinophil accumulation, mucus hypersecretion, and impaired mucociliary clearance. Early pediatric case reports have documented meaningful clinical improvement in plastic bronchitis treated with dupilumab. Importantly, dupilumab already holds FDA approval for moderate-to-severe asthma (2018) and chronic rhinosinusitis with nasal polyps (CRSwNP, 2019), establishing a well-evidenced precedent for its use across the entire Type 2 lower and upper airway continuum.

The "united airway disease" framework is central to this TxGNN prediction: Type 2 inflammation does not respect anatomical divisions and flows continuously from the nasal passages (allergic rhinitis) through the sinuses (CRSwNP, CRSsNP) into the bronchi (eosinophilic bronchitis) and alveolar structures. The sole identified clinical trial (NCT04362501) targets CRSsNP — a directly adjacent upper airway Type 2 condition — and provides indirect mechanistic support for the same IL-4/IL-13 pathway operating further down the airway. The critical caveat is subtype specificity: non-eosinophilic bronchitis (infectious, neutrophilic, or COPD-driven) involves Th1/Th17 and neutrophil-predominant pathways that dupilumab does not address, and IL-4/IL-13 blockade in non-Type 2 airway disease carries a theoretical risk of shifting the immune balance unfavorably.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | Completed | 33 | Dupilumab for chronic rhinosinusitis without nasal polyps (CRSsNP) — evaluates clinical effectiveness across Type 2 endotypes excluding the nasal polyp cluster; provides indirect mechanistic support for the Type 2 united airway continuum connecting upper airway and bronchial inflammation, but cannot be directly extrapolated to bronchitis |

> No clinical trials with dupilumab directly targeting bronchitis as the primary indication were identified. The above trial represents an adjacent upper airway Type 2 condition and is classified as indirect (Relevance Grade B).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | RCT Extension | The Lancet. Respiratory Medicine | TRAVERSE: Long-term safety and efficacy of dupilumab in moderate-to-severe asthma beyond 1 year; confirms sustained suppression of Type 2 lower airway inflammation and durable reduction in exacerbation rates |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Meta-Analysis | The Journal of Asthma | Pooled RCT analysis demonstrates dupilumab significantly reduces exacerbation frequency and improves FEV1 in uncontrolled asthma; broadest quantitative evidence for IL-4/IL-13 blockade in lower airway Type 2 disease |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Exploratory RCT | Chest | Anti-T2 biologic therapy (dupilumab) reverses MRI-measured ventilation defects in prednisone-dependent eosinophilic asthma; imaging-confirmed restoration of airflow in eosinophil-obstructed airways — direct mechanistic link to bronchial disease |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Case Series / Review | Pediatric Pulmonology | Novel therapies for eosinophilic pediatric plastic bronchitis — dupilumab cited as an emerging therapeutic option for fibrinous airway cast formation; most directly relevant publication to bronchitis as a distinct clinical diagnosis |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Comprehensive Review | Tuberculosis and Respiratory Diseases | Comprehensive review of pharmacologic approaches to preventing COPD exacerbations, including emerging biologics targeting Type 2 pathways; contextualizes dupilumab within the broader chronic obstructive airway treatment landscape |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opinion on Pharmacotherapy | Management challenges in asthma overlapping with smoking-induced airway diseases (chronic bronchitis, emphysema, asthma-COPD overlap); identifies the underrepresentation of bronchitis patients in biologic trials and the resulting evidence gap |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The available clinical evidence for dupilumab in bronchitis is indirect — the sole identified trial targets CRSsNP rather than bronchitis, and the literature base covers asthma and COPD rather than bronchitis as a discrete diagnostic entity. Critically, dupilumab is not currently registered in Saudi Arabia for any indication, meaning the regulatory pathway itself remains unopened; establishing a new repurposed indication would first require primary market authorization. Furthermore, the bronchitis category encompasses mechanistically heterogeneous disease subtypes, of which only eosinophilic and plastic bronchitis are plausibly responsive to IL-4/IL-13 blockade.

**To proceed, the following is needed:**

- **Subtype stratification**: Define the target bronchitis population using Type 2 biomarkers (blood eosinophil count ≥300 cells/μL, FeNO ≥25 ppb, sputum eosinophilia ≥3%) to identify the IL-4/IL-13-responsive subgroup; non-eosinophilic bronchitis is a contraindication to this approach
- **Direct clinical evidence**: A dedicated Phase 2 RCT in eosinophilic bronchitis or plastic bronchitis with dupilumab is required before any higher-level decision can be made
- **Saudi Arabia regulatory pathway**: Assess SFDA registration requirements; dupilumab has no existing authorization in Saudi Arabia and would require a full regulatory filing — consider whether the atopic dermatitis indication (TxGNN Rank 2, globally L1 evidence) is a more actionable first entry point for the Saudi market
- **Safety documentation**: Obtain and review the complete package insert for warnings, contraindications, and monitoring requirements (not available in this Evidence Pack); note that dupilumab has known signals including conjunctivitis, injection-site reactions, and paradoxical psoriasiform eruptions that require clinical monitoring protocols
- **MOA verification**: Retrieve formal DrugBank mechanistic data to complete the pharmacological dossier for regulatory submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

