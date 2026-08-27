---
layout: default
title: Roxithromycin
parent: 僅模型預測 (L5)
nav_order: 561
evidence_level: L5
indication_count: 8
---

# Roxithromycin
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

# Roxithromycin: From Bacterial Infections to Leprosy

## One-Sentence Summary

> Roxithromycin is a macrolide antibiotic (erythromycin-class); its specific original approved indication is not available in this evidence pack due to a data gap.
> The TxGNN model predicts it may be effective for **Leprosy**,
> with **0 registered clinical trials** and **5 publications** (preclinical/mechanistic) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — data gap (roxithromycin is a macrolide antibiotic; no approved indication text on file) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for roxithromycin is not available. Based on known information, roxithromycin belongs to the macrolide antibiotic class (related to erythromycin and clarithromycin), whose efficacy in bacterial infections is well established; mechanistically it may be applicable to leprosy given documented class-wide activity against *Mycobacterium leprae*.

The supporting literature is preclinical and mechanistic rather than clinical. In vitro and mouse-footpad studies show that several macrolides — including roxithromycin — inhibit *M. leprae* growth and are bactericidal in animal models (PMID 1648889, PMID 3072920, PMID 2665640). A Japanese case-series/review (PMID 10481449) further notes roxithromycin's anti-inflammatory and immunomodulatory activity alongside its direct anti-mycobacterial effect, both potentially relevant to leprosy's neuroinflammatory complications.

However, a key caveat from the same evidence: in head-to-head mouse studies, clarithromycin was found superior to roxithromycin, with higher drug levels at the infection site (PMID 1648889). This means the prediction rests on a **class-effect inference** rather than roxithromycin-specific human data — clarithromycin, not roxithromycin, is the macrolide actually used in clinical leprosy regimens.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12762831](https://pubmed.ncbi.nlm.nih.gov/12762831/) | 2003 | Review | American Journal of Clinical Dermatology | General review of macrolide antibacterials in skin/soft-tissue infections, covering mechanism of action and drug interactions relevant to the class |
| [10481449](https://pubmed.ncbi.nlm.nih.gov/10481449/) | 1999 | Clinical/Case series | Nihon Hansenbyo Gakkai zasshi (Jpn J Leprosy) | Roxithromycin, alongside clarithromycin, minocycline and fosfomycin, shows anti-inflammatory/immunomodulatory activity plus direct anti-*M. leprae* activity relevant to control of leprous peripheral neuropathy |
| [3072920](https://pubmed.ncbi.nlm.nih.gov/3072920/) | 1988 | In vitro/Animal | Antimicrobial Agents and Chemotherapy | Evaluated newer macrolides (including roxithromycin) against *M. leprae* in vitro and in vivo, building on earlier erythromycin activity data |
| [1648889](https://pubmed.ncbi.nlm.nih.gov/1648889/) | 1991 | Animal (mouse) | Antimicrobial Agents and Chemotherapy | Mouse footpad model: roxithromycin and clarithromycin were both bactericidal against *M. leprae*; clarithromycin was superior, likely due to higher tissue levels at the infection site |
| [2665640](https://pubmed.ncbi.nlm.nih.gov/2665640/) | 1989 | In vitro | Antimicrobial Agents and Chemotherapy | In vitro macrophage screen of >25 antimicrobial agents for anti-leprosy potential via inhibition of phenolic glycolipid I synthesis |

---

## Saudi Arabia Market Information

Roxithromycin is not currently marketed in Saudi Arabia (0 authorizations on record; market status: 未上市/Not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to preclinical/animal and mechanistic studies (L4) with zero registered clinical trials, and the one comparative animal study available shows roxithromycin was *less* effective than clarithromycin against *M. leprae* — the macrolide with actual clinical precedent in leprosy. This is class-effect inference, not roxithromycin-specific human evidence.

**To proceed, the following is needed:**
- TFDA/SFDA package insert data on warnings and contraindications (currently a Blocking data gap — required before any S1 safety screen)
- Confirmed mechanism of action (MOA) data from DrugBank (High-severity data gap)
- Head-to-head or roxithromycin-specific efficacy data against *M. leprae* (current evidence favors clarithromycin)
- Verification of roxithromycin's original approved indication(s), currently unavailable

*Note: Seven additional TxGNN-predicted indications (hypertrichosis, periodontal-related malformation syndrome, Ambras syndrome, Dandy-Walker-associated syndrome, hair shaft abnormality, nephrogenic SIAD, pulmonary hypertension) were also screened. All scored L5/Hold except pulmonary hypertension (L4/Research Question, based on indirect COPD-antibiotic-prophylaxis literature, not disease-specific evidence). None are reported in full here due to absent or non-specific supporting evidence.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

