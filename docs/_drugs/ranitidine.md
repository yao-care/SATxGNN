---
layout: default
title: Ranitidine
parent: 僅模型預測 (L5)
nav_order: 536
evidence_level: L5
indication_count: 10
---

# Ranitidine
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

# Ranitidine: From Peptic Ulcer Disease to Active Peptic Ulcer Disease

## One-Sentence Summary

Ranitidine is a classic histamine H2-receptor antagonist, but this evidence pack's original-indication record is incomplete (a data gap, not evidence that no indication exists). The TxGNN model's top prediction, **Active Peptic Ulcer Disease**, is essentially a reaffirmation of ranitidine's own well-established, decades-old use rather than a genuinely novel repurposing target, supported by **1 clinical trial** (indirectly relevant) and **19 publications**, several of which are direct RCTs of ranitidine in ulcer healing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease / gastric hypersecretory conditions (record incomplete in this evidence pack — DrugBank original-indication field is a data gap, not an absence of indication) |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L1 |
| Saudi Arabia Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate. Based on known pharmacological information, ranitidine is a first-generation histamine H2-receptor antagonist that competitively blocks histamine-stimulated gastric acid secretion at parietal cells — the same mechanism underlying its historical, well-proven efficacy in duodenal and gastric ulcer healing.

The predicted new indication, "active peptic ulcer disease," is not mechanistically distant from ranitidine's original use — it is, in fact, the disease category the drug was originally developed and approved for. The repurposing rationale explicitly notes this is "not a new indication but the original approved use," and that the apparent absence of an original-indication field in this dataset reflects a data-collection gap rather than a true lack of indication.

Because the mechanism (acid suppression via H2-receptor blockade) directly and specifically targets the pathophysiology of peptic ulcer disease, the TxGNN score is mechanistically well-grounded — this is less a discovery of a new therapeutic avenue and more a confirmation that the knowledge graph correctly recovered the drug's foundational indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated PPI/statin effects on clopidogrel antiplatelet activity in PCI patients; ranitidine was not the primary study drug — relevance is indirect (H2RA-vs-PPI context only), not direct efficacy evidence for peptic ulcer disease. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3909374](https://pubmed.ncbi.nlm.nih.gov/3909374/) | 1985 | RCT/Review | Scandinavian Journal of Gastroenterology | Ranitidine 300mg/day achieved 4-week healing rates of 91% (duodenal), 68% (prepyloric), 81% (gastric corporeal) ulcers; maintenance therapy reduced relapse vs placebo over 1 year. |
| [3104657](https://pubmed.ncbi.nlm.nih.gov/3104657/) | 1986 | RCT (comparative) | Klinische Wochenschrift | Compared rioprostil (prostaglandin E1 analogue) vs ranitidine for nocturnal duodenal ulcer healing. |
| [12749277](https://pubmed.ncbi.nlm.nih.gov/12749277/) | 2003 | Prospective controlled study | Hepato-gastroenterology | Ecabet plus ranitidine vs ranitidine alone for inhibition of peptic ulcer relapse, independent of H. pylori eradication. |
| [6317325](https://pubmed.ncbi.nlm.nih.gov/6317325/) | 1983 | Drug monograph review | Drug Intelligence & Clinical Pharmacy | Foundational review confirming ranitidine's FDA approval and efficacy for active duodenal ulcer and gastric hypersecretory conditions; 4–10x more potent than cimetidine. |
| [2905237](https://pubmed.ncbi.nlm.nih.gov/2905237/) | 1988 | Review | Drugs | Reviews the role of prostaglandins and H2-receptor antagonists in peptic ulcer pathophysiology and treatment. |
| [1976583](https://pubmed.ncbi.nlm.nih.gov/1976583/) | 1990 | Review | Hepato-gastroenterology | Reviews acid suppression as the key mechanism in peptic ulcer healing, referencing H2RA class effects. |
| [18493408](https://pubmed.ncbi.nlm.nih.gov/18493408/) | 1996 | Prospective study | Diagnostic and Therapeutic Endoscopy | Endoscopic evaluation of active/healed duodenal ulcer status in patients on regular ranitidine 150mg twice daily during Ramadan fasting. |
| [1348650](https://pubmed.ncbi.nlm.nih.gov/1348650/) | 1992 | Clinical study | The Italian Journal of Gastroenterology | Cirrhotic patients with gastric/duodenal ulcer treated with cimetidine vs ranitidine 300mg/day; 66.2% healed at 6 weeks. |
| [2858110](https://pubmed.ncbi.nlm.nih.gov/2858110/) | 1985 | Animal mechanistic study | Pharmacology | Compared cimetidine, ranitidine, and mifentidine in gastric/duodenal damage models, supporting H2-antagonism as the protective mechanism. |
| [8736619](https://pubmed.ncbi.nlm.nih.gov/8736619/) | 1996 | Comparator drug review | Drugs | Review of ebrotidine notes its antisecretory potency is benchmarked directly against ranitidine. |

---

## Saudi Arabia Market Information

No marketing authorization records are available — the evidence pack lists 0 licenses and market status "Not Marketed."

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ranitidine's antisecretory mechanism is well established for peptic ulcer disease, and the literature base (multiple RCTs, decades of monograph-level evidence) strongly supports efficacy. However, because this indication substantially overlaps with the drug's own original use rather than representing a novel target, and because the current dataset lacks the drug's original-indication record and TFDA safety labeling, guardrails are warranted before advancing further.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a **blocking** data gap that prevents entry into the S1 safety pre-assessment stage
- Confirmed mechanism of action (MOA) data from DrugBank, to formally validate the mechanistic rationale
- Clarification of the drug's original-indication record, since the current "no original indications" listing appears to be a data-collection artifact rather than a true absence
- A safety monitoring plan, given the current safety fields (warnings, contraindications, DDI) are all unresolved/not found
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

