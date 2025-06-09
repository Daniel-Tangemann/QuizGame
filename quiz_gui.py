# quiz_guis.py
import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os
from PIL import Image, ImageTk

# --- quiz_ui ---
def start_quiz(json_path):
    with open(json_path, encoding="utf-8") as f:
        fragen = json.load(f)

    index = 0
    punkte = 0

    window = tk.Tk()
    window.title("Quiz")
    window.geometry("600x400")

    bg_label = tk.Label(window)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    frage_var = tk.StringVar()
    frage_label = tk.Label(window, textvariable=frage_var, font=("Arial", 14), wraplength=500)
    frage_label.pack(pady=20)

    buttons = []
    for _ in range(4):
        b = tk.Button(window, width=50, font=("Arial", 12))
        b.pack(pady=5)
        buttons.append(b)

    def zeige_frage():
        nonlocal index
        if index >= len(fragen):
            messagebox.showinfo("Fertig!", f"Du hast {punkte} von {len(fragen)} Punkten.")
            window.destroy()
            return

        frage = fragen[index]
        frage_var.set(frage["Frage"])

        bg = frage.get("Hintergrundbild")
        if bg and os.path.exists(bg):
            img = Image.open(bg).resize((600, 400))
            bg_img = ImageTk.PhotoImage(img)
            bg_label.config(image=bg_img)
            bg_label.image = bg_img
        else:
            bg_label.config(image="")

        antworten = [frage["Option1"], frage["Option2"], frage["Option3"], frage["Richtig"]]
        import random
        random.shuffle(antworten)

        for b, text in zip(buttons, antworten):
            b.config(text=text, command=lambda t=text: pruefe_antwort(t))

    def pruefe_antwort(auswahl):
        nonlocal index, punkte
        if auswahl == fragen[index]["Richtig"]:
            punkte += 1
        index += 1
        zeige_frage()

    zeige_frage()
    window.mainloop()
