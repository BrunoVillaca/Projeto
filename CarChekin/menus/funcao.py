import sys
sys.path.append(r'D:\Projeto Atualizado\Projeto\CarChekin')
sys.path.append(r'F:\Desktop\Faculdade\UC\Prog\Projeto\CarChekin')
sys.path.append(r'C:\Users\bruno.villaca\OneDrive - Ânima Educação - Ambiente Administrativo\Área de Trabalho\Projeto\CarChekin')


from dao.funcionariosDAO import FuncionariosDAO
from dao.clientesDAO import ClienteDAO
from dao.veiculosDAO import VeiculosDAO
from dao.agendamentoDAO import agendamentoDAO
from dao.estoqueDAO import EstoqueDAO

from DATABASE.database import Database

from modelos.clientes import Cliente
from modelos.veiculos import Veiculos
from modelos.agendamentos import Agendamento


from datetime import datetime

from tkinter import messagebox




class func():


    def buscar_clientes(self):

        self.clientlist.delete(*self.clientlist.get_children())


        db = Database()
        pessoaDAo = ClienteDAO(db.conexao, db.cursor)
        pessoas = pessoaDAo.getAll()


        for pessoa in pessoas:
            self.clientlist.insert('', 'end', values = pessoa.to_tuple())


    def buscar_clientesCPF(self):


        self.clientlist.delete(*self.clientlist.get_children())


        clientecpf = self.CPF_entry.get()


        db = Database()
        pessoaDAo = ClienteDAO(db.conexao, db.cursor)
        pessoa = pessoaDAo.client_data(clientecpf)

     
        self.clientlist.insert('', 'end', values = pessoa.to_tuple())
     
    
    def Cadastrar_Cliente(self):

        
        cliente = Cliente(0, self.entry_tipoCliente.get(), self.entry_cadastro_nome.get(), self.entry_cadastroCPFCNPJ.get(), 
                          self.entry_cadastroendereco.get(), self.entry_cadastroemail.get(), self.entry_cadastrotelefone.get())


        db = Database()
        pessoaDAo = ClienteDAO(db.conexao, db.cursor)
        pessoaDAo.insert(cliente)
        

    def buscar_funcionarios(self):

        self.clientlist3.delete(*self.clientlist3.get_children())



        db = Database()
        funcionarioDAo = FuncionariosDAO(db.conexao, db.cursor)
        funcionarios = funcionarioDAo.getAll()


        for funcionario in funcionarios:
            #print(funcionario.to_tuple())
            self.clientlist3.insert('', 'end', values = funcionario.to_tuple())


    def buscar_veiculos(self):


        self.clientlist4.delete(*self.clientlist4.get_children())


        db = Database()
        veiculoDAo = VeiculosDAO(db.conexao, db.cursor)
        veiculos = veiculoDAo.getAll()


        for veiculo in veiculos:
            #print(funcionario.to_tuple())
            self.clientlist4.insert('', 'end', values = veiculo.to_tuple())


    def buscar_pecas(self):


        self.clientlist5.delete(*self.clientlist5.get_children())


        db = Database()
        pecaDAo = EstoqueDAO(db.conexao, db.cursor)
        pecas = pecaDAo.getAll()


        for peca in pecas:
            self.clientlist5.insert('', 'end', values = peca.to_tuple())        


    def Insert_Veiculo(self):


        valor_cliente = self.en_clienteid.get()


        try:
            cliente_inteiro = int(valor_cliente)
            
            veiculo = Veiculos(0, cliente_inteiro, self.en_modelo.get(), self.en_ano.get(), 
                            self.en_placa.get(), self.en_chassi.get())

            db = Database()
            veiculoDAo = VeiculosDAO(db.conexao, db.cursor)
            veiculoDAo.insert(veiculo)
        

        except ValueError:
            mensagem = "Não foi possível converter para inteiro."
            messagebox.showinfo("Erro!!!", mensagem)
        except Exception as e:
            mensagem = f"Erro ao inserir no banco de dados: {str(e)}"
            messagebox.showinfo("Erro!!!", mensagem)


    def buscar_agendamentos(self):

        status = self.tips.get()


        self.clientlist2.delete(*self.clientlist2.get_children())


        db = Database()
        agendamentoDAo = agendamentoDAO(db.conexao, db.cursor)
        agendamentos = agendamentoDAo.getAlle(status)


        for agendamento in agendamentos:
            self.clientlist2.insert('', 'end', values = agendamento)        


    def limpar_treeview(self):
                self.clientlist2.delete(*self.clientlist2.get_children())
                self.clientlist.delete(*self.clientlist.get_children())


    def Insert_Agendamento(self):
      


        data =  self.en_agendamentodata.get()
        datasql = datetime.strptime(data, '%d/%m/%Y').strftime('%Y-%m-%d')
        hora = self.tipvar.get()
        datahora = datasql + ' ' + hora
      
      
        entradaid = self.en_agendamentoid.get()


        try:
          

            cliente_id = int(entradaid)
            
            agendamento = Agendamento(0, cliente_id, datahora, self.en_agendamentofunc.get()) 
            print(agendamento)

            db = Database()
            agendamentoDAo = agendamentoDAO(db.conexao, db.cursor)
            agendamentoDAo.insert(agendamento)


        except Exception as e:
            mensagem = f"Erro ao inserir no banco de dados: {str(e)}"
            messagebox.showinfo("Erro!!!", mensagem)


    def verificardata(self):


        data_inserida = self.en_agendamentodata.get()


        try:


            data = datetime.strptime(data_inserida, '%d/%m/%Y').strftime('%Y-%m-%d')
            data_agendamento = datetime.strptime(data, '%Y-%m-%d')


            if data_agendamento.date() < datetime.now().date():
                print("Erro: Data inserida é anterior à data de hoje.")
                mensagem = "Erro: Data inserida é anterior à data de hoje."
                messagebox.showinfo( "Erro!!!", mensagem)
            else:
                db = Database()
                agendamentoDAo = agendamentoDAO(db.conexao, db.cursor)
                agendamentoDAo.verificar_disponibilidade(data)


        except ValueError:
            print("Erro: Formato de data inválido.")
            mensagem = "Erro: Formato de data inválido."
            messagebox.showinfo( "Erro!!!", mensagem)


    def encontrar_idveiculo(self):
        

        self.clientlist6.delete(*self.clientlist6.get_children())


        placaveiculo = self.en_agedamentoplaca.get()


        db = Database()
        veiculoDAO = VeiculosDAO(db.conexao, db.cursor)
        veiculo = veiculoDAO.getid(placaveiculo)


        self.clientlist6.insert('', 'end', values = veiculo.to_tuple_sem_codigo2())


    def del_agendamento(self):


        delid = self.entry_altstatusid.get()



        try:         

            db = Database()
            agendamentoDAo = agendamentoDAO(db.conexao, db.cursor)
            agendamentoDAo.delete(delid)


        except Exception as e:
            mensagem = f"Erro ao inserir no banco de dados: {str(e)}"
            messagebox.showinfo("Erro!!!", mensagem)


    def alt_agendamento(self):


        altid = self.entry_altstatusid.get()
        altstatus = self.tips2.get()


        try:         

            db = Database()
            agendamentoDAo = agendamentoDAO(db.conexao, db.cursor)
            agendamentoDAo.alt(altid,altstatus)


        except Exception as e:
            mensagem = f"Erro ao inserir no banco de dados: {str(e)}"
            messagebox.showinfo("Erro!!!", mensagem)