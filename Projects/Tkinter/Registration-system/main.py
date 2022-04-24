from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
from tkinter import tix
import sqlite3
from turtle import bgcolor

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

root = tix.Tk()

class Relatorio():
    def print_cliente(self):
        webbrowser.open('cliente.pdf') # Abre o PDF no navegador

    def gera_relat_cliente(self):
        self.c = canvas.Canvas('cliente.pdf')

        self.codigo_rel = self.entry_cod.get()
        self.nome_rel = self.entry_nome.get()
        self.tel_rel = self.entry_tel.get()
        self.cidade_rel = self.entry_cidade.get()

        self.c.setFont("Helvetica-Bold", 24) # Define a fonte
        self.c.drawString(200, 780, 'Ficha do Cliente') # Escreve no PDF 0-600 (x) | 0 - 800 (y)

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(80, 700, 'Código: ')
        self.c.drawString(80, 650, 'Nome: ')
        self.c.drawString(80, 600, 'Telefone: ')
        self.c.drawString(80, 550, 'Cidade: ')

        self.c.setFont('Helvetica', 18)
        self.c.drawString(150, 700, self.codigo_rel)
        self.c.drawString(150, 650, self.nome_rel)
        self.c.drawString(165, 600, self.tel_rel)
        self.c.drawString(150, 550, self.cidade_rel)

        self.c.rect(x=20, y=440, width=560, height=380, fill=False, stroke=True) # X | Y | Tamanho | Grossura da linha | Fill = prencher a linha de preto

        self.c.showPage()
        self.c.save()
        self.print_cliente()

class Funcs():
    # Comando para limpar os usuarios
    def limpa_clientes(self):
        self.entry_cod.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_tel.delete(0, END)
        self.entry_cidade.delete(0, END)
        self.Tipvar.set('')
        
    # Concta ao banco de dados
    def conecta_bd(self):
        self.conn = sqlite3.connect('cliente.bd')
        self.cursor = self.conn.cursor()
    # Desconcenta ao banco de dados
    def desconecta_bd(self):
        self.conn.close()
    # Criação das váriaveis 
    def variaveis(self):
        self.codigo = self.entry_cod.get()
        self.nome = self.entry_nome.get()
        self.tel = self.entry_tel.get()
        self.cidade = self.entry_cidade.get()           
          
    # Função de double clique com o mouse
    def OnDoubleClick(self, event):
        self.limpa_clientes()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.entry_cod.insert(END, col1)
            self.entry_nome.insert(END, col2)
            self.entry_tel.insert(END, col3)
            self.entry_cidade.insert(END, col4)
    # Criando a table do banco de dados
    def monta_tabelas(self):
        self.conecta_bd()   
        # Cria tabela
        self.cursor.execute("""
            Create table if not exists cadastro(
                cod INTEGER PRIMARY KEY,
                nome_cliente VARCHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade VARCHAR(50));
        """)    # Por algum motivo que apenas Deus sabe, não funciona se colocar INT no lugar de INTEGER
        self.conn.commit(); print('Banco de dados criado')
        self.desconecta_bd()    # Sempre desconecte quando terminar de usar o BD
    
    # Adicionando clientes 
    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""INSERT INTO cadastro(nome_cliente, telefone, cidade) VALUES (?, ?, ?)""", (self.nome, self.tel, self.cidade))
        self.conn.commit()
        self.select_lista()
        self.limpa_clientes()

        self.desconecta_bd()

    # Selecionando clientes
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children()) # Se nao limpar, vai repetir tudo que ja foi adicionado! 
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade from cadastro ORDER BY cod ASC; """)

        for i in lista:
            self.listaCli.insert("", END, values=i)

        self.desconecta_bd()
    
    # Função alterar clientes
    def altera_cliente(self):

        self.variaveis()
        self.conecta_bd()
        self.conn.execute("""UPDATE cadastro SET nome_cliente = ?, telefone = ?, cidade = ?  WHERE cod = ?; """, (self.nome, self.tel, self.cidade, self.codigo))

        self.conn.commit()
        self.select_lista()
        self.limpa_clientes()
        self.desconecta_bd()

    # Função buscar clientes
    def buscar_cliente(self):
        self.listaCli.delete(*self.listaCli.get_children())

        self.entry_nome.insert(END, '%')
        nome = self.entry_nome.get()

        self.entry_cidade.insert(END, '%')
        cidade = self.entry_cidade.get()

        self.entry_tel.insert(END, '%')
        telefone = self.entry_tel.get()

        self.conecta_bd()

        self.cursor.execute(f"""SELECT cod, nome_cliente, telefone, cidade FROM cadastro WHERE nome_cliente LIKE '{nome}' AND cidade LIKE '{cidade}' AND telefone LIKE '{telefone}'""")

        busca_nome_cli = self.cursor.fetchall()

        for i in busca_nome_cli:
            self.listaCli.insert("", END, values=i)

        self.limpa_clientes()

        self.desconecta_bd()

    #Função deletar clientes
    def delete_cliente(self):

        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM cadastro WHERE cod = ?""", (self.codigo,))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_clientes()
        self.select_lista()
    
    # Função deletar a table do banco de dados
    def __delete_table(self):
        self.conecta_bd()
        self.cursor.execute("""DROP TABLE IF EXISTS cadastro; """)
        self.desconecta_bd()

    # Funçao para sair
    def exit(self):
        self.root.destroy()

    # Função para abrir arquivo
    def open_file(self):
        text_file = open('about_me.txt', 'r')
        stuff = text_file.read()

        self.my_text.insert(END, stuff)

        text_file.close()
    
    # Função para remover a seta dos TIX
    def remover_seta_tix(self, *args):
        for self.balao in args:
            self.balao.subwidget('label')['image'] = BitmapImage()


class Applicativo(Funcs, Relatorio):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.criando_widgets()
        self.colunas_frame2()
        self.monta_tabelas()
        self.select_lista()
        self.menus()
        root.mainloop()
    
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.config(background='#708090')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)

    def frames(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#BEBEBE', #bd -> Borda / bg -> background / 
                            highlightbackground='black', highlightthickness=3) # highlightbackground='corda da borda', highlightthickness = espessura da borda

        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.45) # Relx -> Posição no plano x / Rely -> Pos no plano y / relwidth -> Largura / relheight = Altura
                                                                                # (0 a 1)

        self.frame_2 = Frame(self.root, bd=4, background='#BEBEBE', 
                            highlightbackground='black', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.45)

    def criando_widgets(self):
        # Criando canvas

        self.canva_bt = Canvas(self.frame_1, bd=4, bg='black', highlightbackground='#800000', highlightthickness=2, relief='sunken')

        self.canva_bt.place(relx=0.19, rely=0.08, relwidth=0.22, relheight=0.19)
    
        # Criando botão limpar
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=2, bg='#107db2', fg='white', font=('Times New Romans', 9, BOLD), activebackground='#6A5ACD', activeforeground='white', command=self.limpa_clientes)

        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # Criando botão buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#107db2', fg='white', font=('Times New Romans', 9, BOLD), activebackground='#6A5ACD', activeforeground='white', command=self.buscar_cliente)

        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # Criando botão novo
        self.bt_novo = Button(self.frame_1, text='Novo', bd=2, bg='#107db2', fg='white', font=('Times New Romans', 9, BOLD), activebackground='#6A5ACD', activeforeground='white', command=self.add_cliente)

        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criando botão alterar
        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#107db2', fg='white', font=('Times New Romans', 9, BOLD), activebackground='#6A5ACD', activeforeground='white', command=self.altera_cliente)

        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criando botão apagar
        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=2, bg='#107db2', fg='white', font=('Times New Romans', 9, BOLD),  activebackground='#6A5ACD', 
        activeforeground='white', command=self.delete_cliente)

        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criando labels e entrys

        # Label e entry codigo
        self.codigo = Label(self.frame_1, text='Código', bg='#BEBEBE', font=('Times New Romans', 9, BOLD), fg='#1F2214')
        self.codigo.place(relx=0.05, rely=0.05)
        
        self.entry_cod = Entry(self.frame_1)
        self.entry_cod.place(relx=0.05, rely=0.15, relwidth=0.07)
        
        # Label e entry nome
        self.lb_nome = Label(self.frame_1, text='Nome', bg='#BEBEBE', font=('Times New Romans', 9, BOLD), fg='#1F2214')
        self.lb_nome.place(relx=0.05, rely=0.4)

        self.entry_nome = Entry(self.frame_1)
        self.entry_nome.place(relx=0.05, rely=0.5, relwidth=0.6)
        
        # Label e entry telefone
        self.lb_tel = Label(self.frame_1, text='Telefone', bg='#BEBEBE', font=('Times New Romans', 9, BOLD), fg='#1F2214')
        self.lb_tel.place(relx=0.05, rely=0.65)

        self.entry_tel = Entry(self.frame_1)
        self.entry_tel.place(relx=0.05, rely=0.75, relwidth=0.4)
        
        # Label e entry cidade
        self.lb_cidade = Label(self.frame_1, text='Cidade', bg='#BEBEBE', font=('Times New Romans', 9, BOLD), fg='#1F2214')
        self.lb_cidade.place(relx=0.5, rely=0.65)

        self.entry_cidade = Entry(self.frame_1)
        self.entry_cidade.place(relx=0.5, rely=0.75, relwidth=0.4)

        self.Tipvar = StringVar()
        self.TipV = ('', 'M', 'F')
        self.Tipvar.set('')

        # Criação de Tix
        self.balao_buscar = tix.Balloon(self.frame_1)
        # self.balao_buscar.subwidget('label')['image'] = BitmapImage() # retira a setinha

        self.balao_buscar.bind_widget(
            self.bt_buscar,
            balloonmsg = "Digite nos campos o que deseja procurar")

        self.balao_limpar = tix.Balloon(self.frame_1)
        self.balao_limpar.bind_widget(
            self.bt_limpar,
            balloonmsg = 'Limpa todos os campos')

        self.balao_alterar = tix.Balloon(self.frame_1)
        self.balao_alterar.bind_widget(
            self.bt_alterar,
            balloonmsg='Altera um dado já cadastrado de algum cliente')

        self.balao_novo = tix.Balloon(self.frame_1)
        self.balao_novo.bind_widget(
            self.bt_novo,
            balloonmsg='Adiciona um novo cliente')

        self.balao_apagar = tix.Balloon(self.frame_1)
        self.balao_apagar.bind_widget(
            self.bt_apagar,
            balloonmsg='Apaga os dados de um cliente já cadastrado')

    
        self.remover_seta_tix(self.balao_buscar, self.balao_limpar, self.balao_apagar, self.balao_novo, self.balao_alterar)
    
    def colunas_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4', 'col5'))
        
        # Adicionando titulo
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text='Codigo')
        self.listaCli.heading("#2", text='Nome')
        self.listaCli.heading("#3", text='Telefone')
        self.listaCli.heading("#4", text='Cidade')


        # Posição das colunas [Column tem proporção de 500]
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)
        self.listaCli.column("#5", width=40)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)  

        # Criando barra de rolagem
        
        self.scrool_lista = Scrollbar(self.frame_2, orient="vertical")
        self.listaCli.config(yscroll=self.scrool_lista.set)
        
        self.scrool_lista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

        self.listaCli.bind("<Double-1>", self.OnDoubleClick)

    def menus(self):
        # Adicionando Menus
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        # Criação dos menus / tearoff = remover as linhas do menu

        filemenu = Menu(menubar, tearoff=0)
        filemenu2 = Menu(menubar, tearoff=0)
        # Adicionando de fato os menus 

        menubar.add_cascade(label='Opções',menu=filemenu)
        menubar.add_cascade(label='Relatórios', menu=filemenu2)
        # Criando os comandos dos menus

        filemenu.add_command(label='Sobre', command=self.janela_info)
        filemenu.add_command(label= 'Sair', command=self.exit)
        filemenu2.add_command(label='Ficha do Cliente', command=self.gera_relat_cliente)
   
    def janela_info(self):
        self.root2 = Toplevel()
        self.root2.title('Sobre')
        self.root2.geometry('500x300')
        self.root2.resizable(FALSE, FALSE)
        self.root2.config(background='#BEBEBE')
        self.root2.transient(self.root)    # Define que ela é filha do ROOT 
        self.root2.focus_force() # Faz com que ela fique na frente da janela anterior
        self.root2.grab_set() # Para fazer qualquer ação na tela anterior, é preciso fecha-la primeiro

        self.janela_texto()
    
    def janela_texto(self):

        # Criando o texto
        self.my_text = Text(self.root2, width=42, height=15, font=('Maiandra GD', 14))
        
        self.my_text.place(x=10, y=10)

        # Criando a barra e posicionando a barra
        self.scroll_bar_janela = ttk.Scrollbar(self.root2, orient='vertical')

        self.scroll_bar_janela.place(relx=0.96, rely=0.05, relwidth=0.03, relheight=0.94)

        # Adiciona a barra de rolagem ao my_text
        self.my_text.config(yscrollcommand=self.scroll_bar_janela.set)

        self.open_file()

        self.my_text.config(state=DISABLED)



Applicativo()