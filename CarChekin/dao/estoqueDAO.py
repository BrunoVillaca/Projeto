import sys
sys.path.append(r'D:\Projeto Atualizado\Projeto\CarChekin')
sys.path.append(r'F:\Desktop\Faculdade\UC\Prog\Projeto\CarChekin')
sys.path.append(r'C:\Users\bruno.villaca\OneDrive - Ânima Educação - Ambiente Administrativo\Área de Trabalho\Projeto\CarChekin')


from modelos.estoque import Estoque


class EstoqueDAO():
  conexao = None
  cursor  = None  

  def __init__(self, con, cur):
    self.conexao = con
    self.cursor = cur


  def getAll(self):

    
    self.sql = "SELECT * FROM ESTOQUE"


    try:
      self.cursor.execute(self.sql)
      resultado = self.cursor.fetchall()
      
      
      pecas = []
      for linha in resultado:
        peca = Estoque(linha[0], linha[1], linha[2], linha[3])

        pecas.append(peca)
    

      return pecas
    

    except Exception as e:
      return e
      


