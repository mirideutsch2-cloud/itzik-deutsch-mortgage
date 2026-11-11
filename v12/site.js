(() => {
  const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // העט מצייר כשהאזור נכנס
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('go'); io.unobserve(e.target); } }), { threshold: .3 });
  $$('.sec').forEach(s => io.observe(s));

  // חשיפה עדינה
  $$('.c__copy, .steps li, .me__copy, .send__copy, .form').forEach((el, i) => el.classList.add('rv'));
  const rio = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); rio.unobserve(e.target); } }), { threshold: .2 });
  $$('.rv').forEach(el => rio.observe(el));
  $$('.steps li').forEach((li, i) => li.style.transitionDelay = (i * .12) + 's');

  // הדר: שקוף על הכחול, לבן על השאר
  const hd = $('#hd'), dark = $$('.a, .c, .send');
  function tone() {
    const y = 40; const onDark = dark.some(el => { const r = el.getBoundingClientRect(); return r.top <= y && r.bottom > y; });
    hd.classList.toggle('is-solid', !onDark);
  }
  addEventListener('scroll', () => requestAnimationFrame(tone), { passive: true }); tone();

  // תפריט מובייל
  const mb = $('.hd__menu'), mn = $('#mnav');
  const setMenu = open => { mb.setAttribute('aria-expanded', open); mn.hidden = !open; document.body.style.overflow = open ? 'hidden' : ''; };
  mb.addEventListener('click', () => setMenu(mn.hidden));
  mn.addEventListener('click', e => { if (e.target.closest('a')) setMenu(false); });
  addEventListener('keydown', e => { if (e.key === 'Escape' && !mn.hidden) { setMenu(false); mb.focus(); } });

  if (reduce) return;
  // ההצעה מסתובבת אחרי העכבר
  const c = $('#pen'), sheet = $('#sheet');
  c.addEventListener('pointermove', e => {
    const r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
    sheet.style.transform = `rotateX(${6 - y * 12}deg) rotateY(${-8 + x * 18}deg) rotateZ(-2deg)`;
  });
  c.addEventListener('pointerleave', () => sheet.style.transform = '');
  // התמונה בפתיחה זזה קלות
  const a = $('.a'), ph = $('.a__photo');
  a.addEventListener('pointermove', e => { const r = a.getBoundingClientRect(); const x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5; ph.style.transform = `rotate(2deg) translate(${x * -18}px, ${y * -14}px)`; });
})();
