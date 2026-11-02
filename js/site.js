(function () {
  var root = document.documentElement;
  root.classList.add("js");

  var header = document.querySelector("[data-header]");
  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");
  var video = document.querySelector("video.hero-media");
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var booking = document.querySelector("[data-booking]");

  function onScroll() {
    if (!header) return;
    header.classList.toggle("is-solid", window.scrollY > 24);
  }

  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      header.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      document.body.style.overflow = open ? "hidden" : "";
    });
    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("is-open");
        header.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      });
    });
  }

  if (video && reduced) {
    video.pause();
    video.removeAttribute("autoplay");
  }

  if ("IntersectionObserver" in window && !reduced) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.16 });
    document.querySelectorAll(".reveal").forEach(function (el) { observer.observe(el); });
  } else {
    document.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("is-in"); });
  }

  var filters = document.querySelector("[data-filters]");
  if (filters) {
    var buttons = filters.querySelectorAll("button");
    var rows = document.querySelectorAll("[data-cat]");
    var empty = document.querySelector("[data-empty]");
    function apply(cat) {
      var shown = 0;
      rows.forEach(function (row) {
        var on = cat === "all" || row.getAttribute("data-cat") === cat;
        row.hidden = !on;
        if (on) shown += 1;
      });
      buttons.forEach(function (btn) {
        btn.setAttribute("aria-pressed", btn.getAttribute("data-filter") === cat ? "true" : "false");
      });
      if (empty) empty.classList.toggle("is-on", shown === 0);
    }
    filters.addEventListener("click", function (event) {
      var btn = event.target.closest("button");
      if (!btn) return;
      apply(btn.getAttribute("data-filter"));
    });
    var initial = new URLSearchParams(window.location.search).get("cat") || "all";
    if (![...buttons].some(function (btn) { return btn.getAttribute("data-filter") === initial; })) initial = "all";
    apply(initial);
  }

  function closeNav() {
    if (!nav || !toggle) return;
    nav.classList.remove("is-open");
    if (header) header.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
    toggle.setAttribute("aria-label", "Open menu");
    document.body.style.overflow = "";
  }

  document.addEventListener("click", function (event) {
    var closer = event.target.closest("[data-booking-close]");
    if (closer) {
      var dialog = closer.closest("dialog");
      if (dialog) dialog.close();
      return;
    }
    var trigger = event.target.closest("[data-book]");
    if (!trigger || !booking) return;
    closeNav();
    var exp = trigger.getAttribute("data-experience") || "";
    var select = booking.querySelector("[name=experience]");
    if (select && exp) select.value = exp;
    if (typeof booking.showModal === "function") booking.showModal();
  });

  if (booking) {
    booking.addEventListener("click", function (event) {
      if (event.target === booking) booking.close();
    });
  }

  document.querySelectorAll("[data-enquiry]").forEach(function (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var data = new FormData(form);
      var lines = [
        "Hello Mranzi Tours & Safaris, I would like to book.",
        "",
        "Name: " + (data.get("name") || "").trim(),
        "Experience: " + (data.get("experience") || "").trim(),
        "Dates: " + (data.get("dates") || "").trim(),
        "Group size: " + (data.get("group") || "").trim(),
        "Pickup: " + (data.get("pickup") || "").trim(),
        "Note: " + ((data.get("note") || "").trim() || "—")
      ];
      var phone = form.getAttribute("data-phone");
      window.open("https://wa.me/" + phone + "?text=" + encodeURIComponent(lines.join("\n")), "_blank", "noopener");
      var dialog = form.closest("dialog");
      if (dialog && dialog.open) dialog.close();
    });
  });
})();
