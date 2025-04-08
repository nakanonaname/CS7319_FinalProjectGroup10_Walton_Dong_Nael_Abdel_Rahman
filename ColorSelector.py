import tkinter as tk
from tkinter import colorchooser

class ColorSelector(tk.Frame):
    def __init__(self, parent, on_done_callback, default_colors=None):
        super().__init__(parent)
        self.parent = parent
        self.on_done_callback = on_done_callback

        self.canvas = tk.Canvas(self, width=500, height=500, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.colors = default_colors or {
            "player1_color": "#ff3333",
            "player2_color": "#3333ff",
            "board_color": "#f0f0f0",
            "background_color": "#000000"
        }

        def choose_color(label, key):
            color = colorchooser.askcolor(title=f"choose {label}")[1]
            if color:
                self.colors[key] = color
                buttons[key].configure(bg=color)

                r, g, b = self.winfo_rgb(color)
                brightness = (r + g + b) / 3
                if brightness < 65535:
                    buttons[key].configure(fg="white")
                else:
                    buttons[key].configure(fg="black")

        y = 80
        buttons = {}

        for label, key in [
            ("player1 color", "player1_color"),
            ("player2 color", "player2_color"),
            ("board color", "board_color"),
            ("background color", "background_color")
        ]:
            btn = tk.Button(self.parent, text=label, bg=self.colors[key],
                            command=lambda l=label, k=key: choose_color(l, k))
            self.canvas.create_window(250, y, window=btn)
            buttons[key] = btn
            y += 50

        start_btn = tk.Button(self.parent, text="Start", font=("Helvetica", 14),
                              command=self.start_game)
        self.canvas.create_window(250, y + 20, window=start_btn)

    def start_game(self):
        self.on_done_callback(self.colors)
