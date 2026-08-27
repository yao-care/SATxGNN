---
layout: default
title: Letermovir
parent: 僅模型預測 (L5)
nav_order: 368
evidence_level: L5
indication_count: 1
---

# Letermovir
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

# Letermovir: From CMV Prophylaxis to Vulvovaginal Candidiasis

## One-Sentence Summary

> Letermovir is an antiviral agent (CMV terminase complex inhibitor) used for cytomegalovirus prophylaxis; no structured original-indication text is available in this evidence pack, but DrugBank and package-insert sources confirm its antiviral (anti-CMV) use.
> The TxGNN model predicts it may be effective for **Vulvovaginal Candidiasis**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the drug's known mechanism (viral terminase inhibition) has no plausible biological link to an antifungal target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not structured in this data pack; known use is CMV (cytomegalovirus) prophylaxis, per DrugBank/package insert reference cited in the evidence pack |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Saudi Arabia Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (`original_moa = [Data Gap]`). Based on the evidence pack's own repurposing rationale, letermovir is known to act as an inhibitor of the CMV terminase complex (pUL51/pUL56/pUL89), blocking herpesvirus DNA packaging and cleavage — a virus-specific target with no known homolog in humans or fungi.

Vulvovaginal candidiasis is caused by *Candida* spp., whose pathogenic mechanism involves fungal-specific pathways such as ergosterol synthesis (e.g., CYP51/lanosterol demethylase). There is no known overlap between the CMV terminase complex and any fungal drug target.

**This prediction should be interpreted with caution.** The mechanistic rationale supplied alongside this candidate explicitly concludes there is no plausible biological link between letermovir's known antiviral mechanism and antifungal activity against *Candida*. The signal is driven purely by the TxGNN network prediction score (99.88%) and is not corroborated by any mechanistic, clinical, or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Saudi Arabia Market Information

Letermovir is not currently marketed in Saudi Arabia (0 authorizations on file); no product license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has no clinical trial or literature support (Evidence Level L5), and — more importantly — the mechanistic rationale accompanying this candidate indicates no plausible biological link between letermovir's known antiviral (CMV terminase inhibition) mechanism and antifungal activity against *Candida*. The drug is also not currently marketed in Saudi Arabia.

**To proceed, the following is needed:**
- TFDA/SFDA package insert data (warnings, contraindications) — currently a Blocking data gap (DG001), required before any S1 safety pre-assessment
- Confirmed, structured original-indication and MOA data from DrugBank (DG002)
- New mechanistic or preclinical evidence directly linking letermovir to antifungal activity before further evidence generation is justified — absent such evidence, this candidate is not recommended for prioritization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

