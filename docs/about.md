---
layout: default
title: نبذة عن المنصة
nav_order: 90
permalink: /about/
description: "SATxGNN منصة للتنبؤ بإعادة توظيف الأدوية طوّرتها 藥提醒科技有限公司 (yao.care)، مبنية على نموذج TxGNN من جامعة هارفارد، وتغطي الأدوية المسجلة لدى SFDA في المملكة العربية السعودية."
---

# نبذة عن المنصة

<div class="key-takeaway">
تسريع التحقق من أدلة إعادة توظيف الأدوية بالذكاء الاصطناعي — من التنبؤ إلى الدليل في لمحة واحدة.
</div>

---

## الخلفية

<p class="key-answer" data-question="ما هي SATxGNN؟">
<strong>SATxGNN</strong> منصة داعمة للبحث في إعادة توظيف الأدوية، مبنية على نموذج TxGNN
المنشور في <em>Nature Medicine</em> من قِبل مختبر Zitnik Lab في جامعة هارفارد. تتنبأ المنصة
بتوسيع دواعي الاستعمال للأدوية المعتمدة من SFDA في المملكة العربية السعودية. وإلى جانب درجات
التنبؤ بالذكاء الاصطناعي، تدمج المنصة الأدلة السريرية من ClinicalTrials.gov وPubMed لتمكين
الباحثين من تقييم مدى موثوقية كل تنبؤ بسرعة.
</p>

---

## عن المطوّر

هذه المنصة مطوَّرة ومُشغَّلة من قِبل **藥提醒科技有限公司** (yao.care، رقم تسجيل الشركة
83620786، الطابق 12، رقم 220، القطاع 2، جادة تايوان، الحي الغربي، مدينة تايتشونغ، تايوان).

SATxGNN هو موقع المملكة العربية السعودية ضمن خط منتجات "TxGNN لإعادة توظيف الأدوية" التابع للشركة.
النظام نفسه منشور في 30 دولة ومنطقة، ويحمل كل موقع اسم `{CC}TxGNN`
(JpTxGNN وUsTxGNN وDETxGNN وهكذا) على العنوان `{cc}txgnn.yao.care`.
نظرة عامة على المنتج: <https://www.yao.care/medical/txgnn/>.

أما نموذج TxGNN نفسه فقد طوّره مختبر Zitnik Lab في Harvard Medical School ونُشر
في *Nature Medicine*. وهذه المنصة هي نظام الإنتاج الذي بنته 藥提醒科技有限公司 فوق ذلك
النموذج، وتشمل دمج بيانات تسجيل الأدوية الوطنية، والتنبؤ المزدوج عبر الرسم البياني المعرفي
والتعلّم العميق، وتصنيف الأدلة من PubMed / ClinicalTrials، وتكامل السجلات الصحية الإلكترونية
عبر SMART on FHIR.

---

## ما هي إعادة توظيف الأدوية؟

<p class="key-answer" data-question="ما هي إعادة توظيف الأدوية؟">
<strong>إعادة توظيف الأدوية</strong> تعني إيجاد استخدامات علاجية جديدة لأدوية موجودة بالفعل.
وبالمقارنة مع تطوير دواء جديد من الصفر — أي 10 إلى 15 عامًا و1&ndash;2 مليار دولار أمريكي —
تستغرق إعادة التوظيف من 3 إلى 5 سنوات وتكلّف 100&ndash;300 مليون دولار أمريكي، كما أن بيانات
السلامة على البشر متوفرة مسبقًا، ما يجعل خطر الإخفاق أقل.
</p>

<table class="comparison-table">
<thead>
<tr><th>الجانب</th><th>تطوير دواء جديد</th><th>إعادة توظيف الأدوية</th></tr>
</thead>
<tbody>
<tr><td>المدة</td><td>10&ndash;15 عامًا</td><td>3&ndash;5 سنوات</td></tr>
<tr><td>التكلفة</td><td>1&ndash;2 مليار دولار أمريكي</td><td>100&ndash;300 مليون دولار أمريكي</td></tr>
<tr><td>بيانات السلامة</td><td>يجب إثباتها من جديد</td><td>بيانات بشرية متوفرة بالفعل</td></tr>
<tr><td>خطر الإخفاق</td><td>مرتفع جدًا (&gt;90%)</td><td>أقل</td></tr>
</tbody>
</table>

---

## ما هو TxGNN؟

<p class="key-answer" data-question="ما هو TxGNN؟">
<a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> نموذج تعلّم عميق
طوّره مختبر Zitnik Lab في Harvard Medical School ونُشر في <em>Nature Medicine</em>.
يتنبأ النموذج بارتباطات جديدة بين الأدوية والأمراض، وهو أول نموذج أساس لإعادة توظيف الأدوية
مصمَّم خصيصًا للأطباء السريريين.
</p>

<blockquote class="expert-quote">
"يدمج TxGNN رسمًا بيانيًا معرفيًا يضم 17,080 كيانًا طبيًا حيويًا، ويستخدم الشبكات العصبية
الرسومية لتعلّم العلاقات المعقدة بين العقد، متنبئًا بالفعالية المحتملة للأدوية ضد الأمراض
النادرة."
<cite>&mdash; Huang et al., Nature Medicine (2023)</cite>
</blockquote>

---

## مصادر البيانات

<table class="comparison-table">
<thead>
<tr><th>النوع</th><th>المصدر</th><th>الوصف</th></tr>
</thead>
<tbody>
<tr><td>التنبؤ بالذكاء الاصطناعي</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>نموذج التنبؤ بالرسم البياني المعرفي من هارفارد</td></tr>
<tr><td>التجارب السريرية</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>السجل العالمي للتجارب السريرية</td></tr>
<tr><td>الأدبيات العلمية</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>قاعدة بيانات الأدبيات الطبية الحيوية</td></tr>
<tr><td>معلومات الأدوية</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>قاعدة بيانات الأدوية والأهداف الدوائية</td></tr>
<tr><td>بيانات التسجيل</td><td><a href="https://www.sfda.gov.sa/">SFDA</a></td><td>بيانات اعتماد الأدوية في المملكة العربية السعودية</td></tr>
</tbody>
</table>

---

## الأساس الأكاديمي

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## النطاق

| البند | القيمة |
|------|-------|
| تقارير الأدوية | {{ site.drugs.size }} |
| الجهة التنظيمية | SFDA |
| المواقع المنشورة | 30 دولة / منطقة |

---

## التواصل

- **GitHub Issues**: <https://github.com/yao-care/SATxGNN/issues>
- **المطوّر**: 藥提醒科技有限公司 (<https://www.yao.care>, service@yao.care)
- **نظرة عامة على المنتج**: <https://www.yao.care/medical/txgnn/>

---

<div class="disclaimer">
<strong>إخلاء المسؤولية</strong><br>
هذا التقرير مخصص للاستخدام المرجعي في البحث الأكاديمي فقط و<strong>لا يشكّل استشارة طبية</strong>. التزم دائمًا بتعليمات طبيبك، ولا تعدّل دواءك من تلقاء نفسك أبدًا. أي قرار يتعلق بإعادة توظيف دواء يتطلب تحققًا سريريًا كاملًا ومراجعة تنظيمية.
<br><br>
<small>روجعت من قِبل: 藥提醒科技有限公司 (yao.care)</small>
</div>
