---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 5
---

# Carfilzomib
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

# Carfilzomib: From Multiple Myeloma to CMM7

## One-Sentence Summary

Carfilzomib is a second-generation, irreversible proteasome inhibitor established for the treatment of relapsed and refractory multiple myeloma. The TxGNN model predicts it may be effective against **CMM7 (Cutaneous Malignant Melanoma type 7)** — the highest-ranked of five distinct melanoma subtypes flagged by the model. No direct clinical trials or literature specific to CMM7 have been identified; however, **5 preclinical publications** support a biologically plausible mechanism for carfilzomib in the broader melanoma indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple myeloma (relapsed/refractory) |
| Predicted New Indication | CMM7 (Cutaneous Malignant Melanoma type 7) |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 (CMM7-specific) / L4 (broader melanoma with preclinical data) |
| Saudi Arabia Market Status | ✗ Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not captured in this dataset's formal fields. However, the mechanistic rationale embedded in the evidence pack (from the rank-5 melanoma entry) reveals that carfilzomib acts as an **irreversible inhibitor of the 20S proteasome β5 subunit** (chymotrypsin-like activity). By blocking proteasome-mediated protein degradation, it causes proteotoxic stress accumulation, activates the unfolded protein response (UPR) through the PERK/eIF2α/ATF4/CHOP axis, and ultimately drives tumor cell apoptosis. Unlike the first-generation agent bortezomib, carfilzomib binds covalently and irreversibly, providing more sustained proteasome suppression.

CMM7 (Cutaneous Malignant Melanoma type 7) is a rare subtype linked to specific germline susceptibility loci. While no CMM7-specific carfilzomib studies exist, the TxGNN model ranked five melanoma subtypes consecutively in the top 13,229 predictions, suggesting a consistent signal across the melanoma disease family. The biological logic is compelling: melanoma cells exhibit high protein synthesis rates driven by MITF-regulated differentiation factors and elevated antigen-presentation demands, creating a heavy proteasome load that theoretically makes them more sensitive to proteasome inhibition than many other solid tumors.

The most direct experimental evidence comes from PMID 33671902, in which carfilzomib — alone and in combination with bortezomib — induced synergistic apoptosis in B16-F1 murine melanoma cells, with activation of caspases 3, 8, 9, and 12 confirmed by flow cytometry. This confirms that the mechanistic link between proteasome inhibition and melanoma cell death is biologically real, though clinical validation in human patients is entirely absent.

---

## Clinical Trial Evidence

No clinical trials investigating carfilzomib in CMM7 or any melanoma subtype have been identified as of the data cutoff (2026-06-15).

---

## Literature Evidence

No literature directly linking carfilzomib to CMM7 is available. The following publications address carfilzomib in the broader melanoma context and serve as indirect supporting evidence:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In vitro preclinical | Biology | Carfilzomib + bortezomib synergistically induces apoptosis in B16-F1 murine melanoma cells via caspase 3, 8, 9, and 12 activation — most directly relevant study |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | Computational | J Biomol Struct Dyn | Molecular docking and MD simulation across 10 cancer types including melanoma; carfilzomib included as a repurposing candidate against multiple kinase targets |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Basic science | Mol Cancer Res | AIRAP/AIRAPL zinc-finger gene regulates melanoma cell survival via E3-ligase cIAP2 and ubiquitin-proteasome pathway — implicates proteasome dependency in melanoma |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Basic science | Matrix Biology | Carfilzomib activates NF-κB, upregulating heparanase in myeloma tumor cells — identifies a potential resistance mechanism relevant to any solid tumor application |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | Preclinical | Leukemia | BET-targeting PROTACs combined with carfilzomib show synergistic activity via proteasomal degradation — supports proteasome pathway as a combinable oncology target |

---

## Saudi Arabia Market Information

Carfilzomib is **not registered with the Saudi Food and Drug Authority (SFDA)**. No licenses, approved dosage forms, or approved indications are on record in Saudi Arabia.

---

## Cytotoxicity

Carfilzomib is an antineoplastic agent (proteasome inhibitor used in oncology for multiple myeloma).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — irreversible proteasome inhibitor (β5 subunit, chymotrypsin-like activity) |
| Myelosuppression Risk | High — thrombocytopenia and anemia are common class effects; requires regular hematological monitoring |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential and platelets; cardiac function (LVEF — carfilzomib carries known cardiotoxicity risk including heart failure and hypertension); renal function; serum electrolytes |
| Handling Protection | Must follow cytotoxic drug handling regulations — closed-system transfer devices and appropriate PPE required |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Clinical note:** Local SFDA/TFDA package insert data was not retrieved for this report. Based on the established pharmacological class, carfilzomib (Kyprolis®) carries well-documented risks including **cardiac toxicity** (heart failure, hypertension, cardiomyopathy), **pulmonary complications** (dyspnea, pneumonia), **infusion reactions**, and **thromboembolic events**. Clinicians should consult the full prescribing information before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
CMM7 is a rare cutaneous melanoma subtype with zero direct clinical trial or published literature evidence for carfilzomib. While the broader melanoma mechanistic rationale is biologically plausible and supported by in vitro preclinical data, the current evidence base is insufficient (L5 for CMM7 specifically) to justify clinical investment without first establishing preclinical proof-of-concept in human CMM7-representative models.

**To proceed, the following is needed:**
- CMM7-specific in vitro studies (human melanoma cell lines with relevant genetic background) and in vivo xenograft models to confirm proteasome sensitivity in this subtype
- Formal MOA documentation from DrugBank API query (flagged as DG002 in this pack)
- SFDA/TFDA package insert review to resolve safety data gaps (flagged as DG001 — currently Blocking for safety screening)
- Biomarker strategy to identify patient subpopulations most likely to respond (e.g., baseline proteasome activity, UPR activation markers, MITF expression levels)
- Cardiotoxicity risk assessment framework given carfilzomib's known cardiac safety signal in myeloma patients, which would require careful monitoring protocol design for any solid tumor trial
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

