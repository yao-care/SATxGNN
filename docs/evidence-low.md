---
layout: default
title: تنبؤ نموذجي فقط (L5)
nav_order: 23
permalink: /evidence-low/
description: "692 دواءً بمستوى الدليل L5 في هذا الموقع (المملكة العربية السعودية)، مثل Amoxicillin, Atenolol, Ceftriaxone، مع الاستطباب المتوقع الرئيسي ومنتجات مسجلة لدى الهيئة العامة للغذاء والدواء وسجل المراجعة لكل دواء."
---

# تنبؤ نموذجي فقط (L5)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
تعرض هذه الصفحة **{{ site.data.evidence_tier_facts.low.count }}** من أصل **{{ site.data.drug_stats.total_drugs }}** دواءً لها تقرير منشور في هذا الموقع ({{ site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L5 **{{ site.data.evidence_tier_facts.low.by_level.L5 }}**.
النسبة الوسيطة للمستويات L5 في مواقع TxGNN الثلاثين: {{ site.data.evidence_tier_facts.low.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.low.cross.median_share %}هذا الموقع أعلى من الوسيط.{% elsif ev_share < site.data.evidence_tier_facts.low.cross.median_share %}هذا الموقع أدنى من الوسيط.{% else %}هذا الموقع عند الوسيط.{% endif %}

{% if site.data.evidence_tier_facts.low.count > 0 %}
في البيانات المحلية (منتجات مسجلة لدى الهيئة العامة للغذاء والدواء)، لدى **{{ site.data.evidence_tier_facts.low.with_current }}** من هذه الأدوية منتج واحد على الأقل بحالة «مسجلة»، ولدى **{{ site.data.evidence_tier_facts.low.none_current }}** منتجات ليس بينها منتج بحالة «مسجلة»، و**{{ site.data.evidence_tier_facts.low.without_data }}** غير موجودة في البيانات المحلية. لدى **{{ site.data.evidence_tier_facts.low.with_reviews }}** منها مدخلات في سجل المراجعة (تصحيحات لبيانات التسجيل في صفحة الدواء). لدى **{{ site.data.evidence_tier_facts.low.cross.unique_drugs }}** منها استطباب متوقع لا يذكره أي موقع آخر من مواقع TxGNN للدواء نفسه.
{% if site.data.evidence_tier_facts.low.none_current_list.size > 0 %}

لها منتجات وليس بينها منتج بحالة «مسجلة»: {% for r in site.data.evidence_tier_facts.low.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}

تُعرض أولًا الأدوية التي لها منتج محلي بحالة «مسجلة».
{% endif %}

تعريف جميع المستويات: [المنهجية]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

### L5 ({{ site.data.evidence_tier_facts.low.by_level.L5 }} دواء)

<!-- tier-table:start L5（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| الدواء | المستوى | الاستطباب الجديد الرئيسي المتوقع | منتجات مسجلة لدى الهيئة العامة للغذاء والدواء: مسجلة / الإجمالي | سجل المراجعة | في هذا الموقع فقط |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.low.rows %}{% if r.l == "L5" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}نعم ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>إخلاء المسؤولية</strong><br>
هذا التقرير مخصص للاستخدام المرجعي في البحث الأكاديمي فقط و<strong>لا يشكّل استشارة طبية</strong>. التزم دائمًا بتعليمات طبيبك، ولا تعدّل دواءك من تلقاء نفسك أبدًا. أي قرار يتعلق بإعادة توظيف دواء يتطلب تحققًا سريريًا كاملًا ومراجعة تنظيمية.
<br><br>
<small>روجعت من قِبل: 藥提醒科技有限公司 (yao.care)</small>
</div>
