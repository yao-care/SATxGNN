---
layout: default
title: Pentoxyverine
parent: 僅模型預測 (L5)
nav_order: 487
evidence_level: L5
indication_count: 2
---

# Pentoxyverine
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

# Pentoxyverine: From Cough Suppression to Acute Laryngopharyngitis

## One-Sentence Summary

> Pentoxyverine is a centrally-acting, non-opioid antitussive traditionally used to relieve cough associated with the common cold and upper respiratory tract infections.
> The TxGNN model predicts it may be effective for **Acute Laryngopharyngitis** (and, as a secondary candidate, **Nasal Cavity Disease**),
> but currently **no clinical trials and no published literature** support either direction — the signal is model-prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in structured regulatory data (no licenses on file); per known pharmacology, used symptomatically for cough associated with common cold/upper respiratory infection |
| Predicted New Indication | Acute Laryngopharyngitis |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known pharmacological information, pentoxyverine is a centrally-acting, non-opioid cough suppressant with weak local-anesthetic and anticholinergic/antispasmodic properties, long used for symptomatic relief of cough in colds and upper respiratory tract infections.

Acute laryngopharyngitis commonly presents with cough and mucosal irritation, which gives a plausible — though indirect — pharmacological link to pentoxyverine's cough-reflex suppression and local-anesthetic action. The second candidate, nasal cavity disease, has a weaker rationale: any effect would rely on the drug's mild anticholinergic action reducing secretions, which is speculative rather than mechanistically direct.

Both links are theoretical inferences from general drug class knowledge, not findings from the evidence pack itself. No clinical trials, literature, or original-indication/MOA data are available to cross-validate either connection, and the TxGNN score (0.996) reflects model prediction strength only — it is not clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA package insert warnings/contraindications are marked as a Blocking data gap — this must be resolved before any S1 safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests entirely on TxGNN model output (L5, no clinical trials or literature), and the drug is not currently marketed in Taiwan (0 authorizations) with a Blocking gap on TFDA safety labeling — there is no basis yet for S1 safety screening or clinical prioritization.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — required to clear the Blocking gap before any safety evaluation
- Confirmed mechanism of action (MOA) data via DrugBank API
- Confirmed original indication(s) from a regulatory source (current summary is based on general pharmacology, not license records)
- Any clinical trial or literature evidence specific to acute laryngopharyngitis or nasal cavity disease, since none currently exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

