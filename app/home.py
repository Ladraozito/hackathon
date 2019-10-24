import kivy 
from kivy.uix.dropdown import DropDown
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.label import Label


dropdown = DropDown()
item1 = Button(text='Informações da propriedade', size_hint_y=None, height=44)
dropdown.add_widget(item1)

item2 = Button(text='informar despesas', size_hint_y=None, height=44)
dropdown.add_widget(item2)

item3 = Button(text='Relatorio GERAL', size_hint_y=None, height=44)
dropdown.add_widget(item3)

item4 = Button(text='DEPESAS', size_hint_y=None, height=44)
dropdown.add_widget(item4)

item5 = Button(text='LUCRATIVIDADE', size_hint_y=None, height=44)
dropdown.add_widget(item5)

item6 = Button(text='Informar LUCRO', size_hint_y=None, height=44)
dropdown.add_widget(item6)

mainbutton = Button(text='MENU', size_hint=(0.2, 0.2))


mainbutton.bind(on_release=dropdown.open)


dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))


runTouchApp(mainbutton)

