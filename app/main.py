import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

import os.path
import sqlite3 as lite
from datetime import date

from widgets import *


class Main(App):
    def build(self):
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
                vidaUtil integer NOT NULL,
                 valorItemAtual integer NOT NULL
            )''')
            cursor.execute('''CREATE TABLE despesas(
                dia_despesa date NOT NULL,
                desc_despesa varchar(255) NOT NULL,
                valor_despesa float NOT NULL,
                despesa_totalGASTO float NOT NULL
            )''')
            cursor.execute('''CREATE TABLE venda(
                item_vendido varchar(255) NOT NULL,
                quantidade_item integer NOT NULL,
                preco_item float NOT NULL
            ) ''')
            cursor.execute('''CREATE TABLE propriedade (
                endereco varchar(255)NOT NULL ,
                tamanhoFaz float NOT NULL,
                tamanhoLaminaDagua floatNOT NULL,
                qtdTanques integer NOT NULL
            )''')
        self.conn = lite.connect('./dados.db')
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM cadastroInicio")
        dados = cursor.fetchall()
        gerenciador = Gerenciador()
        if len(dados) > 0:
            gerenciador.current = 'home'
        else:
            gerenciador.current = 'login'
        return gerenciador

    def printlog(self, message):
        with open('./log.txt', 'a') as f: f.write(message + "\n")

    def salvaLogin(self, pnome, pfazenda):
        self.printlog(pnome.text)
        self.printlog(pfazenda.text)
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO cadastroInicio (nome, fazenda) VALUES (?, ?)', (pnome.text, pfazenda.text))
        self.conn.commit()

    def login(self, nome, fazenda):
        self.nome = nome
        self.fazenda = fazenda
        with open('dados.txt', 'w', encoding='utf-8') as arquivo:
            string = f'nome,{nome}\n'
            string += f'fazenda,{fazenda}\n'
            arquivo.write(string)
        self.sm.current = 'menu'

    def verificar(self):
        arquivo = open('dados.txt', 'r', encoding="utf-8")
        dados = arquivo.readlines()
        self.nome = dados[0].split(',')[1]
        self.fazenda = dados[1].split(',')[1]
        arquivo.close()

    def guardaDados(self, descricaoitem, valoritem, tempoUsoitem, vidaUtilItem):
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
            perdaAnual = valoritem / vidaUtilItem
        valorItemAtual = valoritem -(tempoUsoitem * perdaAnual)

        self.valoratualItem = (tempoUsoitem * perdaAnual - valoritem)
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO equipamento (desc_item,valor_item,tempoUso,vidaUtil, valorItemAtual)
            VALUES(?, ?, ?, ?, ?)''', (descricaoitem, valoritem, tempoUsoitem, vidaUtilItem, valorItemAtual))
        self.conn.commit()
        cursor = self.conn.cursor()
        cursor.execute("SELECT  valorItemAtual FROM equipamento ")
        valorlidoteste = cursor.fetchall()
        print(valorlidoteste)  # CALCULA VALOR ATUAL DOS EQUIPAMENTOS

    def despesas(self, dia_despesa, desc_despesa, valor_despesa ):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO despesas (dia_despesa, desc_despesa, valor_despesa, despesa_totalGASTO) 
        VALUES (?, ?, ?, 0)''',
        (dia_despesa.text, desc_despesa.text, valor_despesa.text))
        self.conn.commit()
        cursor = self.conn.cursor()
        data_escolhida = '0'
        cursor.execute("SELECT SUM(valor_despesa)  FROM despesas WHERE strftime('%m', dia_despesa ) = ? ",
        (data_escolhida))
        DespesaDoMes= cursor.fetchall()
        print(DespesaDoMes)

    def venda(self, item_vendido, quantidade_item, preco_item):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO venda (item_vendido, quantidade_item, preco_item) VALUES (?, ?, ?)', (item_vendido.text, quantidade_item.text, preco_item.text))
        self.conn.commit()

    def propriedade(self, endereco, tamanhoFaz, tamanhoLaminaDagua, qtdTanques):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO propriedade (endereco, tamanhoFaz ,tamanhoLaminaDagua ,qtdTanques) VALUES (?, ?, ?, ?)', (endereco.text, tamanhoFaz.text ,tamanhoLaminaDagua.text ,qtdTanques.text))
        self.conn.commit()


if __name__ == "__main__":
    Main().run()
