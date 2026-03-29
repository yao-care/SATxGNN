"""疾病映射模組 - 葡萄牙語適應症/治療類別映射至 TxGNN 疾病本體"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# 葡萄牙語-英語疾病/症狀對照表
DISEASE_DICT = {
    # === القلب والأوعية الدموية (Cardiovascular) ===
    "ارتفاع ضغط الدم": "hypertension",
    "ضغط الدم المرتفع": "hypertension",
    "انخفاض ضغط الدم": "hypotension",
    "احتشاء عضلة القلب": "myocardial infarction",
    "نوبة قلبية": "myocardial infarction",
    "ذبحة صدرية": "angina",
    "اضطراب نظم القلب": "arrhythmia",
    "الرجفان الأذيني": "atrial fibrillation",
    "قصور القلب": "heart failure",
    "فشل القلب الاحتقاني": "heart failure",
    "مرض الشريان التاجي": "coronary artery disease",
    "تجلط الأوردة العميقة": "deep vein thrombosis",
    "انسداد رئوي": "pulmonary embolism",
    "ارتفاع الكوليسترول": "hypercholesterolemia",
    "اضطراب الدهون": "dyslipidemia",
    "تصلب الشرايين": "atherosclerosis",
    # === الجهاز التنفسي (Respiratory) ===
    "مرض الانسداد الرئوي المزمن": "chronic obstructive pulmonary disease",
    "الربو": "asthma",
    "الربو القصبي": "asthma",
    "التهاب الرئة": "pneumonia",
    "التهاب الشعب الهوائية": "bronchitis",
    "الإنفلونزا": "influenza",
    "السل": "tuberculosis",
    "التليف الكيسي": "cystic fibrosis",
    "انقطاع النفس أثناء النوم": "obstructive sleep apnea",
    "ضيق التنفس": "dyspnea",
    "التهاب الجيوب الأنفية": "sinusitis",
    "التهاب الأنف التحسسي": "allergic rhinitis",
    # === الجهاز الهضمي (Gastrointestinal) ===
    "ارتجاع المريء": "gastroesophageal reflux disease",
    "قرحة المعدة": "gastric ulcer",
    "التهاب المعدة": "gastritis",
    "متلازمة القولون العصبي": "irritable bowel syndrome",
    "مرض التهاب الأمعاء": "inflammatory bowel disease",
    "داء كرون": "crohn disease",
    "التهاب القولون التقرحي": "ulcerative colitis",
    "الإمساك": "constipation",
    "الإسهال": "diarrhea",
    "الغثيان": "nausea",
    "القيء": "vomiting",
    "الكبد الدهني": "hepatic steatosis",
    "تليف الكبد": "liver cirrhosis",
    "التهاب الكبد": "hepatitis",
    "التهاب الكبد ب": "hepatitis b",
    "التهاب الكبد ج": "hepatitis c",
    "التهاب البنكرياس": "pancreatitis",
    "حصوات المرارة": "cholelithiasis",
    # === الجهاز العصبي (Neurological) ===
    "مرض الزهايمر": "alzheimer disease",
    "الزهايمر": "alzheimer disease",
    "مرض باركنسون": "parkinson disease",
    "الصرع": "epilepsy",
    "التصلب المتعدد": "multiple sclerosis",
    "الصداع النصفي": "migraine",
    "صداع": "headache",
    "السكتة الدماغية": "stroke",
    "اعتلال الأعصاب": "neuropathy",
    "التهاب السحايا": "meningitis",
    "التهاب الدماغ": "encephalitis",
    # === الاضطرابات النفسية (Psychiatric) ===
    "الاكتئاب": "depression",
    "اضطراب الاكتئاب الرئيسي": "major depressive disorder",
    "القلق": "anxiety disorder",
    "اضطراب القلق العام": "generalized anxiety disorder",
    "الاضطراب ثنائي القطب": "bipolar disorder",
    "الفصام": "schizophrenia",
    "الوسواس القهري": "obsessive-compulsive disorder",
    "اضطراب ما بعد الصدمة": "post-traumatic stress disorder",
    "الأرق": "insomnia",
    "اضطراب نقص الانتباه": "attention deficit hyperactivity disorder",
    # === جهاز الغدد الصماء (Endocrine) ===
    "داء السكري": "diabetes mellitus",
    "السكري": "diabetes mellitus",
    "سكري النوع الأول": "type 1 diabetes mellitus",
    "سكري النوع الثاني": "type 2 diabetes mellitus",
    "قصور الغدة الدرقية": "hypothyroidism",
    "فرط نشاط الغدة الدرقية": "hyperthyroidism",
    "السمنة": "obesity",
    "متلازمة الأيض": "metabolic syndrome",
    "النقرس": "gout",
    # === الجهاز العضلي الهيكلي (Musculoskeletal) ===
    "التهاب المفاصل": "arthritis",
    "التهاب المفاصل الروماتويدي": "rheumatoid arthritis",
    "التهاب المفاصل التنكسي": "osteoarthritis",
    "هشاشة العظام": "osteoporosis",
    "الذئبة الحمراء": "systemic lupus erythematosus",
    "الألم العضلي الليفي": "fibromyalgia",
    "آلام أسفل الظهر": "low back pain",
    # === أمراض الجلد (Dermatological) ===
    "الصدفية": "psoriasis",
    "الأكزيما": "eczema",
    "التهاب الجلد التأتبي": "atopic dermatitis",
    "الشرى": "urticaria",
    "حب الشباب": "acne",
    "البهاق": "vitiligo",
    "الثعلبة": "alopecia",
    "الحزام الناري": "herpes zoster",
    # === الجهاز البولي (Urological) ===
    "التهاب المسالك البولية": "urinary tract infection",
    "التهاب المثانة": "cystitis",
    "الفشل الكلوي": "renal failure",
    "مرض الكلى المزمن": "chronic kidney disease",
    "حصوات الكلى": "nephrolithiasis",
    "تضخم البروستاتا الحميد": "benign prostatic hyperplasia",
    # === العيون (Ophthalmological) ===
    "الجلوكوما": "glaucoma",
    "الماء الأزرق": "glaucoma",
    "إعتام عدسة العين": "cataract",
    "الماء الأبيض": "cataract",
    "التهاب الملتحمة": "conjunctivitis",
    "اعتلال الشبكية السكري": "diabetic retinopathy",
    # === الأمراض المعدية (Infectious) ===
    "عدوى فيروس نقص المناعة": "hiv infection",
    "الإيدز": "acquired immunodeficiency syndrome",
    "الملاريا": "malaria",
    "كوفيد-19": "covid-19",
    "كورونا": "covid-19",
    "تسمم الدم": "sepsis",
    # === الحساسية (Allergic) ===
    "حساسية": "allergy",
    "صدمة الحساسية": "anaphylaxis",
    "الربو التحسسي": "allergic asthma",
    "حساسية الطعام": "food allergy",
    # === أمراض النساء (Gynecological) ===
    "بطانة الرحم المهاجرة": "endometriosis",
    "تكيس المبايض": "polycystic ovary syndrome",
    "انقطاع الطمث": "menopause",
    "عسر الطمث": "dysmenorrhea",
    # === السرطان (Oncological) ===
    "سرطان": "cancer",
    "ورم": "cancer",
    "سرطان الثدي": "breast cancer",
    "سرطان الرئة": "lung cancer",
    "سرطان القولون والمستقيم": "colorectal cancer",
    "سرطان البروستاتا": "prostate cancer",
    "سرطان الكبد": "liver cancer",
    "سرطان المعدة": "stomach cancer",
    "سرطان البنكرياس": "pancreatic cancer",
    "اللوكيميا": "leukemia",
    "سرطان الدم": "leukemia",
    "الليمفوما": "lymphoma",
    "الميلانوما": "melanoma",
    # === أعراض عامة (General) ===
    "حمى": "fever",
    "ألم": "pain",
    "ألم مزمن": "chronic pain",
    "التهاب": "inflammation",
    "وذمة": "edema",
    "تعب": "fatigue",
    "فقر الدم": "anemia",
}


def load_disease_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 疾病詞彙表"""
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "disease_vocab.csv"
    return pd.read_csv(filepath)


def build_disease_index(disease_df: pd.DataFrame) -> Dict[str, Tuple[str, str]]:
    """建立疾病名稱索引（關鍵詞 -> (disease_id, disease_name)）"""
    index = {}

    for _, row in disease_df.iterrows():
        disease_id = row["disease_id"]
        disease_name = row["disease_name"]
        name_upper = row["disease_name_upper"]

        # 完整名稱
        index[name_upper] = (disease_id, disease_name)

        # 提取關鍵詞（按空格和逗號分割）
        keywords = re.split(r"[,\s\-]+", name_upper)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) > 3 and kw not in index:  # 只保留較長的關鍵詞
                index[kw] = (disease_id, disease_name)

    return index


def extract_indications(indication_str: str) -> List[str]:
    """從適應症/治療類別文字提取個別適應症

    使用葡萄牙語常見分隔符分割
    """
    if not indication_str:
        return []

    # 正規化
    text = indication_str.strip().lower()

    # 使用分隔符分割
    parts = re.split(r"[.;]", text)

    indications = []
    for part in parts:
        # 再用逗號細分
        sub_parts = re.split(r"[,/]", part)
        for sub in sub_parts:
            sub = sub.strip()
            # 移除常見前綴
            sub = re.sub(r"^(para |tratamento de |indicado para |usado para )", "", sub)
            # 移除常見後綴
            sub = re.sub(r"( e outros| etc\.?)$", "", sub)
            sub = sub.strip()
            if sub and len(sub) >= 2:
                indications.append(sub)

    return indications


def translate_indication(indication: str) -> List[str]:
    """將葡萄牙語適應症翻譯為英文關鍵詞"""
    keywords = []
    indication_lower = indication.lower()

    for pt, en in DISEASE_DICT.items():
        if pt in indication_lower:
            keywords.append(en.upper())

    return keywords


def map_indication_to_disease(
    indication: str,
    disease_index: Dict[str, Tuple[str, str]],
) -> List[Tuple[str, str, float]]:
    """將單一適應症映射到 TxGNN 疾病

    Returns:
        [(disease_id, disease_name, confidence), ...]
    """
    results = []

    # 翻譯為英文關鍵詞
    keywords = translate_indication(indication)

    for kw in keywords:
        # 完全匹配
        if kw in disease_index:
            disease_id, disease_name = disease_index[kw]
            results.append((disease_id, disease_name, 1.0))
            continue

        # 部分匹配
        for index_kw, (disease_id, disease_name) in disease_index.items():
            if kw in index_kw or index_kw in kw:
                results.append((disease_id, disease_name, 0.8))

    # 去重並按信心度排序
    seen = set()
    unique_results = []
    for disease_id, disease_name, conf in sorted(results, key=lambda x: -x[2]):
        if disease_id not in seen:
            seen.add(disease_id)
            unique_results.append((disease_id, disease_name, conf))

    return unique_results[:5]  # 最多返回 5 個匹配


def map_fda_indications_to_diseases(
    fda_df: pd.DataFrame,
    disease_df: Optional[pd.DataFrame] = None,
    indication_field: str = "CLASSE_TERAPEUTICA",
) -> pd.DataFrame:
    """將巴西 ANVISA 藥品治療類別映射到 TxGNN 疾病"""
    if disease_df is None:
        disease_df = load_disease_vocab()

    disease_index = build_disease_index(disease_df)

    results = []

    for _, row in fda_df.iterrows():
        # ANVISA 使用 CLASSE_TERAPEUTICA 而非適應症
        indication_str = row.get(indication_field, "")
        if not indication_str:
            continue

        # 提取個別適應症
        indications = extract_indications(indication_str)

        for ind in indications:
            # 翻譯並映射
            matches = map_indication_to_disease(ind, disease_index)

            if matches:
                for disease_id, disease_name, confidence in matches:
                    results.append({
                        "NUMERO_REGISTRO_PRODUTO": row.get("NUMERO_REGISTRO_PRODUTO", ""),
                        "NOME_PRODUTO": row.get("NOME_PRODUTO", ""),
                        "CLASSE_TERAPEUTICA": indication_str[:100],
                        "extracted_indication": ind,
                        "disease_id": disease_id,
                        "disease_name": disease_name,
                        "confidence": confidence,
                    })
            else:
                results.append({
                    "NUMERO_REGISTRO_PRODUTO": row.get("NUMERO_REGISTRO_PRODUTO", ""),
                    "NOME_PRODUTO": row.get("NOME_PRODUTO", ""),
                    "CLASSE_TERAPEUTICA": indication_str[:100],
                    "extracted_indication": ind,
                    "disease_id": None,
                    "disease_name": None,
                    "confidence": 0,
                })

    return pd.DataFrame(results)


def get_indication_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算適應症映射統計"""
    total = len(mapping_df)
    mapped = mapping_df["disease_id"].notna().sum()
    unique_indications = mapping_df["extracted_indication"].nunique()
    unique_diseases = mapping_df[mapping_df["disease_id"].notna()]["disease_id"].nunique()

    return {
        "total_indications": total,
        "mapped_indications": int(mapped),
        "mapping_rate": mapped / total if total > 0 else 0,
        "unique_indications": unique_indications,
        "unique_diseases": unique_diseases,
    }
