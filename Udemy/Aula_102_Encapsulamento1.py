# _ -> Protegido (Ainda é possivel acessar)
# __ -> Privado (Não acessado)
# Pode ser utilizado em metodo tbm
# Quando modifica um __o python cria um novo atributo com o mesmo nome, mas não altera o atributo principal
# Para modificar precisa _NomeClasse__nomeatributo
class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    property
    def dados(self):    # Permite acessar o metodo Dados
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Thiago')

# print(bd.__dados) # Não pode acessa. Atributo protegido

# print(bd._BaseDeDados__dados) # Consegue acessar

bd.__dados = 'oi'   #  Quando modifica um __ o python cria um novo atributo com o mesmo nome, mas não altera o atributo principal
print(bd.__dados)   
bd.lista_clientes()