from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


from main import LoginApp
class EquipamentoApp(Screen):
    def build(self):    
        return Builder.load_file('equipamento.kv')
