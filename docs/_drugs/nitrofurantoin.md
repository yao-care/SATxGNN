---
layout: default
title: Nitrofurantoin
parent: 僅模型預測 (L5)
nav_order: 446
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
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

# Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin is a nitrofuran antibacterial classically used to treat urinary tract infections (UTI); this indication is not present as structured data in this evidence pack but is corroborated by the pack's own literature (bacteriuria screening, UTI treatment references). The TxGNN model predicts a possible link to **Rheumatoid Arthritis**, but the **12 supporting publications** consist almost entirely of case reports and reviews describing nitrofurantoin-induced pulmonary/hepatic toxicity and antibiotic-associated RA flares — the evidence direction points toward **risk, not therapeutic benefit**. No clinical trials support this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (UTI) / bacteriuria — inferred from literature context; no structured `original_indications` or license data available in this pack |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on known pharmacology, nitrofurantoin is a synthetic nitrofuran antibacterial whose antimicrobial effect comes from bacterial nitroreductase activation, producing reactive intermediates that damage bacterial DNA, ribosomal proteins, and metabolic enzymes. There is no known anti-inflammatory, immunomodulatory, or synovial-targeting pathway that would plausibly extend this mechanism to rheumatoid arthritis.

The literature returned for this pairing does not support a therapeutic rationale. Instead, it clusters around two risk signals: (1) a self-controlled case series (n=31,992 RA patients, CPRD GOLD) examining whether antibiotic exposure is associated with RA flares, and (2) multiple case reports/reviews of nitrofurantoin-induced pulmonary fibrosis and hepatotoxicity — including one report where nitrofurantoin combined with methotrexate (a standard RA drug) caused irreversible pulmonary fibrosis in an RA patient. The TxGNN embedding proximity here most plausibly reflects the frequent literature co-occurrence of "nitrofurantoin" and "rheumatoid arthritis" in adverse-event and drug-interaction reporting, rather than a genuine efficacy signal.

Given the absence of any mechanistic or clinical-trial support, and the presence of literature actively describing harm in this exact patient population (RA patients on methotrexate who receive nitrofurantoin for UTI), this candidate should be treated as a negative/risk signal rather than a repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Self-controlled Case Series | Scientific reports | Nested self-controlled case series in 31,992 newly diagnosed RA patients (UK CPRD GOLD); examined association between antibiotic exposure/timing and RA flares |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | 57 RA patients hospitalized for interstitial lung fibrosis; rare but poor-prognosis complication (~1 per 3,500 patient-years) |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi medical journal | Review of drug-induced pulmonary fibrosis; lists nitrofurantoin among causative drugs and notes RA itself predisposes to fibrosis |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case Report | Cureus | 94-year-old RA patient on long-term methotrexate developed irreversible pulmonary fibrosis after starting nitrofurantoin for a UTI — a drug-drug interaction, not a therapeutic use |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du praticien | Review of drug-induced interstitial lung disease; nitrofurantoin listed among implicated antibiotics |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case Report | Cureus | Differential-diagnosis discussion of autoimmune hepatitis; nitrofurantoin and RA both listed as possible confounding causes, not as treatment |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case Report | Annales de dermatologie et de venereologie | Case of phenylbutazone-induced sialadenitis; nitrofurantoin mentioned as another drug associated with sialadenitis, unrelated to RA treatment |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Cohort | Acta medica Scandinavica | Screening and short-term nitrofurantoin therapy for bacteriuria in middle-aged women — standard UTI indication, not RA-related |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case Report | Revue de pneumologie clinique | Gold-salt-induced pneumonitis with CD4 alveolitis; nitrofurantoin is not the causative drug in this case, only tangentially referenced |
| [4608019](https://pubmed.ncbi.nlm.nih.gov/4608019/) | 1974 | Review | Der Internist | German-language synopsis on alveolitis and pulmonary fibrosis; no abstract available |

---

## Saudi Arabia Market Information

Nitrofurantoin is not currently marketed in Saudi Arabia — no product authorization records are available in this pack (0 licenses).

---

## Safety Considerations

Structured safety data (key warnings, contraindications, drug interactions) is not available for this drug in the current pack (SFDA package insert not retrieved; DDI query returned no results).

Please refer to the package insert for safety information. Separately, the literature reviewed above for this indication surfaces recurring toxicity signals relevant to any repurposing evaluation: nitrofurantoin-induced pulmonary fibrosis (including a clinically significant interaction with methotrexate), drug-induced hepatotoxicity/autoimmune hepatitis, and methemoglobinemia (seen in other predicted-indication branches of this pack, ranks 8 and 10). These should be treated as material risk factors, particularly given overlap with the RA patient population (frequent methotrexate co-therapy).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials support this indication, no mechanistic pathway links nitrofurantoin to RA treatment, and the available literature describes harm (pulmonary fibrosis, drug interaction with methotrexate, RA-flare association with antibiotic use) rather than benefit. The TxGNN score is high, but the evidence base contradicts rather than supports the prediction.

**To proceed, the following is needed:**
- SFDA package insert (warnings, contraindications) — currently a blocking data gap
- Verified mechanism of action data from DrugBank
- Any prospective or mechanistic evidence of anti-inflammatory/immunomodulatory activity, since current literature supports only a risk association
- Reconciliation of the methotrexate–nitrofurantoin interaction signal before this candidate can be considered for RA patients specifically
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

