---
layout: default
title: Clofazimine
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 3
---

# Clofazimine
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

# Clofazimine: From Leprosy to Pneumocystosis

## One-Sentence Summary

Clofazimine (Lamprene) is an antimycobacterial agent used in the treatment of leprosy and drug-resistant tuberculosis as part of multidrug regimens.
The TxGNN model predicts it may be effective for **Pneumocystosis** (Pneumocystis jirovecii pneumonia, PCP),
with **1 clinical trial** and **4 publications** retrieved — however, none directly study clofazimine as a treatment for Pneumocystosis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Leprosy; drug-resistant tuberculosis (no Saudi Arabia approval on record) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, clofazimine is a riminophenazine dye with established antimycobacterial activity. It is understood to exert its effects by generating reactive oxygen species (ROS), disrupting mycobacterial cell membranes, and interfering with microbial electron transport chains. These mechanisms are specifically targeted against mycobacterial pathogens — primarily *Mycobacterium leprae* (leprosy), *M. tuberculosis* complex, and *M. avium* complex (MAC).

Pneumocystosis, however, is caused by *Pneumocystis jirovecii*, an atypical fungus. The known pharmacological targets of clofazimine have no established cross-reactivity with the cell wall architecture, sterol composition, or metabolic pathways of Pneumocystis. There is no preclinical or clinical evidence that riminophenazines possess anti-Pneumocystis activity at clinically achievable concentrations.

The most plausible explanation for this TxGNN prediction is an epidemiological co-morbidity artefact: both MAC infection and PCP are common opportunistic infections in advanced AIDS/HIV patients, and the knowledge graph likely captured this co-occurrence as a shared disease association with clofazimine. The model appears to have constructed a spurious link through shared patient populations rather than a true pharmacological signal. This prediction should be treated as a hypothesis-generating artefact, not a biological finding.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002058](https://clinicaltrials.gov/study/NCT00002058) | N/A | Completed | N/A | Randomized prophylaxis study evaluating clofazimine for **MAC infection** in HIV-infected individuals; a prior episode of *Pneumocystis carinii* pneumonia was used as an **enrollment criterion**, not a treatment target — no data on clofazimine efficacy against Pneumocystosis |

> **Assessment:** The single retrieved trial (NCT00002058) concerns MAC prophylaxis in AIDS patients. PCP history is mentioned only as an eligibility criterion for a high-risk HIV population. This trial provides **no direct evidence** of clofazimine activity against Pneumocystosis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8501340](https://pubmed.ncbi.nlm.nih.gov/8501340/) | 1993 | RCT | *J Infect Dis* | Clofazimine 50 mg as MAC prophylaxis in 110 HIV patients (enrollment included patients with prior PCP episode or CD4 ≤100/mm³); study endpoint was MAC infection — PCP was a patient characteristic, not an outcome measure |
| [2714863](https://pubmed.ncbi.nlm.nih.gov/2714863/) | 1989 | Case Report | *Infection* | Swiss AIDS patient with *M. kansasii* lung disease complicated by PCP; clofazimine was used as part of the anti-mycobacterial regimen — TMP-SMX was the agent used for PCP; clofazimine not implicated in PCP treatment |
| [6299154](https://pubmed.ncbi.nlm.nih.gov/6299154/) | 1983 | Case Report | *Ann Intern Med* | Hemophiliac AIDS patient presenting with PCP followed by disseminated MAC-intracellulare; clofazimine role is in MAC management — no data on Pneumocystosis treatment |
| [11363899](https://pubmed.ncbi.nlm.nih.gov/11363899/) | 1996 | Review | *PI Perspective* | General opportunistic infections update for AIDS patients; contextual document with no specific clofazimine-vs-PCP data |

> **Assessment:** None of the 4 retrieved publications evaluate clofazimine as treatment or prophylaxis for Pneumocystosis. PCP appears consistently as a co-morbidity marker in advanced AIDS patients enrolled for MAC studies. The literature supports clofazimine's anti-mycobacterial role only.

---

## Saudi Arabia Market Information

Clofazimine is **not approved or marketed in Saudi Arabia**. No regulatory licenses are on record. Availability would require importation through special access or compassionate use channels.

---

## Safety Considerations

Safety data (package insert warnings, contraindications, and drug interaction profile) were not available in this Evidence Pack.

Please refer to the official package insert for safety information. Known class-level concerns for clofazimine include irreversible red-brown skin and body fluid discoloration, gastrointestinal toxicity (nausea, abdominal pain, enteropathy), QT interval prolongation (of particular concern in AIDS patients on other QT-prolonging agents), and rare crystal deposition in intestinal tissues. These require confirmation from the current prescribing information before clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for clofazimine in pneumocystosis is rated L5 — model prediction only, with no direct mechanistic, preclinical, or clinical evidence supporting this repurposing hypothesis. Every retrieved study involves clofazimine in a MAC/mycobacterial treatment context within an AIDS population where PCP co-occurs as a background infection; none tested clofazimine against *Pneumocystis jirovecii*. The prediction is most likely a knowledge-graph co-morbidity artefact and does not reflect a true pharmacological signal.

**To proceed, the following would be required:**
- In vitro activity data demonstrating clofazimine or riminophenazine analogues have activity against *Pneumocystis jirovecii* at clinically relevant concentrations
- A mechanistic rationale explaining how clofazimine's ROS generation or membrane disruption would affect a fungal (not mycobacterial) pathogen with a distinct cell wall structure
- Preclinical in vivo data in an immunocompromised animal model of PCP before any clinical investigation is warranted
- Confirmed MOA data from DrugBank and package insert to close the existing data gaps (DG001, DG002) before any further investment in this prediction direction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

