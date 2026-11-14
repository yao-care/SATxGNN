---
layout: default
title: دليل المستخدم
nav_order: 92
permalink: /guide/
description: "دليل استخدام SATxGNN: كيفية البحث عن الأدوية، وقراءة مستويات الأدلة، وتفسير التوصيات."
---

# دليل المستخدم

<div class="key-takeaway">
تحقق من مستوى الدليل أولًا، ثم من التوصية، ثم اقرأ الأدبيات المصدرية.
</div>

---

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## المملكة العربية السعودية: بيانات هذا الموقع

ينشر هذا الموقع تقارير عن **{{ site.data.drug_stats.total_drugs }}** دواءً واردًا في بيانات التسجيل لدى [SFDA](https://www.sfda.gov.sa/) (المملكة العربية السعودية).

مجموعة البيانات: [SFDA Open Data](https://www.sfda.gov.sa/en/open-data)؛ تُنزَّل وتُقارَن تلقائيًا كل أسبوع (يوم الاثنين). التفاصيل: [مصادر البيانات]({{ '/sources/' | relative_url }}).

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

<!-- site-data:end -->

## البحث عن دواء

<ol class="actionable-steps">
<li>استخدم مربع البحث أعلى الصفحة (أسماء المكونات الفعالة تعطي نتائج أدق من الأسماء التجارية).</li>
<li>أو تصفّح القائمة الكاملة في <a href="{{ '/drugs/' | relative_url }}">جميع الأدوية</a>.</li>
<li>يمكنك أيضًا التصفح حسب مستوى الدليل: <a href="{{ '/evidence-high/' | relative_url }}">مرتفع</a>، <a href="{{ '/evidence-medium/' | relative_url }}">متوسط</a>، <a href="{{ '/evidence-low/' | relative_url }}">تنبؤ نموذجي فقط</a>.</li>
</ol>

---

## قراءة التقرير

<p class="key-answer" data-question="ماذا تعني مستويات الأدلة من L1 إلى L5؟">
يسرد كل تقرير دواء دواعي الاستعمال الجديدة المتنبَّأ بها، ويحمل كل داعٍ منها مستوى دليل من
L1 إلى L5. <strong>يعني L1 أن تجارب عشوائية محكومة متعددة من المرحلة الثالثة تدعمه بالفعل؛
أما L5 فيعني تنبؤًا نموذجيًا فقط دون أي دليل بشري.</strong> المعايير الكاملة متاحة في صفحة
<a href="{{ '/methodology/' | relative_url }}">المنهجية</a>.
</p>

| إذا رأيت | فهذا يعني | الإجراء المقترح |
|-----------|----------|------------------|
| L1 / L2 | توجد أدلة من تجارب سريرية | راجع سجلات NCT وPMID المصدرية |
| L3 / L4 | أدلة رصدية أو ما قبل سريرية | تعامل معه كمسار بحثي |
| L5 | تنبؤ نموذجي فقط | لتوليد الفرضيات فقط؛ ليس مرجعًا سريريًا |

---

## الاستشهاد وإمكانية التتبع

كل دليل يرد في التقرير يحمل معرّفًا قابلًا للتتبع:

- **رقم NCT**: يربط بتسجيل الدراسة في ClinicalTrials.gov
- **PMID**: يربط بسجل PubMed
- **معرّف DrugBank**: يربط ببيانات الدواء والأهداف الدوائية

يُرجى قراءة الأدبيات المصدرية للتأكد من السياق قبل الاستشهاد بأي استنتاج من هذه المنصة.

---

## الأسئلة الشائعة

<p class="key-answer" data-question="هل يمكن استخدام التنبؤات سريريًا؟">
<strong>لا.</strong> التنبؤات في هذه المنصة مسارات بحثية وليست استشارة سريرية. وأي تطبيق
سريري لإعادة توظيف دواء يجب أن يمر بتحقق كامل عبر التجارب السريرية ومراجعة تنظيمية.
</p>

<p class="key-answer" data-question="لماذا لا أجد دواءً معينًا؟">
يجب أن يكون المكوّن قابلًا للربط بمفردات DrugBank ليُدرج في التنبؤ. أما المستخلصات العشبية
واللقاحات والسواغات وغيرها مما لا تفهرسه DrugBank فلا تظهر في هذه المنصة.
</p>

---

## عن المطوّر

هذه المنصة مطوَّرة ومُشغَّلة من قِبل **藥提醒科技有限公司** (yao.care). راجع صفحة
<a href="{{ '/about/' | relative_url }}">نبذة عن المنصة</a> للاطلاع على التعريف الكامل بالشركة وخلفية المنهجية.

---

<div class="disclaimer">
<strong>إخلاء المسؤولية</strong><br>
هذا التقرير مخصص للاستخدام المرجعي في البحث الأكاديمي فقط و<strong>لا يشكّل استشارة طبية</strong>. التزم دائمًا بتعليمات طبيبك، ولا تعدّل دواءك من تلقاء نفسك أبدًا. أي قرار يتعلق بإعادة توظيف دواء يتطلب تحققًا سريريًا كاملًا ومراجعة تنظيمية.
<br><br>
<small>روجعت من قِبل: 藥提醒科技有限公司 (yao.care)</small>
</div>
