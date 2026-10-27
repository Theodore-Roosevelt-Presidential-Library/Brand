// Copy-to-clipboard for color swatches
document.addEventListener('click', (e) => {
  const b = e.target.closest('[data-copy]');
  if (!b) return;
  const v = b.getAttribute('data-copy');
  try { navigator.clipboard.writeText(v); } catch (_) {}
  b.classList.add('copied');
  setTimeout(() => b.classList.remove('copied'), 1200);
});

// Collapse the contents panel by default on small screens
const side = document.querySelector('details.side');
if (side && window.matchMedia('(max-width: 860px)').matches) side.removeAttribute('open');

// Filter for the editorial style guide
(function () {
  if (!document.body.classList.contains('page-editorial-style-guide')) return;
  const prose = document.querySelector('.prose');
  const h3s = [...prose.querySelectorAll('h3')];
  const entries = h3s.map((h) => {
    const wrap = document.createElement('section');
    wrap.className = 'entry';
    h.before(wrap);
    let n = h;
    const nodes = [];
    while (n && !(n !== h && /^H[123]$/.test(n.tagName)) && !(n.tagName === 'HR')) { nodes.push(n); n = n.nextElementSibling; }
    nodes.forEach((x) => wrap.appendChild(x));
    return wrap;
  });
  const box = document.createElement('div');
  box.className = 'filter';
  box.innerHTML = '<label class="small" for="q">Find a rule</label><input id="q" type="search" placeholder="e.g. donors, Teddy, gratitude, hours" autocomplete="off">';
  const first = prose.querySelector('h2');
  first.before(box);
  const q = box.querySelector('input');
  q.addEventListener('input', () => {
    const t = q.value.trim().toLowerCase();
    entries.forEach((s) => { s.hidden = t && !s.textContent.toLowerCase().includes(t); });
    prose.querySelectorAll('h2').forEach((h2) => {
      if (h2.id === 'quick-reference' || h2.id === 'open-questions') return;
      let n = h2.nextElementSibling, any = false;
      while (n && n.tagName !== 'H2') { if (n.classList.contains('entry') && !n.hidden) any = true; n = n.nextElementSibling; }
      h2.hidden = !!t && !any;
    });
  });
})();
