# quiz_gui.py
import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os
from PIL import Image, ImageTk
import random

def start_quiz(json_path):
    with open(json_path, encoding="utf-8") as f:
        fragen = json.load(f)
    random.shuffle(fragen)

    index = 0
    richtig = 0
    falsch = 0

    window = tk.Tk()
    window.title("Quiz")
    window.geometry("600x450")

    bg_label = tk.Label(window)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    frage_var = tk.StringVar()
    frage_label = tk.Label(window, textvariable=frage_var, font=("Arial", 14), wraplength=500)
    frage_label.pack(pady=20)

    counter_frame = tk.Frame(window)
    counter_frame.pack()
    richtig_var = tk.StringVar(value="Richtig: 0")
    falsch_var = tk.StringVar(value="Falsch: 0")
    tk.Label(counter_frame, textvariable=richtig_var, fg="#4CAF50", font=("Arial", 12)).pack(side="left", padx=20)
    tk.Label(counter_frame, textvariable=falsch_var, fg="#F44336", font=("Arial", 12)).pack(side="right", padx=20)

    buttons = []
    for _ in range(4):
        b = tk.Button(window, width=50, font=("Arial", 12))
        b.pack(pady=5)
        buttons.append(b)

    menue_button = tk.Button(window, text="Zurück zum Hauptmenü", font=("Arial", 12), command=lambda: [window.destroy(), __import__("mainmenu").start_main_menu()])

    def reset_buttons():
        for b in buttons:
            b.config(bg="SystemButtonFace", fg="black", state="normal")

    def next_question():
        nonlocal index
        index += 1
        zeige_frage()

    def zeige_frage():
        nonlocal index
        if index >= len(fragen):
            frage_var.set("Fertig! Klicke unten für neues Quiz.")
            for b in buttons:
                b.pack_forget()
            menue_button.pack(pady=20)
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
            def on_click(t=text, btn=b):
                nonlocal richtig, falsch
                for bb in buttons:
                    bb.config(state="disabled")
                if t == frage["Richtig"]:
                    btn.config(bg="#4CAF50", fg="#FFFFFF")
                    richtig += 1
                    richtig_var.set(f"Richtig: {richtig}")
                else:
                    btn.config(bg="#F44336", fg="#FFFFFF")
                    falsch += 1
                    falsch_var.set(f"Falsch: {falsch}")
                    for bb in buttons:
                        if bb["text"] == frage["Richtig"]:
                            bb.config(bg="#4CAF50", fg="#FFFFFF")
                window.after(1000, lambda: [reset_buttons(), next_question()])

            b.config(text=text, command=on_click)

    zeige_frage()
    window.mainloop()
