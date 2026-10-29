---
layout: default
title: توقعات إعادة توظيف الأدوية
nav_order: 1
description: "توقعات مدعومة بالذكاء الاصطناعي لإعادة توظيف الأدوية في المملكة العربية السعودية. تحليل قائم على الأدلة للأدوية المعتمدة بحثًا عن استطبابات علاجية جديدة محتملة."
permalink: /
---

# توقعات إعادة توظيف الأدوية — المملكة العربية السعودية

This project uses the TxGNN graph neural network to predict potential new therapeutic uses for medicines approved in Saudi Arabia.

**Disclaimer**: This content is for research purposes only and does not constitute medical advice. All drug repurposing predictions require clinical validation before application.

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## المملكة العربية السعودية: نطاق هذا الموقع

ينشر هذا الموقع تقارير عن **{{ site.data.drug_stats.total_drugs }}** دواءً واردًا في بيانات التسجيل لدى [SFDA](https://www.sfda.gov.sa/) (المملكة العربية السعودية).

التقارير حسب مستوى الدليل: L1 {{ site.data.drug_stats.level_counts.L1 }} · L2 {{ site.data.drug_stats.level_counts.L2 }} · L3 {{ site.data.drug_stats.level_counts.L3 }} · L4 {{ site.data.drug_stats.level_counts.L4 }} · L5 {{ site.data.drug_stats.level_counts.L5 }}

### الأدوية ذات أعلى مستوى دليل في هذا الموقع

| الدواء | مستوى الدليل |
|---|---|
| [Acetylcysteine](/drugs/acetylcysteine/) | L1 |
| [Acyclovir](/drugs/acyclovir/) | L1 |
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Glecaprevir](/drugs/glecaprevir/) | L1 |
| [Grazoprevir](/drugs/grazoprevir/) | L1 |
| [Hyaluronic Acid](/drugs/hyaluronic-acid/) | L1 |
| [Lanadelumab](/drugs/lanadelumab/) | L1 |
| [Natamycin](/drugs/natamycin/) | L1 |
| [Triptorelin](/drugs/triptorelin/) | L1 |

### الأدوية التي لا يغطيها سوى هذا الموقع من بين مواقع TxGNN الثلاثين

| الدواء | مستوى الدليل |
|---|---|
| [Potassium Gluconate](/drugs/potassium-gluconate/) | L4 |
| [Enoxacin](/drugs/enoxacin/) | L5 |
| [Olaratumab](/drugs/olaratumab/) | L5 |
| [Simeprevir](/drugs/simeprevir/) | L5 |
| [Telaprevir](/drugs/telaprevir/) | L5 |
| [Antihemophilic Factor Human Recombinant](/drugs/antihemophilic-factor-human-recombinant/) | L5 |
| [Aluminum Acetate](/drugs/aluminum-acetate/) | L5 |
| [Zalcitabine](/drugs/zalcitabine/) | L5 |
| [Alclometasone](/drugs/alclometasone/) | L5 |
| [Chlorphenoxamine](/drugs/chlorphenoxamine/) | L5 |
| [Tubocurarine](/drugs/tubocurarine/) | L5 |
| [Befunolol](/drugs/befunolol/) | N/A |
| [Lisuride](/drugs/lisuride/) | N/A |

<!-- local-home:end -->

## عن المطوّر

هذه المنصة مطوَّرة ومُشغَّلة من قِبل **藥提醒科技有限公司** (yao.care، رقم تسجيل الشركة
83620786، الطابق 12، رقم 220، القطاع 2، جادة تايوان، الحي الغربي، مدينة تايتشونغ، تايوان).

SATxGNN هو موقع المملكة العربية السعودية ضمن خط منتجات "TxGNN لإعادة توظيف الأدوية" التابع للشركة.
النظام نفسه منشور في 30 دولة ومنطقة، ويحمل كل موقع اسم `{CC}TxGNN`
(JpTxGNN وUsTxGNN وDETxGNN وهكذا) على العنوان `{cc}txgnn.yao.care`.
نظرة عامة على المنتج: <https://www.yao.care/medical/txgnn/>.

أما نموذج TxGNN نفسه فقد طوّره مختبر Zitnik Lab في Harvard Medical School ونُشر
في *Nature Medicine*. وهذه المنصة هي نظام الإنتاج الذي بنته 藥提醒科技有限公司 فوق ذلك
النموذج، وتشمل دمج بيانات تسجيل الأدوية الوطنية، والتنبؤ بالتعلّم العميق مع استبعاد الاستخدامات المسجّلة مسبقًا في الرسم البياني المعرفي، وتصنيف الأدلة من PubMed / ClinicalTrials، وتكامل السجلات الصحية الإلكترونية
عبر SMART on FHIR.
