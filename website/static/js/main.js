const introOverlay = document.querySelector("[data-intro-overlay]");

if (introOverlay) {
  const introVideo = introOverlay.querySelector("video");
  const introSkip = introOverlay.querySelector("[data-intro-skip]");
  const alreadyPlayed = sessionStorage.getItem("introPlayed");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const dismissIntro = () => {
    introOverlay.classList.add("is-hidden");
    document.body.classList.remove("intro-active");
    sessionStorage.setItem("introPlayed", "1");
    window.setTimeout(() => introOverlay.remove(), 700);
  };

  if (alreadyPlayed || reducedMotion || !introVideo) {
    introOverlay.remove();
  } else {
    document.body.classList.add("intro-active");
    introVideo.addEventListener("ended", dismissIntro);
    introOverlay.addEventListener(
      "touchmove",
      (event) => event.preventDefault(),
      { passive: false }
    );
    if (introSkip) {
      introSkip.addEventListener("click", dismissIntro);
    }
    const playPromise = introVideo.play();
    if (playPromise && typeof playPromise.catch === "function") {
      playPromise.catch(dismissIntro);
    }
    // Safety net in case the video stalls or metadata is wrong.
    window.setTimeout(dismissIntro, 15000);
  }
}

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
