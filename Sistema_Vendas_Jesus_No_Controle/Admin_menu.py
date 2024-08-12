import sqlite3
import time
import tkinter as tk
from tkinter import Label, ttk, messagebox,Toplevel
from tkinter import *
from cx import *
import calendar
from tkcalendar import Calendar
import holidays
from datetime import date

class Admin:
    def Admin_mainmenu(self,a,b):
        self.janela_principal.iconbitmap('ImageTk/logo.ico'
        )
        self.janela_principal.title("Usuario")
        self.janela_usu = Frame(
            self.janela_principal, width=1550, height=1000, bg="black"
        )
        self.janela_usu.place(x=0,y=0)
        self.topframe = LabelFrame(
            self.janela_usu, width=1420, height=97, bg="#616161"
        )
        self.topframe.place(x=(1550 - 1450)/2,y=0)
        self.loja_nome = "'AREA EM DESENVOLVIMENTO "
        self.loja_lable = Label(
            self.topframe,
            text=self.loja_nome + " ADMIN",
            bg="#616161",
            anchor="center",
        )
        self.loja_lable.config(font="arial 30 bold", fg="snow")
        self.loja_lable.place(x=150, y=30)
        img = PhotoImage(file="ImageTk/Usu.png")
        img = img.subsample(2, 2)
        self.meu_perfil = ttk.Label(self.topframe, image=img, compound=TOP)
        self.meu_perfil.image = img
        self.meu_perfil.place(x=1250, y=8)

        self.mainframe = LabelFrame(
            self.janela_usu, width=1200, height=105, bg="#c4c2c2"
        )
        self.mainframe.place(x=(1550 - 1200)/2,y=100)

        img = PhotoImage(file="ImageTk/companhia.png")
        """img=img.subsamples(a,b)"""
        self.clientes_bu = Button(
            self.mainframe,
            text="Empresa",
            font="arial 11 bold",
            image=img,
            bd=1,
            command=self.Empresa,
            compound=TOP,
        )
        self.clientes_bu.place(x=620, y=27)
        self.clientes_bu.image = img

        img = PhotoImage(file="ImageTk/sair.png")
        self.sair = Button(
            self.mainframe,
            text="Sair",
            font="arial 11 bold",
            image=img,
            bd=1,
            command=self._del_usu_,
            compound=TOP,
        )
        self.sair.place(x=1050, y=27)
        self.sair.image = img

        img = PhotoImage(file="ImageTk/usuario.png")
        self.trocausuario = Button(
            self.mainframe,
            text="Trocar Usuario",
            font="arial 11 bold",
            image=img,
            command=self.troca_usu,
            bd=1,
            compound=TOP,
        )
        self.trocausuario.place(x=875, y=27)
        self.trocausuario.image = img

        img = PhotoImage(file="ImageTk/inventario.png")
        self.itens_bu = Button(
            self.mainframe,
            text="Estoque",
            font="arial 11 bold",
            image=img,
            bd=1,
            command=self.estoque,
            compound=TOP,
        )
        self.itens_bu.place(x=205, y=27)
        self.itens_bu.image = img

        img = PhotoImage(file="ImageTk/vendas.png")
        self.vendas_h = Button(
            self.mainframe,
            text="Vendas",
            font="arial 11 bold",
            image=img,
            bd=1,
            command=self.vendas,
            compound=TOP,
        )
        self.vendas_h.place(x=370, y=27)
        self.vendas_h.image = img

        self.Empresa()
    
    def estoque(self):
        img = PhotoImage(file="ImageTk/confg.png")
        self.table_itens = LabelFrame(
            self.janela_usu, width=1250, height=640, bg="white"
        )
        self.table_itens.place(x=(1550 - 1250)/2, y=205)
        self.table_itens_add = Button(
            self.table_itens, image=img, bd=0, command=self.execute_itens
        )
        self.table_itens_add.place(x=1220, y=0)
        self.table_itens_add.image = img

        self.pesquisa_cdg_texto = Label(
            self.table_itens, text="Codigo", font="Arial 10 ", bg="white"
        )
        self.pesquisa_cdg_texto.place(x=0, y=0)
        self.pesquisa_produto_texto = Label(
            self.table_itens, text="Produto", font="Arial 10 ", bg="white"
        )
        self.pesquisa_produto_texto.place(x=220, y=0)

        self.pesquisa_cdg_digito = Entry(self.table_itens, width=25, bg="white", bd=1)
        self.pesquisa_cdg_digito.bind(
            "<Return>", lambda event: self.pesquisa_nome_testo.focus()
        )
        self.pesquisa_cdg_digito.bind("<KeyPress-c>", lambda event: self.chama_caixa())
        self.pesquisa_cdg_digito.bind(
            "<KeyRelease>", lambda event: self.tabela_pesquisa_cdg()
        )
        self.pesquisa_cdg_digito.bind(
            "<KeyPress-a>", lambda event: self.execute_itens()
        )
        self.pesquisa_cdg_digito.bind("<KeyPress-s>", lambda event: self._del_usu_())
        self.pesquisa_cdg_digito.bind("<KeyPress-k>", lambda event: self.Empresa())
        self.pesquisa_cdg_digito.place(x=0, y=18, height=25)
        self.pesquisa_nome_testo = Entry(self.table_itens, width=150, bg="white", bd=1)
        self.pesquisa_nome_testo.bind(
            "<Return>", lambda event: self.pesquisa_cdg_digito.focus()
        )
        self.pesquisa_nome_testo.bind(
            "<KeyRelease>", lambda event: self.tabela_pesquisa_nome()
        )
        self.pesquisa_nome_testo.place(x=220, y=18, height=25)

        self.pesquisa_cdg_digito.focus()
        
        estilo = ttk.Style()
        estilo.configure(
            "Treeview",
            font=("Arial", 15),
            background="#9DCFFA",
            foreground="black",
            rowheight=25,
            fieldbackground="#93FDF6",
        )
        self.table = ttk.Treeview(self.table_itens, height=800)
        self.table.place(x=0, y=50, width=1200)
        self.table["columns"] = ("Codigo", "PRODUTO", "PREÇO", "QTDE")

        self.table.column("#0", width=1, minwidth=1)
        self.table.column("#1", width=50, minwidth=20)
        self.table.column("#2", width=20, minwidth=20)
        self.table.column("#3", width=50, minwidth=20)

        self.table.heading("#0", text="Codigo")
        self.table.heading("#1", text="Produto")
        self.table.heading("#2", text="Preço")
        self.table.heading("#3", text="Quantidade")
          
        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()
        b.execute("SELECT Codigo, PRODUTO, PREÇO, QTDE FROM Estoque")
        rows = b.fetchall()
        for row in rows:
            self.table.insert(
                parent="", index="end", text=row[0], values=(row[1], row[2], row[3])
            )
            self.table.place(x=0, y=50, width=1200)
        self.edts.place_forget()

    def tabela_pesquisa_cdg(self):
        codigim=self.pesquisa_cdg_digito.get()        
        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()

        try:
            if codigim:
                b.execute("SELECT Codigo, PRODUTO, PREÇO, QTDE FROM Estoque WHERE Codigo LIKE ?", ('%' + codigim + '%',))
            else:
                b.execute("SELECT Codigo, PRODUTO, PREÇO, QTDE FROM Estoque")

            rows = b.fetchall()
            self.clear_table()
            for row in rows:
                self.table.insert("", "end", text=row[0], values=(row[1], row[2], row[3]))

        except sqlite3.Error as e:
            print("Erro ao acessar o banco de dados:", e)

        finally:
            Banco.close()

    def limpa_pesquisa(self):
        self.pesquisa_cdg_digito.delete(0, END)
        self.pesquisa_nome_testo.delete(0, END)

    def tabela_pesquisa_nome(self):
        texto_digitado = self.pesquisa_nome_testo.get()
        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()

        try:
            if texto_digitado:
                b.execute("SELECT Codigo, PRODUTO, PREÇO, QTDE FROM Estoque WHERE PRODUTO LIKE ?", ('%' + texto_digitado + '%',))
            else:
                b.execute("SELECT Codigo, PRODUTO, PREÇO, QTDE FROM Estoque")

            rows = b.fetchall()
            self.clear_table()
            for row in rows:
                self.table.insert("", "end", text=row[0], values=(row[1], row[2], row[3]))

        except sqlite3.Error as e:
            print("Erro ao acessar o banco de dados:", e)

        finally:
            Banco.close()
            
    def clear_table(self):
        for item in self.table.get_children():
            self.table.delete(item)
        
    def Empresa(self):
        self.table_clientes = LabelFrame(
            self.janela_usu, width=1250, height=640, bg="#666666"
        )
        self.table_clientes.place(x=(1550 - 1250)/2, y=205)
        
        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()  
        b.execute("SELECT nome FROM empresa ")
        nome_empre = b.fetchall()
        self.nome_empre=Label(self.table_clientes,font="Arial 12 bold",text="Nome :",bd=0,bg="#666666",foreground="black")
        self.nome_empre.place(x=2,y=0)
        self.nome_empre_entry=ttk.Combobox(self.table_clientes,font="Arial 10 bold",foreground="black",width=50,height=20)
        self.nome_empre_entry["values"] = nome_empre
        self.nome_empre_entry.bind("<Return>",lambda event:self.caminha_nome())
        self.nome_empre_entry.bind("<<ComboboxSelected>>",lambda event:self.caminha_nome())
        self.nome_empre_entry.place(x=2,y=20)
        self.nome_empre_entry.focus()
        self.Email=Label(self.table_clientes,font="Arial 12 bold",text="Gmail :",bd=0,bg="#666666",foreground="black")
        self.Email.place(x=400,y=0)
        self.Email_entry=Entry(self.table_clientes,font="Arial 10 bold",bd=1,foreground="black",width=50)
        self.Email_entry.bind("<Return>",lambda event:self.Celular_entry.focus())
        self.Email_entry.place(x=400,y=20,height=20)
        self.Celular=Label(self.table_clientes,font="Arial 12 bold",text="Celular :",bd=0,bg="#666666",foreground="black")
        self.Celular.place(x=800,y=0)
        self.Celular_entry=Entry(self.table_clientes,font="Arial 10 bold",bd=1,foreground="black",width=25)
        self.Celular_entry.bind("<Return>",lambda event:self.caminha_cell())
        self.Celular_entry.place(x=800,y=20,height=20)
        self.CNPJ=Label(self.table_clientes,font="Arial 12 bold",text="C.N.P.J :",bd=0,bg="#666666",foreground="black")
        self.CNPJ.place(x=2,y=50)
        self.CNPJ_entry=Entry(self.table_clientes,font="Arial 10 bold",bd=1,foreground="black",width=30)
        self.CNPJ_entry.bind("<Return>",lambda event:self.caminha_cnpf())
        self.CNPJ_entry.place(x=2,y=70,height=20)
        self.IE=Label(self.table_clientes,font="Arial 12 bold",text="Inscr. Estadual :",bd=0,bg="#666666",foreground="black")
        self.IE.place(x=300,y=50)
        self.IE_entry=Entry(self.table_clientes,font="Arial 10 bold",bd=1,foreground="black",width=25)
        self.IE_entry.bind("<Return>",lambda event:self.Endere_entry.focus())
        self.IE_entry.place(x=300,y=70,height=20)

        self.pix_amar = StringVar(value="vazio")
        self.br=Label(self.table_clientes, bg="#666666",text="Chave pix:",font="Arial 12 bold",width=25,bd=0,fg="black")
        self.br.place(x=650,y=50)
        self.A=Radiobutton(self.table_clientes,font="Arial 12 bold",variable=self.pix_amar,value="CPF/CNPJ",text="CPF/CNPJ",bg="#666666",bd=1,fg="black")
        self.A.place(x=550,y=70)
        self.B=Radiobutton(self.table_clientes,font="Arial 12 bold",variable=self.pix_amar,value="TELEFONE",text="TELEFONE",bg="#666666",bd=1,fg="black")
        self.B.place(x=750,y=70)
        self.C=Radiobutton(self.table_clientes,font="Arial 12 bold",variable=self.pix_amar,value="GMAIL",text="GMAIL",bg="#666666",bd=1,fg="black")
        self.C.place(x=950,y=70)

        self.Endere=Label(self.table_clientes,font="Arial 12 bold",text="Endereço :",bd=0,bg="#666666",foreground="black")
        self.Endere.place(x=2,y=100)
        self.Endere_entry=Entry(self.table_clientes,font="Arial 10 bold",bd=1,foreground="black",width=35)
        self.Endere_entry.bind("<Return>",lambda event:self.nu_end_entry.focus())
        self.Endere_entry.place(x=2,y=120,height=20)
        self.nu_end=Label(self.table_clientes,font="Arial 12 bold",text="N° :",bd=0,bg="#666666",foreground="black")
        self.nu_end.place(x=300,y=100)
        self.nu_end_entry=Entry(self.table_clientes,font="Arial 10 bold",bd=1,foreground="black",width=5)
        self.nu_end_entry.bind("<Return>",lambda event:self.Bairro_entry.focus())
        self.nu_end_entry.place(x=300,y=120,height=20)
        self.Bairro=Label(self.table_clientes,font="Arial 12 bold",text="Bairro :",bd=0,bg="#666666",foreground="black")
        self.Bairro.place(x=400,y=100)
        self.Bairro_entry=Entry(self.table_clientes,font="Arial 10 bold",bd=1,foreground="black",width=25)
        self.Bairro_entry.bind("<Return>",lambda event:self.Comple_entry.focus())
        self.Bairro_entry.place(x=400,y=120,height=20)
        self.Comple=Label(self.table_clientes,font="Arial 12 bold",text="Complemento :",bd=0,bg="#666666",foreground="black")
        self.Comple.place(x=650,y=100)
        self.Comple_entry=Entry(self.table_clientes,font="Arial 10 bold",bd=1,foreground="black",width=25)
        self.Comple_entry.bind("<Return>",lambda event:self.estado_entry.focus())
        self.Comple_entry.place(x=650,y=120,height=20)
        self.estado=Label(self.table_clientes,font="Arial 12 bold",text="Estado :",bd=0,bg="#666666",foreground="black")
        self.estado.place(x=2,y=150)
        self.estado_entry=Entry(self.table_clientes,font="Arial 10 bold",bd=1,foreground="black",width=25)
        self.estado_entry.bind("<Return>",lambda event:self.city_entry.focus())
        self.estado_entry.place(x=2,y=170,height=20)
        self.city=Label(self.table_clientes,font="Arial 12 bold",text="Cidade :",bd=0,bg="#666666",foreground="black")
        self.city.place(x=250,y=150)
        self.city_entry=Entry(self.table_clientes,font="Arial 10 bold",bd=1,foreground="black",width=25)
        self.city_entry.bind("<Return>",lambda event:self.Cep_entry.focus())
        self.city_entry.place(x=250,y=170,height=20)
        self.Cep=Label(self.table_clientes,font="Arial 12 bold",text="Cep :",bd=0,bg="#666666",foreground="black")
        self.Cep.place(x=500,y=150)
        self.Cep_entry=Entry(self.table_clientes,font="Arial 10 bold",bd=1,foreground="black",width=25)
        self.Cep_entry.bind("<Return>",lambda event:self.caminha_cep())
        self.Cep_entry.place(x=500,y=170,height=20)
        Button(self.table_clientes, font="Arial 12 bold",text="Salvar",command=self.salvar, bd=3,fg="black",bg="#666666").place(x=750, y=190)
        if self.table_itens.winfo_exists:
            self.table_itens.place_forget()
        if self.table_vendas.winfo_exists:
            self.table_vendas.place_forget()
    def caminha_nome(self):
        nome=self.nome_empre_entry.get()
        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()
        if nome:
            b.execute("SELECT * FROM empresa WHERE nome=?", (nome,))
            valor = b.fetchall()
            if valor:
                messagebox.showinfo("Existe","Usuario ja existente...")
                self.inseri(valor)
            self.Email_entry.focus()    
    def caminha_cnpf(self):
        if not self.so_numero():
            cnpj=self.CNPJ_entry.get()
            Banco = sqlite3.connect("banco.db")
            b = Banco.cursor()
            if cnpj:
                b.execute("SELECT * FROM empresa WHERE cnpj=?", (cnpj,))
                valor = b.fetchall()
                if valor:
                    messagebox.showinfo("Existe","CNPJ ja existente...")
                    self.inseri(valor)
                self.IE_entry.focus()
    def caminha_cell(self):
        if not self.so_numero():
            self.CNPJ_entry.focus()
    def caminha_cep(self):
        if not self.so_numero():
            self.salvar()      
    def so_numero(self):
        tell=self.Celular_entry.get().isalpha()
        cnpj=self.CNPJ_entry.get().isalpha()
        cep=self.Celular_entry.get().isalpha()
        if tell or cnpj or cep:
            messagebox.showerror("Error numerico","Digite apenas numeros !!!")
            return True
    def inseri(self,valor):
        name,gmail,cell,cnpj_,ieeee,pix,endereço,nu_ende,bairro,complemento,estado,cidade,cep=valor[0]
        self.nome_empre_entry.delete(0,END)
        self.Email_entry.delete(0,END)
        self.Celular_entry.delete(0,END)
        self.CNPJ_entry.delete(0,END)
        self.IE_entry.delete(0,END)
        self.Endere_entry.delete(0,END)
        self.nu_end_entry.delete(0,END)
        self.Bairro_entry.delete(0,END)
        self.Comple_entry.delete(0,END)
        self.estado_entry.delete(0,END)
        self.city_entry.delete(0,END)
        self.Cep_entry.delete(0,END)
        self.nome_empre_entry.insert(END,name)
        self.Email_entry.insert(END,gmail)
        self.Celular_entry.insert(END,cell)
        self.CNPJ_entry.insert(END,cnpj_)
        self.IE_entry.insert(END,ieeee)
        self.Endere_entry.insert(END,endereço)
        self.nu_end_entry.insert(END,nu_ende)
        self.Bairro_entry.insert(END,bairro)
        self.Comple_entry.insert(END,complemento)
        self.estado_entry.insert(END,estado)
        self.city_entry.insert(END,cidade)
        self.Cep_entry.insert(END,cep)
        self.pix_amar.set(pix)
        self.Email_entry.focus()

    def salvar(self):
        nome=self.nome_empre_entry.get()
        gmail=self.Email_entry.get()
        cell=self.Celular_entry.get()
        cnpj=self.CNPJ_entry.get()
        ieeee=self.IE_entry.get()
        pix=self.pix_amar.get()
        endereço=self.Endere_entry.get()
        nu_ende=self.nu_end_entry.get()
        bairro=self.Bairro_entry.get()
        complemento=self.Comple_entry.get()
        estado=self.estado_entry.get()
        cidade=self.city_entry.get()
        cep=self.Cep_entry.get()
        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()    
        b.execute("SELECT * FROM empresa WHERE nome=?", (nome,))
        verifica_nome = b.fetchall()
        b.execute("SELECT * FROM empresa WHERE cnpj=?", (cnpj,))
        verifica_cnpj = b.fetchall()
        if nome!="" and gmail!="" and cell!="" and cnpj!="" and ieeee!="" and pix !="vazio" and endereço!="" and nu_ende!="" and bairro!="" and estado!="" and cidade!="" and cep!="" :
            if not verifica_cnpj and not verifica_nome:
                query = "INSERT INTO empresa (nome,gmail,cell,cnpj,iee,pix,endereco,nu_endereco,bairro,complemento,estado,cidade,cep) VALUES (?, ?, ?, ?, ?,?,?,?,?,?,?,?,?)"
                values = (nome,gmail,cell,cnpj,ieeee,pix,endereço,nu_ende,bairro,complemento,estado,cidade,cep)
                b.execute(query,values)
                Banco.commit()
                messagebox.showinfo("Cadastro","Cadastro realizado com sucesso!!!")
            else:
                if messagebox.askyesno("Aviso","Deseja atualizalo ?"):
                    query = "UPDATE empresa SET nome=?, gmail=?, cell=?, cnpj=?, iee=?, pix=?, endereco=?, nu_endereco=?, bairro=?, complemento=?, estado=?, cidade=?, cep=?"
                    values = (nome,gmail,cell,cnpj,ieeee,pix,endereço,nu_ende,bairro,complemento,estado,cidade,cep)
                    b.execute(query,values)
                    Banco.commit()
                    messagebox.showinfo("Atualização","Cadastro atualizado com sucesso!!!") 
        else:
            messagebox.showerror("Vazio","Preencha todos os campos")
    def vendas(self):
        img = PhotoImage(file="ImageTk/confg.png")
        self.table_vendas = LabelFrame(
            self.janela_usu, width=1250, height=640, bg="yellow"
        )
        self.table_vendas.place(x=(1550 - 1250)/2, y=205)
        self.table_vendas_add = Button(self.table_vendas, image=img, bd=0, compound=TOP)
        self.table_vendas_add.place(x=1220, y=0)
        self.table_itens_add.image = img
        if self.table_itens.winfo_exists:
            self.table_itens.place_forget()
        if self.table_clientes.winfo_exists:
            self.table_clientes.place_forget()

    def edt(self):
        self.edts = LabelFrame(self.table_itens, width=1200, height=800, bg="black")
        self.edts.place(x=5, y=0)
        self.edt_itens()

    def fecha_ajustes(self):
        self.limpa_pesquisa()
        self.edts.place_forget()
        self.pesquisa_cdg_digito.focus()

    def validate_entry(self, char):
        if char.isalpha() or char == "":
            return False
        else:
            return True

    def verifica_codigo_fun(self):
        cdg_veri = self.cdg_ent.get()
        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()

        b.execute(
            "SELECT Codigo, PRODUTO, PREÇO, QTDE,custo FROM Estoque WHERE Codigo=?",
            (cdg_veri,),
        )
        result = b.fetchone()
        self.relod_edt()
        self.limpa_entry()
        if result is not None:
            cdg, nome, valor, qtde, custos = result
            self.Cdg.insert(0, str(cdg))
            self.Produto.insert(0, str(nome))
            self.Preco.insert(0, str(valor))
            self.Qtde.insert(0, str(qtde))
            self.custo.insert(0,str(custos))
            Banco.close()
            self.Produto.focus()
        else:
            Banco = sqlite3.connect("banco.db")
            b = Banco.cursor()
            b.execute("SELECT Codigo FROM Estoque ORDER BY Codigo DESC LIMIT 1")
            self.cdg_valor = b.fetchone()[0] 
            cdg_1 = self.cdg_valor + 1
            self.Cdg.insert(0, str(cdg_1))
            self.Produto.focus()

    def edt_itens(self, *args, **kwargs):
        self.toplabel = Label(
            self.edts,
            fg="white",
            bg="#151515",
            anchor="center",
            text="Ajustes",
            font="arial 20",
        )
        self.toplabel.place(x=200, y=0)
        self.text_cdg = Label(
            self.edts,
            fg="white",
            bg="#151515",
            anchor="center",
            text="Codigo",
            font="arial 10",
        )
        self.text_cdg.place(x=5, y=50)
        self.text_produto = Label(
            self.edts,
            fg="white",
            bg="#151515",
            anchor="center",
            text="Produto",
            font="arial 10",
        )
        self.text_produto.place(x=85, y=50)
        self.text_preco = Label(
            self.edts,
            fg="white",
            bg="#151515",
            anchor="center",
            text="Preço",
            font="arial 10",
        )
        self.text_preco.place(x=350, y=50)
        self.text_qtde = Label(
            self.edts,
            fg="white",
            bg="#151515",
            anchor="center",
            text="QTDE",
            font="arial 10",
        )
        self.text_qtde.place(x=430, y=50)
        self.custo = Label(
            self.edts,
            fg="white",
            bg="#151515",
            anchor="center",
            text="Custo",
            font="arial 10",
        )
        self.custo.place(x=350, y=120)
        self.text_cdg_ent = Label(
            self.edts,
            fg="white",
            bg="#151515",
            anchor="center",
            text="Codigo Entrada",
            font="arial 10",
        )
        self.text_cdg_ent.place(x=5, y=0)
        self.Cdg = Entry(self.edts, validate="key", width=5, font="arial 14")
        self.Cdg.config(validatecommand=(self.Cdg.register(self.validate_entry), "%P"))
        self.Cdg.bind("<KeyPress-c>", lambda event: self.chama_caixa())
        self.Cdg.bind("<KeyPress-v>", lambda event: self.fecha_ajustes())
        self.Cdg.bind("<Return>", lambda event: self.Produto.focus())
        self.Cdg.place(x=5, y=70, height=40)

        self.Produto = Entry(self.edts, width=22, font="arial 14")
        self.Produto.bind("<Return>", lambda event: self.Preco.focus())
        self.Produto.place(x=85, y=70, height=40)

        self.Preco = Entry(self.edts, validate="key", width=5, font="arial 14")
        self.Preco.config(
            validatecommand=(self.Cdg.register(self.validate_entry), "%P")
        )
        self.Preco.bind("<KeyPress-c>", lambda event: self.chama_caixa())
        self.Preco.bind("<KeyPress-v>", lambda event: self.fecha_ajustes())
        self.Preco.bind("<Return>", lambda event: self.Qtde.focus())
        self.Preco.place(x=350, y=70, height=40)
        
        self.Qtde = Entry(self.edts, validate="key", width=5, font="arial 14")
        self.Qtde.config(validatecommand=(self.Cdg.register(self.validate_entry), "%P"))
        self.Qtde.bind("<Return>", lambda event: self.custo.focus())
        self.Qtde.bind("<KeyPress-c>", lambda event: self.chama_caixa())
        self.Qtde.bind("<KeyPress-v>", lambda event: self.fecha_ajustes())
        self.Qtde.place(x=430, y=70, height=40)

        self.cdg_ent = Entry(self.edts, width=5, font="arial 14")
        self.cdg_ent.bind("<Return>", lambda event: self.verifica_codigo_fun())
        self.cdg_ent.bind("<KeyPress-c>", lambda event: self.chama_caixa())
        self.cdg_ent.bind("<KeyPress-v>", lambda event: self.fecha_ajustes())
        self.cdg_ent.place(x=5, y=23, height=25)
        self.custo=Entry(self.edts, validate="key", width=5, font="arial 14")
        self.custo.config(
            validatecommand=(self.Cdg.register(self.validate_entry), "%P")
        )
        self.custo.bind("<KeyPress-c>", lambda event: self.chama_caixa())
        self.custo.bind("<KeyPress-v>", lambda event: self.fecha_ajustes())
        self.custo.bind("<Return>", lambda event: self.add_item())
        self.custo.place(x=350, y=140, height=40)

        self.add_item_bu = Button(
            self.edts,
            width=10,
            text="Adicionar",
            bg="white",
            fg="dimgray",
            font="arial 14",
            foreground="black",
            command=self.add_item,
            bd="0",
        )
        self.add_item_bu.place(x=370, y=460, height=25)

        self.del_item_bu = Button(
            self.edts,
            width=10,
            text="Deletar",
            bg="red",
            fg="dimgray",
            font="arial 14",
            foreground="white",
            command=self.del_item,
            bd="0",
        )
        self.del_item_bu.place(x=370, y=495, height=25)

        self.voltar_edts = Button(
            self.edts,
            width=10,
            text="Voltar",
            bg="red",
            fg="dimgray",
            font="arial 14",
            foreground="white",
            command=self.estoque,
            bd="0",
        )
        self.voltar_edts.place(x=1050, y=480, height=25)

        self.cdg_ent.focus()
        self.mostra_itens()

    def add_item(self):
        cdg_add = self.Cdg.get().replace(",", ".")
        produto_add = self.Produto.get()
        preco_add = self.Preco.get().replace(",", ".")
        qtde_add = self.Qtde.get().replace(",", ".")
        Banco = sqlite3.connect("banco.db")
        cursor = Banco.cursor()
        try:
            if cdg_add == "" or preco_add == "" or produto_add == "" or qtde_add == "":
                messagebox.showinfo(
                    "FALTA DADOS",
                    "Prencha todos os campos para adicionar algum item...",
                )
                self.Produto.focus()

            else:
                cursor.execute("SELECT * FROM Estoque WHERE Codigo=? ", (str(cdg_add)))
                rons = cursor.fetchall()
                if len(rons) >= 1:
                    messagebox.askyesno(
                        "Erro", "Codigo ja existente, Deseja atualiza-lo?"
                    )
                    self.alterar_item()
                else:
                    cursor.execute(
                        "INSERT INTO Estoque VALUES('"
                        + str(cdg_add)
                        + "','"
                        + produto_add
                        + "',"
                        + str(preco_add)
                        + ","
                        + str(qtde_add)
                        + ")"
                    )
                    Banco.commit()
                    self.relod_edt()
                    self.Cdg.focus_get()
                    messagebox.showinfo("Sucesso", "Produto adicionado com sucesso")
        except:
            codigo = self.Cdg.get()
            produto = self.Produto.get()
            preco = self.Preco.get()
            custo = self.custo.get()
            qtde = self.Qtde.get()

            query = "INSERT INTO Estoque (Codigo, PRODUTO, PREÇO, custo, QTDE) VALUES (?, ?, ?, ?, ?)"
            values = (codigo, produto, preco, custo, qtde)

            cursor.execute(query, values)
            Banco.commit()
            self.relod_edt()
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso")
            Banco.close()
        self.cdg_ent.focus()

    def del_item(self):
        cdg = self.Cdg.get()
        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()
        try:
            b.execute("DELETE from Estoque WHERE Codigo=?", (cdg,))
            Banco.commit()
            Banco.close()
            self.relod_edt()
            self.cdg_ent.focus()
            messagebox.showinfo("Sucesso", "Produto deletado com sucesso")

        except:
            messagebox.showinfo("Erro", "Produto nao encontrado")
            self.cdg_ent.focus()

    def alterar_item(self):
        cdg_alt = self.Cdg.get().replace(",", ".")
        produto_alt = self.Produto.get()
        preco_alt = self.Preco.get().replace(",", ".")
        qtde_alt = self.Qtde.get().replace(",", ".")
        custo=self.custo.get().replace(",",".")
        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()
        if messagebox.askyesno("Tem Certeza?", "Deseja realmente alterar o Produto?"):
            b.execute(
                "UPDATE Estoque SET PRODUTO ='"
                + produto_alt
                + "', PREÇO ="
                + str(preco_alt)
                + ",QTDE="
                + str(qtde_alt)
                +",custo="
                +str(custo)
                + " WHERE Codigo="
                + str(cdg_alt)
                + ""
            )
            Banco.commit()
            Banco.close()
            self.relod_edt()

    def mostra_itens(self):
        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()
        estilo1 = ttk.Style()
        estilo1.configure(
            "Treeview",
            font=("Arial", 15),
            background="#9DCFFA",
            foreground="black",
            rowheight=25,
            fieldbackground="#93FDF6",
        )
        self.table1 = ttk.Treeview(self.edts, height=15)
        self.table1.place(x=585, y=10, width=600)
        self.table1["columns"] = ("Codigo", "PRODUTO", "PREÇO", "CUSTO", "QTDE")

        self.table1.column("#0", width=100, minwidth=100)
        self.table1.column("#1", width=200, minwidth=200)
        self.table1.column("#2", width=100, minwidth=100)
        self.table1.column("#3", width=100, minwidth=100)
        self.table1.column("#4", width=100, minwidth=100)

        self.table1.heading("#0", text="Codigo")
        self.table1.heading("#1", text="Produto")
        self.table1.heading("#2", text="Preço")
        self.table1.heading("#3", text="Custo")
        self.table1.heading("#4", text="Quantidade")

        b.execute("SELECT Codigo,PRODUTO,PREÇO,custo,QTDE FROM Estoque")
        rows = b.fetchall()
        for row in rows:
            self.table1.insert(
                parent="",
                index="end",
                text=row[0],
                values=(row[1], row[2], row[3], row[4]),
            )
            self.table1.place(x=585, y=10, width=600)
        Banco.close()

    def execute_itens(self):
        self.edt()

    def _del_usu_(self):
        self.janela_principal.destroy()
        exit(0)

    def limpa_entry(self):
        self.Cdg.delete(0, END)
        self.Produto.delete(0, END)
        self.Preco.delete(0, END)
        self.Qtde.delete(0, END)
        self.custo.delete(0,END)

    def relod_edt(self):
        self.edts.place_forget()
        self.table1.place_forget()
        self.relod_edt1()

    def relod_edt1(self):
        self.edt()
        self.mostra_itens()

    def troca_usu(self):
        self.janela_usu.destroy()
        self.topframe.destroy()
        self.mainframe.destroy()
        self.objetos_login()

    def chama_caixa(self):
        self.janela_usu.destroy()
        self.topframe.destroy()
        self.mainframe.destroy()
        self.principal_frame()

