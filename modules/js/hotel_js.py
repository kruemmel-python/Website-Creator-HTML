def generate_hotel_js():
    """Generiert den JavaScript-Code für das Hotel-Template."""

    def generate_menu_loading_js():
        """Generiert den JavaScript-Code zum Laden und Einfügen des Menüs."""
        return '''
// Menü laden und einfügen
fetch('./nav.json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Fehler beim Laden des Menüs');
        }
        return response.json();
    })
    .then(data => {
        const navContainer = document.getElementById('nav');
        let menuHTML = '<li><a href="index.html">Home</a></li>'; // Home-Button hinzufügen

        data.menuItems.forEach(item => {
            if (item.subMenu && item.subMenu.length > 0) {
                menuHTML += `<li class="has-submenu"><a href="#" onclick="toggleSubMenu(this); return false;">${item.title}</a><ul class="submenu">`;
                item.subMenu.forEach(subItem => {
                    menuHTML += `<li><a href="${subItem.url}">${subItem.title}</a></li>`;
                });
                menuHTML += '</ul></li>';
            } else {
                menuHTML += `<li><a href="${item.url}">${item.title}</a></li>`;
            }
        });

        navContainer.querySelector("ul").innerHTML = menuHTML;

        const hamburgerButton = document.querySelector('.hamburger');
        if (hamburgerButton) {
            hamburgerButton.addEventListener('click', toggleMenu);
        }
    })
    .catch(error => {
        console.error(error);
        document.getElementById('nav').innerHTML = '<li>Menü konnte nicht geladen werden.</li>';
    });
'''

    def generate_toggle_submenu_js():
        """Generiert den JavaScript-Code zum Ein- und Ausblenden des Untermenüs."""
        return '''
// Funktion zum Ein- und Ausblenden des Untermenüs
function toggleSubMenu(element) {
    const parentLi = element.parentElement;
    const submenu = parentLi.querySelector('.submenu');
    submenu.classList.toggle('open');
}
'''

    def generate_toggle_menu_js():
        """Generiert den JavaScript-Code zum Ein- und Ausblenden des Menüs (für mobile Geräte)."""
        return '''
// Funktion zum Ein- und Ausblenden des Menüs (für mobile Geräte)
function toggleMenu() {
    const navContainer = document.getElementById('nav');
    navContainer.classList.toggle('open');
}
'''

    def generate_fade_in_title_js():
        """Generiert den JavaScript-Code zum langsamen Einblenden des Titels."""
        return '''
// Funktion zum langsamen Einblenden des Titels
document.addEventListener('DOMContentLoaded', function() {
    const title = document.querySelector('.header h1');
    if (title) {
        title.classList.add('fade-in');
    }
});
'''

    js_content = generate_menu_loading_js() + generate_toggle_submenu_js() + generate_toggle_menu_js() + generate_fade_in_title_js()
    return js_content
