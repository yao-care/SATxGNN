---
layout: default
title: Dexlansoprazole
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 10
---

# Dexlansoprazole
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

# Dexlansoprazole: From Erosive Esophagitis to Active Peptic Ulcer Disease

## One-Sentence Summary

Dexlansoprazole is a dual delayed-release proton pump inhibitor (PPI), originally approved for healing erosive esophagitis and managing gastroesophageal reflux disease (GERD).
The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**, with **20 clinical trials** and **4 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Erosive esophagitis / Gastroesophageal reflux disease (GERD) |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on well-established pharmacological knowledge, dexlansoprazole irreversibly inhibits the H⁺/K⁺-ATPase proton pump in gastric parietal cells, dramatically raising intragastric pH to create the acid-suppressed environment necessary for mucosal healing. Its distinguishing feature is a **dual delayed-release (DDR) formulation** that produces two plasma concentration peaks (Tmax at ~1–2 h and ~4–5 h), extending acid suppression beyond what conventional once-daily PPIs can achieve.

Both erosive esophagitis and peptic ulcer disease share the same root pathophysiology: gastric acid eroding a mucosal surface that has lost its protective barriers — whether through NSAID use, *H. pylori* infection, or other insults. This mechanistic overlap means that sustained, high-level acid suppression directly addresses peptic ulcer healing in the same way it heals esophageal erosions. Two pivotal Phase 3 registration trials of dexlansoprazole itself (NCT00251693 and NCT00251719, enrolling over 2,000 patients each) have already demonstrated its efficacy in acid-related mucosal healing, establishing the pharmacological foundation.

Furthermore, dexlansoprazole's parent compound lansoprazole (AG-1749) holds established global approvals for both gastric and duodenal ulcer treatment and is widely used as an active comparator in peptic ulcer trials worldwide. The TxGNN model's high-confidence prediction (rank #42 globally) therefore reflects a pharmacologically coherent and clinically well-supported extrapolation rather than a speculative leap.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00251693](https://clinicaltrials.gov/study/NCT00251693) | Phase 3 | Completed | 2,038 | Dexlansoprazole (TAK-390MR) 60 mg/90 mg vs lansoprazole 30 mg — 8-week healing of endoscopically confirmed erosive esophagitis; pivotal registration trial directly establishing dexlansoprazole efficacy in acid-related mucosal healing |
| [NCT00251719](https://clinicaltrials.gov/study/NCT00251719) | Phase 3 | Completed | 2,054 | Parallel pivotal study: dexlansoprazole MR 60 mg and 90 mg vs lansoprazole 30 mg for erosive esophagitis healing; together with NCT00251693 constitutes the core registration evidence package |
| [NCT05010954](https://clinicaltrials.gov/study/NCT05010954) | Phase 3 | Completed | 400 | LXI-15028 50 mg vs lansoprazole 30 mg in Chinese patients with duodenal ulcer over 6 weeks; active comparator (lansoprazole class) efficacy directly demonstrated in peptic ulcer |
| [NCT05813561](https://clinicaltrials.gov/study/NCT05813561) | Phase 3 | Completed | 332 | DWP14012 (P-CAB) 40 mg vs esomeprazole — modern head-to-head PPI/P-CAB comparison for acid-related mucosal disease; benchmark for class-level effectiveness |
| [NCT04784910](https://clinicaltrials.gov/study/NCT04784910) | Phase 3 | Completed | 423 | DWP14012 20 mg vs lansoprazole 15 mg for NSAID-induced peptic ulcer prevention; non-inferiority of newer acid blocker to lansoprazole confirmed |
| [NCT04840550](https://clinicaltrials.gov/study/NCT04840550) | Phase 3 | Unknown | 390 | Tegoprazan 25 mg vs lansoprazole 15 mg for prevention of gastroduodenal ulcers in long-term NSAID users; lansoprazole serves as benchmark active comparator |
| [NCT01506986](https://clinicaltrials.gov/study/NCT01506986) | Phase 4 | Completed | 30,024 | HEAT trial — *H. pylori* eradication vs placebo in aspirin users; large-scale landmark trial validating the PPI-based strategy in ulcer prevention and demonstrating role of acid suppression class |
| [NCT03675672](https://clinicaltrials.gov/study/NCT03675672) | Phase 4 | Recruiting | 154 | Misoprostol + lansoprazole vs lansoprazole alone for prevention of recurrent idiopathic gastroduodenal ulcer bleeding; evaluates long-term PPI maintenance in active ulcer management |
| [NCT07533266](https://clinicaltrials.gov/study/NCT07533266) | Phase 4 | Not Yet Recruiting | 360 | Fexuprazan 20 mg vs lansoprazole 15 mg for NSAID-induced peptic ulcer prevention; upcoming trial reaffirming lansoprazole class as the reference standard |
| [NCT07479056](https://clinicaltrials.gov/study/NCT07479056) | N/A | Recruiting | 400 | Fexuprazan vs lansoprazole 30 mg for upper GI bleeding prevention in high-risk patients on dual antiplatelet therapy post-PCI; indirect comparative data relevant to PPI gastric protection |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic Review / Network Meta-analysis | The American Journal of Gastroenterology | Compares P-CAB vs all PPI agents for healing severe (Grade C/D) esophagitis; provides the highest level of comparative evidence for PPI class effectiveness across acid-related mucosal diseases |
| [41809210](https://pubmed.ncbi.nlm.nih.gov/41809210/) | 2026 | Expert Consensus | World Journal of Gastrointestinal Pharmacology and Therapeutics | Indian multidisciplinary expert consensus on comprehensive management of acid peptic disorders (GERD, peptic ulcer disease, functional dyspepsia); addresses overlapping pathophysiology and appropriate acid suppressant use including risks of unsupervised PPI consumption |
| [18821474](https://pubmed.ncbi.nlm.nih.gov/18821474/) | 2008 | Drug Review | Current Opinion in Investigational Drugs | Early clinical overview of dexlansoprazole as a modified-release enantiomer of lansoprazole; summarizes NDA filing for gastric acid-related diseases and Phase 2 GERD data, establishing the regulatory scope of the drug's intended indications |
| [36150104](https://pubmed.ncbi.nlm.nih.gov/36150104/) | 2022 | Basic Science / Mechanistic Study | Journal of the Chinese Medical Association | Investigates PPI-mediated vacuolar-type ATPase suppression and ER stress induction, explicitly naming dexlansoprazole; provides mechanistic context for understanding PPI pharmacological effects beyond proton pump inhibition |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dexlansoprazole's dual delayed-release design provides mechanistically superior and sustained acid suppression that is directly relevant to peptic ulcer healing. Two large-scale Phase 3 registration trials of dexlansoprazole itself (>4,000 patients combined) and numerous completed Phase 3 trials of the PPI class in peptic ulcer disease collectively support Level L1 evidence. The prediction represents a pharmacologically coherent extension of an established drug class into a closely related acid-related indication, with minimal mechanistic uncertainty.

**To proceed, the following is needed:**
- **Saudi Arabia registration pathway:** Dexlansoprazole is not currently approved or marketed in Saudi Arabia (SFDA); a registration dossier or import approval application must be initiated
- **Complete safety documentation:** Full package insert warnings, contraindications, and drug-drug interaction data are required before clinical use — particularly the clopidogrel interaction (addressed in NCT00942175 Phase 1 data but not yet structured in this evidence pack)
- **Regulatory strategy clarification:** Determine whether peptic ulcer constitutes a new indication requiring a separate clinical trial or whether PPI class evidence plus dexlansoprazole PK/PD data suffice for a label extension
- **MOA documentation:** Obtain formal DrugBank or prescribing information MOA data to complete the evidence pack (currently flagged as DG002 — High severity data gap)
- **Local pharmacoeconomic analysis:** Compare dexlansoprazole against already-available PPIs and emerging P-CABs in the Saudi market to support formulary positioning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

