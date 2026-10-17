---
layout: default
title: جميع الأدوية
nav_order: 20
permalink: /drugs/
description: "جميع تقارير التحقق من الأدوية وإحصاءات مستويات الأدلة في SATxGNN."
---
{%- comment -%}2026-10-16：列表不含舊 ID 轉址頁與 noindex 頁{%- endcomment -%}
{% assign listed_drugs = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" %}
{% assign l1_count = listed_drugs | where: "evidence_level", "L1" | size %}
{% assign l2_count = listed_drugs | where: "evidence_level", "L2" | size %}
{% assign l3_count = listed_drugs | where: "evidence_level", "L3" | size %}
{% assign l4_count = listed_drugs | where: "evidence_level", "L4" | size %}
{% assign l5_count = listed_drugs | where: "evidence_level", "L5" | size %}

# جميع الأدوية

{{ listed_drugs.size }} تقرير تحقق من الأدوية

---

## توزيع مستويات الأدلة

| مستوى الدليل | الأدوية | الوصف |
|---------|--------|------|
| **L1** | {{ l1_count }} | تجارب عشوائية محكومة متعددة / مراجعات منهجية |
| **L2** | {{ l2_count }} | تجربة عشوائية محكومة واحدة / تجارب المرحلة الثانية |
| **L3** | {{ l3_count }} | دراسات رصدية / سلاسل حالات كبيرة |
| **L4** | {{ l4_count }} | دراسات ما قبل سريرية / دراسات آليات التأثير |
| **L5** | {{ l5_count }} | تنبؤ نموذجي فقط |

---

## قائمة الأدوية الكاملة

{% assign all_drugs = listed_drugs | sort: 'title' %}

| الدواء | مستوى الدليل | دواعي الاستعمال |
|---------|---------|---------|
{% for drug in all_drugs %}| [{{ drug.title }}]({{ drug.url | relative_url }}) | {{ drug.evidence_level }} | {{ drug.indication_count }} |
{% endfor %}

---

<div class="disclaimer">
<strong>إخلاء المسؤولية</strong><br>
هذا التقرير مخصص للاستخدام المرجعي في البحث الأكاديمي فقط و<strong>لا يشكّل استشارة طبية</strong>. التزم دائمًا بتعليمات طبيبك، ولا تعدّل دواءك من تلقاء نفسك أبدًا. أي قرار يتعلق بإعادة توظيف دواء يتطلب تحققًا سريريًا كاملًا ومراجعة تنظيمية.
<br><br>
<small>روجعت من قِبل: 藥提醒科技有限公司 (yao.care)</small>
</div>
