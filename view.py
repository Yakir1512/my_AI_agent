from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
BoxLayout
class view (BoxLayout):
    def __init__(self, controller, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=10, **kwargs)
        
        self.input = TextInput(hint_text="Enter a joke topic")
        self.output = Label(text="Your joke will appear here")

        btn = Button(text="Get Joke")
        btn.bind(on_press=self.get_joke)

        self.layout.add_widget(self.input)
        self.layout.add_widget(btn)
        self.layout.add_widget(self.output)
        return self.layout
