---
layout: default
title: Sertraline
parent: 僅模型預測 (L5)
nav_order: 571
evidence_level: L5
indication_count: 8
---

# Sertraline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Sertraline: From Panic Disorder to Agoraphobia

## One-Sentence Summary

Sertraline is a selective serotonin reuptake inhibitor (SSRI); this dataset does not carry a confirmed original-indication record (no Saudi Arabia license on file), but sertraline is broadly established internationally for depressive and anxiety-spectrum disorders, including panic disorder. The TxGNN model's most credible new-indication signal in this evidence pack is **Agoraphobia**, supported by **4 clinical trials** (including one completed Phase 4 head-to-head trial) and **19 publications**, several of them meta-analyses and RCTs.

*Note on candidate selection:* This evidence pack scored eight TxGNN-predicted indications for sertraline. The top-ranked-by-score candidates (schizoid, paranoid, schizotypal, histrionic, narcissistic personality disorder; benign paroxysmal torticollis of infancy) each carry Evidence Level L4–L5 and a "Hold" recommendation — the pack's own rationale explicitly flags several as "database association noise" with no plausible mechanistic link. Agoraphobia is the only indication reaching Evidence Level L1 / decision stage S3 ("Proceed with Guardrails"), so it is reported here as the actionable finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this dataset (no Saudi Arabia license record; sertraline is an SSRI-class antidepressant) |
| Predicted New Indication | Agoraphobia |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this dataset (marked as a data gap). Based on known pharmacology, sertraline is an SSRI: it inhibits presynaptic serotonin reuptake, increasing synaptic serotonin availability, which modulates amygdala and limbic-system hyperreactivity — the pathway implicated in panic and phobic-avoidance disorders.

Agoraphobia most commonly presents as a comorbid or downstream feature of panic disorder, and the evidence pack itself notes this is not a novel repurposing hypothesis: sertraline is already approved in many jurisdictions for "panic disorder with or without agoraphobia." The clinical trial and literature evidence below largely reflects this already-established indication rather than a new mechanistic leap, which is why the evidence base is unusually strong (multiple completed RCTs and meta-analyses) compared with the other TxGNN-predicted indications in this pack.

Because Saudi Arabia currently has zero sertraline licenses on file, the practical question is not "does the pharmacology make sense" (it does, and is externally validated) but whether a Saudi market entry/dossier can be supported — which depends on data currently missing from this pack (see Conclusion).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00677352](https://clinicaltrials.gov/study/NCT00677352) | Phase 4 | Completed | 321 | Randomized, double-blind, multicenter comparison of sertraline vs. paroxetine for efficacy and safety in panic disorder |
| [NCT00182533](https://clinicaltrials.gov/study/NCT00182533) | Phase 4 | Terminated | 170 | Sertraline for generalized social phobia with comorbidity (includes agoraphobia-spectrum anxiety); trial terminated |
| [NCT05210153](https://clinicaltrials.gov/study/NCT05210153) | N/A | Unknown | 148 | Plasma level monitoring and CYP2C19 genotyping for sertraline dose personalization (pharmacokinetic study, not an efficacy trial) |
| [NCT05930912](https://clinicaltrials.gov/study/NCT05930912) | N/A | Unknown | 1 | Single-case psychoanalytic treatment study in ASD with comorbid anxiety disorders; low direct relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Meta-analysis | Cochrane Database Syst Rev | Network meta-analysis of pharmacological treatments for panic disorder in adults |
| [35045991](https://pubmed.ncbi.nlm.nih.gov/35045991/) | 2022 | Meta-analysis | BMJ | Network meta-analysis identifying SSRIs, including sertraline, with high remission and low adverse-event rates for panic disorder with/without agoraphobia |
| [9734541](https://pubmed.ncbi.nlm.nih.gov/9734541/) | 1998 | RCT | Am J Psychiatry | Double-blind multicenter trial establishing efficacy and safety of sertraline in panic disorder |
| [9819070](https://pubmed.ncbi.nlm.nih.gov/9819070/) | 1998 | RCT | Arch Gen Psychiatry | Flexible-dose multicenter trial of sertraline in panic disorder |
| [11110009](https://pubmed.ncbi.nlm.nih.gov/11110009/) | 2000 | RCT | Int Clin Psychopharmacol | Pooled analysis of two fixed-dose studies confirming sertraline efficacy in panic disorder with/without agoraphobia |
| [11206597](https://pubmed.ncbi.nlm.nih.gov/11206597/) | 2000 | RCT | J Clin Psychiatry | Sertraline response in panic disorder patients at high risk of poor outcome (including presence of agoraphobia) |
| [12191627](https://pubmed.ncbi.nlm.nih.gov/12191627/) | 2002 | RCT | J Psychiatr Res | Combined data (N=544) from four placebo-controlled sertraline studies; early improvement predicts remission |
| [16505130](https://pubmed.ncbi.nlm.nih.gov/16505130/) | 2006 | RCT | Am J Geriatr Psychiatry | RCT comparing CBT vs. sertraline for anxiety disorders (including agoraphobia) in older adults |
| [15096081](https://pubmed.ncbi.nlm.nih.gov/15096081/) | 2004 | RCT | J Clin Psychiatry | Acute double-blind noninferiority comparison of sertraline vs. paroxetine in panic disorder |
| [16053461](https://pubmed.ncbi.nlm.nih.gov/16053461/) | 2005 | RCT | Bosn J Basic Med Sci | Placebo-controlled comparison of sertraline vs. alprazolam in panic disorder with/without agoraphobia |

*9 additional publications (reviews and further pooled-data analyses) are on file but not listed here for brevity.*

---

## Saudi Arabia Market Information

Sertraline currently holds **no marketing authorization in Saudi Arabia** (0 licenses on file; market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are not currently available in this dataset.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Agoraphobia (in the context of panic disorder) is supported by multiple completed RCTs, pooled analyses, and two recent meta-analyses, and reflects an indication already recognized for sertraline in other jurisdictions — this is confirmatory rather than speculative evidence. However, sertraline has zero existing market presence in Saudi Arabia, and a critical safety data gap currently blocks initial safety assessment.

**To proceed, the following is needed:**
- SFDA/Taiwan package insert data (warnings, contraindications) — currently a **Blocking** gap preventing entry into S1 safety pre-assessment
- Detailed mechanism-of-action documentation from DrugBank
- Drug-drug interaction (DDI) data, currently returning "not found"
- A regulatory pathway assessment for first-time market entry in Saudi Arabia, since no existing license or dosage-form record exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

