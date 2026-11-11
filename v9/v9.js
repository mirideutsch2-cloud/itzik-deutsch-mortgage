// איציק דייטש v9 — סיפור בפרקים. בלי ספריות.
(() => {
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const wide = () => innerWidth > 900;
  const fmt = n => Math.round(n).toLocaleString('en-US');

  // פתיחה
  $$('.hero__kicker, .hero__title span, .hero__cta, .hero__proof').forEach((el, i) => { el.classList.add('rv'); el.style.transitionDelay = (0.15 + i * 0.12) + 's'; });
  setTimeout(() => document.documentElement.classList.add('ready'), 60);

  // חשיפה
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .2 });
  $$('.home__copy, .me__copy, .me__facts, .end .h2, .quotes, .invite__title, .form').forEach(el => { el.classList.add('rv-s'); io.observe(el); });

  // הדר: בהיר מעל רקע בהיר
  const hd = $('#hd'), dark = $$('.hero, .bank, .end, .invite, .ft, .step--dark, .step--acc, .step--img');
  function headerTone() {
    const y = 40, x = innerWidth / 2;
    const onDark = dark.some(el => { const r = el.getBoundingClientRect(); return r.top <= y && r.bottom >= y && r.left <= x && r.right >= x; });
    hd.classList.toggle('is-light', !onDark);
  }

  // פרק 2 — המספר של הבנק
  const iAmt = $('#iAmt'), iYrs = $('#iYrs'), iRate = $('#iRate');
  let interest = 0, principal = 0, shown = 0, progress = reduce ? 1 : 0;
  function calc() {
    principal = +iAmt.value; const n = +iYrs.value * 12, i = +iRate.value / 1200;
    const pay = principal * i / (1 - Math.pow(1 + i, -n));
    interest = pay * n - principal;
    // חיסכון משוער: ‎0.4%‎ פחות ריבית בתמהיל
    const i2 = Math.max(+iRate.value - .4, .5) / 1200, pay2 = principal * i2 / (1 - Math.pow(1 + i2, -n));
    const save = (pay - pay2) * n;
    $('#vAmt').textContent = $('#oAmt').textContent = '₪' + fmt(principal);
    $('#vYrs').textContent = iYrs.value + ' שנה'; $('#oYrs').textContent = iYrs.value;
    $('#vRate').textContent = (+iRate.value).toFixed(1) + '%';
    $('#saveNum').textContent = fmt(Math.round(save / 1000) * 1000);
    $('#waitNum').textContent = fmt(pay - pay2);
    paintBank();
  }
  function paintBank() {
    const v = interest * Math.min(1, progress / .55);
    $('#bankNum').textContent = fmt(v);
    const tot = principal + interest, g = Math.min(1, progress / .55);
    $('#barHome').style.width = (principal / tot * 100 * g) + '%';
    $('#barBank').style.width = (interest / tot * 100 * g) + '%';
  }
  [iAmt, iYrs, iRate].forEach(el => el.addEventListener('input', () => { progress = 1; calc(); }));

  // פרק 4 — רצועה אופקית
  const road = $('.road'), track = $('#track');
  function sizeRoad() {
    if (!wide() || reduce) { road.style.height = ''; track.style.transform = ''; return; }
    const dist = track.scrollWidth - innerWidth;
    road.style.height = (innerHeight + Math.max(0, dist)) + 'px';
  }

  const bank = $('.bank__scroll');
  let ticking = false;
  function onScroll() {
    ticking = false; headerTone();
    if (!reduce) {
      const r = bank.getBoundingClientRect();
      const span = wide() ? bank.offsetHeight - innerHeight : innerHeight * .8;
      const p = wide() ? Math.min(1, Math.max(0, -r.top / span)) : Math.min(1, Math.max(0, (innerHeight - r.top) / span - .3));
      if (p > progress) { progress = p; paintBank(); }
      if (wide()) {
        const rr = road.getBoundingClientRect(), dist = track.scrollWidth - innerWidth;
        const q = Math.min(1, Math.max(0, -rr.top / (road.offsetHeight - innerHeight || 1)));
        track.style.transform = `translateX(${q * dist}px)`; // RTL: התוכן ממשיך שמאלה
      }
    }
  }
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  addEventListener('resize', () => { sizeRoad(); onScroll(); });

  // פרק 5 — ציטוט אחד בכל פעם
  const qs = $$('.q'); let qi = 0;
  $('.quotes__nav') && $('.quotes__nav').addEventListener('click', e => {
    const b = e.target.closest('button'); if (!b) return;
    qs[qi].classList.remove('is-on'); qi = (qi + +b.dataset.q + qs.length) % qs.length; qs[qi].classList.add('is-on');
    $('#qi').textContent = (qi + 1) + ' / ' + qs.length;
  });

  // תפריט מובייל
  const mb = $('.hd__menu'), mn = $('#mnav');
  const setMenu = open => { mb.setAttribute('aria-expanded', open); mn.hidden = !open; document.body.style.overflow = open ? 'hidden' : ''; };
  mb.addEventListener('click', () => setMenu(mn.hidden));
  mn.addEventListener('click', e => { if (e.target.closest('a')) setMenu(false); });
  addEventListener('keydown', e => { if (e.key === 'Escape' && !mn.hidden) { setMenu(false); mb.focus(); } });

  calc(); sizeRoad(); onScroll();
  addEventListener('load', () => { sizeRoad(); onScroll(); });
})();
