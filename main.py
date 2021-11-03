#           POCKETCOSMOS
import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.lang import Builder

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

# load that kv file
Builder.load_file('PocketCosmos.kv')

# define screens
class WindowManager(ScreenManager):
    pass

class MainScreen(Screen):
    pass

class PlayScreen(Screen):
    pass

class PlayScreen(Screen):
    pass

class OptionsScreen(Screen):
    pass

class SavegameScreen(Screen):
    pass

class CreditsScreen(Screen):
    pass


class PocketCosmosApp(App):
    def build(self):
        return WindowManager(ScreenManager)
    

PocketCosmosApp().run()