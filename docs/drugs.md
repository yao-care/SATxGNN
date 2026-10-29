---
layout: default
title: جميع الأدوية
nav_order: 20
permalink: /drugs/
description: "جميع تقارير التحقق من الأدوية وإحصاءات مستويات الأدلة في SATxGNN."
---
{%- comment -%}2026-10-27 build gate：站上各頁的藥物數讀 site.data.drug_stats；它和實際公開藥物頁數／等級分布不一致時，
故意 include 不存在的檔讓 Jekyll 建置失敗，錯誤訊息即修法。{%- endcomment -%}
{%- assign gate_listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign gate_ds = site.data.drug_stats -%}
{%- assign gate_l1 = gate_listed | where: "evidence_level", "L1" | size -%}
{%- assign gate_l2 = gate_listed | where: "evidence_level", "L2" | size -%}
{%- assign gate_l3 = gate_listed | where: "evidence_level", "L3" | size -%}
{%- assign gate_l4 = gate_listed | where: "evidence_level", "L4" | size -%}
{%- assign gate_l5 = gate_listed | where: "evidence_level", "L5" | size -%}
{%- if gate_listed.size != gate_ds.total_drugs or gate_l1 != gate_ds.level_counts.L1 or gate_l2 != gate_ds.level_counts.L2 or gate_l3 != gate_ds.level_counts.L3 or gate_l4 != gate_ds.level_counts.L4 or gate_l5 != gate_ds.level_counts.L5 -%}
{% include ERROR-docs-data-drug_stats-json-out-of-sync--run-python3-scripts-generate_drug_stats-py.html %}
{%- endif %}
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

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
تستند هذه القائمة إلى بيانات التسجيل لدى [SFDA](https://www.sfda.gov.sa/) (المملكة العربية السعودية).

<!-- local-home:end -->

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
