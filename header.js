/* הדר: מצב גלילה, פס התקדמות, תפריט מלא, ומתג 4 גרסאות לדף הדוגמה */
(() => {
  const root = document.documentElement, hd = document.getElementById("nav"), btn = hd.querySelector(".hd__menu"), menu = document.getElementById("menu");
  function onScroll() {
    hd.classList.toggle("scrolled", scrollY > 40);
    const max = document.documentElement.scrollHeight - innerHeight;
    hd.style.setProperty("--sp", max > 0 ? (scrollY / max).toFixed(4) : 0);
  }
  addEventListener("scroll", onScroll, { passive: true }); onScroll();

  /* מודרני: הסתרה בגלילה למטה, חזרה בגלילה למעלה + סמן שזז בין הקישורים לפי הסקשן */
  let lastY = scrollY;
  addEventListener("scroll", () => {
    const y = scrollY;
    if (root.dataset.header === "modern" && menu.hidden) { if (y > lastY + 6 && y > 240) hd.classList.add("hide"); else if (y < lastY - 6 || y < 240) hd.classList.remove("hide"); }
    lastY = y;
  }, { passive: true });
  const links = [...hd.querySelectorAll(".hd__links a")], ind = hd.querySelector(".hd__ind");
  function moveInd(a) { if (!a) { ind.style.opacity = 0; return; } ind.style.opacity = 1; ind.style.left = a.offsetLeft + "px"; ind.style.width = a.offsetWidth + "px"; }
  let active = null;
  const spy = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { active = links.find(a => a.getAttribute("href") === "#" + e.target.id) || null; links.forEach(a => a.classList.toggle("on", a === active)); moveInd(active); } }), { rootMargin: "-45% 0px -50% 0px" });
  links.forEach(a => { const t = document.querySelector(a.getAttribute("href")); if (t) spy.observe(t); a.addEventListener("mouseenter", () => moveInd(a)); });
  hd.querySelector(".hd__links").addEventListener("mouseleave", () => moveInd(active));
  const top = document.getElementById("top"); if (top) new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { active = null; links.forEach(a => a.classList.remove("on")); moveInd(null); } }), { threshold: .5 }).observe(top);
  function setMenu(open) {
    btn.setAttribute("aria-expanded", open); menu.hidden = !open; root.classList.toggle("menu-open", open);
    btn.querySelector(".hd__menu-t").textContent = open ? "סגירה" : "תפריט";
    if (open) menu.querySelector("a").focus();
  }
  btn.addEventListener("click", () => setMenu(menu.hidden));
  menu.addEventListener("click", e => { if (e.target.closest("a")) setMenu(false); });
  addEventListener("keydown", e => { if (e.key === "Escape" && !menu.hidden) { setMenu(false); btn.focus(); } });

  document.documentElement.dataset.header = "modern";
})();
