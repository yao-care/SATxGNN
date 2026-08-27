---
layout: default
title: Tenecteplase
parent: 僅模型預測 (L5)
nav_order: 605
evidence_level: L5
indication_count: 10
---

# Tenecteplase
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

# Tenecteplase: From ST-Elevation Myocardial Infarction to Coronary Stenosis (Intracoronary PCI Adjunct)

## One-Sentence Summary

Tenecteplase is a fibrin-specific thrombolytic, originally used for reperfusion therapy in acute ST-elevation myocardial infarction (STEMI). Among the ten indications the TxGNN model surfaced for this drug, the only one with substantive supporting evidence is **Coronary Stenosis** — specifically as a low-dose intracoronary adjunct during primary PCI — backed by **1 completed Phase 2 RCT** and **10 relevant publications**. The other nine predicted indications (including the two top-ranked STEMI subtypes) have no clinical trial or literature support and are treated separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ST-elevation myocardial infarction (STEMI) — inferred from the repurposing-rationale narrative in the evidence pack; no formal regulatory indication text is on file because the drug is not marketed locally |
| Predicted New Indication | Coronary Stenosis (low-dose intracoronary tenecteplase as PCI adjunct) |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

**Note on other predicted indications:** TxGNN's two highest-scoring predictions (posteroinferior MI, posterolateral MI, both ~99.87%) and four low-relevance hematologic/chromosomal predictions (beta-thalassemia, chromosome 16p deletion, red-cell enzyme deficiencies) returned **zero** clinical trials or literature — these are treated as L5, model-score-only signals with recommendation "Hold." Septal MI (L4) had only a misdiagnosis case report and unrelated PE literature. Congenital coronary artery anomaly (L4) had a single case report describing **failed** fibrinolysis — a negative signal. Coronary stenosis is the only candidate that reached decision stage S2 with real trial data, so it is the focus of this report.

---

## Why is This Prediction Reasonable?

The evidence pack's `original_moa` field is formally marked as a data gap, but the repurposing-rationale text supplied for this candidate provides mechanistic detail: tenecteplase is a genetically engineered variant of tissue plasminogen activator (tPA) with high fibrin specificity, which catalyzes the conversion of plasminogen to plasmin to degrade thrombus. This is consistent with its established role in STEMI, where it is administered intravenously to dissolve the culprit coronary thrombus.

Coronary stenosis frequently coexists with residual or distal thrombus burden — most clearly in the setting of primary PCI for STEMI, where microvascular obstruction from thrombotic embolization is common even after the epicardial vessel is opened. Using tenecteplase as a **low-dose intracoronary** adjunct during PCI (rather than the standard systemic bolus) targets this residual thrombus directly at the lesion site, which is mechanistically a natural extension of its original antithrombotic action rather than a new mechanism.

This mechanistic overlap is reflected in the trial and literature evidence below: the supporting studies are specifically about intracoronary/adjunctive fibrinolytic use during angioplasty and PCI, not about coronary stenosis as an independent disease process. In other words, the "new indication" is really a new **route and clinical context** (intracoronary, periprocedural) for the same underlying pharmacology, which is why the evidence level (L2) is meaningfully higher than the other nine TxGNN predictions in this pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00604695](https://clinicaltrials.gov/study/NCT00604695) | Phase 2 | Completed | 40 | "ICE T" trial evaluating low-dose intracoronary adjunctive tenecteplase during primary PCI for STEMI; hypothesized to enhance breakdown of residual thrombus at the culprit lesion and reduce myocardial damage. Preliminary angiographic efficacy data only (small, single trial). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31870492](https://pubmed.ncbi.nlm.nih.gov/31870492/) | 2020 | Cohort/Feasibility | American Journal of Cardiology | ICE-T-TIMI-49: feasibility/safety of low-dose intracoronary tenecteplase (4 mg) vs. saline in 40 primary PCI patients — the published readout of NCT00604695. |
| [16053952](https://pubmed.ncbi.nlm.nih.gov/16053952/) | 2005 | pending | Journal of the American College of Cardiology | CAPITAL AMI study: compared tenecteplase-facilitated angioplasty vs. tenecteplase alone in high-risk STEMI. |
| [17102829](https://pubmed.ncbi.nlm.nih.gov/17102829/) | 2006 | RCT-related/Cohort | Canadian Journal of Cardiology | TRANSFER-AMI pilot: feasibility of urgent PCI transfer shortly after thrombolysis for STEMI. |
| [16139127](https://pubmed.ncbi.nlm.nih.gov/16139127/) | 2005 | Case series | Journal of the American College of Cardiology | Pre-procedural intracoronary fibrin-specific lytic infusion facilitates percutaneous recanalization of chronic total occlusions. |
| [31020237](https://pubmed.ncbi.nlm.nih.gov/31020237/) | 2019 | Case report | European Heart Journal – Case Reports | Refractory thrombus extraction with stent retriever during primary angioplasty for acute MI in an ectatic, thrombus-prone coronary segment. |
| [11994554](https://pubmed.ncbi.nlm.nih.gov/11994554/) | 2002 | Observational | Journal of Thrombosis and Thrombolysis | Precordial ST depression in inferior MI associated with angiographic slow flow in the non-culprit LAD (same research group as the ICE-T trial). |
| [37823944](https://pubmed.ncbi.nlm.nih.gov/37823944/) | 2023 | Case report | Egyptian Heart Journal | Subacute stent thrombosis in a resource-limited setting attributed to clopidogrel resistance — illustrates the residual-thrombus problem this adjunct targets. |
| [17461362](https://pubmed.ncbi.nlm.nih.gov/17461362/) | 2007 | pending | Giornale Italiano di Cardiologia | Case of right ventricular ischemia mimicking acute MI during angioplasty of the right coronary artery. |
| [23615379](https://pubmed.ncbi.nlm.nih.gov/23615379/) | 2013 | Review | Cerebrovascular Diseases | Historical review of thrombolytic agents (streptokinase to tenecteplase) — general fibrinolytic-class background, not coronary-stenosis-specific. |
| [25733729](https://pubmed.ncbi.nlm.nih.gov/25733729/) | 2016 | Case report | Human & Experimental Toxicology | Thrombolytic therapy in inferolateral MI following carbon monoxide poisoning-induced coronary thrombosis. |

---

## Saudi Arabia Market Information

Tenecteplase is not currently marketed in Saudi Arabia — no product authorizations are on file (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. Local key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack (flagged as a **Blocking**-severity data gap — see Conclusion below); as a fibrinolytic agent, bleeding risk should be assumed material until confirmed otherwise.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only predicted indication with real supporting evidence — coronary stenosis as an intracoronary PCI adjunct — rests on a single small (n=40), completed Phase 2 feasibility/safety trial with no confirmatory Phase 3 outcomes data, and tenecteplase has no market presence or regulatory safety file locally. This does not meet the bar for "Go" or even guarded proceeding; it remains a research question rather than a repurposing-ready candidate. The other nine TxGNN predictions in this pack lack any clinical or literature support (several are mechanistically implausible genetic/hematologic conditions) and should not be advanced.

**To proceed, the following is needed:**
- TFDA/local package insert (warnings, contraindications) — currently a **Blocking** data gap that prevents any S1 safety pre-assessment
- Confirmed original-indication and MOA documentation via DrugBank (currently a **High**-severity data gap)
- A Phase 3 (or larger Phase 2) RCT on intracoronary tenecteplase as a PCI adjunct with clinical outcome endpoints, not just angiographic feasibility
- Local DDI and bleeding-risk data before any safety evaluation can begin
- If revisited, re-screen the remaining nine predictions only if new trial or literature evidence emerges — none currently warrant active development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

