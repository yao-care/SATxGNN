---
layout: default
title: أدلة متوسطة (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "109 دواءً بمستوى الدليل L3–L4 في هذا الموقع (المملكة العربية السعودية)، مثل Acitretin, Alprazolam, Beclomethasone Dipropionate، مع الاستطباب المتوقع الرئيسي ومنتجات مسجلة لدى الهيئة العامة للغذاء والدواء وسجل المراجعة لكل دواء."
---

# أدلة متوسطة (L3-L4)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
تعرض هذه الصفحة **{{ site.data.evidence_tier_facts.medium.count }}** من أصل **{{ site.data.drug_stats.total_drugs }}** دواءً لها تقرير منشور في هذا الموقع ({{ site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L3 **{{ site.data.evidence_tier_facts.medium.by_level.L3 }}**, L4 **{{ site.data.evidence_tier_facts.medium.by_level.L4 }}**.
النسبة الوسيطة للمستويات L3–L4 في مواقع TxGNN الثلاثين: {{ site.data.evidence_tier_facts.medium.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.medium.cross.median_share %}هذا الموقع أعلى من الوسيط.{% elsif ev_share < site.data.evidence_tier_facts.medium.cross.median_share %}هذا الموقع أدنى من الوسيط.{% else %}هذا الموقع عند الوسيط.{% endif %}

{% if site.data.evidence_tier_facts.medium.count > 0 %}
في البيانات المحلية (منتجات مسجلة لدى الهيئة العامة للغذاء والدواء)، لدى **{{ site.data.evidence_tier_facts.medium.with_current }}** من هذه الأدوية منتج واحد على الأقل بحالة «مسجلة»، ولدى **{{ site.data.evidence_tier_facts.medium.none_current }}** منتجات ليس بينها منتج بحالة «مسجلة»، و**{{ site.data.evidence_tier_facts.medium.without_data }}** غير موجودة في البيانات المحلية. لدى **{{ site.data.evidence_tier_facts.medium.with_reviews }}** منها مدخلات في سجل المراجعة (تصحيحات لبيانات التسجيل في صفحة الدواء). لدى **{{ site.data.evidence_tier_facts.medium.cross.unique_drugs }}** منها استطباب متوقع لا يذكره أي موقع آخر من مواقع TxGNN للدواء نفسه.
{% if site.data.evidence_tier_facts.medium.none_current_list.size > 0 %}

لها منتجات وليس بينها منتج بحالة «مسجلة»: {% for r in site.data.evidence_tier_facts.medium.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

تعريف جميع المستويات: [المنهجية]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

### L3 ({{ site.data.evidence_tier_facts.medium.by_level.L3 }} دواء)

<!-- tier-table:start L3（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| الدواء | المستوى | الاستطباب الجديد الرئيسي المتوقع | منتجات مسجلة لدى الهيئة العامة للغذاء والدواء: مسجلة / الإجمالي | سجل المراجعة | في هذا الموقع فقط |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L3" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}نعم ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L4 ({{ site.data.evidence_tier_facts.medium.by_level.L4 }} دواء)

<!-- tier-table:start L4（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| الدواء | المستوى | الاستطباب الجديد الرئيسي المتوقع | منتجات مسجلة لدى الهيئة العامة للغذاء والدواء: مسجلة / الإجمالي | سجل المراجعة | في هذا الموقع فقط |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L4" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}نعم ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>إخلاء المسؤولية</strong><br>
هذا التقرير مخصص للاستخدام المرجعي في البحث الأكاديمي فقط و<strong>لا يشكّل استشارة طبية</strong>. التزم دائمًا بتعليمات طبيبك، ولا تعدّل دواءك من تلقاء نفسك أبدًا. أي قرار يتعلق بإعادة توظيف دواء يتطلب تحققًا سريريًا كاملًا ومراجعة تنظيمية.
<br><br>
<small>روجعت من قِبل: 藥提醒科技有限公司 (yao.care)</small>
</div>
