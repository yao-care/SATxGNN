---
layout: default
title: Niclosamide
parent: 僅模型預測 (L5)
nav_order: 439
evidence_level: L5
indication_count: 10
---

# Niclosamide
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

# Niclosamide: From Tapeworm Infection to Heart Disease

## One-Sentence Summary

Niclosamide is a classic anthelmintic historically used to treat tapeworm (cestode) infections. The TxGNN model predicts a possible link to **Heart Disease**, but the only three supporting clinical trials are graded low-relevance (two withdrawn with zero enrollment, one terminated), and the evidence review itself concludes this signal is most likely a knowledge-graph mapping artifact rather than a genuine mechanistic finding.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tapeworm infection (Taeniasis) — traditional anthelmintic use; no locally approved indication text is available (drug is not marketed in this jurisdiction) |
| Predicted New Indication | Heart disease |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed, source-verified mechanism-of-action data is not available (DrugBank MOA field: Data Gap). Based on the information collected during evidence review, niclosamide is known to uncouple mitochondrial oxidative phosphorylation and to inhibit the STAT3, Wnt/β-catenin, and mTORC1 signaling pathways — mechanisms studied mainly in antiparasitic, antiviral, and antifibrotic contexts, not in cardiovascular disease.

Niclosamide has no established cardiac indication and no direct cardiovascular mechanism of action reported in the literature reviewed. The three clinical trials linked to "heart disease" in this evidence pack are, on closer inspection, COVID-19 (non-severe) treatment studies — one of which combined niclosamide with **diltiazem**, a calcium-channel blocker used in cardiac indications. The evidence review's own assessment is that this combination-drug artifact most likely caused the TxGNN knowledge graph to erroneously associate niclosamide with the "heart disease" node, rather than reflecting a genuine pharmacological relationship.

Given this, the mechanistic plausibility of niclosamide for heart disease is currently weak, and the prediction should be treated as a hypothesis-generating signal requiring independent mechanistic confirmation, not as an evidence-backed repurposing candidate.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04372082](https://clinicaltrials.gov/study/NCT04372082) | Phase 3 | Withdrawn | 0 | Planned trial of hydroxychloroquine + diltiazem-niclosamide combination vs. standard of care for non-severe COVID-19 in patients with comorbidities (incl. cardiovascular disease); withdrawn before enrollment, no data generated. Graded C — not a cardiac-disease trial per se. |
| [NCT04542434](https://clinicaltrials.gov/study/NCT04542434) | Phase 2 | Withdrawn | 0 | Planned placebo-controlled safety/efficacy study of niclosamide in moderate COVID-19 with GI symptoms; withdrawn before enrollment, no data generated. Graded C — target population not cardiac. |
| [NCT03521232](https://clinicaltrials.gov/study/NCT03521232) | Phase 1/2a | Terminated | 27 | Safety, efficacy, and pharmacokinetics of niclosamide enema in ulcerative proctitis/procto-sigmoiditis; terminated early. Exploratory GI safety trial, not cardiac-disease-directed. Graded C. |

## Literature Evidence

Currently no related literature available for the "heart disease" prediction.

## Saudi Arabia Market Information

Niclosamide is not currently marketed in this jurisdiction (market status: 未上市, 0 authorizations on record), so no product licenses are available to list.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (heart disease) is supported only by Grade-C trials — two withdrawn with zero enrollment and one terminated — and the evidence review assesses the underlying signal as a likely TxGNN knowledge-graph mapping artifact (traced to a COVID-19 combination trial that paired niclosamide with the cardiac drug diltiazem) rather than a genuine drug–disease mechanistic link. All lower-ranked predictions (ranks 2–9) have zero supporting trials or literature and largely correspond to rare congenital/chromosomal syndromes with no plausible biological connection to niclosamide's known pharmacology; rank 10's literature set discusses niclosamide's general pharmacology (antifungal, antiviral, antifibrotic, oncology) but none of it addresses the named "disorder of fucoglycosan synthesis." Additionally, TFDA label data (warnings/contraindications) is a Blocking data gap that prevents any S1 safety evaluation from starting.

**To proceed, the following is needed:**
- TFDA (or equivalent) package insert to unblock the S1 safety initial assessment (DG001, Blocking)
- Verified mechanism-of-action data from DrugBank (DG002, High)
- Independent confirmation of whether the "heart disease" TxGNN signal reflects real biology or is an artifact of the diltiazem-combination trial, before allocating further evaluation resources
- If pursuing further, a re-run of the TxGNN mapping/evidence pipeline against a cleaner disease ontology, since several rank 2–10 disease labels appear mismatched or non-standard
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

