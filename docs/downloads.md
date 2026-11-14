---
layout: default
title: التنزيلات
nav_order: 94
permalink: /downloads/
description: "تنزيلات البيانات المفتوحة في SATxGNN: موارد FHIR، ونتائج التنبؤ، وفهرس البحث."
---

# التنزيلات

<div class="key-takeaway">
تُنشر التنبؤات بصيغة FHIR R4، جاهزة للتكامل مع أنظمة السجلات الصحية الإلكترونية.
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

## موارد FHIR

ينشر هذا الموقع التنبؤات كموارد FHIR R4 يمكن لتطبيقات SMART on FHIR استهلاكها مباشرة:

| المورد | المسار | الوصف |
|----------|------|-------------|
| CapabilityStatement | `/fhir/metadata` | بيان قدرات خادم FHIR |
| MedicationKnowledge | `/fhir/MedicationKnowledge/` | موارد الأدوية |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/` | دواعي الاستعمال المتنبَّأ بها |
| Bundle | `/fhir/Bundle/all-predictions.json` | جميع التنبؤات في حزمة واحدة |

---

## فهرس البحث

يوفر الملف `/data/search-index.json` فهرس بحث للأدوية ودواعي الاستعمال لبناء واجهة استعلام
خاصة بك.

---

## شروط الاستخدام

<ol class="actionable-steps">
<li>بيانات هذا الموقع <strong>للاستخدام المرجعي في البحث فقط</strong> ويجب ألا تُتخذ أساسًا لأي قرار طبي.</li>
<li>عند الاستشهاد، انسب العمل إلى SATxGNN (藥提醒科技有限公司) واستشهد بورقة TxGNN الأصلية.</li>
<li>تبقى البيانات المشتقة خاضعة لشروط ترخيص كل مصدر أصلي (انظر <a href="{{ '/sources/' | relative_url }}">مصادر البيانات</a>).</li>
</ol>

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
