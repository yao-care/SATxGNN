---
layout: default
title: Buprenorphine
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 6
---

# Buprenorphine
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

以下是根據 Evidence Pack 生成的評估報告：

---

# Buprenorphine: From Opioid Dependence & Pain to Acute Intermittent Porphyria

## One-Sentence Summary

Buprenorphine is a partial mu-opioid receptor agonist clinically established for opioid use disorder (OUD) management and pain relief. The TxGNN model predicts it may be relevant for **Acute Intermittent Porphyria (AIP)**, with **0 clinical trials** and **1 publication** (a 1993 perioperative case report) currently available to support this direction. Overall evidence remains at an early preclinical/mechanistic hypothesis stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Opioid use disorder / Analgesia (original indication data not available in this dataset; derived from drug class) |
| Predicted New Indication | Acute Intermittent Porphyria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| Taiwan (TFDA) Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known information, buprenorphine is a partial mu-opioid receptor agonist (and kappa-opioid antagonist), whose analgesic and OUD treatment efficacy has been extensively established. Its metabolic pathway primarily involves CYP3A4-mediated glucuronidation rather than pathways that heavily intersect with porphyrin biosynthesis.

Acute Intermittent Porphyria is a rare metabolic disorder caused by defects in the heme biosynthesis pathway. During acute attacks, patients can suffer from severe neuropathic abdominal pain, autonomic dysfunction, and neurological complications. A key clinical challenge in AIP is that many commonly used analgesics and anesthetic agents — particularly barbiturates and certain inducers of CYP enzymes — can trigger or worsen porphyric crises by upregulating ALA-synthase.

The mechanistic link here is therefore not that buprenorphine treats AIP itself, but that it may be **relatively safe to use for pain management in AIP patients**: its CYP3A4 glucuronidation pathway theoretically poses less risk of triggering porphyrinogenic enzyme induction compared to barbiturates or other hazardous agents. This is an important clinical distinction — the prediction reflects safety-in-indication rather than disease-modifying efficacy — and substantially limits the translational scope.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for buprenorphine in acute intermittent porphyria.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Case Report | Masui (Japanese Journal of Anesthesiology) | Perioperative anesthetic management of a 40-year-old female with AIP undergoing radical hysterectomy; describes the challenge of selecting safe agents before AIP was confirmed — buprenorphine noted as a candidate in this context |

---

## Taiwan Market Information

No TFDA-approved products registered for buprenorphine in Taiwan. This drug is not currently marketed in Taiwan.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were available in this dataset.

> **Note for AIP context:** Although formal safety data is unavailable in this Evidence Pack, clinicians should be aware that in AIP patients, drug selection is critical. Agents known to be porphyrinogenic (e.g., barbiturates, certain anticonvulsants) are contraindicated. Buprenorphine's relative safety in AIP should be verified against a porphyria drug safety database (e.g., the European Porphyria Network safe/unsafe drug list at [drugs-porphyria.org](https://www.drugs-porphyria.org)) before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole available evidence is a single 1993 perioperative case report that discusses AIP anesthetic management without directly evaluating buprenorphine as a therapeutic agent for AIP. The mechanistic link is indirect — buprenorphine's potential role is as a pain management option that is *safer to use in AIP patients* rather than as a treatment targeting the underlying metabolic defect. No clinical trials exist, and the evidence level (L4) does not support advancing to a formal repurposing program at this time.

**To proceed, the following is needed:**

- **MOA data (DG002):** Confirm buprenorphine's full receptor pharmacology and metabolic pathway via DrugBank API; verify porphyrinogenic risk classification
- **TFDA/package insert safety data (DG001):** Download and parse the full prescribing information for warnings and contraindications
- **Porphyria drug safety database check:** Cross-reference buprenorphine against established AIP-safe/unsafe drug lists (e.g., drugs-porphyria.org, NAPOS database)
- **Clarify clinical hypothesis:** Determine whether the target claim is (a) buprenorphine is safe to use for pain in AIP patients, or (b) buprenorphine modifies the AIP disease course — these require entirely different evidence standards and study designs
- **Systematic literature search:** A targeted search for "buprenorphine AND porphyria" and "opioids AND AIP pain management" may surface additional evidence not captured in this pipeline run
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

