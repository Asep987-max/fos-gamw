// Script untuk Toggler Menu Mobile
const mobileMenuButton = document.getElementById('mobile-menu-button');
const mobileMenu = document.getElementById('mobile-menu');

mobileMenuButton.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});

// Script untuk menutup menu mobile saat link di klik (opsional)
const mobileMenuLinks = mobileMenu.querySelectorAll('a');
mobileMenuLinks.forEach(link => {
    link.addEventListener('click', () => {
        mobileMenu.classList.add('hidden');
    });
});

// Script untuk menampilkan tahun saat ini di footer
document.getElementById('tahun').textContent = new Date().getFullYear();