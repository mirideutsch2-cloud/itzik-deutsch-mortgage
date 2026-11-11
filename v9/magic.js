// הקסם: לפני/אחרי על הסכום והתקופה שהגולש בחר בפרק 02
(() => {
  const root = document.querySelector('.magic'); if (!root) return;
  const $ = s => document.querySelector(s);
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fmt = n => Math.round(n).toLocaleString('en-US');
  const MIX = { // נתחי ההלוואה והפרש הריבית מהממוצע שבחרו (להמחשה)
    bank:  { share: [.34, .33, .33], d: [ .35,  .15, -.50] },
    itzik: { share: [.24, .46, .30], d: [-.30, -.25, -.75] },
  };
  let mode = 'bank', shown = { pay: 0, int: 0, save: 0 }, anim;
  const spitzer = (P, ratePct, n) => { const i = ratePct / 1200; const pay = P * i / (1 - Math.pow(1 + i, -n)); return { pay, int: pay * n - P }; };
  function compute(m) {
    const P = +$('#iAmt').value, n = +$('#iYrs').value * 12, r = +$('#iRate').value;
    if (m === 'bank') return spitzer(P, r, n); // ההצעה של הבנק = אותו מספר בדיוק כמו בפרק 02
    let pay = 0, int = 0;
    MIX[m].share.forEach((sh, k) => { const t = spitzer(P * sh, Math.max(r + MIX[m].d[k], .5), n); pay += t.pay; int += t.int; });
    return { pay, int };
  }
  function render(animate) {
    const b = compute('bank'), cur = compute(mode);
    const it = compute('itzik'), n = +$('#iYrs').value * 12;
    // אותו מודל משמש גם את פרק 02 (עלות ההמתנה) ואת פרק 05 (כמה נשאר אצלכם) — מספר אחד בכל האתר
    $('#saveNum').textContent = fmt(Math.round((b.int - it.int) / 1000) * 1000);
    $('#waitNum').textContent = fmt(b.pay - it.pay);
    const target = { pay: cur.pay, int: cur.int, save: mode === 'itzik' ? b.int - cur.int : 0 };
    const segs = root.querySelectorAll('.seg'), r = +$('#iRate').value;
    MIX[mode].share.forEach((sh, k) => { segs[k].style.flexGrow = sh * 100; segs[k].querySelector('.seg__r').textContent = Math.max(r + MIX[mode].d[k], .5).toFixed(2) + '%'; });
    cancelAnimationFrame(anim);
    const from = { ...shown }, t0 = performance.now(), dur = animate && !reduce ? 1400 : 0;
    const step = now => {
      const p = dur ? Math.min(1, (now - t0) / dur) : 1, e = 1 - Math.pow(1 - p, 4);
      for (const k in target) shown[k] = from[k] + (target[k] - from[k]) * e;
      $('#mPay').textContent = fmt(shown.pay); $('#mInt').textContent = fmt(shown.int); $('#mSave').textContent = fmt(shown.save);
      if (p < 1) anim = requestAnimationFrame(step);
    };
    if (dur) anim = requestAnimationFrame(step); else step(t0);
  }
  root.querySelector('.magic__switch').addEventListener('click', e => {
    const btn = e.target.closest('button'); if (!btn || btn.dataset.mix === mode) return;
    mode = btn.dataset.mix; root.classList.add('touched');
    root.classList.toggle('is-itzik', mode === 'itzik');
    root.querySelectorAll('.magic__switch button').forEach(x => x.setAttribute('aria-pressed', x === btn));
    render(true);
  });
  ['#iAmt', '#iYrs', '#iRate'].forEach(s => $(s).addEventListener('input', () => render(false)));
  render(false);
})();
