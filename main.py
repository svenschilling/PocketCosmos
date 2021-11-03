#           POCKETCOSMOS
import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.lang import Builder

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen



class PocketCosmosFloatLayout(FloatLayout):
    
    def button_pressed(self):
        print("you clicked it")
    pass

class PocketCosmosApp(App):
    def build(self):
        return PocketCosmosFloatLayout()
    

PocketCosmosApp().run()