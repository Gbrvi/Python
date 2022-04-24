import os

audio_ext = ['.mp3', '.wav', '.ogg']
videos_ext = ['.mp4', '.mov', '.avi']
imagens_ext = ['.jpg', '.jpeg', '.png']
documentos_ext = ['.txt', '.log', '.pdf', '.xls']

tupla_extensao = (audio_ext, videos_ext, imagens_ext, documentos_ext)

def pegar_ext(nome):
    index = nome.rfind('.')
    
    return nome[index:]

def organizar(diretorio):
    AUDIOS_DIR =  os.path.join(diretorio, "audios")
    IMAGENS_DIR =  os.path.join(diretorio, "imagens")
    DOCS_DIR =  os.path.join(diretorio, "documentos")
    VIDEOS_DIR =  os.path.join(diretorio, "videos")
    OUTROS_DIR =  os.path.join(diretorio, "outros")

    lista_diretorio = (AUDIOS_DIR, IMAGENS_DIR, DOCS_DIR, VIDEOS_DIR, OUTROS_DIR)

    for dir in lista_diretorio:
        if not os.path.isdir(dir):
            os.mkdir(dir)

    nomes_arquivos = os.listdir(diretorio)
    nova_pasta = ''

    for arquivo in nomes_arquivos:
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            extensao = (str.lower(pegar_ext(arquivo)))
            if extensao in audio_ext:
                nova_pasta = AUDIOS_DIR
            elif extensao in videos_ext:
                nova_pasta = VIDEOS_DIR
            elif extensao in imagens_ext:
                nova_pasta = IMAGENS_DIR
            elif extensao in documentos_ext:
                nova_pasta = DOCS_DIR
            else:
                nova_pasta = OUTROS_DIR
            velho = os.path.join(diretorio, arquivo)
            novo = os.path.join(nova_pasta, arquivo)

            print(velho, '->', novo)
            
            os.rename(velho, novo)

organizar('C:\\Users\\Acer\\Downloads\\')