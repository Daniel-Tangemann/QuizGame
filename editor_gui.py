# quiz_guis.py
import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os
from PIL import Image, ImageTk

# --- editor_ui ---
def start_editor():
    editor = tk.Tk()
    editor.title("Frageneditor")
    editor.geometry("600x500")

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

    tk.Button(editor, text="Frage hinzufügen", command=frage_hinzufuegen).pack(pady=10)
    tk.Button(editor, text="Speichern als JSON", command=speichern).pack(pady=10)

    editor.mainloop()
