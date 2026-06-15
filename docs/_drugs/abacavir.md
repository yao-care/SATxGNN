---
layout: default
title: Abacavir
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
---

# Abacavir
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

# Abacavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Abacavir is a nucleoside reverse transcriptase inhibitor (NRTI) widely used as part of combination antiretroviral therapy for HIV-1 infection.
The TxGNN model predicts it may also be effective against **Simian Immunodeficiency Virus (SIV) Infection**, supported by **no registered clinical trials** and **1 preclinical in vitro publication** to date.
All three top-ranked predicted indications are non-human diseases or an ultra-rare genetic neurological disorder, reflecting a prediction profile that warrants careful scientific interpretation before clinical translation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (combination antiretroviral therapy) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Abacavir belongs to the carbocyclic nucleoside analogue subclass of NRTIs. Its active intracellular metabolite — carbovir triphosphate (CBV-TP) — competitively inhibits HIV reverse transcriptase and acts as a chain terminator, blocking viral DNA elongation. Abacavir's efficacy in HIV-1 (and HIV-2) infection is well-established in international clinical guidelines and practice.

The mechanistic connection to SIV infection is biologically grounded: SIV and HIV belong to the same *Lentivirus* genus, and their reverse transcriptase enzymes share high structural homology. Carbovir triphosphate can theoretically engage the SIV polymerase active site in the same way it does HIV reverse transcriptase. A 2004 in vitro study (PMID 15040537) directly evaluated 16 approved antiretroviral drugs — including abacavir — against SIV strains (mac251 and B670), providing empirical preclinical support for this mechanism-based cross-reactivity.

That said, SIV naturally infects non-human primates, not humans. Documented human SIV infection cases are extremely rare (isolated occupational exposures), and no formal treatment guidelines exist for this scenario. This prediction therefore reflects a biologically plausible cross-species activity rather than a conventional clinical repurposing pathway. Its most realistic human clinical niche would be post-exposure prophylaxis (PEP) for laboratory or veterinary workers at occupational risk — a context already covered by existing HIV PEP protocols in which Abacavir-containing regimens are already an option.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Abacavir in simian immunodeficiency virus infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro cross-virus susceptibility study | Antiviral Therapy | Tested 16 approved antiretrovirals (including Abacavir) and experimental AMD3100 against HIV-2 (ROD, EHO), SIV (mac251, B670), and SHIV strains; provides direct preclinical evidence for Abacavir activity against SIV reverse transcriptase, relevant to treatment and post-exposure prophylaxis contexts |

---

## Saudi Arabia Market Information

Abacavir currently has no approved products registered in Saudi Arabia (0 authorizations on record). It is not marketed in this territory based on available regulatory data.

> **Note:** Abacavir is internationally approved and widely used globally (e.g., US FDA, EMA) as part of HIV combination regimens such as Triumeq (abacavir/dolutegravir/lamivudine) and Epzicom/Kivexa (abacavir/lamivudine). Absence from the Saudi Arabia registry does not reflect clinical unavailability worldwide.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key safety considerations known from international labeling include a serious, potentially fatal **hypersensitivity reaction** associated with the *HLA-B\*5701* allele (mandatory pre-treatment genetic screening is required in most guidelines), as well as cardiovascular risk signals in high-risk patients. These were flagged as data gaps (DG001) in this evidence pack and should be retrieved from the official Saudi Arabia/SFDA-registered package insert before any clinical decision-making.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (SIV infection) represents a biologically plausible but non-human clinical indication with only a single in vitro preclinical publication (L4 evidence) and no registered clinical trials. The second- and third-ranked predictions (Feline AIDS and a rare neurodevelopmental disorder) face similarly fundamental barriers to human clinical translation — the four clinical trials retrieved for Feline AIDS are all Grade C misclassifications (they are actually human HIV-1 dolutegravir studies, not feline disease trials). There is no viable novel repurposing pathway to pursue at this stage.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Retrieve Abacavir safety warnings and contraindications from the official package insert — particularly *HLA-B\*5701* hypersensitivity screening requirements — before any safety evaluation can proceed
- **Resolve DG002 (High):** Obtain formal MOA data from DrugBank to complete mechanistic plausibility analysis
- **Clarify repurposing intent:** If the goal is human clinical repurposing, SIV and Feline AIDS are veterinary/primate indications; redirect analysis toward Abacavir's potential in human lentiviral or retroviral-associated conditions (e.g., HIV-associated neurocognitive disorders, HTLV-associated myelopathy)
- **PEP niche assessment:** Evaluate whether the SIV finding strengthens the evidence base for occupational PEP guidelines — a narrowly actionable human clinical context
- **Saudi Arabia registration pathway:** If market entry is the goal, initiate SFDA regulatory assessment and literature review for HIV-1 indication (the established use), rather than the predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

