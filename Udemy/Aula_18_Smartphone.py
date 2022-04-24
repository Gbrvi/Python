from Aula_108_eletronico import Eletronico
from Aula_18_Log import LogMixin

class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} NÃO ESTÁ LIGADO'
            print(info)
            self.log_error(info)
            return

        if self._conectado:
            error = f'{self._nome} JÁ ESTÁ CONECTADO'   
            print(error)
            self.log_error(error)
            return         

        info = f'{self._nome} Foi conectado com sucesso'
        print(info)
        self.lof_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} ESTÁ DESLIGADO'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} Foi desligado com sucesso'
        print(info)
        self.lof_info(info)
        self._conectado = False



        
