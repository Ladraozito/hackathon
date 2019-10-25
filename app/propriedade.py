from kivy.uix.screenmanager import Screen


class PropriedadeApp(Screen):
    def limpar(self):
        self.ids['endereco'].text = ''
        self.ids['tamanhoFazenda'].text = ''
        self.ids['tamanhoDagua'].text = ''
        self.ids['QtdTanques'].text = ''
