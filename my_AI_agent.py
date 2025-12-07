from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from openai import OpenAI
from dotenv import load_dotenv
import view
import os

load_dotenv() 

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# client = OpenAI(api_key="sk-xxxxxxxxxxxxxxxxxxxx")

class first_App(App):
    def build(self):
        self.view = view(self)
        return self.view

    def get_joke(self, instance):
        topic = self.input.text
        print("what kind of a joke u want")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role":"system" , "content":"you only respons with jokes you created"},
                {"role": "user", "content": f"tell me a joke about {topic}"}
            ]
        )
        joke = response.choices[0].message.content
        self.output.text = joke

if __name__ == "__main__":
            first_App().run()
    
