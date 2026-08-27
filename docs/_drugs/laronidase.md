---
layout: default
title: Laronidase
parent: 僅模型預測 (L5)
nav_order: 361
evidence_level: L5
indication_count: 2
---

# Laronidase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Laronidase: From Mucopolysaccharidosis I (MPS I) to Lysosomal Storage Disease with Skeletal Involvement

## One-Sentence Summary

Laronidase (recombinant human α-L-iduronidase) is an established enzyme replacement therapy for Mucopolysaccharidosis I (MPS I). The TxGNN model's top prediction, **"lysosomal storage disease with skeletal involvement,"** is not an independent new indication — it is a clinical description of MPS I itself, the disease laronidase already treats. Supporting evidence is limited to **4 literature items and 0 clinical trials**, and a second candidate (Sanfilippo syndrome) appears to be a disease-ontology mapping artifact rather than a real signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Taiwan regulatory data (drug not marketed, no license records); internationally the drug's approved use is Mucopolysaccharidosis I (MPS I) |
| Predicted New Indication | Lysosomal storage disease with skeletal involvement |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L3 (observational cohort + review literature; no registered clinical trials) |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the source record (`original_moa` = Data Gap). Based on known pharmacology, laronidase is a recombinant form of α-L-iduronidase, the lysosomal enzyme deficient in MPS I. It is administered to break down accumulated glycosaminoglycans (dermatan sulfate, heparan sulfate), and its efficacy in MPS I — including the disease's skeletal manifestations — is well established in the literature (e.g., PMID 18758061 on uptake by cultured osteoblasts; PMID 23127271 on 6.5-year follow-up including skeletal radiographs and joint range-of-motion).

The critical caveat: "lysosomal storage disease with skeletal involvement" is not a distinct disease outside MPS I — it describes the skeletal phenotype of MPS I itself (the disease the drug already treats). The mechanistic link is therefore not a repurposing hypothesis but a restatement of the drug's known, approved use. This should be treated as **confirmation of existing activity**, not a new repurposing opportunity.

A second, lower-confidence prediction (Sanfilippo syndrome / MPS III, score 99.22%) was also generated but does not survive scrutiny: MPS III results from deficiency of different enzymes (SGSH, NAGLU, HGSNAT, or GNS) in the heparan sulfate degradation pathway, not α-L-iduronidase, and its pathology is primarily CNS-driven — a compartment a large IV-administered enzyme is unlikely to reach. All 8 literature items retrieved for this candidate, including the pivotal Phase 3 RCT (PMID 15126990), actually discuss laronidase in MPS I, not Sanfilippo syndrome. This strongly suggests a disease-ontology mislabeling issue in the evidence-retrieval pipeline (likely triggered by shared "mucopolysaccharidosis" keyword overlap) rather than a genuine biological signal, and should be flagged for pipeline QA rather than advanced as a candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23127271](https://pubmed.ncbi.nlm.nih.gov/23127271/) | 2012 | Cohort | Pediatric Neurology | 6.5-year ERT follow-up in attenuated MPS I (Scheie syndrome); tracked joint range of motion and skeletal radiographs, but noted disease progression despite treatment |
| [18758061](https://pubmed.ncbi.nlm.nih.gov/18758061/) | 2008 | In vitro mechanistic | Biological & Pharmaceutical Bulletin | Laronidase is taken up by MPS I fibroblasts and osteoblasts mainly via mannose-6-phosphate receptors, supporting a mechanistic basis for skeletal tissue delivery |
| [25345091](https://pubmed.ncbi.nlm.nih.gov/25345091/) | 2014 | Review | Pediatric Endocrinology Reviews | Overview of MPS I pathophysiology (IDUA deficiency, GAG accumulation) across the Hurler/Hurler-Scheie/Scheie spectrum |
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | Review | BioDrugs | Early development overview of laronidase as recombinant α-L-iduronidase ERT for MPS I, including orphan drug and fast-track status |

---

## Taiwan Market Information

Laronidase currently holds no marketing authorization in Taiwan (0 licenses on file; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. Note: the underlying data pack flags TFDA package insert / label data as a **Blocking** data gap (DG001), meaning safety pre-assessment (S1) cannot currently be completed for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked "new" indication is clinically synonymous with MPS I, the drug's known approved use — this is not a genuine repurposing signal, and the automated pipeline's "Proceed with Guardrails" recommendation should be discounted accordingly.
- The secondary candidate (Sanfilippo syndrome) shows a mechanistic mismatch and its supporting literature appears misattributed (all retrieved papers concern MPS I, not MPS III), indicating a likely disease-ontology error in the evidence pipeline.
- A Blocking-severity safety data gap (no TFDA label data) prevents a proper S1 safety assessment, and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- TFDA package insert / label data to resolve the Blocking safety gap (DG001)
- Confirmed original MOA and original indication text (DG002), currently marked Data Gap
- Pipeline QA on disease-ontology mapping for the Sanfilippo/MPS III candidate before it is reused
- If genuine repurposing candidates are sought, re-run prediction excluding disease terms that fall within the MPS I umbrella, since both current candidates collapse back to the drug's known target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

