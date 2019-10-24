import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from equipamento import EquipamentoApp
from login import LoginApp
from home import MeuMenuApp

import os.path 
import sqlite3 as lite
from datetime import date 

Builder.load_file('kv_modules/widgets.kv')
sm = ScreenManager()
sm.add_widget(LoginApp(name='login'))
sm.add_widget(MeuMenuApp(name='menu'))
sm.add_widget(EquipamentoApp(name='equipamento'))

if not os.path.exists('./dados.db'):
    conn = lite.connect('dados.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE credencias('
        nome varchar(255) NOT NULL,
        fazenda varchar(255) NOT NULL,
        desc_item varchar(255) NOT NULL,
        valor_item integer NOT NULL,
        tempoUso integer  NOT NULL,
        vidaUtil  NOT NULL,
    )''')


class MainApp(App):

    def build(self):
        return sm

    def login(self, nome, fazenda):
        self.nome = nome
        self.fazenda = fazenda
        with open('dados.txt', 'w', encoding='utf-8') as arquivo:
            string = f'nome,{nome}\n'
            string += f'fazenda,{fazenda}\n'
            arquivo.write(string)
        sm.current = 'menu'
    
    def verificar(self):
        arquivo = open('dados.txt','r',encoding="utf-8")
        dados = arquivo.readlines()
        self.nome = dados[0].split(',')[1]
        self.fazenda = dados[1].split(',')[1]
        arquivo.close()
    def telaEquipamento(self):
        sm.current = 'equipamento'
    def telaDespesa(self):
        sm.current = 'despesas'


    def guardaDados(self,descricaoitem,valoritem,tempoUsoitem,vidaUtilItem):
        if not valoritem:
            valoritem = 0.0
        else:
            valoritem = valoritem.replace(",", ".")
            valoritem = float(valoritem)
        
        if not vidaUtilItem:
            vidaUtilItem = 0.0
        else:
            vidaUtilItem = float(vidaUtilItem)

        if not tempoUsoitem:
            tempoUsoitem = 0.0
        else:
            tempoUsoitem = float(tempoUsoitem)
        
        if not vidaUtilItem:
            perdaAnual = 0
        else:
            perdaAnual = valoritem/vidaUtilItem
        
        self.valoratualItem = (tempoUsoitem*perdaAnual-valoritem)

    def voltamenu(self):
        sm.current = 'menu'

        

if __name__ == "__main__":
    sm.current = 'login'
    MainApp().run()
