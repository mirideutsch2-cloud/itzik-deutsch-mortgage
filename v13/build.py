# -*- coding: utf-8 -*-
"""Builds the paid-ads landing pages for Itzik Deutsch.
   index.html = version A, b.html = version B (only the headline differs), thanks.html.
   Run: python3 build.py"""
import pathlib

HERE = pathlib.Path(__file__).parent
WA_NUMBER = "972500000000"  # TODO: Itzik's real WhatsApp number
WA_TEXT = "היי איציק, אשמח לבדוק איתך את נושא המשכנתא"

HEADLINES = {
    "A": "מצאתם דירה ולא בטוחים <em>שתעמדו בהחזר?</em>",
    "B": "מצאתם דירה וכל בנק מציע לכם <em>החזר אחר?</em>",
}

# ---------- shared partials ----------
def form(fid, variant):
    return f'''<form class="lead" id="{fid}" novalidate data-variant="{variant}">
  <div class="lead__row">
    <label class="field"><span>שם</span><input name="name" autocomplete="name" required placeholder="השם שלכם"></label>
    <label class="field"><span>טלפון</span><input name="phone" type="tel" inputmode="tel" autocomplete="tel" required placeholder="050-0000000" dir="ltr"></label>
  </div>
  <fieldset class="yn">
    <legend>יש לכם הכנסה קבועה?</legend>
    <label><input type="radio" name="income" value="yes" required><span>כן</span></label>
    <label><input type="radio" name="income" value="no"><span>לא</span></label>
  </fieldset>
  <button class="btn btn--red btn--block" type="submit">איציק, אשמח שתחזור אליי</button>
  <p class="lead__note">אחזור אליכם תוך 24 שעות. השיחה הראשונה עליי.</p>
  <p class="lead__err" role="alert" hidden></p>
</form>'''

HEADER = '''<header class="hd" id="top">
  <div class="hd__bar">
    <a class="hd__brand" href="#top" aria-label="איציק דייטש, לראש הדף">
      <img src="img/logo-dark.svg" alt="" width="54" height="33"><span><b>איציק דייטש</b><small>ייעוץ משכנתאות</small></span>
    </a>
    <nav class="hd__nav" aria-label="ניווט בדף">
      <a href="#guide">למה לבדוק קודם</a><a href="#trust">הגב שמאחוריי</a><a href="#steps">איך זה עובד</a><a href="#calc">מחשבון</a>
    </nav>
    <a class="btn btn--red btn--sm" href="#final">דברו איתי</a>
  </div>
</header>'''

TRUST = '''<section class="sec" id="trust">
  <div class="wrap trust">
    <div class="trust__big glass">
      <span class="kicker">שיתוף פעולה עם חברה ותיקה</span>
      <span class="num"><b data-count="25">25</b><small>שנות ניסיון</small></span>
      <span class="trust__sub">בהשגת ההצעות הטובות ביותר בשוק</span>
    </div>
    <div class="trust__text">
      <h2>ליווי אישי, ומאחוריו <em>25 שנות ניסיון</em></h2>
      <p>אני עובד בשיתוף פעולה עם חברה ותיקה שפועלת בתחום כבר 25 שנה. כך אתם מקבלים ליווי אישי ממני, ולצידו ניסיון של 25 שנה בהשגת ההצעות הטובות ביותר בשוק.</p>
      <ul class="ticks">
        <li><b>כל הבנקים, לא רק אחד.</b> אני בודק את התיק שלכם מול כל הבנקים.</li>
        <li><b>שני אנשי מקצוע על התיק.</b> בפגישת הייעוץ יושבת איתנו גם נציגה מהחברה.</li>
      </ul>
    </div>
  </div>
</section>'''

STEPS_LIST = [
    ("שיחת היכרות", "שיחה קצרה בטלפון, שבה אני מבין מה אתם צריכים ובאיזה שלב אתם נמצאים."),
    ("מסמכים", "אתם שולחים לי את המסמכים, ואני עובר עליהם לפני שאנחנו נפגשים."),
    ("פגישת ייעוץ", "יושבים יחד ובודקים איזה החזר חודשי באמת מתאים לכם."),
    ("מול הבנקים", "אני מגיש את התיק לכל הבנקים, עד שמתקבל אישור עקרוני עם ההצעה הטובה ביותר."),
    ("עד הסוף", "אני מלווה אתכם עד שהמשכנתא מאושרת והכסף מועבר."),
]
STEPS = '''<section class="sec" id="steps">
  <div class="wrap">
    <div class="sec__head"><span class="kicker">איך זה עובד</span><h2>הדרך למשכנתא, <em>שלב אחרי שלב</em></h2></div>
    <ol class="steps">''' + "".join(
        f'<li class="step glass"><span class="step__n">{i+1:02d}</span><h3>{t}</h3><p>{d}</p></li>'
        for i, (t, d) in enumerate(STEPS_LIST)) + '''</ol>
  </div>
</section>'''

TESTI = '''<section class="sec" id="testimonials">
  <div class="wrap">
    <div class="sec__head"><span class="kicker">המלצות</span><h2>לקוחות <em>מספרים</em></h2></div>
    <div class="testi">''' + "".join(f'''
      <figure class="tcard glass is-placeholder">
        <span class="tcard__q" aria-hidden="true">”</span>
        <dl>
          <dt>לפני</dt><dd>[ איפה הם היו לפני שפנו ]</dd>
          <dt>מה עשינו</dt><dd>[ מה עשינו יחד ]</dd>
          <dt>מה יצא</dt><dd>[ התוצאה, עדיף עם מספר ]</dd>
        </dl>
        <figcaption>[ שם הלקוח · עיר ]</figcaption>
      </figure>''' for _ in range(3)) + '''
    </div>
    <p class="draft-note">ממתין ל-2-3 המלצות אמיתיות מלקוחות. לא מפרסמים לפני שהן מגיעות.</p>
  </div>
</section>'''

FOOTER = f'''<footer class="ft">
  <div class="wrap ft__in">
    <img src="img/logo-dark.svg" alt="איציק דייטש" width="64" height="39">
    <p>© איציק דייטש · ייעוץ משכנתאות</p>
    <p class="ft__links"><a href="../accessibility.html">הצהרת נגישות</a> · <a href="../privacy.html">פרטיות</a> · <a href="../terms.html">תנאי שימוש</a></p>
  </div>
</footer>
<a class="wa-float" href="https://wa.me/{WA_NUMBER}?text={WA_TEXT.replace(' ', '%20')}" target="_blank" rel="noopener" aria-label="שלחו לאיציק הודעה בוואטסאפ">
  <svg viewBox="0 0 32 32" aria-hidden="true"><path fill="currentColor" d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3Zm0 23.6a10.6 10.6 0 0 1-5.4-1.5l-.4-.2-3.9 1 1-3.8-.2-.4A10.6 10.6 0 1 1 16 26.6Zm5.8-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7 0a8.7 8.7 0 0 1-4.3-3.8c-.3-.6.3-.5.9-1.7.1-.2 0-.4 0-.5l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.7 3.7 0 0 0-1.1 2.7 6.4 6.4 0 0 0 1.3 3.4 14.7 14.7 0 0 0 5.7 5c2.1.9 2.9 1 4 .8a3.4 3.4 0 0 0 2.2-1.6 2.8 2.8 0 0 0 .2-1.6c0-.2-.3-.3-.6-.4Z"/></svg>
  <span>וואטסאפ</span>
</a>'''

def head(title, desc, robots="index,follow"):
    return f'''<!doctype html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#060a1c">
<link rel="icon" href="../favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="site.css">
</head>
<body>
<a class="skip" href="#main">דילוג לתוכן</a>
<div class="bg" aria-hidden="true"><i class="bg__g1"></i><i class="bg__g2"></i><i class="bg__grid"></i></div>
'''

def landing(variant):
    return head("איציק דייטש · ייעוץ משכנתאות",
                "לפני שחותמים על החוזה, כדאי לדעת בוודאות איזה החזר חודשי תוכלו לעמוד בו לאורך זמן.") + HEADER + f'''
<main id="main">
<!-- 1 · HERO -->
<section class="hero">
  <div class="wrap hero__grid">
    <div class="hero__copy">
      <span class="eyebrow"><i></i>איציק דייטש · יועץ משכנתאות</span>
      <h1>{HEADLINES[variant]}</h1>
      <p class="lede">לפני שחותמים על החוזה, כדאי לדעת בוודאות איזה החזר חודשי תוכלו לעמוד בו לאורך זמן.</p>
      <p>אני איציק דייטש, יועץ משכנתאות. את הבדיקה הזאת אני עושה איתכם, ולאחר מכן משווה עבורכם בין הצעות כל הבנקים עד שנגיע למסלול המתאים לכם ביותר. <b>ואם זה לא העיתוי הנכון, אמליץ לכם לחכות.</b></p>
    </div>
    <div class="hero__visual"><img class="glass-house" src="img/glass-house.webp" alt="" width="1024" height="1024" fetchpriority="high"></div>
    <div class="hero__form glass glass--lit">
      <h2 class="form-title"><span>1</span>בדיקת החזר לפני החתימה</h2>
      {form("lead-hero", variant)}
    </div>
  </div>
</section>

<!-- 2 · PROBLEM -->
<section class="sec" id="problem">
  <div class="wrap problem">
    <div class="sec__head"><span class="kicker">הבעיה</span><h2>החתימה מתקרבת, <em>והשאלה החשובה עדיין פתוחה</em></h2></div>
    <div class="problem__grid">
      <p class="problem__text">מצאתם דירה, והמוכר מחכה לתשובה. רגע לפני שחותמים, חשוב לוודא שההחזר החודשי ישאיר לכם מספיק כדי לחיות בנוחות, לאורך כל שנות המשכנתא.</p>
      <div class="vs glass">
        <div class="vs__col"><span class="vs__who">מה הבנק בודק</span><ul><li>כמה הוא מוכן להלוות לכם</li><li>מה הוא ירוויח מזה</li></ul></div>
        <div class="vs__col vs__col--miss"><span class="vs__who">מה הוא לא בודק</span><ul><li>מה היכולות שלכם</li><li>כמה אתם יכולים לחסוך</li></ul></div>
      </div>
    </div>
    <p class="quote">הדירה החדשה אמורה להביא לכם שקט, <em>גם בתחילת כל חודש.</em></p>
  </div>
</section>

<!-- 3 · GUIDE -->
<section class="sec" id="guide">
  <div class="wrap guide">
    <div class="guide__photo"><div class="halo"></div><img src="img/itzik-cut.webp" alt="איציק דייטש, יועץ משכנתאות" loading="lazy" width="520" height="640"></div>
    <div class="guide__text">
      <span class="kicker">המדריך</span>
      <h2>לפעמים התשובה הנכונה היא <em>״עוד לא״</em></h2>
      <p>כואב לי לראות זוגות שחותמים על דירה, ורק אחרי החתימה מגלים שההחזר החודשי לא משאיר להם מרווח לנשום. לכן, כבר ארבע שנים, אני מתחיל כל ליווי <b>עוד לפני הבנק</b>. אני בודק איתכם את ההכנסות, ההוצאות והתוכניות שלכם, ורק אחר כך מחפש את המסלול.</p>
      <div class="stories">
        <article class="story glass"><span class="story__tag">מחיר למשתכן · ירושלים</span><p>לקוח אחד שלי חשש לקחת משכנתא על דירה במחיר למשתכן בירושלים. ישבנו יחד על המספרים, עד שהיה לו ברור איך ההחזר מסתדר.</p></article>
        <article class="story glass"><span class="story__tag">חיכה שנה-שנתיים</span><p>לקוח אחר הגיע אליי בטוח שהוא מוכן לקנות, והמלצתי לו לחכות שנה-שנתיים. לאחרונה הוא חזר, ועכשיו אנחנו עושים יחד את המשכנתא שלו.</p></article>
      </div>
    </div>
  </div>
</section>

{TRUST}
{STEPS}

<!-- CALCULATOR -->
<section class="sec" id="calc">
  <div class="wrap calc">
    <div class="calc__card glass glass--lit">
      <div class="sec__head sec__head--tight"><span class="kicker">מחשבון</span><h2>כמה יוצא <em>ההחזר החודשי?</em></h2></div>
      <div class="calc__body">
        <div class="calc__inputs">
          <div class="range" data-key="amount">
            <div class="range__top"><label for="c-amount">סכום המשכנתא</label><output id="o-amount"></output></div>
            <div class="range__ctl"><button type="button" class="pm" data-step="-50000" aria-label="הפחתה">−</button><input id="c-amount" type="range" min="200000" max="4000000" step="50000" value="1200000"><button type="button" class="pm" data-step="50000" aria-label="הוספה">+</button></div>
          </div>
          <div class="range" data-key="years">
            <div class="range__top"><label for="c-years">מספר שנים</label><output id="o-years"></output></div>
            <div class="range__ctl"><button type="button" class="pm" data-step="-1" aria-label="הפחתה">−</button><input id="c-years" type="range" min="5" max="30" step="1" value="25"><button type="button" class="pm" data-step="1" aria-label="הוספה">+</button></div>
          </div>
          <div class="range" data-key="rate">
            <div class="range__top"><label for="c-rate">ריבית משוערת</label><output id="o-rate"></output></div>
            <div class="range__ctl"><button type="button" class="pm" data-step="-0.1" aria-label="הפחתה">−</button><input id="c-rate" type="range" min="1" max="8" step="0.1" value="4.6"><button type="button" class="pm" data-step="0.1" aria-label="הוספה">+</button></div>
          </div>
        </div>
        <div class="calc__result">
          <span>החזר חודשי משוער</span>
          <strong><output id="o-pay">0</output> <small>₪</small></strong>
          <p class="calc__fine">הערכה בלבד. ההחזר בפועל תלוי בתמהיל, בבנק ובנתונים האישיים שלכם.</p>
        </div>
      </div>
    </div>
    <div class="calc__cta">
      <h3>מעוניינים לדעת מהו ההחזר המדויק? <em>אבחן אותו יחד איתכם.</em></h3>
      {form("lead-calc", variant)}
    </div>
  </div>
</section>

{TESTI}

<!-- 7 · TOO LATE -->
<section class="sec" id="late">
  <div class="wrap late">
    <div class="sec__head"><span class="kicker kicker--red">מה קורה כשבודקים מאוחר מדי</span><h2>חותמים קודם, <em class="red">בודקים אחר כך</em></h2></div>
    <div class="late__grid">
      <p>מי שחותם על דירה ורק אז מתחיל לבדוק משכנתא, בודק אחרי שכבר התחייב. אם הבנק מאשר פחות ממה שתכננתם, צריך למצוא את ההפרש ממקור אחר. ואם ההחזר החודשי יוצא גבוה מדי, כבר אי אפשר לוותר על העסקה בלי לשלם על כך, ואז נשארים עם החזר כבד לשנים ארוכות.</p>
      <div class="order">
        <div class="order__row order__row--bad glass"><span>חתימה</span><i></i><span>בדיקה</span><i></i><span>הפתעה</span></div>
        <div class="order__row order__row--good glass glass--lit"><span>בדיקה</span><i></i><span>מסלול</span><i></i><span>חתימה בשקט</span></div>
      </div>
    </div>
  </div>
</section>

<!-- 8 · FINAL CTA -->
<section class="sec sec--final" id="final">
  <div class="wrap final">
    <div class="final__copy">
      <h2>בואו נבדוק את זה ביחד, <em>לפני שחותמים</em></h2>
      <p>תארו לעצמכם את היום שבו אתם מקבלים את המפתח, ויודעים בדיוק כמה תשלמו כל חודש וכמה יישאר לכם. בלי הפתעות, ובלי חישובים בראש בתחילת כל חודש.</p>
      <p>השאירו פרטים, ואחזור אליכם לשיחה קצרה. נבדוק יחד אם ההחזר מתאים לכם, ואם כן, נמצא את המסלול הטוב ביותר עבורכם.</p>
    </div>
    <div class="final__form glass glass--lit">{form("lead-final", variant)}</div>
  </div>
</section>
</main>
''' + FOOTER + '\n<script src="site.js"></script>\n</body>\n</html>\n'

def thanks():
    return head("תודה · איציק דייטש", "הפרטים התקבלו.", "noindex,nofollow") + HEADER.replace('<a href="#guide">למה לבדוק קודם</a><a href="#trust">הגב שמאחוריי</a><a href="#steps">איך זה עובד</a><a href="#calc">מחשבון</a>', '<a href="#trust">הגב שמאחוריי</a><a href="#testimonials">המלצות</a><a href="#steps">איך זה עובד</a>').replace('<a class="btn btn--red btn--sm" href="#final">דברו איתי</a>', '') + '''
<main id="main">
<section class="hero hero--thanks">
  <div class="wrap thanks">
    <span class="thanks__check" aria-hidden="true"><svg viewBox="0 0 48 48"><path d="M13 25l7 7 15-16" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
    <h1>תודה, <em>הפרטים אצלי</em></h1>
    <p class="lede">אחזור אליכם תוך 24 שעות.</p>
    <div class="prep glass glass--lit">
      <p>כדי שנוכל להתחיל לבדוק כבר בשיחה, כדאי שיהיו לידכם:</p>
      <ul><li><b>מחיר הדירה</b></li><li><b>גובה ההון העצמי</b></li></ul>
    </div>
  </div>
</section>
''' + TRUST + TESTI + STEPS + '</main>\n' + FOOTER + '\n<script src="site.js"></script>\n</body>\n</html>\n'

(HERE / "index.html").write_text(landing("A"), encoding="utf-8")
(HERE / "b.html").write_text(landing("B"), encoding="utf-8")
(HERE / "thanks.html").write_text(thanks(), encoding="utf-8")
print("built index.html (A), b.html (B), thanks.html")
