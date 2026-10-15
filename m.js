/* איציק דייטש — ניווט מתחלף, משפט שנדלק, בית שנבנה בגלילה, מחשבון, מונים. בלי תלויות. */
(() => {
  const $ = (s, c = document) => c.querySelector(s), $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const root = document.documentElement, clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  root.classList.add("js");
  const nf = new Intl.NumberFormat("he-IL");

  /* ניווט: כהה/בהיר לפי הסקשן שמתחתיו */
  const nav = $("#nav"), darks = $$("[data-theme=dark]");
  function navTheme() {
    const y = nav.getBoundingClientRect().bottom - 10;
    const onDark = darks.some(d => { const r = d.getBoundingClientRect(); return r.top <= y && r.bottom >= y; });
    nav.dataset.t = onDark ? "dark" : "light";
  }

  /* משפט שנדלק מילה-מילה */
  const st = $("#statement");
  (function wrap(n) { [...n.childNodes].forEach(c => { if (c.nodeType === 3) { const f = document.createDocumentFragment(); c.textContent.split(/(\s+)/).forEach(t => { if (!t) return; if (/^\s+$/.test(t)) f.append(t); else { const s = document.createElement("span"); s.className = "w"; s.textContent = t; f.append(s); } }); c.replaceWith(f); } else if (c.nodeType === 1) wrap(c); }); })(st);
  const words = $$(".w", st);

  /* בית שנבנה */
  const build = $("#how"), house = $("#buildHouse"), steps = $$("#steps li"), bar = $("#meterBar"), mt = $("#meterTxt");
  const mobile = matchMedia("(max-width:860px)");
  function buildFrame() {
    if (mobile.matches) return;
    const r = build.getBoundingClientRect(), total = build.offsetHeight - innerHeight;
    const p = clamp(-r.top / Math.max(1, total));
    [0, 1, 2, 3].forEach(i => house.style.setProperty("--p" + (i + 1), clamp(p * 4 - i).toFixed(3)));
    const idx = Math.min(3, Math.floor(p * 4 * 0.999));
    steps.forEach((s, i) => s.classList.toggle("on", i === idx));
    bar.parentNode.style.setProperty("--p", (p * 100).toFixed(1) + "%");
    bar.style.setProperty("--p", (p * 100).toFixed(1) + "%");
    mt.textContent = Math.round(p * 100) + "%";
  }

  function frame() {
    navTheme();
    const vh = innerHeight, sr = st.getBoundingClientRect();
    const sp = clamp((vh * 0.85 - sr.top) / (vh * 0.6 + sr.height * 0.4));
    words.forEach((w, i) => w.style.opacity = reduce ? 1 : (i / words.length < sp * 1.05 ? 1 : 0.15));
    buildFrame();
  }
  let raf = 0; addEventListener("scroll", () => { if (!raf) raf = requestAnimationFrame(() => { raf = 0; frame(); }); }, { passive: true });
  addEventListener("resize", frame); frame();
  if (reduce) $$("#steps li").forEach(s => s.classList.add("on"));

  /* מחשבון (לוח שפיצר) */
  const amt = $("#amt"), yrs = $("#yrs"), rate = $("#rate"), pay = $("#pay");
  let shown = 0, anim = 0;
  function tween(to) {
    cancelAnimationFrame(anim); const from = shown, t0 = performance.now();
    if (reduce) { shown = to; pay.textContent = nf.format(Math.round(to)); return; }
    (function tk(t) { const k = Math.min(1, (t - t0) / 500), e = 1 - Math.pow(1 - k, 3); shown = from + (to - from) * e; pay.textContent = nf.format(Math.round(shown)); if (k < 1) anim = requestAnimationFrame(tk); })(t0);
  }
  function fillTrack(el) { el.style.setProperty("--f", ((el.value - el.min) / (el.max - el.min) * 100).toFixed(1) + "%"); }
  function calc() {
    const P = +amt.value, n = +yrs.value * 12, r = +rate.value / 100 / 12;
    const M = r ? P * r / (1 - Math.pow(1 + r, -n)) : P / n, I = M * n - P;
    $("#oAmt").textContent = "₪" + nf.format(P); $("#oYrs").textContent = yrs.value + " שנים"; $("#oRate").textContent = (+rate.value).toFixed(2) + "%";
    $("#sumP").textContent = "₪" + nf.format(Math.round(P)); $("#sumI").textContent = "₪" + nf.format(Math.round(I));
    $("#save").textContent = "₪" + nf.format(Math.round(I * 0.12 / 1000) * 1000);
    $("#barP").style.width = (P / (P + I) * 100).toFixed(1) + "%"; $("#barI").style.width = (I / (P + I) * 100).toFixed(1) + "%";
    [amt, yrs, rate].forEach(fillTrack); tween(M);
  }
  [amt, yrs, rate].forEach(i => i.addEventListener("input", calc)); calc();

  /* מונים + חשיפות */
  const cio = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return; cio.unobserve(e.target); if (reduce) return;
    const el = e.target, n = +el.dataset.count, dec = +(el.dataset.dec || 0), t0 = performance.now();
    (function tk(t) { const k = Math.min(1, (t - t0) / 1400), v = n * (1 - Math.pow(1 - k, 3)); el.textContent = dec ? v.toFixed(dec) : nf.format(Math.round(v)); if (k < 1) requestAnimationFrame(tk); })(t0);
  }), { threshold: .6 });
  $$("[data-count]").forEach(b => cio.observe(b));
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }), { threshold: .12 });
  $$(".calc__head,.calc__box,.about__txt,.portrait,.svc li,.q,.faq details,.foot__in,.quotes__head").forEach(el => { el.classList.add("rv"); io.observe(el); });
})();
