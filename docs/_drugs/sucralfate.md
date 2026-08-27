---
layout: default
title: Sucralfate
parent: 僅模型預測 (L5)
nav_order: 586
evidence_level: L5
indication_count: 2
---

# Sucralfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Sucralfate: From Peptic Ulcer Disease to Duodenogastric Reflux

## One-Sentence Summary

Sucralfate is a mucosal-protective agent classically used for gastric and duodenal ulcer treatment (formal Saudi registry indication text is not available in this evidence pack — the product is not currently marketed in Saudi Arabia). The TxGNN model predicts it may be effective for **Duodenogastric Reflux** (bile/alkaline reflux gastritis), a prediction reinforced by a body of older clinical literature rather than by any registered clinical trials — **0 registered clinical trials** and **13 publications**, including several small randomized controlled trials, currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Saudi registry (drug not marketed); sucralfate is broadly known as a gastric/duodenal ulcer cytoprotective agent |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, sucralfate is an aluminum sucrose sulfate complex that, in an acidic environment, forms a viscous, adherent barrier over ulcerated or inflamed gastric mucosa. This barrier binds proteinaceous exudate at the injury site, adsorbs bile acids and pepsin, and stimulates local prostaglandin and mucus/bicarbonate production — a cytoprotective effect that is largely independent of acid suppression.

Duodenogastric reflux (bile reflux gastritis) causes mucosal injury through a mechanism distinct from acid-peptic ulcer disease but converging on the same target tissue: bile and duodenal alkaline content damage the gastric mucosal barrier in a manner analogous to acid/pepsin injury in classic peptic ulcer disease. Because sucralfate's barrier-forming and bile-acid-adsorbing action is not acid-dependent, it is mechanistically plausible that a drug proven effective for acid-related mucosal injury would also mitigate bile-induced mucosal injury.

This is not a purely theoretical extrapolation — the literature evidence below shows sucralfate has already been directly studied in duodenogastric/alkaline reflux gastritis for decades (e.g., post-gastrectomy and post-cholecystectomy alkaline reflux gastritis), which substantially strengthens the TxGNN prediction beyond a pure mechanism-of-action inference.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12923369](https://pubmed.ncbi.nlm.nih.gov/12923369/) | 2003 | RCT | Eur J Gastroenterol Hepatol | Randomized trial of sucralfate vs. rabeprazole vs. no treatment for post-cholecystectomy alkaline reactive gastritis |
| [1391144](https://pubmed.ncbi.nlm.nih.gov/1391144/) | 1992 | RCT | Minerva Gastroenterol Dietol | Sucralfate vs. cisapride in dyspepsia associated with duodenogastric reflux gastritis (n=18) |
| [3475771](https://pubmed.ncbi.nlm.nih.gov/3475771/) | 1987 | RCT | Scand J Gastroenterol Suppl | Prospective randomized trial of sucralfate vs. placebo in symptomatic/macroscopic gastritis with duodenogastric reflux |
| [3839973](https://pubmed.ncbi.nlm.nih.gov/3839973/) | 1985 | RCT | Am J Med | Randomized double-blind study: sucralfate 6g/day vs. placebo in alkaline reflux gastritis post-Billroth I/II/vagotomy (n=23) |
| [17285081](https://pubmed.ncbi.nlm.nih.gov/17285081/) | 2006 | Review | J Chir | Review of duodenogastric/gastroesophageal bile reflux pathophysiology, diagnosis (24h bile monitoring), and therapeutic management |
| [14723838](https://pubmed.ncbi.nlm.nih.gov/14723838/) | 2004 | Review | Curr Treat Options Gastroenterol | Review of duodenogastric reflux-induced (alkaline) esophagitis; notes PPIs as best medical treatment, difficulty of DGER management |
| [6372664](https://pubmed.ncbi.nlm.nih.gov/6372664/) | 1984 | Review | Annu Rev Med | Review of alkaline reflux (bile) gastritis and esophagitis pathophysiology and diagnostic features |
| [10228771](https://pubmed.ncbi.nlm.nih.gov/10228771/) | 1999 | Review | Hepatogastroenterology | Review of indications, technique, and outcomes of duodenal switch surgery for pathologic duodenogastric reflux |
| [3552846](https://pubmed.ncbi.nlm.nih.gov/3552846/) | 1987 | Review | Gastroenterol Clin Biol | Pharmacologic basis for medical treatment of duodenogastric reflux (abstract not available) |
| [3838414](https://pubmed.ncbi.nlm.nih.gov/3838414/) | 1985 | Review | Am J Gastroenterol | ACG committee review of sucralfate's nonulcer uses, including gastritis; notes efficacy not yet clearly established, needs further study |

---

## Saudi Arabia Market Information

Sucralfate currently holds no marketing authorization in Saudi Arabia (0 registered products).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high and is corroborated by decades of literature — including several small RCTs — directly testing sucralfate in duodenogastric/alkaline reflux gastritis, but there are no registered clinical trials, no confirmed MOA record, and the drug has no current marketing authorization or safety/labeling data in Saudi Arabia, making a "Go" or "Proceed with Guardrails" premature.

**To proceed, the following is needed:**
- SFDA-approved package insert (warnings, contraindications) — currently a blocking data gap
- Confirmed DrugBank/mechanism-of-action data for sucralfate
- A formal DDI review, since the current query returned no results
- Assessment of Saudi Arabia market-entry pathway, since the product is not currently marketed
- Ideally, a contemporary, adequately powered RCT or systematic review, since existing trials are small and decades old
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

