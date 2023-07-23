# Importando dependencias do TKinter====================================================================================
from tkinter import *
from tkinter.ttk import Style
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# Importnaod pillow
from PIL import ImageTk, Image

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# Importando main
from main import *

# cores=================================================================================================================

cor0 = "#2e2d2b"  # Preta
cor1 = "#feffff"  # Branca
cor2 = "#e5e5e5"  # grey
cro3 = "#00a095"  # Verde
cor4 = "#403d3d"  # letra
cor6 = "#003452"  # azul
cor7 = "#ef5350"  # vermelha

cor8 = "#146C94"  # azul
cor9 = "#263238"  # + verde
cor10 = "#e9edf5"  # + verde

# Criando janela========================================================================================================

janela = Tk()
janela.title("")
janela.geometry('810x535')
janela.config(background=cor1)
janela.resizable(width=FALSE, height=FALSE)

style = Style()
style.theme_use("clam")

# criando frames========================================================================================================

frame_logo = Frame(janela, width=850, height=52, bg=cor6)
frame_logo.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=cor1, relief=RAISED)
frame_botoes.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

frame_detalhes = Frame(janela, width=800, height=200, bg=cor1, relief=SOLID)
frame_detalhes.grid(row=1, column=1, padx=10, pady=1, sticky=NSEW)

frame_tabela = Frame(janela, width=800, height=100, bg=cor1, relief=SOLID)
frame_tabela.grid(row=3, column=0, padx=10, pady=0, sticky=NSEW, columnspan=5)

# Adicionando as imagens da logo========================================================================================

global imagem, imagem_string, l_imagem

app_lg = Image.open('logo.png')
app_lg = app_lg.resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text=" Sistema de registro de Alunos", width=850, compound=LEFT, anchor=NW,
                 font='Verdana 15', bg=cor6, fg=cor1)
app_logo.place(x=5, y=-5)

# abriando a imagem

imagem = Image.open('logo.png')
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_detalhes, image=imagem, bg=cor1, fg=cor4)
l_imagem.place(x=390, y=10)


# criando funções para CRUD=============================================================================================
# funcao add
def add():
    global imagem, imagem_string, l_imagem

    # Obtendo os valores
    nome = entrada_nome.get()
    email = entrada_email.get()
    tel = entrada_telefone.get()
    sexo = entrada_sexo.get()
    data = data_nasciemento.get()
    endereco = entrada_endereco.get()
    cursos = entrada_curso.get()
    img = imagem_string

    lista = [nome, email, tel, sexo, data, endereco, cursos, img]

    # Verificando se a lista esta vazia:
    for i in lista:
        if i == '':
            messagebox.showerror("ERRO", "Preencha todos os campos")
            return
    # Registrando os valores
    sistema_de_registro.register_student(lista)

    # limpando os campos de entradas
    entrada_nome.delete(0, END)
    entrada_email.delete(0, END)
    entrada_telefone.delete(0, END)
    entrada_sexo.delete(0, END)
    data_nasciemento.delete(0, END)
    entrada_endereco.delete(0, END)
    entrada_curso.delete(0, END)

    # Mostrando os valores na tabela
    mostrar_alunos()


# Funcao procurar
def procurar_aluno():
    global imagem, imagem_string, l_imagem

    # obtendo id
    id_aluno = int(entrada_id.get())

    # procurar aluno
    dados = sistema_de_registro.searsh_studant(id_aluno)

    # Limpar dados
    entrada_nome.delete(0, END)
    entrada_email.delete(0, END)
    entrada_telefone.delete(0, END)
    entrada_sexo.delete(0, END)
    data_nasciemento.delete(0, END)
    entrada_endereco.delete(0, END)
    entrada_curso.delete(0, END)

    # inserir dados
    entrada_nome.insert(END, dados[1])
    entrada_email.insert(END, dados[2])
    entrada_telefone.insert(END, dados[3])
    entrada_sexo.insert(END, dados[4])
    data_nasciemento.insert(END, dados[5])
    entrada_endereco.insert(END, dados[6])
    entrada_curso.insert(END, dados[7])
    imagem = dados[8]
    imagem_string = imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem, bg=cor1, fg=cor4)
    l_imagem.place(x=390, y=10)


# Funcao atualiar
def atualizar():
    global imagem, imagem_string, l_imagem

    # obtendo o id do aluno
    id_aluno = int(entrada_id.get())

    # Obtendo os valores
    nome = entrada_nome.get()
    email = entrada_email.get()
    tel = entrada_telefone.get()
    sexo = entrada_sexo.get()
    data = data_nasciemento.get()
    endereco = entrada_endereco.get()
    cursos = entrada_curso.get()
    img = imagem_string

    lista = [nome, email, tel, sexo, data, endereco, cursos, img, id_aluno]

    # Verificando se a lista esta vazia:
    for i in lista:
        if i == '':
            messagebox.showerror("ERRO", "Preencha todos os campos")
            return
    # Registrando os valores
    sistema_de_registro.update_studants(lista)

    # limpando os campos de entradas
    entrada_nome.delete(0, END)
    entrada_email.delete(0, END)
    entrada_telefone.delete(0, END)
    entrada_sexo.delete(0, END)
    data_nasciemento.delete(0, END)
    entrada_endereco.delete(0, END)
    entrada_curso.delete(0, END)

    # abrindo a imagem
    imagem = Image.open('logo.png')
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem, bg=cor1, fg=cor4)
    l_imagem.place(x=390, y=10)

    # Mostrando os valores na tabela
    mostrar_alunos()


#Funcao deletar
def deletar():
    global imagem, imagem_string, l_imagem

    # obtendo o id do aluno
    id_aluno = int(entrada_id.get())

    #deletando aluno
    sistema_de_registro.delete_studante(id_aluno)

    # limpando os campos de entradas
    entrada_nome.delete(0, END)
    entrada_email.delete(0, END)
    entrada_telefone.delete(0, END)
    entrada_sexo.delete(0, END)
    data_nasciemento.delete(0, END)
    entrada_endereco.delete(0, END)
    entrada_curso.delete(0, END)
    entrada_id.delete(0, END)

    # abrindo a imagem
    imagem = Image.open('logo.png')
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem, bg=cor1, fg=cor4)
    l_imagem.place(x=390, y=10)

    mostrar_alunos()

# Criando os campus de entrada==========================================================================================

l_nome = Label(frame_detalhes, text="Nome *", anchor=NW, font='Ivy 10', bg=cor1, fg=cor4)
l_nome.place(x=4, y=10)
entrada_nome = Entry(frame_detalhes, width=30, justify='left', relief=SOLID)
entrada_nome.place(x=7, y=40)

l_email = Label(frame_detalhes, text="Email *", anchor=NW, font='Ivy 10', bg=cor1, fg=cor4)
l_email.place(x=4, y=70)
entrada_email = Entry(frame_detalhes, width=30, justify='left', relief=SOLID)
entrada_email.place(x=7, y=100)

l_telefone = Label(frame_detalhes, text="Telefone *", anchor=NW, font='Ivy 10', bg=cor1, fg=cor4)
l_telefone.place(x=4, y=130)
entrada_telefone = Entry(frame_detalhes, width=15, justify='left', relief=SOLID)
entrada_telefone.place(x=7, y=160)

l_sexo = Label(frame_detalhes, text="Sexo *", anchor=NW, font='Ivy 10', bg=cor1, fg=cor4)
l_sexo.place(x=127, y=130)
entrada_sexo = ttk.Combobox(frame_detalhes, width=7, font='Ivy 8 bold', justify='center')
entrada_sexo['values'] = ('M', 'F', 'T')
entrada_sexo.place(x=130, y=160)

l_data_nascimento = Label(frame_detalhes, text="Data de nascimento *", anchor=NW, font='Ivy 10', bg=cor1, fg=cor4)
l_data_nascimento.place(x=220, y=10)
data_nasciemento = DateEntry(frame_detalhes, width=18, justify='center', backgroud='darkblue', foreground='white',
                             bordewidth=2, year=2023)
data_nasciemento.place(x=224, y=40)

l_endereco = Label(frame_detalhes, text="Endereço *", anchor=NW, font='Ivy 10', bg=cor1, fg=cor4)
l_endereco.place(x=220, y=70)
entrada_endereco = Entry(frame_detalhes, width=20, justify='left', relief=SOLID)
entrada_endereco.place(x=224, y=100)

cursos = [
    'Medicina',
    'Direito',
    'Administração',
    'Engenharia Civil',
    'Psicologia',
    'Arquitetura e Urbanismo',
    'Enfermagem',
    'Odontologia',
    'Pedagogia',
    'Ciência da Computação',
    'Economia',
    'Fisioterapia',
    'Nutrição',
    'Jornalismo',
    'Publicidade e Propaganda',
    'Engenharia de Software',
    'Engenharia de Produção',
    'Farmácia',
    'Medicina Veterinária',
    'Gastronomia',
    'Biomedicina',
    'Engenharia Mecânica',
    'Engenharia Elétrica',
    'Engenharia de Computação',
    'Engenharia Química',
    'Engenharia Ambiental',
    'Ciências Biológicas',
    'Engenharia Biomédica',
    'Engenharia de Alimentos',
    'Engenharia Aeroespacial',
    'Engenharia de Sistemas',
    'Engenharia de Robótica',
    'Engenharia de Cibersegurança',
    'Engenharia Nuclear',
    'Engenharia de Energias Renováveis',
    'Engenharia de Inteligência Artificial',
    'Engenharia de Biotecnologia',
    'Engenharia de Mineração',
    'Engenharia de Sistemas Aeroespaciais']
l_curso = Label(frame_detalhes, text="Curso *", anchor=NW, font='Ivy 10', bg=cor1, fg=cor4)
l_curso.place(x=220, y=130)
entrada_curso = ttk.Combobox(frame_detalhes, width=20, font='Ivy 8 bold', justify='center')
entrada_curso['values'] = cursos
entrada_curso.place(x=224, y=160)


# funcao para escolher imagem
def escolher_imagem():
    global imagem, imagem_string, l_imagem
    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem, bg=cor1, fg=cor4)
    l_imagem.place(x=390, y=10)


botao_carregar = Button(frame_detalhes, command=escolher_imagem, text="Carregar foto".upper(), width=20,
                        compound=CENTER, anchor=CENTER, overrelief=RIDGE, font='Ivy 7 bold', bg=cor1, fg=cor0)
botao_carregar.place(x=390, y=160)


# Tabela Alunos
def mostrar_alunos():
    # creating a treeview with dual scrollbars
    list_header = ['id', 'Nome', 'email', 'Telefone', 'sexo', 'Data', 'Endereço', 'Curso']

    # view all students
    df_list = sistema_de_registro.view_all_students()

    tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "center", "center", "center", "center", "center", "center"]
    h = [40, 150, 150, 70, 70, 70, 120, 100, 100]
    n = 0

    for col in list_header:
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        # adjust the column's width to the header string
        tree_aluno.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in df_list:
        tree_aluno.insert('', 'end', values=item)


# Procurar aluno========================================================================================================

frame_procurar = Frame(frame_botoes, width=40, height=50, bg=cor1, relief=RAISED)
frame_procurar.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

l_nome = Label(frame_procurar, text="Procurar aluno [Inserir ID]", anchor=NW, font='Ivy 10', bg=cor1, fg=cor4)
l_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

entrada_id = Entry(frame_procurar, width=5, justify='center', relief=SOLID, font='Ivy 10')
entrada_id.grid(row=1, column=0, padx=0, pady=10, sticky=NSEW)

botao_procurar = Button(frame_procurar, text="Procurar", command=procurar_aluno, width=9, anchor=CENTER,
                        overrelief=RIDGE, font='Ivy 7 bold',
                        bg=cor1, fg=cor0)
botao_procurar.grid(row=1, column=1, padx=0, pady=10, sticky=NSEW)

# Botoes [add, del, update]=============================================================================================

app_add = Image.open('add.png')
app_add = app_add.resize((25, 25))
app_add = ImageTk.PhotoImage(app_add)
botao_add = Button(frame_botoes, image=app_add, command=add, relief=GROOVE, text="Adicionar", width=100, compound=LEFT,
                   overrelief=RIDGE, font='Ivy 7 bold',
                   bg=cor1, fg=cor0)
botao_add.grid(row=1, column=0, padx=10, pady=5, sticky=NSEW)

app_update = Image.open('update.png')
app_update = app_update.resize((25, 25))
app_update = ImageTk.PhotoImage(app_update)
botao_update = Button(frame_botoes, command=atualizar, image=app_update, relief=GROOVE, text="Atualizar", width=100,
                      compound=LEFT,
                      overrelief=RIDGE, font='Ivy 7 bold',
                      bg=cor1, fg=cor0)
botao_update.grid(row=2, column=0, padx=10, pady=5, sticky=NSEW)

app_delete = Image.open('delete.png')
app_delete = app_delete.resize((25, 25))
app_delete = ImageTk.PhotoImage(app_delete)
botao_update = Button(frame_botoes, command=deletar, image=app_delete, relief=GROOVE, text="Deletar", width=100, compound=LEFT,
                      overrelief=RIDGE, font='Ivy 7 bold',
                      bg=cor1, fg=cor0)
botao_update.grid(row=3, column=0, padx=10, pady=5, sticky=NSEW)

# linha separadora
l_linha = Label(frame_botoes, relief=GROOVE, width=1, height=123, anchor=NW, font='Ivy 1', bg=cor0, fg=cor0)
l_linha.place(x=236, y=15)

# Chamar tabela
mostrar_alunos()

janela.mainloop()
