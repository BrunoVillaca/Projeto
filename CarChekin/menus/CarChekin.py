import sys
sys.path.append(r'D:\Projeto Atualizado\Projeto\CarChekin')
sys.path.append(r'F:\Desktop\Faculdade\UC\Prog\Projeto\CarChekin')
sys.path.append(r'C:\Users\bruno.villaca\OneDrive - Ânima Educação - Ambiente Administrativo\Área de Trabalho\Projeto\CarChekin')


from tkinter import *
from tkinter import ttk
from funcao import func
from tkinter import messagebox




root = Tk()


class Aplication(func):
    def __init__(self):
        self.root = root
        self.Tela()
        self.Frames() 
        self.Buttons_frame1()
        self.Entrys()
        self.Frame2_list()
        self.Frame1_list()
        root.mainloop()

    def Tela(self):
        self.root.title("CarChekin")
        self.root.configure(background='#84d6f6')
        self.root.geometry("1280x720")
        self.root.resizable(True, True)
        self.root.maxsize(width= 1980, height= 1080)
        self.root.minsize(width= 1024, height= 768)


    def Frames(self):
        self.frame_1 = Frame(self.root, bd= 4, bg= '#65bedd', 
                             highlightbackground='#45a6c5', highlightthickness= 3)
        self.frame_1.place(relx= 0.02 ,  rely= 0.02 , relheight= 0.46, relwidth= 0.96)

        self.frame_2 = Frame(self.root, bd= 4, bg= '#65bedd', 
                             highlightbackground='#45a6c5', highlightthickness= 3)
        self.frame_2.place(relx= 0.02 ,  rely= 0.5 , relheight= 0.46, relwidth= 0.96)


# Criando os Botoes, as Labels e as Entrys da janela.
    def Buttons_frame1(self):

#Botao Buscar.       
        self.bt_buscar = Button(self.frame_1, text= "Buscar" ,command= self.buscar_clientes )
        self.bt_buscar.place(relx= 0.02 ,  rely= 0.1 , relheight= 0.15, relwidth= 0.1)


# Botao Buscar por cpf.
        self.bt_buscar2 = Button(self.frame_1, text= "Buscar por CPF", command= self.buscar_clientesCPF)
        self.bt_buscar2.place(relx= 0.02 ,  rely= 0.3 , relheight= 0.15, relwidth= 0.1)


# Botao Cadastrar Veiculos.
        self.bt_cadastrarveiculo = Button(self.frame_1, text= "Cadastrar Veiculo", command= self.Cadastrar_Veiculos)
        self.bt_cadastrarveiculo.place(relx= 0.15 ,  rely= 0.3 , relheight= 0.15, relwidth= 0.1)


# Botao Cadastrar Cliente.
        self.bt_cadastrarcliente = Button(self.frame_1, text= "Cadastrar Cliente" ,command= self.Cadastrar_Clientes )
        self.bt_cadastrarcliente.place(relx= 0.15 ,  rely= 0.1 , relheight= 0.15, relwidth= 0.1)


# Botao Agendamentos
        self.bt_agendamentos = Button(self.frame_1, text= "Agendamentos", command= self.buscar_agendamentos)
        self.bt_agendamentos.place(relx= 0.28 ,  rely= 0.3 , relheight= 0.15, relwidth= 0.1)


# Botao Agendar Serviços
        self.bt_agendarservico = Button(self.frame_1, text= "Agendar Serviço", command= self.Agendar_Servico)
        self.bt_agendarservico.place(relx= 0.28 ,  rely= 0.5 , relheight= 0.15, relwidth= 0.1)


# Botao Peças.
        self.bt_pecas = Button(self.frame_1, text= "Estoque", command= self.Consultar_Estoque)
        self.bt_pecas.place(relx= 0.02 ,  rely= 0.7 , relheight= 0.15, relwidth= 0.1)


# Botao Limpar dados.
        self.bt_limpar = Button(self.frame_1, text= "Limpar", command = self.limpar_treeview)
        self.bt_limpar.place(relx= 0.28 ,  rely= 0.7 , relheight= 0.15, relwidth= 0.1)


# Botao Funcionarios.
        self.bt_funcionarios = Button(self.frame_1, text= "Funcionarios", command= self.Exibir_Funcionarios)
        self.bt_funcionarios.place(relx= 0.15 ,  rely= 0.7 , relheight= 0.15, relwidth= 0.1)


# Botao Consultar Veiculos.
        self.bt_consultarveiculos = Button(self.frame_1, text= "Consultar Veiculos",  command= self.Consultar_Veiculos)
        self.bt_consultarveiculos.place(relx= 0.15 ,  rely= 0.5 , relheight= 0.15, relwidth= 0.1)


# Labels        
        self.lb_CPF = Label(self.frame_1, text = 'CPF: ', bg= '#65bedd')
        self.lb_CPF.place(relx= 0.0 ,  rely= 0.5)


        self.lb_busca_clientes = Label(self.frame_1, text = 'Busca de Clientes', bg= '#65bedd' )
        self.lb_busca_clientes.place(relx= 0.02 ,  rely= 0.01)

        self.lb_tipo_busca = Label(self.frame_1, text = 'Tipo de Busca:', bg= '#65bedd' )
        self.lb_tipo_busca.place(relx= 0.27 ,  rely= 0.1)

# Botão de Seleção da Opção de Busca do agendamento.
      
      
        self.tips = StringVar(self.frame_1)
        self.tipsv = ("Agendado", "Iniciado", "Concluido")
        self.tips.set ("Selecione")
        self.popupMenu2 = OptionMenu(self.frame_1, self.tips, *self.tipsv)
        self.popupMenu2.place(relx= 0.30 ,  rely= 0.2 )  


# Entrys

    def Entrys(self):
        self.CPF_entry = Entry(self.frame_1)
        self.CPF_entry.place(relx= 0.025 ,  rely= 0.5, relwidth= 0.09)


    def Frame1_list(self):
        
#Insere o nome das Colunas e Inicializa o Treeview
        self.clientlist2 = ttk.Treeview(self.frame_1, height= 3, columns= ("col0", "col1", "col2" ,"col3" ,"col4" ,"col5","col6"))
        self.clientlist2.heading("#0", text= "")
        self.clientlist2.heading("#1", text= "ID")
        self.clientlist2.heading("#2", text= "Placa Veiculo")
        self.clientlist2.heading("#3", text= "Modelo Veiculo")
        self.clientlist2.heading("#4", text= "Data / Hora")
        self.clientlist2.heading("#5", text= "Nome Cliente")
        self.clientlist2.heading("#6", text = "Funcionario")


# Modifica o a largura das colunas.
        self.clientlist2.column("#0", width= 0)
        self.clientlist2.column("#1", width= 35)
        self.clientlist2.column("#2", width= 100)
        self.clientlist2.column("#3", width= 170)
        self.clientlist2.column("#4", width= 120)
        self.clientlist2.column("#5", width= 170)
        self.clientlist2.column("#6", width= 100)

# Indica a posiçao do Treview.
        self.clientlist2.place(relx= 0.4 ,  rely= 0.03 , relheight= 0.9, relwidth= 0.6)


# Coloca a scrollBar da Treeview.

        self.scrollclientlist2 = Scrollbar(self.frame_1, orient='vertical')

        self.clientlist2.configure(yscroll = self.scrollclientlist2.set)

        self.scrollclientlist2.place(relx= 0.98, rely= 0.03, relwidth= 0.02, relheight= 0.9)



    def Frame2_list(self):
        
#Insere o nome das Colunas e Inicializa o Treeview
        self.clientlist = ttk.Treeview(self.frame_2, height= 3, columns= ("col1", "col2" ,"col3" ,"col4" ,"col5" ,"col6", "col7"))
        self.clientlist.heading("#0", text= "")
        self.clientlist.heading("#1", text= "ID")
        self.clientlist.heading("#2", text= "TIPO")
        self.clientlist.heading("#3", text= "NOME")
        self.clientlist.heading("#4", text= "CPFCNPJ")
        self.clientlist.heading("#5", text= "ENDEREÇO")
        self.clientlist.heading("#6", text= "EMAIL")
        self.clientlist.heading("#7", text= "TELEFONE")
# Modifica o a largura das colunas.
        self.clientlist.column("#0", width= 10)
        self.clientlist.column("#1", width= 30)
        self.clientlist.column("#2", width= 30)
        self.clientlist.column("#3", width= 200)
        self.clientlist.column("#4", width= 100)
        self.clientlist.column("#5", width= 200)
        self.clientlist.column("#6", width= 150)
        self.clientlist.column("#7", width= 80)

# Indica a posiçao do Treview.
        self.clientlist.place(relx= 0.0005 ,  rely= 0.1 , relheight= 0.85, relwidth= 0.98)


# Coloca a scrollBar da Treeview.

        self.scrollclientlist = Scrollbar(self.frame_2, orient='vertical')

        self.clientlist.configure(yscroll = self.scrollclientlist.set)

        self.scrollclientlist.place(relx= 0.98, rely= 0.1, relwidth= 0.02, relheight= 0.85)



    def Cadastrar_Clientes(self):
            

            self.root2 = Toplevel()
            self.root2.title("Cadastro de Clientes")
            self.root2.configure(background='#84d6f6')
            self.root2.geometry('800x600')
            self.root2.resizable(False, False)
            self.root2.transient(self.root)
            self.root2.focus_force()
            self.root2.grab_set()

        # Frames da Tela de CLientes:

            self.frame_3 = Frame(self.root2, bd= 4, bg= '#65bedd', 
                             highlightbackground='#45a6c5', highlightthickness= 3)
            self.frame_3.place(relx= 0.02 ,  rely= 0.05 , relheight= 0.90, relwidth= 0.48)

            self.frame_4 = Frame(self.root2, bd= 4, bg= '#65bedd', 
                             highlightbackground='#45a6c5', highlightthickness= 3)
            self.frame_4.place(relx= 0.51 ,  rely= 0.05 , relheight= 0.40, relwidth= 0.48)

        #Labels das entradas dos cadastros dos Clientes no Frame 3.
            
            self.lb_cadastroclientes = Label(self.frame_3, text = 'Cadastro de Cliente:', bg = '#65bedd')
            self.lb_cadastroclientes.place(relx= 0.3 ,  rely= 0.01) 
            
            self.lb_cadastroTipoCliente = Label(self.frame_3, text = 'Tipo Cliente:', bg= '#65bedd')
            self.lb_cadastroTipoCliente.place(relx= 0.01 ,  rely= 0.2)             


            self.lb_cadastroNome = Label(self.frame_3, text = 'Nome:', bg= '#65bedd')
            self.lb_cadastroNome.place(relx= 0.04 ,  rely= 0.3)


            self.lb_cadastroCPFCNPJ = Label(self.frame_3, text = 'CPF/CNPJ:', bg= '#65bedd')
            self.lb_cadastroCPFCNPJ.place(relx= 0.02 ,  rely= 0.4)


            self.lb_cadastroEndereco = Label(self.frame_3, text = 'Endereço:', bg= '#65bedd')
            self.lb_cadastroEndereco.place(relx= 0.02 ,  rely= 0.5) 

            self.lb_cadastroemail = Label(self.frame_3, text = 'Email:', bg= '#65bedd')
            self.lb_cadastroemail.place(relx= 0.03 ,  rely= 0.6) 

            self.lb_cadastrotelefone = Label(self.frame_3, text = 'Telefone:', bg= '#65bedd')
            self.lb_cadastrotelefone.place(relx= 0.02 ,  rely= 0.7)
        


        #entrada de dados dos cadastros dos clientesno frame 3.

            self.entry_tipoCliente = Entry(self.frame_3)
            self.entry_tipoCliente.place(relx= 0.21, rely= 0.2, relwidth= 0.2)
        
            self.entry_cadastro_nome = Entry(self.frame_3)
            self.entry_cadastro_nome.place(relx= 0.21 ,  rely= 0.3, relwidth= 0.6)


            self.entry_cadastroCPFCNPJ = Entry(self.frame_3)
            self.entry_cadastroCPFCNPJ.place(relx= 0.21 ,  rely= 0.4, relwidth= 0.3)

            self.entry_cadastroendereco = Entry(self.frame_3)
            self.entry_cadastroendereco.place(relx= 0.21, rely= 0.5, relwidth= 0.6)
        
            self.entry_cadastroemail = Entry(self.frame_3)
            self.entry_cadastroemail.place(relx= 0.21 ,  rely= 0.6, relwidth= 0.5)


            self.entry_cadastrotelefone = Entry(self.frame_3)
            self.entry_cadastrotelefone.place(relx= 0.21 ,  rely= 0.7, relwidth= 0.4)



        #Botao cadastrar Cliente no frame 3.


            self.bt_cadastrarCliente = Button(self.frame_3, text= "Cadastrar Cliente", command= self.Cadastrar_Cliente)
            self.bt_cadastrarCliente.place(relx= 0.3 ,  rely= 0.8 , relheight= 0.1, relwidth= 0.3)


        # Labels, Botões e entry da funcionalidade de excluir Clientes no Frame 4.

            self.lb_delclientes = Label(self.frame_4, text = 'Deletar Clientes:', bg = '#65bedd')
            self.lb_delclientes.place(relx= 0.3 ,  rely= 0.01) 
            

            self.lb_delclientecpfcnpj = Label(self.frame_4, text = 'CPF/CNPJ:', bg= '#65bedd')
            self.lb_delclientecpfcnpj.place(relx= 0.01 ,  rely= 0.2)             


            self.entry_delcpfcnpj = Entry(self.frame_4)
            self.entry_delcpfcnpj.place(relx= 0.21, rely= 0.2, relwidth= 0.27)


            self.bt_delCliente = Button(self.frame_4, text= "Deletar Cliente")
            self.bt_delCliente.place(relx= 0.3 ,  rely= 0.8 , relheight= 0.1, relwidth= 0.3)



    def Cadastrar_Veiculos(self):
            

            self.root3 = Toplevel()
            self.root3.title("Cadastro de Veiculos")
            self.root3.configure(background='#84d6f6')
            self.root3.geometry('800x600')
            self.root3.resizable(False, False)
            self.root3.transient(self.root)
            self.root3.focus_force()
            self.root3.grab_set()





        # Frames da Tela de Veiculos:

            self.frame_5 = Frame(self.root3, bd= 4, bg= '#65bedd', 
                             highlightbackground='#45a6c5', highlightthickness= 3)
            self.frame_5.place(relx= 0.02 ,  rely= 0.05 , relheight= 0.90, relwidth= 0.48)


            self.frame_6 = Frame(self.root3, bd= 4, bg= '#65bedd', 
                             highlightbackground='#45a6c5', highlightthickness= 3)
            self.frame_6.place(relx= 0.51 ,  rely= 0.05 , relheight= 0.40, relwidth= 0.48)


         #Labels das entradas dos cadastros dos Veiculos.


            self.lb_clienteid = Label(self.frame_5, text = 'Cliente ID:', bg= '#65bedd')
            self.lb_clienteid.place(relx= 0.02 ,  rely= 0.2)


            self.lb_modelo = Label(self.frame_5, text = 'Modelo:', bg= '#65bedd')
            self.lb_modelo.place(relx= 0.02 ,  rely= 0.3)


            self.lb_ano = Label(self.frame_5, text = 'Ano:', bg= '#65bedd')
            self.lb_ano.place(relx= 0.02 ,  rely= 0.4)         



            self.lb_placa = Label(self.frame_5, text = 'Placa:', bg= '#65bedd')
            self.lb_placa.place(relx= 0.02 ,  rely= 0.5) 


            self.lb_chassi= Label(self.frame_5, text = 'Chassi:', bg= '#65bedd')
            self.lb_chassi.place(relx= 0.02 ,  rely= 0.6)


            self.lb_cadastro = Label(self.frame_5, text = 'Cadastro de Veiculos:', bg= '#65bedd')
            self.lb_cadastro.place(relx= 0.3 ,  rely= 0.02)


        #entrada de dados dos cadastros dos Veiculos.

            self.en_clienteid = Entry(self.frame_5)
            self.en_clienteid.place(relx= 0.22, rely= 0.2, relwidth= 0.12)
        
            self.en_modelo = Entry(self.frame_5)
            self.en_modelo.place(relx= 0.22 ,  rely= 0.3, relwidth= 0.5)


            self.en_ano = Entry(self.frame_5)
            self.en_ano.place(relx= 0.22 ,  rely= 0.4, relwidth= 0.18)



            self.en_placa = Entry(self.frame_5)
            self.en_placa.place(relx= 0.22, rely= 0.5, relwidth= 0.25)
        
            self.en_chassi = Entry(self.frame_5)
            self.en_chassi.place(relx= 0.22 ,  rely= 0.6, relwidth= 0.35)



        #Botao cadastrar Veiculo.
            self.bt_cadastrarveiculo2 = Button(self.frame_5, text= "Cadastrar Veiculos" ,command = self.Insert_Veiculo)
            self.bt_cadastrarveiculo2.place(relx= 0.3 ,  rely= 0.8 , relheight= 0.1, relwidth= 0.35)


        # Labels, Botões e entry da funcionalidade de excluir Veiculos no Frame 6.

            self.lb_delveiculos = Label(self.frame_6, text = 'Deletar Veiculos:', bg = '#65bedd')
            self.lb_delveiculos.place(relx= 0.3 ,  rely= 0.01) 
            

            self.lb_delclientecpfcnpj = Label(self.frame_6, text = 'Placa do Veiculo:', bg= '#65bedd')
            self.lb_delclientecpfcnpj.place(relx= 0.01 ,  rely= 0.2)             


            self.entry_delcpfcnpj = Entry(self.frame_6)
            self.entry_delcpfcnpj.place(relx= 0.31, rely= 0.2, relwidth= 0.27)


            self.bt_delCliente = Button(self.frame_6, text= "Deletar Veiculo")
            self.bt_delCliente.place(relx= 0.3 ,  rely= 0.8 , relheight= 0.1, relwidth= 0.3)


    def Agendar_Servico(self):
            

            self.root4 = Toplevel()
            self.root4.title("Agendar/Alterar Serviços")
            self.root4.configure(background='#84d6f6')
            self.root4.geometry('800x600')
            self.root4.resizable(False, False)
            self.root4.transient(self.root)
            self.root4.focus_force()
            self.root4.grab_set()
                     

            self.en_agedamentoplaca = Entry(self.root4)
            self.en_agedamentoplaca.place(relx= 0.66 ,  rely= 0.7, relwidth= 0.2)


            self.bt_verificarro = Button(self.root4, text= "Verificar Cadastro Carro", command= self.encontrar_idveiculo )
            self.bt_verificarro.place(relx= 0.6 ,  rely= 0.55 , relheight= 0.1, relwidth= 0.25)


            self.frame_7 = Frame(self.root4, bd= 4, bg= '#65bedd', 
                             highlightbackground='#45a6c5', highlightthickness= 3)
            self.frame_7.place(relx= 0.02 ,  rely= 0.05 , relheight= 0.75, relwidth= 0.48)


            self.frame_8 = Frame(self.root4, bd= 4, bg= '#65bedd', 
                             highlightbackground='#45a6c5', highlightthickness= 3)
            self.frame_8.place(relx= 0.51 ,  rely= 0.05 , relheight= 0.40, relwidth= 0.48)


        # CLientList para exivbir as dados do carro.

            self.clientlist6 = ttk.Treeview(self.root4, height= 3, columns= ("col0" "col1", "col2" ,"col3" ,"col4"))
            self.clientlist6.heading("#0", text= "")
            self.clientlist6.heading("#1", text= "ID")
            self.clientlist6.heading("#2", text= "MARCA / MODELO")
            self.clientlist6.heading("#3", text= "ANO")
            self.clientlist6.heading("#4", text = "PLACA")


            self.clientlist6.column("#0", width= 0)
            self.clientlist6.column("#1", width= 50)
            self.clientlist6.column("#2", width= 220)
            self.clientlist6.column("#3", width= 100)
            self.clientlist6.column("#4", width= 150)


            self.clientlist6.place(relx= 0.05 ,  rely= 0.85 , relheight= 0.1, relwidth= 0.9) 

        



        #Labels das entradas dos cadastros dos Veiculos.


            self.lb_cadastroveiculos = Label(self.frame_7, text = 'Agendar Serviço', bg= '#65bedd')
            self.lb_cadastroveiculos.place(relx= 0.3 ,  rely= 0.05) 


            self.lb_agendamentodata = Label(self.frame_7, text = 'Data do Agendamento:', bg= '#65bedd')
            self.lb_agendamentodata.place(relx= 0.02 ,  rely= 0.2)


            self.tipvar = StringVar(self.frame_7)
            self.tipv = ("08:00:00", "09:00:00", "10:00:00", "11:00:00", "12:00:00", "13:00:00", "14:00:00")
            self.tipvar.set ("Selecione")
            self.popupMenu = OptionMenu(self.frame_7, self.tipvar, *self.tipv)
            self.popupMenu.place(relx= 0.40 ,  rely= 0.3 )             

            
            self.lb_agendamentohora = Label(self.frame_7, text = 'Hora do Agendamento:', bg= '#65bedd')
            self.lb_agendamentohora.place(relx= 0.02 ,  rely= 0.3)



            self.lb_agendamentoid = Label(self.frame_7, text = 'ID Carro:', bg= '#65bedd')
            self.lb_agendamentoid.place(relx= 0.02 ,  rely= 0.5)


            self.lb_cadastrofunc = Label(self.frame_7, text = 'Funcionario:', bg= '#65bedd')
            self.lb_cadastrofunc.place(relx= 0.02 ,  rely= 0.6)         


        #entrada de dados dos cadastros dos Veiculos.

            self.en_agendamentodata = Entry(self.frame_7)
            self.en_agendamentodata.place(relx= 0.40, rely= 0.2, relwidth= 0.2)
        

            self.en_agedamentoplaca = Entry(self.root4)
            self.en_agedamentoplaca.place(relx= 0.66 ,  rely= 0.7, relwidth= 0.2)

            self.en_agendamentoid = Entry(self.frame_7)
            self.en_agendamentoid.place(relx= 0.40 ,  rely= 0.5, relwidth= 0.2)


            self.en_agendamentofunc = Entry(self.frame_7)
            self.en_agendamentofunc.place(relx= 0.40 ,  rely= 0.6)


        #Botao cadastrar Veiculo.
            self.bt_cadastraragendamento = Button(self.frame_7, text= "Fazer Agendamento",  command= self.Insert_Agendamento )
            self.bt_cadastraragendamento.place(relx= 0.05 ,  rely= 0.8 , relheight= 0.1, relwidth= 0.35)


            self.bt_verificardata = Button(self.frame_7, text= "Verificar Disponibilidade\n Data", command= self.verificardata)
            self.bt_verificardata.place(relx= 0.5 ,  rely= 0.8 , relheight= 0.1, relwidth= 0.45)


        # Labels, Botões e entry da funcionalidade de excluir Agendamentos no Frame 8.

            self.lb_delveiculos = Label(self.frame_8, text = 'Status do Agendamento', bg = '#65bedd')
            self.lb_delveiculos.place(relx= 0.3 ,  rely= 0.01) 
            

            self.lb_altstatus = Label(self.frame_8, text = 'Status Agendamento:', bg= '#65bedd')
            self.lb_altstatus.place(relx= 0.01 ,  rely= 0.3) 


            self.tips2 = StringVar(self.frame_8)
            self.tipsv2 = ("Iniciado", "Concluido")
            self.tips2.set ("Selecione")
            self.popupMenu3 = OptionMenu(self.frame_8, self.tips2, *self.tipsv2)
            self.popupMenu3.place(relx= 0.35 ,  rely= 0.3 )  


            self.lb_altstatusid = Label(self.frame_8, text = 'ID do Agendamento:', bg= '#65bedd')
            self.lb_altstatusid.place(relx= 0.01 ,  rely= 0.2)             


            self.entry_altstatusid = Entry(self.frame_8)
            self.entry_altstatusid.place(relx= 0.35, rely= 0.2, relwidth= 0.2)


            self.bt_delAgendamento = Button(self.frame_8, text= "Cancelar Agendamento", command= self.del_agendamento)
            self.bt_delAgendamento.place(relx= 0.6 ,  rely= 0.8 , relheight= 0.2, relwidth= 0.37)


            self.bt_altstatus = Button(self.frame_8, text= "Alterar Status\n Agendamento", command= self.alt_agendamento)
            self.bt_altstatus.place(relx= 0.05 ,  rely= 0.8 , relheight= 0.2, relwidth= 0.37)


    def Exibir_Funcionarios(self):
            

            self.root5 = Toplevel()
            self.root5.title("Agendar Serviços")
            self.root5.configure(background='#84d6f6')
            self.root5.geometry('800x600')
            self.root5.resizable(False, False)
            self.root5.transient(self.root)
            self.root5.focus_force()
            self.root5.grab_set()
            

        #Labels das entradas dos cadastros dos Veiculos.


            self.lb_cadastroveiculos = Label(self.root5, text = 'Funcionarios', bg= '#84d6f6')
            self.lb_cadastroveiculos.place(relx= 0.4 ,  rely= 0.05) 


            self.bt_exibirfuncionarios = Button(self.root5, text= "Exibir Funcionarios", command= self.buscar_funcionarios)
            self.bt_exibirfuncionarios.place(relx= 0.4 ,  rely= 0.1 )
           
          
            self.clientlist3 = ttk.Treeview(self.root5, height= 3, columns= ("col0" "col1", "col2" ,"col3" ,"col4" ,"col5" ,"col6"))
            self.clientlist3.heading("#0", text= "")
            self.clientlist3.heading("#1", text= "ID")
            self.clientlist3.heading("#2", text= "Matricula")
            self.clientlist3.heading("#3", text= "NOME")
            self.clientlist3.heading("#4", text= "ENDEREÇO")
            self.clientlist3.heading("#5", text= "EMAIL")
            self.clientlist3.heading("#6", text= "TELEFONE")


# Modifica o a largura das colunas.
            self.clientlist3.column("#0", width= 0)
            self.clientlist3.column("#1", width= 30)
            self.clientlist3.column("#2", width= 30)
            self.clientlist3.column("#3", width= 200)
            self.clientlist3.column("#4", width= 200)
            self.clientlist3.column("#5", width= 150)
            self.clientlist3.column("#6", width= 100)


# Indica a posiçao do Treview.
            self.clientlist3.place(relx= 0.025 ,  rely= 0.2 , relheight= 0.75, relwidth= 0.93)


# Coloca a scrollBar da Treeview.
            self.scrollclientlist3 = Scrollbar(self.root5, orient='vertical')
            self.clientlist3.configure(yscroll = self.scrollclientlist3.set)
            self.scrollclientlist3.place(relx= 0.95, rely= 0.2, relwidth= 0.03, relheight= 0.75)



    def Consultar_Veiculos(self):
            

            self.root6 = Toplevel()
            self.root6.title("Agendar Serviços")
            self.root6.configure(background='#84d6f6')
            self.root6.geometry('800x600')
            self.root6.resizable(False, False)
            self.root6.transient(self.root)
            self.root6.focus_force()
            self.root6.grab_set()
            
        
            self.bt_buscarveiculos = Button(self.root6, text= "Buscar Veiculos", command= self.buscar_veiculos)
            self.bt_buscarveiculos.place(relx= 0.1 ,  rely= 0.1 , relheight= 0.1, relwidth= 0.2)
        #Labels das entradas dos cadastros dos Veiculos.


            self.lb_consultarveiculos = Label(self.root6, text = 'Veiculos', bg= '#84d6f6')
            self.lb_consultarveiculos.place(relx= 0.4 ,  rely= 0.05) 


            self.clientlist4 = ttk.Treeview(self.root6, height= 3, columns= ("col0","col1", "col2" ,"col3" ,"col4" ,"col5" ,"col6"))
            self.clientlist4.heading("#0", text= "")
            self.clientlist4.heading("#1", text= "ID")
            self.clientlist4.heading("#2", text= "CLIENTE")
            self.clientlist4.heading("#3", text= "MODELO")
            self.clientlist4.heading("#4", text= "ANO")
            self.clientlist4.heading("#5", text= "PLACA")
            self.clientlist4.heading("#6", text= "CHASSI")


# Modifica o a largura das colunas.
            self.clientlist4.column("#0", width= 0)
            self.clientlist4.column("#1", width= 30)
            self.clientlist4.column("#2", width= 60)
            self.clientlist4.column("#3", width= 200)
            self.clientlist4.column("#4", width= 150)
            self.clientlist4.column("#5", width= 200)
            self.clientlist4.column("#6", width= 80)


# Indica a posiçao do Treview.
            self.clientlist4.place(relx= 0.025 ,  rely= 0.2 , relheight= 0.75, relwidth= 0.93)


# Coloca a scrollBar da Treeview.
            self.scrollclientlist4 = Scrollbar(self.root6, orient='vertical')
            self.clientlist4.configure(yscroll = self.scrollclientlist4.set)
            self.scrollclientlist4.place(relx= 0.95, rely= 0.2, relwidth= 0.03, relheight= 0.75)



    def Consultar_Estoque(self):
            

            self.root7 = Toplevel()
            self.root7.title("Consultar Estoque")
            self.root7.configure(background='#84d6f6')
            self.root7.geometry('600x400')
            self.root7.resizable(False, False)
            self.root7.transient(self.root)
            self.root7.focus_force()
            self.root7.grab_set()
            
        
            self.bt_buscarestoque = Button(self.root7, text= "Buscar Estoque", command= self.buscar_pecas)
            self.bt_buscarestoque.place(relx= 0.1 ,  rely= 0.1 , relheight= 0.1, relwidth= 0.2)
        #Labels das entradas dos cadastros dos Veiculos.


            self.lb_consultarestoque = Label(self.root7, text = 'Estoque', bg= '#84d6f6')
            self.lb_consultarestoque.place(relx= 0.4 ,  rely= 0.05) 


            self.clientlist5 = ttk.Treeview(self.root7, height= 3, columns= ("col0","col1", "col2" ,"col3" ,"col4"))
            self.clientlist5.heading("#0", text= "")
            self.clientlist5.heading("#1", text= "ID")
            self.clientlist5.heading("#2", text= "Nome da Peça")
            self.clientlist5.heading("#3", text= "Fornecedor")
            self.clientlist5.heading("#4", text= "Quantidade")


# Modifica o a largura das colunas.
            self.clientlist5.column("#0", width= 0)
            self.clientlist5.column("#1", width= 40)
            self.clientlist5.column("#2", width= 250)
            self.clientlist5.column("#3", width= 150)
            self.clientlist5.column("#4", width= 70)


# Indica a posiçao do Treview.
            self.clientlist5.place(relx= 0.025 ,  rely= 0.2 , relheight= 0.75, relwidth= 0.93)


# Coloca a scrollBar da Treeview.
            self.scrollclientlist5 = Scrollbar(self.root7, orient='vertical')
            self.clientlist5.configure(yscroll = self.scrollclientlist5.set)
            self.scrollclientlist5.place(relx= 0.95, rely= 0.2, relwidth= 0.03, relheight= 0.75)



Aplication()