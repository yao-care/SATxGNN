---
layout: default
title: Norethisterone
parent: 僅模型預測 (L5)
nav_order: 449
evidence_level: L5
indication_count: 1
---

# Norethisterone
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

Using the Evidence Pack as provided (no additional research tools needed — this is a report-authoring task from supplied JSON data). I'll flag where the pack itself has gaps rather than filling them in.

---

# Norethisterone: From an Unregistered Original Indication to Amenorrhea

## One-Sentence Summary

> Norethisterone (DB00717) is a synthetic progestin with no approved indication currently on file for this market (it is not marketed and holds zero authorizations here). The TxGNN model predicts a potential link to **amenorrhea**, with a very high raw prediction score (99.60%), but the underlying evidence is indirect: **8 clinical trials** and **20 publications** were retrieved, and most involve norethisterone as an *add-back component* in combination regimens for heavy menstrual bleeding rather than as a therapy studied directly for amenorrhea as a target disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication is on file (0 licenses registered; `original_indications` is empty in the source data) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.60% (rank 6,720) |
| Evidence Level | L3 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for norethisterone is not available in this evidence pack, and no original approved indication is on record for this market either — so a direct "original indication → new indication" comparison cannot be made from registration data alone.

That said, the evidence pack's own repurposing rationale supplies useful mechanistic context: norethisterone is a synthetic progestin that acts on endometrial progesterone receptors and on the hypothalamic-pituitary-ovarian axis (via negative feedback) to regulate the menstrual cycle. Because that axis directly governs whether menstrual bleeding occurs, there is genuine biological plausibility for a link between norethisterone and amenorrhea (either inducing it therapeutically or being implicated in its pathophysiology).

However, this plausibility comes with an important caveat that the pack itself flags: in five of the eight retrieved trials (the LIBERTY 1, LIBERTY 2, LIBERTY EXTENSION, the withdrawal study, and the MySaturn imaging study), norethindrone/norethisterone acetate is used only as a low-dose "add-back" component alongside relugolix and estradiol, and the disease actually being treated is **heavy menstrual bleeding associated with uterine fibroids** — not amenorrhea itself. In those trials, "amenorrhea rate" is a *secondary efficacy endpoint* signaling that bleeding was successfully suppressed, not the target condition being studied. In the remaining three trials (NCT05620355, NCT01441635, NCT01817530), the actual study drug is **elagolix**, not norethisterone — these were pulled in only because they share the same indication category. Taken together, this means the apparent trial volume overstates how directly the evidence supports norethisterone-for-amenorrhea specifically, which is why the evidence level below is graded L3 rather than higher.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05620355](https://clinicaltrials.gov/study/NCT05620355) | Phase 3 | Unknown | 312 | BG2109 (elagolix-class) alone or with add-back therapy vs. placebo for heavy menstrual bleeding associated with uterine fibroids; norethisterone's role as an intervention is unconfirmed (low relevance). |
| [NCT01441635](https://clinicaltrials.gov/study/NCT01441635) | Phase 2 | Completed | 271 | Proof-of-concept study of elagolix vs. placebo for heavy uterine bleeding and fibroid/uterine volume reduction; study drug is elagolix, not norethisterone. |
| [NCT01817530](https://clinicaltrials.gov/study/NCT01817530) | Phase 2 | Completed | 571 | Elagolix alone or with add-back therapy vs. placebo for heavy menstrual bleeding with uterine fibroids; study drug is elagolix, not norethisterone. |
| [NCT03103087](https://clinicaltrials.gov/study/NCT03103087) (LIBERTY 2) | Phase 3 | Completed | 382 | Relugolix 40mg + estradiol 1mg + norethindrone acetate 0.5mg vs. placebo over 24 weeks for heavy menstrual bleeding with uterine fibroids; amenorrhea rate used as a secondary success endpoint. |
| [NCT03049735](https://clinicaltrials.gov/study/NCT03049735) (LIBERTY 1) | Phase 3 | Completed | 388 | Sister trial to LIBERTY 2, same regimen and design for heavy menstrual bleeding with uterine fibroids. |
| [NCT03751124](https://clinicaltrials.gov/study/NCT03751124) | Phase 3 | Completed | 229 | Randomized withdrawal study evaluating long-term (up to 104 weeks) efficacy/safety of relugolix + estradiol + norethindrone acetate following the LIBERTY parent studies. |
| [NCT06953076](https://clinicaltrials.gov/study/NCT06953076) (MySaturn) | N/A | Recruiting | 111 | Ultrasound assessment of fibroid tissue changes during relugolix + estradiol + norethisterone treatment; imaging endpoints, not amenorrhea as primary outcome. |
| [NCT03412890](https://clinicaltrials.gov/study/NCT03412890) (LIBERTY EXTENSION) | Phase 3 | Completed | 477 | Open-label, single-arm, 28-week extension study of relugolix + estradiol + norethindrone acetate for long-term safety/efficacy in prior LIBERTY participants. |

*Note: None of the above trials studies amenorrhea as the primary target disease with norethisterone as the sole/primary intervention. The three elagolix trials are indication-matched but drug-mismatched; the five relugolix-combination trials use norethisterone only as an add-back component in fibroid/HMB treatment, with amenorrhea appearing as a secondary endpoint.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | RCT | PLoS One | WHICH trial: compared effects of DMPA-IM vs. norethisterone enanthate (NET-EN) injectable contraception on estradiol levels and menstrual, psychological, and behavioral measures. |
| [6786825](https://pubmed.ncbi.nlm.nih.gov/6786825/) | 1981 | Phase I Clinical Trial | Contraception | Phase I trial of norethisterone enanthate and norethisterone acetate in 20 women; recorded amenorrhea, spotting, and other menstrual disorders as outcomes alongside LH/FSH suppression. |
| [37103532](https://pubmed.ncbi.nlm.nih.gov/37103532/) | 2023 | Review | Obstetrics and Gynecology | Overview of oral GnRH antagonists (co-administered with add-back steroids, including norethindrone) for uterine leiomyoma management. |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Cochrane review of combination injectable contraceptives, covering effectiveness and bleeding-pattern side effects. |
| [8313486](https://pubmed.ncbi.nlm.nih.gov/8313486/) | 1993 | Review | Bulletin of the World Health Organization | WHO memorandum reviewing once-a-month injectable estrogen/progestogen contraceptives (Cyclofem, Mesigyna), including efficacy and side effects. |
| [1908716](https://pubmed.ncbi.nlm.nih.gov/1908716/) | 1991 | Review | Current Opinion in Obstetrics & Gynecology | Review of sustained-release subdermal progestin implants as a contraceptive approach. |
| [12222332](https://pubmed.ncbi.nlm.nih.gov/12222332/) | 1991 | Review | Entre Nous (Copenhagen) | Overview of once-a-month estrogen/progestogen injectable contraceptives. |
| [3322079](https://pubmed.ncbi.nlm.nih.gov/3322079/) | 1987 | Review | Akusherstvo i Ginekologiia | Review of prolonged-action contraceptives. |
| [12335903](https://pubmed.ncbi.nlm.nih.gov/12335903/) | 1979 | Review | Contraception, Fertilité, Sexualité | Review discussing endometriosis and infertility. |
| [3659794](https://pubmed.ncbi.nlm.nih.gov/3659794/) | 1987 | Review | La Revue du Praticien | Review of progestational contraception. |

*Note: The retrieved literature set is dominated by older (1970s–1990s) general reviews on hormonal/injectable contraception rather than studies specific to amenorrhea as a treatment target; only the top entries above were prioritized for direct relevance and study rigor.*

---

## Taiwan Market Information

Norethisterone currently holds **0 authorizations** and is **not marketed** in this jurisdiction — there are no license records to report.

---

## Safety Considerations

No key warnings, contraindications, or drug-drug interaction data were returned for this query. Please refer to the package insert for safety information.

*Note: The evidence pack flags the absence of a parsed TFDA package insert as a blocking data gap (DG001) — this must be resolved before a formal safety (S1) evaluation can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the supporting evidence is indirect: most trials use norethisterone as an add-back component for heavy menstrual bleeding/uterine fibroids, with "amenorrhea" appearing only as a secondary treatment-success endpoint rather than the studied disease, and three of the eight trials involve a different drug (elagolix) entirely — consistent with the pack's own L3 evidence grading and "Research Question" (S1) classification. Combined with a blocking safety data gap and zero market presence, this candidate is not yet ready to advance.

**To proceed, the following is needed:**
- Resolve DG001 (blocking): obtain and parse the TFDA/manufacturer package insert for warnings, contraindications, and drug interactions before any safety (S1) evaluation
- Resolve DG002: obtain formal DrugBank mechanism-of-action data to substantiate the mechanistic rationale
- Clarify whether "amenorrhea" in this dataset should be interpreted as the disease to be treated (e.g., secondary amenorrhea) or as a treatment-success endpoint (induced amenorrhea from bleeding suppression) — this materially changes the evidence interpretation
- Confirm norethisterone's actual role and dosing in the three elagolix-associated trials (NCT05620355, NCT01441635, NCT01817530) or exclude them from the evidence base
- If repurposing is pursued, assess the registration pathway given the drug currently has no approved indication or market presence in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

