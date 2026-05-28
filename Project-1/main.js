// ── PAGE ROUTER ──
function navigate(pageId) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
  const page = document.getElementById(pageId);
  if (page) {
    page.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
  document.querySelectorAll(`[data-page="${pageId}"]`).forEach(el => el.classList.add('active'));
  closeMobileNav();
}

// ── TOAST ──
function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 3200);
}

// ── BACKEND MODAL ──
function showBackendModal() {
  document.getElementById('backend-modal').classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeModal() {
  document.getElementById('backend-modal').classList.remove('open');
  document.body.style.overflow = '';
}

// ── MOBILE NAV ──
function toggleMobileNav() {
  const nav = document.getElementById('mobile-nav');
  const burger = document.querySelector('.hamburger');
  nav.classList.toggle('open');
  burger.classList.toggle('open');
  burger.setAttribute('aria-expanded', nav.classList.contains('open'));
}
function closeMobileNav() {
  const nav = document.getElementById('mobile-nav');
  const burger = document.querySelector('.hamburger');
  nav.classList.remove('open');
  burger.classList.remove('open');
  burger.setAttribute('aria-expanded', 'false');
}

// ── CONTACT FORM ──
function handleContactForm(e) {
  e.preventDefault();
  showBackendModal();
}

// ── SEARCH ──
function handleSearch(e) {
  e.preventDefault();
  showBackendModal();
}

// ── SCROLL REVEAL ──
function initScrollReveal() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.card, .pillar, .section-header, .contact-item').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    observer.observe(el);
  });
}

// ── STAT COUNTER ANIMATION ──
function animateCounters() {
  document.querySelectorAll('.stat-num').forEach(el => {
    const text = el.textContent.trim();
    const num = parseFloat(text.replace(/[^0-9.]/g, ''));
    const suffix = text.replace(/[0-9.]/g, '');
    if (isNaN(num)) return;
    let start = 0;
    const duration = 1200;
    const step = 16;
    const increment = num / (duration / step);
    const timer = setInterval(() => {
      start += increment;
      if (start >= num) {
        start = num;
        clearInterval(timer);
      }
      el.textContent = (Number.isInteger(num) ? Math.round(start) : start.toFixed(1)) + suffix;
    }, step);
  });
}

// ── CLOSE MODAL ON ESC ──
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeModal();
});

// ── CLOSE MODAL ON BACKDROP CLICK ──
document.addEventListener('click', (e) => {
  if (e.target.classList.contains('modal-overlay')) closeModal();
});

// ── INIT ──
document.addEventListener('DOMContentLoaded', () => {
  navigate('home');
  initScrollReveal();

  // Trigger counter animation when hero stats come into view
  const statsEl = document.querySelector('.hero-stats');
  if (statsEl) {
    const statsObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounters();
          statsObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    statsObserver.observe(statsEl);
  }
});