Danke für die Klärung! Hier ist eine angepasste `README.md`, die deutlich macht, dass der Name des Template-Ordners zwar `hotel` ist, aber die generierte Haupt-HTML-Datei in `index.html` umbenannt werden sollte, falls diese Datei als Startseite verwendet werden soll.

---

# CipherCore Website Generator

## Überblick

Dieses Projekt ist ein **CipherCore Website Generator**, der es Benutzern ermöglicht, maßgeschneiderte HTML-, CSS- und JavaScript-Dateien für eine Website zu erstellen. Das Programm bietet eine grafische Benutzeroberfläche (GUI) zur Konfiguration verschiedener Bereiche der Website, einschließlich Kopfbereich, Seitenmenü, Hauptinhalt und Fußbereich.

## Inhaltsverzeichnis

- [Features](#features)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [GUI-Übersicht](#gui-%C3%BCbersicht)
- [Beispiel für eine generierte Webseite](#beispiel-f%C3%BCr-eine-generierte-webseite)
- [Projektstruktur](#projektstruktur)
- [Häufige Probleme](#h%C3%A4ufige-probleme)
- [Lizenz](#lizenz)

## Features

- **Kopfbereich**: Konfiguration von Hintergrundfarbe, Textfarbe, Schriftart, Schriftgröße und Textausrichtung mit Vorschau im Webview.
- **Seitenmenü, Hauptinhalt und Fußbereich**: Anpassung dieser Bereiche mit Optionen zur Farbe, Schriftart, Ausrichtung und Schriftgröße, ebenfalls mit Vorschauoptionen.
- **Einstellungen speichern und laden**: Speichern und Laden der Konfiguration in einer JSON-Datei, um eigene Templates zu speichern und später wieder zu laden.
- **Automatische Generierung von `nav.json`**: `nav.json` wird basierend auf den Menüeinstellungen erstellt, um die Navigation dynamisch zu steuern.
- **Template-Generierung**: Automatische Erstellung eines vollständigen Templates mit HTML-, CSS- und JavaScript-Dateien.

## Installation

### Voraussetzungen

- Python 3.x

### Installationsschritte

1. Klonen Sie das Repository:
    ```bash
    git clone https://github.com/dein-benutzername/ciphercore-website-generator.git
    ```

2. Navigieren Sie in das Projektverzeichnis:
    ```bash
    cd ciphercore-website-generator
    ```

3. Installieren Sie eventuell benötigte Abhängigkeiten:
    ```bash
    pip install -r requirements.txt
    ```

4. Starten Sie die Anwendung:
    ```bash
    python main.py
    ```

## Verwendung

1. Starten Sie das Programm und konfigurieren Sie die gewünschten Einstellungen für den Kopfbereich, das Seitenmenü, den Hauptinhalt und den Fußbereich.
2. Passen Sie die Farben, Schriftarten und Schriftgrößen an, um ein individuelles Design zu erstellen.
3. Speichern oder laden Sie Konfigurationen über die Schaltflächen im Menü.
4. Klicken Sie auf **Template erstellen**, um das Template zu generieren. Die Dateien werden im `templates/hotel`-Ordner gespeichert.
5. Falls die generierte Hauptdatei als Startseite verwendet werden soll, benennen Sie die Datei `hotel.html` in `index.html` um.

## GUI-Übersicht

Die Benutzeroberfläche bietet folgende Konfigurationsmöglichkeiten:

- **Linke Seite**: Grundlegende Einstellungen für Menütyp, Farben und Schriftarten sowie Schaltflächen zum Speichern und Laden von Konfigurationen.
- **Rechte Seite**: Eingabefelder für die Namen der Menüpunkte und Untermenüs.
  
![Main GUI](https://github.com/user-attachments/assets/6e38acd7-ef32-4e46-baf2-095a73bc9652)
*Die Hauptoberfläche zur Konfiguration der Template-Einstellungen.*

## Beispiel für eine generierte Webseite

Die generierten Dateien umfassen `hotel.html`, `hotel_styles.css`, `animations.js` und `nav.json`. Hier ist ein Beispiel der generierten `Hotel`-Vorlage:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Über mich</title>
    <link rel="stylesheet" href="hotel_styles.css">
    <script src="animations.js"></script>
</head>
<body>

    <header class="header">
        <h1>Über mich</h1>
        <nav class="menu" id="nav">
            <ul></ul>
        </nav>
    </header>
    <main style="padding-top: 80px;">
        <section class="section">
            <h1>Willkommen auf meiner persönlichen Seite</h1>
            <p>Hallo! Mein Name ist [Ihr Name]. Diese Seite bietet einen Einblick in meine Interessen und Projekte.</p>
        </section>
    </main>
    <footer class="footer">
        <p>&copy; 2023 Persönliche Webseite. Alle Rechte vorbehalten.</p>
    </footer>

    <script src="load_menu.js"></script>
</body>
</html>
```

#### Beispielstruktur für `nav.json`

```json
{
  "menuItems": [
    {
      "title": "Home",
      "url": "index.html",
      "subMenu": []
    },
    {
      "title": "Über uns",
      "url": "about.html",
      "subMenu": [
        { "title": "Unsere Geschichte", "url": "history.html" },
        { "title": "Unser Team", "url": "team.html" }
      ]
    }
  ]
}
```

## Projektstruktur

```
ciphercore-website-generator/
│
├── main.py
├── generator.py
├── modules/
│   ├── kopfbereich.py
│   ├── seitenmenue.py
│   ├── hauptinhalt.py
│   ├── fussbereich.py
│   ├── css/
│   │   └── hotel_css.py
│   ├── html/
│   │   └── hotel_html.py
│   └── js/
│       └── hotel_js.py
├── templates/
│   └── hotel/
│       ├── hotel_styles.css
│       ├── hotel.html
│       ├── animations.js
│       ├── nav.json
│       └── ... (weitere Untermenü-HTML-Dateien)
├── requirements.txt
└── README.md
```

## Häufige Probleme

### JSON-Formatierungsfehler

- Stellen Sie sicher, dass `nav.json` korrekt formatiert ist. Fehlerhafte Formatierungen können dazu führen, dass Menüs nicht geladen werden.

### Ungültige Zeichen in Dateinamen

- Sonderzeichen in den Namen von Menü- oder Untermenüpunkten werden automatisch durch `_` ersetzt, um Probleme beim Dateizugriff zu vermeiden.

### Menü wird nicht angezeigt

- Stellen Sie sicher, dass `nav.json` korrekt erstellt wurde und dass `load_menu.js` verfügbar ist, um die Menüpunkte dynamisch zu laden.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der [LICENSE](LICENSE)-Datei.

## Kontakt

Für Fragen oder Anregungen kontaktieren Sie bitte [Ralf Krümmel](mailto:ralf.kruemmel+python.de).

---

In dieser Version wird jetzt klar, dass `hotel.html` im `templates/hotel` Ordner gespeichert wird und manuell in `index.html` umbenannt werden sollte, wenn sie als Startseite dienen soll.
