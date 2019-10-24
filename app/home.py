from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
dropdown = DropDown()
for index in range(10):
    
    btn = Button(text='Value %d' % index, size_hint_y=None, height=44)



    dropdown.add_widget(btn)


mainbutton = Button(text='MENU', size_hint=(0.2, 0.2))


mainbutton.bind(on_release=dropdown.open)


dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

runTouchApp(mainbutton)