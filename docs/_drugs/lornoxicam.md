---
layout: default
title: Lornoxicam
parent: 僅模型預測 (L5)
nav_order: 388
evidence_level: L5
indication_count: 10
---

# Lornoxicam
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

# Lornoxicam: From Musculoskeletal and Postoperative Pain to Rheumatoid Arthritis

## One-Sentence Summary

Lornoxicam is an oxicam-class NSAID with established international use for musculoskeletal pain, postoperative pain, and osteoarthritis, but it currently holds no marketing authorization in Saudi Arabia. The TxGNN model's top-ranked prediction is efficacy in **Rheumatoid Arthritis**, a mechanistically plausible extension of its existing anti-inflammatory use, supported by **0 registry-listed clinical trials** but **20 literature references**, including several controlled clinical studies from the early 2000s.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in Saudi regulatory data (drug unlicensed); literature documents established use in musculoskeletal/joint pain, postoperative pain, and lumbar-sciatica conditions (PMID 8706598) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, lornoxicam belongs to the oxicam class of non-steroidal anti-inflammatory drugs (NSAIDs) and is a potent, non-selective inhibitor of COX-1 and COX-2, distinguished from other oxicams by a comparatively short elimination half-life (3–5 hours).

The relationship between lornoxicam's established uses and rheumatoid arthritis is close rather than novel: published literature already describes lornoxicam as used "in the muscular skeletal and joint disorders such as osteoarthritis and rheumatoid arthritis" (PMID 22469263), and notes the drug is marketed in 31 countries across Europe, the Middle East, the Far East and South America for osteoarthritis, rheumatoid arthritis, acute lumbar-sciatica and postoperative pain (PMID 19821419). This suggests the TxGNN prediction largely reflects an already-validated pharmacological use rather than a mechanistically speculative repurposing — the opportunity here is market entry into Saudi Arabia, where the product is currently unlicensed, rather than discovery of a new biological mechanism.

Mechanistically, RA is an autoimmune inflammatory joint disease driven substantially by prostaglandin-mediated inflammation, which is directly addressed by COX inhibition. This explains why several controlled clinical studies of lornoxicam in RA patients exist from the early 2000s (predating mandatory clinical trial registry requirements introduced around 2007), which is consistent with the absence of entries in ClinicalTrials.gov/ICTRP despite substantial literature support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12404032](https://pubmed.ncbi.nlm.nih.gov/12404032/) | 2002 | RCT (crossover, double-blind) | Reumatismo | Lornoxicam 8mg/16mg vs diclofenac 150mg/day in RA patients; dose-finding for analgesic efficacy and safety |
| [12207202](https://pubmed.ncbi.nlm.nih.gov/12207202/) | 2002 | Clinical study (long-term) | Minerva Medica | Long-term efficacy and safety assessment of lornoxicam in RA |
| [12087911](https://pubmed.ncbi.nlm.nih.gov/12087911/) | 2002 | Clinical study | Terapevticheskii Arkhiv | Clinical response, safety, and effects on blood pressure/heart rhythm variability in RA patients with hypertension |
| [19821419](https://pubmed.ncbi.nlm.nih.gov/19821419/) | 2009 | Systematic Review | Cochrane Database of Systematic Reviews | Confirms lornoxicam is prescribed for osteoarthritis, RA, lumbar-sciatica and postoperative pain across 31 countries |
| [8706598](https://pubmed.ncbi.nlm.nih.gov/8706598/) | 1996 | Review | Drugs | Comprehensive pharmacology review; efficacy comparable to opioid analgesics; short elimination half-life |
| [22469263](https://pubmed.ncbi.nlm.nih.gov/22469263/) | 2011 | Review | Profiles of Drug Substances, Excipients, and Related Methodology | Comprehensive drug substance profile including mechanism of action and established RA/OA use |
| [29026298](https://pubmed.ncbi.nlm.nih.gov/29026298/) | 2017 | Preclinical (animal RA model) | International Journal of Nanomedicine | Nanomicellar lornoxicam formulation improves therapeutic efficacy vs free drug in experimental RA models |
| [12240779](https://pubmed.ncbi.nlm.nih.gov/12240779/) | 2002 | Review | Clinical Therapeutics | Literature review of NSAID dose-effect relationships in RA and osteoarthritis, including lornoxicam |
| [23567043](https://pubmed.ncbi.nlm.nih.gov/23567043/) | 2013 | Formulation study | Journal of Controlled Release | Transdermal patch delivering lornoxicam + teriflunomide for intra-articular RA treatment |
| [25553695](https://pubmed.ncbi.nlm.nih.gov/25553695/) | 2015 | Formulation study | Pakistan Journal of Pharmaceutical Sciences | Chronotherapeutic pulsincap delivery of lornoxicam targeting early-morning RA symptom peaks |

---

## Saudi Arabia Market Information

Lornoxicam currently has no approved marketing authorization in Saudi Arabia (0 licenses on record); no product/authorization data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Lornoxicam's efficacy in rheumatoid arthritis is already well-established internationally through COX-inhibiting NSAID pharmacology and multiple early-2000s controlled clinical studies, but Saudi-specific safety labeling, drug interaction data, and local trial evidence are absent, so market entry should proceed only with additional safeguards.

**To proceed, the following is needed:**
- SFDA-approved package insert with warnings/contraindications (currently a blocking data gap — DG001)
- Detailed mechanism-of-action data from DrugBank to support the S1 safety review (DG002)
- Drug-drug interaction data (current DDI query returned no results)
- A decision on whether existing international RA trial evidence is sufficient for SFDA submission, or whether a local bridging study is required

*Note: this pack also lists "migraine disorder" (rank 3) as a candidate with a completed Phase 2 RCT specifically testing lornoxicam (NCT00293657) — a separate evaluation may be warranted if that indication is of interest.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

