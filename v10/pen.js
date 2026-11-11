// "העט האדום": איציק מסמן על ההצעה בזמן הגלילה. הקווים מצוירים ביד (רעד קטן), לא צורות מושלמות.
(() => {
  const doc = document.getElementById('doc'), ink = document.getElementById('ink'), sec = document.getElementById('pen');
  const notes = [...document.querySelectorAll('.note')];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const NS = 'http://www.w3.org/2000/svg';

  // רנדום יציב, כדי שהקווים ייראו אותו דבר בכל טעינה
  let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const j = a => (rnd() - .5) * 2 * a;

  // מיקום יחסי לדף (בלי השפעת הסיבוב)
  function box(el) {
    let x = 0, y = 0, e = el;
    while (e && e !== doc) { x += e.offsetLeft; y += e.offsetTop; e = e.offsetParent; }
    return { x, y, w: el.offsetWidth, h: el.offsetHeight };
  }
  const smooth = pts => pts.reduce((d, p, i, a) => {
    if (!i) return `M${p[0].toFixed(1)} ${p[1].toFixed(1)}`;
    const q = a[i - 1], mx = (q[0] + p[0]) / 2, my = (q[1] + p[1]) / 2;
    return d + ` Q${q[0].toFixed(1)} ${q[1].toFixed(1)} ${mx.toFixed(1)} ${my.toFixed(1)}`;
  }, '');

  // עיגול של עט: קצת יותר מסיבוב מלא, לא סגור בדיוק
  function circle(b, pad = 10) {
    const cx = b.x + b.w / 2, cy = b.y + b.h / 2, rx = b.w / 2 + pad, ry = b.h / 2 + pad * .7, pts = [];
    const start = -2.2 + j(.3), turns = 1.12;
    for (let i = 0; i <= 44; i++) { const t = start - (i / 44) * Math.PI * 2 * turns; const k = 1 + j(.035) + i / 44 * .06; pts.push([cx + Math.cos(t) * rx * k, cy + Math.sin(t) * ry * k]); }
    return [smooth(pts)];
  }
  // קו מחיקה: שתי משיכות, קצת עקומות
  function strike(b) {
    const y = b.y + b.h * .55, a = [], c = [];
    for (let i = 0; i <= 10; i++) { a.push([b.x + b.w + 6 - (b.w + 12) * i / 10, y + j(1.4) - i * .3]); c.push([b.x + b.w + 4 - (b.w + 8) * i / 10, y + 3 + j(1.4) + i * .25]); }
    return [smooth(a), smooth(c)];
  }
  // סוגר בצד הטבלה + חץ להערה
  function bracket(b) {
    const x = b.x - 14, pts = [];
    for (let i = 0; i <= 14; i++) { const t = i / 14; pts.push([x - Math.sin(t * Math.PI) * 10 + j(1), b.y + 8 + t * (b.h - 16)]); }
    const mid = b.y + b.h / 2, arrow = [[x - 10, mid], [x - 46, mid - 6 + j(2)]];
    return [smooth(pts), smooth(arrow), `M${x - 46} ${mid - 6} l9 -7 M${x - 46} ${mid - 6} l10 5`];
  }
  // קו תחתון כפול
  function under(b) {
    const out = [];
    [0, 6].forEach(o => { const p = []; for (let i = 0; i <= 12; i++) p.push([b.x + b.w + 4 - (b.w + 8) * i / 12, b.y + b.h + 3 + o + j(1.2) + Math.sin(i) * .8]); out.push(smooth(p)); });
    return out;
  }

  const MARKS = [
    { el: 'tPrime', fn: b => circle(b, 9) },
    { el: 'tFeeNum', fn: b => strike(b) },
    { el: 'tTracks', fn: b => bracket(b) },
    { el: 'tTotalNum', fn: b => under(b).concat(circle(b, 12)) },
  ];
  let paths = [];
  function build() {
    ink.innerHTML = ''; seed = 7;
    ink.setAttribute('viewBox', `0 0 ${doc.offsetWidth} ${doc.offsetHeight}`);
    paths = MARKS.map(m => m.fn(box(document.getElementById(m.el))).map(d => {
      const p = document.createElementNS(NS, 'path'); p.setAttribute('d', d); p.setAttribute('pathLength', '1');
      p.style.strokeDasharray = '1'; p.style.strokeDashoffset = reduce ? '0' : '1'; ink.appendChild(p); return p;
    }));
    fit(); placeNotes(); update();
  }

  // הערות בשוליים מול הסימון (מחשב); בטלפון — אחת בכל פעם מתחת להצעה
  const wide = () => innerWidth > 900;
  let scale = 1;
  function placeNotes() {
    if (!wide()) { notes.forEach(n => { n.style.top = ''; n.style.position = ''; n.style.insetInline = ''; }); return; }
    let last = -999;
    notes.forEach(n => {
      n.style.position = 'absolute'; n.style.insetInline = '0';
      const t = box(document.getElementById(n.dataset.for)).y * scale - 6;
      const top = Math.max(t, last + 12); n.style.top = top + 'px'; last = top + n.offsetHeight;
    });
  }
  // ההצעה נכנסת לגובה המסך
  function fit() {
    const wrap = doc.parentElement, avail = wrap.clientHeight - (wide() ? 0 : document.getElementById('notes').offsetHeight + 12);
    const s = Math.min(1, avail / doc.offsetHeight); scale = s;
    doc.style.transform = `rotate(-.6deg) scale(${s})`;
  }

  function update() {
    const r = sec.getBoundingClientRect(), span = sec.offsetHeight - innerHeight;
    const p = reduce ? 1 : Math.min(1, Math.max(0, -r.top / span));
    const n = MARKS.length;
    paths.forEach((group, i) => {
      const a = (i / n) * .9 + .04, local = Math.min(1, Math.max(0, (p - a) / (.9 / n * .72)));
      group.forEach((path, k) => { const s = Math.min(1, Math.max(0, local * group.length - k)); path.style.strokeDashoffset = 1 - s; });
      group.on = local > .55;
    });
    const last = paths.reduce((m, g, i) => g.on ? i : m, -1);
    notes.forEach((nt, i) => nt.classList.toggle('on', wide() ? paths[i].on : i === last));
  }

  let tick = false;
  addEventListener('scroll', () => { if (!tick) { tick = true; requestAnimationFrame(() => { tick = false; update(); }); } }, { passive: true });
  addEventListener('resize', build);
  (document.fonts ? document.fonts.ready : Promise.resolve()).then(build);
})();
