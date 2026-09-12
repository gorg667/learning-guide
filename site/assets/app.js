/* Learning How to Learn — tiny client script: nav toggle, theme, search, TOC highlight */
(function () {
  'use strict';

  // Mobile nav
  var menuBtn = document.getElementById('menu-btn');
  if (menuBtn) {
    menuBtn.addEventListener('click', function () {
      var open = document.body.classList.toggle('nav-open');
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('click', function (e) {
      if (document.body.classList.contains('nav-open') &&
          !e.target.closest('#sidebar') && !e.target.closest('#menu-btn')) {
        document.body.classList.remove('nav-open');
        menuBtn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // Theme toggle
  var themeBtn = document.getElementById('theme-btn');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var root = document.documentElement;
      var cur = root.getAttribute('data-theme');
      var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      var isDark = cur ? cur === 'dark' : prefersDark;
      var next = isDark ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('theme', next); } catch (e) {}
    });
  }

  // Scroll the active sidebar item into view
  var active = document.querySelector('.sidebar li.active');
  if (active && active.scrollIntoView) {
    try { active.scrollIntoView({ block: 'center' }); } catch (e) {}
  }

  // TOC highlight on scroll
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  if (tocLinks.length && 'IntersectionObserver' in window) {
    var map = {};
    tocLinks.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var headings = Object.keys(map).map(function (id) { return document.getElementById(id); }).filter(Boolean);
    var current = null;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          if (current) current.classList.remove('active');
          current = map[en.target.id];
          if (current) current.classList.add('active');
        }
      });
    }, { rootMargin: '-70px 0px -70% 0px', threshold: 0 });
    headings.forEach(function (h) { io.observe(h); });
  }

  // Search
  var input = document.getElementById('search');
  var results = document.getElementById('search-results');
  if (input && results) {
    var index = null, loading = false, sel = -1;

    function load(cb) {
      if (index) return cb();
      if (loading) return;
      loading = true;
      fetch('search.json').then(function (r) { return r.json(); }).then(function (j) {
        index = j; loading = false; cb();
      }).catch(function () { loading = false; });
    }

    function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
    function hl(text, terms) {
      var out = esc(text);
      terms.forEach(function (t) {
        if (!t) return;
        var re = new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig');
        out = out.replace(re, '<mark>$1</mark>');
      });
      return out;
    }

    function run() {
      var q = input.value.trim().toLowerCase();
      sel = -1;
      if (q.length < 2) { results.hidden = true; results.innerHTML = ''; return; }
      load(function () {
        var terms = q.split(/\s+/);
        var hits = [];
        index.forEach(function (ch) {
          var title = ch.t.toLowerCase(), summ = ch.s.toLowerCase();
          var score = 0;
          terms.forEach(function (t) {
            if (title.indexOf(t) >= 0) score += 10;
            if (summ.indexOf(t) >= 0) score += 3;
          });
          if (score) hits.push({ score: score, url: ch.u, title: ch.t, ctx: ch.p + ' · ' + ch.s });
          ch.h.forEach(function (h) {
            var ht = h.t.toLowerCase(), s = 0;
            terms.forEach(function (t) { if (ht.indexOf(t) >= 0) s += 5; });
            if (s) hits.push({ score: s, url: ch.u + '#' + h.id, title: h.t, ctx: 'in ' + ch.t });
          });
        });
        hits.sort(function (a, b) { return b.score - a.score; });
        hits = hits.slice(0, 20);
        if (!hits.length) {
          results.innerHTML = '<div class="sr-ctx" style="padding:.6rem">No matches. Try a different word.</div>';
        } else {
          results.innerHTML = hits.map(function (h) {
            return '<a href="' + h.url + '"><div class="sr-title">' + hl(h.title, terms) + '</div><div class="sr-ctx">' + esc(h.ctx) + '</div></a>';
          }).join('');
        }
        results.hidden = false;
      });
    }

    input.addEventListener('input', run);
    input.addEventListener('focus', function () { if (input.value.trim().length >= 2) run(); });
    input.addEventListener('keydown', function (e) {
      var items = results.querySelectorAll('a');
      if (e.key === 'Escape') { results.hidden = true; input.blur(); return; }
      if (!items.length) return;
      if (e.key === 'ArrowDown') { e.preventDefault(); sel = Math.min(items.length - 1, sel + 1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); sel = Math.max(0, sel - 1); }
      else if (e.key === 'Enter') { e.preventDefault(); if (sel >= 0) items[sel].click(); else items[0].click(); return; }
      else return;
      Array.prototype.forEach.call(items, function (a, i) { a.classList.toggle('sel', i === sel); });
      items[sel].scrollIntoView({ block: 'nearest' });
    });
    document.addEventListener('click', function (e) {
      if (!e.target.closest('#search') && !e.target.closest('#search-results')) results.hidden = true;
    });
    // "/" focuses search
    document.addEventListener('keydown', function (e) {
      if (e.key === '/' && document.activeElement !== input && !/INPUT|TEXTAREA/.test(document.activeElement.tagName)) {
        e.preventDefault(); input.focus();
      }
    });
  }

  // Remember reading position per chapter (lightweight)
  try {
    var key = 'pos:' + location.pathname;
    var saved = sessionStorage.getItem(key);
    if (saved && !location.hash) window.scrollTo(0, parseInt(saved, 10));
    window.addEventListener('scroll', function () {
      sessionStorage.setItem(key, String(window.scrollY));
    }, { passive: true });
  } catch (e) {}
})();
