# Closure
def externa(id):
    dic = {'pt': 'Olá', 'pi': 'Ahoy', 'en' : 'Hello'}
    
    def interna(nome):
        print(f'{dic[id]} {nome}')
    return interna  # Precisa ser instanciada  

func = externa('pt')
func('Mari') #Func agora recebe parametros para interna

func_2 = externa('pi')
func_2('Ricardao')