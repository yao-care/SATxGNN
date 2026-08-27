---
layout: default
title: Iodixanol
parent: 僅模型預測 (L5)
nav_order: 335
evidence_level: L5
indication_count: 3
---

# Iodixanol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Iodixanol: From Diagnostic Contrast Agent to Osteoarthritis (Weak Signal)

## One-Sentence Summary

Iodixanol (DB01249) is a non-ionic iodinated contrast medium (Visipaque) used for diagnostic imaging (CT/angiography), with no established therapeutic indication. TxGNN's top-ranked prediction ("osteoarthritis susceptibility") is flagged in the evidence pack itself as a duplicate label of osteoarthritis with no independent evidence, so this report centers on **Osteoarthritis**, the only candidate with actual literature (**7 publications**, **0 clinical trials**) — though that literature describes iodixanol as an imaging/research tool, not a treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diagnostic contrast agent for radiographic/CT imaging (non-ionic iodinated contrast medium, Visipaque) — not a therapeutic agent |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.07% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for iodixanol beyond its role as a contrast medium. As a non-ionic iodinated agent, it has no known pharmacological effect on cartilage metabolism, synovial inflammation, or joint disease progression — its function is purely radiographic (X-ray attenuation for imaging).

The literature linking iodixanol to osteoarthritis does not describe any therapeutic effect. Every publication uses iodixanol as a diffusible contrast/tracer molecule to study cartilage and osteochondral-interface properties (solute transport, finite-element modeling, photon-counting CT imaging) — i.e., iodixanol as a **research/imaging tool for studying OA**, not as an OA treatment.

The TxGNN score most likely reflects a spurious statistical association: the model has learned that "iodixanol" and "osteoarthritis" co-occur frequently in the literature (because it's a standard imaging tracer in OA cartilage research), and has mistaken this co-occurrence for a treatment relationship. The evidence pack's own rationale for the top-ranked candidate ("osteoarthritis susceptibility") independently confirms this — it notes that entry is a variant label of osteoarthritis with no independent evidence and no establishable mechanistic link. The third candidate, rheumatoid arthritis, is supported only by a case report on managing contrast-media hypersensitivity in an RA patient — again describing safe *use of* a contrast agent in RA patients, not a treatment effect *on* RA.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Solute transport study | Journal of Biomechanics | First use of iodixanol (~1550 Da) as a neutral diffusing CT contrast agent to study osteochondral-interface permeability in equine/human OA models |
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Imaging technique | Annals of Biomedical Engineering | Dual-contrast (nanoparticle + molecular) photon-counting CT to assess articular cartilage health |
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Imaging technique | Annals of Biomedical Engineering | Nanoparticle diffusion CT imaging to reveal detailed cartilage function |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | In vitro | Journal of Experimental Orthopaedics | Iodine contrast agents do not affect Platelet-Rich Plasma function in vitro (relevant to intra-articular injection use) |
| [30145230](https://pubmed.ncbi.nlm.nih.gov/30145230/) | 2018 | Animal cartilage biomechanics | Osteoarthritis and Cartilage | Aging effects on mandibular condylar cartilage stiffness in horses, assessed via diffusion imaging |
| [28518064](https://pubmed.ncbi.nlm.nih.gov/28518064/) | 2017 | Finite element / experimental protocol | Journal of Visualized Experiments | Protocol for studying neutral/charged solute transport across articular cartilage in OA context |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Finite element modeling | Journal of Biomechanics | FEM of neutral solute transport across the osteochondral interface to understand OA progression |

*Note: rheumatoid arthritis is supported only by one case report ([36628042](https://pubmed.ncbi.nlm.nih.gov/36628042/), 2022, Cureus) on desensitization to a related iodinated contrast agent (iohexol) in an RA patient — describing safe administration, not a treatment effect.*

## Saudi Arabia Market Information

Iodixanol currently has no marketing authorization in Saudi Arabia (0 licenses on file; market status: not marketed).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials for any of the three predicted indications, and all available literature describes iodixanol as an imaging/research tracer rather than a therapeutic agent — there is no mechanistic basis for a treatment effect in osteoarthritis or rheumatoid arthritis. The top TxGNN-ranked candidate is itself flagged as a non-independent duplicate signal.

**To proceed, the following is needed:**
- Confirmed mechanism of action data from DrugBank/primary literature
- TFDA/SFDA-equivalent package insert (warnings, contraindications) — currently a blocking data gap
- Any preclinical or mechanistic study directly testing iodixanol (not merely using it as a contrast tracer) against joint/autoimmune disease pathology
- Saudi Arabia regulatory pathway assessment, given the drug is not currently marketed there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

