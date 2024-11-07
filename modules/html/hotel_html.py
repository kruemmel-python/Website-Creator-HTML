def generate_header_html(menu_type):
    """Generiert den HTML-Code für den Header basierend auf dem Menütyp."""
    if menu_type == "header":
        return '''
<header class="header">
    <h1>Hotel Template</h1>
    <nav class="menu" id="nav">
        <ul></ul>
    </nav>
</header>
'''
    else:
        return '''
<header class="header">
    <h1>Hotel Template</h1>
</header>
<nav class="menu" id="nav">
    <ul></ul>
</nav>
'''

def get_main_style(menu_type):
    """Gibt den Stil für das Haupt-Element basierend auf dem Menütyp zurück."""
    if menu_type == "header":
        return 'style="padding-top: 80px;"'  # Abstand, um Platz für das Header-Menü zu schaffen
    else:
        return 'style="margin-left: 250px; padding: 20px;"'

def generate_footer_html():
    """Generiert den HTML-Code für den Footer."""
    return '''
<footer class="footer">
    <p>&copy; 2023 Hotel Template. All rights reserved.</p>
</footer>
'''

def generate_hotel_html(menu_type, menu_items, menu_names, submenu_names):
    """Generiert das gesamte HTML-Dokument für die Startseite."""
    header_html = generate_header_html(menu_type)
    main_style = get_main_style(menu_type)
    footer_html = generate_footer_html()

    # Gesamtes HTML-Dokument für die Startseite
    html_content = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hotel Template</title>
    <link rel="stylesheet" href="hotel_styles.css">
    <script src="animations.js"></script>
</head>
<body>

    {header_html}
    <main class="content" {main_style}>
        <section class="section">
            <h1>Welcome to Our Stunning Hotel</h1>
            <p>Enjoy luxurious rooms with breathtaking views and world-class amenities.</p>
            <button class="button" onclick="fadeInText()">Check available rooms</button>
        </section>
    </main>

    {footer_html}

    <script src="load_menu.js"></script>
</body>
</html>'''
    return html_content
