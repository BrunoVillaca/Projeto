class Veiculos:
    
    
# Atributos
    __veiculoID = None
    __clienteID = None
    __modeloveiculo = None
    __anoveiculo = None
    __placaveiculo = None
    __chassiveiculo = None
  

  # Método Construtor
    def __init__(self, veiculoid, clienteid, modeloveiculo, anoveiculo, placaveiculo, chassiveiculo):
  

      self.__veiculoID = veiculoid
      self.__clienteID = clienteid
      self.__modeloveiculo = modeloveiculo
      self.__anoveiculo = anoveiculo
      self.__placaveiculo = placaveiculo
      self.__chassiveiculo = chassiveiculo


  # Método __str__: com ele, podemos ver o conteúdo do objeto mais fácil...
    def __str__(self):
        return f"{self.__veiculoID} - {self.__clienteID} - {self.__modeloveiculo} - {self.__anoveiculo} - {self.__placaveiculo} -{self.__chassiveiculo}"
    

    def to_tuple(self):
       
      return (f'{self.__veiculoID}' , f'{self.__clienteID}', f'{self.__modeloveiculo}',f'{self.__anoveiculo}',f'{self.__placaveiculo}',f'{self.__chassiveiculo}')


    def to_tuple_sem_codigo(self):
       
      return (self.__clienteID,f'{self.__modeloveiculo}',f'{self.__anoveiculo}',f'{self.__placaveiculo}',f'{self.__chassiveiculo}')
    

    def to_tuple_sem_codigo2(self):
       
      return (f'{self.__veiculoID}',f'{self.__modeloveiculo}',f'{self.__anoveiculo}',f'{self.__placaveiculo}')