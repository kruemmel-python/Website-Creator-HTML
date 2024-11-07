import tkinter as tk
from tkinter import ttk, colorchooser, messagebox
import webview

def open_fussbereich_gui(footer_bg_var, footer_text_var, footer_font_family_var, footer_font_size_var, footer_text_align_var):
    """Erstellt eine GUI für den Fußbereich mit HTML-Darstellung und anpassbaren Stilen."""
    window = tk.Toplevel()
    window.title("Fußbereich Konfiguration")
    window.geometry("900x700")

    # Linke Seite: Labels und Eingabefelder für Farbe und Schriftstil
    left_frame = ttk.Frame(window, width=250)
    left_frame.pack(side="left", fill="y", padx=10, pady=10)
    
    # Hintergrundfarbe auswählen
    ttk.Label(left_frame, text="Hintergrundfarbe:").pack(anchor="nw")
    bg_color_var = tk.StringVar(value=footer_bg_var.get())
    bg_color_button = ttk.Button(left_frame, text="Farbe wählen", command=lambda: choose_color(bg_color_var))
    bg_color_button.pack(fill="x", pady=5)
    
    # Schriftfarbe auswählen
    ttk.Label(left_frame, text="Schriftfarbe:").pack(anchor="nw")
    text_color_var = tk.StringVar(value=footer_text_var.get())
    text_color_button = ttk.Button(left_frame, text="Farbe wählen", command=lambda: choose_color(text_color_var))
    text_color_button.pack(fill="x", pady=5)

    # Schriftgröße Dropdown-Menü
    ttk.Label(left_frame, text="Schriftgröße:").pack(anchor="nw")
    font_size_var = tk.StringVar(value=footer_font_size_var.get())
    font_size_dropdown = ttk.Combobox(left_frame, textvariable=font_size_var, values=[str(size) for size in range(8, 49, 2)])
    font_size_dropdown.pack(fill="x", pady=5)

    # Schriftart Dropdown-Menü
    ttk.Label(left_frame, text="Schriftart:").pack(anchor="nw")
    font_family_var = tk.StringVar(value=footer_font_family_var.get())
    font_family_dropdown = ttk.Combobox(left_frame, textvariable=font_family_var, values=["Arial", "Courier New", "Helvetica", "Times New Roman", "Verdana"])
    font_family_dropdown.pack(fill="x", pady=5)

    # Textausrichtung Dropdown-Menü
    ttk.Label(left_frame, text="Textausrichtung:").pack(anchor="nw")
    text_align_var = tk.StringVar(value=footer_text_align_var.get())
    text_align_dropdown = ttk.Combobox(left_frame, textvariable=text_align_var, values=["left", "center", "right", "justify"])
    text_align_dropdown.pack(fill="x", pady=5)

    # Rechte Seite: Oberer und unterer Bereich
    right_frame = ttk.Frame(window)
    right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    # Eingabebox für Fußbereich-HTML-Code
    footer_code_label = ttk.Label(right_frame, text="Fußbereich-Code:")
    footer_code_label.pack(anchor="nw")
    footer_code_box = tk.Text(right_frame, height=5)
    footer_code_box.insert("1.0", "<p>&copy; 2023, Mein Unternehmen. Alle Rechte vorbehalten.</p>")
    footer_code_box.pack(fill="x", padx=5, pady=5)

    def choose_color(color_var):
        """Öffnet einen Farbwähler und speichert die ausgewählte Farbe."""
        color = colorchooser.askcolor()[1]
        if color:
            color_var.set(color)

    def open_webview():
        """Öffnet ein Webview-Fenster für eine reine Vorschau des HTML- und CSS-Inhalts."""
        footer_code = footer_code_box.get("1.0", tk.END).strip()
        css = f"""
        <style>
            .footer {{
                background-color: {bg_color_var.get()};
                color: {text_color_var.get()};
                font-family: {font_family_var.get()};
                font-size: {font_size_var.get()}px;
                padding: 1rem;
                text-align: {text_align_var.get()};
            }}
        </style>
        """
        styled_html = f"<html><head>{css}</head><body><div class='footer'>{footer_code}</div></body></html>"
        webview.create_window('Live-Ansicht Fußbereich', html=styled_html, width=600, height=400)
        webview.start()

    def apply_changes():
        """Übernimmt die aktuellen Einstellungen in die Haupt-GUI."""
        footer_bg_var.set(bg_color_var.get())
        footer_text_var.set(text_color_var.get())
        footer_font_family_var.set(font_family_var.get())
        footer_font_size_var.set(font_size_var.get())
        footer_text_align_var.set(text_align_var.get())
        messagebox.showinfo("Übernommen", "Die Änderungen wurden in die Haupt-GUI übernommen.")

    # Button für die vollständige Vorschau in Webview
    full_preview_button = ttk.Button(right_frame, text="Vollständige Vorschau in Webview", command=open_webview)
    full_preview_button.pack(anchor="nw", pady=5)

    # Button zum Übernehmen der Änderungen
    apply_button = ttk.Button(right_frame, text="Übernehmen", command=apply_changes)
    apply_button.pack(anchor="nw", pady=5)

    window.mainloop()
