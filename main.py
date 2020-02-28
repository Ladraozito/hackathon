from kivy.app import App
from mywidgets import *


class Main(App):
    def build(self):
        return Gerenciador()


if __name__ == '__main__':
    Main().run()
