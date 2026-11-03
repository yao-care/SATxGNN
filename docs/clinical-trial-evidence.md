---
layout: default
title: "أدوية لاستطبابها الجديد أدلة من تجارب سريرية"
nav_order: 25
permalink: /clinical-trial-evidence/
description: "الأدوية المسجلة لدى SFDA التي لاستطبابها الجديد الذي تنبأ به TxGNN أدلة من تجارب سريرية (L1-L2): الاستطباب ومستوى الأدلة وعدد التجارب المسجلة."
last_modified_at: 2026-11-03
---
{%- comment -%}
2026-11-03：回答 AI 搜尋常問的「本國藥物中，哪些新適應症有臨床試驗證據」。全表由 Liquid 從藥物頁產生，不寫死藥名或數字。
收錄＝公開藥物頁（排除 id_redirect 與 noindex）中 evidence_level 為 L1 或 L2（本站 evidence-high 標準：L1 多個 Phase 3 RCT／系統性回顧，
L2 單一 RCT 或多個 Phase 2 試驗）。預測新適應症與等級註記取自各藥物頁快速總覽表；下列欄名是本站藥物頁實際用到的寫法（建頁時逐頁核對），
新寫法抓不到時顯示「انظر التقرير」、等級仍取 front matter。試驗數＝該藥物頁引用的不重複 NCT 編號數。
{%- endcomment -%}
{%- assign ind_labels = "الاستطباب الجديد المتوقع|الاستطباب الجديد المتنبأ به|المؤشر الجديد المتنبأ به|المؤشر الجديد المتوقع" | split: "|" -%}
{%- assign lev_labels = "مستوى الأدلة|مستوى الدليل" | split: "|" -%}
{%- assign listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign l1 = listed | where: "evidence_level", "L1" | sort: "title" -%}
{%- assign l2 = listed | where: "evidence_level", "L2" | sort: "title" -%}
{%- assign trial_drugs = l1 | concat: l2 -%}
{%- assign latest = trial_drugs | sort: "last_modified_at" | last -%}
{%- assign latest_date = latest.last_modified_at | date: "%Y-%m-%d" -%}

# الأدوية في السعودية التي لاستطبابها الجديد أدلة من تجارب سريرية

<p class="key-answer" data-question="ما الأدوية في السعودية التي لديها أدلة من تجارب سريرية لاستطباب جديد؟">
من بين {{ listed.size }} دواءً لها تقرير في SATxGNN، هناك <strong>{{ trial_drugs.size }}</strong> دواءً لها استطباب جديد تنبّأ به TxGNN بمستوى أدلة <strong>L1 أو L2</strong> ({{ l1.size }} في L1 و{{ l2.size }} في L2)، أي أنه وُجدت أدلة من تجارب سريرية (تجارب عشوائية محكومة أو تجارب من المرحلة 2–3 أو مراجعات منهجية).
</p>

مصدر الأدوية هو بيانات التسجيل لدى [الهيئة العامة للغذاء والدواء (SFDA)](https://www.sfda.gov.sa/en/open-data) (قائمة الأدوية البشرية المسجلة في المملكة العربية السعودية)؛ وتعكس القائمة تقارير الأدوية كما حُدّثت آخر مرة في {{ latest_date }}.

<div class="key-takeaway">
وجود أدلة من التجارب لاستطباب متوقع لا يثبت الفعالية. لا يزال كل مرشح أدناه <strong>يتطلب التحقق السريري</strong> والمراجعة التنظيمية قبل أي استخدام سريري.
</div>

---

## الأدوية التي لديها أدلة من التجارب (L1–L2)

<div class="table-wrapper"><table>
<thead>
<tr><th>الدواء</th><th>الاستطباب الجديد المتوقع</th><th>مستوى الأدلة</th><th>التجارب المسجلة المستشهد بها (NCT)</th></tr>
</thead>
<tbody>
{%- for drug in trial_drugs -%}
{%- assign indication = "" -%}
{%- for lab in ind_labels -%}{%- if indication == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign qo = drug.content | split: needle -%}{%- if qo.size > 1 -%}{%- assign indication = qo[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign level_cell = "" -%}
{%- for lab in lev_labels -%}{%- if level_cell == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign lv = drug.content | split: needle -%}{%- if lv.size > 1 -%}{%- assign level_cell = lv[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign parts = drug.content | split: "NCT" -%}
{%- capture nct_ids -%}{%- for p in parts offset: 1 -%}{%- assign id = p | slice: 0, 8 -%}{%- assign rest = id | remove: "0" | remove: "1" | remove: "2" | remove: "3" | remove: "4" | remove: "5" | remove: "6" | remove: "7" | remove: "8" | remove: "9" -%}{%- if id.size == 8 and rest == "" -%}{{ id }},{%- endif -%}{%- endfor -%}{%- endcapture -%}
{%- assign nct_count = nct_ids | split: "," | uniq | size %}
<tr><td><a href="{{ drug.url | relative_url }}">{{ drug.title }}</a></td><td>{% if indication != "" %}{{ indication }}{% else %}انظر التقرير{% endif %}</td><td>{{ drug.evidence_level }}{% if level_cell != "" and level_cell != drug.evidence_level %} <a href="{{ drug.url | relative_url }}" title="{{ level_cell | strip_html | escape }}">(مع تحفّظ)</a>{% endif %}</td><td>{{ nct_count }}</td></tr>
{%- endfor %}
</tbody>
</table></div>

## كيف تقرأ هذه القائمة

- **مستوى الأدلة** يتبع [معايير]({{ '/evidence-high/' | relative_url }}) الموقع: L1 = تجارب عشوائية محكومة متعددة من المرحلة الثالثة / مراجعات منهجية؛ L2 = تجربة عشوائية محكومة واحدة أو تجارب متعددة من المرحلة الثانية. وتعني «(مع تحفّظ)» أن التقرير يضع تحفّظاً على المستوى؛ اقرأ الملاحظة في التقرير قبل الاعتماد عليه.
- **الاستطباب الجديد المتوقع** هو التنبؤ الرئيسي في كل تقرير. تُستبعد الاستطبابات وموانع الاستعمال المسجلة مسبقاً في الرسم البياني المعرفي لـ TxGNN، لكن قد يتداخل بعض التنبؤات مع استخدام قائم؛ ويوضح التقرير ذلك عند الاقتضاء.
- **التجارب المسجلة المستشهد بها** هي عدد أرقام ClinicalTrials.gov (NCT) المستشهد بها في التقرير. تستشهد التقارير بمجموعة مختارة من التجارب التي عُثر عليها؛ ويعني 0 أن التقرير لا يستشهد بأي تجربة مسجلة، ويبيّن قسم أدلة الأدبيات أساس المستوى.
- لجميع المستويات والمنهجية الكاملة، انظر [أدلة مرتفعة (L1-L2)]({{ '/evidence-high/' | relative_url }}) و[جميع الأدوية]({{ '/drugs/' | relative_url }}) و[المنهجية]({{ '/methodology/' | relative_url }}).

---

<div class="disclaimer">
<strong>إخلاء المسؤولية</strong><br>
هذا التقرير مخصص للاستخدام المرجعي في البحث الأكاديمي فقط و<strong>لا يشكّل استشارة طبية</strong>. التزم دائمًا بتعليمات طبيبك، ولا تعدّل دواءك من تلقاء نفسك أبدًا. أي قرار يتعلق بإعادة توظيف دواء يتطلب تحققًا سريريًا كاملًا ومراجعة تنظيمية.
<br><br>
<small>روجعت من قِبل: 藥提醒科技有限公司 (yao.care)</small>
</div>
