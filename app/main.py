import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from despesas import DespesasApp
from equipamento import EquipamentoApp
from login import LoginApp
from home import MeuMenuApp

import os.path 
import sqlite3 as lite
from datetime import date

class MainApp(App):
    def __init__(self):
        App.__init__(self)
        self.sm = ScreenManager()
        self.sm.add_widget(LoginApp(name='login'))
        self.sm.add_widget(MeuMenuApp(name='menu'))
        self.sm.add_widget(EquipamentoApp(name='equipamento'))
        self.sm.add_widget(DespesasApp(name='telaDespesas'))
        if not os.path.exists('./dados.db'):
            self.conn = lite.connect('./dados.db')
            cursor = self.conn.cursor()
            cursor.execute('''CREATE TABLE cadastroInicio(
                nome varchar(255) NOT NULL,
                fazenda varchar(255) NOT NULL
                )''')
            cursor.execute('''CREATE TABLE equipamento(
                desc_item varchar(255) NOT NULL,
                valor_item integer NOT NULL,
                tempoUso integer  NOT NULL,
                vidaUtil integer NOT NULL
            )''')
        
        self.conn = lite.connect('./dados.db')
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM cadastroInicio")
        dados = cursor.fetchall()
        if len(dados) > 0: 
            self.sm.current = 'menu'
        else:
            self.sm.current = 'login'

    def build(self):
        return self.sm

    def printlog(self, message):
        with open('./log.txt','a') as f: f.write(message+"\n")

    def salvaLogin(self,pnome,pfazenda):
        self.printlog(pnome.text)
        self.printlog(pfazenda.text)
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO cadastroInicio (nome, fazenda) VALUES (?, ?)',(pnome.text, pfazenda.text))
        self.conn.commit()
        self.sm.current = 'menu'

    def login(self, nome, fazenda):
        self.nome = nome
        self.fazenda = fazenda
        with open('dados.txt', 'w', encoding='utf-8') as arquivo:
            string = f'nome,{nome}\n'
            string += f'fazenda,{fazenda}\n'
            arquivo.write(string)
        self.sm.current = 'menu'
    
    def verificar(self):
        arquivo = open('dados.txt','r',encoding="utf-8")
        dados = arquivo.readlines()
        self.nome = dados[0].split(',')[1]
        self.fazenda = dados[1].split(',')[1]
        arquivo.close()

    def telaEquipamento(self):
        self.sm.current = 'equipamento'
    def telaDespesas(self):
        self.sm.current = 'Despesas'
     

    
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
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO equipamento (desc_item,valor_item,tempoUso,vidaUtil)
            VALUES(?, ?, ?, ?)''',(descricaoitem,valoritem,tempoUsoitem,vidaUtilItem))               
    def voltamenu(self):
        self.sm.current = 'menu'


if __name__ == "__main__":
    Builder.load_file('kv_modules/widgets.kv')
    MainApp().run()
