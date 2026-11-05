// Global Test Data — small progressive enhancements: copy buttons, status filters, search.
(function () {
  "use strict";

  // Copy buttons
  document.addEventListener("click", function (ev) {
    var btn = ev.target.closest("button.copy");
    if (!btn) return;
    var text = btn.getAttribute("data-copy");
    var done = function () {
      btn.textContent = "Copied";
      btn.classList.add("done");
      setTimeout(function () { btn.textContent = "Copy"; btn.classList.remove("done"); }, 1400);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, function () {});
    }
  });

  // Status filters on country pages
  var boxes = document.querySelectorAll("input[data-filter]");
  function applyFilters() {
    var hidden = {};
    boxes.forEach(function (b) { if (!b.checked) hidden[b.getAttribute("data-filter")] = true; });
    document.querySelectorAll("section.cat:not(.avoid) tr[data-status]").forEach(function (tr) {
      tr.hidden = !!hidden[tr.getAttribute("data-status")];
    });
  }
  boxes.forEach(function (b) { b.addEventListener("change", applyFilters); });

  // Search on the directory page
  var q = document.getElementById("q");
  var out = document.getElementById("results");
  if (!q || !out) return;
  var data = null;
  var labels = { "reserved": "Reserved", "published-example": "Official example", "derived": "Derived", "avoid": "Avoid" };
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function render(term) {
    term = term.trim().toLowerCase();
    if (!term || !data) { out.hidden = true; out.innerHTML = ""; return; }
    var words = term.split(/\s+/);
    var hits = data.filter(function (x) {
      var hay = [x.country, x.country_name, x.type, x.value, x.label, x.category, x.status, x.notes || ""]
        .join(" ").toLowerCase();
      return words.every(function (w) { return hay.indexOf(w) !== -1; });
    }).slice(0, 60);
    out.hidden = false;
    if (!hits.length) { out.innerHTML = '<p class="muted">No matches.</p>'; return; }
    out.innerHTML = "<ul>" + hits.map(function (x) {
      var href = x.country.toLowerCase() + "/index.html#" + encodeURIComponent(x.id);
      return '<li><a href="' + href + '"><code>' + esc(x.value) + "</code></a> " +
        '<span class="badge s-' + esc(x.status) + '">' + esc(labels[x.status] || x.status) + "</span> " +
        '<span class="rmeta">' + esc(x.country_name) + " · " + esc(x.type) + " — " + esc(x.label) + "</span></li>";
    }).join("") + "</ul>";
  }
  q.addEventListener("input", function () {
    if (data) { render(q.value); return; }
    fetch("data/all.json").then(function (r) { return r.json(); }).then(function (d) {
      data = d; render(q.value);
    }).catch(function () { out.hidden = false; out.innerHTML = '<p class="muted">Search data could not be loaded.</p>'; });
  });
})();
