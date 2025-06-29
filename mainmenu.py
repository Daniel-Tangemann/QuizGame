import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os
from PIL import Image, ImageTk
from quiz_gui import start_quiz
from editor_gui import start_editor

# Setze Arbeitsverzeichnis auf Ordner dieser Datei
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# --- hauptmenu ---
def start_main_menu():
    root = tk.Tk()
    root.title("Quizspiel Hauptmenü")
    root.geometry("500x600")

    def open_file():
        filepath = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filepath:
            root.destroy()
            start_quiz(filepath)

    def open_editor():
        root.destroy()
        start_editor()

    tk.Label(root, text="Willkommen zum Quizspiel!", font=("Arial", 16)).pack(pady=40)
    tk.Button(root, text="Quiz starten (JSON wählen)", command=open_file, width=30).pack(pady=10)
    tk.Button(root, text="Frageneditor öffnen", command=open_editor, width=30).pack(pady=10)

    root.mainloop()
