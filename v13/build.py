# -*- coding: utf-8 -*-
"""Itzik Deutsch · paid-ads landing (v13, per miri-web-design).
   index.html = version A, b.html = version B (only the headline differs), thanks.html.
   Type: Karantina (display) + IBM Plex Sans Hebrew (text) — the pair approved for Itzik.
   Run: python3 build.py"""
import pathlib

HERE = pathlib.Path(__file__).parent
WA_NUMBER = "972500000000"  # TODO: Itzik's real WhatsApp number
WA_TEXT = "היי איציק, אשמח לבדוק איתך את נושא המשכנתא"


def lines(*ls):
    """Headline set by hand: each line masked so it can rise in."""
    return "".join(f'<span class="ln"><span>{l}</span></span>' for l in ls)


HEADLINES = {
    "A": lines("מצאתם דירה", "ולא בטוחים", 'שתעמדו <em>בהחזר?</em>'),
    "B": lines("מצאתם דירה", "וכל בנק מציע לכם", '<em>החזר אחר?</em>'),
}


def chapter(name):
    return f'<p class="ch"><i></i>{name}</p>'


def form(fid, variant, dark=True):
    return f'''<form class="lead{' lead--dark' if dark else ''}" id="{fid}" novalidate data-variant="{variant}">
  <label class="field"><span>שם</span><input name="name" autocomplete="name" required></label>
  <label class="field"><span>טלפון</span><input name="phone" type="tel" inputmode="tel" autocomplete="tel" required dir="ltr"></label>
  <fieldset class="yn">
    <legend>יש לכם הכנסה קבועה?</legend>
    <div class="yn__opts"><label><input type="radio" name="income" value="yes" required><span>כן</span></label><label><input type="radio" name="income" value="no"><span>לא</span></label></div>
  </fieldset>
  <button class="btn" type="submit">איציק, אשמח שתחזור אליי</button>
  <p class="lead__note">אחזור אליכם תוך 24 שעות. השיחה הראשונה עליי.</p>
  <p class="lead__err" role="alert" hidden></p>
</form>'''


def header(cta=True):
    return f'''<header class="hd">
  <a class="hd__brand" href="#top" aria-label="איציק דייטש, לראש הדף"><img src="img/logo-dark.svg" alt="" width="52" height="31"><span>איציק דייטש<small>ייעוץ משכנתאות</small></span></a>
  {'<a class="btn btn--sm" href="#final">בדיקת החזר</a>' if cta else ''}
</header>'''


TRUST = f'''<section class="trust fx" id="trust">
  <div class="trust__num" aria-hidden="true">25</div>
  <div class="trust__copy">
    {chapter("הגב שמאחוריי")}
    <h2 class="h1">{lines("ליווי אישי,", "ומאחוריו <em>25 שנות ניסיון</em>")}</h2>
    <p>אני עובד בשיתוף פעולה עם חברה ותיקה שפועלת בתחום כבר 25 שנה. כך אתם מקבלים ליווי אישי ממני, ולצידו ניסיון של 25 שנה בהשגת ההצעות הטובות ביותר בשוק.</p>
    <dl class="facts">
      <div><dt>כל הבנקים</dt><dd>אני בודק את התיק שלכם מול כל הבנקים, ולא רק מול אחד.</dd></div>
      <div><dt>שני אנשי מקצוע</dt><dd>בפגישת הייעוץ יושבת איתנו גם נציגה מהחברה.</dd></div>
    </dl>
  </div>
</section>'''

STEPS_LIST = [
    ("שיחת היכרות", "שיחה קצרה בטלפון, שבה אני מבין מה אתם צריכים ובאיזה שלב אתם נמצאים."),
    ("מסמכים", "אתם שולחים לי את המסמכים, ואני עובר עליהם לפני שאנחנו נפגשים."),
    ("פגישת ייעוץ", "יושבים יחד ובודקים איזה החזר חודשי באמת מתאים לכם."),
    ("מול הבנקים", "אני מגיש את התיק לכל הבנקים, עד שמתקבל אישור עקרוני עם ההצעה הטובה ביותר."),
    ("עד הסוף", "אני מלווה אתכם עד שהמשכנתא מאושרת והכסף מועבר."),
]
STEPS = f'''<section class="steps sec" id="steps">
  <div class="wrap">
    {chapter("איך זה עובד")}
    <h2 class="h1">{lines("הדרך למשכנתא,", "שלב אחרי שלב")}</h2>
    <ol class="road fx">''' + "".join(
    f'<li><span class="road__dot"></span><h3>{t}</h3><p>{d}</p></li>' for t, d in STEPS_LIST) + '''</ol>
  </div>
</section>'''

# Testimonials: per the skill, never invented and hidden until real ones (name + city + a number) arrive.
TESTI = '<!-- המלצות: יוצגו כאן כשיגיעו 2-3 המלצות אמיתיות (לפני · מה עשינו · מה יצא) -->'

FOOTER = f'''<footer class="ft">
  <div class="wrap ft__in">
    <img src="img/logo-dark.svg" alt="איציק דייטש" width="60" height="36">
    <p>איציק דייטש · ייעוץ משכנתאות</p>
    <p class="ft__links"><a href="../accessibility.html">הצהרת נגישות</a><a href="../privacy.html">פרטיות</a><a href="../terms.html">תנאי שימוש</a></p>
    <p class="ft__credit">עיצוב: מירי דייטש</p>
  </div>
</footer>
<a class="wa" href="https://wa.me/{WA_NUMBER}?text={WA_TEXT.replace(' ', '%20')}" target="_blank" rel="noopener" aria-label="שלחו לאיציק הודעה בוואטסאפ">
  <svg viewBox="0 0 32 32" aria-hidden="true"><path fill="currentColor" d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3Zm0 23.6a10.6 10.6 0 0 1-5.4-1.5l-.4-.2-3.9 1 1-3.8-.2-.4A10.6 10.6 0 1 1 16 26.6Zm5.8-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7 0a8.7 8.7 0 0 1-4.3-3.8c-.3-.6.3-.5.9-1.700.1-.2 0-.4 0-.5l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.7 3.7 0 0 0-1.1 2.7 6.4 6.4 0 0 0 1.3 3.4 14.7 14.7 0 0 0 5.7 5c2.1.9 2.9 1 4 .8a3.4 3.4 0 0 0 2.2-1.6 2.8 2.8 0 0 0 .2-1.6c0-.2-.3-.3-.6-.4Z"/></svg>
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
<meta name="theme-color" content="#0D1135">
<link rel="icon" href="../favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Karantina:wght@700&family=IBM+Plex+Sans+Hebrew:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="site.css">
<script>document.documentElement.classList.add('js')</script>
</head>
<body id="top">
<a class="skip" href="#main">דילוג לתוכן</a>
'''


def landing(v):
    return head("איציק דייטש · ייעוץ משכנתאות",
                "לפני שחותמים על החוזה, כדאי לדעת בוודאות איזה החזר חודשי תוכלו לעמוד בו לאורך זמן.") + header() + f'''
<main id="main">

<!-- 1 · פתיחה -->
<section class="hero fx">
  <div class="hero__copy">
    <p class="hero__who">איציק דייטש, יועץ משכנתאות</p>
    <h1 class="display">{HEADLINES[v]}</h1>
    <p class="lede">לפני שחותמים על החוזה, כדאי לדעת בוודאות איזה החזר חודשי תוכלו לעמוד בו לאורך זמן.</p>
    <p class="hero__p">אני איציק דייטש, יועץ משכנתאות. את הבדיקה הזאת אני עושה איתכם, ולאחר מכן משווה עבורכם בין הצעות כל הבנקים עד שנגיע למסלול המתאים לכם ביותר. ואם זה לא העיתוי הנכון, אמליץ לכם לחכות.</p>
  </div>
  <div class="hero__form">{form("lead-hero", v)}</div>
  <figure class="hero__house" aria-hidden="true"><img src="img/glass-house.webp" alt="" width="1024" height="1024" fetchpriority="high"></figure>
</section>

<!-- 2 · הבעיה -->
<section class="problem sec">
  <div class="wrap">
    {chapter("הבעיה")}
    <h2 class="h1">{lines("החתימה מתקרבת,", "<em>והשאלה החשובה עדיין פתוחה</em>")}</h2>
    <div class="problem__grid">
      <div class="problem__copy">
        <p>מצאתם דירה, והמוכר מחכה לתשובה. רגע לפני שחותמים, חשוב לוודא שההחזר החודשי ישאיר לכם מספיק כדי לחיות בנוחות, לאורך כל שנות המשכנתא.</p>
        <p>הבנק יבדוק כמה הוא מוכן להלוות לכם, ומה הוא ירוויח מזה. הוא לא יבדוק מה היכולות שלכם, וכמה אתם יכולים לחסוך.</p>
      </div>
      <div class="ledger fx" aria-label="מה הבנק בודק ומה לא">
        <div class="ledger__col"><h3>הבנק בודק</h3><p>כמה הוא מוכן להלוות לכם</p><p>מה הוא ירוויח מזה</p></div>
        <div class="ledger__col ledger__col--no"><h3>הבנק לא בודק</h3><p><s>מה היכולות שלכם</s></p><p><s>כמה אתם יכולים לחסוך</s></p></div>
      </div>
    </div>
    <blockquote class="pull fx">{lines("הדירה החדשה אמורה להביא לכם שקט,", "<em>גם בתחילת כל חודש.</em>")}</blockquote>
  </div>
</section>

<!-- 3 · המדריך -->
<section class="guide sec">
  <div class="wrap guide__grid">
    <figure class="guide__photo fx"><img src="img/itzik-cut.webp" alt="איציק דייטש, יועץ משכנתאות" width="520" height="640" loading="lazy"></figure>
    <div class="guide__copy">
      {chapter("איציק")}
      <h2 class="h1">{lines("לפעמים התשובה הנכונה", "היא <em>״עוד לא״</em>")}</h2>
      <p>כואב לי לראות זוגות שחותמים על דירה, ורק אחרי החתימה מגלים שההחזר החודשי לא משאיר להם מרווח לנשום. לכן, כבר ארבע שנים, אני מתחיל כל ליווי עוד לפני הבנק. אני בודק איתכם את ההכנסות, ההוצאות והתוכניות שלכם, ורק אחר כך מחפש את המסלול.</p>
      <div class="cases">
        <article><h3>ירושלים, מחיר למשתכן</h3><p>לקוח אחד שלי חשש לקחת משכנתא על דירה במחיר למשתכן בירושלים. ישבנו יחד על המספרים, עד שהיה לו ברור איך ההחזר מסתדר.</p></article>
        <article><h3>חיכה שנה-שנתיים</h3><p>לקוח אחר הגיע אליי בטוח שהוא מוכן לקנות, והמלצתי לו לחכות שנה-שנתיים. לאחרונה הוא חזר, ועכשיו אנחנו עושים יחד את המשכנתא שלו.</p></article>
      </div>
    </div>
  </div>
</section>

<!-- 4 · למה לסמוך -->
{TRUST}

<!-- 5 · איך זה עובד -->
{STEPS}

<!-- מחשבון -->
<section class="calc sec" id="calc">
  <div class="wrap">
    {chapter("מחשבון")}
    <div class="calc__grid">
      <div class="calc__inputs">
        <h2 class="h2">כמה יוצא ההחזר החודשי?</h2>
        <div class="rng"><div class="rng__top"><label for="c-amount">סכום המשכנתא</label><output id="o-amount" dir="ltr"></output></div><input id="c-amount" type="range" min="200000" max="4000000" step="50000" value="1200000"></div>
        <div class="rng"><div class="rng__top"><label for="c-years">מספר שנים</label><output id="o-years"></output></div><input id="c-years" type="range" min="5" max="30" step="1" value="25"></div>
        <div class="rng"><div class="rng__top"><label for="c-rate">ריבית משוערת</label><output id="o-rate" dir="ltr"></output></div><input id="c-rate" type="range" min="1" max="8" step="0.1" value="4.6"></div>
      </div>
      <div class="calc__out" aria-live="polite">
        <p class="calc__label">ההחזר החודשי המשוער שלכם</p>
        <p class="calc__num"><output id="o-pay">0</output><span>₪</span></p>
        <p class="calc__fine">הערכה בלבד. ההחזר בפועל תלוי בתמהיל, בבנק ובנתונים האישיים שלכם.</p>
      </div>
    </div>
    <div class="calc__cta">
      <h3 class="h2">מעוניינים לדעת מהו ההחזר המדויק? <em>אבחן אותו יחד איתכם.</em></h3>
      {form("lead-calc", v, dark=False)}
    </div>
  </div>
</section>

{TESTI}

<!-- 7 · מאוחר מדי -->
<section class="late sec">
  <div class="wrap">
    {chapter("מה קורה כשבודקים מאוחר מדי")}
    <h2 class="h1">{lines("חותמים קודם,", '<em class="red">בודקים אחר כך</em>')}</h2>
    <div class="late__grid">
      <p>מי שחותם על דירה ורק אז מתחיל לבדוק משכנתא, בודק אחרי שכבר התחייב. אם הבנק מאשר פחות ממה שתכננתם, צריך למצוא את ההפרש ממקור אחר. ואם ההחזר החודשי יוצא גבוה מדי, כבר אי אפשר לוותר על העסקה בלי לשלם על כך, ואז נשארים עם החזר כבד לשנים ארוכות.</p>
      <div class="order fx">
        <div class="order__row order__row--bad"><span>חתימה</span><span>בדיקה</span><span>החזר כבד לשנים</span></div>
        <div class="order__row order__row--good"><span>בדיקה</span><span>מסלול</span><span>חתימה בשקט</span></div>
      </div>
    </div>
  </div>
</section>

<!-- 8 · סוף טוב -->
<section class="final fx" id="final">
  <figure class="final__house" aria-hidden="true"><img src="img/glass-house.webp" alt="" width="1024" height="1024" loading="lazy"></figure>
  <div class="final__copy">
    <h2 class="h1">{lines("בואו נבדוק את זה ביחד,", "<em>לפני שחותמים</em>")}</h2>
    <p>תארו לעצמכם את היום שבו אתם מקבלים את המפתח, ויודעים בדיוק כמה תשלמו כל חודש וכמה יישאר לכם. בלי הפתעות, ובלי חישובים בראש בתחילת כל חודש.</p>
    <p>השאירו פרטים, ואחזור אליכם לשיחה קצרה. נבדוק יחד אם ההחזר מתאים לכם, ואם כן, נמצא את המסלול הטוב ביותר עבורכם.</p>
    {form("lead-final", v)}
  </div>
</section>
</main>
''' + FOOTER + '\n<script src="site.js"></script>\n</body>\n</html>\n'


def thanks():
    return head("תודה · איציק דייטש", "הפרטים התקבלו.", "noindex,nofollow") + header(cta=False) + f'''
<main id="main">
<section class="hero hero--thanks fx">
  <div class="hero__copy">
    <h1 class="display">{lines("תודה,", "<em>הפרטים אצלי</em>")}</h1>
    <p class="lede">אחזור אליכם תוך 24 שעות.</p>
    <p class="hero__p">כדי שנוכל להתחיל לבדוק כבר בשיחה, כדאי שיהיו לידכם <b>מחיר הדירה</b> ו<b>גובה ההון העצמי</b>.</p>
  </div>
  <figure class="hero__house" aria-hidden="true"><img src="img/glass-house.webp" alt="" width="1024" height="1024"></figure>
</section>
{TRUST}
{TESTI}
{STEPS}
</main>
''' + FOOTER + '\n<script src="site.js"></script>\n</body>\n</html>\n'


(HERE / "index.html").write_text(landing("A"), encoding="utf-8")
(HERE / "b.html").write_text(landing("B"), encoding="utf-8")
(HERE / "thanks.html").write_text(thanks(), encoding="utf-8")
print("built index.html (A), b.html (B), thanks.html")
