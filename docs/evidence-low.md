---
layout: default
title: تنبؤ نموذجي فقط (L5)
nav_order: 23
permalink: /evidence-low/
description: "مرشحو المستوى L5 في SATxGNN: تنبؤ نموذجي فقط، دون أي أدلة سريرية أو أدبية حتى الآن."
---

# تنبؤ نموذجي فقط (L5)

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L5 %}
تعرض هذه الصفحة **{{ pd_m }}** من أصل **{{ site.data.drug_stats.total_drugs }}** دواءً لها تقرير منشور في هذا الموقع ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%). تعريف المستويات: [المنهجية]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
مرشحون بتنبؤ نموذجي فقط دون أي أدلة بشرية حتى الآن
</p>

---

## المعايير

| المستوى | التعريف | الدلالة السريرية |
|-------|------------|------------------|
| **L5** | تنبؤ نموذجي فقط | مرحلة الفرضية؛ لا توجد أدلة بشرية بعد |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | sort: "title" %}

### L5 ({{ l5_drugs.size }} دواء)

| الدواء | دواعي الاستعمال | الرابط |
|---------|---------|------|
{% for drug in l5_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [عرض التقرير]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>إخلاء المسؤولية</strong><br>
هذا التقرير مخصص للاستخدام المرجعي في البحث الأكاديمي فقط و<strong>لا يشكّل استشارة طبية</strong>. التزم دائمًا بتعليمات طبيبك، ولا تعدّل دواءك من تلقاء نفسك أبدًا. أي قرار يتعلق بإعادة توظيف دواء يتطلب تحققًا سريريًا كاملًا ومراجعة تنظيمية.
<br><br>
<small>روجعت من قِبل: 藥提醒科技有限公司 (yao.care)</small>
</div>
