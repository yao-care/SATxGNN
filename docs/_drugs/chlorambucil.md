---
layout: default
title: Chlorambucil
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 8
---

# Chlorambucil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Chlorambucil: From Chronic Lymphocytic Leukemia to Pregerminal Center CLL/SLL

## One-Sentence Summary

Chlorambucil is a nitrogen mustard alkylating agent with a long-established role in chronic lymphocytic leukemia (CLL) treatment, historically serving as the standard-of-care comparator in multiple landmark Phase 3 trials.
The TxGNN model predicts it may be effective for **Pregerminal Center Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma (unmutated IGHV subtype)**,
with **1 publication** identified for this specific molecular subtype; however, broader Phase 3 CLL trial evidence — including CAM307 and RESONATE-2 — provides meaningful indirect support through extrapolation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Lymphocytic Leukemia (CLL) |
| Predicted New Indication | Pregerminal Center Chronic Lymphocytic Leukemia / Small Lymphocytic Lymphoma |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the DrugBank record in this Evidence Pack. Based on established pharmacological classification, chlorambucil is a bifunctional nitrogen mustard alkylating agent that forms covalent cross-links with DNA strands, impairing replication and triggering programmed cell death. It has historically demonstrated selective activity against B-cell lineage malignancies, particularly indolent lymphoproliferative disorders such as CLL, where slowly cycling B cells accumulate rather than proliferate rapidly.

Pregerminal center CLL (unmutated IGHV subtype) is a molecularly distinct form of CLL in which the malignant B-cell clone has not undergone somatic hypermutation in the immunoglobulin heavy chain variable-region gene — a marker of pre-germinal center origin. This subtype carries an inferior prognosis compared to the mutated IGHV form and shows comparatively less dependence on BCR-pathway signalling, making genotoxic strategies such as alkylation mechanistically relevant. While the unmutated IGHV subtype generally responds less durably to chlorambucil-based chemoimmunotherapy than targeted agents (e.g., ibrutinib), the drug retains direct cytotoxic activity through DNA damage induction.

Multiple completed Phase 3 CLL trials — including CAM307 (alemtuzumab vs. chlorambucil, NCT00046683), RESONATE-2 (ibrutinib vs. chlorambucil), and CLL11 (obinutuzumab + chlorambucil vs. rituximab + chlorambucil) — enrolled broad, unselected CLL populations that inherently include pregerminal center patients. These trials collectively represent L1-level evidence for chlorambucil in CLL broadly, and the TxGNN prediction reflects this well-established position in the B-cell lymphoproliferative knowledge graph. Subtype-specific Phase 3 data remain absent, which limits the evidence level to L2 via extrapolation.

---

## Clinical Trial Evidence

Currently no clinical trials are registered specifically targeting pregerminal center CLL/SLL (unmutated IGHV subtype).

> **Context note**: Multiple completed Phase 3 trials in unselected CLL populations used chlorambucil as the active comparator arm (see CAM307, RESONATE-2, CLL11). These trials did not stratify enrollment by IGHV mutation status as an exclusion criterion, meaning the unmutated IGHV subgroup is represented in their datasets — subgroup analyses from these trials would constitute the most accessible source of subtype-specific evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12577769](https://pubmed.ncbi.nlm.nih.gov/12577769/) | 2003 | Review | Nederlands Tijdschrift voor Geneeskunde | Describes two molecular subtypes of CLL — pregerminal center (unmutated IGHV, aggressive) vs. post-germinal center (mutated IGHV, indolent). Notes ~50% of Binet A patients eventually require treatment and >25% die of CLL-related causes; argues for risk-adapted approaches based on IGHV subtype |

---

## Saudi Arabia Market Information

Chlorambucil is currently **not registered or marketed** in Saudi Arabia. No product authorizations are on record. Any clinical use would require importation under a named-patient or compassionate use pathway, subject to SFDA approval.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Nitrogen mustard alkylating agent (chloroethylamine class) |
| Myelosuppression Risk | Moderate-to-High — dose-dependent neutropenia and thrombocytopenia are the primary haematological toxicities; reported in Phase II studies (PMID 3307632) and Phase I dose-escalation (PMID 3179770) |
| Emetogenicity Classification | Low — oral route with relatively low acute emetogenic potential; CNS toxicity (seizures) becomes dose-limiting at high-dose pulse regimens |
| Monitoring Items | CBC with differential (at baseline and at regular intervals during treatment), hepatic function, renal function, neurological assessment at high doses |
| Handling Protection | Must comply with cytotoxic drug handling regulations; closed-system transfer devices recommended; avoid crushing tablets; appropriate PPE required for preparation and administration |

---

## Safety Considerations

Please refer to the package insert for safety information.

> No key warnings, contraindications, or drug interaction data were available in this Evidence Pack. Remediation required: obtain the full prescribing information / package insert (Data Gap DG001) and query DrugBank for DDI data before proceeding to clinical evaluation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Chlorambucil has well-established Phase 3-level evidence in broad, unselected CLL populations — including patients with the unmutated IGHV (pregerminal center) subtype — providing a credible scientific basis for this TxGNN prediction. However, the absence of subtype-specific randomised trial data, missing MOA documentation, and zero Saudi Arabia market authorisations require resolution before advancing.

**To proceed, the following is needed:**

- **Subgroup data extraction**: Request or retrieve IGHV-stratified subgroup analyses from published Phase 3 CLL trials (CAM307, RESONATE-2, CLL11) to quantify chlorambucil efficacy specifically in the unmutated IGHV population
- **MOA documentation** (DG002): Query DrugBank API or published pharmacology references to formally document mechanism of action for the dossier
- **Safety data** (DG001): Obtain and parse the full prescribing information / package insert for key warnings, contraindications, and handling instructions
- **Treatment context clarification**: Determine whether the clinical question concerns chlorambucil monotherapy or combination use (e.g., chlorambucil + obinutuzumab per CLL11), as combination regimens have substantially stronger evidence in unmutated IGHV CLL
- **Regulatory pathway assessment**: Evaluate SFDA named-patient importation or registration requirements given the complete absence of Saudi Arabia market authorisation
- **Comparative effectiveness review**: Benchmark against current standard of care for unmutated IGHV CLL (BTK inhibitors, BCL-2 inhibitors) to contextualise the clinical niche where chlorambucil may remain relevant (e.g., elderly or frail patients with contraindications to targeted agents)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

