---
layout: default
title: Colchicine
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 3
---

# Colchicine
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

# Colchicine: From Gout and Inflammatory Conditions to Plasmodium falciparum Malaria

## One-Sentence Summary

Colchicine is an ancient plant alkaloid derived from *Colchicum autumnale*, historically used for gout and autoinflammatory conditions. The TxGNN model predicts it may be effective for **Plasmodium falciparum malaria**, with **0 registered clinical trials** and **6 publications** currently available — all of which are indirect preclinical or in vitro mechanistic studies that do not directly test colchicine as an antimalarial. Evidence at this stage is insufficient to support clinical development without further foundational research.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Saudi Arabia; historically indicated for gout and inflammatory conditions |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 — preclinical/mechanistic studies only, no clinical trials |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Colchicine's primary mechanism of action is the inhibition of tubulin polymerization, thereby disrupting microtubule assembly. This arrests cell division at the mitotic spindle stage and suppresses neutrophil migration. Because *Plasmodium falciparum* relies on microtubule-dependent processes — including spindle formation during gametocyte development and intraerythrocytic schizogony — tubulin-binding agents represent a theoretically valid target class for antimalarial activity.

The body of indirect evidence comes from a class-effect perspective: structurally distinct tubulin-binding compounds (tubulozoles, cytochalasin B, curcumin) have shown in vitro activity against *P. falciparum*, and one study noted that Colcemid (a colchicine analogue) produced similar effects on protein synthesis as tubulozoles in the parasite model. These findings suggest that plasmodial tubulin is a pharmacologically exploitable target, lending biological plausibility to the TxGNN prediction.

However, critical gaps remain. No study has directly tested colchicine as an antimalarial agent. The therapeutic concentration window of colchicine (narrow index, ~0.5–3 ng/mL plasma) versus the parasite inhibitory concentration required has not been assessed. Furthermore, plasmodial tubulin differs structurally from mammalian tubulin, raising both the possibility of selectivity and the risk of inadequate potency at non-toxic doses. The TxGNN high score most likely reflects a network-level protein-pathway association rather than direct translational evidence.

Currently, detailed mechanism of action data specific to colchicine is not available in this evidence pack. Based on established pharmacology, colchicine inhibits microtubule polymerization and neutrophil chemotaxis, and this class-level activity mechanistically intersects with *P. falciparum* biology — but direct antimalarial evidence in any model system is absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for colchicine in Plasmodium falciparum malaria.

---

## Literature Evidence

All 6 retrieved publications are indirect — none directly studies colchicine against *P. falciparum*. They examine related compounds (tubulozoles, curcumin, cytoskeletal binders) or parasite biology (pfmdr1, intermediate filaments). Listed here for completeness:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2655935](https://pubmed.ncbi.nlm.nih.gov/2655935/) | 1989 | In vitro screening | Cell Biology International Reports | Nine tubulin-binding compounds tested against *P. falciparum* in vitro; tubulozole-T showed selective antimalarial activity; plasmodial tubulin differs from mammalian protein at molecular level |
| [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) | 1989 | In vitro screening | Cell Biology International Reports | Parallel report confirming cytoskeletal-binding compounds are active against *P. falciparum*; actin-binding cytochalasin B also tested |
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | In vitro mechanistic | Antimicrobial Agents and Chemotherapy | Tubulozole isomers investigated as antimalarial agents; Colcemid noted to produce similar protein synthesis inhibition as tubulozoles in parasite models |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | Observational/Serological | Clinical and Experimental Immunology | 82% of acute malaria sera contained antibodies to intermediate filaments; suggests cytoskeletal involvement in host immune response during malaria infection |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | Molecular biology | Molecular and Cellular Biology | pfmdr1 (ABC transporter) expression in mammalian cells linked to increased chloroquine susceptibility; relevant to drug resistance mechanism context |
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro mechanistic | PLoS ONE | Curcumin disrupts *P. falciparum* microtubules at clinically achievable concentrations; parallels drawn with cancer cell tubulin-binding mechanism |

> **Note:** None of these publications directly test colchicine. Evidence is class-level and indirect. Tier 3 (preclinical/mechanistic) for all entries.

---

## Saudi Arabia Market Information

Colchicine is not currently registered or marketed in Saudi Arabia. No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important context:** Colchicine has a **narrow therapeutic index** with no well-defined threshold between therapeutic, toxic, and lethal doses (PMID [20586571](https://pubmed.ncbi.nlm.nih.gov/20586571/)). This is especially relevant for any new indication development — dose selection and toxicity monitoring would be a critical development requirement. Safety database for this evidence pack is pending TFDA/SFDA package insert extraction.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no direct clinical or preclinical evidence that colchicine is effective against *Plasmodium falciparum*. All available literature examines structurally related but distinct compounds, providing class-level biological plausibility only. The prediction score reflects a protein-network association in TxGNN rather than translatable clinical evidence.

**To proceed, the following is needed:**

- **In vitro antimalarial assay**: Direct testing of colchicine against *P. falciparum* strains (3D7, Dd2) to establish IC₅₀ and determine if effective concentrations fall within the drug's therapeutic plasma range
- **Selectivity index**: Compare parasite IC₅₀ versus human cell CC₅₀ to assess whether a therapeutic window exists
- **MOA confirmation**: Confirm whether colchicine disrupts *P. falciparum* tubulin specifically, given known structural differences from mammalian tubulin
- **Safety data extraction**: Retrieve TFDA/SFDA package insert warnings and contraindications (Data Gap DG001) before any clinical planning
- **Comparator benchmark**: Benchmark colchicine's potential antimalarial potency against existing artemisinin-based regimens to assess clinical relevance

---

> **Additional Finding — High Priority:**
> The second-ranked TxGNN prediction — **Familial Mediterranean Fever (FMF)** — carries **L1 evidence** (multiple review-grade publications, 1 registered trial on second-line therapy implying colchicine as established first-line, PMID [68234](https://pubmed.ncbi.nlm.nih.gov/68234/) dating to 1977) with a recommendation of **Proceed with Guardrails**. Multiple FMF reviews explicitly state that colchicine is the only agent proven to prevent attacks and amyloidosis (e.g., PMID [25649364](https://pubmed.ncbi.nlm.nih.gov/25649364/), [38354004](https://pubmed.ncbi.nlm.nih.gov/38354004/)). The mechanistic link is strong and well-characterised: colchicine suppresses neutrophil chemotaxis and pyrin–microtubule interactions, directly counteracting FMF's inflammasome-driven pathology. **A separate FMF-focused report is recommended as the higher-priority repurposing candidate.**
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

