---
layout: default
title: Vinorelbine
parent: 僅模型預測 (L5)
nav_order: 667
evidence_level: L5
indication_count: 10
---

# Vinorelbine
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

Using the txgnn-pipeline skill wasn't a fit here (that skill covers model training/deployment, not individual report authoring), so I'm producing the report directly from the Evidence Pack per the given template.

# Vinorelbine: From Non-Small Cell Lung Cancer to Ewing Sarcoma

## One-Sentence Summary

Vinorelbine (Navelbine) is a semi-synthetic vinca alkaloid chemotherapy agent whose established clinical use, per the literature evidence in this pack, centers on non-small cell lung cancer (NSCLC) and metastatic breast cancer.
The TxGNN model predicts it may be effective for **Ewing Sarcoma**, with **4 clinical trials** and **5 publications** currently supporting this direction — though none provide Ewing-sarcoma-specific molecular targeting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Saudi Arabia license on record (drug not marketed); established literature describes use in non-small cell lung cancer and metastatic breast cancer |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.9990% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Blocking/High data gaps for TFDA warnings and formal MOA respectively). Based on known information, Vinorelbine is a semi-synthetic vinca alkaloid that binds tubulin to block spindle-microtubule assembly, arresting cells in mitosis and triggering apoptosis. Its established efficacy — per the literature in this pack — is in non-small cell lung cancer (single-agent and cisplatin combinations) and metastatic breast cancer.

Ewing sarcoma is a highly proliferative small round-cell sarcoma of childhood and young adulthood. Because vinorelbine's cytotoxic mechanism is broadly antiproliferative rather than pathway-specific, it has plausible activity against any rapidly dividing tumor, including pediatric sarcomas — this is the general biological rationale behind the TxGNN prediction.

However, the supporting evidence is largely indirect: completed Phase II data (NCT00003234, PMID 22633624) demonstrate vinorelbine activity in relapsed/refractory pediatric solid tumors and sarcomas broadly, with the strongest efficacy signal actually reported in **rhabdomyosarcoma** rather than Ewing sarcoma specifically. No Ewing-sarcoma-specific molecular target or biomarker evidence exists; the mechanistic link is best characterized as "broad-spectrum cytotoxic agent applied to a high-proliferation tumor class," not disease-specific pharmacology.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003234](https://clinicaltrials.gov/study/NCT00003234) | Phase 2 | Completed | 50 | Phase II study of Navelbine (vinorelbine) in children with recurrent or refractory malignancies, including sarcoma populations; drug and population directly relevant. |
| [NCT00180947](https://clinicaltrials.gov/study/NCT00180947) | Phase 2 | Unknown | 210 | Vinorelbine + cyclophosphamide in refractory/relapsed rhabdomyosarcoma, Ewing tumors, osteosarcoma, neuroblastoma, and medulloblastoma; drug-specific but outcome status unknown. |
| [NCT05999994](https://clinicaltrials.gov/study/NCT05999994) | Phase 2 | Recruiting | 105 | CAMPFIRE — pediatric/young-adult multi-cancer master protocol platform trial; whether a vinorelbine-specific treatment arm is included is unconfirmed. |
| [NCT06451302](https://clinicaltrials.gov/study/NCT06451302) | N/A | Active, not recruiting | 100 | Prospective multicenter cohort study of risk-stratification-oriented treatment outcomes/safety in pediatric Ewing sarcoma (China); vinorelbine not specifically named as the study drug. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Phase II Trial | European Journal of Cancer | Vinorelbine + continuous low-dose oral cyclophosphamide in children/young adults with relapsed/refractory solid tumors; good tolerance, notable efficacy specifically in rhabdomyosarcoma. |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Phase II Trial (rhabdomyosarcoma, non-Ewing-specific) | Cancer | Vinorelbine activity in previously treated advanced childhood sarcomas, with evidence of activity concentrated in rhabdomyosarcoma. |
| [37637411](https://pubmed.ncbi.nlm.nih.gov/37637411/) | 2023 | Review | Frontiers in Pharmacology | Comprehensive review of chemotherapeutic drug options for soft tissue sarcomas, including vinca alkaloids. |
| [26260582](https://pubmed.ncbi.nlm.nih.gov/26260582/) | 2016 | Preclinical (synergy study) | International Journal of Cancer | PLK1 inhibitor synergizes with microtubule-interfering drugs (including vinorelbine) to induce apoptosis in Ewing sarcoma cells in vitro. |
| [36451163](https://pubmed.ncbi.nlm.nih.gov/36451163/) | 2022 | Case Report | BMC Urology | Case report/review of extraosseous Ewing sarcoma/pPNET of the kidney; disease-descriptive, not a vinorelbine treatment study. |

## Saudi Arabia Market Information

Currently no Saudi Arabia market authorization is on record for Vinorelbine (`market_status: 未上市`, 0 licenses).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic chemotherapy (Vinca alkaloid class, tubulin-binding antimicrotubule agent) |
| Myelosuppression Risk | High — literature in this pack (PMID 9535205) identifies myelosuppression as the dose-limiting toxicity of vinorelbine |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential (neutrophil count), liver and renal function |
| Handling Protection | Standard cytotoxic drug handling precautions apply (vinca alkaloid); confirm against TFDA/Saudi-specific handling protocol once obtained |

## Safety Considerations

Please refer to the package insert for safety information (key warnings, contraindications, and DDI data are all currently unavailable — DDI query returned no results).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Ewing sarcoma signal (L2 evidence) rests on Phase II trials whose clearest efficacy is in rhabdomyosarcoma rather than Ewing sarcoma specifically, and a Blocking data gap (missing TFDA/regulatory warnings and contraindications) means this candidate cannot yet enter S1 safety review. The drug also currently has no market authorization in Saudi Arabia.

**To proceed, the following is needed:**
- TFDA/Saudi package insert safety data (warnings, contraindications) — Blocking gap, required before any S1 safety assessment
- Formal DrugBank-sourced mechanism of action and toxicity classification
- Confirmation of whether NCT05999994 (CAMPFIRE) and NCT06451302 include a vinorelbine-specific treatment arm
- Follow-up on NCT00180947 (status: Unknown) for unpublished outcome data
- Regulatory pathway assessment for Saudi Arabia market entry, since the drug is not currently marketed there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

