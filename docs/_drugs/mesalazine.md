---
layout: default
title: Mesalazine
parent: 僅模型預測 (L5)
nav_order: 410
evidence_level: L5
indication_count: 7
---

# Mesalazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Mesalazine: From Ulcerative Colitis to Rheumatoid Arthritis

## One-Sentence Summary

Mesalazine (5-ASA) is an anti-inflammatory agent used to treat ulcerative colitis and other inflammatory bowel conditions (based on drug context in the evidence literature; formal original-indication text is unavailable because the drug is not registered in Taiwan). Across 7 TxGNN-predicted indications for this drug, the strongest evidence-backed candidate is **Rheumatoid Arthritis**, supported by **6 registered clinical trials** and **20 publications**, though the active-moiety attribution (5-ASA vs. sulfapyridine) remains scientifically contested. A secondary candidate, **Osteoarthritis**, has mechanistic/preclinical support (3 publications, no trials) but insufficient evidence for clinical action. The remaining 5 predictions (including the single highest TxGNN score, a rare genetic disorder) have zero clinical trials or literature and are assessed as likely knowledge-graph noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ulcerative colitis (inferred from supporting literature; not confirmed by Taiwan regulatory filings — drug unregistered) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% (rank 7017 of screened pairs) |
| Evidence Level | L2 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

### All Predicted Indications (Screening Overview)

Because this evidence pack covers multiple candidate indications for the same drug, the full screening set is shown for transparency:

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|------------------|------------------|
| 1 | Congenital hypotrichosis with juvenile macular dystrophy | 99.65% | L5 | S0 | Hold |
| 2 | Osteoarthritis | 99.63% | L4 | S1 | Research Question |
| 3 | Rheumatoid Arthritis | 99.57% | L2 | S2 | **Proceed with Guardrails** |
| 4 | Seborrheic keratosis | 99.50% | L5 | S0 | Hold |
| 5 | Osteoarthritis susceptibility | 99.35% | L5 | S0 | Hold |
| 6 | Vulvar inverted follicular keratosis | 99.33% | L5 | S0 | Hold |
| 7 | Pseudoachondroplasia | 99.19% | L5 | S0 | Hold |

Note: the single highest TxGNN score (rank 1) has zero supporting trials or literature and is explicitly flagged in the source rationale as likely embedding-level noise/false positive — it is not used as the report's primary subject. Ranks 4–7 are similarly unsupported (benign keratoses and structural/genetic disorders with no plausible mechanistic tie to 5-ASA's anti-inflammatory action).

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for mesalazine is not available in the regulatory record (Data Gap). Based on the supporting literature within this evidence pack, 5-aminosalicylic acid (5-ASA/mesalazine) acts through inhibition of prostaglandin (PGE2) and leukotriene (LTB4/LTC4) release from inflamed tissue, NF-κB pathway suppression, and modulation of lymphocyte activation — mechanisms it shares with its parent compound sulfasalazine, which is cleaved in the colon into sulfapyridine and mesalazine.

Sulfasalazine has long been an established disease-modifying antirheumatic drug (DMARD) for rheumatoid arthritis, which provides indirect mechanistic plausibility for mesalazine in the same disease. However, multiple head-to-head studies in this evidence pack (PMID 2860942, PMID 2877851, PMID 8535642) directly investigated which of sulfasalazine's two cleavage products drives its antirheumatic effect, and the weight of evidence points to **sulfapyridine**, not mesalazine, as the primary active moiety — mesalazine alone showed only weak first-line effect. This is a material caveat: efficacy demonstrated for sulfasalazine as a whole cannot be directly attributed to mesalazine.

For osteoarthritis, a 2024 mechanistic study (PMID 38310093) identified a novel OSCAR-PPARγ axis through which 5-ASA suppresses cartilage/bone-destructive inflammation, supported by older ex vivo human synovial tissue data (PMID 1673814) showing sulfasalazine metabolites inhibit prostaglandin/leukotriene release. This is a biologically coherent but early-stage (preclinical/ex vivo) signal with no clinical trials to date.

---

## Clinical Trial Evidence

### Rheumatoid Arthritis (primary candidate)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02930343](https://clinicaltrials.gov/study/NCT02930343) | Phase 3 | Terminated | 136 | Sulfasalazine vs. leflunomide-based combination DMARD therapy in RA patients failing methotrexate monotherapy. Directly relevant to RA (Grade A relevance), but terminated with no published results — evidence strength is limited. |
| [NCT00637780](https://clinicaltrials.gov/study/NCT00637780) | Phase 4 | Terminated | 2 | Steady-state pharmacokinetics of sulfasalazine delayed-release tablets in pediatric juvenile idiopathic arthritis (Grade B relevance — PK study, not efficacy; terminated at n=2). |
| [NCT00514982](https://clinicaltrials.gov/study/NCT00514982) | Phase 2 | Withdrawn | 0 | IBD-therapy step-up approach for Hermansky-Pudlak syndrome-associated colitis. Grade C relevance — studies IBD immunopathogenesis, not RA; withdrawn with 0 enrollment. |
| [NCT05580861](https://clinicaltrials.gov/study/NCT05580861) | Phase 1/2 | Recruiting | 64 | Sulfasalazine combined with standard induction therapy in older AML patients, exploiting SSZ's xCT-inhibitory action. Grade C relevance — oncology context, not RA. |
| [NCT06201793](https://clinicaltrials.gov/study/NCT06201793) | Phase 2 | Completed | 46 | Minocycline efficacy/safety in ulcerative colitis patients on mesalamine. Grade C relevance — UC context, different drug studied. |
| [NCT03591770](https://clinicaltrials.gov/study/NCT03591770) | Phase 4 | Terminated | 15 | Shingrix vaccine immunogenicity in UC patients on tofacitinib. Grade C relevance — unrelated to RA or mesalazine efficacy. |

**Assessment**: Only one trial (NCT02930343) directly tests an RA indication with adequate sample size, and it was terminated without published results. No trial isolates mesalazine's independent effect from sulfasalazine.

### Osteoarthritis (secondary candidate)

Currently no related clinical trials registered.

---

## Literature Evidence

### Rheumatoid Arthritis (primary candidate)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2860942](https://pubmed.ncbi.nlm.nih.gov/2860942/) | 1985 | Clinical comparative study | BMJ | Sulphapyridine, not 5-ASA, showed pronounced second-line antirheumatic effect over 24 weeks; 5-ASA showed only weak first-line effect. |
| [2877851](https://pubmed.ncbi.nlm.nih.gov/2877851/) | 1986 | Clinical comparative study | Drugs | 30 RA patients treated with either 5-ASA or sulphapyridine alone; sulphasalazine-comparable improvement seen with sulphapyridine, not with 5-ASA. |
| [2899645](https://pubmed.ncbi.nlm.nih.gov/2899645/) | 1988 | Cohort | J Rheumatol | Sulfasalazine treatment normalized elevated activated-lymphocyte levels in RA patients after 12 weeks; mode of action still unclear. |
| [8535642](https://pubmed.ncbi.nlm.nih.gov/8535642/) | 1995 | Comparative review | Br J Rheumatol | Reviews evidence favoring sulphapyridine over 5-ASA as the active/toxicity-driving moiety in RA treatment. |
| [7588084](https://pubmed.ncbi.nlm.nih.gov/7588084/) | 1995 | Review | Drugs | Comprehensive review establishing sulfasalazine as a DMARD since the 1940s; active-moiety question (parent drug vs. sulfapyridine vs. mesalazine) remains uncertain. |
| [10743803](https://pubmed.ncbi.nlm.nih.gov/10743803/) | 2000 | Ex vivo mechanistic | J Rheumatol | Sulfasalazine and metabolites' effects on inflammatory cytokine/MMP mRNA levels in rheumatoid synovial fibroblasts. |
| [12235076](https://pubmed.ncbi.nlm.nih.gov/12235076/) | 2002 | Pharmacovigilance/safety cohort | Gut | Re-evaluation of serious adverse reactions reported to the UK Committee on Safety of Medicines for sulphasalazine and mesalazine. |
| [7904547](https://pubmed.ncbi.nlm.nih.gov/7904547/) | 1993 | Review | Clin Pharmacokinet | Reviews pharmacokinetics of slow-acting antirheumatic drugs including sulphasalazine; notes delayed onset of clinical effect (months). |
| [41443863](https://pubmed.ncbi.nlm.nih.gov/41443863/) | 2025 | Case report | Intern Med (Tokyo) | Case of 5-ASA-induced colitis in an RA patient without underlying IBD, following sulfasalazine then mesalazine exposure — relevant safety signal for RA population use. |
| [7781502](https://pubmed.ncbi.nlm.nih.gov/7781502/) | 1995 | Review | Dtsch Med Wochenschr | General review of mesalazine pharmacology (abstract not available). |

### Osteoarthritis (secondary candidate)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38310093](https://pubmed.ncbi.nlm.nih.gov/38310093/) | 2024 | Preclinical mechanistic | Nature Communications | 5-ASA suppresses osteoarthritis via the OSCAR-PPARγ axis, competing with extracellular matrix signaling implicated in cartilage/bone destruction. |
| [1673814](https://pubmed.ncbi.nlm.nih.gov/1673814/) | 1991 | Ex vivo human tissue pharmacology | Wien Klin Wochenschr | Sulfasalazine and metabolites (incl. 5-ASA) inhibit prostaglandin/leukotriene release from human synovial tissue in OA, chondrocalcinosis, and RA patients. |
| [38491514](https://pubmed.ncbi.nlm.nih.gov/38491514/) | 2024 | Bioinformatics target identification | J Transl Med | Computational identification of OA therapeutic targets by integrating transcriptomic and drug-target interaction datasets. |

---

## Taiwan Market Information

Mesalazine currently has no marketed products or drug licenses registered in Taiwan (0 authorizations). No approved indication text is available for this drug in the Taiwan regulatory record.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available in this evidence pack — this is flagged as a **Blocking** data gap (DG001: TFDA package insert warnings/contraindications), meaning a formal safety pre-assessment (S1) cannot yet be completed at the candidate level.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Rheumatoid Arthritis specifically; all other predicted indications remain on **Hold**)

**Rationale:**
Rheumatoid arthritis has the only indication-relevant, adequately-powered clinical trial (though terminated) plus decades of literature on sulfasalazine/mesalazine in RA. However, the evidence base directly questions whether mesalazine itself (versus sulfapyridine) is the active component for RA efficacy, and the drug is entirely unregistered in Taiwan with no available safety labeling — both must be resolved before any clinical advancement. Osteoarthritis is mechanistically promising but preclinical-only and should remain a research question, not an action item. The remaining five predictions lack any supporting evidence and should not be pursued.

**To proceed, the following is needed:**
- TFDA/original manufacturer package insert (warnings, contraindications) — currently a Blocking gap
- Formal drug-drug interaction data
- A trial or pharmacological study isolating mesalazine's independent antirheumatic effect from sulfapyridine
- Published results from NCT02930343 (terminated Phase 3 RA trial), if obtainable from the sponsor
- Confirmation of original approved indication(s) and mechanism of action from DrugBank/manufacturer sources
- Regulatory pathway assessment given the drug is currently unregistered in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

