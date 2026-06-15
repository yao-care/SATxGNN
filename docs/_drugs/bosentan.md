---
layout: default
title: Bosentan
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 9
---

# Bosentan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Bosentan: From Pulmonary Arterial Hypertension to Rheumatoid Arthritis

## One-Sentence Summary

Bosentan is a dual endothelin receptor antagonist (ERA) established for the treatment of pulmonary arterial hypertension (PAH) and systemic sclerosis-related digital ulcers.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, supported by **1 Phase 2 clinical trial** (targeting the related vasculitic condition giant cell arteritis, not yet recruiting) and **16 publications** — predominantly animal studies directly demonstrating anti-arthritic effects and mechanistic reviews linking the endothelin pathway to RA pathophysiology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary Arterial Hypertension (PAH) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from the regulatory source is not currently available for this report. Based on known pharmacology, Bosentan is a dual ETA/ETB endothelin receptor antagonist — it competitively blocks the binding of endothelin-1 (ET-1) at both receptor subtypes, reducing ET-1-driven vasoconstriction and fibrotic signalling. ET-1 plasma and synovial fluid levels are significantly elevated in rheumatoid arthritis patients, and ET-1 is known to promote synovial angiogenesis, fibroblast activation, and joint inflammation through downstream cytokine cascades involving TNF-α, IL-17, and IL-15.

Crucially, two independent animal models provide direct mechanistic support. In collagen-induced arthritis (CIA mice), Bosentan treatment significantly ameliorated joint inflammation and suppressed TNF-α expression — the same cytokine that drives RA progression in humans. In zymosan-induced arthritis, ET-1 blockade reduced neutrophil accumulation, oedema, and articular hypernociception mediated through LTB4 and CXCL-1. A third study demonstrated that IL-15, closely associated with clinical RA, triggers joint pain via a sequential ET-1-dependent pathway that is suppressible by dual ERA treatment.

While the mechanistic rationale is coherent and biologically plausible, the evidence gap between animal models and human RA clinical trials remains wide. Unlike Bosentan's established use in PAH and limited systemic sclerosis — where Phase 3 RCTs confirm efficacy — no dedicated human RA trials have been conducted. The single retrieved clinical trial targets giant cell arteritis (a large-vessel vasculitis) rather than RA specifically, offering only indirect translational value.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT06957002](https://clinicaltrials.gov/study/NCT06957002) | Phase 2 | Not Yet Recruiting | 40 | Bosentan + glucocorticoids vs glucocorticoids alone in giant cell arteritis (GCA); primary endpoint: failure-free survival at 12 months. Target completion: September 2029. **Note:** GCA is a large-vessel vasculitis distinct from RA — this trial provides mechanistic proof-of-concept for ERA anti-inflammatory activity in autoimmune vasculopathy but does not constitute direct RA evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22249931](https://pubmed.ncbi.nlm.nih.gov/22249931/) | 2012 | Animal Study | *Inflammation Research* | Bosentan directly ameliorates collagen-induced arthritis (CIA) in mice; TNF-α upregulates endothelin system genes, and dual ETA/ETB blockade reduces joint inflammation — strongest direct evidence supporting repurposing hypothesis |
| [18515326](https://pubmed.ncbi.nlm.nih.gov/18515326/) | 2008 | Animal Study | *J Leukocyte Biology* | ET-1 levels elevated in RA synovial membrane; ETA/ETB receptor blockade reduces neutrophil accumulation, oedema, and LTB4/TNF-α/CXCL-1 in zymosan-induced arthritis model |
| [16766656](https://pubmed.ncbi.nlm.nih.gov/16766656/) | 2006 | Animal Study | *PNAS* | IL-15 (closely linked to clinical RA) triggers articular hypernociception via a sequential IFN-γ → ET-1 → prostaglandin pathway; dual ERA treatment inhibits this pain cascade |
| [19969421](https://pubmed.ncbi.nlm.nih.gov/19969421/) | 2010 | Animal Study | *Pain* | IL-17 mediates articular hypernociception in antigen-induced arthritis; establishes cytokine-endothelin crosstalk relevant to Bosentan's potential analgesic-anti-inflammatory mechanism in RA |
| [20054770](https://pubmed.ncbi.nlm.nih.gov/20054770/) | 2009 | Case Report | *Kardiologia Polska* | Bosentan used for Eisenmenger syndrome in a child concurrently diagnosed with juvenile rheumatoid arthritis; case notable for co-management feasibility, no adverse interaction reported |
| [19851110](https://pubmed.ncbi.nlm.nih.gov/19851110/) | 2010 | Review | *Curr Opin Rheumatology* | Comprehensive review of rheumatic skin and systemic disease; contextualises overlapping vasculopathic and inflammatory pathways across connective tissue diseases |
| [19487226](https://pubmed.ncbi.nlm.nih.gov/19487226/) | 2009 | Review | *Rheumatology (Oxford)* | Reviews vascular disease and PAH in SLE and Sjögren's syndrome; highlights ET-1's central role in CTD vasculopathy, providing mechanistic context for ERA use across rheumatic diseases |
| [24268012](https://pubmed.ncbi.nlm.nih.gov/24268012/) | 2014 | Review | *Rheum Dis Clin N Am* | PAH associated with connective tissue diseases; notes RA among affected CTDs, underscoring shared ET-1-driven vascular pathology |
| [16218473](https://pubmed.ncbi.nlm.nih.gov/16218473/) | 2005 | Review | *Lupus* | ET-1-driven PAH documented across multiple CTDs including RA; supports biological plausibility of ERA intervention in RA vasculopathy |
| [18238768](https://pubmed.ncbi.nlm.nih.gov/18238768/) | 2008 | Review | *Am J Health-Syst Pharm* | Reviews ERA therapy options for systemic sclerosis complications; contextualises Bosentan's anti-fibrotic and anti-vasoconstrictive pharmacology relevant to inflammatory arthropathy |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data were available in the current evidence pack. Clinicians should note that Bosentan is a known inducer of CYP3A4 and CYP2C9 enzymes, carries a hepatotoxicity risk (monthly LFT monitoring required), and is teratogenic (Category X in pregnancy). These class effects of endothelin receptor antagonists are well established in the PAH literature and must be factored into any repurposing protocol.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for Bosentan in rheumatoid arthritis is scientifically credible — ET-1 is elevated in RA synovial tissue, animal models directly confirm anti-arthritic efficacy, and the endothelin–TNF-α–IL-17 axis is biologically plausible — but the evidence base remains entirely preclinical. No human RA clinical trial has been conducted, and the single retrieved trial targets a related but distinct vasculitic condition. Evidence Level L3 is insufficient to proceed to clinical application without dedicated prospective human studies.

**To proceed, the following is needed:**

- **Proof-of-concept human pilot study**: A small Phase 1/2 open-label study in biologic-naïve or refractory RA patients assessing synovial ET-1 modulation and clinical endpoints (DAS28, HAQ)
- **MOA documentation**: Formal retrieval of Bosentan's complete pharmacological profile from DrugBank to confirm receptor selectivity and downstream pathway interactions relevant to RA
- **Safety monitoring plan**: Establish LFT monitoring protocol (baseline + monthly), CYP interaction screening (particularly with MTX, which is a RA cornerstone therapy), and pregnancy prevention programme prior to any clinical use
- **Regulatory pathway clarification**: Bosentan is not marketed in Saudi Arabia; import or compassionate use pathway would need to be established before any investigator-initiated trial
- **Biomarker strategy**: Identify patient subgroups most likely to respond (e.g., RA patients with elevated serum ET-1, concurrent Raynaud's phenomenon, or vasculopathic features) to enrich trial population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

