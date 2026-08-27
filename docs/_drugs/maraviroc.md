---
layout: default
title: Maraviroc
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
---

# Maraviroc
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

# Maraviroc: From HIV-1 Infection to HER2-Positive Breast Carcinoma

## Note on Candidate Selection

This Evidence Pack lists 10 TxGNN-predicted indications for maraviroc. The raw top-ranked hit by score (**multiple endocrine neoplasia**, 99.82%) is explicitly flagged in its own `repurposing_rationale` as model noise — MEN is a RET/MEN1-driven endocrine syndrome with no known link to CCR5 signaling, and no supporting trials or literature exist. Eight of the ten candidates share this pattern: high TxGNN scores with no mechanistic or evidentiary support (L5), or literature that is merely HIV-comorbidity co-occurrence rather than a treatment hypothesis (candidiasis, CMV infection, cutaneous lymphomas via an unrelated receptor, ACKR1).

Only **rank 10 — HER2-positive breast carcinoma** — has a literature-supported, receptor-correct mechanistic hypothesis (evidence level L3, decision stage S1, "Research Question"). This report focuses on that candidate as the only scientifically defensible one in the set.

---

## One-Sentence Summary

Maraviroc is a CCR5 co-receptor antagonist used in combination antiretroviral therapy for HIV-1 infection. Among 10 TxGNN-predicted indications, the only one with a coherent, receptor-correct mechanistic rationale is **HER2-Positive Breast Carcinoma**, where a single in vitro mechanistic study — but **zero clinical trials** — supports the hypothesis that blocking CCR5 could reverse trastuzumab resistance.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (CCR5 co-receptor antagonist, combination antiretroviral therapy) — not captured in `original_indications`/`original_moa`, which are flagged as data gaps (DG002) in this pack; inferred from drug identity and corroborating HIV/ART context across the literature evidence |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.22% (global rank 11,167) |
| Evidence Level | L3 |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question stage) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for maraviroc is flagged as a data gap in this pack (DG002, High severity). Based on known information, maraviroc is a CCR5 co-receptor antagonist that blocks HIV-1 entry into CD4+ T-cells by preventing gp120 binding to CCR5; its efficacy in HIV-1 infection is well established as part of combination antiretroviral therapy.

The mechanistic bridge to HER2-positive breast carcinoma comes from a single in vitro study (PMID 32404410): HER2-positive breast cancer cells can autocrine-secrete the chemokine CCL5, which activates CCR5 and drives ERK pathway signaling, and this autocrine loop was shown to mediate resistance to trastuzumab. Since maraviroc directly antagonizes CCR5, it is the only receptor-correct candidate among the 10 predictions — the drug's known target directly matches the receptor implicated in the disease mechanism, unlike the other candidates, which either lack any mechanistic literature or point to a different receptor entirely (e.g., ACKR1 in the cutaneous lymphoma hits).

This remains a preclinical, in vitro hypothesis only. There is no evidence yet that CCR5 blockade with maraviroc restores trastuzumab sensitivity in animal models or patients, and no clinical trials have tested this combination.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32404410](https://pubmed.ncbi.nlm.nih.gov/32404410/) | 2020 | Mechanistic/In vitro | Molecular Cancer Therapeutics | Autocrine CCL5 secretion by HER2-positive breast cancer cells activates CCR5, driving ERK pathway activation and mediating resistance to trastuzumab — the mechanistic basis for testing a CCR5 antagonist in this setting |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question stage)**

**Rationale:**
The only mechanistically coherent prediction in this candidate set (HER2-positive breast carcinoma) is supported by a single in vitro study with no in vivo, animal, or clinical validation, and the drug is not currently marketed in Saudi Arabia. This is a research hypothesis, not an evidence base sufficient for clinical consideration.

**To proceed, the following is needed:**
- TFDA/regulatory package insert data on warnings and contraindications (DG001, currently blocking)
- Drug mechanism-of-action confirmation from DrugBank or equivalent (DG002)
- In vivo (animal) validation that CCR5 blockade reverses trastuzumab resistance in HER2+ models
- If preclinical validation succeeds, a Phase 1/2 trial design combining maraviroc with trastuzumab in trastuzumab-resistant HER2+ breast cancer patients
- Oncology-population safety and drug-interaction data for maraviroc (none currently available; DDI query returned no results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

