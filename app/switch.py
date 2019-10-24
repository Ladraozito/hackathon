from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from main import LoginApp

Builder.load_file('kv_modules/main_widget.kv')
sm = ScreenManager()
sm.add_widget(LoginApp(name='login'))

class MainApp(App):
    def build(self):
        return sm

    def login(self, nome, fazenda):
        self.nome = nome
        self.fazenda = fazenda
        print(nome, fazenda)

if __name__ == "__main__":
    MainApp().run()
