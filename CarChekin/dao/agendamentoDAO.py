
import sys
sys.path.append(r'F:\Desktop\Faculdade\UC\Prog\Projeto\CarChekin')
sys.path.append(r'C:\Users\bruno.villaca\OneDrive - Ânima Educação - Ambiente Administrativo\Área de Trabalho\Projeto\CarChekin')

from tkinter import messagebox
from modelos.agendamentos import Agendamento


class agendamentoDAO:
  conexao = None
  cursor  = None  


  def __init__(self, con, cur):
    self.conexao = con
    self.cursor = cur


  def getAll(self):


    self.sql = "SELECT * FROM AGENDAMENTOS"


    try:
      self.cursor.execute(self.sql)
      resultado = self.cursor.fetchall()


      agendamentos = []
      for linha in resultado:
        agendamento = Agendamento(linha[0], linha[1], linha[2], linha[3], linha[4])
        #estamos adicionando cada um destes objetos Pessoa
        agendamentos.append(agendamento)

      return agendamentos
         
      
    except Exception as e:
      return e


  def getAlle(self, status):
           
      values = status

      self.sql = f'''

        SELECT 
          AG.AgendamentoID AS 'Id agendamento',
          V.PlacaVeiculo AS 'Placa do veiculo',
          V.ModeloVeiculo AS 'Modelo veiculo',
          AG.DataHora AS 'Data',
          C.NomeCliente AS 'Nome do cliente',
          F.Nome AS 'Nome funcionario'
        FROM 
            AGENDAMENTOS AG
            INNER JOIN VEICULOS V ON AG.VeiculoID = V.VeiculoID
            INNER JOIN CLIENTES C ON V.ClienteID = C.ClienteID
            INNER JOIN FUNCIONARIOS F ON AG.FuncionarioID = F.FuncionarioID
        WHERE
            AG.Status = '{values}' -- Filtra os resultados pelo status 'Agendado'
        ORDER BY
            AG.DataHora; -- Ordena os resultados pela coluna 'DataHora'
      '''


      try:
        self.cursor.execute(self.sql)
        resultado = self.cursor.fetchall()
    

        agendamentos = []
        for agendamento in resultado:
          agendamentos.append(agendamento)
        return agendamentos
          
        
      except Exception as e:
        return e
    

  def verificar_disponibilidade(self, _dataagendamento):


    self.sql = f"SELECT COUNT (*) FROM AGENDAMENTOS WHERE DATE(DataHora) = '{_dataagendamento}'"


    try:


      self.cursor.execute(self.sql)
      quantidade_agendamentos = self.cursor.fetchone()[0]
      print(quantidade_agendamentos)


      if quantidade_agendamentos >= 5:
         
         mensagem = "Não temos agendamento disponiveis nesta Data."
         messagebox.showinfo( "Mensagem", mensagem)
    
        
      elif quantidade_agendamentos <= 5:
            mensagem = "Temos Agendamento disponiveis nessa data."
            messagebox.showinfo("Mensagem", mensagem)

    
    except Exception as e:
      return e


  def insert(self, _agendamento):

    
    values = _agendamento.to_tuple_sem_codigo2()

    self.sql = f"INSERT INTO AGENDAMENTOS (VeiculoID, DataHora, FuncionarioID) VALUES {values}"


    try:
      self.cursor.execute(self.sql)
      self.conexao.commit()


    except Exception as e:
      return e


  def delete(self, delid):

    
    values = delid
    self.sql = f'''DELETE FROM AGENDAMENTOS WHERE AgendamentoID = {values}; '''
    print(self.sql)


    try:
      self.cursor.execute(self.sql)
      self.conexao.commit()


    except Exception as e:
      return e
    

  def alt(self, altid, altstatus):

    
    value1 = altid
    value2 = altstatus

    self.sql = f'''UPDATE AGENDAMENTOS SET Status = '{value2}' WHERE AgendamentoID = {value1};'''
    print(self.sql)


    try:
      self.cursor.execute(self.sql)
      self.conexao.commit()


    except Exception as e:
      return e
    