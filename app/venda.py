from kivy.uix.screenmanager import Screen


class VendaApp(Screen):
    def limpar(self):
        self.ids['descrevaVenda'].text = ''
        self.ids['quantidadeVenda'].text = ''
        self.ids['valorVenda'].text = ''
