import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from tkinter import filedialog, messagebox
import json
from generator import generate_template

def on_generate():
    """Generiert das Template basierend auf den eingegebenen Optionen."""
    template_name = "index"
    menu_type = menu_type_var.get()
    menu_items = int(menu_items_var.get())
    submenu_count = int(submenu_count_var.get())
    menu_names = [menu_name_entry.get() for menu_name_entry in menu_name_entries]
    submenu_names = [[submenu_entry.get() for submenu_entry in submenu_entries[i]] for i in range(menu_items)]

    # Erstellen der Template-Optionen als Dictionary
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
        "footer_font_size": footer_font_size_var.get()
    }

    # Übergabe an die Template-Generierungsfunktion
    generate_template(template_name, options)

def update_menu_entries():
    """Aktualisiert die Menü- und Untermenü-Einträge basierend auf den eingegebenen Werten."""
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

def save_settings():
    """Speichert die aktuellen Einstellungen in einer JSON-Datei."""
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
        "footer_font_size": footer_font_size_var.get()
    }
    
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, 'w') as file:
            json.dump(options, file)
        messagebox.showinfo("Einstellungen gespeichert", "Die Einstellungen wurden erfolgreich gespeichert.")

def load_settings():
    """Lädt die Einstellungen aus einer JSON-Datei und aktualisiert die GUI."""
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, 'r') as file:
            options = json.load(file)

        # Aktualisierung der GUI-Variablen
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

        # Aktualisiert die Menü- und Untermenü-Einträge basierend auf den geladenen Werten
        update_menu_entries()
        messagebox.showinfo("Einstellungen geladen", "Die Einstellungen wurden erfolgreich geladen.")

def choose_color(color_var):
    """Öffnet den Farbwähler und speichert die ausgewählte Farbe."""
    color = colorchooser.askcolor()[1]
    if color:
        color_var.set(color)

def create_left_frame(root):
    """Erstellt den linken Frame für allgemeine Einstellungen."""
    left_frame = tk.Frame(root)
    left_frame.pack(side="left", fill="y", padx=10, pady=10)

    ttk.Label(left_frame, text="Menütyp:").grid(row=0, column=0, pady=5, sticky="w")
    menu_type_dropdown = ttk.OptionMenu(left_frame, menu_type_var, "side", "side")
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

    ttk.Button(left_frame, text="Einstellungen speichern", command=save_settings).grid(row=20, column=0, pady=10)
    ttk.Button(left_frame, text="Einstellungen laden", command=load_settings).grid(row=20, column=1, pady=10)

    return left_frame

def create_right_frame(root):
    """Erstellt den rechten Frame für Menü- und Untermenü-Einstellungen mit Scrollmöglichkeit."""
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

    # Inneres Frame für Inhalt
    global right_inner_frame
    right_inner_frame = ttk.Frame(right_frame)
    right_inner_frame.pack(fill="both", expand=True)

    ttk.Button(right_inner_frame, text="Aktualisiere Menüpunkte", command=update_menu_entries).pack(pady=10)
    ttk.Button(right_inner_frame, text="Template erstellen", command=on_generate).pack(pady=10)

    # Mausrad-Scrollen aktivieren
    canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

    return right_inner_frame

# Hauptfenster erstellen
root = tk.Tk()
root.title("Webseiten Generator mit css json und html5")

# Variablen initialisieren
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

menu_background_color_var = tk.StringVar(value="#0034FF")
menu_text_color_var = tk.StringVar(value="#FFFFFF")
menu_font_family_var = tk.StringVar(value="Arial")
menu_font_size_var = tk.StringVar(value="16")

footer_background_color_var = tk.StringVar(value="#0034FF")
footer_text_color_var = tk.StringVar(value="#FFFFFF")
footer_font_family_var = tk.StringVar(value="Arial")
footer_font_size_var = tk.StringVar(value="16")

# Listen für Menü- und Untermenü-Eingabefelder
menu_name_entries = []
submenu_entries = []

# Frames erstellen
create_left_frame(root)
create_right_frame(root)

# Starte die GUI
root.mainloop()
