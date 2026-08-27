---
layout: default
title: Pitavastatin
parent: 僅模型預測 (L5)
nav_order: 501
evidence_level: L5
indication_count: 10
---

# Pitavastatin
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

# Pitavastatin: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Pitavastatin is an HMG-CoA reductase inhibitor (statin) established for treating hypercholesterolemia and mixed dyslipidemia. The TxGNN model's top-ranked prediction is **Homozygous Familial Hypercholesterolemia (HoFH)**, but this specific candidate currently has **no registered clinical trials** and only **2 supporting publications** (one indirect RCT, one case report) — evidence is thin, and the drug's own mechanism is known to have limited efficacy in this particular patient population.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / mixed dyslipidemia (as HMG-CoA reductase inhibitor) — no formal approved-label text available (drug not marketed in Saudi Arabia) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.99% (rank 171) |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed official mechanism-of-action documentation is not available (data gap, severity: High). Based on the evidence collected, pitavastatin is a synthetic HMG-CoA reductase inhibitor: it blocks hepatic cholesterol biosynthesis, which upregulates LDL receptor expression and thereby lowers LDL-C — the pharmacological basis of its established use in hypercholesterolemia and mixed dyslipidemia.

HoFH and general hypercholesterolemia are mechanistically related, but the connection is weaker than for other statin indications. The evidence pack's own rationale for this candidate states it directly: HoFH patients have severely deficient or absent LDL receptor function, so a mechanism that works by *upregulating* the LDL receptor has intrinsically limited effect in this population. Clinically, statins in HoFH are used only as **adjunct** therapy alongside PCSK9 inhibitors or LDL apheresis — not as a standalone treatment. The mechanistic link exists, but its clinical impact in HoFH specifically is constrained.

For context, other TxGNN-predicted indications for pitavastatin in this evidence pack have substantially stronger support — e.g., hyperlipoproteinemia (rank 2, L1, 12 trials including Phase 4 RCTs) and HIV-associated cardiovascular risk reduction (rank 7, L1, including the landmark REPRIEVE trial, NEJM 2023). Those may warrant separate evaluation as more mature candidates.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | RCT | The Lancet HIV | INTREPID trial: pitavastatin vs. pravastatin in HIV-1 patients with dyslipidaemia. Population is not HoFH-specific; relevant mainly for showing pitavastatin's efficacy/safety profile independent of CYP450-mediated drug interactions. |
| [39532566](https://pubmed.ncbi.nlm.nih.gov/39532566/) | 2025 | Case report | Journal of Clinical Lipidology | Two cases of autosomal recessive hypercholesterolemia (ARH) — a condition clinically indistinguishable from HoFH — showing rapid lipid-lowering response to treatment. |

## Saudi Arabia Market Information

Pitavastatin is not currently marketed in Saudi Arabia — no product authorization records are available (0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/SFDA package insert data is flagged as a Blocking data gap — key warnings, contraindications, and drug-drug interaction data could not be retrieved and should be sourced before any safety evaluation.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for pitavastatin specifically in HoFH is limited to two publications (no dedicated RCT or trial registered), and the drug's own mechanism of action is explicitly constrained in this population — LDL receptor upregulation has reduced effect when receptor function is severely deficient or absent, limiting pitavastatin to an adjunct role alongside PCSK9 inhibitors or LDL apheresis rather than standalone therapy.

**To proceed, the following is needed:**
- SFDA-approved package insert (warnings, contraindications, DDI) — currently a Blocking data gap
- Verified mechanism-of-action documentation from DrugBank or primary literature — currently a High-severity data gap
- A dedicated clinical trial or larger case series evaluating pitavastatin (alone or as PCSK9i/apheresis adjunct) specifically in HoFH patients
- Formal S1 safety review prior to any further evaluation stage
- Consider evaluating the stronger-evidence candidates in this same evidence pack (hyperlipoproteinemia, HIV-associated CVD risk reduction) as parallel or alternative repurposing targets
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

