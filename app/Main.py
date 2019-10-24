from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix import button

main_widget_kv = """
#:import get_color_from_hex kivy.utils.get_color_from_hex

FloatLayout:
    canvas.before:
        Color:
            rgba: get_color_from_hex('#CDFFCC')
        Rectangle:
            pos: self.pos
            size: self.size
    Image:
        size_hint: .5, .5,
        pos_hint: {"center_x": .5, "center_y": .75}
        source: 'logo.png'
    Label:
        id: msg
        size_hint: .7, .1
        pos_hint: {"center_x": .5, "center_y": .55}
        text:
    GridLayout:
        cols: 1
        spacing: 5
        size_hint: .7, .37
        pos_hint: {"center_x": .5, "center_y": .5}

        Label:
            text: "Nome do proprietario:"
            size_hint_x: .3
            text_size: self.size
            halign: 'left'
            valign: 'middle'
            color: get_color_from_hex('#000000')
        TextInput:
            id: nome
            multiline: False
        Label:
            text: "Nome da fazenda:"
            size_hint_x: .3
            text_size: self.size
            halign: 'left'
            valign: 'middle'
            color: get_color_from_hex('#000000')    
            Label:
        TextInput:
            id: fazenda
            multiline: False
        
        Label:
        Button:
            size_hint: 2., 2.
            text: "REGISTRAR-SE"
            on_release: app.login(nome.text, fazenda.text)
"""


class LoginApp(App):
    def build(self):
        main_widget = Builder.load_string(main_widget_kv)
        return main_widget
    
    def login(self, nome, fazenda):
        self.nome = nome
        self.fazenda = fazenda


LoginApp().run()
