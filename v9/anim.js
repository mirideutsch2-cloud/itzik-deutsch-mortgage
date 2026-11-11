// תנועה + הדר חכם
(() => {
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fmt = n => Math.round(n).toLocaleString('en-US');
  document.documentElement.classList.add('js-anim');

  // כותרות: שורה-שורה עולות מתוך מסכה (מפצלים לפי <br> בלבד — בלי לשבור מילים)
  $$('.home .h2, .bank__top .h2, .me__quote, .road__head .h2, .end .h2, .invite__title, .magic__head .h2').forEach(h => {
    const parts = h.innerHTML.split(/<br\s*\/?>/i);
    h.innerHTML = parts.map(p => `<span class="ln"><span>${p}</span></span>`).join('');
    h.classList.add('a-lines');
  });
  $$('.home__img, .me__img').forEach(el => el.classList.add('a-img'));
  $$('.home__copy .lead, .me__sig, .me__story, .me__facts, .bank__after > *, .end__scene, .invite__what, .form, .magic__switch, .magic__mix, .magic__stats').forEach(el => { el.classList.remove('rv-s'); el.classList.add('a-up'); });

  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .18, rootMargin: '0px 0px -6% 0px' });
  $$('.a-lines, .a-img, .chap, .a-up').forEach(el => io.observe(el));

  // "0 · 3 · 1" נספרים כשנכנסים
  const countIO = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return; countIO.unobserve(e.target);
    const el = e.target, to = +el.textContent; if (reduce || !to) return;
    const t0 = performance.now();
    const tick = now => { const p = Math.min(1, (now - t0) / 1200); el.textContent = Math.round(to * (1 - Math.pow(1 - p, 3))); if (p < 1) requestAnimationFrame(tick); };
    el.textContent = 0; requestAnimationFrame(tick);
  }), { threshold: .6 });
  $$('.me__facts b').forEach(b => countIO.observe(b));

  // ── הדר חכם: פרק פעיל + מחוון שגולש + פס התקדמות ──
  const hd = $('#hd'), nav = $('.hd__nav'), ind = $('.hd__ind'), links = $$('.hd__nav a[data-sec]');
  const secs = links.map(a => document.getElementById(a.dataset.sec));
  let active = null;
  function moveInd(a) {
    if (!a || !nav.offsetWidth) { ind.style.opacity = 0; return; }
    const nr = nav.getBoundingClientRect(), r = a.getBoundingClientRect();
    ind.style.width = r.width + 'px'; ind.style.transform = `translateX(${r.left - nr.left}px)`; ind.style.opacity = 1;
  }
  function spy() {
    const y = innerHeight * .4; let cur = null;
    secs.forEach((s, i) => { if (!s) return; const r = s.getBoundingClientRect(); if (r.top <= y && r.bottom > y) cur = links[i]; });
    if (cur !== active) { links.forEach(a => a.classList.toggle('is-on', a === cur)); active = cur; moveInd(cur); }
    const max = document.documentElement.scrollHeight - innerHeight;
    $('#hdProg').style.transform = `scaleX(${max > 0 ? scrollY / max : 0})`;
  }
  let ticking = false;
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(() => { ticking = false; spy(); }); } }, { passive: true });
  addEventListener('resize', () => moveInd(active));

  // ── הכפתור בהדר הופך אישי: אחרי שהגולש שיחק במספרים, הוא רואה כמה מחכה לו ──
  let shown = 0;
  const num = sel => +((($(sel) || {}).textContent || '0').replace(/[^\d]/g, ''));
  function personalize() {
    const to = Math.max(num('#mSave'), num('#saveNum')); if (!to) return;
    hd.classList.add('is-personal');
    const from = shown, t0 = performance.now(), dur = reduce ? 0 : 1100;
    const tick = now => { const p = dur ? Math.min(1, (now - t0) / dur) : 1; shown = from + (to - from) * (1 - Math.pow(1 - p, 3)); $('#hdSave').textContent = fmt(shown); if (p < 1) requestAnimationFrame(tick); };
    if (dur) requestAnimationFrame(tick); else tick(t0);
    $('.hd__cta').setAttribute('aria-label', `₪${fmt(to)} יכולים להישאר אצלכם — לשיחת היכרות`);
  }
  // מופעל רק מפעולה של הגולש: הזזת סליידר או לחיצה על המתג
  ['#iAmt', '#iYrs', '#iRate'].forEach(s => $(s) && $(s).addEventListener('change', () => setTimeout(personalize, 50)));
  $('.magic__switch') && $('.magic__switch').addEventListener('click', () => setTimeout(personalize, 1500));

  // הירו: פרלקסה עדינה בגלילה
  const heroImg = $('.hero__img');
  if (!reduce && heroImg) addEventListener('scroll', () => {
    const y = scrollY; if (y > innerHeight * 1.2) return;
    heroImg.style.transform = `translateY(${y * .25}px) scale(${1 + y / innerHeight * .08})`;
  }, { passive: true });

  // שלבי הדרך נכנסים כשהם נראים
  const stepIO = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) e.target.classList.add('seen'); }), { threshold: .35 });
  $$('.step').forEach(s => stepIO.observe(s));

  spy();
})();
