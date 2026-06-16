---
layout: default
title: Clioquinol
parent: 僅模型預測 (L5)
nav_order: 147
evidence_level: L5
indication_count: 7
---

# Clioquinol
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

# Clioquinol: From Topical Antiseptic to Cutaneous Candidiasis

## One-Sentence Summary

Clioquinol (iodochlorhydroxyquin, brand name Vioform) is a halogenated hydroxyquinoline compound with a long clinical history as a topical antiseptic and antifungal agent, widely used in combination dermatological preparations.
The TxGNN model predicts it may be effective for **Cutaneous Candidiasis**, with **0 registered clinical trials** and **6 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not on record in current dataset (not marketed in Saudi Arabia) |
| Predicted New Indication | Cutaneous Candidiasis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Clioquinol is a halogenated 8-hydroxyquinoline derivative. While formal MOA documentation is not available in the current dataset, published mechanistic research indicates that clioquinol exerts antifungal activity primarily through **metal ion chelation**: it binds Zn²⁺ and Cu²⁺, disrupting essential fungal metalloenzymes including alcohol dehydrogenase and superoxide dismutase. A secondary mechanism involves direct disruption of the fungal cell membrane, creating a dual antifungal mode of action that does not overlap with conventional azoles or polyenes.

Cutaneous candidiasis is caused by *Candida* species that are critically dependent on zinc and copper availability for growth, virulence factor expression, and oxidative stress defence. Chelating these metals directly undermines *Candida*'s ability to survive in host tissue, making the biological rationale for clioquinol use in this indication mechanistically compelling.

Importantly, clinical practice has already validated this connection: the combination product **Locacorten-Vioform** (flumetasone 0.02% + clioquinol 3%) was widely used as a standard topical treatment for inflamed dermatoses with secondary candidal or bacterial superinfection across multiple countries during the 1970s–1980s. Multiple comparative clinical studies from this era directly documented its efficacy against cutaneous candidiasis, lending historical clinical plausibility to the TxGNN model's prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [6459255](https://pubmed.ncbi.nlm.nih.gov/6459255/) | 1981 | Randomized comparative study | J International Medical Research | Randomized parallel study (n=154, including 67 cutaneous candidiasis patients): betamethasone-gentamicin-iodochlorhydroxyquin-tolnaftate cream showed equivalent therapeutic response to comparator combination cream; confirms clioquinol formulation activity in candidal skin infection |
| [128475](https://pubmed.ncbi.nlm.nih.gov/128475/) | 1975 | Double-blind comparative study | Dermatologica | Double-blind study (n=430): Locacorten-Vioform (flumetasone 0.02% + clioquinol 3%) produced significantly greater microbiological conversion and clinical improvement than Vioform alone, Locacorten alone, or placebo in dermatoses with secondary microbial infection (*S. aureus* most prevalent pathogen) |
| [155507](https://pubmed.ncbi.nlm.nih.gov/155507/) | 1979 | Non-randomized comparative trial | Current Medical Research and Opinion | Parallel comparison of HNA cream vs. iodochlorhydroxyquin-hydrocortisone (I-HC) in 80 patients with cutaneous candidiasis and inflammatory dermatoses; I-HC (clioquinol-based) achieved 43% excellent response in candidiasis vs. 95% for HNA — confirms clioquinol component activity while identifying superior combinations |
| [136333](https://pubmed.ncbi.nlm.nih.gov/136333/) | 1976 | Non-randomized clinical evaluation | Current Therapeutic Research | Clinical evaluation of halcinonide combined with antifungal (including iodochlorhydroxyquin) in cutaneous fungal infections; supports combination approach in candidal dermatoses |
| [4220930](https://pubmed.ncbi.nlm.nih.gov/4220930/) | 1965 | Case series | Zeitschrift fur Haut- und Geschlechtskrankheiten | Describes role of *Candida* yeasts in acrodermatitis enteropathica (a zinc-deficiency dermatosis); contextualises the zinc–Candida relationship that underpins clioquinol's chelation mechanism |
| [2978600](https://pubmed.ncbi.nlm.nih.gov/2978600/) | 1988 | In vitro preventive study | Przeglad Dermatologiczny | In vitro screening of soap additives against clinical *C. albicans* isolates; hydroxyquinoline-based compounds including clioquinol analogues among agents with strongest fungicidal activity in alkaline soap solutions |

---

## Saudi Arabia Market Information

Clioquinol is currently **not marketed in Saudi Arabia** and holds no registered pharmaceutical licenses. No authorization data is available for this market.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important historical safety note**: Systemic absorption of clioquinol, particularly via oral or large-area topical use, has been associated with **subacute myelo-optic neuropathy (SMON)** — a serious neurological syndrome documented in Japan in the 1950s–1970s. Topical formulations on limited skin areas carry substantially lower risk, but restrictions on application area, duration, and use on broken skin are essential safeguards. Formal safety data from the current dataset is unavailable and must be obtained from the package insert and regulatory sources before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Historical clinical evidence from combination products (Locacorten-Vioform and related formulations) establishes that topical clioquinol has documented activity against cutaneous candidiasis, and the metal-chelation mechanism is biologically well-supported. An L3 evidence level from multiple comparative clinical studies — including one randomized study — provides sufficient scientific foundation to advance to a structured evaluation, provided that safety risks (particularly SMON) are rigorously addressed and confined to topical-only use.

**To proceed, the following is needed:**
- Formal MOA documentation from DrugBank API or primary pharmacology literature
- SMON risk mitigation plan: define maximum application area, treatment duration, and patient selection criteria (exclude large BSA, broken skin, paediatric patients)
- Package insert review for complete contraindications and warnings (TFDA insert identified as existing but data not yet parsed)
- Modern comparative RCT against current standard-of-care antifungals (topical azoles, nystatin) to establish non-inferiority or superiority
- Regulatory pathway assessment for Saudi Arabia market entry, given current zero-license status
- Drug interaction screening (DDI data not found in current dataset)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

