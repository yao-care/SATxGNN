---
layout: default
title: توقعات إعادة توظيف الأدوية
nav_order: 1
description: "توقعات مدعومة بالذكاء الاصطناعي لإعادة توظيف الأدوية في المملكة العربية السعودية. تحليل قائم على الأدلة للأدوية المعتمدة بحثًا عن استطبابات علاجية جديدة محتملة."
permalink: /
---

# توقعات إعادة توظيف الأدوية — المملكة العربية السعودية

يستخدم هذا المشروع الشبكة العصبية البيانية TxGNN للتنبؤ باستخدامات علاجية جديدة محتملة للأدوية المعتمدة في المملكة العربية السعودية.

**إخلاء المسؤولية**: هذا المحتوى مخصص لأغراض البحث فقط ولا يشكّل استشارة طبية. تتطلب جميع تنبؤات إعادة توظيف الأدوية تحققًا سريريًا قبل التطبيق.

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## المملكة العربية السعودية: نطاق هذا الموقع

ينشر هذا الموقع تقارير عن **{{ site.data.drug_stats.total_drugs }}** دواءً واردًا في بيانات التسجيل لدى [SFDA](https://www.sfda.gov.sa/) (المملكة العربية السعودية).

### بيانات الأدوية في المملكة العربية السعودية

| البند | التفاصيل |
|------|--------|
| مجموعة البيانات | قائمة الأدوية البشرية المسجلة (المحلية وغير المحلية، ملفا Excel، إصدار 2023) ضمن البيانات المفتوحة للهيئة |
| الناشر | الهيئة العامة للغذاء والدواء (SFDA) |
| التنزيل | <https://www.sfda.gov.sa/en/open-data> |
| طبيعة البيانات | قائمة بالأدوية المسجلة فقط، دون أرقام تراخيص ودون حقل لحالة التسجيل |
| التحديث | يُعاد تنزيل القائمة كل يوم اثنين عبر سير عمل آلي؛ وإذا نشرت الهيئة على الصفحة قائمة أحدث للأدوية البشرية تُستخدم تلقائيًا |

التفاصيل: [مصادر البيانات]({{ '/sources/' | relative_url }}).

التقارير حسب مستوى الدليل:

| مستوى الدليل | التقارير | النسبة |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

62 من أزواج الدواء والمرض المتوقعة في هذا الموقع لا تظهر في أي موقع آخر من مواقع TxGNN الثلاثين.

### الأدوية ذات أعلى مستوى دليل في هذا الموقع

| الدواء | مستوى الدليل |
|---|---|
| [Acetylcysteine](/drugs/acetylcysteine/) | L1 |
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Grazoprevir](/drugs/grazoprevir/) | L1 |
| [Peginterferon Alfa-2A](/drugs/peginterferon-alfa-2a/) | L1 |
| [Ribavirin](/drugs/ribavirin/) | L1 |
| [Clofarabine](/drugs/clofarabine/) | L1 |
| [Clomipramine](/drugs/clomipramine/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |
| [Peginterferon Alfa-2B](/drugs/peginterferon-alfa-2b/) | L1 |

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

هذه المنصة مطوَّرة ومُشغَّلة من قِبل **藥提醒科技有限公司** (yao.care). راجع صفحة
<a href="{{ '/about/' | relative_url }}">نبذة عن المنصة</a> للاطلاع على التعريف الكامل بالشركة وخلفية المنهجية.
