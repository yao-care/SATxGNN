---
layout: default
title: Pantoprazole
parent: 僅模型預測 (L5)
nav_order: 475
evidence_level: L5
indication_count: 6
---

# Pantoprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Pantoprazole: From Acid-Related GI Disorders to Active Peptic Ulcer Disease

## One-Sentence Summary

Pantoprazole is a proton pump inhibitor (PPI); this evidence pack does not carry a formal local original-indication record (drug is not currently marketed under a local license). TxGNN's top-ranked prediction is **Active Peptic Ulcer Disease**, but the model's own rationale flags this as an *existing core indication* rather than a novel repurposing target, with **3 clinical trials** and **19 publications** currently supporting the mechanism-disease link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on file locally (0 licenses); TFDA label and MOA data are pending (Data Gap DG001, DG002) |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L1 |
| Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed local mechanism-of-action documentation is not on file for this evidence pack (Data Gap DG002). However, the accompanying model rationale identifies Pantoprazole as an **irreversible proton pump inhibitor (H+/K+-ATPase inhibitor)**: it binds covalently to the gastric parietal cell proton pump, blocking the final step of acid secretion — the first-line mechanism for treating acid-peptic disease.

Importantly, the model's own reasoning for this top-ranked prediction states explicitly that acid suppression via H+/K+-ATPase inhibition **is not a repurposing mechanism but the drug's core, already-established indication** for peptic ulcer disease — making it the strongest possible mechanistic link in the dataset, but also the least "new."

Practically, this means the TxGNN score here should be read as a **validation signal** (the model correctly recovers a known drug-disease relationship) rather than a genuine repurposing discovery. For an actual novel-use case, later-ranked candidates in this evidence pack (e.g., peptic ulcer perforation, L2 evidence) may be more informative, since Pantoprazole's role there is explicitly noted as adjunctive/indirect rather than core.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Multicenter, randomized, double-blind, active-controlled comparison of Ilaprazole vs. Pantoprazole triple therapy (7 days) for H. pylori eradication in gastric/duodenal ulcer patients |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated influence of statins and PPIs (including pantoprazole) on clopidogrel antiplatelet effect in patients on dual antiplatelet therapy after PCI — a safety/DDI study, not an ulcer-efficacy endpoint |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | Completed | 316 | Prospective study identifying risk factors for poor SRH fading or early rebleeding after endoscopic hemostasis + high-dose PPI infusion, to define selection criteria for second-look endoscopy |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | RCT | Hepato-gastroenterology | Compared lansoprazole vs. pantoprazole efficacy in active duodenal ulcer treatment and H. pylori eradication |
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | Prospective RCT: intermittent vs. continuous pantoprazole infusion for peptic ulcer bleeding/rebleeding prevention |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | RCT | Aliment Pharmacol Ther | Compared three pantoprazole-based triple therapy regimens for H. pylori eradication and gastric ulcer healing |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | RCT | J Gastroenterol Hepatol | Prospective RCT: pantoprazole infusion as adjuvant to endoscopic therapy reduced rebleeding after peptic ulcer bleeding |
| [9678814](https://pubmed.ncbi.nlm.nih.gov/9678814/) | 1998 | RCT | Aliment Pharmacol Ther | Two-week pantoprazole + amoxicillin/clarithromycin effective for H. pylori eradication and duodenal ulcer healing |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Review | Am J Gastroenterol | Network meta-analysis comparing P-CAB vs. PPI (including pantoprazole) efficacy/safety in healing Grade C/D esophagitis |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Overview of pantoprazole pharmacology; notes no significant drug-drug interactions identified across interaction studies |
| [9017763](https://pubmed.ncbi.nlm.nih.gov/9017763/) | 1997 | Review | Pharmacotherapy | Reviews PPI mechanism (H+/K+-ATPase inhibition) and comparative efficacy vs. H2-receptor antagonists in acid-related disease |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | Clinical | Aliment Pharmacol Ther | Pantoprazole + amoxicillin + azithromycin/clarithromycin regimens for H. pylori eradication in duodenal ulcer |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Preclinical | Inflammopharmacology | Pantoprazole + mesenchymal stem cells accelerated healing of experimentally induced gastric ulcer in rats (oxidative stress/inflammation/apoptosis pathways) |

## Saudi Arabia Market Information

Pantoprazole is not currently marketed under any local license — 0 authorizations on record.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level is L1, supported by a completed Phase 3 RCT and multiple additional RCTs on pantoprazole in peptic ulcer/H. pylori treatment. However, the mechanistic rationale itself confirms this is Pantoprazole's established core indication, not a novel repurposing finding — the guardrail requirement stems from the missing local regulatory and safety record, not from evidentiary uncertainty about efficacy.

**To proceed, the following is needed:**
- TFDA package insert / local label data (Data Gap DG001, blocking — required before any S1 safety review)
- Formal DrugBank/MOA record for this evidence pack (Data Gap DG002)
- Confirmation of original approved indications to properly frame this as "known use" vs. "new use" in any filing
- DDI and contraindication data (current query returned no results)
- If a genuine repurposing opportunity is the goal, evaluate rank 2 ("peptic ulcer perforation," L2, adjunctive mechanism) instead, since rank 1 largely validates known pharmacology rather than expanding it
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

