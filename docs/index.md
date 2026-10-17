---
layout: default
title: توقعات إعادة توظيف الأدوية
nav_order: 1
description: "توقعات مدعومة بالذكاء الاصطناعي لإعادة توظيف الأدوية في المملكة العربية السعودية. تحليل قائم على الأدلة للأدوية المعتمدة بحثًا عن استطبابات علاجية جديدة محتملة."
permalink: /
---

# توقعات إعادة توظيف الأدوية — المملكة العربية السعودية

This project uses the TxGNN knowledge graph to predict potential new therapeutic uses for medicines approved in Saudi Arabia.

**Disclaimer**: This content is for research purposes only and does not constitute medical advice. All drug repurposing predictions require clinical validation before application.

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
النموذج، وتشمل دمج بيانات تسجيل الأدوية الوطنية، والتنبؤ بالتعلّم العميق مع استبعاد الاستخدامات المسجّلة مسبقًا في الرسم البياني المعرفي، وتصنيف الأدلة من PubMed / ClinicalTrials، وتكامل السجلات الصحية الإلكترونية
عبر SMART on FHIR.
