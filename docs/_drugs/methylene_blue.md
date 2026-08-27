---
layout: default
title: Methylene Blue
parent: 僅模型預測 (L5)
nav_order: 415
evidence_level: L5
indication_count: 3
---

# Methylene Blue
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

# Methylene Blue: From Redox/Diagnostic Dye to Three TxGNN-Predicted Indications

## One-Sentence Summary

Methylene blue is not currently marketed in Saudi Arabia, and this evidence pack has no data on its original approved indication or mechanism of action (both flagged as data gaps — DG001 Blocking, DG002 High). TxGNN produced three predictions: **bronchitis** (highest score, 0.9997), **methemoglobinemia, alpha type** (0.9936), and **methemoglobinemia due to methemoglobin reductase deficiency** (0.9936). Only the third has credible mechanistic and literature support — the top-ranked bronchitis prediction is explicitly flagged in the evidence as a likely embedding-similarity false positive with no treatment-relevant evidence.

---

## Quick Overview

| Item | Bronchitis (Rank 1) | Methemoglobinemia, alpha type (Rank 2) | Methemoglobinemia due to reductase deficiency (Rank 3) |
|------|------|------|------|
| TxGNN Prediction Score | 99.97% | 99.36% | 99.36% |
| Evidence Level | L5 | L4 | L3 |
| Clinical Trials | 0 | 0 | 0 |
| Literature | 10 | 2 | 5 |
| Recommended Decision | Hold | Research Question | Proceed with Guardrails |

| Item | Content |
|------|------|
| Original Indication | Not available — no approved-indication data in this evidence pack |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for methylene blue in this evidence pack (DG002). The available literature does, however, describe a well-characterized redox mechanism relevant to one of the three predictions: methylene blue is reduced by NADPH-dependent methemoglobin reductase to leucomethylene blue, which in turn non-enzymatically reduces Fe³⁺ methemoglobin back to functional Fe²⁺ hemoglobin — bypassing the deficient NADH–cytochrome b5 reductase (diaphorase I) pathway seen in hereditary methemoglobin reductase deficiency. This is textbook-level, mechanism-matched pharmacology, not a speculative association, and is consistent with methylene blue's known clinical role as a reducing agent.

**Methemoglobinemia due to reductase deficiency (Rank 3):** Direct mechanistic fit as above. G6PD deficiency must be excluded first, since G6PD-deficient patients lack the NADPH supply this pathway depends on, and methylene blue can be ineffective or precipitate hemolysis in that setting.

**Methemoglobinemia, alpha type (Rank 2):** The same reductive mechanism applies only if "alpha type" refers to the erythrocyte-restricted diaphorase deficiency (RCM Type I). If it instead refers to HbM disease (structural globin-chain/heme-pocket mutations), methylene blue cannot reduce the structurally abnormal hemoglobin and is pharmacologically ineffective — a known contraindication-type distinction. The two literature items provided do not resolve which subtype is meant, so this prediction stays a research question rather than an actionable one.

**Bronchitis (Rank 1):** No treatment-relevant mechanistic link exists. Across the 10 retrieved publications, methylene blue appears almost exclusively as a diagnostic/histologic stain (bronchoscopic tumor staining, chromoendofibroscopy) or as a laboratory tracer/reagent (bronchoalveolar lavage fluid quantitation, biosensor/tracer studies), with several other citations unrelated to methylene blue at all (case reports, an unrelated beta-blocker study, unrelated plant extracts). The high TxGNN score here is best explained as an embedding-similarity artifact rather than genuine therapeutic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the three predicted indications (bronchitis, methemoglobinemia alpha type, or methemoglobinemia due to reductase deficiency).

---

## Literature Evidence

### Methemoglobinemia due to methemoglobin reductase deficiency (strongest evidence, Rank 3)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36638001](https://pubmed.ncbi.nlm.nih.gov/36638001/) | 2023 | Retrospective cohort (veterinary) | Am J Vet Res | Long-term oral methylene blue in dogs with hereditary CYB5R (diaphorase) deficiency reduced methemoglobin levels and characterized the inflammatory phenotype |
| [35202847](https://pubmed.ncbi.nlm.nih.gov/35202847/) | 2022 | Case report (veterinary) | Top Companion Anim Med | Oral methylene blue corrected elevated methemoglobin (35%) in a CYB5R-deficient dog |
| [29845943](https://pubmed.ncbi.nlm.nih.gov/29845943/) | 2018 | Case report | Neth J Med | 61-year-old with congenital methemoglobinemia (novel CYB5R3 variant); methylene blue produced transient correction, supporting diagnosis |
| [14109019](https://pubmed.ncbi.nlm.nih.gov/14109019/) | 1964 | Case report | Arch Intern Med | Classic description of hereditary diaphorase deficiency and methemoglobinemia |
| [14248326](https://pubmed.ncbi.nlm.nih.gov/14248326/) | 1964 | Case report | Arch Fr Pediatr | Recessive congenital methemoglobinemia linked to diaphorase I deficiency |

### Methemoglobinemia, alpha type (Rank 2)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3537620](https://pubmed.ncbi.nlm.nih.gov/3537620/) | 1986 | Clinical review | Medical Toxicology | General review of drug/chemical-induced methemoglobinemia, including methylene blue as treatment; not subtype-specific |
| [26950891](https://pubmed.ncbi.nlm.nih.gov/26950891/) | 2016 | Basic science | J Photochem Photobiol B | Biophysical study of methylene blue–protein binding; notes methemoglobinemia among known MB toxicities, background pharmacology only |

### Bronchitis (Rank 1 — evidence assessed as not treatment-relevant)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9387672](https://pubmed.ncbi.nlm.nih.gov/9387672/) | 1996 | Diagnostic technique study | Zhonghua Wai Ke Za Zhi | Methylene blue used as a bronchoscopic stain to distinguish malignant tumors (97% stained) from bronchitis (8% stained) — diagnostic, not therapeutic |
| [7313968](https://pubmed.ncbi.nlm.nih.gov/7313968/) | 1981 | Diagnostic technique study | Terapevticheskii Arkhiv | Chromoendofibroscopy with methylene blue for differentiating benign/malignant GI and bronchial lesions — diagnostic use |
| [8420409](https://pubmed.ncbi.nlm.nih.gov/8420409/) | 1993 | Method/technique study | Am Rev Respir Dis | Methylene blue used as one of several tracer dyes to quantify intra-alveolar fluid in lavage — laboratory technique |
| [2749902](https://pubmed.ncbi.nlm.nih.gov/2749902/) | 1989 | Basic science | Tsitologiia | Methylene blue (chromosmon) used as a reagent in erythrocyte hemoglobin spectrophotometry — lab technique |
| [6121761](https://pubmed.ncbi.nlm.nih.gov/6121761/) | 1982 | Basic science (unrelated drug) | Int J Clin Pharmacol Ther Toxicol | Beta-blocker study; methylene blue used only as a circulation-time indicator dye |
| [31419501](https://pubmed.ncbi.nlm.nih.gov/31419501/) | 2020 | Basic science (unrelated compound) | J Ethnopharmacol | Plant essential oil (not methylene blue) with traditional bronchitis use |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Basic science (unrelated, biosensor) | Anal Chim Acta | Aptasensor for theophylline detection — unrelated to methylene blue treatment |
| [21767626](https://pubmed.ncbi.nlm.nih.gov/21767626/) | 2011 | Basic science (unrelated compound) | J Ethnopharmacol | Plant extract (not methylene blue) with antidepressant/neuroprotective effects |
| [20084922](https://pubmed.ncbi.nlm.nih.gov/20084922/) | 2009 | Case report (unrelated) | Mikrobiyol Bul | Moraxella catarrhalis endocarditis case; no methylene blue link |
| [17120034](https://pubmed.ncbi.nlm.nih.gov/17120034/) | 2007 | Case report (unrelated) | Eur J Pediatr | Tracheoesophageal fistula case; no methylene blue link |

---

## Saudi Arabia Market Information

Methylene blue is currently not marketed in Saudi Arabia (0 authorizations on file).

---

## Safety Considerations

Please refer to the package insert for safety information. A TFDA package-insert warnings/contraindications lookup (DG001) is flagged as a **Blocking** data gap — this must be resolved before any Stage-1 safety evaluation can proceed. Drug-drug interaction data was also not found (query status: not_found).

---

## Conclusion and Next Steps

### Methemoglobinemia due to methemoglobin reductase deficiency
**Decision: Proceed with Guardrails**

**Rationale:** The reductive mechanism directly matches this disease's pathophysiology, supported by human and veterinary case literature (L3). This is essentially standard-of-care use rather than a novel repurposing hypothesis.

**To proceed, the following is needed:**
- TFDA/local package insert with warnings and contraindications (DG001)
- Confirmation of G6PD-deficiency screening as a mandatory pre-treatment safeguard
- MOA documentation (DG002)

### Methemoglobinemia, alpha type
**Decision: Research Question**

**Rationale:** Mechanistic plausibility depends entirely on which "alpha type" subtype is meant (enzyme-deficiency vs. structural HbM variant), and the two available citations don't resolve this.

**To proceed, the following is needed:**
- Clarification of the exact disease subtype/ICD mapping behind "methemoglobinemia, alpha type"
- Subtype-specific clinical or case-series evidence

### Bronchitis
**Decision: Hold**

**Rationale:** No treatment-relevant mechanistic or clinical evidence exists; the high TxGNN score is not corroborated by any of the 10 retrieved publications and is assessed as a likely false positive.

**To proceed, the following is needed:**
- New, treatment-specific evidence (not currently expected to emerge from further literature mining of this signal)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

