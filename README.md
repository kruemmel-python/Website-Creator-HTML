# CipherCore Website Generator

## Überblick

Dieses Projekt ist ein CipherCore Website Generator, der es Benutzern ermöglicht, maßgeschneiderte HTML-, CSS- und JavaScript-Dateien für eine Website zu erstellen. Das Programm bietet eine grafische Benutzeroberfläche (GUI) zur Konfiguration verschiedener Bereiche der Website, einschließlich Kopfbereich, Seitenmenü, Hauptinhalt und Fußbereich.

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

- **Kopfbereich**: Konfiguration von Hintergrundfarbe, Textfarbe, Schriftart, Schriftgröße und Textausrichtung. Vor dem Übernehmen der Änderungen kann eine Vorschau in einem Webview-Fenster angezeigt werden.
- **Seitenmenü**: Konfiguration von Hintergrundfarbe, Textfarbe, Schriftart, Schriftgröße und Textausrichtung. Vor dem Übernehmen der Änderungen kann eine Vorschau in einem Webview-Fenster angezeigt werden.
- **Hauptinhalt**: Konfiguration von Hintergrundfarbe, Textfarbe, Schriftart, Schriftgröße und Textausrichtung. Vor dem Übernehmen der Änderungen kann eine Vorschau in einem Webview-Fenster angezeigt werden.
- **Fußbereich**: Konfiguration von Hintergrundfarbe, Textfarbe, Schriftart, Schriftgröße und Textausrichtung. Vor dem Übernehmen der Änderungen kann eine Vorschau in einem Webview-Fenster angezeigt werden.
- **Einstellungen speichern und laden**: Speichern und Laden der Konfigurationseinstellungen in einer JSON-Datei. Dies sorgt dafür, dass eigene Templates gespeichert und später wieder geladen werden können.
- **Template-Generierung**: Erstellung eines vollständigen Templates mit HTML-, CSS- und JavaScript-Dateien basierend auf den Benutzereingaben.

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

![image](https://github.com/user-attachments/assets/6e38acd7-ef32-4e46-baf2-095a73bc9652)

![image](https://github.com/user-attachments/assets/f48e0d03-5fed-47b9-a657-ce32157e07a9)

![image](https://github.com/user-attachments/assets/da07ea1c-b0d7-4bbe-953d-56aafd1ad1cd)




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

## Kontakt

Für Fragen oder Anregungen kontaktieren Sie bitte [Ihren Namen](mailto:ihre-email@example.com).

---
