from time import sleep
class Pessoa:
    def __init__(self, nome, idade, andando=False, falando=False, passos=0):
        self.nome = nome
        self.idade = idade
        self.andando = andando
        self.falando = falando
        self.passos = passos

    def falar(self, assunto=None):
        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def andar(self, local=None):
        print(f'{self.nome} está andando')
        self.andando = True
        self.passos += 1

        if self.passos == 5:
            print(f'{self.nome} chegou ao destino')
            self.andando = False

    def parado(self):
        if not self.andando:
            print('Sim')
        else:
            print('Não')

    def correr(self):
        while True:
            km = int(input('Quantos metros deseja percorrer? [5/10] '))
            if km == 5 or km == 10:
                break
            else:
                print('Apenas 5 ou 10 KM')
        print(f'Correndo {km} km...')
        sleep(km)
        print('....')
        print('Parabéns! Você correu', km, 'km!')        
        
p1 = Pessoa('Igor', 20)
p1.correr()

