---
layout: default
title: Ceritinib
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Ceritinib
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

# Ceritinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Ceritinib is a second-generation anaplastic lymphoma kinase (ALK) tyrosine kinase inhibitor, approved in multiple jurisdictions for ALK-positive non-small cell lung cancer (NSCLC), but not currently marketed in Saudi Arabia.
The TxGNN model predicts it may be effective for **Gingival Fibromatosis**, yet there are currently **0 clinical trials** and **0 publications** directly supporting this indication.
This prediction appears to reflect knowledge graph topological proximity rather than any established biological mechanism, and does not support clinical translation at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive Non-Small Cell Lung Cancer (inferred from drug class; no Saudi Arabia authorization on record) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on published literature embedded in the Evidence Pack, ceritinib is a potent, selective second-generation ALK (anaplastic lymphoma kinase) inhibitor. It works by blocking ALK tyrosine kinase activity and its downstream oncogenic signaling cascades — including RAS-MAPK and PI3K-AKT pathways — thereby inhibiting the proliferation and survival of cancer cells harboring ALK gene rearrangements. The landmark ASCEND-4 Phase 3 trial (PMID 28126333) established first-line efficacy in ALK-rearranged NSCLC, and ceritinib received FDA Breakthrough Therapy designation for this indication in 2014 (PMID 24980964).

Gingival fibromatosis is a benign fibrous proliferative disorder of the gums, driven primarily by CTGF/TGF-β-mediated fibroblast activation and collagen overproduction. There is no established connection between ALK signaling and the pathogenesis of this condition. The TxGNN model assigns a high score (99.86%), but the repurposing rationale within the Evidence Pack explicitly attributes this to knowledge graph topological proximity rather than direct biological mechanism — no direct pathway link has been identified.

Beyond the mechanistic disconnect, the risk-benefit calculus is severely unfavorable: ceritinib is a systemic cytotoxic-class targeted therapy with documented GI toxicity, hepatotoxicity, QT prolongation risk, and pulmonary toxicity. Applying such a drug to a benign condition manageable by surgical intervention cannot be justified without compelling mechanistic or preclinical evidence, neither of which currently exists. This prediction is best understood as computational noise.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Ceritinib is not currently authorized for marketing in Saudi Arabia. No license records are on file in this dataset.

---

## Cytotoxicity

Ceritinib is an antineoplastic agent (ALK-positive NSCLC indication; targeted kinase inhibitor class). The following applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Second-generation ALK tyrosine kinase inhibitor (TKI) |
| Myelosuppression Risk | Low to moderate; less hematologic toxicity than conventional cytotoxics, but anemia and neutropenia have been reported in post-marketing surveillance (PMID 34864500 — FDA FAERS analysis) |
| Emetogenicity Classification | Moderate to high; nausea, vomiting, and diarrhea are the predominant dose-limiting toxicities at the 750 mg fasted dose; the ASCEND-8 trial demonstrated that 450 mg with food significantly reduces GI adverse events (PMID 35344649) |
| Monitoring Items | Liver function (ALT/AST/bilirubin), QTc interval (ECG before and during treatment), blood glucose (hyperglycemia risk), complete blood count, pulmonary symptoms (interstitial lung disease / pneumonitis), and bradycardia |
| Handling Protection | Required — oral targeted antineoplastic; follow institutional cytotoxic drug handling and disposal regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Formal warnings and contraindications data were not retrievable for this dataset (Data Gap: TFDA package insert parsing pending). From published post-marketing evidence, clinically significant signals include QT prolongation (PMID 26008987, PMID 29413968), severe hepatotoxicity, interstitial lung disease, and hypersensitivity reactions including diffuse infiltrative lung disease and pericarditis (PMID 31280988). Drug interaction data were not found in the query log. Prescribers should consult the full approved label before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no biologically plausible mechanism linking ALK inhibition to gingival fibromatosis — a benign fibrous condition driven by CTGF/TGF-β rather than ALK signaling — and the Evidence Pack contains zero clinical trials and zero supporting publications for this indication. The TxGNN high score (99.86%) is explicitly attributed to graph topological proximity and should not be interpreted as mechanistic support.

**To proceed, the following would be needed:**

- Evidence of ALK expression or activating mutations in gingival fibromatosis tissue (molecular profiling data)
- Preclinical in vitro or in vivo data demonstrating ceritinib activity in gingival fibroblast proliferation models
- A proposed mechanistic link connecting ALK signaling to CTGF/TGF-β pathways in gingival fibrosis
- Retrieval of formal MOA data from DrugBank (currently data gap — DrugBank API query recommended)
- Full safety profile from the SFDA-approved package insert or EMA/FDA label (TFDA insert parsing currently pending)
- Re-evaluation against higher-ranked indications with mechanistic plausibility (e.g., Rank 6 — Lung Germ Cell Tumor, which has 1 completed Phase 0 trial and 10 supporting publications, and carries a "Research Question" designation at S1)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

