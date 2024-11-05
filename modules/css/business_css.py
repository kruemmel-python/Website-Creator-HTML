from css_generator import CSS  # Verwende nun die lokale css_generator.py

def generate_business_css():
    css = CSS()
    css.add_rule('body', {
        'font-family': 'Verdana, sans-serif',
        'color': '#222',
        'margin': '0',
        'padding': '0'
    })
    css.add_rule('.header', {
        'background-color': '#444',
        'color': '#fff',
        'padding': '30px',
        'text-align': 'center',
        'font-size': '28px'
    })
    css.add_rule('.section', {
        'background-color': '#f4f4f4',
        'padding': '20px',
        'text-align': 'left'
    })
    css.add_rule('.button', {
        'background-color': '#007bff',
        'padding': '10px 20px',
        'color': '#fff',
        'border': 'none',
        'cursor': 'pointer'
    })
    return css.css_text()
