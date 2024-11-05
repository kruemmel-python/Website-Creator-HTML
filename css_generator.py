class CSS:
    def __init__(self):
        """Initialisiert eine neue CSS-Klasse."""
        self.rules = []

    def add_rule(self, selector, properties):
        """Fügt eine CSS-Regel hinzu.

        Args:
            selector (str): Der CSS-Selektor.
            properties (dict): Ein Dictionary mit CSS-Eigenschaften und ihren Werten.
        """
        properties_str = "; ".join([f"{key}: {value}" for key, value in properties.items()])
        rule = f"{selector} {{ {properties_str}; }}"
        self.rules.append(rule)

    def css_text(self):
        """Gibt den gesamten CSS-Text als String zurück."""
        return "\n".join(self.rules)

    def save(self, filename):
        """Speichert den CSS-Text in einer Datei.

        Args:
            filename (str): Der Dateiname, unter dem der CSS-Text gespeichert werden soll.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(self.css_text())
        except IOError as e:
            print(f"Fehler beim Schreiben der Datei {filename}: {e}")

# Beispielverwendung
if __name__ == "__main__":
    css = CSS()
    css.add_rule('.header', {
        'background-color': '#0034FF',
        'color': 'white',
        'padding': '1.5rem',
        'text-align': 'center',
        'font-size': '24px',
        'font-weight': 'bold',
        'display': 'flex',
        'align-items': 'center',
        'justify-content': 'space-between'
    })
    css.save('styles.css')
