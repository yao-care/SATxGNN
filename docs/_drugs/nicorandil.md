---
layout: default
title: Nicorandil
parent: 僅模型預測 (L5)
nav_order: 440
evidence_level: L5
indication_count: 7
---

# Nicorandil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Nicorandil: From Angina Pectoris to Benign Prostatic Hyperplasia

## One-Sentence Summary

Nicorandil is a potassium-channel opener / nitric oxide donor classically used for angina pectoris (this original-indication detail is not present in the current regulatory data pack and is stated here as general pharmacological background, not as sourced Saudi Arabia data). The TxGNN model predicts it may be effective for **Benign Prostatic Hyperplasia (BPH)**, but currently only **3 preclinical/mechanistic publications** support this direction, with **no registered clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Angina pectoris (general pharmacological knowledge; not available in the Saudi Arabia regulatory record, as the drug is not marketed there) |
| Predicted New Indication | Benign Prostatic Hyperplasia (disease) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 (preclinical / mechanism studies only) |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data from the drug record itself is not available (`original_moa` is a data gap). However, the evidence pack's repurposing rationale identifies nicorandil as a dual-action vasodilator: a KATP channel opener and a nitric oxide (NO) donor.

There is a proposed "vascular dysfunction" hypothesis for BPH/lower urinary tract symptoms (LUTS), in which impaired prostatic blood flow (ischemia) contributes to prostatic hyperplasia, and this is associated with atherosclerotic risk factors such as hypertension. Since nicorandil's core pharmacology is vasodilation, the theoretical link is that improving prostatic blood flow could relieve LUTS.

This is an indirect, organ-perfusion-based mechanistic link rather than a direct hit on the primary molecular pathway of BPH (androgen/AR signaling). The connection is of moderate strength and currently rests on animal and mechanistic studies rather than human clinical data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31735753](https://pubmed.ncbi.nlm.nih.gov/31735753/) | 2019 | Review | Nihon Yakurigaku Zasshi (Folia Pharmacologica Japonica) | Reviews prostatic blood flow as a target in BPH; notes clinical association between BPH/BPE and atherosclerotic disease (e.g., hypertension) via impaired lower urinary tract blood supply. |
| [26165338](https://pubmed.ncbi.nlm.nih.gov/26165338/) | 2015 | Cohort/Pilot (inferred) | Nihon Yakurigaku Zasshi (Folia Pharmacologica Japonica) | Discusses LUTS as a vascular dysfunction and the effect of nicorandil as a vasodilator; abstract text not available. |
| [24448152](https://pubmed.ncbi.nlm.nih.gov/24448152/) | 2014 | Animal study | Scientific Reports | In spontaneously hypertensive rats, 6 weeks of nicorandil treatment was used to study prostatic blood flow and ventral prostatic hyperplasia, supporting a prostatic-ischemia mechanism for BPH development. |

## Saudi Arabia Market Information

Nicorandil is not currently marketed in Saudi Arabia (0 authorizations on record); no license or product information is available.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all currently unavailable — DDI query returned no results, and the TFDA/regulatory package insert data required for a formal safety screen is flagged as a blocking data gap.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The BPH hypothesis rests entirely on one animal study and two review/mechanistic articles (Evidence Level L4), with no clinical trials in humans and no registered ICTRP studies. Combined with the fact that regulatory/package-insert safety data is a blocking gap (cannot yet complete a preliminary safety screen) and the drug is unmarketed in Saudi Arabia, there is currently insufficient basis to advance beyond a research question.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications) to clear the blocking safety data gap
- Confirmed original indication and detailed MOA sourced from an authoritative drug reference (DrugBank API or equivalent)
- Preclinical or early human data specifically linking KATP-channel/NO-donor vasodilation to prostatic volume or LUTS symptom outcomes
- If pursued, a Phase 2 proof-of-concept trial in BPH/LUTS patients, given no clinical trials currently exist for this indication

*Note: Four additional lower-ranked predictions (alopecia, hypotrichosis simplex, congenital hypotrichosis milia, diffuse alopecia areata, osteoarthritis/osteoarthritis susceptibility) were also flagged by TxGNN but carry Evidence Level L5 (model prediction only, no literature or trials) and are all recommended Hold.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

