# file: pygubu_helpers.py
import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent

class BaseApp:
    def __init__(self, layout, root, master=None):
        self.builder = pygubu.Builder()
        self.builder.add_resource_path(PROJECT_PATH)
        PROJECT_UI = PROJECT_PATH / layout
        self.builder.add_from_file(PROJECT_UI)

        self.root = self.builder.get_object(root, master)
        self.builder.connect_callbacks(self)
      
    def run(self):
        self.root.mainloop()
















