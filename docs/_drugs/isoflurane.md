---
layout: default
title: Isoflurane
parent: 僅模型預測 (L5)
nav_order: 342
evidence_level: L5
indication_count: 7
---

# Isoflurane
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Isoflurane: From General Anesthesia to Multiple Predicted Indications

## One-Sentence Summary

Isoflurane is a volatile halogenated inhalational agent used internationally for induction and maintenance of general anesthesia; it is **not currently marketed in Saudi Arabia** and has no local approved indication on file. TxGNN ranks **Prinzmetal angina** as its top predicted new indication (score **99.67%**), but of the 7 candidate indications returned, only **migraine disorder** (13 publications) and **manic bipolar affective disorder** (3 publications) have any supporting literature — none have registered clinical trials, so the overall evidence base remains preclinical/case-level at best.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack — no Saudi Arabia license on file. Isoflurane is internationally classified as a general (inhalational) anesthetic agent. |
| Predicted New Indication (top rank) | Prinzmetal angina |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 (model prediction only — no trials, no literature) |
| Saudi Arabia Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

**All 7 TxGNN-predicted indications, ranked:**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|
| 1 | Prinzmetal angina | 99.67% | L5 | Hold |
| 2 | Tourette syndrome | 99.61% | L5 | Hold |
| 3 | Manic bipolar affective disorder | 99.57% | L4 | Research Question |
| 4 | Trichotillomania | 99.54% | L5 | Hold |
| 5 | Dysthymic disorder | 99.27% | L5 | Hold |
| 6 | Nephrogenic syndrome of inappropriate antidiuresis | 99.09% | L5 | Hold ⚠ (mechanistic direction likely reversed — see below) |
| 7 | Migraine disorder | 99.06% | L4 | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for isoflurane is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, isoflurane is a volatile halogenated general anesthetic; its established efficacy is in producing reversible loss of consciousness and analgesia via GABA-A potentiation and NMDA receptor antagonism. Mechanistically, two of the seven candidates have a plausible biological rationale:

- **Migraine disorder (rank 7):** Isoflurane and related inhalational anesthetics have been shown experimentally to inhibit cortical spreading depression (CSD), the pathophysiological correlate of migraine aura. A case report also describes successful use of general anesthesia (isoflurane) to terminate refractory status migrainosus. This supports a plausible but narrow use-case — acute, treatment-resistant status migrainosus under medical supervision — not chronic migraine prophylaxis, since inhalational general anesthesia is not a feasible maintenance route.
- **Manic bipolar affective disorder (rank 3):** Isoflurane can induce a burst-suppression EEG pattern, mechanistically analogous to the cortical "reset" effect proposed for electroconvulsive therapy (ECT) in refractory depression/mania, and it shares NMDA-antagonist pharmacology with ketamine (used off-label for rapid mood stabilization). Evidence is limited to a small non-randomized comparative case series and case reports, with no controlled trials.

The remaining five candidates (Prinzmetal angina, Tourette syndrome, trichotillomania, dysthymic disorder, and nephrogenic SIADH) have **no supporting literature or trials at all** and rest solely on the TxGNN model score. Of particular concern is **nephrogenic syndrome of inappropriate antidiuresis**: inhalational anesthetics, including isoflurane, are pharmacologically known to *promote* ADH release and SIADH-like physiology as an intraoperative side effect — meaning the model may be capturing an adverse-effect association rather than a therapeutic relationship. This candidate should not be advanced without independent mechanistic scrutiny.

A cross-cutting practical barrier applies to every candidate: isoflurane is administered only as an inhaled general anesthetic gas, which is incompatible with chronic outpatient management of any of these conditions (migraine prophylaxis, bipolar maintenance, Tourette's, trichotillomania, dysthymia). Route compatibility data was not resolved for any indication in this evidence pack (`route_compatibility.status: pending`), so this remains a documented gap rather than a settled conclusion.

---

## Clinical Trial Evidence

Currently no related clinical trials registered — this applies to **all 7** predicted indications, including migraine disorder and manic bipolar affective disorder. No ClinicalTrials.gov or ICTRP records were found for isoflurane against any of the candidate indications as of the 2026-08-13 data cutoff.

---

## Literature Evidence

### Migraine disorder (rank 7) — 13 publications identified, top 10 most relevant shown

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26323741](https://pubmed.ncbi.nlm.nih.gov/26323741/) | 2015 | Case report | Braz J Anesthesiol | General anesthesia (propofol/isoflurane, acting on sub-GABA-A receptors) used to terminate refractory status migrainosus. |
| [8665587](https://pubmed.ncbi.nlm.nih.gov/8665587/) | 1996 | Preclinical | Cephalalgia | Inhalational anesthetics (incl. isoflurane-class agents) inhibit cortical spreading depression, the proposed substrate of migraine aura. |
| [27122032](https://pubmed.ncbi.nlm.nih.gov/27122032/) | 2016 | Preclinical/Review | J Neuroscience | Maps cortical regions susceptible to spreading depolarization, relevant to migraine aura pathophysiology. |
| [17267580](https://pubmed.ncbi.nlm.nih.gov/17267580/) | 2007 | Preclinical | J Pharmacol Exp Ther | NMDA receptor antagonists (isoflurane shares this pharmacology) suppress cortical spreading depression in rats. |
| [40764901](https://pubmed.ncbi.nlm.nih.gov/40764901/) | 2025 | Preclinical (pending classification) | J Headache Pain | Tests whether CGRP antagonist atogepant's migraine efficacy is mediated via CSD suppression — establishes CSD as a druggable migraine target. |
| [22523186](https://pubmed.ncbi.nlm.nih.gov/22523186/) | 2012 | Preclinical | Cephalalgia | Chronic topiramate suppresses potassium-induced cortical spreading depression in rats. |
| [24256609](https://pubmed.ncbi.nlm.nih.gov/24256609/) | 2013 | Preclinical | J Headache Pain | CGRP receptor antagonist reduces spinal trigeminal activity during nitroglycerin-induced migraine model. |
| [24004534](https://pubmed.ncbi.nlm.nih.gov/24004534/) | 2013 | Preclinical (pending classification) | J Headache Pain | Changes in CGRP/nitric oxide receptor expression in trigeminal ganglion after migraine-model pretreatment. |
| [20974582](https://pubmed.ncbi.nlm.nih.gov/20974582/) | 2011 | Preclinical (pending classification) | Cephalalgia | NO donor infusion increases CGRP/nNOS-positive neurons in trigeminal ganglion, a migraine-relevant pathway. |
| [27091721](https://pubmed.ncbi.nlm.nih.gov/27091721/) | 2016 | Basic science | Annals of Neurology | Identifies extracranial (periosteal) inflammatory gene upregulation in chronic migraine patients. |

### Manic bipolar affective disorder (rank 3) — 3 publications identified

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8462536](https://pubmed.ncbi.nlm.nih.gov/8462536/) | 1993 | Comparative case series (non-randomized) | Eur J Anaesthesiol | Burst-suppression isoflurane anesthesia compared intra-individually with ECT in 12 severely depressed patients; both produced marked improvement. |
| [7502646](https://pubmed.ncbi.nlm.nih.gov/7502646/) | 1995 | Case report | AANA Journal | Case of a patient with manic-depressive psychosis receiving isoflurane anesthesia; reports a malignant hyperthermia differential diagnosis, not a treatment outcome for the psychiatric condition. |
| [18930636](https://pubmed.ncbi.nlm.nih.gov/18930636/) | 2008 | Preclinical (animal PET imaging) | Psychiatry Research | Isoflurane used only as anesthesia for PET imaging in an ouabain-induced rat mania model; not evidence of isoflurane's own therapeutic effect. |

### All other candidates (Prinzmetal angina, Tourette syndrome, trichotillomania, dysthymic disorder, nephrogenic SIADH)

Currently no related literature available.

---

## Saudi Arabia Market Information

Isoflurane holds **no marketing authorization in Saudi Arabia** — 0 licenses on record, no product names or approved indication text available.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data were not available in this evidence pack; retrieval of the TFDA/local package insert is flagged as a **Blocking** data gap that must be resolved before any safety (S1) assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No predicted indication for isoflurane is supported by any registered clinical trial. The two candidates with any literature support — migraine disorder and manic bipolar affective disorder — rest on case reports, small non-randomized case series, and preclinical/animal studies (Evidence Level L4), which is insufficient to progress beyond a research hypothesis. The top-ranked candidate by TxGNN score, Prinzmetal angina, along with Tourette syndrome, trichotillomania, and dysthymic disorder, have zero literature or trial support (L5). The nephrogenic SIADH candidate raises a direction-of-causality concern (isoflurane is a known SIADH-promoting agent, not an established treatment) and should not be advanced as-is.

**To proceed, the following is needed:**
- TFDA/local package insert (warnings, contraindications, DDI) — currently a Blocking gap for any safety assessment
- Formal mechanism-of-action documentation from DrugBank or equivalent source
- Route-of-administration feasibility analysis — isoflurane is inhalational-only, which is incompatible with chronic maintenance therapy for any of the 5 non-acute candidates
- Independent mechanistic review of the nephrogenic SIADH candidate to rule out a spurious adverse-effect association
- If pursuing migraine or bipolar mania as research questions: targeted literature search for controlled trials and expert consultation on whether a feasible clinical protocol (e.g., acute status migrainosus rescue) could even be designed around inhalational administration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

