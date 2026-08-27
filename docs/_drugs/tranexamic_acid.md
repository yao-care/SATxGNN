---
layout: default
title: Tranexamic Acid
parent: 僅模型預測 (L5)
nav_order: 631
evidence_level: L5
indication_count: 1
---

# Tranexamic Acid
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

# Tranexamic Acid: From Heavy Menstrual Bleeding to Amenorrhea

## One-Sentence Summary

Tranexamic acid is an anti-fibrinolytic agent whose established clinical role is reducing heavy menstrual bleeding (menorrhagia) and other bleeding conditions by inhibiting plasminogen activation. The TxGNN model predicts a possible link to **Amenorrhea**, but this direction is mechanistically counter-intuitive — the drug reduces blood loss during menstruation rather than suppressing menstruation itself. Currently only **2 review-type publications** support this direction, with **no clinical trials, no ICTRP records, and no dedicated mechanistic studies**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Heavy menstrual bleeding / menorrhagia (anti-fibrinolytic hemostatic use; no formal indication record available in this data set) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a data gap). Based on known pharmacology, tranexamic acid is an anti-fibrinolytic agent that inhibits plasminogen activator, thereby reducing clot breakdown and menstrual blood loss — its established use is treating **heavy** menstrual bleeding, not stopping menstruation altogether.

This creates a notable mechanistic mismatch with the predicted indication. Amenorrhea (absence of menstruation) is clinically achieved through hormonal mechanisms — GnRH agonists, combined oral contraceptives — not through hemostatic agents. The high TxGNN score (99.19%) most likely reflects the knowledge graph clustering tranexamic acid near other "menstrual disorder" nodes (e.g., menorrhagia and amenorrhea both sitting within the same menstrual-disturbance disease cluster) rather than a genuine mechanistic pathway supporting amenorrhea induction.

The two supporting publications reinforce this interpretation rather than contradict it: one reviews pharmacological therapy for **abnormal uterine bleeding** (i.e., reducing bleeding, not inducing amenorrhea), and the other discusses **menses suppression in hematologic cancer patients**, where tranexamic acid — if used at all — would play a supportive hemostatic role alongside hormonal agents that do the actual suppressing. Neither paper provides direct evidence that tranexamic acid itself induces amenorrhea.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause (New York, N.Y.) | Reviews pharmacological therapy for abnormal uterine bleeding; nonhormonal agents (including antifibrinolytics) reduce bleeding volume but do not induce amenorrhea — hormonal options are used for that purpose |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Review | Journal of Oncology Pharmacy Practice | Systematic review of menses prophylaxis/suppression in pre-menopausal hematologic cancer patients; notes lack of comparative data among suppression agents, with antifibrinolytics used as an adjunct rather than the primary suppressive mechanism |

## Saudi Arabia Market Information

Tranexamic acid is not currently marketed in Saudi Arabia under this data set (0 authorizations recorded), so no product-level licensing table is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted mechanistic link between tranexamic acid (a hemostatic, anti-fibrinolytic agent) and amenorrhea (absence of menstruation) runs contrary to the drug's known pharmacology, and the supporting literature (2 reviews, no trials) does not directly substantiate the prediction — it more plausibly reflects a knowledge-graph clustering artifact around "menstrual disorder" nodes than a genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert with full warnings and contraindications (currently a blocking data gap)
- Confirmed mechanism of action (MOA) data from DrugBank or primary pharmacology sources
- Dedicated primary research or mechanistic studies directly testing tranexamic acid's effect on menstrual suppression (not just bleeding reduction)
- Clinical trial or ICTRP evidence specific to amenorrhea, which currently does not exist
- Re-evaluation of whether the TxGNN score reflects a true signal or a graph-topology artifact before allocating further review resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

