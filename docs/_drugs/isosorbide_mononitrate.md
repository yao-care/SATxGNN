---
layout: default
title: Isosorbide Mononitrate
parent: 僅模型預測 (L5)
nav_order: 346
evidence_level: L5
indication_count: 10
---

# Isosorbide Mononitrate
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

# Isosorbide Mononitrate: From Nitrate Vasodilator (Original Indication Not on File) to Pulmonary Arterial Hypertension

*Note: This Evidence Pack contains 10 TxGNN-predicted indications for ISMN. Nine of the ten (hypertrichosis, alopecia, congenital hair/craniofacial syndromes, etc.) have zero clinical trials, zero literature, and are explicitly flagged in the pack's own rationale as speculative or spurious knowledge-graph associations. This report focuses on the one candidate with an actual mechanistic and literature basis — **Pulmonary Arterial Hypertension (PAH)**, rank 10 by TxGNN score but the only candidate reaching decision stage S1.*

---

## One-Sentence Summary

Isosorbide Mononitrate (ISMN) is a long-acting organic nitrate / nitric oxide (NO) donor; its original approved indication is not documented in this evidence pack, and the drug is not currently marketed locally.
The TxGNN model predicts potential relevance to **Pulmonary Arterial Hypertension**, supported by **0 clinical trials** and **6 publications**, of which only one directly modeled a pulmonary hypertension disease state (an animal model), and none tested ISMN itself as monotherapy in PAH patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no approved indication text on file; drug not marketed locally) |
| Predicted New Indication | Pulmonary Arterial Hypertension |
| TxGNN Prediction Score | 99.94% (rank 1464 among all predictions) |
| Evidence Level | L4 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ISMN is not available in DrugBank per this evidence pack (`original_moa: [Data Gap]`). Based on the literature captured in this pack, ISMN is a long-acting organic nitrate that undergoes non-enzymatic metabolism to release nitric oxide (NO). NO activates soluble guanylate cyclase (sGC), raising intracellular cGMP and producing vascular smooth muscle relaxation.

This NO–sGC–cGMP axis is a clinically validated therapeutic target in PAH — sGC *stimulator* drugs (e.g., riociguat) are an approved PAH drug class that acts on the same pathway ISMN engages as an NO donor. This provides a plausible, if indirect, mechanistic rationale for the TxGNN association.

However, the mechanistic overlap does not equate to interchangeable pharmacology. ISMN itself is a conventional nitrate, not a targeted sGC stimulator, and is subject to well-known nitrate tolerance with chronic dosing. Of the 6 literature items retrieved, only one (PMID 29705351, a monocrotaline-induced pulmonary hypertension rat model) examined the NO–sGC pathway in a pulmonary hypertension context — and even that study centered on sGC stimulation broadly, not ISMN specifically. One additional paper (PMID 29377691) tested a synthetic NO-donor/bardoxolone methyl hybrid molecule derived from ISMN, not ISMN itself, in a PAH rat model. The remaining four papers concern ISMN pharmacology in unrelated contexts (portal hypertension in cirrhosis, coronary artery disease/erectile dysfunction, general vasodilator pharmacokinetics) and do not test ISMN in PAH patients or models.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29705351](https://pubmed.ncbi.nlm.nih.gov/29705351/) | 2018 | Preclinical (animal model) | Life Sciences | NO-sensitive soluble guanylate cyclase (sGC) activity examined in monocrotaline-induced pulmonary hypertensive rats; supports NO-enhancing drugs' relevance to PH progression |
| [29377691](https://pubmed.ncbi.nlm.nih.gov/29377691/) | 2018 | Medicinal chemistry / synthesis | Journal of Medicinal Chemistry | A synthesized NO-donor hybrid derived from ISMN + bardoxolone methyl lowered mean pulmonary artery pressure and RV systolic pressure in PAH rats (tests a novel hybrid molecule, not ISMN alone) |
| [3384359](https://pubmed.ncbi.nlm.nih.gov/3384359/) | 1988 | Mechanism study | Gut | ISMN decreased portal venous pressure in cirrhotic patients with portal hypertension (non-PAH population) |
| [9673832](https://pubmed.ncbi.nlm.nih.gov/9673832/) | 1998 | Review | Clinical Pharmacokinetics | General pharmacokinetic review of vasodilator drug classes, including nitrates |
| [16422873](https://pubmed.ncbi.nlm.nih.gov/16422873/) | 2005 | Cohort (non-PAH population) | Journal of Sexual Medicine | Hemodynamic effects of sildenafil (PDE5 inhibitor) combined with ISMN in men with coronary artery disease and erectile dysfunction |
| [2759546](https://pubmed.ncbi.nlm.nih.gov/2759546/) | 1989 | Cohort (cirrhosis, non-PAH) | Hepatology | ISMN showed no significant effect on hepatic hemodynamics in HBsAg-positive cirrhosis patients |

---

## Saudi Arabia Market Information

The drug is currently not marketed and has no registered authorizations in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Additional note from the evidence pack's own repurposing rationale (not from the safety database): ISMN is subject to nitrate tolerance with chronic use, and co-administration with PDE5 inhibitors — a standard component of contemporary PAH therapy — is a recognized contraindication due to risk of severe hypotension. This is a material constraint on any PAH development pathway and should be formally verified against the package insert once available.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The NO–sGC–cGMP mechanistic link to PAH is biologically plausible and consistent with an approved drug class in PAH (sGC stimulators), but no study in this pack tested ISMN itself in PAH patients or PAH animal models — the only PAH-model data involves a synthetic hybrid molecule, not ISMN. Evidence level is L4 (mechanism/preclinical only), and there is a known, clinically significant drug interaction (PDE5 inhibitors, standard PAH therapy) that constrains feasibility.

**To proceed, the following is needed:**
- Preclinical testing of ISMN itself (not a synthetic hybrid) in validated PAH animal models
- Formal DDI and contraindication data (TFDA/package insert) confirming PDE5 inhibitor interaction risk and nitrate tolerance profile
- Confirmation of the drug's original approved indication and MOA (currently a data gap) to assess regulatory pathway to a new indication
- If preclinical signal holds, an early-phase mechanistic/PK study in PAH patients before any Go decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

