# -*- coding: utf-8 -*-
"""מייצר את עמודי החובה (נגישות, פרטיות, תנאים, 404) באותו עיצוב. הרצה: python3 build_pages.py"""
BASE = "/itzik-deutsch-mortgage/"  # נתיב מוחלט — כדי שעמוד 404 יעבוד מכל עומק

def page(fname, title, lead, body, robots=True):
    return f'''<!doctype html>
<html lang="he" dir="rtl" data-font="plex" data-header="modern" data-hero="calm">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} — איציק דייטש</title>
<meta name="robots" content="noindex">
<link rel="icon" href="{BASE}favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="{BASE}favicon-32.png"><link rel="apple-touch-icon" href="{BASE}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Hebrew:wght@200;400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{BASE}m.css"><link rel="stylesheet" href="{BASE}fonts-switch.css"><link rel="stylesheet" href="{BASE}header.css"><link rel="stylesheet" href="{BASE}system.css"><link rel="stylesheet" href="{BASE}pages.css">
<script defer src="{BASE}header.js"></script>
</head>
<body>
<a class="skip" href="#main">דילוג לתוכן</a>
<header class="hd" id="nav" data-t="light">
  <div class="hd__in">
    <a class="brand" href="{BASE}" aria-label="איציק דייטש — לעמוד הבית"><img class="brand__logo brand__logo--d" src="{BASE}logo.png" alt="" width="60" height="34"><span>איציק דייטש<small>ייעוץ משכנתאות</small></span></a>
    <nav class="hd__links" aria-label="ראשי"><i class="hd__ind" aria-hidden="true"></i><a href="{BASE}#how">איך זה עובד</a><a href="{BASE}#calc">מחשבון</a><a href="{BASE}#about">מי אני</a><a href="{BASE}#faq">שאלות</a></nav>
    <div class="hd__end"><a class="btn btn--sm" href="{BASE}#contact">לשיחת היכרות</a></div>
    <button class="hd__menu" type="button" aria-expanded="false" aria-controls="menu"><span class="hd__burger" aria-hidden="true"><i></i><i></i></span><span class="hd__menu-t">תפריט</span></button>
  </div>
</header>
<div class="menu" id="menu" hidden>
  <nav class="menu__links" aria-label="תפריט מלא"><a href="{BASE}#how"><span>01</span>איך זה עובד</a><a href="{BASE}#calc"><span>02</span>מחשבון</a><a href="{BASE}#about"><span>03</span>מי אני</a><a href="{BASE}#faq"><span>04</span>שאלות</a><a href="{BASE}#contact"><span>05</span>יצירת קשר</a></nav>
  <div class="menu__foot"><a class="btn" href="{BASE}#contact">לשיחת היכרות חינם <span aria-hidden="true">←</span></a></div>
</div>
<main id="main" class="doc">
  <div class="wrap doc__in">
    <span class="micro">[ {title} ]</span>
    <h1 class="h2">{lead}</h1>
    {body}
  </div>
</main>
<footer class="docfoot"><div class="wrap foot__bar"><span>© איציק דייטש · עיצוב ובנייה: מירי דייטש</span><span><a href="{BASE}accessibility.html">הצהרת נגישות</a> · <a href="{BASE}privacy.html">מדיניות פרטיות</a> · <a href="{BASE}terms.html">תנאי שימוש</a></span></div></footer>
</body>
</html>
'''

DRAFT = '<p class="draft" role="note"><b>טיוטה לדוגמה.</b> הנוסח נכתב כבסיס בלבד ויש להשלים את הפרטים המסומנים [ בסוגריים ] ולאשר מול עורך/ת דין{extra} לפני עלייה לאוויר.</p>'

acc = DRAFT.format(extra=" ומורשה/ית נגישות") + '''
<p>אנחנו רואים חשיבות רבה במתן שירות שוויוני לכל הלקוחות, ופועלים כדי שהאתר יהיה נגיש לאנשים עם מוגבלות, בהתאם לחוק שוויון זכויות לאנשים עם מוגבלות, התשנ״ח–1998, לתקנות שוויון זכויות לאנשים עם מוגבלות (התאמות נגישות לשירות), התשע״ג–2013, ולתקן הישראלי ת״י 5568 המבוסס על הנחיות WCAG 2.0 ברמה AA.</p>
<h2 class="h3">מה נעשה באתר</h2>
<ul class="list">
<li>ניווט מלא במקלדת, כולל קישור "דילוג לתוכן" בתחילת כל עמוד וסימון פוקוס ברור.</li>
<li>ניגודיות צבעים של 4.5:1 לפחות לטקסט רגיל.</li>
<li>גודל טקסט גוף של 17–20 פיקסלים, ואפשרות הגדלה עד 200% בלי אובדן תוכן.</li>
<li>כיבוי אנימציות אוטומטי למשתמשים שהגדירו "הפחתת תנועה" במערכת ההפעלה.</li>
<li>כותרות במבנה היררכי, טקסט אמיתי (לא תמונות של טקסט) ותיאורים חלופיים לתמונות.</li>
<li>תוויות לכל שדות הטופס והמחשבון.</li>
<li>תמיכה מלאה בעברית ובכיווניות מימין לשמאל, ותצוגה מותאמת לטלפון, לטאבלט ולמחשב.</li>
<li>אזורי לחיצה בגודל 44 פיקסלים לפחות.</li>
</ul>
<h2 class="h3">מגבלות ידועות</h2>
<p>[ יש לפרט כאן רכיבים שעדיין אינם נגישים במלואם, אם קיימים, ואת מועד התיקון הצפוי. ]</p>
<h2 class="h3">רכז/ת נגישות ופניות</h2>
<p>נתקלתם בבעיית נגישות? נשמח לשמוע ולתקן.</p>
<ul class="list list--plain">
<li>שם: [ שם רכז/ת הנגישות ]</li>
<li>טלפון: <a href="tel:+972500000000" dir="ltr">[ 050-000-0000 ]</a></li>
<li>דוא״ל: [ כתובת דוא״ל ]</li>
</ul>
<p class="meta">תאריך עדכון ההצהרה: [ תאריך ] · תאריך בדיקת הנגישות האחרונה: [ תאריך ]</p>'''

priv = DRAFT.format(extra="") + '''
<p>מדיניות זו מסבירה איזה מידע נאסף באתר של איציק דייטש — ייעוץ משכנתאות, למה, ומה הזכויות שלכם, בהתאם לחוק הגנת הפרטיות, התשמ״א–1981 ותקנותיו.</p>
<h2 class="h3">איזה מידע נאסף</h2>
<ul class="list">
<li><b>טופס יצירת קשר:</b> שם, מספר טלפון ונושא הפנייה — רק אם בחרתם למלא ולשלוח.</li>
<li><b>המחשבון:</b> המספרים שאתם מזינים מחושבים בדפדפן שלכם בלבד, ואינם נשמרים או נשלחים.</li>
<li><b>מידע טכני:</b> האתר טוען פונט מ-Google Fonts, ולכן Google עשויה לקבל את כתובת ה-IP שלכם לצורך הצגת הפונט. [ אם יתווספו כלי סטטיסטיקה או פרסום — יש לפרט כאן. ]</li>
</ul>
<h2 class="h3">למה המידע משמש</h2>
<p>אך ורק כדי לחזור אליכם לגבי הפנייה ולתת את השירות שביקשתם. המידע לא נמכר ולא מועבר לצד שלישי, למעט [ ספק דיוור / מערכת ניהול לקוחות — אם יש ] ולפי דרישת דין.</p>
<h2 class="h3">אבטחה ושמירה</h2>
<p>[ פרטו היכן המידע נשמר, למשך כמה זמן, ואילו אמצעי אבטחה ננקטים. ]</p>
<h2 class="h3">הזכויות שלכם</h2>
<p>אתם רשאים לבקש לעיין במידע שנשמר עליכם, לתקן אותו או למחוק אותו. פנו אלינו: <a href="tel:+972500000000" dir="ltr">[ 050-000-0000 ]</a> · [ דוא״ל ].</p>
<p class="meta">עדכון אחרון: [ תאריך ]</p>'''

terms = DRAFT.format(extra="") + '''
<p>השימוש באתר כפוף לתנאים הבאים. הגלישה באתר מהווה הסכמה להם.</p>
<h2 class="h3">המידע באתר</h2>
<p>התכנים באתר, לרבות המחשבון, הדוגמאות והמספרים, נועדו להמחשה ולמידע כללי בלבד. הם אינם מהווים ייעוץ פיננסי, הצעה לקבלת הלוואה או התחייבות לתנאים כלשהם. תנאי משכנתא בפועל נקבעים על ידי הגוף המלווה ותלויים בנתונים האישיים שלכם.</p>
<h2 class="h3">המחשבון</h2>
<p>החישוב מבוסס על לוח שפיצר ועל ריבית קבועה לאורך כל התקופה, ואינו כולל הצמדה, עמלות או שינויי ריבית. הערכת החיסכון היא דוגמה ואינה הבטחה.</p>
<h2 class="h3">קניין רוחני</h2>
<p>העיצוב, הטקסטים, הלוגו והאיורים באתר שייכים ל[ שם העסק ] ואין להעתיקם ללא אישור בכתב.</p>
<h2 class="h3">אחריות</h2>
<p>[ השלימו סעיף הגבלת אחריות בנוסח שיאושר על ידי עורך/ת דין. ]</p>
<h2 class="h3">דין וסמכות שיפוט</h2>
<p>על התנאים יחול הדין הישראלי, וסמכות השיפוט הבלעדית נתונה לבתי המשפט ב[ עיר ].</p>
<p class="meta">עדכון אחרון: [ תאריך ]</p>'''

nf = '''<p>יכול להיות שהקישור ישן, או שהכתובת הוקלדה לא נכון. בניגוד לבנק — כאן אין שום עמלה על זה.</p>
<svg class="nf" viewBox="0 0 400 220" aria-hidden="true"><path d="M30 200h340M80 200V120l120-70 120 70v80" fill="none" stroke="currentColor" stroke-width="1.4" stroke-dasharray="6 6"/><text x="200" y="165" text-anchor="middle" font-size="44" font-weight="200" fill="currentColor">404</text></svg>
<p><a class="btn" href="/itzik-deutsch-mortgage/">חזרה לעמוד הבית <span aria-hidden="true">←</span></a></p>'''

for f, t, l, b in [
    ("accessibility.html", "הצהרת נגישות", "האתר נגיש <em class=\"acc\">לכולם.</em>", acc),
    ("privacy.html", "מדיניות פרטיות", "מה קורה עם <em class=\"acc\">המידע שלכם.</em>", priv),
    ("terms.html", "תנאי שימוש", "תנאי השימוש <em class=\"acc\">באתר.</em>", terms),
    ("404.html", "הדף לא נמצא", "הדף הזה <em class=\"acc\">לא נבנה.</em>", nf),
]:
    open(f, "w", encoding="utf-8").write(page(f, t, l, b))
print("ok")
