---
layout: default
title: Ampicillin
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 10
---

# Ampicillin
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

# Ampicillin: From Bacterial Infections to Laryngitis

## One-Sentence Summary

Ampicillin is a broad-spectrum beta-lactam antibiotic historically used to treat a wide range of bacterial infections, including respiratory tract, urinary tract, and soft tissue infections.
The TxGNN model predicts it may be effective for **Laryngitis**, with **1 clinical trial** and **20 publications** currently identified in support of this direction.
However, the available evidence is indirect — the single trial involved a related combination antibiotic, and the literature largely reflects case reports and observational studies rather than direct ampicillin-in-laryngitis trials.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (no Saudi Arabia regulatory registration on record) |
| Predicted New Indication | Laryngitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L3 (observational studies and guideline review) |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, ampicillin is an aminopenicillin beta-lactam antibiotic that acts by inhibiting bacterial cell wall synthesis through binding to penicillin-binding proteins (PBPs), ultimately causing bacteriolysis. Its spectrum includes streptococci, enterococci, *Listeria*, and — in the pre-resistance era — *Haemophilus influenzae* type b and *Neisseria gonorrhoeae*.

The mechanistic rationale for laryngitis is plausible but context-dependent. Bacterial laryngitis is most commonly caused by *H. influenzae* type b (classically associated with acute epiglottitis), *Streptococcus pyogenes*, and *Streptococcus pneumoniae* — all organisms historically within ampicillin's coverage. Prior to widespread Hib vaccination and the emergence of beta-lactamase-producing strains, ampicillin was a first-line agent for *H. influenzae* epiglottitis. Multiple cohort studies from the 1970s–1990s describe its clinical use in this context.

However, two key limitations constrain this prediction. First, the majority of laryngitis cases are viral in origin, and antibiotics offer no benefit for viral laryngitis. Second, the prevalence of beta-lactamase-producing *H. influenzae* has risen substantially since the 1980s, eroding ampicillin monotherapy effectiveness for bacterial upper airway infections. Current guidelines recommend ampicillin-sulbactam or third-generation cephalosporins rather than ampicillin alone for confirmed bacterial laryngitis. The TxGNN high-score prediction likely reflects the strong graph-network co-occurrence between ampicillin and upper respiratory tract infection nodes, rather than a direct, validated treatment relationship.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01406275](https://clinicaltrials.gov/study/NCT01406275) | N/A (Post-marketing surveillance) | Completed | 363 | Post-marketing safety/efficacy study of **amoxicillin/clavulanate** (CLAVAMOX®) in Japanese paediatric patients with multiple indications including laryngitis; direct ampicillin evidence is not provided |

> **Note:** No registered clinical trials directly evaluating ampicillin monotherapy for laryngitis were identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39879424](https://pubmed.ncbi.nlm.nih.gov/39879424/) | 2025 | Guideline Review | CoDAS | Quality assessment (AGREE II) of clinical guidelines for laryngitis and pharyngitis management; provides methodological framework for evidence-based antibiotic decision-making |
| [5314768](https://pubmed.ncbi.nlm.nih.gov/5314768/) | 1971 | Cohort | British Medical Journal | Early cohort describing epiglottitis in adults with antibiotic management context |
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | Cohort | Anaesthesia and Intensive Care | Review of 161 paediatric acute epiglottitis cases (1975–1984); describes airway management and antibiotic use, with five deaths; contextualises severity of bacterial laryngeal disease |
| [25944348](https://pubmed.ncbi.nlm.nih.gov/25944348/) | 2015 | Cohort | Otolaryngology–Head and Neck Surgery | Hospital-level variation in perioperative antibiotic choice for laryngectomy and its association with surgical site infection rates; highlights importance of antibiotic selection in laryngeal surgery |
| [6465636](https://pubmed.ncbi.nlm.nih.gov/6465636/) | 1984 | Case Series | Annals of Emergency Medicine | Three adult epiglottitis cases; emphasises diagnostic difficulty and antibiotic treatment in acute upper airway obstruction |
| [2603419](https://pubmed.ncbi.nlm.nih.gov/2603419/) | 1989 | Cohort | Western Journal of Medicine | Nine adult acute epiglottitis cases over 2 years; intubation required in 44%; describes antibiotic treatment and outcomes |
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | Case Report | Annals of Otology, Rhinology, and Laryngology | Novel case of spontaneous laryngeal abscess in uncontrolled diabetes; historical review of modern cases in the antibiotic era; notes rarity since introduction of broad-spectrum antibiotics |
| [30579693](https://pubmed.ncbi.nlm.nih.gov/30579693/) | 2019 | Case Report | Auris Nasus Larynx | Laryngeal actinomycosis post-bone marrow transplantation; treated with high-dose penicillin (ampicillin-class); supports beta-lactam use in specific bacterial laryngeal infections |
| [34986973](https://pubmed.ncbi.nlm.nih.gov/34986973/) | 2023 | Case Report | Auris Nasus Larynx | COVID-19-associated acute epiglottitis requiring emergency airway management; underscores need for broad-spectrum antibiotic cover in severe laryngeal presentations |
| [1712371](https://pubmed.ncbi.nlm.nih.gov/1712371/) | 1991 | Case Series | Journal of Clinical Gastroenterology | Short-term antibiotic treatment of Whipple's disease in 19 patients; one patient specifically treated with **ampicillin** 2 g/day with clinical response — indirect evidence of ampicillin activity in systemic infectious disease context |

---

## Saudi Arabia Market Information

Ampicillin has **no registered pharmaceutical licenses** in Saudi Arabia (SFDA/NCBE database). The drug is not currently marketed in the Saudi market.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data including key warnings, contraindications, and drug interactions were not retrievable in this Evidence Pack (classified as data gaps DG001 and DG002). Clinicians should consult the current SmPC or product labelling before any clinical application. Known class-level concerns for beta-lactam penicillins include hypersensitivity reactions (including anaphylaxis), ampicillin-associated maculopapular rash (particularly in patients with Epstein-Barr virus infection or CLL), and Clostridioides difficile-associated diarrhoea.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's high prediction score (99.97%) for ampicillin in laryngitis is mechanistically plausible for bacterial laryngitis caused by *H. influenzae* or streptococcal species, but current evidence is limited to indirect observational data and case reports (L3). No clinical trial directly evaluates ampicillin monotherapy in laryngitis, and increasing beta-lactamase resistance among key pathogens substantially limits real-world clinical utility compared to newer agents or combination regimens.

**To proceed, the following is needed:**
- Clarification of MOA data (DrugBank API query — flagged as DG002 High severity)
- Retrieval of current Saudi Arabia SmPC/warnings and contraindications (DG001 Blocking)
- Drug-drug interaction data (DDI query returned not_found; re-query recommended)
- A targeted literature review distinguishing viral vs. bacterial laryngitis populations and identifying any head-to-head comparison of ampicillin against current standard-of-care (ampicillin-sulbactam or cephalosporins) in bacterial upper airway infections
- Epidemiological data on local *H. influenzae* beta-lactamase prevalence in the target market to assess whether ampicillin monotherapy retains residual clinical viability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

