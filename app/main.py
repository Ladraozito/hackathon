from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix import button
from kivy.uix.screenmanager import Screen


class LoginApp(Screen):
    def login(self, nome, fazenda):
        self.nome = nome
        self.fazenda = fazenda
