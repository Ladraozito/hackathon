from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix import button

main_widget_kv = """
#:import get_color_from_hex kivy.utils.get_color_from_hex

FloatLayout:
    canvas.before: 
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'background.jpg'

    Image:
        size_hint: .3, .2,
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
            font_name: 'Roboto-BoldItalic'
            size_hint_x: .6
            text_size: self.size
            halign: 'left'
            valign: 'middle'
            color: get_color_from_hex('#FFFFFF')
            bold: True
        TextInput:
            id: nome
            multiline: False
        Label:
            text: "Nome da fazenda:"
            font_name: 'Roboto-BoldItalic'
            size_hint_x: .6
            text_size: self.size
            halign: 'left'
            valign: 'middle'
            color: get_color_from_hex('#FFFFFF')
            bold: True    
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
