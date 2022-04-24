from termcolor import colored
class TodoList:
    def __init__(self):
        self.__fazeres = []
    
    @property
    def fazeres(self):
        return self.__fazeres

    def adicionar(self, *item):
        self.fazeres.extend(item)

    def mostrar(self):
        if not self.fazeres:
            print('Todas tarefas realizadas!')
            return

        print('------------------------')
        print(colored('\tTAREFAS', 'red'))
        for listar in self.fazeres:
            print(f'-{listar}')
        print('------------------------')

    
    def feito(self, tarefa):
        if tarefa == 'tudo':
            self.fazeres.clear()
            return
        
        if tarefa not in self.fazeres:
            print('Tarefa não encontrada')
            return
        
        self.fazeres.remove(tarefa)
        self.mostrar()


alline = TodoList()
alline.adicionar('Cozinhar', 'Varrer a casa', 'Limpar o fogão')
alline.adicionar('Correr')
alline.feito('Cozinhar')



