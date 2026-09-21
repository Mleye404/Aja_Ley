// AJA LEY — comportements front-end simples (menu mobile, galerie produit).
document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.getElementById("navToggle");
  var closeBtn = document.getElementById("mobileNavClose");
  var mobileNav = document.getElementById("mobileNav");
  var backdrop = document.getElementById("mobileNavBackdrop");

  if (!toggle || !mobileNav || !backdrop) return;

  function openMenu() {
    mobileNav.classList.add("open");
    backdrop.classList.add("open");
    toggle.classList.add("active");
    toggle.setAttribute("aria-expanded", "true");
    mobileNav.setAttribute("aria-hidden", "false");
    document.body.classList.add("nav-open");
  }

  function closeMenu() {
    mobileNav.classList.remove("open");
    backdrop.classList.remove("open");
    toggle.classList.remove("active");
    toggle.setAttribute("aria-expanded", "false");
    mobileNav.setAttribute("aria-hidden", "true");
    document.body.classList.remove("nav-open");
  }

  toggle.addEventListener("click", function () {
    if (mobileNav.classList.contains("open")) {
      closeMenu();
    } else {
      openMenu();
    }
  });

  if (closeBtn) closeBtn.addEventListener("click", closeMenu);
  backdrop.addEventListener("click", closeMenu);

  mobileNav.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", closeMenu);
  });

  // Ferme le menu si la fenêtre repasse en largeur desktop.
  window.addEventListener("resize", function () {
    if (window.innerWidth > 900) closeMenu();
  });
});
