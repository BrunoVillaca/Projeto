
import sys
sys.path.append(r'D:\Projeto Atualizado\Projeto\CarChekin')
sys.path.append(r'F:\Desktop\Faculdade\UC\Prog\Projeto\CarChekin')
sys.path.append(r'C:\Users\bruno.villaca\OneDrive - Ânima Educação - Ambiente Administrativo\Área de Trabalho\Projeto\CarChekin')


from modelos.clientes import Cliente


class ClienteDAO():
  conexao = None
  cursor  = None  

  def __init__(self, con, cur):
    self.conexao = con
    self.cursor = cur

  #getAll() quando for chamado, vai pegar todas as pessoas da tabela Pessoa lá no sqlite, criar um objeto para cada uma e retorna uma lista!!!
  def getAll(self):

    
    self.sql = "SELECT * FROM CLIENTES"


    try:
      self.cursor.execute(self.sql)
      resultado = self.cursor.fetchall()
 
      
      #estamos criando uma lista pessoas para guardar objetos do tipo Pessoa
      pessoas = []
      for linha in resultado:
        pessoa = Cliente(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6])
        #estamos adicionando cada um destes objetos Pessoa
        pessoas.append(pessoa)


      return pessoas
    

    except Exception as e:
      return e
      

  def client_data(self, clientecpf):
    
  
    self.sql = f"SELECT * FROM CLIENTES WHERE CPFCNPJ = {clientecpf} "
    

    try:
      self.cursor.execute(self.sql)
      resultado = self.cursor.fetchall()
      for linha in resultado:
        pessoa = Cliente(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6])
      return(pessoa)
     
       
    except Exception as e:
      return e

      
  def insert(self, _cliente):

    
    values = _cliente.to_tuple_sem_codigo()
    self.sql = f"INSERT INTO CLIENTES (TipoCliente, NomeCliente, CPFCNPJ, Endereco, Email, Telefone) VALUES {values}"
    

    try:
      self.cursor.execute(self.sql)
      self.conexao.commit()

        
    except Exception as e:
      return e

  


      
      
  