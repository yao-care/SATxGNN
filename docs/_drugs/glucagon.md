---
layout: default
title: Glucagon
parent: 僅模型預測 (L5)
nav_order: 295
evidence_level: L5
indication_count: 1
---

# Glucagon
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

# Glucagon (DB00040): Original Indication Not on File → Predicted Signal for Irritable Bowel Syndrome (Likely False Positive)

## One-Sentence Summary

The Evidence Pack does not contain data on glucagon's original approved indication or mechanism of action (both flagged as data gaps). The TxGNN model predicts a possible new indication for **Irritable Bowel Syndrome (IBS)** with a high score (99.24%), but the underlying **10 clinical trials** and **20 publications** almost entirely study **GLP-1 receptor agonists** (ROSE-010, liraglutide, exendin-4) — a different drug class acting on the opposite receptor from glucagon (GCGR). The repurposing rationale itself flags this as likely an entity-confusion artifact in the knowledge graph, not a genuine pharmacological signal for glucagon.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no data in this Evidence Pack) |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for glucagon is not available in this Evidence Pack (marked as a High-severity data gap), and no original indication is on file. Based on general pharmacology, glucagon is a glucagon receptor (GCGR) agonist that raises blood glucose via hepatic glycogenolysis and gluconeogenesis, and its recognized GI use is limited to transient smooth-muscle relaxation (antispasmodic effect during endoscopy/imaging) — not a mechanism aimed at chronic IBS management.

**This prediction should be treated with caution rather than as reasonable support for repurposing.** Nearly all of the supporting clinical trials and literature involve **GLP-1 receptor agonists** (ROSE-010, liraglutide, exendin-4, native GLP-1) — a pharmacologically distinct class that acts on GLP-1R, not GCGR. Although glucagon and GLP-1 both derive from the same preproglucagon gene via tissue-specific post-translational processing, their downstream receptors and physiological effects are essentially opposite (GLP-1 inhibits GI motility and lowers glucose; glucagon promotes glycogenolysis and raises glucose). The high TxGNN score most likely reflects gene/family-level over-linkage between glucagon and GLP-1 nodes in the knowledge graph rather than a real pharmacological basis for glucagon itself treating IBS. Of the 11 clinical trials retrieved, 10 were explicitly graded "C" (not relevant — wrong drug entity) by the evidence review; none support glucagon as an IBS therapy.

## Clinical Trial Evidence

*Note: nearly all trials below study GLP-1 receptor agonists (ROSE-010, liraglutide, exendin-4) or unrelated dietary/lifestyle interventions — not glucagon. They are listed for transparency but were graded low relevance ("C") to the glucagon→IBS prediction.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | Studied ROSE-010 (GLP-1 analog, not glucagon) on GI motor function in constipation-predominant IBS |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Native GLP-1 and analog ROSE-010 inhibit prandial GI motility; mechanistic study, not glucagon |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | Terminated | 8 | Liraglutide (GLP-1 agonist) for chronic high bowel frequency post-IPAA; opposite mechanism to glucagon |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Completed | 66 | Exercise training effects on gut dysbiosis and GLP-1 hormone in IBS; no drug intervention |
| [NCT04230655](https://clinicaltrials.gov/study/NCT04230655) | N/A | Unknown | 110 | Low-calorie diet + intragastric balloon for obesity; unrelated to glucagon or IBS pharmacology |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | N/A | Completed | 12 | Reactive hypoglycemia and fructo-oligosaccharide supplementation; no glucagon intervention |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | N/A | Completed | 37 | Butyrate's role in colon health/IBS; unrelated to glucagon |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | N/A | Completed | 41 | Eating rate of ultra-processed foods and metabolic response; unrelated to glucagon |
| [NCT06333717](https://clinicaltrials.gov/study/NCT06333717) | N/A | Completed | 33 | Whole grain rye bread effect on gut-brain axis in healthy subjects; unrelated to glucagon |
| [NCT04111263](https://clinicaltrials.gov/study/NCT04111263) | N/A | Completed | 33 | Gut-microbiota-targeted nutrition for barrier integrity under hypoxia; unrelated to glucagon |

## Literature Evidence

*Note: literature below concerns GLP-1 receptor agonists/endogenous GLP-1, not glucagon itself.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | RCT | Scand J Gastroenterol | ROSE-010 (GLP-1 agonist) reduces pain during IBS attacks; subgroup analysis of responders |
| [22517769](https://pubmed.ncbi.nlm.nih.gov/22517769/) | 2012 | RCT | Am J Physiol Gastrointest Liver Physiol | ROSE-010 dose-response study on GI motor/bowel function in IBS-C |
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic Review | Frontiers in Endocrinology | GLP-1 receptor agonists (incl. ROSE-010) inhibit migrating motor complex, improving IBS symptoms |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Experimental Physiology | Endogenous GLP-1 from gut L-cells implicated in IBS pathophysiology |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Review | Expert Opin Investig Drugs | Reviews investigational drugs for IBS-C, including GLP-1-class agents |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Cohort | Clin Res Hepatol Gastroenterol | Decreased serum GLP-1 correlates with abdominal pain in IBS-C patients |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Preclinical | Neurogastroenterol Motil | Exendin-4 (GLP-1 agonist) ameliorated GI dysfunction in a rat IBS model |
| [23338623](https://pubmed.ncbi.nlm.nih.gov/23338623/) | 2013 | Preclinical | Int J Mol Med | GLP-1's role in pathogenesis of experimental IBS-C and IBS-D rat models |
| [31311066](https://pubmed.ncbi.nlm.nih.gov/31311066/) | 2019 | Preclinical | Neurogastroenterol Motil | Ghrelin sensitizes colonic neurons to exendin-4, linked to postprandial IBS symptoms |
| [40880735](https://pubmed.ncbi.nlm.nih.gov/40880735/) | 2025 | Cohort | Frontiers in Nutrition | Low FODMAP diet increases circulating GLP-1 in IBS patients |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a decision-stage S0 signal with Evidence Level L4, and the repurposing rationale flags a probable knowledge-graph entity confusion between glucagon (GCGR agonist) and GLP-1 receptor agonists — the drug class that actually underlies nearly all supporting trials and literature. Proceeding to a repurposing evaluation without resolving this would risk acting on a false-positive signal.

**To proceed, the following is needed:**
- Resolve the glucagon/GLP-1 entity ambiguity in the knowledge graph before any further scoring or reporting on this candidate
- Obtain glucagon's confirmed original indication and mechanism of action (DrugBank API query — Data Gap DG002)
- Obtain TFDA/manufacturer package insert warnings and contraindications (Data Gap DG001, Blocking severity — required before any S1 safety pre-assessment)
- If a genuine glucagon-specific mechanistic hypothesis for IBS exists (e.g., via its antispasmodic GI effect), source trials/literature that study glucagon directly rather than GLP-1 receptor agonists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

