# editor_gui.py
import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os

def start_editor():
    editor = tk.Tk()
    editor.title("Frageneditor")
    editor.geometry("600x550")

    eingaben = {}
    for label in ["Frage", "Option1", "Option2", "Option3", "Richtig", "Hintergrundbild"]:
        tk.Label(editor, text=label).pack()
        eingaben[label] = tk.Entry(editor, width=80)
        eingaben[label].pack()

    fragen_liste = []

    def frage_hinzufuegen():
        frage = {k: v.get() for k, v in eingaben.items()}
        fragen_liste.append(frage)
        for entry in eingaben.values():
            entry.delete(0, tk.END)

    def speichern():
        pfad = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if pfad:
            with open(pfad, "w", encoding="utf-8") as f:
                json.dump(fragen_liste, f, indent=4, ensure_ascii=False)
            messagebox.showinfo("Gespeichert", f"Datei gespeichert unter:\n{pfad}")

    def laden():
        pfad = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if pfad and os.path.exists(pfad):
            try:
                with open(pfad, "r", encoding="utf-8") as f:
                    daten = json.load(f)
                    if isinstance(daten, list):
                        fragen_liste.extend(daten)
                        messagebox.showinfo("Geladen", f"{len(daten)} Fragen geladen.")
                    else:
                        messagebox.showerror("Fehler", "Datei enthält keine gültige Fragenliste.")
            except Exception as e:
                messagebox.showerror("Fehler", f"Konnte Datei nicht laden:\n{e}")

    def zurueck_zum_menue():
        editor.destroy()
        import mainmenu
        mainmenu.start_main_menu()

    tk.Button(editor, text="Frage hinzufügen", command=frage_hinzufuegen).pack(pady=5)
    tk.Button(editor, text="Speichern als JSON", command=speichern).pack(pady=5)
    tk.Button(editor, text="Fragen aus Datei laden", command=laden).pack(pady=5)
    tk.Button(editor, text="Zurück zum Hauptmenü", command=zurueck_zum_menue).pack(pady=10)

    editor.mainloop()
