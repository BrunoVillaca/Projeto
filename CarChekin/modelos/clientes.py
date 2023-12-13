class Cliente:


  # Atributos
    __Cliente_ID = None
    __TipoCliente = None
    __NomeCliente = None
    __CPFCNPJ = None
    __Endereco = None
    __Email = None
    __Telefone = None  


  # Método Construtor
    def __init__(self, Cliente_ID, TipoCliente,NomeCliente,CPFCNPJ, Endereco, Email,Telefone ):
       
       self.__Cliente_ID = Cliente_ID
       self.__TipoCliente = TipoCliente
       self.__NomeCliente = NomeCliente
       self.__CPFCNPJ  = CPFCNPJ
       self.__Endereco = Endereco
       self.__Email = Email
       self.__Telefone = Telefone



  # Método __str__: com ele, podemos ver o conteúdo do objeto mais fácil...
    def __str__(self):

      return f"{self.__Cliente_ID} - {self.__TipoCliente} - {self.__NomeCliente} - {self.__CPFCNPJ} - {self.__Endereco}' - {self.__Email} - {self.__Telefone}"
      #return (f'{self.__Cliente_ID}' , f'{self.__nome}', f'{self.__cpf}',f'{self.__endereco}',f'{self.__email}',f'{self.__telefone}',f'{self.__tipoCliente}')
    
    def to_tuple(self):
       
      return (f'{self.__Cliente_ID}' , f'{self.__TipoCliente}', f'{self.__NomeCliente}',f'{self.__CPFCNPJ}',f'{self.__Endereco}',f'{self.__Email}',f'{self.__Telefone}')
       
    def to_tuple_sem_codigo(self):
       
      return (f'{self.__TipoCliente}', f'{self.__NomeCliente}',f'{self.__CPFCNPJ}',f'{self.__Endereco}',f'{self.__Email}',f'{self.__Telefone}')
       
  

