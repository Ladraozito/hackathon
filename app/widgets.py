from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.app import App


class Gerenciador(ScreenManager):
    pass


class Login(Screen):
    pass


class Home(Screen):
    def carregar_valoritem(self):
        pass


class Equipamento(Screen):
    def limpar(self):
        self.ids['descricao'].text = ''
        self.ids['valor'].text = ''
        self.ids['TempoUso'].text = ''
        self.ids['vidaUtil'].text = ''

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'home'
            return True

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.voltar)



class Despesas(Screen):
    def limpar(self):
        self.ids['mes'].text = ''
        self.ids['texto'].text = ''
        self.ids['gastoMes'].text = ''

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'home'
            return True

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.voltar)


class Venda(Screen):
    def limpar(self):
        self.ids['descrevaVenda'].text = ''
        self.ids['quantidadeVenda'].text = ''
        self.ids['valorVenda'].text = ''

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'home'
            return True

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.voltar)


class Propriedade(Screen):
    def limpar(self):
        self.ids['endereco'].text = ''
        self.ids['tamanhoFazenda'].text = ''
        self.ids['tamanhoDagua'].text = ''
        self.ids['QtdTanques'].text = ''

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'home'
            return True

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.voltar)

