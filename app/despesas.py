from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class DespesasApp(Screen):
    def limpar(self):
        self.ids['mes'].text = ''
        self.ids['texto'].text = ''
        self.ids['gastoMes'].text = ''
