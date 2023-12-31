import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS estudantes(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       email TEXT NOT NULL,
                       tel TEXT NOT NULL,
                       sexo TEXT NOT NULL,
                       data_de_nascimento TEXT NOT NULL,
                       endereco TEXT NOT NULL,
                       curso TEXT NOT NULL,
                       picture TEXT NOT NULL)
                       ''')
        
    def register_student(self, estudantes):
        self.c.execute("INSERT INTO estudantes(nome, email, tel, sexo, data_de_nascimento, endereco, curso, picture) "
                       "VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (estudantes))
        self.conn.commit()
        
        #Mostrando mensagem de sucessso
        messagebox.showinfo('Sucesso', 'Registo com sucesso')
    
    def view_all_students(self):
        self.c.execute("SELECT * FROM estudantes")
        dados = self.c.fetchall()
        return dados
    
    def searsh_studant(self, id):
        try:
            self.c.execute("SELECT * FROM estudantes WHERE id=?", (id,))
            dados = self.c.fetchone()
            return dados
        except TypeError:
            messagebox.showinfo("Erro!", f"Não existe cadastro com o ID{id}")

    def update_studants(self, novos_valores):
        query = ("UPDATE estudantes SET nome=?, email=?, tel=?, data_de_nascimento=?, sexo=?, endereco=?, curso=?, picture=? WHERE id=?")
        self.c.execute(query, novos_valores)
        self.conn.commit()

                #Mostrando mensagem de sucessso
        messagebox.showinfo(f'Sucesso', f'Estudante com ID{novos_valores[8]} foi aualizado')

    def delete_studante(self, id):
        self.c.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.conn.commit()
        messagebox.showinfo(f'Sucesso', f'Estudante com ID{id} foi deletado')


# Criando instancia do sistema de registro
sistema_de_registro = SistemaDeRegistro()
