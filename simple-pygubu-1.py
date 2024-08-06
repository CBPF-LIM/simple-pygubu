import tkinter as tk
import tkinter.ttk as ttk
import pygubu

# Builder
builder = pygubu.Builder()

# Load Layout
builder.add_from_file("layout.ui")

# Load window: same as -> root = tk.Tk()
root = builder.get_object('root')

# Callbacks
def calculate():
    entry = builder.get_object('entry')
    output = builder.get_object('output')

    name = entry.get()
    output.config(text=name)

# Command map
commands = {
  'calculate': calculate
}

# Use command map
builder.connect_callbacks(commands)

# Main loop
root.mainloop()
