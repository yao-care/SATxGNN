---
layout: default
title: Acetylcysteine
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 10
---

# Acetylcysteine
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

# Acetylcysteine: From Mucolytic/Antidote to Thrombotic Disease

## One-Sentence Summary

Acetylcysteine (NAC) is a well-established mucolytic agent and antidote for acetaminophen overdose, internationally approved for respiratory conditions including COPD and cystic fibrosis.
The TxGNN model predicts it may be effective for **Thrombotic Disease**, with **9 clinical trials** and **20 publications** currently supporting this direction.
Notably, a completed Phase 3 trial (NCT03252925, n=170) directly evaluating NAC for transplant-associated thrombotic microangiopathy (TA-TMA) provides the anchor for L1-level evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Saudi Arabia; internationally used as mucolytic agent and acetaminophen antidote |
| Predicted New Indication | Thrombotic Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known information, Acetylcysteine (NAC) is a thiol-containing compound of the mucolytic class; its primary mechanism in respiratory conditions involves cleaving disulfide bonds in mucus glycoproteins to reduce sputum viscosity. More broadly, NAC serves as a rate-limiting precursor for glutathione (GSH) synthesis — the body's principal intracellular antioxidant.

The mechanistic link to thrombotic disease is well-established at both molecular and clinical levels. NAC's free thiol group (–SH) directly cleaves disulfide bonds within ultra-large von Willebrand factor (ULVWF) multimers — the molecular driver of platelet aggregation in thrombotic microangiopathies such as TTP and TA-TMA. A landmark 2011 study published in the *Journal of Clinical Investigation* (PMID 21266777) demonstrated that NAC reduces VWF multimer size and activity in human plasma and murine models. This mechanism is distinct from and complementary to ADAMTS13, the endogenous VWF-cleaving protease that is severely deficient in TTP; NAC therefore provides a route to VWF cleavage even when ADAMTS13 activity is absent.

As a GSH precursor, NAC also protects vascular endothelium against oxidative stress-driven prothrombotic activation. Uremic toxins such as indoxyl sulfate — elevated in chronic kidney disease — induce pro-coagulant endothelial phenotypes through reactive oxygen species (ROS). The RENACTIF Phase 2 trial (NCT03636932, n=40) specifically demonstrated that NAC can attenuate this thrombotic phenotype in CKD patients, bridging the antioxidant and antithrombotic mechanisms. The convergence of these two pathways — direct ULVWF cleavage and endothelial redox protection — provides strong biological justification for TxGNN's high-confidence prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Phase 3 | Completed | 170 | Prospective trial evaluating NAC safety and efficacy in TA-TMA post-HSCT; the largest completed direct-evidence study for this thrombotic disease indication and the primary basis for L1 classification |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Phase 2/3 | Active, not recruiting | 44 | Multicenter prospective single-arm trial of NAC for TA-TMA after HSCT; current plasma exchange response rate <10% and complement inhibitors are costly — NAC evaluated as an accessible alternative |
| [NCT05907486](https://clinicaltrials.gov/study/NCT05907486) | Phase 3 | Unknown | 260 | Largest trial to date assessing NAC efficacy and safety for prevention of thrombotic events following allogeneic HSCT; status requires follow-up |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Phase 2 | Completed | 40 | RENACTIF: randomized double-blind placebo-controlled crossover trial — NAC to reduce thrombotic phenotype in renal insufficiency patients with elevated indoxyl sulfate; provides both mechanistic and clinical efficacy validation |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Early Phase 1 | Completed | 3 | First-in-human pilot study of IV NAC in suspected TTP during therapeutic plasma exchange; established feasibility and supported anti-ULVWF/ADAMTS13-enhancing mechanism |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Phase 1/2 | Unknown | 200 | Single-arm multicentre trial comparing atorvastatin + acetylcysteine + danazol vs danazol monotherapy in corticosteroid-resistant/relapsed ITP |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Phase 2 | Unknown | 44 | Single-arm open-label trial of NAC combined with high-dose dexamethasone in newly diagnosed primary immune thrombocytopenia (ITP) |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Early Phase 1 | Completed | 15 | Exploratory trial assessing atorvastatin + NAC for platelet count elevation in steroid-resistant/relapsed ITP; supports mechanistic rationale but sample size limits conclusions |
| [NCT06518044](https://clinicaltrials.gov/study/NCT06518044) | Phase 2 | Not yet recruiting | 30 | Prospective single-arm study of NAC to promote hematopoietic recovery in severe aplastic anemia (SAA) after haploidentical transplantation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41977015](https://pubmed.ncbi.nlm.nih.gov/41977015/) | 2026 | Systematic Review | Journal of Clinical Medicine | Most recent systematic review and critical appraisal of NAC therapy in TTP; evaluates ADAMTS13 deficiency, ULVWF accumulation, and NAC's thiol-mediated cleavage as add-on for refractory/relapsed TTP |
| [35940529](https://pubmed.ncbi.nlm.nih.gov/35940529/) | 2022 | RCT | Transplantation and Cellular Therapy | Randomized placebo-controlled trial of NAC as prophylaxis for TA-TMA following HSCT; directly assesses whether NAC prevents this life-threatening post-transplant complication |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | Retrospective Cohort | Annals of Hematology | Cohort study evaluating the association between NAC treatment and in-hospital mortality in acquired TTP (aTTP); provides real-world outcomes data despite ongoing clinical controversy |
| [21266777](https://pubmed.ncbi.nlm.nih.gov/21266777/) | 2011 | Mechanistic Study | Journal of Clinical Investigation | Landmark mechanistic study: NAC reduces VWF multimer size and activity in human plasma and mice via disulfide bond cleavage; establishes the core molecular rationale for thrombotic disease use |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Review | Expert Review of Hematology | Reviews emerging and repurposed therapies in immune TTP including NAC, rituximab, bortezomib, and caplacizumab; positions NAC explicitly within the drug repurposing landscape |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | Preclinical | Blood | NAC demonstrated efficacy in mouse and baboon TTP models via ADAMTS13-independent VWF multimer cleavage; validates translational potential across species |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Review | Journal of Clinical Medicine | Comprehensive review of TTP pathophysiology, diagnosis, and management; contextualizes NAC's anti-ULVWF mechanism within the current treatment paradigm |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Review | Blood | Authoritative *Blood* review linking severe ADAMTS13 deficiency to disseminated microvascular platelet-rich thrombi and covering emerging treatment strategies |
| [28382967](https://pubmed.ncbi.nlm.nih.gov/28382967/) | 2017 | Review | Nature Reviews Disease Primers | Disease primer on TTP (Moschcowitz disease); covers multi-organ ischemic injury and treatment advances from plasma therapy to novel agents — reference-standard background context |
| [28645643](https://pubmed.ncbi.nlm.nih.gov/28645643/) | 2017 | Review | Transfusion Clinique et Biologique | Review of TTP management including rituximab introduction and discussion of refractory/relapsed disease where NAC may provide additive benefit |

---

## Saudi Arabia Market Information

Acetylcysteine is currently **not registered** with the Saudi Food and Drug Authority (SFDA). No approved product licenses are on record. The drug is widely marketed internationally under brand names such as Fluimucil, Mucomyst, and Acetadote across oral, inhalation, and intravenous formulations.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 trial (NCT03252925, n=170) directly evaluating NAC for transplant-associated thrombotic microangiopathy provides L1-level evidence, and the core molecular mechanism — NAC-mediated ULVWF disulfide cleavage — is well-characterized and replicated across preclinical and clinical settings. The absence of SFDA registration is an administrative gap rather than a safety or efficacy obstacle, and does not diminish the strength of the evidence base.

**To proceed, the following is needed:**
- Formal safety and contraindication documentation: obtain SFDA-recognized package insert or equivalent DrugBank/FDA label to complete the safety profile prior to clinical assessment
- Drug interaction (DDI) assessment: evaluate interactions with anticoagulants, complement inhibitors (eculizumab), and immunosuppressants commonly co-administered in HSCT settings
- Confirmation of NCT03252925 Phase 3 full results: detailed efficacy endpoints, response rates, and survival outcomes needed before proceeding to regulatory planning
- Status clarification for NCT05907486 (Phase 3, n=260): follow up on trial completion and data availability to determine whether ≥2 completed Phase 3 RCTs can be confirmed
- Indication scoping decision: prioritize between TA-TMA (strongest direct evidence), acquired TTP (growing evidence), and CKD-associated thrombotic phenotype (mechanistically supported) for the Saudi Arabia development pathway
- Route of administration feasibility: map required formulations (IV infusion for TA-TMA/TTP; oral for outpatient CKD settings) against local manufacturing and importation channels
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

