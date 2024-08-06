import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "layout.ui"

class App:
    def __init__(self, master=None):
        self.builder = pygubu.Builder()

        self.builder.add_resource_path(PROJECT_PATH)
        self.builder.add_from_file(PROJECT_UI)

        self.root = self.builder.get_object('root', master)
        self.builder.connect_callbacks(self)

    def run(self):
        self.root.mainloop()

    def calculate(self):
        entry = self.builder.get_object('entry')
        output = self.builder.get_object('output')

        name = entry.get()
        output.config(text=name)

app = App()
app.run()
