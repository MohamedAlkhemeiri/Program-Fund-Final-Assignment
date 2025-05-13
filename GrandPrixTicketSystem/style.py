# style.py

import tkinter as tk

def apply_style(window):
    window.configure(bg="#f5fcff")

def style_label(parent, text, size=12, weight="normal", fg="#333", bg="#f5fcff"):
    return tk.Label(parent, text=text, font=("Helvetica", size, weight), fg=fg, bg=bg)

def style_button(parent, text, command, width=25, bg="#007acc", fg="white"):
    return tk.Button(parent, text=text, command=command, bg=bg, fg=fg, width=width, font=("Helvetica", 11))
