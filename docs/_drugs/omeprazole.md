---
layout: default
title: Omeprazole
parent: 僅模型預測 (L5)
nav_order: 463
evidence_level: L5
indication_count: 2
---

# Omeprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Omeprazole: From Peptic Ulcer Disease to Duodenogastric Reflux

## One-Sentence Summary

Omeprazole is a proton pump inhibitor originally used for peptic ulcer disease, GERD, and H. pylori eradication (a well-established indication not captured in this Evidence Pack's Saudi licensing data, since the drug is currently unmarketed there). The TxGNN model predicts it may be effective for **Duodenogastric Reflux (DGR)**, but the supporting evidence is limited to **1 non-therapeutic clinical trial** and **20 publications**, several of which raise a mechanistic safety concern rather than confirm benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease / GERD / *H. pylori* eradication *(general knowledge — not present in the Saudi licensing data, which shows no authorizations)* |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (DG002, High severity). Based on known pharmacology, omeprazole irreversibly inhibits the gastric H⁺/K⁺-ATPase to suppress acid secretion — a mechanism proven effective for acid-related disorders such as peptic ulcer disease and GERD.

However, the core pathology of duodenogastric reflux is not acid excess but reflux of alkaline duodenal content (bile acids, pancreatic enzymes, lysolecithin) into the stomach. Omeprazole does not act directly on this mechanism. The repurposing rationale extracted from this Evidence Pack is explicitly cautious: several preclinical studies (PMID 33027361, PMID 10389684) suggest that acid suppression with omeprazole may *prolong* mucosal exposure to bile reflux and has been associated with promotion of gastric carcinogenesis in DGR animal models. Some clinical cohort studies in Barrett's esophagus (PMID 10994616, PMID 9824338) do suggest omeprazole can reduce measured duodenogastric/duodenogastroesophageal reflux parameters, but this is a secondary physiological effect rather than a validated treatment indication for DGR itself.

In short, the mechanistic link is weak and directionally ambiguous — plausible symptomatic modulation is counterbalanced by an unresolved preclinical safety signal, which is why this candidate sits at Evidence Level L4 with a Hold recommendation rather than proceeding further.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | Phase NA | Completed | 157 | Evaluated endoscopic tri-modal imaging (NBI/AFI/WLI) to distinguish functional dyspepsia from reflux disease (acid or bile). This is a diagnostic imaging study, not a treatment trial of omeprazole for DGR. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Review | European Journal of Pediatrics | Describes primary duodenogastric reflux in children/adolescents, refractory to classical antacid therapy. |
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | Cohort | Scandinavian Journal of Gastroenterology | Long-term omeprazole therapy in Barrett's esophagus was associated with reduced antral duodenogastric reflux. |
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | Cohort | Gut | Omeprazole 20mg twice daily assessed for effect on duodenogastric and duodenogastro-oesophageal bile reflux in Barrett's esophagus. |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | Cohort | Acta Cirúrgica Brasileira | Rat model of DGR; investigated whether omeprazole and nitrites have a protective or promoting effect on gastric mucosa/adenocarcinoma risk. |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | Cohort | Digestive Diseases and Sciences | Rat model: gastric acid blockade with omeprazole promoted gastric carcinogenesis induced by DGR — a safety signal. |
| [8076761](https://pubmed.ncbi.nlm.nih.gov/8076761/) | 1994 | Cohort | Gastroenterology | Examined relationship of pH and duodenogastroesophageal reflux to esophageal mucosal damage and Barrett's esophagus. |
| [11552908](https://pubmed.ncbi.nlm.nih.gov/11552908/) | 2001 | Cohort | Alimentary Pharmacology & Therapeutics | PPI therapy (pantoprazole) reduced acid reflux but effect on biliary reflux and esophageal motility was less clear. |
| [9841990](https://pubmed.ncbi.nlm.nih.gov/9841990/) | 1998 | Cohort | Journal of Gastrointestinal Surgery | Assessed bile reflux in Barrett's esophagus and effect of medical acid suppression vs. Nissen fundoplication. |
| [21916229](https://pubmed.ncbi.nlm.nih.gov/21916229/) | 2011 | Cohort | Experimental & Clinical Gastroenterology | Characterized DGR in duodenal ulcer patients and its dynamics after *H. pylori* eradication. |
| [11232672](https://pubmed.ncbi.nlm.nih.gov/11232672/) | 2001 | Cohort | American Journal of Gastroenterology | Compared acid/bile reflux in Barrett's esophagus vs. reflux esophagitis and the effect of PPI therapy. |

## Saudi Arabia Market Information

Omeprazole currently has no marketing authorization records in Saudi Arabia (0 authorizations; market status: Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information. *(Key warnings, contraindications, and drug interaction data are not available in this Evidence Pack — TFDA/SFDA package insert extraction (DG001) is flagged as a Blocking data gap.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for omeprazole in DGR is weak and partly contradicted by preclinical evidence suggesting acid suppression may promote gastric carcinogenesis under DGR conditions; the only registered trial is a diagnostic imaging study, not a treatment trial, and no evidence directly tests omeprazole's efficacy against DGR as a primary endpoint.

**To proceed, the following is needed:**
- TFDA/SFDA package insert warnings and contraindications (DG001, Blocking — required before any S1 safety review)
- Confirmed mechanism of action data (DG002)
- A dedicated clinical study testing omeprazole safety/efficacy specifically in DGR patients (not derived from Barrett's esophagus or GERD sub-analyses)
- Resolution of the preclinical carcinogenesis-promotion signal (PMID 10389684, 33027361) before any further advancement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

