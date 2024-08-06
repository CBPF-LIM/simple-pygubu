from pygubu_helpers import BaseApp

class App(BaseApp):
    def calculate(self):
        entry = self.builder.get_object('entry')
        output = self.builder.get_object('output')

        name = entry.get()
        output.config(text=name)

app = App('layout.ui', 'root')
app.run()
