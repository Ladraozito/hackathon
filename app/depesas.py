from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


from main import LoginApp
class despesasApp(Screen):
    def build(self):    
        return Builder.load_file('main_widget.kv')