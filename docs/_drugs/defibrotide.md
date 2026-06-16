---
layout: default
title: Defibrotide
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
---

# Defibrotide
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

# Defibrotide: From Hepatic Veno-Occlusive Disease to Thrombotic Thrombocytopenic Purpura

## One-Sentence Summary

Defibrotide is a polydeoxyribonucleotide antithrombotic agent with established international use in hepatic veno-occlusive disease / sinusoidal obstruction syndrome (VOD/SOS) following hematopoietic stem cell transplantation (HSCT), though it is not currently registered in Taiwan.
The TxGNN model predicts potential efficacy across 10 platelet and vascular disorders; among these, **Thrombotic Thrombocytopenic Purpura (TTP)** carries the strongest evidence base, supported by **11 publications** spanning case reports, case series, reviews, and a 2023 in vitro translational study — though no dedicated clinical trials have been registered for this indication.
The highest-scoring TxGNN prediction (pseudo-von Willebrand disease, 99.91%) lacks any supporting evidence and remains at Hold stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hepatic Veno-Occlusive Disease / Sinusoidal Obstruction Syndrome (VOD/SOS) post-HSCT (inferred from Phase 3 trial NCT02851407; no Taiwan registration) |
| Predicted New Indication (Highest Evidence) | Thrombotic Thrombocytopenic Purpura (TTP) — TxGNN Rank #4 |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L3 (case series, observational studies, in vitro translational study) |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Defibrotide is a single-stranded polydeoxyribonucleotide (derived from porcine intestinal mucosa) whose clinical success in VOD/SOS reflects a multi-modal mechanism centered on restoring endothelial homeostasis under microvascular stress. While detailed MOA data is unavailable in the current data package, its known actions include: stimulating endothelial release of prostacyclin (PGI₂) and tissue plasminogen activator (tPA), downregulating adhesion molecules (E-selectin, VCAM-1), and signaling through adenosine receptors (A1/A2) to dampen platelet activation and microvascular thrombosis.

TTP and VOD/SOS share a critical common pathology: widespread microvascular endothelial injury driving platelet-rich microthrombus formation and end-organ ischemia. In TTP, ADAMTS13 deficiency allows ultra-large vWF multimers to accumulate in the circulation, triggering uncontrolled platelet adhesion and consumption — precisely the endothelial–platelet axis that Defibrotide's mechanism opposes through PGI₂ induction and adhesion molecule suppression. This mechanistic overlap creates a biologically plausible rationale for repurposing.

The strongest contemporary evidence comes from a 2023 translational study (PMID 37001283) that directly demonstrated Defibrotide's ability to mitigate endothelial cell injury caused by plasmas from COVID-19 patients with TTP/aHUS-like thrombotic microangiopathies. This in vitro finding, combined with a coherent series of historical clinical reports dating from 1984 to 2002, provides a consistent mechanistic-to-clinical evidence thread. One important caveat: PMID 7896218 (1994) documents a case of TTP occurring *following* Defibrotide administration — whether causal or coincidental, this signal must be treated as a priority safety monitoring item in any future prospective study.

---

## All Predicted Indications — Summary

| Rank | Indication | TxGNN Score | Evidence Level | Decision |
|------|-----------|-------------|----------------|----------|
| 1 | Pseudo-von Willebrand disease | 99.91% | L5 | Hold |
| 2 | Primary release disorder of platelets | 99.91% | L4 | Research Question |
| 3 | Glanzmann thrombasthenia | 99.88% | L5 | Hold |
| **4** | **Thrombotic thrombocytopenic purpura** | **99.71%** | **L3** | **Proceed with Guardrails** |
| 5 | Scott syndrome | 99.67% | L5 | Hold |
| 6 | Bleeding diathesis due to collagen receptor defect | 99.43% | L5 | Hold |
| 7 | Hemorrhagic disorder due to constitutional thrombocytopenia | 99.39% | L5 | Hold |
| 8 | Congenital factor V deficiency | 99.30% | L5 | Hold |
| 9 | Fetal and neonatal alloimmune thrombocytopenia | 99.23% | L5 | Hold |
| 10 | Thrombocytopenic purpura (broad category) | 99.22% | L3 | Research Question |

**Note on Hold recommendations:** Ranks 1, 3, 5, 6, 7, 8, 9 are mechanistically incompatible with Defibrotide's known pharmacology (gene-defect disorders, PS-flipase pathway diseases, receptor-deficiency disorders) and should not advance without major new mechanistic evidence.

---

## Clinical Trial Evidence

No clinical trials specifically targeting TTP with Defibrotide are currently registered. The Phase 3 trial below is the primary approved-indication trial and provides the most complete safety database for Defibrotide in an HSCT context, with indirect relevance to platelet and endothelial endpoints shared with TTP.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02851407](https://clinicaltrials.gov/study/NCT02851407) | Phase 3 | Completed | 372 | Defibrotide vs best supportive care for VOD/SOS prevention in high-risk adult and pediatric HSCT patients; primary FDA-registration trial for Defibrotide — provides comprehensive safety and tolerability database; HSCT setting overlaps with TTP-adjacent platelet consumption and endothelial injury events |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37001283](https://pubmed.ncbi.nlm.nih.gov/37001283/) | 2023 | Translational/In vitro | Thrombosis Research | Defibrotide directly mitigates microvascular endothelial cell injury induced by COVID-19 plasmas; protective against TTP/aHUS/VOD-associated microangiopathy pathways in vitro — strongest contemporary mechanistic link |
| [11960280](https://pubmed.ncbi.nlm.nih.gov/11960280/) | 2002 | Case Series | Bone Marrow Transplantation | Defibrotide described as a promising treatment for TTP in bone marrow transplant patients |
| [10775024](https://pubmed.ncbi.nlm.nih.gov/10775024/) | 2000 | Case Report | Clin Appl Thromb Hemost | Defibrotide induced medium-to-long-term remission in patients with recurrent TTP refractory to standard plasma exchange |
| [8317470](https://pubmed.ncbi.nlm.nih.gov/8317470/) | 1993 | Case Series | Am J Hematol | Case series demonstrating clinical response to defibrotide treatment in TTP |
| [6547211](https://pubmed.ncbi.nlm.nih.gov/6547211/) | 1984 | Pilot Study | Nephron | Early pilot study of a new antithrombotic agent (defibrotide) in acute renal failure due to HUS and TTP |
| [3754836](https://pubmed.ncbi.nlm.nih.gov/3754836/) | 1986 | Observational | Haemostasis | Defibrotide in acute renal failure caused by thrombotic microangiopathy; early evidence of anti-TMA activity |
| [19228075](https://pubmed.ncbi.nlm.nih.gov/19228075/) | 2009 | Review | Drugs | Comprehensive review of TA-TMA diagnosis and treatment in HSCT; Defibrotide mentioned among therapeutic options for a condition with 60–90% mortality despite treatment |
| [17603513](https://pubmed.ncbi.nlm.nih.gov/17603513/) | 2007 | Review | Bone Marrow Transplantation | TA-TMA management review: highlights pathophysiological overlap with TTP and endothelial injury shared with Defibrotide's target mechanism |
| [30305540](https://pubmed.ncbi.nlm.nih.gov/30305540/) | 2018 | Review | Jpn J Clin Hematol | Management of transplant-associated TMA; vascular endothelial insult as central pathogenesis — directly relevant to Defibrotide's endothelial-protective mechanism |
| [7896218](https://pubmed.ncbi.nlm.nih.gov/7896218/) | 1994 | Adverse Event Report | Haematologica | ⚠️ **Safety Signal**: TTP documented after Defibrotide therapy — causal vs. coincidental relationship unresolved; must be incorporated as a monitoring endpoint in any future prospective study |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **⚠️ Priority Safety Signal**: PMID 7896218 (1994, *Haematologica*) reports a case of TTP occurring after Defibrotide administration. The causal vs. coincidental nature of this event remains unresolved in the literature. Any prospective investigation of Defibrotide in TTP must include TTP exacerbation as a pre-specified safety monitoring endpoint, with pre-planned stopping rules.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Defibrotide's endothelial-protective and anti-platelet-adhesion mechanisms are mechanistically congruent with TTP pathophysiology, a 2023 in vitro study provides direct experimental support, and multiple historical clinical case reports document clinical use in TTP patients — together constituting L3 evidence sufficient to advance to structured investigation.

**To proceed, the following is needed:**
- Complete MOA documentation (DrugBank API query — data gap DG002 pending)
- Review of full package insert warnings and contraindications (data gap DG001)
- Pharmacovigilance adjudication of PMID 7896218 adverse event signal before designing TTP studies
- Pilot investigator-initiated trial (IIT) or registry study in the HSCT-associated TMA/TTP subpopulation, where Defibrotide is already co-administered for VOD prophylaxis — enabling opportunistic observation of TTP endpoints
- Drug-drug interaction profile assessment (no DDI data currently available)
- Pre-IND regulatory consultation on feasibility of an indication expansion from VOD/SOS to TTP
- Taiwan registration pathway assessment: Defibrotide is not currently marketed in Taiwan; compassionate use or accelerated review eligibility for orphan TTP indication should be explored
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

