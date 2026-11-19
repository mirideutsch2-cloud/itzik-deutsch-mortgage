(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* header turns solid after the hero */
  const hd = document.querySelector('.hd');
  const onScroll = () => hd.classList.toggle('is-solid', scrollY > 40);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* reveal: headings rise line by line, hairlines draw, copy rises ≤20px */
  document.querySelectorAll('.sec .h1').forEach(h => h.classList.add('rv'));
  document.querySelectorAll('.sec .wrap > p, .problem__copy, .guide__copy > p, .cases, .calc__inputs, .calc__out, .calc__cta, .late__grid > p, .trust__copy > p, .facts, .final__copy > p, .final .lead').forEach(e => e.classList.add('up'));
  const targets = document.querySelectorAll('.fx, .rv, .ch, .up, .ledger, .road, .order, .guide__photo');
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }), { threshold: .2, rootMargin: '0px 0px -8% 0px' });
  targets.forEach(t => io.observe(t));

  /* gentle parallax on the glass house */
  const house = document.querySelector('.hero__house img');
  if (house && !reduce) {
    addEventListener('scroll', () => {
      const y = Math.min(scrollY, innerHeight);
      house.style.transform = `translateY(${y * 0.12}px)`;
    }, { passive: true });
  }

  /* calculator (Spitzer) — the visitor's own number, giant */
  const $ = id => document.getElementById(id);
  const amount = $('c-amount'), years = $('c-years'), rate = $('c-rate');
  if (amount) {
    const nf = new Intl.NumberFormat('he-IL');
    const out = $('o-pay');
    let shown = 0, raf;
    const fill = r => r.style.setProperty('--p', ((r.value - r.min) / (r.max - r.min) * 100) + '%');
    const show = to => {
      cancelAnimationFrame(raf);
      if (reduce) { shown = to; out.textContent = nf.format(to); return; }
      const from = shown, t0 = performance.now();
      const tick = t => {
        const k = Math.min(1, (t - t0) / 600), e = 1 - Math.pow(1 - k, 3);
        shown = Math.round(from + (to - from) * e);
        out.textContent = nf.format(shown);
        if (k < 1) raf = requestAnimationFrame(tick);
      };
      raf = requestAnimationFrame(tick);
    };
    const calc = () => {
      const P = +amount.value, n = +years.value * 12, r = +rate.value / 100 / 12;
      const pay = r ? P * r / (1 - Math.pow(1 + r, -n)) : P / n;
      $('o-amount').textContent = '₪' + nf.format(P);
      $('o-years').textContent = years.value + ' שנים';
      $('o-rate').textContent = (+rate.value).toFixed(1) + '%';
      [amount, years, rate].forEach(fill);
      show(Math.round(pay));
    };
    [amount, years, rate].forEach(r => r.addEventListener('input', calc));
    calc();
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
      if (name.length < 2) { bad.push('שם'); f.elements.name.closest('.field').classList.add('is-bad'); }
      if (!/^(\+?972|0)5\d{8}$/.test(phone) && !/^0\d{8,9}$/.test(phone)) { bad.push('טלפון תקין'); f.elements.phone.closest('.field').classList.add('is-bad'); }
      if (!income) bad.push('האם יש הכנסה קבועה');
      if (bad.length) { err.textContent = 'חסר: ' + bad.join(', '); err.hidden = false; return; }
      err.hidden = true;
      const lead = { variant: f.dataset.variant, form: f.id, name, phone, income };
      /* measurement: A/B variant + steady-income flag */
      (window.dataLayer = window.dataLayer || []).push({ event: 'lead', ...lead });
      /* TODO: send `lead` to the CRM / Make / Sheets webhook here before redirecting */
      location.href = 'thanks.html?v=' + lead.variant + '&income=' + income;
    });
  });
})();
