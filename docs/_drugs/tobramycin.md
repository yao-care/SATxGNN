---
layout: default
title: Tobramycin
parent: 僅模型預測 (L5)
nav_order: 624
evidence_level: L5
indication_count: 10
---

# Tobramycin
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

# Tobramycin: From Bacterial Infections to Exposure Keratitis

## One-Sentence Summary

> Tobramycin is an aminoglycoside antibiotic originally used to treat serious Gram-negative bacterial infections (e.g., *Pseudomonas aeruginosa*).
> The TxGNN model predicts it may be effective for **Exposure Keratitis**,
> with **2 clinical trials** and **7 publications** currently identified, though most evidence is only indirectly related.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (aminoglycoside antibiotic) — no country-specific approved indication text on file |
| Predicted New Indication | Exposure Keratitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information, tobramycin is an aminoglycoside antibiotic that binds the bacterial 30S ribosomal subunit, effective mainly against Gram-negative organisms such as *Pseudomonas aeruginosa*; its efficacy in serious bacterial infections is well established.

Exposure keratitis, however, is fundamentally a mechanical/structural condition — corneal exposure caused by inadequate eyelid closure — rather than a primary infectious disease. Tobramycin's plausible role here is indirect: as prophylaxis or adjunctive treatment against secondary bacterial infection of the exposed cornea, not as a direct treatment for the underlying condition.

This mechanistic link is therefore weak/indirect. Supporting literature also includes in vitro data showing aminoglycoside (including tobramycin) corneal epithelial toxicity, meaning any use in an already-compromised cornea would require careful risk-benefit weighing rather than being a straightforward repurposing opportunity.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05313828](https://clinicaltrials.gov/study/NCT05313828) | N/A | Unknown | 40 | Study of treatment modalities for dendritic (herpetic) corneal ulcer; tobramycin not specifically used — graded low relevance (C) |
| [NCT06200727](https://clinicaltrials.gov/study/NCT06200727) | N/A | Unknown | 170 | Platelet-rich fibrin (PRF) membrane for ophthalmic diseases including corneal ulcer; no direct antibiotic mechanism link — graded low relevance (C) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | In vitro toxicity | Current Eye Research | Demonstrates corneal epithelial cytotoxicity of tobramycin (and other aminoglycosides) in rabbit model — relevant safety signal for ocular use |
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | In vitro/lab (MIC/PAE) | Nippon Ganka Gakkai Zasshi | MIC and post-antibiotic effect of antibiotic eyedrops (incl. tobramycin) against keratitis isolates in Japan |
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | Case report | Oxford Medical Case Reports | Bacterial keratitis from multi-drug-resistant *Shewanella algae* in a bedridden patient unable to close eyes voluntarily (exposure-related risk factor) |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | *Bacillus cereus* keratitis associated with contact lens wear |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | Case report | Eye & Contact Lens | Bilateral MRSA keratitis following photorefractive keratectomy |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | Case report (non-infectious) | Yan Ke Xue Bao | Corneal dellen in Graves ophthalmopathy — not an infectious etiology |
| [33847093](https://pubmed.ncbi.nlm.nih.gov/33847093/) | 2021 | Case series (veterinary, feline) | Polish Journal of Veterinary Sciences | Feline ocular toxoplasmosis outcomes — low translational relevance |

## Taiwan Market Information

Tobramycin currently has no marketing authorization on file (market status: Not Marketed, 0 licenses).

## Safety Considerations

Please refer to the package insert for safety information. (TFDA warning/contraindication data retrieval is currently a **Blocking** data gap — safety pre-assessment (S1) cannot be completed until this is resolved.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (exposure keratitis) rests on an indirect mechanistic link, low-relevance clinical trials, and literature that includes a corneal toxicity signal for tobramycin itself. Combined with the unresolved blocking gap in TFDA warning/contraindication data, there is insufficient basis to proceed at this time.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently blocking S1 safety evaluation
- Detailed mechanism of action (MOA) data from DrugBank
- Formal risk-benefit assessment of ocular epithelial toxicity if any ophthalmic use is considered
- Consider prioritizing other candidates in this evidence pack with stronger support (e.g., **otitis externa**, L3/S2, "Proceed with Guardrails") ahead of exposure keratitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

