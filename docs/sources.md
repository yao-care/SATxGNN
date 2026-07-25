---
layout: default
title: مصادر البيانات
nav_order: 93
permalink: /sources/
description: "مصادر البيانات التي تقوم عليها SATxGNN: بيانات تسجيل SFDA، وTxGNN، وClinicalTrials.gov، وPubMed، وDrugBank."
---

# مصادر البيانات

<div class="key-takeaway">
كل استنتاج يعود إلى مصدر بيانات عام — لا شيء هنا صندوق أسود.
</div>

---

## نظرة عامة على المصادر

<table class="comparison-table">
<thead>
<tr><th>النوع</th><th>المصدر</th><th>الاستخدام</th></tr>
</thead>
<tbody>
<tr><td>بيانات التسجيل</td><td><a href="https://www.sfda.gov.sa/">SFDA</a></td><td>قائمة الأدوية المعتمدة ومكوناتها في المملكة العربية السعودية</td></tr>
<tr><td>نموذج التنبؤ</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>التنبؤ بالارتباط بين الأدوية والأمراض</td></tr>
<tr><td>التجارب السريرية</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>تصنيف الأدلة (NCT)</td></tr>
<tr><td>الأدبيات العلمية</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>تصنيف الأدلة (PMID)</td></tr>
<tr><td>معلومات الأدوية</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>ربط المكونات وبيانات الأهداف الدوائية</td></tr>
<tr><td>التفاعلات الدوائية</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>بيانات التفاعلات بين الأدوية</td></tr>
</tbody>
</table>

---

## التراخيص

لكل مصدر ترخيصه الخاص — يُرجى التحقق منه قبل الاستشهاد:

- **TxGNN**: للاستخدام الأكاديمي؛ يُستشهد بـ Huang et al. (2023)
- **ClinicalTrials.gov / PubMed**: بيانات عامة من المعاهد الوطنية الأمريكية للصحة (NIH)
- **DrugBank**: الاستخدام غير التجاري خاضع لشروط ترخيصها
- **SFDA**: خاضع لشروط البيانات المفتوحة للجهة التنظيمية في المملكة العربية السعودية

---

## وتيرة التحديث

| البيانات | الوتيرة |
|------|-----------|
| بيانات التسجيل | وفق ما تنشره الجهة التنظيمية |
| أدلة التجارب والأدبيات | تُجمع من جديد بشكل دوري |
| بيانات التفاعلات الدوائية | تُراجع كل ثلاثة أشهر |

---

## الاستشهاد الأكاديمي

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

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

<div class="disclaimer">
<strong>إخلاء المسؤولية</strong><br>
هذا التقرير مخصص للاستخدام المرجعي في البحث الأكاديمي فقط و<strong>لا يشكّل استشارة طبية</strong>. التزم دائمًا بتعليمات طبيبك، ولا تعدّل دواءك من تلقاء نفسك أبدًا. أي قرار يتعلق بإعادة توظيف دواء يتطلب تحققًا سريريًا كاملًا ومراجعة تنظيمية.
<br><br>
<small>روجعت من قِبل: 藥提醒科技有限公司 (yao.care)</small>
</div>
