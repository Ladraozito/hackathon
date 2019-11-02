from kivy.uix.screenmanager import ScreenManager, Screen


class EquipamentoApp(Screen):
    def limpar(self):
        self.ids['descricao'].text = ''
        self.ids['valor'].text = ''
        self.ids['TempoUso'].text = ''
        self.ids['vidaUtil'].text = ''
