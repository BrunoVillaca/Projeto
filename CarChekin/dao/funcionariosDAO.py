
import sys
sys.path.append(r'F:\Desktop\Faculdade\UC\Prog\Projeto\CarChekin')
sys.path.append(r'C:\Users\bruno.villaca\OneDrive - Ânima Educação - Ambiente Administrativo\Área de Trabalho\Projeto\CarChekin')

from modelos.funcionarios import Funcionario



class FuncionariosDAO():
  conexao = None
  cursor  = None  

  def __init__(self, con, cur):
    self.conexao = con
    self.cursor = cur

  #getAll() quando for chamado, vai pegar todas as pessoas da tabela Pessoa lá no sqlite, criar um objeto para cada uma e retorna uma lista!!!
  def getAll(self):
    sql = "SELECT * FROM FUNCIONARIOS"

    try:
      self.cursor.execute(sql)
      resultado = self.cursor.fetchall()

      # print('2')
      # print(resultado)
      
      #estamos criando uma lista pessoas para guardar objetos do tipo Pessoa
      funcionarios = []
      for linha in resultado:
        funcionario = Funcionario(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5])
      
        #estamos adicionando cada um destes objetos Pessoa
        funcionarios.append(funcionario)
      return funcionarios
      




      
      
    except Exception as e:
      return e