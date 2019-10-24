from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from main import LoginApp
class MainApp(App):
    def build(self):
        return Builder.load_file('equipamento.kv')


MainApp().run()