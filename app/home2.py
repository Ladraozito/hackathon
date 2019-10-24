import kivy 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
  
arquivo = open('dados.txt','r',encoding="utf-8")
dados = arquivo.readlines()
nome = dados[0].split(',')[1]
fazenda = dados[1].split(',')[1]
print(nome,fazenda)
arquivo.close()

class MeuMenuApp(App):
    def build(self):
        return Builder.load_file('home2.kv')


MeuMenuApp().run()  