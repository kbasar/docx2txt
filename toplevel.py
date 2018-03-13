import tkinter as tk
from tkinter import ttk

class Example(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.pack()
        btn = ttk.Button(self, text = "Press", command = self.openTopLevel)
        btn.pack()

    def openTopLevel(self):
        topLevelWindow = tk.Toplevel(self)
        # Make topLevelWindow remain on top until destroyed, or attribute changes.
        topLevelWindow.attributes('-topmost', 'true')

root = tk.Tk()
main = Example(root)
root.mainloop()