---
layout: default
title: أدلة متوسطة (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "مرشحو إعادة توظيف الأدوية من المستويين L3-L4 في SATxGNN، المدعومون بأدلة رصدية أو ما قبل سريرية."
---

# أدلة متوسطة (L3-L4)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
مرشحون بأدلة أولية تحتاج إلى مزيد من التحقق
</p>

---

## المعايير

| المستوى | التعريف | الدلالة السريرية |
|-------|------------|------------------|
| **L3** | دراسات رصدية / سلاسل حالات كبيرة | دعم أولي؛ يحتاج إلى تحقق إضافي |
| **L4** | دراسات ما قبل سريرية / دراسات آليات التأثير | دعم نظري؛ بعيد عن الاستخدام السريري |

---

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | sort: "title" %}

### L3 ({{ l3_drugs.size }} دواء)

| الدواء | دواعي الاستعمال | الرابط |
|---------|---------|------|
{% for drug in l3_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [عرض التقرير]({{ drug.url | relative_url }}) |
{% endfor %}

### L4 ({{ l4_drugs.size }} دواء)

| الدواء | دواعي الاستعمال | الرابط |
|---------|---------|------|
{% for drug in l4_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [عرض التقرير]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>إخلاء المسؤولية</strong><br>
هذا التقرير مخصص للاستخدام المرجعي في البحث الأكاديمي فقط و<strong>لا يشكّل استشارة طبية</strong>. التزم دائمًا بتعليمات طبيبك، ولا تعدّل دواءك من تلقاء نفسك أبدًا. أي قرار يتعلق بإعادة توظيف دواء يتطلب تحققًا سريريًا كاملًا ومراجعة تنظيمية.
<br><br>
<small>روجعت من قِبل: 藥提醒科技有限公司 (yao.care)</small>
</div>
