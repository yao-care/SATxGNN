---
layout: default
title: Metronidazole
parent: 僅模型預測 (L5)
nav_order: 418
evidence_level: L5
indication_count: 10
---

# Metronidazole
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

# Metronidazole: From Anaerobic/Protozoal Infections to Pneumocystosis

## One-Sentence Summary

Metronidazole is a nitroimidazole antimicrobial historically used against anaerobic bacterial and protozoal infections (e.g., amoebiasis, trichomoniasis, bacterial vaginosis). The TxGNN model predicts it may be effective for **Pneumocystosis (Pneumocystis pneumonia)** with a very high similarity score (99.99%), but this is a **model-only prediction (L5)** — no clinical trials or literature directly support therapeutic use, and the underlying pharmacological mechanism appears incompatible with the target pathogen.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Saudi Arabia regulatory records (drug is not marketed); per literature in this evidence pack, historically indicated for anaerobic bacterial and protozoal infections (amoebic colitis, trichomoniasis) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not currently available (data gap, High severity). Based on known pharmacology and the mechanistic analysis included in this evidence pack, metronidazole is a nitroimidazole **prodrug**: it requires reductive activation under **anaerobic conditions** to form cytotoxic free-radical intermediates that damage microbial DNA. This mechanism is effective only against obligate/facultative anaerobic bacteria and select anaerobic protozoa (e.g., *Trichomonas*, *Entamoeba*, *Giardia*).

*Pneumocystis jirovecii*, the causative organism of pneumocystosis, is a fungus that does not share this anaerobic reductive-activation pathway. Mechanistically, there is **no established pathway** by which metronidazole would exert antimicrobial activity against it, and the accepted standard of care for this condition is trimethoprim-sulfamethoxazole (TMP-SMX), a wholly different drug class.

The high TxGNN similarity score likely reflects indirect associations in the knowledge graph — several of the retrieved literature items describe patients who happened to receive metronidazole for an unrelated indication (e.g., amoebic dysentery, diarrhea) and were separately diagnosed with Pneumocystis pneumonia, rather than metronidazole being used to treat pneumocystosis itself. This is graph co-occurrence noise rather than a therapeutic signal, which is consistent with the evidence pack's own recommendation of **Hold** at decision stage S0.

## Clinical Trial Evidence

The clinicaltrials.gov search returned 24 trials, but on relevance review essentially all are unrelated to metronidazole or pneumocystosis (primary-care payment models, dementia care technology, depression apps, diabetes care programs, etc.) — database co-occurrence noise rather than genuine drug-indication trials. No trial testing metronidazole for pneumocystosis was identified.

**Currently no related clinical trials registered.**

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | American Family Physician | Explicitly lists metronidazole as drug of choice for amebic colitis/trichomoniasis, while noting **TMP-SMX** (not metronidazole) is the drug of choice for Pneumocystis pneumonia — supports mechanistic separation rather than overlap |
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clinic Proceedings | General review of antiparasitic agents; does not address pneumocystosis-specific use |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clinical Pharmacokinetics | Pharmacokinetic rationale for antiprotozoal therapy in normal and immunocompromised hosts; general |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Topics in Antiviral Medicine | Overview of HIV-related opportunistic infections including PCP; does not mention metronidazole as treatment |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clinical Pharmacy | Reviews AIDS infectious complications (PCP most common); metronidazole not discussed as PCP therapy |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Reviews of Infectious Diseases | General critique of antimicrobial prophylaxis trials; not specific to this drug-disease pair |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case Report | American Review of Respiratory Disease | Patient treated with metronidazole/tetracycline for diarrhea later developed Pneumocystis carinii pneumonia + CMV — incidental temporal association, not treatment of PCP |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case Report | Kansenshogaku Zasshi | AIDS patient treated with metronidazole for amebic dysentery, subsequently diagnosed with PCP — incidental co-occurrence, not causal treatment evidence |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case Report | J Formosan Medical Association | AIDS patient with CMV and amoebic colitis (metronidazole used for amoebiasis, not PCP) |
| [2280469](https://pubmed.ncbi.nlm.nih.gov/2280469/) | 1990 | Review | Nihon Rinsho | General review of antiprotozoal drugs; abstract not available |

## Saudi Arabia Market Information

Metronidazole is currently **not marketed** in Saudi Arabia per this evidence pack (0 authorizations on record). No product listing is available to summarize.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are marked as not yet available in this evidence pack — TFDA/SFDA package insert retrieval is flagged as a Blocking data gap.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN similarity score (99.99%), the evidence level is L5 (model prediction only) — no clinical trials and no literature support therapeutic use of metronidazole for pneumocystosis, and the drug's anaerobic-reduction mechanism is not applicable to *Pneumocystis jirovecii*, a fungus with no analogous activation pathway. The standard of care (TMP-SMX) is unrelated in class and mechanism.

**To proceed, the following is needed:**
- TFDA/SFDA package insert with full warnings/contraindications (DG001, Blocking — required before any S1 safety screening)
- Structured DrugBank mechanism-of-action data (DG002, High)
- If further repurposing signals for this drug are pursued, prioritize the pack's higher-support candidates instead — **cap polyposis** (L3, direct mechanistic literature including a dedicated case series questioning an anti-inflammatory mode of action) and **ulcerative proctosigmoiditis** / **vulvar ulceration (amoebic subset)** (both L4, plausible anaerobic/antiprotozoal mechanistic fit) — rather than pneumocystosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

