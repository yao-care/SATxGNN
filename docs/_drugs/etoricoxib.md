---
layout: default
title: Etoricoxib
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
---

# Etoricoxib
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

# Etoricoxib: From COX-2-Mediated Pain/Inflammatory Conditions to Migraine Disorder

## One-Sentence Summary

Etoricoxib (DrugBank DB01628) is a selective COX-2 inhibitor; its formal original-indication and mechanism-of-action records are not available in this Evidence Pack (flagged as data gaps DG001/DG002), though the attached clinical-trial evidence context (ankylosing spondylitis, post-orthopedic pain, cervical osteoarthritis) is consistent with its known use as an anti-inflammatory/analgesic NSAID. The TxGNN model's top prediction is **Migraine Disorder**, but this is a **pure computational signal with zero supporting clinical trials or literature** — the repurposing rationale explicitly states "純屬TxGNN預測" (prediction only, no clinical/preclinical evidence).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack (data gap — see DG002); trial context suggests inflammatory/musculoskeletal pain use |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only, no studies) |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity). Based on the mechanistic rationale attached to this prediction: COX-2 and the prostaglandin pathway are known to participate in trigeminovascular system activation, which is part of migraine pathophysiology in general. However, the Evidence Pack itself states there is **no clinical or preclinical evidence** of etoricoxib being studied in migraine — this connection is derived purely from TxGNN's learned embedding space, not from any observed drug-disease association.

It is worth noting that within the same Evidence Pack, two related but distinct entities — **Headache Disorder** (rank 9) and **Trigeminal Autonomic Cephalalgia** (rank 10) — carry stronger, literature-sourced rationale: several case reports/case series describe etoricoxib and celecoxib as effective in indomethacin-responsive headache syndromes (primary stabbing headache, cough headache), which share a COX-pathway mechanism with indomethacin. This offers indirect biological plausibility for COX-2 inhibition in *some* headache subtypes, but it does not directly validate the rank-1 "Migraine Disorder" prediction, which remains an unsupported model output.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Saudi Arabia Market Information

Etoricoxib is **not currently marketed** in Saudi Arabia — 0 authorizations are on file in this Evidence Pack, and no license/product records exist to summarize.

---

## Safety Considerations

Formal key warnings, contraindications, and DDI data are not available in this Evidence Pack (all fields marked as data gaps; DDI query returned "not_found"). This is flagged as **Blocking (DG001)** — TFDA/SFDA package insert warnings and contraindications must be obtained before this candidate can enter safety pre-screening (S1).

**Additional safety signals surfaced incidentally in the literature (attached to other predicted-indication evidence blocks, not migraine):**
- Case report of etoricoxib-induced life-threatening hyperkalemia and acute kidney dysfunction in a patient on telmisartan + low-sodium diet (PMID 21373319).
- Case report of reversible cerebral vasoconstriction syndrome possibly induced by etoricoxib (PMID 25229174).

These are not migraine-specific but are relevant background risk signals (renal/electrolyte and cerebrovascular) given the drug's cardiovascular/renal safety profile as a COX-2 inhibitor.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Migraine Disorder) has an Evidence Level of L5 — a model score only, with zero clinical trials or publications — and the drug is not marketed in Saudi Arabia. A Blocking data gap (missing TFDA/SFDA label warnings and contraindications) also prevents progression to safety pre-screening.

**To proceed, the following is needed:**
- TFDA/SFDA official package insert (warnings, contraindications) — resolves DG001 (Blocking)
- Formal MOA data via DrugBank API — resolves DG002 (High)
- Any preclinical or clinical data specifically on etoricoxib in migraine (currently none exist)
- If pursuing the COX-2/headache mechanism further, consider redirecting research priority toward **Headache Disorder** and **Trigeminal Autonomic Cephalalgia** (both L4, "Research Question" stage), which have case-report-level human evidence, rather than classic Migraine Disorder
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

