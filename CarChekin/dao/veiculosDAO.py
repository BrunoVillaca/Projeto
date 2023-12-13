
import sys
sys.path.append(r'F:\Desktop\Faculdade\UC\Prog\Projeto\CarChekin')
sys.path.append(r'C:\Users\bruno.villaca\OneDrive - Ânima Educação - Ambiente Administrativo\Área de Trabalho\Projeto\CarChekin')


from modelos.veiculos import Veiculos


class VeiculosDAO:
  conexao = None
  cursor  = None  


  def __init__(self, con, cur):
    self.conexao = con
    self.cursor = cur


  #getAll() quando for chamado, vai pegar todas as pessoas da tabela Pessoa lá no sqlite, criar um objeto para cada uma e retorna uma lista!!!
  def getAll(self):


    sql = "SELECT * FROM Veiculos"


    try:
      self.cursor.execute(sql)
      resultado = self.cursor.fetchall()

      
      #estamos criando uma lista pessoas para guardar objetos do tipo Pessoa
      veiculos = []
      for linha in resultado:
        veiculo = Veiculos(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5])
        #estamos adicionando cada um destes objetos Pessoa
        veiculos.append(veiculo)
      return veiculos
      
      
    except Exception as e:
      print(e)
      return e
    

  def insert(self, _veiculo):


    values = _veiculo.to_tuple_sem_codigo()
    
    
    self.sql = f"INSERT INTO VEICULOS (ClienteID, ModeloVeiculo, AnoVeiculo, PlacaVeiculo, ChassiVeiculo) VALUES {values}"


    
    try:
      self.cursor.execute(self.sql)
      self.conexao.commit()

        
    except Exception as e:
      return e
    


  def getid(self, placaveiculo):
    
    values = placaveiculo


    self.sql = f"SELECT * FROM VEICULOS WHERE PlacaVeiculo = '{values}' "
    

    try:                    

      self.cursor.execute(self.sql)
      resultado = self.cursor.fetchall()
      for linha in resultado:
        veiculo = Veiculos(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5])
      
      return(veiculo)


    except Exception as e:
      return e     
        
