import tkinter as tk
from scene import Scene


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.scene = Scene(master)
        self.bind("<w>", self.scene.handle_move)
        self.bind("<s>", self.scene.handle_move)
        self.bind("<a>", self.scene.handle_move)
        self.bind("<d>", self.scene.handle_move)
        self.bind("<e>", self.scene.handle_move)
        self.bind("<q>", self.scene.handle_move)

        self.bind("<Control-w>", self.scene.handle_turn)
        self.bind("<Control-s>", self.scene.handle_turn)
        self.bind("<Control-a>", self.scene.handle_turn)
        self.bind("<Control-d>", self.scene.handle_turn)
        self.bind("<Control-e>", self.scene.handle_turn)
        self.bind("<Control-q>", self.scene.handle_turn)

        self.bind_all("<MouseWheel>", self.scene.handle_zoom)

        self.bind("<Return>", self.scene.reset)


root = tk.Tk()
app = Application(master=root)
app.focus_set()
app.mainloop()

