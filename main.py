import tkinter as tk
import ffmpeg
from tkinter.filedialog import askopenfilename, asksaveasfilename

filepath = ""

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

    ffmpeg.input(filepath).output(converted_filepath).run()

    label_save['text'] = f"Saved to {converted_filepath}"

window = tk.Tk()
window.title("AudioConverter")

window.rowconfigure(0, minsize=150, weight=1)
window.columnconfigure(1, minsize=400, weight=1)

fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
label_open = tk.Label(fr_buttons, text="No file opened...")
btn_save = tk.Button(fr_buttons, text="Save As...", command=convert_file)
label_save = tk.Label(fr_buttons, text="No target location...")

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
label_open.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=2, column=0, sticky="ew", padx=5, pady=10)
label_save.grid(row=3, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")

window.mainloop()
