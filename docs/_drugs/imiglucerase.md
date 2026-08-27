---
layout: default
title: Imiglucerase
parent: 僅模型預測 (L5)
nav_order: 322
evidence_level: L5
indication_count: 5
---

# Imiglucerase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Imiglucerase: From Gaucher Disease to Hurler Syndrome

## One-Sentence Summary

Imiglucerase is a recombinant enzyme replacement therapy (ERT) originally developed to supply glucocerebrosidase for the treatment of **Gaucher disease**. The TxGNN model predicts it may also be effective for **Hurler syndrome (MPS I)**, but this direction is currently supported by **0 clinical trials** and only **2 general review articles**, neither of which specifically studies imiglucerase in Hurler syndrome.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease (established per cited literature; no Saudi Arabia license record on file — product not marketed) |
| Predicted New Indication | Hurler syndrome |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a High-severity data gap). Based on the information available in this evidence pack, imiglucerase is a recombinant form of human **glucocerebrosidase (GBA)**, the enzyme deficient in Gaucher disease. Its established efficacy comes from directly replacing this missing enzyme, allowing lysosomal breakdown of glucocerebroside to resume.

Hurler syndrome (Mucopolysaccharidosis type I, MPS I), however, is caused by deficiency of a **different enzyme — alpha-L-iduronidase (IDUA)** — which breaks down glycosaminoglycans, not glucocerebroside. There is no molecular-level overlap between the substrate imiglucerase acts on and the substrate accumulating in Hurler syndrome. Hurler syndrome already has its own dedicated ERT, laronidase (recombinant IDUA), which imiglucerase cannot substitute for.

The mechanistic rationale in this evidence pack explicitly flags this as a likely **category-level artifact**: both drug and disease belong to the broader "lysosomal storage disease + enzyme replacement therapy" cluster in the knowledge graph, which may be driving the high TxGNN score rather than a true enzyme-substrate relationship. This distinction is important — the prediction should be interpreted as a hypothesis worth noting, not as evidence of a genuine pharmacological link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Review | Proceedings of the National Academy of Sciences of the United States of America | Describes PET-based imaging of enzyme replacement therapy across multiple lysosomal storage diseases (Gaucher, Fabry, Hurler, Hunter, Maroteaux-Lamy, Pompe); does not evaluate imiglucerase specifically for Hurler syndrome. |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de médecine interne | General review of ERT development for lysosomal storage diseases, tracing the history from alglucerase to imiglucerase (Cerezyme) for Gaucher disease; mentions the broader ERT/LSD treatment class without addressing MPS I. |

---

## Saudi Arabia Market Information

Imiglucerase is currently **not marketed** in Saudi Arabia — there are no license or product authorization records on file (0 authorizations).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted association between imiglucerase and Hurler syndrome lacks both clinical evidence (no trials) and disease-specific literature support (only 2 general reviews that do not evaluate this drug-disease pair directly). More importantly, the underlying mechanism is biologically discordant — imiglucerase replaces glucocerebrosidase, while Hurler syndrome results from alpha-L-iduronidase deficiency — suggesting the high TxGNN score may reflect broad "ERT/LSD" category similarity rather than a genuine molecular mechanism.

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings, contraindications) — currently a **Blocking** data gap preventing safety pre-screening
- Confirmed mechanism of action (MOA) documentation from DrugBank or equivalent source
- Any preclinical or in vitro data specifically testing glucocerebrosidase activity or off-target effects relevant to IDUA-substrate accumulation in MPS I
- Clarification on whether category-level (ERT/LSD) knowledge graph clustering should be down-weighted in future TxGNN scoring, given the same pattern also appears in this drug's other top-ranked predictions (Scheie syndrome, cholesteryl ester storage disease)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

