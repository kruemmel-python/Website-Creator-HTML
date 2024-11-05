---

# Webseiten Generator mit CSS, JSON und HTML5

Dieses Projekt ist ein GUI-basierter Webseiten-Generator, der es Benutzern ermöglicht, individuelle Webseiten mit CSS-, HTML- und JavaScript-Dateien zu erstellen. Der Generator bietet eine grafische Benutzeroberfläche, über die verschiedene Seitenlayouts konfiguriert und generiert werden können. Die Konfigurationen können in JSON-Dateien gespeichert und wieder geladen werden.

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

- **Seitenvorlagen**: Unterstützung für verschiedene Arten von Seitenvorlagen (Hotel, Business, Immobilien).
- **Menü-Generator**: Erstellen Sie benutzerdefinierte Menüs mit beliebig vielen Untermenüpunkten.
- **Farbanpassung**: Definieren Sie Farben für Hintergrund, Text, Header, Menü und Footer.
- **Schriftart und -größe**: Wählen Sie Schriftarten und Schriftgrößen für verschiedene Bereiche der Seite.
- **JSON-Konfiguration**: Speichern und laden Sie Design-Einstellungen für wiederverwendbare Designs.
- **Automatisierte Generierung**: Erzeugt vollständige HTML-, CSS- und JavaScript-Dateien für das ausgewählte Template.

## Installation

### Voraussetzungen

- Python 3.x

### Installationsschritte

1. Klonen Sie das Repository:
    ```bash
    git clone https://github.com/kruemmel-python/Website-Creator-HTML.git
    ```
   
2. Navigieren Sie in das Projektverzeichnis:
    ```bash
    cd Website-Creator-HTML
    ```

3. Installieren Sie eventuell benötigte Abhängigkeiten:
    ```bash
    pip install -r requirements.txt
    ```

4. Starten Sie die Anwendung:
    ```bash
    python main.py
    ```

![image](https://github.com/user-attachments/assets/8865f1dd-ce44-490d-b204-739b43f89e6c)



![image](https://github.com/user-attachments/assets/c4d9ecab-629b-4612-9c6b-a199ee86eba2)


![image](https://github.com/user-attachments/assets/5111b61d-3475-4d6d-8f2f-8780f2329a17)




## Verwendung

1. Starten Sie das Programm und wählen Sie eine Seitenvorlage aus (`Hotel`, `Business` oder `Real Estate`).
2. Legen Sie die Anzahl der Menüpunkte und Untermenüpunkte fest und konfigurieren Sie die Namen.
3. Passen Sie die Farben, Schriftarten und Schriftgrößen an, um ein individuelles Design zu erstellen.
4. Speichern Sie die Konfiguration oder laden Sie eine vorherige Konfiguration.
5. Generieren Sie das Template, indem Sie auf „Template erstellen“ klicken. Die Dateien werden im `templates`-Ordner gespeichert.

## GUI-Übersicht

Die Benutzeroberfläche bietet folgende Einstellungen:

- **Linke Seite**: Grundlegende Einstellungen für Menütyp, Farben und Schriftarten sowie Schaltflächen zum Speichern und Laden von Konfigurationen.
- **Rechte Seite**: Eingabefelder für die Namen der Menüpunkte und Untermenüs.

## Beispiel für eine generierte Webseite

Die generierten Dateien umfassen HTML, CSS und JavaScript. Hier ist ein Beispiel einer generierten `Hotel`-Vorlage:

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

## Projektstruktur

Die Projektstruktur gliedert sich in verschiedene Module für die Generierung von CSS, HTML und JavaScript-Dateien für die einzelnen Vorlagen:

```
webseiten-generator/
│
├── modules/                   # Module für die verschiedenen Vorlagen
│   ├── css/                   # CSS-Generatoren
│   │   ├── business_css.py
│   │   ├── hotel_css.py
│   │   └── real_estate_css.py
│   │
│   ├── html/                  # HTML-Generatoren
│   │   ├── business_html.py
│   │   ├── hotel_html.py
│   │   └── real_estate_html.py
│   │
│   └── js/                    # JavaScript-Generatoren
│       ├── animations.js      # Gemeinsame JS-Animationen
│       ├── business_js.py
│       └── hotel_js.py
│
├── templates/                 # Generierte Templates
│   ├── business/              # Business-Vorlagen
│   ├── hotel/                 # Hotel-Vorlagen
│   └── real_estate/           # Immobilien-Vorlagen
│
├── css_generator.py           # Modul zur CSS-Generierung
├── generator.py               # Hauptmodul zur Template-Generierung
└── main.py                    # Hauptanwendung mit der GUI
```

### Modulbeschreibung

- **CSS-Module (`css/`)**: Enthält die Dateien zur Generierung der CSS-Stylesheets für verschiedene Seitentypen (`hotel_css.py`, `business_css.py`, etc.).
- **HTML-Module (`html/`)**: Enthält die HTML-Generierungslogik für die unterschiedlichen Templates.
- **JavaScript-Module (`js/`)**: Enthält JavaScript-Module, um interaktive Funktionen und Animationen zu integrieren.

## Häufige Probleme

### JSON-Formatierungsfehler

- Vergewissern Sie sich, dass die `nav.json`-Datei korrekt formatiert ist. Fehlerhafte Formatierungen können dazu führen, dass Menüs nicht geladen werden.

### Ungültige Zeichen in Dateinamen

- Sonderzeichen in den Namen von Menü- oder Untermenüpunkten werden automatisch durch `_` ersetzt, um Probleme beim Dateizugriff zu vermeiden.

### Menü wird nicht angezeigt

- Stellen Sie sicher, dass die `nav.json`-Datei korrekt erstellt wurde und dass die `load_menu.js`-Datei verfügbar ist, um die Menüpunkte dynamisch zu laden.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der [LICENSE](LICENSE)-Datei.

