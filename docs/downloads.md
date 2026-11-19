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

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## المملكة العربية السعودية: محتوى الملفات حاليًا

| الملف | المحتوى الحالي |
|---|---|
| `/data/search-index.json` | {{ site.data.local_facts.files.search_index }} دواءً مع استطباباتها المتوقعة |
| `/data/drugs.json` | {{ site.data.local_facts.files.drugs_json }} دواءً مع مستوى الدليل والاستطباب الأصلي |
| `/fhir/MedicationKnowledge/` | {{ site.data.local_facts.fhir.medication_knowledge }} من موارد MedicationKnowledge (واحد لكل دواء) |
| `/fhir/ClinicalUseDefinition/` | {{ site.data.local_facts.fhir.clinical_use_definition }} من موارد ClinicalUseDefinition (واحد لكل استطباب متوقع) |

إعادة استخدام مجموعة البيانات المحلية: [SFDA Open Data](https://www.sfda.gov.sa/en/open-data), تنشرها الهيئة العامة للغذاء والدواء؛ وتخضع إعادة استخدامها لشروط الجهة الناشرة، ولا يمنح هذا الموقع أي حقوق إضافية.

{% if site.data.local_facts.top_licensed.size > 0 %}الأدوية ذات أكبر عدد من منتجات مسجلة لدى الهيئة العامة للغذاء والدواء بحالة «مسجلة»: {% for r in site.data.local_facts.top_licensed limit: 5 offset: 3 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.lv }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}أحدث التصحيحات في سجل المراجعة: {% for r in site.data.local_facts.recent_reviews limit: 8 offset: 16 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

<!-- local-facts:end -->

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
