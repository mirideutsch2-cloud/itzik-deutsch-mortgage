(() => {
  document.documentElement.classList.add('js');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* header: hide on scroll down, show on scroll up */
  const hd = document.querySelector('.hd');
  let lastY = scrollY;
  addEventListener('scroll', () => {
    const y = scrollY;
    hd.classList.toggle('is-hidden', y > 200 && y > lastY);
    lastY = y;
  }, { passive: true });

  /* reveal on enter */
  const els = document.querySelectorAll('.sec__head, .problem__grid, .quote, .guide > *, .trust > *, .step, .calc > *, .tcard, .late__grid > *, .final > *');
  els.forEach(el => el.classList.add('rv'));
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }), { threshold: .15 });
  els.forEach(el => io.observe(el));

  /* calculator (Spitzer) */
  const $ = id => document.getElementById(id);
  const amount = $('c-amount'), years = $('c-years'), rate = $('c-rate');
  if (amount) {
    const nf = new Intl.NumberFormat('he-IL');
    const out = $('o-pay');
    let shown = 0, raf;
    const fill = r => r.style.setProperty('--p', ((r.value - r.min) / (r.max - r.min) * 100) + '%');
    const animate = to => {
      cancelAnimationFrame(raf);
      if (reduce) { shown = to; out.textContent = nf.format(to); return; }
      const from = shown, t0 = performance.now();
      const tick = t => {
        const k = Math.min(1, (t - t0) / 500), e = 1 - Math.pow(1 - k, 3);
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
      animate(Math.round(pay));
    };
    [amount, years, rate].forEach(r => r.addEventListener('input', calc));
    document.querySelectorAll('.pm').forEach(b => b.addEventListener('click', () => {
      const r = b.parentElement.querySelector('input');
      const step = +b.dataset.step;
      const v = Math.min(+r.max, Math.max(+r.min, +r.value + step));
      r.value = step % 1 ? v.toFixed(1) : v;
      calc();
    }));
    calc();
  }

  /* lead forms */
  document.querySelectorAll('form.lead').forEach(f => {
    const err = f.querySelector('.lead__err');
    f.addEventListener('submit', ev => {
      ev.preventDefault();
      const name = f.name.value.trim();
      const phone = f.phone.value.replace(/[^\d+]/g, '');
      const income = (f.querySelector('input[name=income]:checked') || {}).value;
      f.querySelectorAll('.field').forEach(x => x.classList.remove('is-bad'));
      const bad = [];
      if (name.length < 2) { bad.push('שם'); f.name.closest('.field').classList.add('is-bad'); }
      if (!/^(\+?972|0)5\d{8}$/.test(phone) && !/^0\d{8,9}$/.test(phone)) { bad.push('טלפון תקין'); f.phone.closest('.field').classList.add('is-bad'); }
      if (!income) bad.push('האם יש הכנסה קבועה');
      if (bad.length) { err.textContent = 'חסר: ' + bad.join(', '); err.hidden = false; return; }
      err.hidden = true;
      const lead = { variant: f.dataset.variant, form: f.id, name, phone, income };
      /* measurement: A/B variant + steady income flag */
      (window.dataLayer = window.dataLayer || []).push({ event: 'lead', ...lead });
      /* TODO: send `lead` to the CRM / Make / Sheets webhook here before redirecting */
      location.href = 'thanks.html?v=' + lead.variant + '&income=' + income;
    });
  });
})();
