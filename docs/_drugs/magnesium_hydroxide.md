---
layout: default
title: Magnesium Hydroxide
parent: 僅模型預測 (L5)
nav_order: 395
evidence_level: L5
indication_count: 6
---

# Magnesium Hydroxide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Magnesium Hydroxide: From Antacid Use to Active Peptic Ulcer Disease

## One-Sentence Summary

> Magnesium hydroxide is a classic antacid, long used generically for gastric acid neutralization and symptomatic relief of hyperacidity.
> The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**,
> with **0 disease-specific clinical trials** but **20 supporting publications** (including several controlled trials of antacid-class therapy) currently backing this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally registered in this market (drug is not marketed); generically used as an antacid for gastric hyperacidity/dyspepsia |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation is not available in this evidence pack (flagged as a High-severity data gap). Based on the information that is available, magnesium hydroxide is a classic antacid component (frequently formulated in combination with aluminum hydroxide, e.g., Maalox-type products), and its role in neutralizing gastric acid has been established through decades of clinical use.

The predicted indication — active peptic ulcer disease — is mechanistically continuous with, rather than distinct from, the drug's traditional antacid use. Peptic ulcer disease is fundamentally an acid/pepsin-mediated mucosal injury condition, which is precisely the pathology that antacid neutralization is designed to address. This is less a "repurposing" leap and more a formal validation of an already well-established pharmacological role.

Mechanistically, the supporting literature describes magnesium hydroxide as acting through gastric acid neutralization, elevation of intragastric pH, and stimulation of prostaglandin-dependent mucosal cytoprotection — a mechanism that has underpinned its use as a first-line/adjunct peptic ulcer therapy for decades, typically administered in combination with aluminum hydroxide.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scand J Gastroenterol | 12-week double-blind trial: antacid/anticholinergic vs. cimetidine vs. placebo in 72 patients with active duodenal/prepyloric ulcers; antacid arm significantly outperformed placebo |
| [6086186](https://pubmed.ncbi.nlm.nih.gov/6086186/) | 1984 | RCT | Clin Gastroenterol | Review/trial data on antacids and anticholinergics in duodenal ulcer treatment |
| [1526089](https://pubmed.ncbi.nlm.nih.gov/1526089/) | 1992 | RCT (H2-blocker comparator) | Clin Pharmacol Ther | 8-week multicenter RCT of nizatidine vs. placebo in benign gastric ulcer; used as an indirect efficacy benchmark for acid-suppressive/antacid therapy |
| [37146](https://pubmed.ncbi.nlm.nih.gov/37146/) | 1979 | Review | Fortschritte der Medizin | Reviews antacid neutralizing capacity and dosing needed to inhibit pepsin activity and support ulcer healing |
| [22950493](https://pubmed.ncbi.nlm.nih.gov/22950493/) | 2013 | Review | Curr Pharm Des | Updates cellular/molecular mechanisms of antacid-mediated gastric cytoprotection and ulcer healing beyond prostaglandins |
| [2595273](https://pubmed.ncbi.nlm.nih.gov/2595273/) | 1989 | Animal study (rat) | Scand J Gastroenterol | Al(OH)3/Mg(OH)2-containing antacid dose-dependently prevented gastric lesions from ethanol, aspirin, and stress in rats, comparable to a PGE2 analog |
| [3018068](https://pubmed.ncbi.nlm.nih.gov/3018068/) | 1986 | Small clinical comparison | J Clin Gastroenterol | Compared postprandial acid-buffering duration of sodium bicarbonate vs. aluminum-magnesium hydroxide in duodenal ulcer patients |
| [2401189](https://pubmed.ncbi.nlm.nih.gov/2401189/) | 1990 | Retrospective clinical study | Drugs Exp Clin Res | 267 pediatric patients with peptic symptoms; evaluated efficacy of various pharmacological agents (incl. antacids) in acute and relapse phases |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | In vitro evaluation | Med Pharm Rep | Evaluated acid-neutralizing capacity of commercially marketed antacids (magnesium/aluminum hydroxide-based) |
| [31111054](https://pubmed.ncbi.nlm.nih.gov/31111054/) | 2019 | Animal study (rat) | BioMed Res Int | Hydrotalcite (Mg/Al hydroxide compound) reduced NSAID-induced gastric injury in rats, linked to EGF/PGE2 secretion |

---

## Saudi Arabia Market Information

Not currently marketed in this jurisdiction; no product authorization records available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L2 is supported by multiple older RCTs and mechanistic studies establishing antacid efficacy in acid-related ulcer disease, and the mechanism (acid neutralization + prostaglandin-mediated mucosal cytoprotection) is well characterized. However, no disease-specific clinical trials exist, the drug is not currently marketed in this jurisdiction, and safety/labeling data are unavailable — so guardrails are warranted before advancing further.

**To proceed, the following is needed:**
- TFDA/SFDA package insert (warnings, contraindications) — currently a Blocking data gap preventing S1 safety review
- Formal mechanism-of-action documentation from DrugBank or equivalent source
- Drug-drug interaction (DDI) data (current query status: not found)
- Confirmation of market registration pathway/status in Saudi Arabia
- Contemporary trials evaluating magnesium hydroxide specifically against current "active peptic ulcer disease" diagnostic criteria, since most supporting literature predates modern PPI-era treatment standards
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

