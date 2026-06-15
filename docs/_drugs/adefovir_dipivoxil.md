---
layout: default
title: Adefovir Dipivoxil
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 10
---

# Adefovir Dipivoxil
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

# Adefovir Dipivoxil: From Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Adefovir dipivoxil (Hepsera) is a nucleotide analogue antiviral drug with established global use for chronic hepatitis B virus (HBV) infection, though it is not currently registered or marketed in Saudi Arabia.
The TxGNN model predicts it may be effective for **Chronic Hepatitis C Virus Infection**, achieving a score of 99.97%,
with **9 clinical trials** and **15 publications** identified — however, critical review reveals that virtually all of this evidence pertains to HBV treatment, not HCV, representing a systematic ontology mismatch rather than genuine mechanistic support.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hepatitis B Virus Infection (FDA-approved globally; not licensed in Saudi Arabia) |
| Predicted New Indication | Chronic Hepatitis C Virus Infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Saudi Arabia Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this dataset. Based on established pharmacological knowledge, adefovir dipivoxil is an oral prodrug hydrolyzed intracellularly to adefovir diphosphate, which competitively inhibits viral DNA polymerase (including its reverse transcriptase activity) and terminates viral DNA chain elongation. This mechanism supports its FDA-approved use against HBV at 10 mg/day, and it was also historically investigated for HIV at higher doses (60 mg/day) before being superseded by tenofovir due to unacceptable renal tubular toxicity.

The TxGNN model's prediction of HCV efficacy most likely arises from knowledge graph proximity between hepatitis-related disease nodes and antiviral drug nodes. HBV and HCV are both chronic, hepatotropic viral infections that share a large body of co-management literature, co-infection trials, and treatment guideline sections. In graph neural network models, this shared disease ontology ("chronic hepatitis," "liver disease," "nucleotide antiviral") generates high proximity scores that may not reflect mechanistic compatibility.

**The mechanistic case against this prediction is strong.** Hepatitis C virus is a positive-sense single-stranded RNA virus that replicates entirely through its own NS5B RNA-dependent RNA polymerase (RdRp) — an enzyme fundamentally distinct from the DNA polymerase and reverse transcriptase inhibited by adefovir. The current standard of care for HCV consists of direct-acting antivirals (DAAs) specifically targeting HCV NS5A, NS5B RdRp, and NS3/4A serine protease. Adefovir has no known interaction with any of these targets, and no pharmacological rationale supports its use in HCV at clinically achievable doses.

---

## Clinical Trial Evidence

All 9 identified trials are HBV studies inadvertently matched to this query due to shared disease ontology. No trials specifically evaluate adefovir efficacy in HCV infection.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00371761](https://clinicaltrials.gov/study/NCT00371761) | Phase 3 | Completed | 25 | PegIntron vs. Adefovir in HBeAg-positive chronic hepatitis B (Taiwan); marginally relevant in query context but adefovir's role is strictly HBV-targeted |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | Completed | 120 | IFN-α2b plus ribavirin (a standard HCV agent) for chronic HBV; ribavirin presence explains the HCV keyword match, but adefovir's HCV efficacy is not evaluated |
| [NCT01205165](https://clinicaltrials.gov/study/NCT01205165) | Phase 4 | Completed | 104 | Adefovir antiviral effect assessed over 52 weeks in Korean chronic HBV patients with compensated liver disease |
| [NCT00645294](https://clinicaltrials.gov/study/NCT00645294) | Phase 1/2 | Completed | 47 | Pharmacokinetics and safety of single-dose adefovir in children and adolescents aged 2–17 with chronic HBV |
| [NCT00973219](https://clinicaltrials.gov/study/NCT00973219) | N/A | Completed | 151 | Peg-IFN alfa-2a plus adefovir vs. Peg-IFN plus tenofovir vs. no treatment in HBeAg-negative HBV patients with low viral load |
| [NCT00013702](https://clinicaltrials.gov/study/NCT00013702) | Phase 2 | Completed | 30 | Adefovir added to lamivudine for HBV treatment in HIV-coinfected patients with decompensated liver disease and lamivudine-resistant virus |
| [NCT01925820](https://clinicaltrials.gov/study/NCT01925820) | Phase 4 | Unknown | 540 | Pegasys plus entecavir vs. entecavir vs. Pegasys monotherapy in HBeAg-negative chronic HBV patients |
| [NCT00810524](https://clinicaltrials.gov/study/NCT00810524) | Phase 4 | Unknown | 600 | Influence of early vs. conventional antiviral therapy on long-term prognosis in chronic HBV infection (10-year follow-up) |
| [NCT02560649](https://clinicaltrials.gov/study/NCT02560649) | Phase 4 | Unknown | 324 | Response-guided therapy (RGT) strategy using Peg-IFN add-on in NUC-experienced HBeAg-positive CHB patients achieving viral suppression |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [25892855](https://pubmed.ncbi.nlm.nih.gov/25892855/) | 2015 | Cohort | Mediators of Inflammation | TLR-9, CD86, and CD95 expression on circulating B cells in chronic HBV vs. HCV patients before and after antiviral therapy — immune profiling study, not adefovir efficacy in HCV |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antiviral drugs for HBV and HCV with renal effects; adefovir explicitly categorized as HBV-specific nucleotide analogue, while separate DAA agents are listed for HCV |
| [22370225](https://pubmed.ncbi.nlm.nih.gov/22370225/) | 2012 | Guideline | Orvosi Hetilap | Hungarian national consensus guideline for HBV, HCV, and HDV management; adefovir appears only in the HBV section |
| [19149648](https://pubmed.ncbi.nlm.nih.gov/19149648/) | 2009 | Review | Med Chem | Bicyclol as a novel dual HBV/HCV agent; adefovir mentioned as an existing HBV-approved comparator drug |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Chronic HBV and HCV treatment review; adefovir listed as HBV treatment option, not HCV |
| [16699274](https://pubmed.ncbi.nlm.nih.gov/16699274/) | 2006 | Review | Dig Dis | Established therapies for HBV (IFN, lamivudine, adefovir) and HCV (IFN + ribavirin) are clearly distinguished as separate treatment domains |
| [16880074](https://pubmed.ncbi.nlm.nih.gov/16880074/) | 2006 | Review | Gastroenterol Clin North Am | HBV pathway to recovery; adefovir discussed as one of several approved HBV antivirals |
| [18221137](https://pubmed.ncbi.nlm.nih.gov/18221137/) | 2006 | Review | Recent Pat Anti-Infect Drug Discov | Pegylated interferons for HBV treatment; adefovir dipivoxil listed as one of five approved HBV drugs |
| [15588803](https://pubmed.ncbi.nlm.nih.gov/15588803/) | 2004 | Review | Best Pract Res Clin Gastroenterol | HBV strategies (IFN-α, lamivudine, adefovir) vs. HCV strategies (IFN + ribavirin) — explicitly separate therapeutic pathways |
| [32289307](https://pubmed.ncbi.nlm.nih.gov/32289307/) | 2020 | Case Report | Am J Med | Hypophosphatemic osteomalacia secondary to adefovir-induced Fanconi syndrome — clinically important renal safety signal for long-term use |

---

## Saudi Arabia Market Information

Adefovir dipivoxil has no current SFDA registrations. The drug is **not marketed in Saudi Arabia**.

For global reference: adefovir dipivoxil is marketed internationally as **Hepsera® 10 mg tablets** (Gilead Sciences), with original FDA approval in September 2002 for the treatment of chronic hepatitis B in adults. It is approved in both HBeAg-positive and HBeAg-negative patients. Several generic formulations are also available in Asian markets.

---

## Safety Considerations

Formal SFDA package insert data (warnings and contraindications) is unavailable for this drug, as it has no Saudi Arabia registration. No drug interaction data was identified in the DDI query. Based on available literature evidence:

- **Renal Tubular Toxicity**: PMID 32289307 documents a confirmed case of hypophosphatemic osteomalacia caused by adefovir-induced Fanconi syndrome following chronic use. This is a recognized class effect of nucleotide phosphonate analogues, particularly significant at higher doses (the HIV-range 60 mg/day dose was abandoned for this reason). Even at the HBV-approved 10 mg/day dose, long-term use requires periodic monitoring of renal function (eGFR) and serum phosphate.

Please refer to the Hepsera international package insert for complete safety information, including precautions in renal impairment, pregnancy (Category C), and pediatric populations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score of 99.97% for chronic HCV infection is a high-confidence false positive generated by disease ontology proximity in the knowledge graph, not mechanistic compatibility. Adefovir dipivoxil's active metabolite inhibits DNA polymerase and reverse transcriptase — enzymes entirely irrelevant to HCV replication, which depends solely on NS5B RNA-dependent RNA polymerase. Every one of the 9 clinical trials and all 15 publications identified are HBV studies; not a single data point demonstrates adefovir activity in any HCV model or patient population. With highly effective pan-genotypic DAA regimens already available for HCV (sofosbuvir, ledipasvir, daclatasvir), there is no unmet need that could justify repurposing investigation here.

**To proceed with any adefovir repurposing program, the following would be needed:**

- Complete MOA data from DrugBank to confirm the exact drug target profile
- Saudi Arabia SFDA registration and package insert to fulfill the safety assessment pre-requisite (currently a blocking data gap)
- If HCV investigation were still desired: in vitro evidence of adefovir activity against HCV NS5B RdRp or any validated HCV replication system, and a credible mechanistic hypothesis beyond DNA polymerase inhibition
- **Alternative and more scientifically grounded paths to consider:** The HBV indication (TxGNN rank 6, Evidence Level L1, "Proceed with Guardrails") represents confirmed efficacy with multiple completed Phase 3 RCTs — if Saudi Arabia market entry is the goal, this established indication is the appropriate starting point; the HIV indication (TxGNN rank 2, Evidence Level L1) has Phase 3 RCT data but was abandoned due to renal toxicity at the required 60 mg dose, and would require a renal safety management plan if revisited
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

