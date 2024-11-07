from css_generator import CSS

def add_header_styles(css, options):
    """Fügt Stile für den Header hinzu, einschließlich dynamischer Textausrichtung."""
    
    # Basisstile für den Header
    header_styles = {
        'background-color': options['header_background_color'],
        'color': options['header_text_color'],
        'padding': '1.5rem',
        'font-size': f"{options['header_font_size']}px",
        'font-weight': 'bold',
        'font-family': options['header_font_family'],
        'display': 'flex',
        'align-items': 'center',
    }

    # Dynamische Ausrichtung des Headers basierend auf der GUI-Option
    if options['header_text_align'] == 'center':
        header_styles['justify-content'] = 'center'
    elif options['header_text_align'] == 'right':
        header_styles['justify-content'] = 'flex-end'
    else:  # Standardmäßig linksbündig
        header_styles['justify-content'] = 'flex-start'

    css.add_rule('.header', header_styles)

    # Titelstile für h1-Element im Header
    css.add_rule('.header h1', {
        'opacity': '0',
        'transition': 'opacity 2s ease-in',
        'margin-left': '20px' if options['header_text_align'] != 'center' else '0'
    })
    css.add_rule('.header h1.fade-in', {
        'opacity': '1'
    })

def add_content_styles(css, options):
    """Fügt Stile für den Hauptinhalt hinzu, einschließlich dynamischer Textausrichtung."""
    css.add_rule('.content', {
        'text-align': options['content_text_align']  # Dynamische Textausrichtung für den Inhalt
    })

def add_header_menu_styles(css, options):
    """Fügt Stile für das Header-Menü hinzu."""
    css.add_rule('.menu', {
        'display': 'flex',
        'gap': '1rem',
        'align-items': 'center',
        'position': 'relative',
        'text-align': options['menu_text_align']  # Dynamische Textausrichtung
    })
    css.add_rule('.menu ul', {'display': 'flex', 'list-style': 'none', 'padding': '0', 'margin': '0'})
    css.add_rule('.menu a', {
        'color': options['menu_text_color'],
        'text-decoration': 'none',
        'padding': '0.8rem 1rem',
        'border-radius': '5px',
        'transition': 'background-color 0.3s ease, transform 0.3s ease'
    })
    css.add_rule('.menu a:hover', {'background-color': '#4A90E2', 'transform': 'scale(1.05)'})

    css.add_rule('.has-submenu', {'position': 'relative'})
    css.add_rule('.submenu', {
        'display': 'none',
        'position': 'absolute',
        'top': '100%',
        'left': '0',
        'background-color': '#0022CC',
        'border-radius': '5px',
        'padding': '0.5rem',
        'list-style': 'none',
        'min-width': '150px',
        'z-index': '10'
    })
    css.add_rule('.submenu a', {
        'padding': '0.5rem 1rem',
        'display': 'block',
        'white-space': 'nowrap',
        'color': '#FFFFFF',
        'text-decoration': 'none'
    })
    css.add_rule('.submenu a:hover', {'background-color': '#0059b3'})
    css.add_rule('.submenu.open', {'display': 'block'})  # Sichtbar bei "open" Klasse

def add_sidebar_menu_styles(css, options):
    """Fügt Stile für das Sidebar-Menü hinzu, einschließlich dynamischer Textausrichtung."""
    css.add_rule('.menu', {
        'width': '250px',
        'background-color': options['menu_background_color'],
        'color': options['menu_text_color'],
        'padding': '10px',
        'position': 'fixed',
        'height': '100vh',
        'overflow-y': 'auto',
        'font-family': options['menu_font_family'],
        'font-size': f"{options['menu_font_size']}px",
        'text-align': options['menu_text_align']  # Dynamische Textausrichtung
    })
    css.add_rule('.menu ul', {'list-style': 'none', 'padding': '0'})
    css.add_rule('.menu a', {
        'color': options['menu_text_color'],
        'background-color': '#4A90E2',
        'text-decoration': 'none',
        'display': 'block',
        'padding': '0.8rem',
        'margin': '0.5rem 0',
        'border-radius': '5px',
        'transition': 'background-color 0.3s ease, transform 0.3s ease'
    })
    css.add_rule('.menu a:hover', {'background-color': '#0034FF', 'transform': 'translateX(5px)'})

    css.add_rule('.has-submenu', {'position': 'relative'})
    css.add_rule('.submenu', {
        'display': 'none',
        'position': 'relative',
        'left': '0',
        'background-color': '#0022CC',
        'border-radius': '5px',
        'padding': '0.5rem',
        'list-style': 'none',
        'min-width': '150px',
        'z-index': '10'
    })
    css.add_rule('.submenu a', {
        'padding': '0.5rem 1rem',
        'display': 'block',
        'white-space': 'nowrap',
        'color': '#FFFFFF',
        'text-decoration': 'none'
    })
    css.add_rule('.submenu a:hover', {'background-color': '#0059b3'})
    css.add_rule('.submenu.open', {'display': 'block'})  # Sichtbar bei "open" Klasse

def add_common_styles(css, options):
    """Fügt gemeinsame Stile hinzu, einschließlich dynamischer Textausrichtung für den Footer."""
    css.add_rule('.has-submenu > a', {'font-weight': 'bold', 'cursor': 'pointer'})
    css.add_rule('body', {
        'background-color': options['background_color'],
        'color': options['text_color'],
        'font-family': options['font_family'],
        'font-size': f"{options['font_size']}px",
        'display': 'flex',
        'flex-direction': 'column',
        'min-height': '100vh',
        'margin': '0',
        'padding': '0'
    })
    css.add_rule('footer', {
        'background-color': options['footer_background_color'],
        'color': options['footer_text_color'],
        'font-family': options['footer_font_family'],
        'font-size': f"{options['footer_font_size']}px",
        'padding': '1rem',
        'text-align': options['footer_text_align'],  # Dynamische Textausrichtung
        'margin-top': 'auto'
    })

def generate_hotel_css(menu_type, options):
    css = CSS()

    # Styling für den Header
    add_header_styles(css, options)

    # Styling für den Hauptinhalt
    add_content_styles(css, options)

    # Styling für das Menü
    if menu_type == "header":
        add_header_menu_styles(css, options)
    else:
        add_sidebar_menu_styles(css, options)

    # Gemeinsame Stile
    add_common_styles(css, options)

    return css.css_text()
