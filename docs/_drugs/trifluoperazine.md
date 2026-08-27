---
layout: default
title: Trifluoperazine
parent: 僅模型預測 (L5)
nav_order: 638
evidence_level: L5
indication_count: 1
---

# Trifluoperazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Trifluoperazine: From Antipsychotic Use to Manic Bipolar Affective Disorder

## One-Sentence Summary

Trifluoperazine is a phenothiazine-class antipsychotic historically used to manage psychotic disorders; the specific approved indication text is not present in the current dataset. The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, with **0 clinical trials** and **20 publications** currently identified, though none of the literature has yet been fully classified for study design or direct relevance.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in available regulatory data (DrugBank/SFDA license text not returned); literature consistently describes trifluoperazine as a phenothiazine antipsychotic |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on the supporting literature, trifluoperazine belongs to the phenothiazine class of antipsychotics, and its dopaminergic antagonism is consistent with mechanisms implicated in mania — one identified study (PMID 970489) directly links dopaminergic activity to manic episodes, providing mechanistic plausibility for antimanic effect.

Historically, trifluoperazine and related phenothiazines have been used clinically to manage agitation and affective symptoms alongside primary antipsychotic use — several older reports in the evidence set (e.g., PMID 14084030, PMID 13761179) describe its use in combination regimens for agitated depression and affective disturbance, and broader reviews (PMID 17017818, PMID 24943390) document antipsychotic use, including phenothiazines, across bipolar disorder treatment settings. This existing precedent of psychiatric use, combined with the class-level mechanistic rationale, supports the biological plausibility of the TxGNN prediction, though no study in the current evidence set directly tests trifluoperazine as a treatment for bipolar mania in a controlled trial.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14084030](https://pubmed.ncbi.nlm.nih.gov/14084030/) | 1963 | Double-blind study | Current Therapeutic Research, Clinical and Experimental | Double-blind study of trifluoperazine withdrawal in patients maintained on tranylcypromine + trifluoperazine combination therapy |
| [17017818](https://pubmed.ncbi.nlm.nih.gov/17017818/) | 2006 | Review | The Journal of Clinical Psychiatry | Reviews efficacy of typical and atypical antipsychotics for anxiety symptoms in bipolar disorder and major depression |
| [19461391](https://pubmed.ncbi.nlm.nih.gov/19461391/) | 2009 | Review | Journal of Psychiatric Practice | Reviews use and safety of antipsychotic drugs (including phenothiazines) during pregnancy in psychotic and bipolar illness |
| [40926568](https://pubmed.ncbi.nlm.nih.gov/40926568/) | 2026 | Review | Journal of Applied Toxicology | Reviews phenothiazine derivatives, noting their long-standing use in mania associated with bipolar disorder and psychosis |
| [24943390](https://pubmed.ncbi.nlm.nih.gov/24943390/) | 2014 | Cross-sectional survey | Journal of Clinical Psychopharmacology | Survey of psychotropic prescription patterns in Ugandan psychiatric inpatients, including bipolar affective disorder cohorts |
| [6636782](https://pubmed.ncbi.nlm.nih.gov/6636782/) | 1983 | Case series | Wiener Klinische Wochenschrift | Describes MAO-inhibitor plus lithium/neuroleptic regimens in rapid-cycling manic-depressive patients resistant to standard therapy |
| [970489](https://pubmed.ncbi.nlm.nih.gov/970489/) | 1976 | Mechanistic case study | The American Journal of Psychiatry | Explores dopaminergic mechanisms in mania using dopamine-stimulating and -blocking agents, supporting a dopaminergic model of manic illness |
| [2544917](https://pubmed.ncbi.nlm.nih.gov/2544917/) | 1989 | Case-control study | Psychiatry Research | Examines platelet adrenergic receptor binding differences across depressive, schizophrenic, and bipolar patient groups |
| [13761179](https://pubmed.ncbi.nlm.nih.gov/13761179/) | 1961 | Case series | The American Journal of Psychiatry | Reports on combined tranylcypromine-trifluoperazine therapy in patients with agitated depression |
| [3935307](https://pubmed.ncbi.nlm.nih.gov/3935307/) | 1985 | Case report | Canadian Journal of Psychiatry | Case report of bipolar disorder presenting in an adolescent, discussing diagnostic and treatment considerations |

## Saudi Arabia Market Information

Trifluoperazine currently has no registered market authorizations in Saudi Arabia (market status: Not Marketed; 0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available in this dataset; DG001 flags SFDA package insert retrieval as a Blocking gap for safety evaluation.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a strong TxGNN score and reasonable class-level mechanistic support, but there are no clinical trials directly testing trifluoperazine in bipolar mania, and a Blocking data gap (missing SFDA/package insert safety data) currently prevents even an initial safety (S1) assessment.

**To proceed, the following is needed:**
- SFDA package insert data (warnings, contraindications) — currently Blocking (DG001)
- Confirmed mechanism of action from DrugBank — currently High severity gap (DG002)
- Drug-drug interaction data (current query returned no results)
- Prospective or retrospective clinical evidence specifically evaluating trifluoperazine in manic bipolar affective disorder, beyond historical combination-therapy reports
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

