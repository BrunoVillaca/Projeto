class Estoque:
    
# Atributos
    __pecaID = None
    __nomepeca = None
    __fornecedor = None
    __quantidade = None

  



  # Método Construtor
    def __init__(self, pecaid, nomepeca, fornecedor, quantidade):
  
      self.__pecaID = pecaid
      self.__nomepeca = nomepeca
      self.__fornecedor = fornecedor
      self.__quantidade = quantidade




  # Método __str__: com ele, podemos ver o conteúdo do objeto mais fácil...
    def __str__(self):
        return f"{self.__pecaID} - {self.__nomepeca} - {self.__fornecedor} - {self.__quantidade}"
    
    def to_tuple(self):
       
      return (f'{self.__pecaID}' , f'{self.__nomepeca}', f'{self.__fornecedor}',f'{self.__quantidade}')
       
    def to_tuple_sem_codigo(self):
       
      return (f'{self.__nomepeca}', f'{self.__fornecedor}',f'{self.__quantidade}')