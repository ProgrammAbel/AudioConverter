import tkinter as tk
from tkinter import ttk
import ffmpeg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os, sys

filepath = ""

try:
    # PyInstaller stores path in _MEIPASS
    base_path = sys._MEIPASS
except AttributeError:
    base_path = os.path.abspath(".")

def open_file():
    global filepath
    filepath = askopenfilename(
                      filetypes=[("Video Files", "*.mp4")]
                      )

    if not filepath:
        return

    label_open['text'] = filepath

def convert_file():
    converted_filepath = asksaveasfilename(
            defaultextension=".mp3",
            filetypes=[("Audio Files", "*.mp3")]
    )

    label_save['text'] = "Conversion in progress..."
    ffmpeg.input(filepath).output(converted_filepath).run(cmd=base_path + '/ffmpeg/ffmpeg.exe')
    label_save['text'] = f"Done! Saved to {converted_filepath}"

def open_help():
    help_dialog = tk.Toplevel()
    help_dialog.wm_title("About")
    label = ttk.Label(
            help_dialog,
            text="AudioConverter v0.1.0\nThis utility was created by Abel Binoop!"
            )
    label.pack(side="top", fill="x", padx=5, pady=10)
    help_button = ttk.Button(help_dialog, text="Okay", command=help_dialog.destroy)
    help_button.pack(pady=5)
    help_dialog.mainloop()

window = tk.Tk()
window.title("AudioConverter")

window.rowconfigure(0, minsize=150, weight=1)
window.columnconfigure(1, minsize=400, weight=1)

menubar = tk.Menu(window)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=open_help)
menubar.add_cascade(label="Help", menu=help_menu)

fr_buttons = tk.Frame(window)
btn_open = ttk.Button(fr_buttons, text="Open", command=open_file)
label_open = ttk.Label(fr_buttons, text="No file opened...")
btn_save = ttk.Button(fr_buttons, text="Save As...", command=convert_file)
label_save = ttk.Label(fr_buttons, text="No target location...")

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
label_open.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=2, column=0, sticky="ew", padx=5, pady=10)
label_save.grid(row=3, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")

window.config(menu=menubar)

window.mainloop()
