---
layout: default
title: Pemetrexed
parent: 僅模型預測 (L5)
nav_order: 485
evidence_level: L5
indication_count: 10
---

# Pemetrexed
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

# Pemetrexed: From Malignant Pleural Mesothelioma to Malignant Peritoneal Mesothelioma

## One-Sentence Summary

Pemetrexed is a multitargeted antifolate chemotherapy agent whose established use is in malignant pleural mesothelioma (standard first-line combination with cisplatin) and non-squamous NSCLC. The TxGNN model predicts it may also be effective for **Malignant Peritoneal Mesothelioma**, a rare, biologically related mesothelial-origin tumor, with **11 clinical trials** and **20 publications** currently supporting this direction.

*Note: The structured `original_indications` and `taiwan_regulatory.licenses` fields in this evidence pack are empty (data gap), but the pack's own literature and clinical-trial evidence confirm pemetrexed's established role in pleural mesothelioma — this is explicitly flagged in the rationale for related candidates in this pack.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malignant pleural mesothelioma / non-squamous NSCLC (established indications per literature evidence in this pack; structured regulatory field is a data gap) |
| Predicted New Indication | Malignant Peritoneal Mesothelioma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Pemetrexed is a multitargeted antifolate that inhibits thymidylate synthase (TS), dihydrofolate reductase (DHFR), and glycinamide ribonucleotide formyltransferase (GARFT) — key folate-dependent enzymes required for de novo purine and thymidine biosynthesis. This mechanism is confirmed repeatedly across the literature evidence in this pack (e.g., PMID 31569615, PMID 26538423), even though the drug-level `original_moa` field itself is marked as a data gap.

Malignant peritoneal mesothelioma (MPeM) and malignant pleural mesothelioma (MPM) are both cancers arising from mesothelial cells lining serosal cavities, sharing the same cell of origin, histology, and asbestos-related etiology — they differ mainly by anatomic site (peritoneum vs. pleura). Because cisplatin-pemetrexed is the guideline-recognized standard first-line regimen for MPM, oncologists have long extrapolated this regimen to MPeM as an accepted off-label standard, given the absence of a dedicated approved regimen for the rarer peritoneal form (as explicitly noted in this pack's rationale: "屬廣泛接受之 off-label 標準治療").

Mechanistically, there is no biological reason antifolate cytotoxicity would behave differently by anatomic compartment — tumor cell proliferation dependence on folate metabolism is intrinsic to the mesothelial malignant phenotype, not to its cavity of origin. This supports the plausibility of the TxGNN prediction, though the evidence base is composed largely of small retrospective/prospective series and Phase 1/2 trials rather than a dedicated Phase 3 RCT in MPeM specifically.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Phase 1 | Terminated | 85 | ADI-PEG 20 (arginine-degrading enzyme) + pemetrexed/cisplatin in arginine-dependent tumors, including advanced peritoneal mesothelioma dose-escalation cohort |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | Active, not recruiting | 30 | TRC102 (methoxyamine) + cisplatin/pemetrexed in advanced solid tumors and mesothelioma refractory to pemetrexed/cisplatin |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | Recruiting | 66 | Randomized trial: carboplatin+pemetrexed+bevacizumab ± atezolizumab as neoadjuvant/palliative therapy for peritoneal mesothelioma |
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | Recruiting | 64 | ICARuS II: intraperitoneal vs. intravenous chemotherapy after cytoreductive surgery + HIPEC for malignant peritoneal mesothelioma |
| [NCT01353482](https://clinicaltrials.gov/study/NCT01353482) | Phase 1/2 | Withdrawn | 0 | Vorinostat + pemetrexed-cisplatin first-line in mesothelioma (trial withdrawn before enrollment) |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | Completed | 19 | Cisplatin + pemetrexed + imatinib mesylate dose-finding study in unresectable/metastatic mesothelioma |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Phase 2 | Unknown | 40 | Maintenance talazoparib following first-line platinum-based chemotherapy in pleural or peritoneal mesothelioma |
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | Completed | 48 | Pemetrexed + gemcitabine front-line chemotherapy for pleural or peritoneal mesothelioma |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | Recruiting | 28 | Sintilimab + bevacizumab combined with pemetrexed/cisplatin in unresectable malignant peritoneal mesothelioma |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | Suspended | 66 | MESOTIP: PIPAC + systemic chemotherapy (cisplatin+pemetrexed) vs. systemic chemotherapy alone as 1st-line treatment for malignant peritoneal mesothelioma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospective study | Expert Review of Anticancer Therapy | Evaluates efficacy of first-line systemic pemetrexed + cisplatin chemotherapy in malignant peritoneal mesothelioma |
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Retrospective study | Japanese Journal of Clinical Oncology | Efficacy and safety of pemetrexed + cisplatin as first-line chemotherapy in advanced MPeM; efficacy remains unclear vs. MPM |
| [41133016](https://pubmed.ncbi.nlm.nih.gov/41133016/) | 2025 | Retrospective study | Clinical Medicine Insights: Oncology | Compares first-line pemetrexed-platinum vs. gemcitabine-platinum regimens in MPeM |
| [33743636](https://pubmed.ncbi.nlm.nih.gov/33743636/) | 2021 | Retrospective study | BMC Cancer | Efficacy of second-line treatment and prognostic factors in advanced MPeM following first-line cisplatin+pemetrexed |
| [31417959](https://pubmed.ncbi.nlm.nih.gov/31417959/) | 2019 | Cohort (Tier 2) | Pleura and Peritoneum | Bidirectional chemotherapy (incl. pemetrexed-based regimens) enabling surgery/HIPEC in unresectable MPeM |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | Case report | BMJ Case Reports | MPeM patient responding to rechallenge with cisplatin + pemetrexed after progression |
| [33257382](https://pubmed.ncbi.nlm.nih.gov/33257382/) | 2020 | Case report | BMJ Case Reports | Nivolumab used as later-line therapy for MPeM after initial systemic chemotherapy |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Review (Tier 3) | Translational Lung Cancer Research | Overview of MPeM epidemiology, pathology, and treatment approaches |
| [26941986](https://pubmed.ncbi.nlm.nih.gov/26941986/) | 2016 | Review (Tier 3) | Journal of Gastrointestinal Oncology | Diagnosis and management of patients with MPeM |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review (Tier 3) | Journal of Clinical Medicine | Review of treatment options for MPeM, including surgical cytoreduction/HIPEC and systemic chemotherapy |

---

## Saudi Arabia Market Information

Pemetrexed is currently **not marketed** in this jurisdiction (`market_status = 未上市`), with **0 registered authorizations** in this evidence pack. No product listings are available to tabulate.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — antifolate class (thymidylate synthase / DHFR / GARFT inhibitor), consistent with mechanism described across the literature evidence in this pack |
| Myelosuppression Risk | Not detailed in this evidence pack — please refer to the package insert for haematological toxicity data |
| Emetogenicity Classification | Not detailed in this evidence pack — please refer to the package insert |
| Monitoring Items | Not detailed in this evidence pack; standard antifolate monitoring (CBC with differential, renal and hepatic function) is recommended pending package insert confirmation |
| Handling Protection | Cytotoxic drug handling precautions apply; follow local cytotoxic handling regulations and the package insert |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not available in this evidence pack — DDI query status: not found.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong (shared mesothelial origin, established antifolate activity), and multiple Phase 1/2 trials plus retrospective series directly support pemetrexed-based regimens in malignant peritoneal mesothelioma as a widely accepted off-label extension of the MPM standard of care. However, evidence is limited to small/retrospective studies (no dedicated Phase 3 RCT in MPeM specifically), and this candidate carries a **Blocking** data gap on TFDA package insert warnings/contraindications, preventing a full S1 safety evaluation.

**To proceed, the following is needed:**
- TFDA package insert PDF (warnings, contraindications) — currently Blocking (DG001)
- DrugBank-confirmed mechanism of action data — currently High priority gap (DG002)
- Drug-drug interaction (DDI) data (currently "not found")
- Confirmation of original approved indication(s) and regulatory/license status (currently blank in `taiwan_regulatory.licenses`)
- Consideration of whether a peritoneal-mesothelioma-specific Phase 3 RCT is feasible given disease rarity, or whether guideline extrapolation from MPM evidence is accepted as sufficient
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

