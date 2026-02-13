// Modern Professional Interactions for AURA FARMING

document.addEventListener('DOMContentLoaded', function() {
    // Global IntersectionObserver for animate-on-scroll elements
    const scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                scrollObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -30px 0px' });

    document.querySelectorAll('.animate-on-scroll, .fade-in').forEach(el => {
        scrollObserver.observe(el);
    });

    // Enhanced product card interactions
    const productCards = document.querySelectorAll('.product-card');
    
    productCards.forEach(card => {
        // Add smooth hover effects
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
        });
        
        // Add loading states for buttons
        const buttons = card.querySelectorAll('.btn');
        buttons.forEach(btn => {
            btn.addEventListener('click', function(e) {
                if (this.href && this.href.includes('add_to_cart')) {
                    e.preventDefault();
                    
                    const originalText = this.innerHTML;
                    this.innerHTML = '<span class="loading-spinner"></span> Adding...';
                    this.disabled = true;
                    
                    // Simulate API call
                    setTimeout(() => {
                        window.location.href = this.href;
                    }, 500);
                }
            });
        });
    });
    
    // Search enhancement
    const searchInput = document.querySelector('input[type="search"]');
    if (searchInput) {
        let searchTimeout;
        
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            
            // Add visual feedback
            this.style.borderColor = 'var(--primary-green)';
            
            searchTimeout = setTimeout(() => {
                this.style.borderColor = '';
            }, 1000);
        });
        
        // Add search suggestions (placeholder functionality)
        searchInput.addEventListener('focus', function() {
            this.placeholder = 'Try searching for "toolkits", "plants", "organic soil"...';
        });
        
        searchInput.addEventListener('blur', function() {
            this.placeholder = 'Search for plants, tools, kits...';
        });
    }
    
    // Enhanced form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = this.querySelector('button[type="submit"], input[type="submit"]');
            
            if (submitBtn) {
                const originalText = submitBtn.innerHTML || submitBtn.value;
                submitBtn.innerHTML = '<span class="loading-spinner"></span> Processing...';
                submitBtn.disabled = true;
            }
        });
    });
    
    // Cart badge animation
    const cartBadge = document.querySelector('.badge');
    if (cartBadge) {
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.type === 'childList' || mutation.type === 'characterData') {
                    // Animate when cart count changes
                    cartBadge.style.transform = 'scale(1.3)';
                    setTimeout(() => {
                        cartBadge.style.transform = 'scale(1)';
                    }, 200);
                }
            });
        });
        
        observer.observe(cartBadge, { childList: true, subtree: true, characterData: true });
    }
    
    // Toast notification system (for future use)
    window.showToast = function(message, type = 'success') {
        const toast = document.createElement('div');
        toast.className = `toast-notification toast-${type}`;
        toast.innerHTML = `
            <div class="toast-content">
                <i class="bi bi-check-circle-fill"></i>
                <span>${message}</span>
            </div>
        `;
        
        // Add CSS for toast
        toast.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--primary-green);
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 0.5rem;
            z-index: 9999;
            opacity: 0;
            transform: translateY(-20px);
            transition: all 0.3s ease;
            box-shadow: var(--shadow-lg);
        `;
        
        document.body.appendChild(toast);
        
        // Animate in
        setTimeout(() => {
            toast.style.opacity = '1';
            toast.style.transform = 'translateY(0)';
        }, 100);
        
        // Remove after 3 seconds
        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateY(-20px)';
            setTimeout(() => document.body.removeChild(toast), 300);
        }, 3000);
    };
    
    // Smooth scroll for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Performance optimization: Lazy load images
    const images = document.querySelectorAll('img[loading="lazy"]');
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.style.transition = 'opacity 0.3s';
                img.style.opacity = '0';
                
                const tempImg = new Image();
                tempImg.onload = () => {
                    img.style.opacity = '1';
                };
                tempImg.src = img.src;
                
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
});

// Add CSS for loading spinner
const style = document.createElement('style');
style.textContent = `
    .toast-notification {
        max-width: 300px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
    }
    
    .toast-content {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    .toast-success {
        background: var(--primary-green) !important;
    }
    
    .toast-error {
        background: #ef4444 !important;
    }
    
    .toast-warning {
        background: #f59e0b !important;
    }
    
    .loading-spinner {
        display: inline-block;
        width: 16px;
        height: 16px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        border-top-color: #fff;
        animation: spin 1s ease-in-out infinite;
    }
    
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
`;

document.head.appendChild(style);