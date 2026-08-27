---
layout: default
title: Eletriptan
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 4
---

# Eletriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the provided report template (no additional skill applies — this is a direct content-generation task against an explicit user-supplied format) to produce the evaluation report.

I reviewed the Evidence Pack. Key points that shape the report:
- `original_indications` and Saudi `licenses` are empty (drug not marketed in Saudi Arabia), so the "original indication" has to be stated from established pharmacology (eletriptan = triptan for acute migraine), not from a license record.
- The #1 predicted indication, "migraine with brainstem aura," is a subtype where triptans are a classic **relative contraindication** (vasoconstriction risk in vertebrobasilar circulation) — the evidence pack's own `repurposing_rationale` flags this, not as a positive new-use hypothesis. I represent that honestly rather than dressing it up as a therapeutic opportunity.
- Ranks 2–4 (atrophoderma vermiculata, ulerythema ophryogenesis, sciatic neuropathy) have zero trials/literature (S0/L5) and are flagged in the source data itself as likely embedding artifacts — I note this briefly rather than building out empty sections for them.

Here is the report:

---

# Eletriptan: From Acute Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

> Eletriptan is a selective 5-HT1B/1D receptor agonist (triptan) established for the acute treatment of migraine attacks.
> The TxGNN model assigns its highest new-indication score to **migraine with brainstem aura**,
> but this "prediction" is better read as a **safety flag than a therapeutic opportunity** — no clinical trials and only general triptan/migraine literature (18 publications) exist, and triptans are conventionally considered a **relative contraindication** in this specific migraine subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute treatment of migraine (with or without aura) — established pharmacological use; no Saudi Arabia license record exists to cite an official indication text |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Eletriptan is a selective 5-HT1B/1D receptor agonist. Its classic mechanism is to induce vasoconstriction of intracranial (including meningeal) arteries and to inhibit release of inflammatory neuropeptides from the trigeminovascular system — a mechanism well established for typical migraine, with or without classic aura (PMID 12498013, 24065716).

However, "migraine with brainstem aura" (formerly called basilar-type migraine) is treated differently. In IHS/ICHD-3 classification and in most national drug labels, this subtype is listed as a **relative contraindication for triptans**, because the same vasoconstrictive mechanism that relieves typical migraine is theorized to worsen ischemic risk in the vertebrobasilar circulation. In other words, the biological "link" TxGNN found here is real at the receptor-pharmacology level, but it points toward a **risk signal, not a positive efficacy hypothesis** — this is fundamentally different from an ordinary repurposing candidate where mechanistic overlap supports a new benefit.

One directly relevant RCT (PMID 15469451) tested eletriptan 80 mg administered during the aura phase itself and found no benefit — consistent with the conventional caution around treating aura-phase/brainstem-aura presentations with triptans. A separate case report (PMID 25155004) describes a myocardial infarction temporally associated with eletriptan use, reinforcing that vasoconstrictive class effects warrant caution in patients with vascular risk factors, which is conceptually related to (though not identical to) the brainstem-aura concern.

For context, the other three TxGNN-predicted indications in this pack (atrophoderma vermiculata, ulerythema ophryogenesis, sciatic neuropathy) have zero supporting trials or literature (evidence level L5, decision stage S0) and no plausible mechanistic link to 5-HT1B/1D agonism; per the evidence pack's own annotations, these are most likely embedding-proximity artifacts of the knowledge graph rather than genuine hypotheses, and are not carried forward in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15469451](https://pubmed.ncbi.nlm.nih.gov/15469451/) | 2004 | RCT | European Journal of Neurology | Eletriptan 80 mg given during the aura phase showed no benefit — directly tests early/aura-phase dosing relevant to the brainstem-aura question |
| [12807526](https://pubmed.ncbi.nlm.nih.gov/12807526/) | 2003 | RCT | Cephalalgia | Eletriptan 40 mg effective and tolerable in patients with prior poor response/tolerance to sumatriptan, in patients with and without aura (n=446) |
| [11844898](https://pubmed.ncbi.nlm.nih.gov/11844898/) | 2002 | RCT | European Neurology | Eletriptan 40/80 mg superior to placebo and comparable/better than Cafergot for acute migraine |
| [17501848](https://pubmed.ncbi.nlm.nih.gov/17501848/) | 2007 | RCT (functional/subanalysis) | Headache | Eletriptan improved work productivity and functional impairment scores during acute migraine attacks |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review/Guideline | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies, including triptans |
| [12498013](https://pubmed.ncbi.nlm.nih.gov/12498013/) | 2002 | Review (drug profile) | Current Opinion in Investigational Drugs | Describes eletriptan's 5-HT1B/1D receptor binding profile (6-fold greater affinity for 5-HT1D than sumatriptan) |
| [11687056](https://pubmed.ncbi.nlm.nih.gov/11687056/) | 2001 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Systematic review of eletriptan efficacy/harm for acute migraine |
| [17636718](https://pubmed.ncbi.nlm.nih.gov/17636718/) | 2007 | Review (Cochrane, withdrawn) | Cochrane Database of Systematic Reviews | Updated Cochrane review of eletriptan for acute migraine (later withdrawn) |
| [24065716](https://pubmed.ncbi.nlm.nih.gov/24065716/) | 2014 | Review (mechanism) | Cephalalgia | Discusses serotonin's role in migraine pathophysiology, underlying the 5-HT1B/1D mechanistic rationale |
| [25155004](https://pubmed.ncbi.nlm.nih.gov/25155004/) | 2014 | Case report | Revista Portuguesa de Cardiologia | Myocardial infarction temporally associated with eletriptan use — vasoconstrictive class safety signal |

**Note:** none of the 18 identified publications directly study "migraine with brainstem aura" (basilar-type migraine) as a treated population; the list above reflects the closest available evidence (general triptan/eletriptan efficacy and mechanism) plus the two records most relevant to the aura/vascular-safety question.

---

## Saudi Arabia Market Information

Eletriptan currently has no product authorization on record in Saudi Arabia (market status: Not Marketed, 0 authorizations).

---

## Safety Considerations

Please refer to the package insert for safety information.

**Additional note from the evidence pack's mechanistic analysis (not from a formal safety/DDI query, which returned no data):** migraine with brainstem aura (basilar-type migraine) is conventionally regarded as a relative contraindication for triptans, including eletriptan, due to theoretical vasoconstriction risk in the vertebrobasilar circulation. This should be treated as a critical prescribing caution rather than a supporting rationale for the predicted indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction is mechanistically explainable (5-HT1B/1D agonism) but represents a known relative contraindication rather than a validated therapeutic opportunity; no clinical trials exist for this specific indication, and the one directly relevant RCT found no benefit from aura-phase dosing.
- The remaining three TxGNN predictions in this pack have no clinical trial or literature support (L5/S0) and are not being pursued further.

**To proceed, the following is needed:**
- Official Saudi/manufacturer package insert warnings and contraindications (currently a blocking data gap — required before any S1 safety screening)
- Confirmed DrugBank mechanism-of-action record (currently a data gap; the MOA used above was reconstructed from literature, not from a verified DrugBank field)
- If this indication is to be reconsidered, a formal risk-benefit assessment specific to vertebrobasilar/brainstem-aura vasoconstriction risk, ideally with cardiology/neurology input, rather than reliance on general migraine efficacy data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

