// משחק: 3 מפתחות → דו״ח חיסכון אישי (תגמול ישיר)
(() => {
  const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fmt = n => Math.round(n).toLocaleString('en-US');
  const hd = $('#hd'), panel = $('#questPanel'), qBtn = $('.hd__quest'), toast = $('#toast'), report = $('#report');
  const NAMES = { m1: 'גיליתם כמה הבנק מרוויח', m2: 'ראיתם את הקסם', m3: 'סיפרתם מי אתם' };
  const SIT = { first: 'דירה ראשונה', upgrade: 'משפרי דיור', refi: 'מחזור משכנתא' };
  const STEP1 = {
    first: 'חצי שעה. כמה יש לכם להון עצמי, מה אתם מסוגלים להחזיר בחודש, ומה הכי מפחיד אתכם בבנק. בלי התחייבות.',
    upgrade: 'חצי שעה. איך מוכרים וקונים באותו זמן בלי להיתקע עם שתי משכנתאות, ומה עושים עם הישנה. בלי התחייבות.',
    refi: 'חצי שעה. שולחים לי את דוח היתרות, ואני אומר לכם אם מחזור שווה את זה, ובכמה. בלי התחייבות.',
  };
  let state = { m1: false, m2: false, m3: false, sit: null };
  try { Object.assign(state, JSON.parse(localStorage.getItem('itzikQuest') || '{}')); } catch (e) {}
  const save = () => { try { localStorage.setItem('itzikQuest', JSON.stringify(state)); } catch (e) {} };
  const count = () => ['m1', 'm2', 'm3'].filter(k => state[k]).length;

  function paint(newKey) {
    const n = count();
    $$('.hd__keys .k').forEach((k, i) => k.classList.toggle('on', i < n));
    $('#qCount').textContent = n;
    qBtn.setAttribute('aria-label', `המשימות שלכם: ${n} מתוך 3`);
    $$('.qpanel__list li').forEach(li => li.classList.toggle('done', !!state[li.dataset.q]));
    hd.classList.toggle('is-done', n === 3);
    if (state.sit) { $$('.quiz button').forEach(b => b.setAttribute('aria-pressed', b.dataset.sit === state.sit)); }
  }
  let tTimer;
  function say(html) {
    toast.innerHTML = html; toast.classList.add('show');
    clearTimeout(tTimer); tTimer = setTimeout(() => toast.classList.remove('show'), 3200);
  }
  function complete(key) {
    if (state[key]) return;
    state[key] = true; save(); paint(key);
    const n = count();
    if (n < 3) say(`🔑 <b>מפתח ${n} מתוך 3</b> · ${NAMES[key]}`);
    else { say('🔑🔑🔑 <b>פתחתם את הדו״ח האישי שלכם!</b>'); setTimeout(openReport, reduce ? 300 : 1300); }
  }

  // משימה 1: הזזת סליידר בפרק הבנק
  ['#iAmt', '#iYrs', '#iRate'].forEach(s => $(s) && $(s).addEventListener('change', () => complete('m1')));
  // משימה 2: הקסם
  $('.magic__switch') && $('.magic__switch').addEventListener('click', e => { if (e.target.closest('[data-mix="itzik"]')) setTimeout(() => complete('m2'), 1400); });
  // משימה 3: השאלון — וגם משנה את שלב 01 לפי המצב
  function applySit() {
    if (!state.sit) return;
    const p = $('.step p'); if (!p) return;
    p.classList.add('swap'); setTimeout(() => { p.textContent = STEP1[state.sit]; p.classList.remove('swap'); }, reduce ? 0 : 300);
  }
  $$('.quiz button').forEach(b => b.addEventListener('click', () => { state.sit = b.dataset.sit; save(); paint(); applySit(); complete('m3'); }));

  // פאנל המשימות
  const setPanel = open => { panel.hidden = !open; qBtn.setAttribute('aria-expanded', open); };
  qBtn.addEventListener('click', e => { e.stopPropagation(); if (count() === 3) openReport(); else setPanel(panel.hidden); });
  panel.addEventListener('click', e => { if (e.target.closest('a')) setPanel(false); });
  document.addEventListener('click', e => { if (!panel.hidden && !e.target.closest('#questPanel')) setPanel(false); });
  addEventListener('keydown', e => { if (e.key === 'Escape') setPanel(false); });

  // הפרס: דו״ח אישי עם המספרים של הגולש
  const spitzer = (P, r, n) => { const i = r / 1200, pay = P * i / (1 - Math.pow(1 + i, -n)); return { pay, int: pay * n - P }; };
  function numbers() {
    const P = +$('#iAmt').value, yrs = +$('#iYrs').value, n = yrs * 12, r = +$('#iRate').value;
    const bank = spitzer(P, r, n);
    const share = [.24, .46, .30], d = [-.30, -.25, -.75];
    let pay = 0, int = 0; share.forEach((s, k) => { const t = spitzer(P * s, Math.max(r + d[k], .5), n); pay += t.pay; int += t.int; });
    return { P, yrs, r, bank, mix: { pay, int } };
  }
  function openReport() {
    const x = numbers(), saveAmt = x.bank.int - x.mix.int, month = x.bank.pay - x.mix.pay;
    $('#rSit').textContent = SIT[state.sit] || '—';
    $('#rLoan').textContent = `₪${fmt(x.P)} · ${x.yrs} שנה · ${x.r.toFixed(1)}%`;
    $('#rBank').textContent = `₪${fmt(x.bank.int)}`;
    $('#rMix').textContent = `₪${fmt(x.mix.int)}`;
    $('#rSave').textContent = `₪${fmt(saveAmt)}`;
    $('#rMonth').textContent = `₪${fmt(month)}`;
    const msg = `היי איציק, פתחתי את הדו״ח באתר 🔑\nמצב: ${SIT[state.sit] || '-'}\nמשכנתא: ₪${fmt(x.P)} ל-${x.yrs} שנה, ריבית ${x.r.toFixed(1)}%\nלפי הדו״ח יכול להישאר אצלנו כ-₪${fmt(saveAmt)}. אשמח לשיחת היכרות.`;
    $('#rWa').href = 'https://wa.me/972500000000?text=' + encodeURIComponent(msg);
    if (typeof report.showModal === 'function') report.showModal(); else report.setAttribute('open', '');
    burst();
  }
  $('#rPrint').addEventListener('click', () => print());

  // חגיגה קטנה: חלקיקים בצבעי המותג (לא בהפחתת תנועה)
  function burst() {
    if (reduce) return;
    const cols = ['#B8232A', '#E0434A', '#181842', '#E8E9F7'];
    for (let i = 0; i < 36; i++) {
      const el = document.createElement('i'); el.className = 'burst';
      el.style.background = cols[i % cols.length]; el.style.left = innerWidth / 2 + 'px'; el.style.top = innerHeight / 2 + 'px';
      document.body.appendChild(el);
      const a = Math.random() * Math.PI * 2, d = 140 + Math.random() * 260;
      el.animate([{ transform: 'translate(-50%,-50%) rotate(0)', opacity: 1 }, { transform: `translate(${Math.cos(a) * d}px, ${Math.sin(a) * d + 120}px) rotate(${Math.random() * 540}deg)`, opacity: 0 }], { duration: 1200 + Math.random() * 600, easing: 'cubic-bezier(.2,.8,.3,1)' }).onfinish = () => el.remove();
    }
  }

  paint(); applySit();
})();
