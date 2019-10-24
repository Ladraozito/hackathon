import kivy
import sqlite3 as lite
import os.path 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from equipamento import EquipamentoApp
from main import LoginApp
from home2 import MeuMenuApp
from despesas import despesasApp

Builder.load_file('kv_modules/main_widget.kv')
sm = ScreenManager()
sm.add_widget(LoginApp(name='login'))
sm.add_widget(MeuMenuApp(name='menu'))
sm.add_widget(EquipamentoApp(name='equipamento'))
sm.add_widget(DespesasApp(name='despesas'))

if not os.path.exists('./dados.db'):
    conn = lite.connect('dados.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE credencias('
        nome varchar(255) NOT NULL,
        fazenda varchar(255) NOT NULL
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
        sm.current = 'despesa'


    def guardaDados(self,descricaoitem,valoritem,TempoUsoitem,vidaUtilItem):
        trocaponto = valoritem.replace(",", ".")
        valoritemconvertido = float (trocaponto)
        self.valoratualItem = (TempoUsoitem*(valoritem/vidaUtilItem)-valoritem)

    def voltamenu(self):
        sm.current = 'menu'

        

if __name__ == "__main__":
    sm.current = 'login'
    MainApp().run()
