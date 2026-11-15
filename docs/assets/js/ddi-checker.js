/**
 * SATxGNN Drug-Drug Interaction Checker
 *
 * Client-side DDI checking with 15 built-in curated rules (DDInter consulted as a reference; not a full database lookup).
 * Provides real-time interaction alerts for drug repurposing candidates.
 *
 * @author SATxGNN Team
 * @version 1.0.0
 */
(function(global) {
  'use strict';

  const CONFIG = {
    // This site does not publish /data/ddi-index.json; only the curated rules
    // below are used. Set a URL here once such a file exists.
    ddiDataUrl: null,
    maxAlerts: 10
  };

  // Severity levels with priority (higher = more severe)
  const SEVERITY = {
    'Major': { priority: 3, class: 'ddi-major', label: 'شديد' },
    'Moderate': { priority: 2, class: 'ddi-moderate', label: 'متوسط' },
    'Minor': { priority: 1, class: 'ddi-minor', label: 'طفيف' }
  };

  // 15 built-in high-priority DDI rules (hand-curated, DDInter consulted as a reference)
  // Format: { drug1: [synonym list], drug2: [synonym list], severity, summary, detail }
  const CURATED_DDI_RULES = [
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['ibuprofen', 'advil', 'motrin', 'brufen']
      ],
      severity: 'Major',
      summary: 'وارفارين + إيبوبروفين: زيادة خطر النزف',
      detail: 'تثبط مضادات الالتهاب غير الستيرويدية وظيفة الصفائح الدموية وقد تعزز التأثير المضاد للتخثر للوارفارين، مما يزيد خطر النزف الهضمي زيادة كبيرة.',
      recommendation: 'استخدم الباراسيتامول بدلًا منه، أو أضف مثبطًا لمضخة البروتون لحماية المعدة.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['aspirin', 'acetylsalicylic acid']
      ],
      severity: 'Major',
      summary: 'وارفارين + أسبرين: زيادة خطر النزف',
      detail: 'يؤثر كلاهما في الإرقاء؛ ويزيد استخدامهما معًا خطر النزف زيادة كبيرة.',
      recommendation: 'إذا كان الجمع بينهما ضروريًا فاستخدم جرعة منخفضة من الأسبرين وراقب نسبة INR عن كثب.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['naproxen', 'aleve', 'naprosyn']
      ],
      severity: 'Major',
      summary: 'وارفارين + نابروكسين: زيادة خطر النزف',
      detail: 'الجمع بين النابروكسين والوارفارين يزيد خطر النزف الهضمي وغيره من حالات النزف.',
      recommendation: 'استخدم الباراسيتامول لتسكين الألم بدلًا منه.'
    },
    {
      drugs: [
        ['metformin', 'glucophage'],
        ['iodixanol', 'visipaque', 'iopamidol', 'isovue', 'contrast']
      ],
      severity: 'Major',
      summary: 'ميتفورمين + مواد التباين اليودية: خطر الحماض اللبني',
      detail: 'قد تسبب مواد التباين إصابة كلوية حادة تؤدي إلى تراكم الميتفورمين والحماض اللبني.',
      recommendation: 'أوقف الميتفورمين قبل الإجراء بـ48 ساعة ولا تستأنفه إلا بعد التأكد من سلامة وظائف الكلى.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['clarithromycin', 'biaxin', 'klacid']
      ],
      severity: 'Major',
      summary: 'كولشيسين + كلاريثرومايسين: خطر السمية',
      detail: 'الكلاريثرومايسين مثبط قوي لإنزيم CYP3A4 ويرفع مستويات الكولشيسين في الدم بشدة.',
      recommendation: 'تجنب الجمع بينهما أو خفّض جرعة الكولشيسين بدرجة كبيرة.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['ritonavir', 'norvir', 'cobicistat', 'tybost']
      ],
      severity: 'Major',
      summary: 'كولشيسين + مثبطات بروتياز فيروس نقص المناعة البشرية: خطر سمية شديدة',
      detail: 'ترفع مثبطات بروتياز فيروس نقص المناعة البشرية مستويات الكولشيسين بشكل ملحوظ وقد تسبب سمية قاتلة.',
      recommendation: 'مضاد استطباب لدى مرضى القصور الكلوي أو الكبدي.'
    },
    {
      drugs: [
        ['simvastatin', 'zocor'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'سيمفاستاتين + أميودارون: خطر اعتلال العضلات',
      detail: 'يرفع الأميودارون مستويات السيمفاستاتين، مما يزيد خطر انحلال الربيدات.',
      recommendation: 'لا تتجاوز 20 ملغ يوميًا من السيمفاستاتين، أو انتقل إلى ستاتين آخر.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['tramadol', 'ultram']
      ],
      severity: 'Major',
      summary: 'مثبطات استرداد السيروتونين الانتقائية + ترامادول: خطر متلازمة السيروتونين',
      detail: 'يزيد كلاهما النشاط السيروتونيني؛ وقد يسبب استخدامهما معًا متلازمة سيروتونين مهددة للحياة.',
      recommendation: 'راقب الأعراض عن كثب (فرط الحرارة، الرمع العضلي، تغير الحالة الذهنية) وفكّر في مسكن بديل.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['linezolid', 'zyvox']
      ],
      severity: 'Major',
      summary: 'مثبطات استرداد السيروتونين الانتقائية + لينزوليد: خطر متلازمة السيروتونين',
      detail: 'اللينزوليد مثبط لأوكسيداز أحادي الأمين؛ والجمع بينه وبين هذه المثبطات بالغ الخطورة.',
      recommendation: 'تجنب الجمع بينهما. إذا كان اللينزوليد ضروريًا فأوقف مثبط استرداد السيروتونين واترك فترة تخلص مناسبة.'
    },
    {
      drugs: [
        ['amiodarone', 'cordarone'],
        ['moxifloxacin', 'avelox']
      ],
      severity: 'Major',
      summary: 'أميودارون + موكسيفلوكساسين: خطر إطالة فترة QT',
      detail: 'قد يطيل كلاهما فترة QT؛ ويزيد استخدامهما معًا خطر تسرع القلب البطيني متعدد الأشكال (torsades de pointes).',
      recommendation: 'تجنب الجمع بينهما أو راقب تخطيط القلب عن كثب.'
    },
    {
      drugs: [
        ['digoxin', 'lanoxin'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'ديجوكسين + أميودارون: خطر التسمم بالديجوكسين',
      detail: 'يرفع الأميودارون مستويات الديجوكسين في الدم بنحو 70%.',
      recommendation: 'عند بدء الأميودارون خفّض جرعة الديجوكسين إلى النصف وراقب مستوياته في الدم.'
    },
    {
      drugs: [
        ['clopidogrel', 'plavix'],
        ['omeprazole', 'prilosec', 'esomeprazole', 'nexium']
      ],
      severity: 'Moderate',
      summary: 'كلوبيدوغريل + مثبطات مضخة البروتون: انخفاض التأثير المضاد للصفائح',
      detail: 'يثبط الأوميبرازول إنزيم CYP2C19، فيقل تحويل الكلوبيدوغريل إلى مستقلبه الفعال.',
      recommendation: 'فكّر في البانتوبرازول أو أحد حاصرات H2 بدلًا منه.'
    },
    {
      drugs: [
        ['lithium', 'lithobid'],
        ['ibuprofen', 'advil', 'naproxen', 'aleve', 'diclofenac']
      ],
      severity: 'Major',
      summary: 'ليثيوم + مضادات الالتهاب غير الستيرويدية: خطر التسمم بالليثيوم',
      detail: 'تقلل مضادات الالتهاب غير الستيرويدية الإطراح الكلوي لليثيوم فترتفع مستوياته في الدم.',
      recommendation: 'تجنب الجمع بينهما أو راقب مستويات الليثيوم عن كثب.'
    },
    {
      drugs: [
        ['potassium', 'k-dur', 'klor-con'],
        ['spironolactone', 'aldactone', 'eplerenone', 'inspra']
      ],
      severity: 'Major',
      summary: 'مكملات البوتاسيوم + مدرات البول الحافظة للبوتاسيوم: خطر فرط بوتاسيوم الدم',
      detail: 'يرفع كلاهما بوتاسيوم المصل؛ وقد يسبب استخدامهما معًا فرط بوتاسيوم الدم المهدد للحياة.',
      recommendation: 'راقب بوتاسيوم المصل بانتظام وتجنب مكملات البوتاسيوم المتزامنة.'
    },
    {
      drugs: [
        ['methotrexate', 'trexall'],
        ['trimethoprim', 'bactrim', 'septra', 'sulfamethoxazole']
      ],
      severity: 'Major',
      summary: 'ميثوتريكسات + تريميثوبريم-سلفاميثوكسازول: خطر تثبيط نقي العظم',
      detail: 'يثبط كلاهما استقلاب الفولات؛ ويزيد استخدامهما معًا خطر تثبيط نقي العظم والتهاب الأغشية المخاطية.',
      recommendation: 'تجنب الجمع بينهما، أو احرص على مكملات كافية من الفولات وراقب تعداد الدم عن كثب.'
    }
  ];

  let ddiIndex = null;
  let isLoaded = false;

  /**
   * Load DDI index data
   */
  async function loadDDIIndex() {
    if (isLoaded) return;
    if (!CONFIG.ddiDataUrl) {
      isLoaded = true;
      return;
    }

    try {
      const response = await fetch(CONFIG.ddiDataUrl);
      if (response.ok) {
        ddiIndex = await response.json();
        isLoaded = true;
        console.log('DDI index loaded:', ddiIndex?.count || 0, 'interactions');
      }
    } catch (error) {
      console.warn('DDI index not available, using curated rules only');
      isLoaded = true;
    }
  }

  /**
   * Normalize drug name for comparison
   */
  function normalizeDrugName(name) {
    if (!name) return '';
    return name.toLowerCase()
      .replace(/\s+/g, ' ')
      .replace(/[^a-z0-9\s]/g, '')
      .trim();
  }

  /**
   * Check if a drug name matches any of the synonyms
   */
  function matchesDrug(drugName, synonyms) {
    const normalized = normalizeDrugName(drugName);
    return synonyms.some(syn => {
      const normalizedSyn = normalizeDrugName(syn);
      return normalized.includes(normalizedSyn) || normalizedSyn.includes(normalized);
    });
  }

  /**
   * Check for DDI between two drugs using curated rules
   */
  function checkCuratedDDI(drug1, drug2) {
    const alerts = [];

    for (const rule of CURATED_DDI_RULES) {
      const [drugGroup1, drugGroup2] = rule.drugs;

      // Check if drug1 matches group1 and drug2 matches group2, or vice versa
      if (
        (matchesDrug(drug1, drugGroup1) && matchesDrug(drug2, drugGroup2)) ||
        (matchesDrug(drug1, drugGroup2) && matchesDrug(drug2, drugGroup1))
      ) {
        alerts.push({
          drug1: drug1,
          drug2: drug2,
          severity: rule.severity,
          severityInfo: SEVERITY[rule.severity],
          summary: rule.summary,
          detail: rule.detail,
          recommendation: rule.recommendation,
          source: 'قواعد التداخلات المدمجة في SATxGNN (15 قاعدة مختارة؛ ليست بحثًا كاملًا في DDInter)'
        });
      }
    }

    return alerts;
  }

  /**
   * Check DDI for a list of medications
   * @param {string[]} medications - Array of medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkInteractions(medications) {
    if (!medications || medications.length < 2) {
      return [];
    }

    const allAlerts = [];
    const seen = new Set();

    // Check all pairs
    for (let i = 0; i < medications.length; i++) {
      for (let j = i + 1; j < medications.length; j++) {
        const drug1 = medications[i];
        const drug2 = medications[j];
        const pairKey = [drug1, drug2].sort().join('|');

        if (seen.has(pairKey)) continue;
        seen.add(pairKey);

        const alerts = checkCuratedDDI(drug1, drug2);
        allAlerts.push(...alerts);
      }
    }

    // Sort by severity (highest first) and limit
    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority)
      .slice(0, CONFIG.maxAlerts);
  }

  /**
   * Check if a new drug has interactions with existing medications
   * @param {string} newDrug - The new drug to check
   * @param {string[]} currentMeds - Array of current medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkNewDrug(newDrug, currentMeds) {
    if (!newDrug || !currentMeds || currentMeds.length === 0) {
      return [];
    }

    const allAlerts = [];

    for (const currentDrug of currentMeds) {
      const alerts = checkCuratedDDI(newDrug, currentDrug);
      allAlerts.push(...alerts);
    }

    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority);
  }

  /**
   * Format alerts as HTML for display
   */
  function formatAlertsHTML(alerts) {
    if (!alerts || alerts.length === 0) {
      return '<div class="ddi-no-alerts">لم يُعثر على تنبيهات للتداخلات الدوائية</div>';
    }

    let html = '<div class="ddi-alerts">';

    alerts.forEach((alert, index) => {
      html += `
        <div class="ddi-alert ${alert.severityInfo.class}">
          <div class="ddi-alert-header">
            <span class="ddi-severity-badge">${alert.severityInfo.label}</span>
            <span class="ddi-summary">${escapeHtml(alert.summary)}</span>
          </div>
          <div class="ddi-alert-body">
            <p class="ddi-detail">${escapeHtml(alert.detail)}</p>
            <p class="ddi-recommendation"><strong>التوصية:</strong> ${escapeHtml(alert.recommendation)}</p>
          </div>
          <div class="ddi-alert-footer">
            <span class="ddi-source">المصدر: ${escapeHtml(alert.source)}</span>
          </div>
        </div>
      `;
    });

    html += '</div>';
    return html;
  }

  /**
   * Format alerts for CDS Hooks response
   */
  function formatForCDSHooks(alerts) {
    return alerts.map((alert, index) => ({
      uuid: `ddi-alert-${index}`,
      summary: alert.summary,
      indicator: alert.severity === 'Major' ? 'critical' : alert.severity === 'Moderate' ? 'warning' : 'info',
      detail: `${alert.detail}\n\nالتوصية: ${alert.recommendation}`,
      source: {
        label: 'SATxGNN DDI Checker',
        url: 'https://satxgnn.yao.care/'
      }
    }));
  }

  function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Export
  global.TwTxGNN = global.TwTxGNN || {};
  global.TwTxGNN.DDIChecker = {
    load: loadDDIIndex,
    checkInteractions: checkInteractions,
    checkNewDrug: checkNewDrug,
    formatAlertsHTML: formatAlertsHTML,
    formatForCDSHooks: formatForCDSHooks,
    SEVERITY: SEVERITY
  };

  // Auto-load when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadDDIIndex);
  } else {
    loadDDIIndex();
  }

})(typeof window !== 'undefined' ? window : this);
