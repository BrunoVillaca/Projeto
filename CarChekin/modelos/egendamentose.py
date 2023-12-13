class Agendamentoe:


  # Atributos
    __agendamentoID = None
    __placaVeiculo = None
    __modeloVeiculo = None
    __dataHora = None
    __nomeCliente = None
    __nomeFuncionario = None




  # Método Construtor
    def __init__(self, agendamentoid, placaveiculo, modeloveiculo, datahora, nomecliente, nomefuncionario):
        
        self.__agendamentoID  = agendamentoid
        self.__placaVeiculo = placaveiculo
        self.__modeloVeiculo = modeloveiculo
        self.__dataHora = datahora
        self.__nomeCliente = nomecliente
        self.__nomeFuncionario = nomefuncionario


  # Método __str__: com ele, podemos ver o conteúdo do objeto mais fácil...
    def __str__(self):
        return f"{self.__agendamentoID} - {self.__placaVeiculo} - {self.__modeloVeiculo} - {self.__dataHora} - {self.__nomeCliente} - {self.__nomeFuncionario}"
    

    def to_tuple(self):
       
      return (f'{self.__agendamentoID}' , f'{self.__placaVeiculo}', f'{self.__modeloVeiculo}',f'{self.__dataHora}',f'{self.__nomeCliente}',f'{self.__nomeFuncionario}')
       
    def to_tuple_sem_codigo(self):
       
      return (f'{self.__placaVeiculo}',f'{self.__modeloVeiculo}',f'{self.__dataHora}',f'{self.__nomeCliente}',f'{self.__nomeFuncionario}')