---
layout: default
title: أدلة مرتفعة (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "52 دواءً بمستوى الدليل L1–L2 في هذا الموقع (المملكة العربية السعودية)، مثل Acetylcysteine, Bendamustine, Busulfan، مع الاستطباب المتوقع الرئيسي ومنتجات مسجلة لدى الهيئة العامة للغذاء والدواء وسجل المراجعة لكل دواء."
---

# أدلة مرتفعة (L1-L2)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
تعرض هذه الصفحة **{{ site.data.evidence_tier_facts.high.count }}** من أصل **{{ site.data.drug_stats.total_drugs }}** دواءً لها تقرير منشور في هذا الموقع ({{ site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L1 **{{ site.data.evidence_tier_facts.high.by_level.L1 }}**, L2 **{{ site.data.evidence_tier_facts.high.by_level.L2 }}**.
النسبة الوسيطة للمستويات L1–L2 في مواقع TxGNN الثلاثين: {{ site.data.evidence_tier_facts.high.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.high.cross.median_share %}هذا الموقع أعلى من الوسيط.{% elsif ev_share < site.data.evidence_tier_facts.high.cross.median_share %}هذا الموقع أدنى من الوسيط.{% else %}هذا الموقع عند الوسيط.{% endif %}

{% if site.data.evidence_tier_facts.high.count > 0 %}
في البيانات المحلية (منتجات مسجلة لدى الهيئة العامة للغذاء والدواء)، لدى **{{ site.data.evidence_tier_facts.high.with_current }}** من هذه الأدوية منتج واحد على الأقل بحالة «مسجلة»، ولدى **{{ site.data.evidence_tier_facts.high.none_current }}** منتجات ليس بينها منتج بحالة «مسجلة»، و**{{ site.data.evidence_tier_facts.high.without_data }}** غير موجودة في البيانات المحلية. لدى **{{ site.data.evidence_tier_facts.high.with_reviews }}** منها مدخلات في سجل المراجعة (تصحيحات لبيانات التسجيل في صفحة الدواء). لدى **{{ site.data.evidence_tier_facts.high.cross.unique_drugs }}** منها استطباب متوقع لا يذكره أي موقع آخر من مواقع TxGNN للدواء نفسه.
{% if site.data.evidence_tier_facts.high.none_current_list.size > 0 %}

لها منتجات وليس بينها منتج بحالة «مسجلة»: {% for r in site.data.evidence_tier_facts.high.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

تعريف جميع المستويات: [المنهجية]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
مرشحون يمكن إعطاؤهم الأولوية في التقييم السريري
</p>

أيّ هذه الأدوية لديها أدلة من التجارب لاستطبابها الجديد المتوقع، وكم عدد التجارب المسجلة المستشهد بها؟ انظر [الأدوية في السعودية التي لاستطبابها الجديد أدلة من تجارب سريرية]({{ '/clinical-trial-evidence/' | relative_url }}).

---

## المعايير

| المستوى | التعريف | الدلالة السريرية |
|-------|------------|------------------|
| **L1** | تجارب عشوائية محكومة متعددة من المرحلة الثالثة / مراجعات منهجية | دعم قوي؛ يمكن النظر في الاستخدام السريري |
| **L2** | تجربة عشوائية محكومة واحدة أو تجارب متعددة من المرحلة الثانية | دعم متوسط؛ يمكن تصميم تجارب تحقق |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

### L1 ({{ site.data.evidence_tier_facts.high.by_level.L1 }} دواء)

<!-- tier-table:start L1（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| الدواء | المستوى | الاستطباب الجديد الرئيسي المتوقع | منتجات مسجلة لدى الهيئة العامة للغذاء والدواء: مسجلة / الإجمالي | سجل المراجعة | في هذا الموقع فقط |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L1" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}نعم ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L2 ({{ site.data.evidence_tier_facts.high.by_level.L2 }} دواء)

<!-- tier-table:start L2（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| الدواء | المستوى | الاستطباب الجديد الرئيسي المتوقع | منتجات مسجلة لدى الهيئة العامة للغذاء والدواء: مسجلة / الإجمالي | سجل المراجعة | في هذا الموقع فقط |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L2" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}نعم ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>إخلاء المسؤولية</strong><br>
هذا التقرير مخصص للاستخدام المرجعي في البحث الأكاديمي فقط و<strong>لا يشكّل استشارة طبية</strong>. التزم دائمًا بتعليمات طبيبك، ولا تعدّل دواءك من تلقاء نفسك أبدًا. أي قرار يتعلق بإعادة توظيف دواء يتطلب تحققًا سريريًا كاملًا ومراجعة تنظيمية.
<br><br>
<small>روجعت من قِبل: 藥提醒科技有限公司 (yao.care)</small>
</div>
