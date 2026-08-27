---
layout: default
title: Nizatidine
parent: 僅模型預測 (L5)
nav_order: 448
evidence_level: L5
indication_count: 7
---

# Nizatidine
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

Using the Evidence Pack provided, here is the evaluation report. Note: I flag one important data quality issue up front — TxGNN's **rank-1 prediction ("active peptic ulcer disease") is not actually a novel indication**; the evidence pack's own rationale text confirms this is Nizatidine's known, already-approved H2-receptor-antagonist use. I've followed the template's extraction rules for rank 1 (as instructed) but flagged this clearly wherever it affects interpretation, and pulled out the one genuinely novel candidate with real (if limited) evidence — gastroduodenitis — so the decision section isn't misleading.

---

# Nizatidine: From Established Peptic Ulcer Therapy to Emerging Gastroduodenal Protection

## One-Sentence Summary

> Nizatidine is a histamine H2-receptor antagonist with an established, well-documented role in treating peptic ulcer disease and related acid-related gastrointestinal disorders. The TxGNN model's top-ranked prediction — **active peptic ulcer disease** (score **99.96%**) — is backed by strong Phase 3 RCT evidence, but this is Nizatidine's *own known, already-approved use*, not a novel repurposing target. Among the six other candidates screened, only **gastroduodenitis** (NSAID-induced gastroduodenal mucosal protection) shows genuine, though limited (**L3**), supporting clinical evidence; the remaining candidates lack direct clinical or literature support.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Peptic ulcer disease / acid-related GI disorders (H2-receptor antagonist class use — no formal Saudi Arabia label text on file) |
| Predicted New Indication (Rank 1) | Active Peptic Ulcer Disease *(⚠️ this is Nizatidine's existing approved use, not a novel candidate — see note below)* |
| TxGNN Prediction Score (Rank 1) | 99.96% |
| Evidence Level (Rank 1) | L1 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** (for the repurposing pipeline as a whole — see Conclusion) |

> **Important Note:** Rank 1 ("active peptic ulcer disease") scores highest because it is the drug's known, on-label mechanism — the model is correctly re-identifying existing pharmacology rather than surfacing a new use. It is presented here per the standard extraction rule, but should not be counted as a repurposing opportunity. The most credible *genuine* candidate in this evidence pack is **Rank 6 — gastroduodenitis** (Evidence Level L3, decision stage S2, "Research Question"), discussed further below.

---

## Why is This Prediction Reasonable?

**Mechanism of action.** A formal structured MOA record (DrugBank field) is not yet on file for this drug (data gap **DG002**, High severity). However, the mechanistic rationale embedded in this evidence pack confirms the well-established pharmacology of H2-receptor antagonists: Nizatidine directly inhibits histamine-stimulated gastric acid secretion at the gastric parietal cell H2 receptor. This is the same mechanism that underlies its original, approved use in peptic ulcer disease — which is exactly why Rank 1 scores so highly; it is a re-statement of known pharmacology rather than an extrapolation.

**Relationship between original and predicted use.** Because Rank 1 duplicates the known indication, the more meaningful repurposing question is whether acid suppression generalizes to *adjacent* gastroduodenal pathology. Evidence quality drops sharply once we move away from classic gastric/duodenal ulcer: peptic ulcer perforation and duodenal obstruction are mechanical/surgical problems that acid suppression cannot resolve (no supporting literature at all, L5, judged as prediction noise by the pack's own rationale); duodenogastric reflux is driven by bile/pancreatic (alkaline) reflux rather than acid excess, so the mechanistic fit is weak; and multiple endocrine neoplasia is a genetic tumour syndrome where H2RA relevance is confined to a rare MEN1/Zollinger-Ellison subset, with no direct evidence.

**Why gastroduodenitis stands out.** The one candidate with a defensible mechanistic and evidentiary basis is **gastroduodenitis**, specifically NSAID-induced gastroduodenal mucosal injury. Acid suppression has a direct, well-understood protective role in NSAID-associated mucosal damage, and two small prospective/cohort studies (PMID 7863248, PMID 1969684) demonstrate that nizatidine reduces NSAID/piroxicam-induced gastroduodenal lesions. This is Phase 1–2-grade evidence (L3), not confirmatory, but it is a real, mechanistically coherent signal — unlike the other five candidates.

---

## Clinical Trial Evidence (Rank 1: Active Peptic Ulcer Disease)

Currently no related clinical trials registered.

---

## Literature Evidence (Rank 1: Active Peptic Ulcer Disease)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [1526089](https://pubmed.ncbi.nlm.nih.gov/1526089/) | 1992 | RCT | Clin Pharmacol Ther | 8-week multicenter RCT: nizatidine 150 mg BID or 300 mg qHS vs. placebo in active benign gastric ulcer — evaluated healing and symptom relief |
| [2570656](https://pubmed.ncbi.nlm.nih.gov/2570656/) | 1989 | RCT | Clin Pharmacol Ther | Two-phase placebo-controlled RCT: nizatidine 150 mg BID for duodenal ulcer healing over 4–8 weeks |
| [2892259](https://pubmed.ncbi.nlm.nih.gov/2892259/) | 1987 | RCT | Scand J Gastroenterol Suppl | 1-year maintenance RCT (n=513) in healed duodenal ulcer: nizatidine 150 mg qHS cut recurrence to 34% vs. 64% with placebo at 12 months |
| [9198292](https://pubmed.ncbi.nlm.nih.gov/9198292/) | 1997 | RCT | Zhonghua Yi Xue Za Zhi | Clarithromycin-based combination therapy for H. pylori eradication in peptic ulcer disease (Chinese cohort) |
| [1982108](https://pubmed.ncbi.nlm.nih.gov/1982108/) | 1990 | RCT | Hepatogastroenterology | 8-week multicenter RCT: nizatidine (150 mg BID or 300 mg qHS) vs. ranitidine 150 mg BID in gastric ulcer healing |
| [7960687](https://pubmed.ncbi.nlm.nih.gov/7960687/) | 1994 | Cohort | Isr J Med Sci | Double-blind trial (n=55): nizatidine 300 mg qHS vs. placebo on duodenal ulcer healing and mucosal inflammatory mediators |
| [1974318](https://pubmed.ncbi.nlm.nih.gov/1974318/) | 1990 | Cohort | Medicina (Firenze) | Effects of nizatidine vs. misoprostol on gastric pH, pepsin, and mucus parameters in 20 duodenal ulcer patients |
| [2905640](https://pubmed.ncbi.nlm.nih.gov/2905640/) | 1988 | Review | Drugs | Preliminary pharmacodynamic/pharmacokinetic review of nizatidine's therapeutic use in peptic ulcer disease |
| [2184124](https://pubmed.ncbi.nlm.nih.gov/2184124/) | 1990 | Review | Gastroenterol Clin North Am | Overview of medical therapy for peptic ulcer disease, covering H2RAs including nizatidine |
| [8097411](https://pubmed.ncbi.nlm.nih.gov/8097411/) | 1993 | Review | Bailliere's Clin Gastroenterol | Pharmacology of gastric acid inhibition (neural/hormonal/paracrine regulation) |

### Supplementary Evidence — Genuine Repurposing Candidate: Gastroduodenitis (Rank 6, L3)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [7863248](https://pubmed.ncbi.nlm.nih.gov/7863248/) | 1994 | Cohort | Scand J Gastroenterol Suppl | RCT (n=269) in rheumatic patients on NSAIDs: nizatidine (150–600 mg/day) in therapy/prevention of NSAID-induced gastroduodenal ulcer |
| [1969684](https://pubmed.ncbi.nlm.nih.gov/1969684/) | 1990 | Cohort | Z Gastroenterol | Single-blind crossover study (n=12): nizatidine prevented piroxicam-induced gastric mucosal lesions vs. placebo |

---

## Saudi Arabia Market Information

Nizatidine is currently **not marketed in Saudi Arabia** — no market authorization records are on file (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(No structured key warnings, contraindications, or drug-interaction data were retrievable — DDI query returned "not found," and the SFDA/Saudi package insert has not yet been obtained; see data gap DG001 below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Rank 1's high score reflects Nizatidine's already-known, approved H2RA mechanism rather than a novel indication — it is not a repurposing opportunity and should not drive a "Go" decision.
- Of the six genuinely novel candidates, only gastroduodenitis (NSAID-induced mucosal protection) has any direct supporting evidence, and it is limited to two small 1990s trials (L3, decision stage S2, "Research Question") — not sufficient for a Go or Guardrails decision. The remaining five candidates (perforation, obstruction, duodenogastric reflux, gastrojejunal ulcer, multiple endocrine neoplasia) are explicitly flagged **Hold** by the evidence pack's own scoring, with weak-to-absent mechanistic fit and no clinical or trial evidence.
- A **Blocking** data gap (DG001 — missing SFDA/Saudi package insert warnings and contraindications) currently prevents this candidate from even entering the S1 safety pre-assessment stage, independent of efficacy evidence strength.
- Nizatidine has zero market authorizations in Saudi Arabia (Not Marketed), so there is no existing regulatory foothold to build a repurposing submission on.

**To proceed, the following is needed:**
- Obtain the official Saudi Arabia (SFDA) package insert/label safety data to resolve the Blocking gap (DG001) and unlock S1 safety evaluation
- Obtain a structured DrugBank/MOA record to formally resolve the High-severity gap (DG002)
- If gastroduodenitis (NSAID-protection) is pursued as the lead candidate, commission an updated systematic review or new prospective trial, since existing evidence is limited to two small studies from 1990 and 1994
- Determine a Saudi Arabia market-entry strategy given the current "Not Marketed" status before any repurposing regulatory submission is considered
- In future evidence-pack generation, exclude the drug's own known/approved indication from the "predicted new indication" ranking to avoid conflating model calibration checks with genuine repurposing signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

