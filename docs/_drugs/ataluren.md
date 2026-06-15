---
layout: default
title: Ataluren
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 6
---

# Ataluren
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

# Ataluren: From Nonsense Mutation Duchenne Muscular Dystrophy to Benign Recurrent Intrahepatic Cholestasis

## One-Sentence Summary

Ataluren (Translarna) is a small-molecule premature termination codon (PTC) readthrough agent, conditionally approved in Europe for treating Duchenne muscular dystrophy caused by nonsense mutations (nmDMD). The TxGNN model predicts it may be effective for **benign recurrent intrahepatic cholestasis (BRIC)**, with the broader cluster of cholestatic and bilirubin metabolism diseases supported by **1 indirect clinical trial** and **1 in vitro publication**. No direct clinical evidence exists for the top-ranked indication, and the current recommendation is **Hold** pending genotype stratification and preclinical validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Nonsense mutation Duchenne muscular dystrophy (nmDMD) |
| Predicted New Indication | Benign recurrent intrahepatic cholestasis (BRIC) |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ataluren's mechanism of action is to promote ribosomal readthrough of premature stop codons (PTCs) introduced by nonsense mutations — it allows the ribosome to skip past a disease-causing stop signal, partially restoring functional protein production. This mechanism is mutation-type-dependent, not disease-specific: in principle, it can apply to any single-gene disorder where a nonsense mutation is the pathogenic cause, regardless of which organ system is affected.

Benign recurrent intrahepatic cholestasis (BRIC) is a rare genetic disease caused by mutations in one of two genes: ATP8B1 (causing BRIC type 1) or ABCB11 (causing BRIC type 2). In patients who carry a nonsense mutation in either gene, ataluren's readthrough mechanism could theoretically restore partial transporter protein function at the canalicular membrane, potentially reducing the frequency or severity of cholestatic episodes. This mechanistic bridge from nmDMD to BRIC is scientifically coherent but remains untested.

Among the broader cluster of TxGNN-predicted cholestatic indications, **familial intrahepatic cholestasis (PFIC2)** offers the most compelling mechanistic anchoring. A 2021 in vitro study (PMID 32702170, published in *Hepatology*) directly tested PTC readthrough agents against six ABCB11 nonsense mutations in PFIC2 cell models, demonstrating restoration of BSEP (bile salt export pump) protein — the same gene implicated in BRIC2. While this does not constitute clinical evidence, it confirms that the molecular hypothesis is experimentally tractable.

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked indication (BRIC). The following trial appears under the related bilirubin metabolism disease cluster and is the only ataluren trial identified across all six predicted indications:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01141075](https://clinicaltrials.gov/study/NCT01141075) | Phase 2 | Terminated | 11 | Ataluren in nonsense mutation methylmalonic acidemia (MMA) — a different inborn metabolic error, not a cholestatic or bilirubin disease. Classified as Grade C relevance: provides indirect mechanistic support showing ataluren can be studied in nonsense mutation metabolic diseases, but cannot be cited as direct evidence for any cholestatic indication. Trial terminated early; efficacy not established. |

---

## Literature Evidence

No literature is available directly supporting the top-ranked indication (BRIC). The following publication is identified under the familial intrahepatic cholestasis prediction cluster:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [32702170](https://pubmed.ncbi.nlm.nih.gov/32702170/) | 2021 | Preclinical / In vitro | Hepatology | Tested pharmacological PTC readthrough (including ataluren) against six ABCB11 nonsense mutations in a PFIC2 cell model. Demonstrated proof-of-concept restoration of BSEP protein expression. This is the only study in the dataset with a direct mechanistic link to the predicted indication cluster. Clinical translation not yet demonstrated. |

---

## Saudi Arabia Market Information

Ataluren is not approved or marketed in Saudi Arabia. No authorization records are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (BRIC) rests entirely on AI model inference with no supporting preclinical or clinical data (L5). While the mechanistic rationale — PTC readthrough in nonsense mutation cholestatic disease — is biologically sound, the absence of any direct evidence precludes a Go or Proceed with Guardrails decision at this stage.

**To proceed, the following is needed:**
- **Genotype stratification**: Confirm that the target patient subpopulation carries nonsense mutations in ATP8B1 (BRIC1) or ABCB11 (BRIC2); ataluren is ineffective against missense or frameshift mutations
- **Preclinical validation**: In vitro or animal model studies using BRIC-specific nonsense mutations; PMID 32702170 provides a usable protocol template for ABCB11 targets
- **Indication prioritization**: Consider re-ranking the lead candidate — PFIC2 (familial intrahepatic cholestasis, Rank 4) has direct in vitro evidence and may be a stronger starting point than BRIC (Rank 1) for hypothesis-driven development
- **Safety data resolution**: Retrieve and review the full package insert to complete the safety profile before any clinical planning (currently a blocking data gap)
- **MOA data**: Obtain full pharmacological characterization from DrugBank or primary sources to support the mechanism rationale in any regulatory or ethics submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

