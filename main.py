from kivy.app import App 
from kivy.uix.button import Button
class SimplApp(App):
    def build(self):
        return Button(text="PUT ME")



if __name__=='__main__':
    SimplApp().run()       