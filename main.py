import json
import os
import tkinter as tk
from tkinter import ttk, colorchooser, filedialog, messagebox
from generator import generate_template
from modules.kopfbereich import open_kopfbereich_gui
from modules.seitenmenue import open_seitenmenue_gui
from modules.hauptinhalt import open_hauptinhalt_gui
from modules.fussbereich import open_fussbereich_gui
from modules.css.hotel_css import generate_hotel_css
from modules.html.hotel_html import generate_hotel_html
from modules.js.hotel_js import generate_hotel_js
from generator import generate_template, generate_submenu_html

# Hilfsfunktionen zur Dateierstellung und zum Schreiben von Inhalten
def create_directory(path):
    os.makedirs(path, exist_ok=True)

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

# Funktion zur Hinzufügung neuer Menüeinträge
def add_menu_entries(menu):
    # Kopfbereich
    kopf_menu = tk.Menu(menu, tearoff=0)
    kopf_menu.add_command(label="Kopfbereich anzeigen", command=lambda: open_kopfbereich_gui(
        header_background_color_var, header_text_color_var, header_font_family_var, header_font_size_var, header_text_align_var
    ))
    menu.add_cascade(label="Kopfbereich", menu=kopf_menu)

    # Seitenmenü
    seitenmenu = tk.Menu(menu, tearoff=0)
    seitenmenu.add_command(label="Seitenmenü anzeigen", command=lambda: open_seitenmenue_gui(
        menu_background_color_var, menu_text_color_var, menu_font_family_var, menu_font_size_var, menu_text_align_var
    ))
    menu.add_cascade(label="Seitenmenü", menu=seitenmenu)

    # Hauptinhalt
    hauptinhalt_menu = tk.Menu(menu, tearoff=0)
    hauptinhalt_menu.add_command(label="Hauptinhalt anzeigen", command=lambda: open_hauptinhalt_gui(
        background_color_var, text_color_var, font_family_var, font_size_var, content_text_align_var
    ))
    menu.add_cascade(label="Hauptinhalt", menu=hauptinhalt_menu)

    # Fußbereich
    fuss_menu = tk.Menu(menu, tearoff=0)
    fuss_menu.add_command(label="Fußbereich anzeigen", command=lambda: open_fussbereich_gui(
        footer_background_color_var, footer_text_color_var, footer_font_family_var, footer_font_size_var, footer_text_align_var
    ))
    menu.add_cascade(label="Fußbereich", menu=fuss_menu)

    # Einstellungen
    settings_menu = tk.Menu(menu, tearoff=0)
    settings_menu.add_command(label="Einstellungen speichern", command=save_settings)
    settings_menu.add_command(label="Einstellungen laden", command=load_settings)
    menu.add_cascade(label="Einstellungen", menu=settings_menu)

# Funktion zur Generierung des Templates mit allen erforderlichen Dateien
def generate_template(template_name, options):
    template_folder = os.path.join("templates", template_name)
    create_directory(template_folder)

    # Generiere CSS
    css_content = generate_hotel_css(options["menu_type"], options)
    css_path = os.path.join(template_folder, f"{template_name}_styles.css")
    write_file(css_path, css_content)

    # Generiere Haupt-HTML-Seite
    html_content = generate_hotel_html(options["menu_type"], options["menu_items"], options["menu_names"], options["submenu_names"])
    html_path = os.path.join(template_folder, f"{template_name}.html")
    write_file(html_path, html_content)

    # Generiere JavaScript
    js_content = generate_hotel_js()
    js_path = os.path.join(template_folder, "animations.js")
    write_file(js_path, js_content)

    # Generiere eine HTML-Seite für jeden Untermenüpunkt
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

# GUI-Logik zum Erstellen des Templates basierend auf Benutzereingaben
def on_generate():
    template_name = "hotel"
    menu_type = menu_type_var.get()
    menu_items = int(menu_items_var.get())
    submenu_count = int(submenu_count_var.get())
    menu_names = [menu_name_entry.get() for menu_name_entry in menu_name_entries]
    submenu_names = [[submenu_entry.get() for submenu_entry in submenu_entries[i]] for i in range(menu_items)]

    options = {
        "menu_type": menu_type,
        "menu_items": menu_items,
        "menu_names": menu_names,
        "submenu_names": submenu_names,
        "background_color": background_color_var.get(),
        "text_color": text_color_var.get(),
        "font_family": font_family_var.get(),
        "font_size": font_size_var.get(),
        "header_background_color": header_background_color_var.get(),
        "header_text_color": header_text_color_var.get(),
        "header_font_family": header_font_family_var.get(),
        "header_font_size": header_font_size_var.get(),
        "menu_background_color": menu_background_color_var.get(),
        "menu_text_color": menu_text_color_var.get(),
        "menu_font_family": menu_font_family_var.get(),
        "menu_font_size": menu_font_size_var.get(),
        "footer_background_color": footer_background_color_var.get(),
        "footer_text_color": footer_text_color_var.get(),
        "footer_font_family": footer_font_family_var.get(),
        "footer_font_size": footer_font_size_var.get(),
        "header_text_align": header_text_align_var.get(),
        "menu_text_align": menu_text_align_var.get(),
        "content_text_align": content_text_align_var.get(),
        "footer_text_align": footer_text_align_var.get()
    }

    generate_template(template_name, options)

# Aktualisiert Menü- und Untermenüeinträge basierend auf Benutzerangaben
def update_menu_entries():
    for widget in menu_name_entries + [entry for sublist in submenu_entries for entry in sublist]:
        widget.destroy()
    menu_name_entries.clear()
    submenu_entries.clear()

    for i in range(int(menu_items_var.get())):
        menu_frame = ttk.LabelFrame(right_inner_frame, text=f"Menüpunkt {i+1}")
        menu_frame.pack(fill="x", pady=5)

        menu_name_label = ttk.Label(menu_frame, text="Name:")
        menu_name_label.grid(row=0, column=0, padx=5, pady=2)
        menu_name_entry = ttk.Entry(menu_frame)
        menu_name_entry.grid(row=0, column=1, padx=5, pady=2)
        menu_name_entries.append(menu_name_entry)

        sub_entries = []
        for j in range(int(submenu_count_var.get())):
            submenu_label = ttk.Label(menu_frame, text=f"Untermenü {j+1} Name:")
            submenu_entry = ttk.Entry(menu_frame)
            submenu_label.grid(row=j+1, column=0, padx=5, pady=2)
            submenu_entry.grid(row=j+1, column=1, padx=5, pady=2)
            sub_entries.append(submenu_entry)

        submenu_entries.append(sub_entries)

# Speichert die aktuellen GUI-Einstellungen in einer JSON-Datei
def save_settings():
    options = {
        "menu_type": menu_type_var.get(),
        "menu_items": menu_items_var.get(),
        "submenu_count": submenu_count_var.get(),
        "background_color": background_color_var.get(),
        "text_color": text_color_var.get(),
        "font_family": font_family_var.get(),
        "font_size": font_size_var.get(),
        "header_background_color": header_background_color_var.get(),
        "header_text_color": header_text_color_var.get(),
        "header_font_family": header_font_family_var.get(),
        "header_font_size": header_font_size_var.get(),
        "menu_background_color": menu_background_color_var.get(),
        "menu_text_color": menu_text_color_var.get(),
        "menu_font_family": menu_font_family_var.get(),
        "menu_font_size": menu_font_size_var.get(),
        "footer_background_color": footer_background_color_var.get(),
        "footer_text_color": footer_text_color_var.get(),
        "footer_font_family": footer_font_family_var.get(),
        "footer_font_size": footer_font_size_var.get(),
        "header_text_align": header_text_align_var.get(),
        "menu_text_align": menu_text_align_var.get(),
        "content_text_align": content_text_align_var.get(),
        "footer_text_align": footer_text_align_var.get()
    }

    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, 'w') as file:
            json.dump(options, file)
        messagebox.showinfo("Einstellungen gespeichert", "Die Einstellungen wurden erfolgreich gespeichert.")

# Lädt die Einstellungen aus einer JSON-Datei und aktualisiert die GUI
def load_settings():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, 'r') as file:
            options = json.load(file)

        menu_type_var.set(options.get("menu_type", "header"))
        menu_items_var.set(options.get("menu_items", "3"))
        submenu_count_var.set(options.get("submenu_count", "2"))
        background_color_var.set(options.get("background_color", "#FFFFFF"))
        text_color_var.set(options.get("text_color", "#000000"))
        font_family_var.set(options.get("font_family", "Arial"))
        font_size_var.set(options.get("font_size", "16"))
        header_background_color_var.set(options.get("header_background_color", "#0034FF"))
        header_text_color_var.set(options.get("header_text_color", "#FFFFFF"))
        header_font_family_var.set(options.get("header_font_family", "Arial"))
        header_font_size_var.set(options.get("header_font_size", "24"))
        menu_background_color_var.set(options.get("menu_background_color", "#0034FF"))
        menu_text_color_var.set(options.get("menu_text_color", "#FFFFFF"))
        menu_font_family_var.set(options.get("menu_font_family", "Arial"))
        menu_font_size_var.set(options.get("menu_font_size", "16"))
        footer_background_color_var.set(options.get("footer_background_color", "#0034FF"))
        footer_text_color_var.set(options.get("footer_text_color", "#FFFFFF"))
        footer_font_family_var.set(options.get("footer_font_family", "Arial"))
        footer_font_size_var.set(options.get("footer_font_size", "16"))
        header_text_align_var.set(options.get("header_text_align", "center"))
        menu_text_align_var.set(options.get("menu_text_align", "left"))
        content_text_align_var.set(options.get("content_text_align", "justify"))
        footer_text_align_var.set(options.get("footer_text_align", "center"))

        update_menu_entries()
        messagebox.showinfo("Einstellungen geladen", "Die Einstellungen wurden erfolgreich geladen.")

# Farbwahl-Funktion
def choose_color(color_var):
    color = colorchooser.askcolor()[1]
    if color:
        color_var.set(color)

# Erstellen des linken Frames für allgemeine Einstellungen
def create_left_frame(root):
    left_frame = tk.Frame(root)
    left_frame.pack(side="left", fill="y", padx=10, pady=10)

    ttk.Label(left_frame, text="Menütyp:").grid(row=0, column=0, pady=5, sticky="w")
    menu_type_dropdown = ttk.OptionMenu(left_frame, menu_type_var, "Seitenmenue", "side")
    menu_type_dropdown.grid(row=0, column=1, pady=5, sticky="w")

    ttk.Label(left_frame, text="Anzahl der Menüpunkte:").grid(row=1, column=0, pady=5, sticky="w")
    ttk.Entry(left_frame, textvariable=menu_items_var).grid(row=1, column=1, pady=5, sticky="w")

    ttk.Label(left_frame, text="Anzahl der Untermenüs pro Menüpunkt:").grid(row=2, column=0, pady=5, sticky="w")
    ttk.Entry(left_frame, textvariable=submenu_count_var).grid(row=2, column=1, pady=5, sticky="w")

    color_options = [
        ("Hintergrundfarbe:", background_color_var),
        ("Textfarbe:", text_color_var),
        ("Header Hintergrundfarbe:", header_background_color_var),
        ("Header Textfarbe:", header_text_color_var),
        ("Menü Hintergrundfarbe:", menu_background_color_var),
        ("Menü Textfarbe:", menu_text_color_var),
        ("Footer Hintergrundfarbe:", footer_background_color_var),
        ("Footer Textfarbe:", footer_text_color_var)
    ]
    for row, (label, var) in enumerate(color_options, start=3):
        ttk.Label(left_frame, text=label).grid(row=row, column=0, pady=5, sticky="w")
        ttk.Button(left_frame, text="Farbe auswählen", command=lambda v=var: choose_color(v)).grid(row=row, column=1, pady=5, sticky="w")

    font_options = [
        ("Schriftart:", font_family_var),
        ("Header Schriftart:", header_font_family_var),
        ("Menü Schriftart:", menu_font_family_var),
        ("Footer Schriftart:", footer_font_family_var)
    ]
    for row, (label, var) in enumerate(font_options, start=11):
        ttk.Label(left_frame, text=label).grid(row=row, column=0, pady=5, sticky="w")
        ttk.OptionMenu(left_frame, var, "Arial", "Arial", "Times New Roman", "Courier New").grid(row=row, column=1, pady=5, sticky="w")

    font_size_options = [
        ("Schriftgröße:", font_size_var),
        ("Header Schriftgröße:", header_font_size_var),
        ("Menü Schriftgröße:", menu_font_size_var),
        ("Footer Schriftgröße:", footer_font_size_var)
    ]
    for row, (label, var) in enumerate(font_size_options, start=15):
        ttk.Label(left_frame, text=label).grid(row=row, column=0, pady=5, sticky="w")
        ttk.Entry(left_frame, textvariable=var).grid(row=row, column=1, pady=5, sticky="w")

    # Textausrichtungsoptionen hinzufügen
    align_options = ["left", "center", "right", "justify"]
    ttk.Label(left_frame, text="Header Textausrichtung:").grid(row=19, column=0, pady=5, sticky="w")
    ttk.OptionMenu(left_frame, header_text_align_var, *align_options).grid(row=19, column=1, pady=5, sticky="w")

    ttk.Label(left_frame, text="Menü Textausrichtung:").grid(row=20, column=0, pady=5, sticky="w")
    ttk.OptionMenu(left_frame, menu_text_align_var, *align_options).grid(row=20, column=1, pady=5, sticky="w")

    ttk.Label(left_frame, text="Inhalt Textausrichtung:").grid(row=21, column=0, pady=5, sticky="w")
    ttk.OptionMenu(left_frame, content_text_align_var, *align_options).grid(row=21, column=1, pady=5, sticky="w")

    ttk.Label(left_frame, text="Fußbereich Textausrichtung:").grid(row=22, column=0, pady=5, sticky="w")
    ttk.OptionMenu(left_frame, footer_text_align_var, *align_options).grid(row=22, column=1, pady=5, sticky="w")

    return left_frame

# Erstellen des rechten Frames für Menü- und Untermenü-Einstellungen
def create_right_frame(root):
    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    right_frame = ttk.Frame(canvas)
    right_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=right_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    global right_inner_frame
    right_inner_frame = ttk.Frame(right_frame)
    right_inner_frame.pack(fill="both", expand=True)

    ttk.Button(right_inner_frame, text="Aktualisiere Menüpunkte", command=update_menu_entries).pack(pady=10)
    ttk.Button(right_inner_frame, text="Template erstellen", command=on_generate).pack(pady=10)

    canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

    return right_inner_frame

# Hauptfenster erstellen und Menüleiste konfigurieren
root = tk.Tk()
root.title("Hotel Template Generator")

menu = tk.Menu(root)
root.config(menu=menu)
add_menu_entries(menu)

# Initialisierung der Variablen für die Einstellungen
menu_type_var = tk.StringVar(value="header")
menu_items_var = tk.StringVar(value="3")
submenu_count_var = tk.StringVar(value="2")

background_color_var = tk.StringVar(value="#FFFFFF")
text_color_var = tk.StringVar(value="#000000")
font_family_var = tk.StringVar(value="Arial")
font_size_var = tk.StringVar(value="16")

header_background_color_var = tk.StringVar(value="#0034FF")
header_text_color_var = tk.StringVar(value="#FFFFFF")
header_font_family_var = tk.StringVar(value="Arial")
header_font_size_var = tk.StringVar(value="24")
header_text_align_var = tk.StringVar(value="center")

menu_background_color_var = tk.StringVar(value="#0034FF")
menu_text_color_var = tk.StringVar(value="#FFFFFF")
menu_font_family_var = tk.StringVar(value="Arial")
menu_font_size_var = tk.StringVar(value="16")
menu_text_align_var = tk.StringVar(value="left")

footer_background_color_var = tk.StringVar(value="#0034FF")
footer_text_color_var = tk.StringVar(value="#FFFFFF")
footer_font_family_var = tk.StringVar(value="Arial")
footer_font_size_var = tk.StringVar(value="16")
footer_text_align_var = tk.StringVar(value="center")

content_text_align_var = tk.StringVar(value="justify")

menu_name_entries = []
submenu_entries = []

# Frames erstellen
create_left_frame(root)
create_right_frame(root)

# Starte die GUI
root.mainloop()
