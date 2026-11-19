(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = matchMedia('(pointer: fine)').matches;

  /* header: hides on scroll down, returns on scroll up */
  const hd = document.querySelector('.hd');
  let lastY = scrollY;
  addEventListener('scroll', () => {
    const y = scrollY;
    hd.classList.toggle('is-hidden', y > 300 && y > lastY + 2);
    if (y < lastY - 2 || y < 300) hd.classList.remove('is-hidden');
    lastY = y;
  }, { passive: true });

  /* hero enters */
  const hero = document.querySelector('.hero');
  requestAnimationFrame(() => requestAnimationFrame(() => hero && hero.classList.add('in')));

  /* mouse parallax in the hero world (bg + floating glass tiles) */
  if (hero && fine && !reduce) {
    hero.addEventListener('pointermove', e => {
      const r = hero.getBoundingClientRect();
      hero.style.setProperty('--mx', ((e.clientX - r.left) / r.width - .5).toFixed(3));
      hero.style.setProperty('--my', ((e.clientY - r.top) / r.height - .5).toFixed(3));
    });
    hero.addEventListener('pointerleave', () => { hero.style.setProperty('--mx', 0); hero.style.setProperty('--my', 0); });
  }

  /* reveals */
  document.querySelectorAll('.sec .h1, .pull').forEach(h => h.querySelectorAll('.ln').forEach(l => l.classList.add('rv-ln')));
  document.querySelectorAll('.problem__copy, .guide__copy > p, .cases, .trust__copy > p, .facts, .calc__card, .calc__out, .calc__cta, .late__grid > p, .final__copy > p, .final .card, .final__key, .ledger').forEach(e => e.classList.add('up'));
  const targets = document.querySelectorAll('.rv-ln, .up, .neon--v, .big-dia, .guide__photo, .road, .order, .ledger');
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }), { threshold: .2, rootMargin: '0px 0px -6% 0px' });
  targets.forEach(t => io.observe(t));

  /* calculator (Spitzer) */
  const $ = id => document.getElementById(id);
  const amount = $('c-amount'), years = $('c-years'), rate = $('c-rate');
  if (amount) {
    const nf = new Intl.NumberFormat('he-IL');
    const out = $('o-pay');
    let shown = 0, raf;
    const pct = r => (r.value - r.min) / (r.max - r.min) * 100;
    const fill = r => {
      const p = pct(r);
      r.style.setProperty('--p', p + '%');
      r.parentElement.style.setProperty('--p', `calc(${p}% + ${(.5 - p / 100) * 24}px)`);
    };
    const show = to => {
      cancelAnimationFrame(raf);
      if (reduce) { shown = to; out.textContent = nf.format(to); return; }
      const from = shown, t0 = performance.now();
      const tick = t => {
        const k = Math.min(1, (t - t0) / 700), e = 1 - Math.pow(1 - k, 3);
        shown = Math.round(from + (to - from) * e);
        out.textContent = nf.format(shown);
        if (k < 1) raf = requestAnimationFrame(tick);
      };
      raf = requestAnimationFrame(tick);
    };
    const labels = () => {
      $('o-amount').textContent = '₪' + nf.format(+amount.value);
      $('o-years').textContent = years.value + ' שנים';
      $('o-rate').textContent = (+rate.value).toFixed(1) + '%';
      [amount, years, rate].forEach(fill);
    };
    const calc = () => {
      const P = +amount.value, n = +years.value * 12, r = +rate.value / 100 / 12;
      const pay = r ? P * r / (1 - Math.pow(1 + r, -n)) : P / n;
      labels();
      show(Math.round(pay));
    };
    [amount, years, rate].forEach(r => r.addEventListener('input', calc));
    document.querySelectorAll('.pm').forEach(b => b.addEventListener('click', () => {
      const r = $(b.dataset.for), step = +b.dataset.step;
      const v = Math.min(+r.max, Math.max(+r.min, +r.value + step));
      r.value = Math.abs(step) < 1 ? v.toFixed(1) : v;
      calc();
    }));
    /* count up the first time the calculator is seen */
    const calcIo = new IntersectionObserver(es => { if (es[0].isIntersecting) { calc(); calcIo.disconnect(); } }, { threshold: .3 });
    labels();
    calcIo.observe(out);
  }

  /* lead forms */
  document.querySelectorAll('form.lead').forEach(f => {
    const err = f.querySelector('.lead__err');
    f.addEventListener('submit', ev => {
      ev.preventDefault();
      const name = f.elements.name.value.trim();
      const phone = f.elements.phone.value.replace(/[^\d+]/g, '');
      const income = (f.querySelector('input[name=income]:checked') || {}).value;
      f.querySelectorAll('.field').forEach(x => x.classList.remove('is-bad'));
      const bad = [];
      if (!income) bad.push('האם יש הכנסה קבועה');
      if (name.length < 2) { bad.push('שם'); f.elements.name.closest('.field').classList.add('is-bad'); }
      if (!/^(\+?972|0)5\d{8}$/.test(phone) && !/^0\d{8,9}$/.test(phone)) { bad.push('טלפון תקין'); f.elements.phone.closest('.field').classList.add('is-bad'); }
      if (bad.length) { err.textContent = 'חסר: ' + bad.join(', '); err.hidden = false; return; }
      err.hidden = true;
      const lead = { variant: f.dataset.variant, form: f.id, name, phone, income };
      (window.dataLayer = window.dataLayer || []).push({ event: 'lead', ...lead });
      /* TODO: send `lead` to the CRM / Make / Sheets webhook here before redirecting */
      location.href = 'thanks.html?v=' + lead.variant + '&income=' + income;
    });
  });
})();
