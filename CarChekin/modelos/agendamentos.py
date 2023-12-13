class Agendamento:


  # Atributos
    __agendamentoID = None
    __veiculoID = None
    __datahora = None
    __funcionarioID = None




  # Método Construtor
    def __init__(self, agendamentoid, veiculoid, datahora, funcionarioid):
        
        self.__agendamentoID  = agendamentoid
        self.__veiculoID = veiculoid
        self.__datahora = datahora
        self.__funcionarioID = funcionarioid


  # Método __str__: com ele, podemos ver o conteúdo do objeto mais fácil...
    def __str__(self):
        return f"{self.__agendamentoID} - {self.__veiculoID} - {self.__datahora}  - {self.__funcionarioID}"
    

    def to_tuple(self):
       
      return (f'{self.__agendamentoID}' , f'{self.__veiculoID}', f'{self.__datahora}',f'{self.__funcionarioID}')
       
    def to_tuple_sem_codigo(self):
       
      return (f'{self.__veiculoID}',f'{self.__datahora}',f'{self.__funcionarioID}')
    
    def to_tuple_sem_codigo2(self):
       
      return (self.__veiculoID,f'{self.__datahora}',f'{self.__funcionarioID}')