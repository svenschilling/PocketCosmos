import kivy
kivy.require('2.0.0')
from kivy.app import App

from kivy.core.window import WindowBase, Window

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

from kivy.animation import Animation



class AnimationFloatLayout(FloatLayout):
    
    def button_pressed(self):
        print("you clicked it")
    
    def animate_it(self, widget, *args):
        animate = Animation(
            background_color=()


        )


    
class AnimationApp(App):
    def build(self):
        return AnimationFloatLayout()
    

AnimationApp().run()