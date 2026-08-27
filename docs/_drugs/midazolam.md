---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 420
evidence_level: L5
indication_count: 1
---

# Midazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Midazolam: From Procedural Sedation to Insomnia

## One-Sentence Summary

Midazolam is a short-acting benzodiazepine most widely used for procedural sedation, anesthesia induction, and premedication. The TxGNN model predicts it may also be effective for **Insomnia**, with **32 clinical trials** and **11 publications** currently identified as related evidence — though most of the trials use midazolam only as a comparator arm rather than as the primary intervention being tested for insomnia.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Saudi Arabia licensing data (0 licenses on file). Based on known pharmacology, midazolam is used for procedural sedation, anesthesia premedication/induction, and ICU sedation. |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L3 |
| Saudi Arabia Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, midazolam is a short-acting benzodiazepine that acts as a positive allosteric modulator at the GABA-A receptor, producing sedative, hypnotic, anxiolytic, and amnestic effects. Its efficacy for procedural sedation and anesthesia has long been established, and mechanistically the same GABAergic sedative-hypnotic activity may be applicable to insomnia — this is the same receptor mechanism exploited by classic hypnotic benzodiazepines (e.g., flurazepam, triazolam) that are already approved for sleep disorders.

Several of the retrieved trials and publications are not testing midazolam as a primary insomnia treatment, but rather use it as an active comparator against newer sedative agents (dexmedetomidine, remimazolam, ketamine) in postoperative or ICU sleep-quality settings. This pattern is consistent with midazolam's established but off-label use as a short-term hypnotic, rather than representing a novel repurposing signal with strong new-indication-specific trial design.

The oldest and most directly relevant evidence — a cluster of double-blind, randomized studies from the 1980s–1990s — evaluated oral midazolam specifically for insomnia and sleep-disorder populations, and found it to be an effective, well-tolerated short-term hypnotic. This gives some historical clinical grounding to the TxGNN prediction, even though these studies predate modern trial registries and are not phase-classified.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | NA | Recruiting | 280 | Preoperative oral midazolam for postoperative pain in colorectal cancer patients with sleep disturbance/anxiety; states oral midazolam solution is safe and effective for short-term hypnosis |
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | Completed | 111 | Compares postoperative sleep quality of dexmedetomidine vs. midazolam sedation in TURP patients |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | N/A | Terminated | 5 | Compares dexmedetomidine vs. midazolam on sleep quality/quantity via 24-hour polysomnography in ICU patients |
| [NCT00744380](https://clinicaltrials.gov/study/NCT00744380) | NA | Completed | 23 | Randomized double-blind study of midazolam vs. dexmedetomidine for facilitating extubation in ICU patients |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | Terminated | 6 | Polysomnographic comparison of α2 agonist (dexmedetomidine) vs. GABA agonist (midazolam) sedation on sleep stages |
| [NCT07336095](https://clinicaltrials.gov/study/NCT07336095) | Phase 3 | Not yet recruiting | 195 | Oral melatonin vs. oral midazolam premedication in children undergoing tonsillectomy |
| [NCT04082767](https://clinicaltrials.gov/study/NCT04082767) | Phase 3 | Unknown | 120 | Sedation efficacy of dexmedetomidine vs. midazolam in critically ill ventilated children |
| [NCT05606315](https://clinicaltrials.gov/study/NCT05606315) | Phase 4 | Unknown | 285 | Remimazolam besylate (midazolam-class benzodiazepine) for ICU sedation after oral/maxillofacial surgery |
| [NCT05466279](https://clinicaltrials.gov/study/NCT05466279) | NA | Completed | 131 | Remimazolam vs. propofol+midazolam general anesthesia, randomized controlled trial |
| [NCT06480500](https://clinicaltrials.gov/study/NCT06480500) | Phase 2 | Recruiting | 110 | i-CBT plus IV ketamine for suicidality in treatment-resistant depression, midazolam-controlled RCT |

Note: most listed trials use midazolam as a comparator/control arm against newer sedatives, rather than testing midazolam as a primary treatment for insomnia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT | Journal of Clinical Psychopharmacology | Randomized, double-blind, parallel-group, multicenter study of sleep, performance, and plasma levels in chronic insomniacs using flurazepam and midazolam over 14 days |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | RCT (executive summary) | Journal of Clinical Psychopharmacology | Executive summary of the above multicenter 14-day flurazepam vs. midazolam study in chronic insomniacs |
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | British Journal of Clinical Pharmacology | Double-blind study of midazolam 15 mg vs. Vesparax in insomnia secondary to neuromuscular disease; midazolam was effective and better tolerated, without hangover effect |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | Dose-finding study | Arzneimittel-Forschung | Multicenter pilot study evaluating oral midazolam (10–30 mg) efficacy and tolerance in 75 hospitalized patients with mild-to-moderate insomnia |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Review | Orvosi Hetilap | Review of insomnia pathophysiology, including hyperarousal and cerebral hypoperfusion mechanisms relevant to hypnotic drug use |

---

## Saudi Arabia Market Information

Midazolam currently has no marketing authorization on file in Saudi Arabia (market status: Not Marketed, 0 licenses). No authorization number, product name, or approved indication text is available for this drug in the Evidence Pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI fields in this Evidence Pack are marked as data gaps; the TFDA/SFDA package-insert warning and contraindication data is flagged as a **Blocking** gap — DG001 — which prevents S1 safety pre-screening.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Midazolam is not currently marketed in Saudi Arabia (0 licenses), and the blocking data gap on TFDA/SFDA package-insert warnings and contraindications prevents any S1 safety pre-screening. While historical double-blind RCTs from the 1980s–1990s support midazolam's efficacy as a short-term hypnotic, most current registered trials use midazolam only as a comparator rather than as the primary insomnia intervention, so the evidence base for this specific repurposing signal remains indirect.

**To proceed, the following is needed:**
- TFDA/SFDA package insert with full warnings, contraindications, and drug interaction data (DG001)
- Confirmed mechanism of action documentation from DrugBank (DG002)
- Assessment of Saudi Arabia regulatory pathway, given the drug currently has no local marketing authorization
- A modern, phase-classified RCT evaluating midazolam specifically as a primary treatment for insomnia (not merely as a comparator arm)
- DDI review, particularly for CNS depressant and CYP3A4-interacting co-medications relevant to chronic insomnia populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

