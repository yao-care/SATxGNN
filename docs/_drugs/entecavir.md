---
layout: default
title: Entecavir
parent: تنبؤ نموذجي فقط (L5)
nav_order: 306
evidence_level: L5
indication_count: 9
monitor_inn: "ENTECAVIR"
predicted_indications: ["chronic hepatitis C virus infection", "HIV infectious disease", "hepatitis C virus infection", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "hepatitis, viral, animal", "hepatitis E virus infection", "hepatitis A virus infection"]
last_modified_at: 2026-11-24
description: "Entecavir: الاستطباب الجديد المتوقع التهاب الكبد C الفيروسي المزمن (chronic hepatitis C virus infection) (مستوى الدليل L5). المنتجات المسجلة لدى SFDA: 17 (السارية: 17)"
---

# Entecavir
{: .fs-9 }

مستوى الأدلة: **L5** | دواعي الاستعمال المتوقعة: **9** 
{: .fs-6 .fw-300 }

---

## جدول المحتويات
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## تقرير التقييم الصيدلاني

</div>

## إنتكافير: مثبط بوليميراز فيروس التهاب الكبد B (نظير نيوكليوزيدي) → التهاب الكبد C الفيروسي المزمن (chronic hepatitis C virus infection)
{: .text-alpha }

## ملخص في جملة واحدة

إنتكافير دواء مضاد للفيروسات من فئة النظائر النيوكليوزيدية، يعمل على إنزيم البوليميراز لفيروس التهاب الكبد B. يتوقع نموذج TxGNN أنه قد يفيد في **التهاب الكبد C الفيروسي المزمن (chronic hepatitis C virus infection)**، لكن الدعم المتاح يقتصر على تجربتين سريريتين وعدد من المنشورات التي تتناول العدوى المشتركة بفيروسَي B وC، ولا توجد دراسة تختبر فعالية الدواء ضد فيروس C نفسه.

## نظرة سريعة

| البند | المحتوى |
|------|------|
| الاستطباب الأصلي | غير مسجل في البيانات المحلية |
| الاستطباب الجديد المتوقع | التهاب الكبد C الفيروسي المزمن (chronic hepatitis C virus infection) |
| درجة تنبؤ TxGNN | 0.9998 |
| مستوى الأدلة | L5 |
| حالة السوق في السعودية | مُسوَّق (التراخيص السارية: 17 من 17) |
| عدد التراخيص | 17 (السارية: 17) |
| القرار الموصى به | إيقاف مؤقت |

## لماذا يبدو هذا التنبؤ معقولاً؟

وفقًا لقسمي «Mechanism of Action» و«Microbiology» في معلومات الوصف المعتمدة من إدارة الغذاء والدواء الأمريكية (Prescribing Information) لـ Entecavir (ترجمة غير رسمية): «إنتيكافير دواء مضاد للفيروسات يعمل ضد فيروس التهاب الكبد B. […] إنتيكافير، وهو نظير نوكليوزيدي للديوكسي غوانوزين ذو نشاط ضد المنتسخة العكسية (rt) لفيروس HBV، يُفسفَر بكفاءة إلى الشكل الفعّال ثلاثي الفوسفات، الذي يبلغ عمر النصف داخل الخلية له 15 ساعة. ومن خلال التنافس مع الركيزة الطبيعية ديوكسي غوانوزين ثلاثي الفوسفات، يُثبّط إنتيكافير ثلاثي الفوسفات وظيفيًا الأنشطة الثلاثة جميعها للمنتسخة العكسية لفيروس HBV: تمهيد القواعد، والانتساخ العكسي للسلسلة السالبة من الرنا المرسال قبل الجينومي، وتخليق السلسلة الموجبة من دنا HBV.» النص الأصلي بالإنجليزية: "Entecavir is an antiviral drug against hepatitis B virus. […] Entecavir, a deoxyguanosine nucleoside analogue with activity against HBV reverse transcriptase (rt), is efficiently phosphorylated to the active triphosphate form, which has an intracellular half-life of 15 hours. By competing with the natural substrate deoxyguanosine triphosphate, entecavir triphosphate functionally inhibits all three activities of the HBV reverse transcriptase: base priming, reverse transcription of the negative strand from the pregenomic messenger RNA, and synthesis of the positive strand of HBV DNA." ([DailyMed: Baraclude (entecavir) prescribing information, E.R. Squibb & Sons, L.L.C.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=046e61c9-9298-4b2e-b76e-b26b81fecd20)، إصدار 2019-11-06؛ تاريخ الاطلاع 2026-11-20). المعروف أن إنتكافير نظير نيوكليوزيدي يثبّط بوليميراز فيروس التهاب الكبد B ونسخه العكسي.

أما فيروس التهاب الكبد C فهو فيروس RNA يعتمد على إنزيم NS5B، وليس لإنتكافير نشاط مباشر معروف ضده. لذلك فالرابط الآلي ضعيف، ولا يتجاوز كونه رابطاً سريرياً غير مباشر: في المرضى المصابين بالفيروسين معاً، قد يعاود فيروس B النشاط بعد العلاج المضاد لفيروس C بالمضادات المباشرة (DAA)، فيُستخدم إنتكافير للوقاية من ذلك أو لعلاجه. أي أن فائدته تخص فيروس B وليس فيروس C.

## الأدلة من التجارب السريرية

| رقم التجربة | المرحلة | الحالة | عدد المشاركين | أبرز النتائج |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | المرحلة 2/3 | مكتملة | 23 | دراسة استباقية لمضادات الفيروسات المباشرة في العدوى المشتركة B/C، لرصد معاودة نشاط فيروس B؛ ليست اختباراً لفعالية إنتكافير ضد فيروس C |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | غير محددة | غير معروفة | 60 | دراسة عشوائية مفتوحة لنظير نيوكليوزيدي وقائي (12 مقابل 24 أسبوعاً) لمنع معاودة فيروس B أثناء علاج فيروس C؛ تدعم الوقاية من B وليس علاج C |

## الأدلة من المنشورات العلمية

| PMID | السنة | النوع | المجلة | أبرز النتائج |
|------|-----|------|------|---------|
| [34864158](https://pubmed.ncbi.nlm.nih.gov/34864158/) | 2022 | تجربة عشوائية | Clinical Gastroenterology and Hepatology | إنتكافير يمنع معاودة نشاط فيروس B أثناء علاج فيروس C بالمضادات المباشرة في العدوى المزدوجة |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | مراجعة | Expert Opinion on Pharmacotherapy | مراجعة لتطورات علاج العدوى المشتركة B/C |
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | دراسة أترابية | Viruses | معاودة نشاط فيروس C لدى مرضى التهاب الكبد B إيجابيي أضداد C بعد علاج B بالنظائر النيوكليوزيدية (66 مريضاً) |
| [35108715](https://pubmed.ncbi.nlm.nih.gov/35108715/) | 2022 | دراسة سريرية | Digestive Diseases | معاودة نشاط فيروس B لدى المرضى المعالَجين بالمضادات المباشرة لفيروس C |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | مراجعة | Minerva Gastroenterologica e Dietologica | تأثير الأدوية المضادة لفيروسَي B وC (ومنها إنتكافير) على وظائف الكلى |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | مراجعة | Wiener Medizinische Wochenschrift | العلاج الحالي لالتهاب الكبد B وC وآفاقه |

تُظهر هذه الأدلة أن إنتكافير مفيد في العدوى المشتركة من جهة فيروس B فقط، ولا توجد دراسة منشورة تقيس تأثيره على فيروس C.

## معلومات السوق في السعودية

<!-- licenses:begin -->

| اسم المنتج المسجل (بالإنجليزية كما في SFDA) | المادة الفعالة (بالإنجليزية) | الشركة المصنّعة | الحالة |
|------|------|------|------|
| ARVIDA 0.5 mg Tablet | ENTECAVIR | APOTEX RESEARCH PRIVATE LIMITED | ساري |
| BARACLUDE 0.5MG F.C. TABLETS | ENTECAVIR | BRISTOL-MYERS SQUIBB | ساري |
| BARACLUDE 1MG F.C. TABLETS | ENTECAVIR | BRISTOL-MYERS SQUIBB | ساري |
| ELIVE | ENTECAVIR | AJA PHARMACEUTICAL INDUSTRIES | ساري |
| ENTAVIR 0.5 mg Film Coated Tablet | ENTECAVIR | SPIMACO | ساري |

يعرض الجدول أعلاه 5 من أصل 17 من المنتجات المسجلة في البيانات.

<!-- licenses:end -->

## السلامة

- **موانع الاستعمال والتحذيرات:** لم تتوفر بيانات من نشرة العبوة؛ يُرجى الرجوع إلى نشرة العبوة لمعلومات السلامة.
- **التداخلات الدوائية:** سُجّل 44 تداخلاً دوائياً، ومنها تداخلات متوسطة الشدة مع: فاموتيدين، رانيتيدين، ميتفورمين، أمفوتريسين B، أموكسيسيلين، ميسالازين، سيميتيدين، فانكوميسين، كاناميسين، ليفوفلوكساسين، نيومايسين، أورليستات، سلفاسالازين، بوليميكسين B.

## الخلاصة والخطوات التالية

**القرار: إيقاف مؤقت**

**المبررات:**
- لا توجد دراسة تتناول التهاب الكبد C المزمن مباشرة؛ فكل الأدلة المتاحة تخص الوقاية من معاودة فيروس B في العدوى المشتركة، ولا آلية معروفة لتأثير الدواء على فيروس C، لذا يبقى مستوى الأدلة L5 رغم ارتفاع درجة التنبؤ.

**للمضي قدماً يلزم:**
- دراسات مخبرية أو سريرية تختبر نشاط إنتكافير ضد فيروس C مباشرة، إن وُجد مبرر علمي لذلك.
- تحديد ما إذا كان المقصود هو استخدامه في الوقاية في العدوى المشتركة B/C، وهو استخدام يتعلق بفيروس B.
- بيانات آلية العمل ونشرة العبوة المعتمدة (التحذيرات وموانع الاستعمال).
- التحقق من وضع التراخيص المحلية الحالية.

<!-- review:begin log -->

## سجل المراجعة

فيما يلي سجل المراجعة لهذه الصفحة. استُبدلت العبارة التي تفيد بعدم توفر بيانات عن آلية العمل بمقتطف من معلومات الوصف الرسمية المذكورة (مع ترجمة غير رسمية)؛ ولم تُعَد كتابة تنبؤات النموذج أو مستويات الأدلة أو الاستنتاجات.

| تاريخ المراجعة | البند | الإجراء | المصدر |
|------|------|------|------|
| 2026-11-20 | استُبدلت عبارة «لا تتوفر بيانات عن آلية العمل» بمقتطف من معلومات الوصف الأمريكية | استُبدلت عبارة عدم توفر بيانات آلية العمل بمقتطف موثق المصدر | [DailyMed: Baraclude (entecavir) prescribing information, E.R. Squibb & Sons, L.L.C.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=046e61c9-9298-4b2e-b76e-b26b81fecd20) |

<!-- review:end log -->

## إخلاء المسؤولية

هذا المحتوى لأغراض البحث فقط ولا يشكل نصيحة طبية.
يلزم التحقق السريري قبل أي تطبيق سريري.

---

