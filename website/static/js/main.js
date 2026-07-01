const header = document.querySelector("[data-header]");
const navToggle = document.querySelector("[data-nav-toggle]");
const siteNav = document.querySelector("[data-site-nav]");

if (header) {
  const setHeader = () => {
    header.classList.toggle("is-scrolled", window.scrollY > 18);
  };
  setHeader();
  window.addEventListener("scroll", setHeader, { passive: true });
}

if (navToggle && siteNav) {
  navToggle.addEventListener("click", () => {
    const open = navToggle.getAttribute("aria-expanded") === "true";
    navToggle.setAttribute("aria-expanded", String(!open));
    siteNav.classList.toggle("is-open", !open);
    document.body.classList.toggle("nav-open", !open);
  });

  siteNav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      navToggle.setAttribute("aria-expanded", "false");
      siteNav.classList.remove("is-open");
      document.body.classList.remove("nav-open");
    });
  });
}

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.16 });

document.querySelectorAll(".reveal").forEach((el) => revealObserver.observe(el));

const parallaxEls = Array.from(document.querySelectorAll("[data-parallax]"));
let ticking = false;

function updateParallax() {
  parallaxEls.forEach((el) => {
    const speed = Number(el.dataset.speed || 0.08);
    const rect = el.getBoundingClientRect();
    const midpoint = rect.top + rect.height / 2 - window.innerHeight / 2;
    el.style.setProperty("--parallax-y", `${midpoint * speed * -1}px`);
  });
  ticking = false;
}

if (parallaxEls.length && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  updateParallax();
  window.addEventListener("scroll", () => {
    if (!ticking) {
      window.requestAnimationFrame(updateParallax);
      ticking = true;
    }
  }, { passive: true });
}
