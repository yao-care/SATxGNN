---
layout: default
title: Azathioprine
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine: From Organ Transplant Rejection to Inflammatory Bowel Disease

## One-Sentence Summary

Azathioprine is a thiopurine immunosuppressant historically used to prevent organ transplant rejection and manage systemic autoimmune diseases.
The TxGNN model predicts it may be effective for **Inflammatory Bowel Disease (IBD)** — encompassing Crohn's disease and ulcerative colitis —
with **multiple Phase 3 clinical trials** and **Cochrane systematic reviews** (including a 2025 update) providing robust support for this direction.

> **Note on TxGNN ranking:** The four highest-ranked TxGNN predictions (ranks 1–4, scores >99.68%) are congenital developmental disorders — colobomatous microphthalmia-rhizomelic dysplasia, brachydactyly-syndactyly syndrome, acromesomelic dysplasia, and WHIM syndrome — none of which have any mechanistic or clinical basis for azathioprine repurposing. These scores likely reflect indirect network connections in the knowledge graph rather than genuine therapeutic relevance, and all carry an evidence level of **L5 / Hold**. The first clinically actionable prediction is **Inflammatory Bowel Disease** (rank 5, score 99.52%), backed by decades of Phase 3 trial evidence and Cochrane-level synthesis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Organ transplant rejection prevention; autoimmune diseases |
| Predicted New Indication | Inflammatory Bowel Disease (Crohn's disease & ulcerative colitis) |
| TxGNN Prediction Score | 99.52% (model rank 5) |
| Evidence Level | L1 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Azathioprine is a prodrug that is non-enzymatically converted to 6-mercaptopurine (6-MP) after oral administration. 6-MP is then further metabolized by TPMT and HPRT into the active 6-thioguanine nucleotides (6-TGNs). These metabolites suppress de novo purine synthesis and incorporate into the DNA of rapidly dividing lymphocytes, triggering apoptosis of activated T and B cells and inhibiting their proliferation. A secondary mechanism involves inhibition of Rac1 GTPase-mediated signalling, which amplifies pro-inflammatory cytokine production.

Inflammatory bowel disease is driven by a sustained, dysregulated mucosal immune response. In Crohn's disease, Th1/Th17 T-cell hyperactivation drives transmural granulomatous inflammation; in ulcerative colitis, aberrant mucosal T-cell activity sustains mucosal injury and ulceration. Azathioprine's mechanism directly intercepts these lymphocyte-driven pathways, making it biologically coherent as an IBD maintenance agent. This mechanistic alignment is what the TxGNN knowledge graph captures in its high prediction score.

The prediction is not merely theoretical — azathioprine is already enshrined in international IBD guidelines as a first-line immunomodulator for steroid-dependent and steroid-refractory disease. The SONIC trial (Phase 3, 508 patients) demonstrated that infliximab plus azathioprine is superior to either agent alone in Crohn's disease. The 2025 updated Cochrane review confirmed its role in ulcerative colitis maintenance. Saudi Arabia's current absence of local registration represents a regulatory opportunity, not an evidence gap. Key caveats include the need for pre-treatment TPMT/NUDT15 pharmacogenomic screening to avoid potentially life-threatening myelosuppression, and careful risk-benefit assessment when combining with biologics (increased lymphoma risk).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Phase 3 | Unknown | 84 | Directly compares low-dose AZA + allopurinol optimization vs standard AZA monotherapy in ulcerative colitis; tests whether allopurinol co-administration improves 6-TGN levels and reduces treatment failures |
| [NCT00094458](https://clinicaltrials.gov/study/NCT00094458) | Phase 3 | Completed | 508 | Three-arm SONIC-type trial in biologic- and immunomodulator-naïve Crohn's disease: infliximab alone, AZA alone, or infliximab + AZA; established the superiority of combination therapy |
| [NCT02177071](https://clinicaltrials.gov/study/NCT02177071) | Phase 4 | Completed | 211 | SPARE trial: patients in sustained steroid-free remission on IFX+AZA randomized to continue combination, IFX monotherapy, or AZA monotherapy — evaluates whether anti-metabolite withdrawal is safe |
| [NCT02517684](https://clinicaltrials.gov/study/NCT02517684) | Phase 4 | Completed | 100 | Top-down IFX + AZA vs conventional step-up approach (steroids/EEN + AZA) in moderate-to-severe pediatric Crohn's disease; directly evaluates AZA-containing regimens in children |
| [NCT05584228](https://clinicaltrials.gov/study/NCT05584228) | N/A | Not Yet Recruiting | 150 | SMART trial: AZA + subcutaneous infliximab vs ileocecal resection in symptomatic small bowel Crohn's stricture — positions AZA + biologic combination as the medical management comparator arm |
| [NCT07235904](https://clinicaltrials.gov/study/NCT07235904) | Phase 4 | Recruiting | 300 | MIRACLE trial: mirikizumab (top-down) vs AZA (standard of care) in newly diagnosed moderate-to-severe UC — reinforces AZA as the current benchmark therapy against which newer biologics are measured |
| [NCT01015391](https://clinicaltrials.gov/study/NCT01015391) | N/A | Unknown | 100 | Randomized open-label study comparing T2 (plant-derived combination) vs AZA for maintaining clinical and endoscopic remission in Crohn's disease after surgical resection |
| [NCT03185611](https://clinicaltrials.gov/study/NCT03185611) | Phase 3 | Unknown | 120 | Rifaximin + thiopurine vs thiopurine alone for preventing postoperative endoscopic recurrence in high-risk Crohn's disease; AZA (thiopurine) forms the backbone of both treatment arms |
| [NCT04304950](https://clinicaltrials.gov/study/NCT04304950) | Phase 4 | Completed | 28 | IBD chronotherapy study: morning vs evening administration of AZA/6-MP in IBD patients — evaluates whether circadian timing influences efficacy and disease outcomes |
| [NCT00113503](https://clinicaltrials.gov/study/NCT00113503) | Phase 2 | Terminated | 50 | Multi-site trial directly comparing weight-based vs metabolite-guided (6-TGN level) AZA dosing in steroid-dependent Crohn's disease; terminated early but provides dosing optimization data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Cochrane SR | Cochrane Database Syst Rev | Updated Cochrane review on AZA and 6-MP for maintenance of remission in UC; most current evidence synthesis confirming thiopurine efficacy for long-term disease management |
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE trial: top-down infliximab + AZA vs AZA alone in acute severe UC responding to IV steroids — directly addresses optimal AZA-based post-hospitalization maintenance strategy |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Meta-analysis | Aliment Pharmacol Ther | Meta-analysis establishing efficacy of AZA and 6-MP in UC; demonstrated benefit comparable to that seen in Crohn's disease and provided pooled efficacy estimates |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Cochrane SR | Cochrane Database Syst Rev | Cochrane systematic review of AZA/6-MP for remission maintenance in UC — predecessor to the 2025 update, providing longitudinal evidence tracking |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Review | J Crohn's Colitis | State-of-the-art review of thiopurine treatment in IBD; covers current indications, TPMT/NUDT15 pharmacogenomics, metabolite-guided optimization, and long-term safety considerations |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Review | Expert Rev Gastroenterol Hepatol | Updated molecular mechanism of AZA in IBD including Rac1 GTPase inhibition and T-cell apoptosis induction; bridges 45 years of clinical experience with emerging mechanistic insights |
| [10499471](https://pubmed.ncbi.nlm.nih.gov/10499471/) | 1999 | Review | Scand J Gastroenterol Suppl | Foundational review on AZA long-term clinical efficacy and safety in IBD; documents early regulatory approval context and clinical evidence base |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Basic/Translational | Cell Reports Medicine | Identifies *Blautia wexlerae* gut microbiota as a driver of AZA therapy failure in IBD by reducing 6-MP bioavailability; highlights microbiome as a modifiable factor in treatment response |
| [36462311](https://pubmed.ncbi.nlm.nih.gov/36462311/) | 2023 | Cohort | Biomed Pharmacother | TPMT gene DNA methylation and AZA pharmacokinetics in very early onset IBD children; demonstrates higher TPMT activity in VEO-IBD compared to adolescent IBD, with implications for dose calibration |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | Review | J Gastroenterol Hepatol | Comprehensive review of AZA/6-MP pharmacogenetics and metabolite monitoring in IBD; covers TPMT polymorphisms, 6-TGN therapeutic windows, and strategies to reduce toxicity while maximizing efficacy |

---

## Saudi Arabia Market Information

Azathioprine is currently **not registered in Saudi Arabia**. The Saudi Food and Drug Authority (SFDA) database contains no active product authorizations as of the data cutoff (June 2026). No local product information, approved indications, or regulatory dossiers are on record.

This represents a registration gap. The drug has well-established global regulatory approvals for IBD in multiple jurisdictions (US FDA, EMA, Japan PMDA) and could be pursued for local registration using existing international clinical dossiers.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Key monitoring requirements derived from clinical literature:**
> - **Pharmacogenomics before initiation**: TPMT and NUDT15 genotyping is strongly recommended. The NUDT15 c.415C>T variant is prevalent in East Asian and Southeast Asian populations and predicts severe thiopurine-induced leukopenia at standard doses — dose reduction or avoidance is required in carriers.
> - **Haematological monitoring**: Regular CBC (with differential) is essential to detect neutropenia and thrombocytopenia, particularly in the first year of treatment.
> - **Long-term cancer surveillance**: Prolonged thiopurine use is associated with increased risk of non-melanoma skin cancer and lymphoma (especially EBV-associated lymphoma). Annual skin examination and assessment of lymphoma symptoms are recommended.
> - **Combination therapy caution**: When combined with biologics (e.g., infliximab), the lymphoma risk is further elevated — individual benefit-risk assessment is required before initiating combination therapy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for azathioprine in IBD is among the strongest in drug repurposing — it includes four consecutive Cochrane systematic reviews (2007, 2012, 2016, 2025), a meta-analysis, and multiple completed Phase 3 RCTs, with a mechanistic rationale that is thoroughly characterized at the molecular level. The principal challenge is not clinical uncertainty but rather the need for pharmacogenomic safeguards (TPMT/NUDT15 screening) and regulatory registration in Saudi Arabia.

**To proceed, the following is needed:**

- **SFDA registration**: Submit a New Drug Application or Abridged Application for IBD indication using reference country approvals (FDA/EMA), leveraging the established global clinical dossier
- **Pharmacogenomic protocol**: Establish pre-treatment TPMT and NUDT15 genotyping pathway for the Saudi patient population, with dose-adjustment guidelines for at-risk genotypes
- **Safety monitoring plan**: Define CBC and liver function monitoring schedule; implement long-term lymphoma and skin cancer surveillance programme
- **Mechanistic documentation**: Resolve DrugBank data gap (DG002) to complete MOA documentation for the regulatory dossier
- **Drug interaction assessment**: Conduct formal DDI review (DG001 resolution) — particularly co-administration with allopurinol (which can increase 6-TGN levels and toxicity) and biologics
- **Local pharmacist/physician education**: Develop prescriber training on thiopurine metabolite monitoring (6-TGN levels) to optimize dosing and minimize treatment failure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

