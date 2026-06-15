---
layout: default
title: Apomorphine
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 10
---

# Apomorphine
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

# Apomorphine: From Parkinson's Disease to Perisylvian Polymicrogyria with Cerebellar Hypoplasia and Arthrogryposis

## One-Sentence Summary

Apomorphine is a direct-acting dopamine receptor agonist with established clinical use in the acute management of "off" episodes in Parkinson's disease.
The TxGNN model's top prediction suggests potential activity in **Polymicrogyria, Perisylvian, with Cerebellar Hypoplasia and Arthrogryposis** (OMIM#618798),
however **0 clinical trials** and **0 publications** currently support this direction, and biological plausibility is low.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (off-episodes); no Saudi Arabia regulatory record available |
| Predicted New Indication | Polymicrogyria, Perisylvian, with Cerebellar Hypoplasia and Arthrogryposis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Saudi Arabia Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Apomorphine is not available in the current dataset. Based on established pharmacological knowledge, Apomorphine is a potent, non-selective dopamine receptor agonist acting across D1–D5 receptor subtypes. It is administered subcutaneously or sublingually and is best known for reversing motor off-episodes in Parkinson's disease by bypassing the striatal dopaminergic deficit.

Perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis (OMIM#618798) is an extremely rare congenital structural brain malformation arising from defective neuronal migration during embryonic cortical development. The pathogenesis involves disrupted radial glial scaffolding and cortical laminar organization — processes that are not regulated by dopaminergic signaling. There is no established molecular link between D1–D5 receptor agonism and the correction of neuronal migration defects.

The TxGNN model's high score (99.75%) most likely reflects indirect co-disease or co-gene connections within the knowledge graph (e.g., shared comorbidity nodes or phenotypic overlap with other dopamine-related disorders) rather than a direct mechanistic basis. Without biological plausibility and with zero supporting clinical or preclinical evidence, this prediction should be interpreted with caution and is not suitable for further development at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Saudi Arabia Market Information

Apomorphine is not currently registered or marketed in Saudi Arabia. No authorization records are available in the regulatory database.

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** Key warnings and contraindications data were identified as a Blocking data gap (DG001) during this evaluation. The SFDA/TFDA package insert should be retrieved and reviewed before any clinical planning proceeds. Known class-level concerns for dopamine agonists include nausea, vomiting (often requiring antiemetic pre-treatment with domperidone), hypotension, somnolence, and impulse control disorders.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis is a congenital structural brain malformation with a disease mechanism (neuronal migration defect) that has no established connection to the dopamine receptor system. There is no clinical or preclinical evidence supporting Apomorphine in this condition, and the biological rationale is absent.

**To proceed, the following is needed:**
- Retrieve and review the SFDA/package insert for Apomorphine to address the Blocking data gap (DG001: key warnings and contraindications)
- Obtain detailed mechanism of action data from DrugBank (DG002) to enable mechanistic plausibility analysis
- Review the TxGNN knowledge graph paths to understand which graph edges generated this high-score prediction
- Evaluate whether any upstream neurological or developmental pathway intersects with dopaminergic signaling before considering any exploratory study design

---

> **Analyst Note — Other Predicted Indications:**
> Among the 10 TxGNN predictions in this Evidence Pack, **schizophrenia** (rank 5; score 99.69%) is the only indication reaching **L3 evidence** and a *Research Question* staging recommendation. It is supported by 2 clinical trials (NCT00009048, NCT03911726) and 20 publications spanning dopamine autoreceptor hypothesis studies and neuroendocrine challenge paradigms. The historical "presynaptic autoreceptor" rationale — low-dose Apomorphine preferentially stimulating D2 autoreceptors to suppress dopamine synthesis — provides biological plausibility, though no direct therapeutic RCT exists. A safety caveat applies: as a full dopamine agonist, higher doses risk exacerbating positive psychotic symptoms. This direction warrants a dedicated evidence review separate from the present Hold recommendation for the top-ranked indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

