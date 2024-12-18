import json
import os
from modules.css.hotel_css import generate_hotel_css
from modules.html.hotel_html import generate_hotel_html
from modules.js.hotel_js import generate_hotel_js

def create_directory(path):
    """Erstellt ein Verzeichnis, falls es nicht existiert."""
    os.makedirs(path, exist_ok=True)

def write_file(path, content):
    """Schreibt Inhalt in eine Datei."""
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

def generate_submenu_html(template_name, submenu_name, options):
    """Generiert HTML-Inhalt für eine Untermenüseite."""
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{submenu_name}</title>
    <link rel="stylesheet" href="{template_name}_styles.css">
    <script src="animations.js"></script>
</head>
<body>

    <header class="header">
        <h1>{submenu_name}</h1>
    </header>
    <nav class="menu" id="nav">
        <ul></ul>
    </nav>
    <main style="margin-left: 250px; padding: 20px;">
        <section class="section">
            <h1>{submenu_name}</h1>
            <p>This is the page for {submenu_name}. Enjoy exploring our exclusive offerings and amenities.</p>
        </section>
    </main>

    <footer style="background-color: {options['footer_background_color']}; color: {options['footer_text_color']}; font-family: {options['footer_font_family']}; font-size: {options['footer_font_size']}px; padding: 1rem; text-align: {options['footer_text_align']}; margin-top: auto;">
        <p>&copy; 2024 CipherCore. All rights reserved.</p>
    </footer>

    <script src="load_menu.js"></script>
</body>
</html>'''

def generate_template(template_name, options):
    template_folder = os.path.join("templates", template_name)
    create_directory(template_folder)

    # Generiere CSS
    css_content = generate_hotel_css(options["menu_type"], options)
    css_path = os.path.join(template_folder, f"{template_name}_styles.css")
    write_file(css_path, css_content)

    # Generiere Haupt-HTML-Seite (z.B. hotel.html)
    html_content = generate_hotel_html(options["menu_type"], options["menu_items"], options["menu_names"], options["submenu_names"])
    html_path = os.path.join(template_folder, f"{template_name}.html")
    write_file(html_path, html_content)

    # Generiere JavaScript
    js_content = generate_hotel_js()
    js_path = os.path.join(template_folder, "animations.js")
    write_file(js_path, js_content)

    # Generiere eine HTML-Seite für jeden Untermenüpunkt, die das Menü und alle Funktionen übernimmt
    for i, submenu_list in enumerate(options["submenu_names"]):
        for submenu_name in submenu_list:
            submenu_html_content = generate_submenu_html(template_name, submenu_name, options)
            submenu_path = os.path.join(template_folder, f"{submenu_name.replace(' ', '_')}.html")
            write_file(submenu_path, submenu_html_content)

    # Generiere nav.json für das Menü
    nav_data = {
        "menuItems": [
            {
                "title": options["menu_names"][i],
                "url": f"{options['menu_names'][i].replace(' ', '_')}.html",
                "subMenu": [{"title": submenu, "url": f"{submenu.replace(' ', '_')}.html"} for submenu in submenu_list]
            }
            for i, submenu_list in enumerate(options["submenu_names"])
        ]
    }

    nav_json_path = os.path.join(template_folder, "nav.json")
    with open(nav_json_path, "w", encoding="utf-8") as json_file:
        json.dump(nav_data, json_file, indent=4)

    print(f"{template_name.capitalize()} template created with HTML, CSS, JavaScript, submenu pages, and nav.json.")
