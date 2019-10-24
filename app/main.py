from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix import button
from kivy.uix.screenmanager import Screen


class LoginApp(App):
    def build(self):
        return Builder.load_file('kv_modules/main_widget.kv')

    def login(self, nome, fazenda):
        self.nome = nome
        self.fazenda = fazenda

if __name__ == "__main__":
    LoginApp().run()
