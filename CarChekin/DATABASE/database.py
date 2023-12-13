# Importar a biblioteca que acessa o SQLite..chama "sqlite3"

import sqlite3

class Database:
    #Atributos
    conexao = None
    cursor = None

    #Método construtor
    def __init__(self):
        self.conexao = sqlite3.connect("CarChekin.db")
        self.cursor = self.conexao.cursor() ; print("Conectando ao Banco de Dados")


    def __del__(self):
        self.conexao.commit()

    def disconnect_bd(self):
        self.conexao.close() ; print("desconectando do Banco de Dados")



    
    



