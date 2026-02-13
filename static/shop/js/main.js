/**
 * AURA FARMING – Frontend interactions & animations
 */

(function () {
  'use strict';

  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  // ----- Scroll-triggered animations -----
  function initScrollAnimations() {
    var elements = document.querySelectorAll('.animate-on-scroll');
    if (!elements.length) return;

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
          }
        });
      },
      { rootMargin: '0px 0px -60px 0px', threshold: 0.1 }
    );

    elements.forEach(function (el) {
      observer.observe(el);
    });
  }

  // ----- Navbar: add background on scroll -----
  function initNavbarScroll() {
    var navbar = document.querySelector('.navbar');
    if (!navbar) return;

    function onScroll() {
      if (window.scrollY > 20) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    }

    window.addEventListener('scroll', function () {
      window.requestAnimationFrame(onScroll);
    });
    onScroll();
  }

  // ----- Auto-dismiss alerts after 5s -----
  function initAlertDismiss() {
    document.querySelectorAll('.alert-dismissible').forEach(function (alert) {
      setTimeout(function () {
        var bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
        bsAlert.close();
      }, 5000);
    });
  }

  // ----- Smooth scroll for anchor links -----
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
      var id = anchor.getAttribute('href');
      if (id === '#') return;
      var target = document.querySelector(id);
      if (!target) return;
      anchor.addEventListener('click', function (e) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    });
  }

  // ----- Add to cart button feedback (visual) -----
  function initAddToCartFeedback() {
    document.querySelectorAll('a[href*="add_to_cart"]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var text = btn.textContent.trim();
        if (text === 'Added!') return;
        btn.textContent = 'Added!';
      });
    });
  }

  // ----- Bootstrap carousel: pause on hover -----
  function initCarouselHover() {
    document.querySelectorAll('.carousel').forEach(function (carousel) {
      carousel.addEventListener('mouseenter', function () {
        var bs = bootstrap.Carousel.getInstance(carousel);
        if (bs) bs.pause();
      });
      carousel.addEventListener('mouseleave', function () {
        var bs = bootstrap.Carousel.getInstance(carousel);
        if (bs) bs.cycle();
      });
    });
  }

  // ----- Run all -----
  ready(function () {
    initScrollAnimations();
    initNavbarScroll();
    initAlertDismiss();
    initSmoothScroll();
    initAddToCartFeedback();
    initCarouselHover();
  });
})();
