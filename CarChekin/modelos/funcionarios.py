class Funcionario:


  # Atributos
    __funcionarioID = None
    __matriculaID = None
    __nome = None
    __endereco = None
    __email = None
    __telefone = None


  # Método Construtor
    def __init__(self, id, matricula, nome, endereco, email, telefone):
        self.__funcionarioID = id
        self.__matriculaID  = matricula
        self.__nome = nome
        self.__endereco = endereco
        self.__email = email
        self.__telefone = telefone
 

  # Método __str__: com ele, podemos ver o conteúdo do objeto mais fácil...
    def __str__(self):
        return f"{self.__funcionarioID} - {self.__matriculaID} - {self.__nome} - {self.__endereco} - {self.__email} -{self.__telefone}"


    def to_tuple(self):
       
      return (f'{self.__funcionarioID}' , f'{self.__matriculaID}', f'{self.__nome}',f'{self.__endereco}',f'{self.__email}',f'{self.__telefone}')