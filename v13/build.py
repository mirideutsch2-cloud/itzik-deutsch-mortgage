# -*- coding: utf-8 -*-
"""Itzik Deutsch · paid-ads landing (v13 · "glass world").
   Built from what worked in Miri's references: a cinematic dark 3D world (glass house on a neon
   platform, light strips, circuit floor, floating glass tiles), an interactive glass card with
   numbered steps in the hero, the logo's rounded diamond as the recurring shape, chips with a red
   underline, heavy display type. Blue leads; red = actions + the one warning.
   index.html = version A, b.html = version B (headline only), thanks.html.
   Run: python3 build.py"""
import pathlib

HERE = pathlib.Path(__file__).parent
WA_NUMBER = "972500000000"  # TODO: Itzik's real WhatsApp number
WA_TEXT = "היי איציק, אשמח לבדוק איתך את נושא המשכנתא"
WA_URL = f"https://wa.me/{WA_NUMBER}?text={WA_TEXT.replace(' ', '%20')}"
WA_ICON = '<svg viewBox="0 0 32 32" aria-hidden="true"><path fill="currentColor" d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3Zm0 23.6a10.6 10.6 0 0 1-5.4-1.5l-.4-.2-3.9 1 1-3.8-.2-.4A10.6 10.6 0 1 1 16 26.6Zm5.8-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7 0a8.7 8.7 0 0 1-4.3-3.8c-.3-.6.3-.5.9-1.7.1-.2 0-.4 0-.5l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.7 3.7 0 0 0-1.1 2.7 6.4 6.4 0 0 0 1.3 3.4 14.7 14.7 0 0 0 5.7 5c2.1.9 2.9 1 4 .8a3.4 3.4 0 0 0 2.2-1.6 2.8 2.8 0 0 0 .2-1.6c0-.2-.3-.3-.6-.4Z"/></svg>'


def lines(*ls):
    return "".join(f'<span class="ln"><span>{l}</span></span>' for l in ls)


HEADLINES = {
    "A": lines("מצאתם דירה", "ולא בטוחים", 'שתעמדו <em>בהחזר?</em>'),
    "B": lines("מצאתם דירה", "וכל בנק מציע לכם", '<em>החזר אחר?</em>'),
}


def chapter(name):
    return f'<p class="ch"><i class="dia"></i>{name}</p>'


def form(fid, variant, title="בדיקת החזר לפני החתימה"):
    return f'''<form class="card glass lead" id="{fid}" novalidate data-variant="{variant}">
  <p class="card__title">{title}</p>
  <fieldset class="card__step yn">
    <legend><b>1.</b> יש לכם הכנסה קבועה?</legend>
    <div class="chips"><label><input type="radio" name="income" value="yes" required><span>כן</span></label><label><input type="radio" name="income" value="no"><span>לא</span></label></div>
  </fieldset>
  <div class="card__step">
    <p class="card__label"><b>2.</b> איך חוזרים אליכם?</p>
    <div class="card__fields">
      <label class="field"><span class="sr">שם</span><input name="name" autocomplete="name" required placeholder="שם"></label>
      <label class="field"><span class="sr">טלפון</span><input name="phone" type="tel" inputmode="tel" autocomplete="tel" required dir="ltr" placeholder="טלפון"></label>
    </div>
  </div>
  <button class="btn btn--block" type="submit">איציק, אשמח שתחזור אליי</button>
  <p class="lead__note">אחזור אליכם תוך 24 שעות. השיחה הראשונה עליי.</p>
  <p class="lead__err" role="alert" hidden></p>
</form>'''


def header(landing=True):
    nav = '<nav class="hd__nav" aria-label="ניווט בדף"><a href="#guide">איציק</a><a href="#steps">איך זה עובד</a><a href="#calc">מחשבון</a><a href="#final">צור קשר</a></nav>' if landing else ''
    return f'''<header class="hd"><div class="hd__bar glass">
  <a class="hd__brand" href="#top" aria-label="איציק דייטש, לראש הדף"><img src="img/logo-dark.svg" alt="" width="50" height="30"><span>איציק דייטש<small>יועץ משכנתאות</small></span></a>
  {nav}
  <a class="btn btn--sm btn--wa" href="{WA_URL}" target="_blank" rel="noopener">{WA_ICON}<span>וואטסאפ</span></a>
</div></header>'''


TRUST = f'''<section class="trust sec" id="trust">
  <div class="wrap trust__grid">
    <div class="trust__copy">
      {chapter("הגב שמאחוריי")}
      <h2 class="h1">{lines("ליווי אישי,", "ומאחוריו <em>25 שנות ניסיון</em>")}</h2>
      <p>אני עובד בשיתוף פעולה עם חברה ותיקה שפועלת בתחום כבר 25 שנה. כך אתם מקבלים ליווי אישי ממני, ולצידו ניסיון של 25 שנה בהשגת ההצעות הטובות ביותר בשוק.</p>
      <div class="facts">
        <div class="fact glass"><b>כל הבנקים</b><span>אני בודק את התיק שלכם מול כל הבנקים, ולא רק מול אחד.</span></div>
        <div class="fact glass"><b>שני אנשי מקצוע</b><span>בפגישת הייעוץ יושבת איתנו גם נציגה מהחברה.</span></div>
      </div>
    </div>
    <div class="big-dia" aria-hidden="true"><div class="big-dia__shape"></div><span class="big-dia__num">25</span><span class="big-dia__cap">שנות ניסיון</span></div>
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
    <h2 class="h1">{lines("הדרך למשכנתא,", "<em>שלב אחרי שלב</em>")}</h2>
    <ol class="road">''' + "".join(
    f'<li class="road__step glass"><span class="road__dia"><b>{i+1}</b></span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS_LIST)) + '''</ol>
  </div>
</section>'''

TESTI = '<!-- המלצות: יוצגו כאן כשיגיעו 2-3 המלצות אמיתיות (לפני · מה עשינו · מה יצא) -->'

FOOTER = f'''<footer class="ft">
  <div class="wrap ft__in">
    <img src="img/logo-dark.svg" alt="איציק דייטש" width="60" height="36">
    <p>איציק דייטש · יועץ משכנתאות</p>
    <p class="ft__links"><a href="../accessibility.html">הצהרת נגישות</a><a href="../privacy.html">פרטיות</a><a href="../terms.html">תנאי שימוש</a></p>
    <p class="ft__credit">עיצוב: מירי דייטש</p>
  </div>
</footer>
<a class="wa" href="{WA_URL}" target="_blank" rel="noopener" aria-label="שלחו לאיציק הודעה בוואטסאפ">{WA_ICON}</a>'''


def head(title, desc, robots="index,follow"):
    return f'''<!doctype html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#070B22">
<link rel="icon" href="../favicon.ico">
<link rel="preload" as="image" href="img/hero-scene.webp">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Karantina:wght@700&family=IBM+Plex+Sans+Hebrew:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="site.css">
<script>document.documentElement.classList.add('js')</script>
</head>
<body id="top">
<a class="skip" href="#main">דילוג לתוכן</a>
'''

TILES = '<div class="tiles" aria-hidden="true">' + "".join(f'<i class="tile t{i}"></i>' for i in range(1, 7)) + '</div>'


def hero(v):
    return f'''<section class="hero" data-par>
  <div class="hero__bg" aria-hidden="true"><img src="img/hero-scene.webp" alt="" width="1920" height="1074" fetchpriority="high"></div>
  {TILES}
  <div class="hero__in">
    <div class="hero__copy">
      <p class="hero__who"><i class="dot"></i>איציק דייטש · יועץ משכנתאות</p>
      <h1 class="display">{HEADLINES[v]}</h1>
      <p class="lede">לפני שחותמים על החוזה, כדאי לדעת בוודאות איזה החזר חודשי תוכלו לעמוד בו לאורך זמן.</p>
      {form("lead-hero", v)}
      <p class="hero__p">אני איציק דייטש, יועץ משכנתאות. את הבדיקה הזאת אני עושה איתכם, ולאחר מכן משווה עבורכם בין הצעות כל הבנקים עד שנגיע למסלול המתאים לכם ביותר. <b>ואם זה לא העיתוי הנכון, אמליץ לכם לחכות.</b></p>
      <ul class="chips-u">
        <li class="glass">כל הבנקים</li><li class="glass">25 שנות ניסיון</li><li class="glass">השיחה הראשונה עליי</li>
      </ul>
    </div>
  </div>
</section>'''


def landing(v):
    return head("איציק דייטש · יועץ משכנתאות",
                "לפני שחותמים על החוזה, כדאי לדעת בוודאות איזה החזר חודשי תוכלו לעמוד בו לאורך זמן.") + header() + f'''
<main id="main">
{hero(v)}

<!-- 2 · הבעיה -->
<section class="problem sec">
  <span class="neon neon--v" aria-hidden="true"></span>
  <div class="wrap">
    {chapter("הבעיה")}
    <h2 class="h1">{lines("החתימה מתקרבת,", "<em>והשאלה החשובה עדיין פתוחה</em>")}</h2>
    <div class="problem__grid">
      <div class="problem__copy">
        <p>מצאתם דירה, והמוכר מחכה לתשובה. רגע לפני שחותמים, חשוב לוודא שההחזר החודשי ישאיר לכם מספיק כדי לחיות בנוחות, לאורך כל שנות המשכנתא.</p>
        <p>הבנק יבדוק כמה הוא מוכן להלוות לכם, ומה הוא ירוויח מזה. הוא לא יבדוק מה היכולות שלכם, וכמה אתם יכולים לחסוך.</p>
      </div>
      <div class="ledger glass">
        <div class="ledger__col"><h3>הבנק בודק</h3><p><i class="ok"></i>כמה הוא מוכן להלוות לכם</p><p><i class="ok"></i>מה הוא ירוויח מזה</p></div>
        <div class="ledger__col ledger__col--no"><h3>הבנק לא בודק</h3><p><i class="no"></i><s>מה היכולות שלכם</s></p><p><i class="no"></i><s>כמה אתם יכולים לחסוך</s></p></div>
      </div>
    </div>
    <blockquote class="pull">{lines("הדירה החדשה אמורה להביא לכם שקט,", "<em>גם בתחילת כל חודש.</em>")}</blockquote>
  </div>
</section>

<!-- 3 · המדריך -->
<section class="guide sec" id="guide">
  <div class="wrap guide__grid">
    <figure class="guide__photo"><span class="guide__dia" aria-hidden="true"></span><img src="img/itzik-cut.webp" alt="איציק דייטש, יועץ משכנתאות" width="520" height="640" loading="lazy"><figcaption class="glass">איציק דייטש<span>יועץ משכנתאות · 4 שנים בתחום</span></figcaption></figure>
    <div class="guide__copy">
      {chapter("איציק")}
      <h2 class="h1">{lines("לפעמים התשובה הנכונה", "היא <em>״עוד לא״</em>")}</h2>
      <p>כואב לי לראות זוגות שחותמים על דירה, ורק אחרי החתימה מגלים שההחזר החודשי לא משאיר להם מרווח לנשום. לכן, כבר ארבע שנים, אני מתחיל כל ליווי עוד לפני הבנק. אני בודק איתכם את ההכנסות, ההוצאות והתוכניות שלכם, ורק אחר כך מחפש את המסלול.</p>
      <div class="cases">
        <article class="case glass"><span class="case__tag">ירושלים · מחיר למשתכן</span><p>לקוח אחד שלי חשש לקחת משכנתא על דירה במחיר למשתכן בירושלים. ישבנו יחד על המספרים, עד שהיה לו ברור איך ההחזר מסתדר.</p></article>
        <article class="case glass"><span class="case__tag">חיכה שנה-שנתיים</span><p>לקוח אחר הגיע אליי בטוח שהוא מוכן לקנות, והמלצתי לו לחכות שנה-שנתיים. לאחרונה הוא חזר, ועכשיו אנחנו עושים יחד את המשכנתא שלו.</p></article>
      </div>
    </div>
  </div>
</section>

{TRUST}
{STEPS}

<!-- מחשבון -->
<section class="calc sec" id="calc">
  <div class="circuit" aria-hidden="true"></div>
  <div class="wrap">
    {chapter("מחשבון")}
    <div class="calc__grid">
      <div class="calc__card glass">
        <h2 class="h2">כמה יוצא ההחזר החודשי?</h2>
        <div class="rng"><p class="rng__label"><b>1.</b> סכום המשכנתא</p><div class="rng__ctl"><button type="button" class="pm" data-for="c-amount" data-step="50000" aria-label="הוספה">+</button><div class="rng__track"><output class="bubble" id="o-amount" dir="ltr"></output><input id="c-amount" type="range" min="200000" max="4000000" step="50000" value="1200000" aria-label="סכום המשכנתא"></div><button type="button" class="pm" data-for="c-amount" data-step="-50000" aria-label="הפחתה">−</button></div></div>
        <div class="rng"><p class="rng__label"><b>2.</b> מספר שנים</p><div class="rng__ctl"><button type="button" class="pm" data-for="c-years" data-step="1" aria-label="הוספה">+</button><div class="rng__track"><output class="bubble" id="o-years"></output><input id="c-years" type="range" min="5" max="30" step="1" value="25" aria-label="מספר שנים"></div><button type="button" class="pm" data-for="c-years" data-step="-1" aria-label="הפחתה">−</button></div></div>
        <div class="rng"><p class="rng__label"><b>3.</b> ריבית משוערת</p><div class="rng__ctl"><button type="button" class="pm" data-for="c-rate" data-step="0.1" aria-label="הוספה">+</button><div class="rng__track"><output class="bubble" id="o-rate" dir="ltr"></output><input id="c-rate" type="range" min="1" max="8" step="0.1" value="4.6" aria-label="ריבית משוערת"></div><button type="button" class="pm" data-for="c-rate" data-step="-0.1" aria-label="הפחתה">−</button></div></div>
      </div>
      <div class="calc__out" aria-live="polite">
        <p class="calc__label">ההחזר החודשי המשוער שלכם</p>
        <p class="calc__num"><output id="o-pay">0</output><span>₪</span></p>
        <p class="calc__fine">הערכה בלבד. ההחזר בפועל תלוי בתמהיל, בבנק ובנתונים האישיים שלכם.</p>
      </div>
    </div>
    <div class="calc__cta">
      <h3 class="h2">מעוניינים לדעת מהו ההחזר המדויק? <em>אבחן אותו יחד איתכם.</em></h3>
      {form("lead-calc", v, "ההחזר המדויק, יחד איתי")}
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
      <div class="order">
        <div class="order__row order__row--bad glass"><span>חתימה</span><i></i><span>בדיקה</span><i></i><span>החזר כבד לשנים</span></div>
        <div class="order__row order__row--good glass"><span>בדיקה</span><i></i><span>מסלול</span><i></i><span>חתימה בשקט</span></div>
      </div>
    </div>
  </div>
</section>

<!-- 8 · סוף טוב -->
<section class="final sec" id="final">
  <div class="wrap final__grid">
    <div class="final__copy">
      <h2 class="h1">{lines("בואו נבדוק את זה ביחד,", "<em>לפני שחותמים</em>")}</h2>
      <p>תארו לעצמכם את היום שבו אתם מקבלים את המפתח, ויודעים בדיוק כמה תשלמו כל חודש וכמה יישאר לכם. בלי הפתעות, ובלי חישובים בראש בתחילת כל חודש.</p>
      <p>השאירו פרטים, ואחזור אליכם לשיחה קצרה. נבדוק יחד אם ההחזר מתאים לכם, ואם כן, נמצא את המסלול הטוב ביותר עבורכם.</p>
      {form("lead-final", v, "בואו נבדוק ביחד")}
    </div>
    <figure class="final__key" aria-hidden="true" data-par-el><img src="img/key.webp" alt="" width="1168" height="880" decoding="async"></figure>
  </div>
</section>
</main>
''' + FOOTER + '\n<script src="site.js"></script>\n</body>\n</html>\n'


def thanks():
    return head("תודה · איציק דייטש", "הפרטים התקבלו.", "noindex,nofollow") + header(False) + f'''
<main id="main">
<section class="hero hero--thanks" data-par>
  <div class="hero__bg" aria-hidden="true"><img src="img/hero-scene.webp" alt="" width="1920" height="1074"></div>
  {TILES}
  <div class="hero__in">
    <div class="hero__copy">
      <h1 class="display">{lines("תודה,", "<em>הפרטים אצלי</em>")}</h1>
      <p class="lede">אחזור אליכם תוך 24 שעות.</p>
      <div class="card glass prep">
        <p class="card__title">כדי שנוכל להתחיל לבדוק כבר בשיחה, כדאי שיהיו לידכם:</p>
        <ul><li><b>1.</b> מחיר הדירה</li><li><b>2.</b> גובה ההון העצמי</li></ul>
      </div>
    </div>
  </div>
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
