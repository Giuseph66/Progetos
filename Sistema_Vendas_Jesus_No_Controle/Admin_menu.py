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
            self.janela_principal, width=1550, height=1000, bg="white"
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

        img = PhotoImage(file="ImageTk/Perfil.png")
        """img=img.subsamples(a,b)"""
        self.clientes_bu = Button(
            self.mainframe,
            text="Clientes",
            font="arial 11 bold",
            image=img,
            bd=1,
            command=self.cliente,
            compound=TOP,
        )
        self.clientes_bu.place(x=620, y=27)
        self.clientes_bu.image = img

        img = PhotoImage(file="ImageTk/Funcionario.png")
        img = img.subsample(20)
        self.funcionario_bu = Button(
            self.mainframe,
            text="Funcionario",
            font="arial 11 bold",
            image=img,
            bd=1,
            command=self.funcionario,
            compound=TOP,
        )
        self.funcionario_bu.place(x=720, y=27)
        self.funcionario_bu.image = img

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

        img = PhotoImage(file="ImageTk/itens.png")
        self.pedidos_f = Button(
            self.mainframe,
            text="Pedidos",
            font="arial 11 bold",
            image=img,
            bd=1,
            command=self.Pedidos,
            compound=TOP,
        )
        self.pedidos_f.place(x=47, y=27)
        self.pedidos_f.image = img

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

        img = PhotoImage(file="ImageTk/caixa.png")
        self.caixa = Button(
            self.mainframe,
            text="Caixa",
            font="arial 11 bold",
            image=img,
            bd=1,
            command=self.chama_caixa,
            compound=TOP,
        )
        self.caixa.place(x=510, y=27)
        self.caixa.image = img
        self.funcionario()

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
            "<KeyPress>", lambda event: self.tabela_pesquisa_cdg()
        )
        self.pesquisa_cdg_digito.bind(
            "<KeyPress-a>", lambda event: self.execute_itens()
        )
        self.pesquisa_cdg_digito.bind("<KeyPress-s>", lambda event: self._del_usu_())
        self.pesquisa_cdg_digito.bind("<KeyPress-k>", lambda event: self.cliente())
        self.pesquisa_cdg_digito.place(x=0, y=18, height=25)
        self.pesquisa_nome_testo = Entry(self.table_itens, width=150, bg="white", bd=1)
        self.pesquisa_nome_testo.bind(
            "<Return>", lambda event: self.pesquisa_cdg_digito.focus()
        )
        self.pesquisa_nome_testo.bind(
            "<KeyPress>", lambda event: self.tabela_pesquisa_nome()
        )
        self.pesquisa_nome_testo.place(x=220, y=18, height=25)

        self.pesquisa_cdg_digito.focus()

        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()
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

        b.execute("SELECT Codigo, PRODUTO, PREÇO, QTDE FROM Estoque")
        rows = b.fetchall()
        for row in rows:
            self.table.insert(
                parent="", index="end", text=row[0], values=(row[1], row[2], row[3])
            )
            self.table.place(x=0, y=50, width=1200)
        Banco.close()

        self.edts.place_forget()

    def tabela_pesquisa_cdg(self):
        self.table.destroy()
        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()
        estilo = ttk.Style()
        estilo.configure(
            "Treeview",
            font=("Arial", 15),
            background="#9DCFFA",
            foreground="black",
            rowheight=25,
            fieldbackground="#93FDF6",
        )
        self.table_1 = ttk.Treeview(self.table_itens, height=800)
        self.table_1.place(x=0, y=50, width=1200)
        self.table_1["columns"] = ("Codigo", "PRODUTO", "PREÇO", "QTDE")

        self.table_1.column("#0", width=1, minwidth=1)
        self.table_1.column("#1", width=50, minwidth=20)
        self.table_1.column("#2", width=20, minwidth=20)
        self.table_1.column("#3", width=50, minwidth=20)

        self.table_1.heading("#0", text="Codigo")
        self.table_1.heading("#1", text="Produto")
        self.table_1.heading("#2", text="Preço")
        self.table_1.heading("#3", text="Quantidade")

        b.execute(
            "SELECT Codigo, PRODUTO, PREÇO, QTDE FROM Estoque WHERE Codigo=?",
            (self.pesquisa_cdg_digito.get(),),
        )
        rows = b.fetchall()
        for row in rows:
            self.table_1.insert(
                parent="", index="end", text=row[0], values=(row[1], row[2], row[3])
            )
            self.table_1.place(x=0, y=50, width=1200)
        Banco.close()

    def limpa_pesquisa(self):
        self.pesquisa_cdg_digito.delete(0, END)
        self.pesquisa_nome_testo.delete(0, END)

    def tabela_pesquisa_nome(self):
        self.table.destroy()
        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()
        estilo = ttk.Style()
        estilo.configure(
            "Treeview",
            font=("Arial", 15),
            background="#9DCFFA",
            foreground="black",
            rowheight=25,
            fieldbackground="#93FDF6",
        )
        self.table_2 = ttk.Treeview(self.table_itens, height=800)
        self.table_2.place(x=0, y=50, width=1200)
        self.table_2["columns"] = ("Codigo", "PRODUTO", "PREÇO", "QTDE")

        self.table_2.column("#0", width=1, minwidth=1)
        self.table_2.column("#1", width=50, minwidth=20)
        self.table_2.column("#2", width=20, minwidth=20)
        self.table_2.column("#3", width=50, minwidth=20)

        self.table_2.heading("#0", text="Codigo")
        self.table_2.heading("#1", text="Produto")
        self.table_2.heading("#2", text="Preço")
        self.table_2.heading("#3", text="Quantidade")

        b.execute(
            "SELECT Codigo, PRODUTO, PREÇO, QTDE FROM Estoque WHERE Codigo=?",
            (self.pesquisa_nome_testo.get(),),
        )
        rows = b.fetchall()
        for row in rows:
            self.table_2.insert(
                parent="", index="end", text=row[0], values=(row[1], row[2], row[3])
            )
            self.table_2.place(x=0, y=50, width=1200)
        Banco.close()

    def Pedidos(self):
        img = PhotoImage(file="ImageTk/confg.png")
        self.table_pedidos = LabelFrame(
            self.janela_usu, width=1250, height=640, bg="black"
        )
        self.table_pedidos.place(x=(1550 - 1250)/2, y=205)
        self.table_pedidos_add = Button(
            self.table_pedidos, image=img, bd=0, compound=TOP
        )
        self.table_pedidos_add.place(x=1220, y=0)
        self.table_itens_add.image = img
        if self.table_itens.winfo_exists:
            self.table_itens.place_forget()
        if self.table_clientes.winfo_exists:
            self.table_clientes.place_forget()
        if self.table_vendas.winfo_exists:
            self.table_vendas.place_forget()
        if self.table_funcionarios.winfo_exists:
            self.table_funcionarios.place_forget()
    def funcionario(self):
        img = PhotoImage(file="ImageTk/confg.png")
        self.table_funcionarios = LabelFrame(
            self.janela_usu, width=1250, height=640, bg="green"
        )
        self.table_funcionarios.place(x=(1550 - 1250)/2, y=205)

        self.conexão = sqlite3.connect('banco.db')
        self.cursor = self.conexão.cursor()
        self.calen=Calendar(self.table_funcionarios, bordercolor="#014502",font="arial 12 bold")
        self.calen["background"] = "#014502" 
        self.calen.place(x=945,y=0,width=300,height=250)
        self.calen.bind("<<CalendarSelected>>", lambda event:self.limpa_fun())
        self.cursor.execute("SELECT nome FROM Pessoas")
        self.dados = self.cursor.fetchall()
        self.combo_func=ttk.Combobox(self.table_funcionarios,justify="center",font="arial 12 bold",width=41)
        self.combo_func["values"] = [row[0] for row in self.dados]
        self.combo_func.bind("<<ComboboxSelected>>",lambda event:self.atualisa_func())
        self.combo_func.set("Funcionario")
        self.combo_func.place(x=55,y=10)
        self.complemento_calen()
        #self.but_confia=Button(self.table_funcionarios,text=)
        if self.table_itens.winfo_exists:
            self.table_itens.place_forget()
        if self.table_clientes.winfo_exists:
            self.table_clientes.place_forget()
        if self.table_vendas.winfo_exists:
            self.table_vendas.place_forget()
        if self.table_pedidos.winfo_exists:
            self.table_pedidos.place_forget()
    def limpa_fun(self):
        self.ponto.destroy()
        self.ponto_2.destroy()
        self.complemento_calen()
        self.atualisa_func()
    def complemento_calen(self):
        self.data=self.calen.get_date()
        self.dia,self.mes,self.ano=self.data.split("/")
        self.dia_semana = calendar.weekday(int(self.ano),int(self.mes),int(self.dia))
        self.dias_da_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        self.meses_do_ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        #messagebox.showinfo("sl",f"O dia da semana é {self.dias_da_semana[self.dia_semana]}")
        self.quantidade_de_dias = calendar.monthrange(int(self.ano), int(self.mes))[1]
        self.txtx=Label(self.table_funcionarios,text="Manhâ:",fg="white",width=6,font="arial 12 bold",bg="green",bd=2)
        self.txtx.place(x=980,y=250)
        self.txtx=Label(self.table_funcionarios,text="Almoço:",fg="black",width=6,font="arial 12 bold",bg="green",bd=2)
        self.txtx.place(x=1070,y=250)
        self.txtx=Label(self.table_funcionarios,text="Tarde:",fg="white",width=6,font="arial 12 bold",bg="green",bd=2)
        self.txtx.place(x=1150,y=250)
        self.txtx=Label(self.table_funcionarios,text="Entra:",fg="white",width=6,font="arial 12 bold",bg="green",bd=2)
        self.txtx.place(x=945,y=270)
        self.txtx=Label(self.table_funcionarios,text="Sai:",fg="white",width=6,font="arial 12 bold",bg="green",bd=2)
        self.txtx.place(x=1015,y=270)
        self.txtx=Label(self.table_funcionarios,text="Entra:",fg="white",width=6,font="arial 12 bold",bg="green",bd=2)
        self.txtx.place(x=1115,y=270)
        self.txtx=Label(self.table_funcionarios,text="Sai:",fg="white",width=6,font="arial 12 bold",bg="green",bd=2)
        self.txtx.place(x=1185,y=270)
        self.ehora_m=Entry(self.table_funcionarios,width=6,font="arial 12 bold",bg="#ded63c",bd=2)
        self.ehora_m.bind("<Return>", lambda event:self.shora_m.focus())
        self.ehora_m.bind("<KeyPress-0>", lambda event:self.auto())
        self.ehora_m.bind("<KeyPress-F>", lambda event:self.auto_O())
        self.ehora_m.place(x=945,y=290)
        self.shora_m=Entry(self.table_funcionarios,width=6,font="arial 12 bold",bg="#ded63c",bd=2)
        self.shora_m.bind("<Return>", lambda event:self.ehora_t.focus())
        self.shora_m.place(x=1015,y=290)
        self.ehora_t=Entry(self.table_funcionarios,width=6,font="arial 12 bold",bg="#ded63c",bd=2)
        self.ehora_t.bind("<Return>", lambda event:self.shora_t.focus())
        self.ehora_t.place(x=1115,y=290)
        self.shora_t=Entry(self.table_funcionarios,width=6,font="arial 12 bold",bg="#ded63c",bd=2)
        self.shora_t.bind("<Return>", lambda event:self.cadas_ponto())
        self.shora_t.place(x=1185,y=290)
        self.slv_hrs_butao=Button(self.table_funcionarios,width=6,command=self.cadas_ponto,text="Salvar",font="arial 12 bold",bg="white",bd=2)
        self.slv_hrs_butao.place(x=1150,y=320)
        self.txtx=Label(self.table_funcionarios,text="Salário:",fg="white",width=6,font="arial 12 bold",bg="green",bd=2)
        self.txtx.place(x=475,y=10)
        self.txtx=Label(self.table_funcionarios,text="Horas trabalhadas:",fg="white",width=20,font="arial 12 bold",bg="green",bd=2)
        self.txtx.place(x=610,y=10)
        self.salario=Entry(self.table_funcionarios,width=6,font="arial 12 bold",bg="#70f06c",bd=2)
        self.salario.bind("<Return>", lambda event:self.shora_t.focus())
        self.salario.place(x=540,y=10)
        self.horas_trabalhadas=Entry(self.table_funcionarios,width=6,font="arial 12 bold",bg="#70f06c",bd=2)
        self.horas_trabalhadas.bind("<Return>", lambda event:self.shora_t.focus())
        self.horas_trabalhadas.place(x=800,y=10)
        self.atalio=Button(self.table_funcionarios,width=6,command=self.auto,text="Auto",font="arial 12 bold",bg="green",bd=2)
        self.atalio.place(x=1000,y=320)
        
        self.pontos()
    def atualisa_func(self):
        self.sal=self.salario.get()
        self.hr=self.horas_trabalhadas.get()
        self.funcionario_combo=self.combo_func.get()
        dia_sem=self.dias_da_semana[self.dia_semana]
        self.cursor.execute("SELECT salario,hora FROM ponto WHERE funcionario=?",(self.funcionario_combo,))
        sla=self.cursor.fetchone()
        if sla is not None:
            salario,hora=sla
            self.salario.delete(0,END)
            self.horas_trabalhadas.delete(0,END)
            self.salario.insert(0,str(salario))
            self.horas_trabalhadas.insert(0,str(hora))
        else:
            self.salario.delete(0,END)
            self.horas_trabalhadas.delete(0,END)

        self.cursor.execute("SELECT entri_manha, sai_manha, entri_tarde, sai_tarde FROM ponto WHERE data=? AND funcionario=?", (self.data, self.funcionario_combo))
        sla1=self.cursor.fetchone()
        if sla1 is not None:
            entri_manha,sai_manha,entri_tarde,sai_tarde=sla1
            self.ehora_m.delete(0,END)
            self.shora_m.delete(0,END)
            self.ehora_t.delete(0,END)
            self.shora_t.delete(0,END)
            if entri_manha is not None:
                self.ehora_m.insert(0,entri_manha)
            if sai_manha is not None:
                self.shora_m.insert(0,sai_manha)
            if entri_tarde is not None:
                self.ehora_t.insert(0,entri_tarde)
            if sai_tarde is not None:
                self.shora_t.insert(0,sai_tarde)
        else:
            self.cursor.execute("INSERT INTO ponto (data,funcionario,salario,hora,dia_semana) VALUES(?,?,?,?,?)", (self.data, self.funcionario_combo,self.sal,self.hr,dia_sem))
            self.conexão.commit()
        
        self.ponto.destroy()
        self.ponto_2.destroy()
        self.pontos()
    def cadas_ponto(self):
        self.entri_m=self.ehora_m.get()
        self.sai_m=self.shora_m.get()
        self.entri_t=self.ehora_t.get()
        self.sai_t=self.shora_t.get()
        self.cursor.execute("UPDATE ponto SET entri_manha=?, sai_manha=?, entri_tarde=?, sai_tarde=? WHERE data=? AND funcionario=?", (self.entri_m,self.sai_m,self.entri_t,self.sai_t,self.data, self.funcionario_combo))
        self.conexão.commit()
        messagebox.showinfo("Salvo",f"Ponto do dia {self.data} foi salvo!!!")
        self.limpa_fun()
        
    def auto(self):
        sal=self.ehora_m.get()
        if sal=="":
            self.ehora_m.delete(0,END)
            self.shora_m.delete(0,END)
            self.ehora_t.delete(0,END)
            self.shora_t.delete(0,END)
            self.ehora_m.insert(0,"7:0")
            self.shora_m.insert(0,"11:00")
            self.ehora_t.insert(0,"13:00")
            self.shora_t.insert(0,"18:00")
            self.shora_t.focus()
    def auto_O(self):
        sal=self.ehora_m.get()
        if sal =="":
            self.shora_m.delete(0,END)
            self.ehora_t.delete(0,END)
            self.shora_t.delete(0,END)
            self.shora_m.insert(0,"O")
            self.ehora_t.insert(0,"L")
            self.shora_t.insert(0,"G")
            self.shora_t.focus()
    def pontos(self):
        if hasattr(self, 'fram_hole'):
            if self.fram_hole is not None:
                self.fram_hole.place_forget() 
        self.funcionario_combo=self.combo_func.get()
        self.ponto=LabelFrame(self.table_funcionarios,width=450,height=585,bg="#ded63c",bd=2)
        self.ponto.place(x=5,y=45)
        self.ponto_2=LabelFrame(self.table_funcionarios,width=450,height=585,bg="#ded63c",bd=2)
        self.ponto_2.place(x=475,y=45)
        mes_fun=StringVar(value=self.meses_do_ano[int(self.mes)-1])
        self.mes_fun=Entry(self.ponto,textvariable=mes_fun,justify="center",font="arial 12 bold",bg="#f0ea7f",fg="black",width=34)
        self.mes_fun.place(x=70,y=50)
        mes_fun=StringVar(value=self.meses_do_ano[int(self.mes)-1])
        self.mes_fun=Entry(self.ponto_2,textvariable=mes_fun,justify="center",font="arial 12 bold",bg="#f0ea7f",fg="black",width=34)
        self.mes_fun.place(x=70,y=50)
        self.calculu_buton=Button(self.ponto,width=30,command=self.calculo,text="Calcular Horas extras",font="arial 12 bold",bg="green",bd=2)
        self.calculu_buton.place(x=70,y=10)
        self.calculu_buton2=Button(self.ponto_2,width=30,command=self.calculo,text="Calcular Horas extras",font="arial 12 bold",bg="green",bd=2)
        self.calculu_buton2.place(x=70,y=10)
        self.calculu_buton3=Button(self.ponto_2,width=30,command=self.calculo,text="Calcular Horas extras",font="arial 12 bold",bg="green",bd=2)
        self.calculu_buton3.place(x=70,y=540)
        if self.quantidade_de_dias==30:
            self.calculu_buton4=Button(self.ponto,width=30,command=self.calculo,text="Calcular Horas extras",font="arial 12 bold",bg="green",bd=2)
            self.calculu_buton4.place(x=70,y=540)
        
        cont=1
        y=80
        dia_semana = calendar.weekday(int(self.ano),int(self.mes),int(cont))
        dias=self.dias_da_semana[dia_semana]
        mes_fun=StringVar(value=cont)
        mes_fun1=StringVar(value=cont)
        mes_fun2=StringVar(value=cont)
        mes_fun3=StringVar(value=cont)
        mes_fun4=StringVar(value=f"0{cont} : {dias[0]}")
        self.dias_da_semana_Cores = ["#fa2007", "#fa7107", "#f4fa50", "#75ffd1", "#75dfff", "#64fab1","#31fa2a"]
        for _ in range(int((self.quantidade_de_dias+1)/2)):
            dia_semana = calendar.weekday(int(self.ano),int(self.mes),int(cont))
            cor=self.dias_da_semana_Cores[dia_semana]
            dias=self.dias_da_semana[dia_semana]
            if cont<=9:
                self.data_atu=f"0{str(cont)}/{self.mes}/{self.ano}"
                mes_fun4=StringVar(value=f"0{cont} : {dias[0]}")
            else:
                self.data_atu=f"{str(cont)}/{self.mes}/{self.ano}"
                mes_fun4=StringVar(value=f"{cont} : {dias[0]}")
            self.ehora_m_o=Entry(self.ponto,textvariable=mes_fun,justify="center",font="arial 12 bold",bg=cor,fg="black",width=10)
            self.ehora_m_o.place(x=2,y=y)
            self.shora_m_o=Entry(self.ponto,textvariable=mes_fun1,justify="center",font="arial 12 bold",bg=cor,fg="black",width=10)
            self.shora_m_o.place(x=99,y=y)
            self.ehora_t_o=Entry(self.ponto,textvariable=mes_fun2,justify="center",font="arial 12 bold",bg=cor,fg="black",width=10)
            self.ehora_t_o.place(x=197,y=y)
            self.shora_t_o=Entry(self.ponto,textvariable=mes_fun3,justify="center",font="arial 12 bold",bg=cor,fg="black",width=10)
            self.shora_t_o.place(x=296,y=y)
            self.ale=Entry(self.ponto,textvariable=mes_fun4,font="arial 12 bold",bg=cor,fg="black",width=5)
            self.ale.place(x=395,y=y)
            self.cursor.execute("SELECT entri_manha, sai_manha, entri_tarde, sai_tarde FROM ponto WHERE data=? AND funcionario=?", (str(self.data_atu), self.funcionario_combo))
            sla1=self.cursor.fetchone()
            if sla1 is not None:
                entri_manha,sai_manha,entri_tarde,sai_tarde=sla1
                if entri_manha is not None:
                    self.ehora_m_o.delete(0,END)
                    self.ehora_m_o.insert(0,entri_manha)
                if sai_manha is not None:
                    self.shora_m_o.delete(0,END)
                    self.shora_m_o.insert(0,sai_manha)
                if entri_tarde is not None:
                    self.ehora_t_o.delete(0,END)
                    self.ehora_t_o.insert(0,entri_tarde)
                if sai_tarde is not None:
                    self.shora_t_o.delete(0,END)
                    self.shora_t_o.insert(0,sai_tarde)
            cont+=1
            mes_fun=StringVar(value=cont)
            mes_fun1=StringVar(value=cont)
            mes_fun2=StringVar(value=cont)
            mes_fun3=StringVar(value=cont)
            y+=30
        y=80
        for _ in range(int((self.quantidade_de_dias)/2)):
            dia_semana = calendar.weekday(int(self.ano),int(self.mes),int(cont))
            cor=self.dias_da_semana_Cores[dia_semana]
            dias=self.dias_da_semana[dia_semana]
            if cont<=9:
                self.data_atu=f"0{str(cont)}/{self.mes}/{self.ano}"
                mes_fun4=StringVar(value=f"{cont} : {dias[0]}")
            else:
                self.data_atu=f"{str(cont)}/{self.mes}/{self.ano}"
                mes_fun4=StringVar(value=f"{cont} : {dias[0]}")
            self.ehora_m_o=Entry(self.ponto_2,textvariable=mes_fun,justify="center",font="arial 12 bold",bg=cor,fg="black",width=10)
            self.ehora_m_o.place(x=2,y=y)
            self.shora_m_o=Entry(self.ponto_2,textvariable=mes_fun1,justify="center",font="arial 12 bold",bg=cor,fg="black",width=10)
            self.shora_m_o.place(x=99,y=y)
            self.ehora_t_o=Entry(self.ponto_2,textvariable=mes_fun2,justify="center",font="arial 12 bold",bg=cor,fg="black",width=10)
            self.ehora_t_o.place(x=197,y=y)
            self.shora_t_o=Entry(self.ponto_2,textvariable=mes_fun3,justify="center",font="arial 12 bold",bg=cor,fg="black",width=10)
            self.shora_t_o.place(x=296,y=y)
            self.ale=Entry(self.ponto_2,textvariable=mes_fun4,font="arial 12 bold",bg=cor,fg="black",width=5)
            self.ale.place(x=395,y=y)
            self.cursor.execute("SELECT entri_manha, sai_manha, entri_tarde, sai_tarde FROM ponto WHERE data=? AND funcionario=?", (str(self.data_atu), self.funcionario_combo))
            sla1=self.cursor.fetchone()
            if sla1 is not None:
                entri_manha,sai_manha,entri_tarde,sai_tarde=sla1
                if entri_manha is not None:
                    self.ehora_m_o.delete(0,END)
                    self.ehora_m_o.insert(0,entri_manha)
                if sai_manha is not None:
                    self.shora_m_o.delete(0,END)
                    self.shora_m_o.insert(0,sai_manha)
                if entri_tarde is not None:
                    self.ehora_t_o.delete(0,END)
                    self.ehora_t_o.insert(0,entri_tarde)
                if sai_tarde is not None:
                    self.shora_t_o.delete(0,END)
                    self.shora_t_o.insert(0,sai_tarde)
            cont+=1
            y+=30
            mes_fun=StringVar(value=cont)
            mes_fun1=StringVar(value=cont)
            mes_fun2=StringVar(value=cont)
            mes_fun3=StringVar(value=cont)
        
        self.combo_func.focus()
    def calculo(self):
        self.calculu_buton.destroy()
        self.calculu_buton2.destroy()
        self.calculu_buton3.destroy()
        if self.quantidade_de_dias==30:
            self.calculu_buton4.destroy()
        self.br_holidays = holidays.BR()
        self.sal=float(self.salario.get())
        self.hr=float(self.horas_trabalhadas.get())
        cont=0
        horas_extras60=0
        horas_extras110=0
        folga_don=False
        for _ in range(int(self.quantidade_de_dias+1)):
            if cont<=9:
                self.data_atu_m=f"0{str(cont)}/{self.mes}/{self.ano}"
                self.data_atu_f=f"{self.ano}/{self.mes}/0{str(cont)}"
            else:
                self.data_atu_m=f"{str(cont)}/{self.mes}/{self.ano}"
                self.data_atu_f=f"{self.ano}/{self.mes}/{str(cont)}"
            self.cursor.execute("SELECT entri_manha, sai_manha, entri_tarde, sai_tarde,dia_semana FROM ponto WHERE data=? AND funcionario=?", (str(self.data_atu_m), self.funcionario_combo))
            sla1=self.cursor.fetchone()
            cont+=1           
            if sla1 is not None :
                entri_manha,sai_manha,entri_tarde,sai_tarde,dia_semana=sla1
                
                if entri_manha is not None and entri_manha not in("","F", "O", "L", "G"):
                    ehorasm, eminutosm = entri_manha.split(":")
                else:
                    ehorasm, eminutosm = 0,0
                if sai_manha is not None and sai_manha not in("","F", "O", "L", "G"):
                    shorasm, sminutosm = sai_manha.split(":")
                else:
                    shorasm, sminutosm =0,0
                if entri_tarde is not None and entri_tarde not in("","F", "O", "L", "G"):
                    ehorast, eminutost = entri_tarde.split(":")
                else:
                    ehorast, eminutost =0,0
                if sai_tarde is not None and sai_tarde not in("","F", "O", "L", "G"):
                    shorast, sminutost = sai_tarde.split(":")
                else:
                    shorast, sminutost = 0,0

                eminutos_totalm = float(ehorasm) * 60 + float(eminutosm)
                sminutos_totalm = float(shorasm) * 60 + float(sminutosm)
                eminutos_totalt = float(ehorast) * 60 + float(eminutost)
                sminutos_totalt = float(shorast) * 60 + float(sminutost)

                horas_d = (sminutos_totalm-eminutos_totalm)+(sminutos_totalt-eminutos_totalt)
                    #self.br_holidays.get(self.data_atu_f)
                seg_sabado= ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado")

                if dia_semana in seg_sabado:
                    if self.data_atu_f in self.br_holidays:
                        horas_extras110+=horas_d
                    else:
                        horas_extras60_m = horas_d - 480 if horas_d > 480 else 0
                elif dia_semana == "Domingo":
                    if entri_manha == "F" and sai_manha == "O" and entri_tarde == "L" and sai_tarde == "G":
                        folga_don=True
                    else:
                        horas_extras60_m = horas_d - 240 if horas_d > 240 else 0
                else:
                    horas_extras60_m = 0

                if horas_extras60_m > 0:
                    horas_extras60+=horas_extras60_m
        if folga_don==False:
            horas_extras110+=300
            horas_extras60-=60
        self.vlr_hr=self.sal/self.hr
        vlr_hr_60=1.6*self.vlr_hr
        vlr_hr_110=2.1*self.vlr_hr
        self.txtx=Label(self.ponto,text=f"Horas extras 60% = {horas_extras60/60:.2f} : {(horas_extras60/60)*vlr_hr_60 :.2f} R$",fg="black",width=30,font="arial 12 bold",bg="#f0ea7f",bd=3)
        self.txtx.place(x=70,y=10)
        self.txtx=Label(self.ponto_2,text=f"Horas extras 110% = {horas_extras110/60:.2f} : {(horas_extras110/60)*vlr_hr_110 :.2f} R$",fg="black",width=30,font="arial 12 bold",bg="#f0ea7f",bd=3)
        self.txtx.place(x=70,y=10)
        cal = calendar.monthcalendar(int(self.ano),int( self.mes))
        domingos = 0
        feriados = 0
        for semana in cal:
            for dia in semana:
                if dia != 0:
                    data = date(int(self.ano),int( self.mes), dia)
                    if data.weekday() == 6:  
                        domingos += 1

                    if data in self.br_holidays:
                        feriados += 1

        dias_inuteis=domingos+feriados
        dias_uteis=self.quantidade_de_dias-dias_inuteis
        
        valor60=(horas_extras60/60) * vlr_hr_60
        valor110=(horas_extras110/60) * vlr_hr_110
        reflexos = (((horas_extras60/60) * vlr_hr_60) + ((horas_extras110/60) * vlr_hr_110)) / dias_uteis * dias_inuteis
        self.txtx=Label(self.ponto_2,text=f"Reflexos de Horas extras  = {(((horas_extras60/60) * vlr_hr_60) + ((horas_extras110/60) * vlr_hr_110)) / dias_uteis :.2f} : {reflexos :.2f} R$",fg="black",width=40,font="arial 12 bold",bg="#f0ea7f",bd=3)
        self.txtx.place(x=20,y=540)
        if self.quantidade_de_dias==30:
            self.txtx=Label(self.ponto,text=f"Reflexos de Horas extras  = {(((horas_extras60/60) * vlr_hr_60) + ((horas_extras110/60) * vlr_hr_110)) / dias_uteis :.2f} : {reflexos :.2f} R$",fg="black",width=40,font="arial 12 bold",bg="#f0ea7f",bd=3)
            self.txtx.place(x=20,y=540)

        self.fram_hole=LabelFrame(self.table_funcionarios,width=300,height=200,bg="#d5edce",bd=3)
        self.fram_hole.place(x=945,y=380)
        self.fram_hole1=LabelFrame(self.fram_hole,width=150,height=200,bg="#d5edce",bd=3)
        self.fram_hole1.place(x=0,y=0)
        self.fram_hole2=LabelFrame(self.fram_hole,width=150,height=200,bg="#d5edce",bd=3)
        self.fram_hole2.place(x=150,y=0)
        txtx_sla =Label(self.fram_hole1, text=f"Salario... Horas = ",  width=15, font="arial 10 bold", bg="#cde8c5",bd=3)
        txtx_sla.place(x=0, y=0)
        txtx_sla=Label(self.fram_hole1,text=f"Extras 60% = ",width=15,font="arial 10 bold",bg="#cde8c5",bd=3)
        txtx_sla.place(x=0,y=25)
        txtx_sla=Label(self.fram_hole1,text=f"Extras 110% = ",width=15,font="arial 10 bold",bg="#cde8c5",bd=3)
        txtx_sla.place(x=0,y=50)
        txtx_sla=Label(self.fram_hole1,text=f"Reflexos Extras = ",width=15,font="arial 10 bold",bg="#cde8c5",bd=3)
        txtx_sla.place(x=0,y=75)
        txtx_sla=Label(self.fram_hole1,text=f"INSS  = ",width=15,font="arial 10 bold",bg="#cde8c5",bd=3)
        txtx_sla.place(x=0,y=100)
        txtx_sla=Label(self.fram_hole1,text=f"Salario - INSS =",width=12,font="arial 12 bold",bg="#cde8c5",bd=3)
        txtx_sla.place(x=0,y=150)
        txtx_sla =Label(self.fram_hole2, text=f"{self.hr} Hrs | {self.sal} R$",  width=15, font="arial 10 bold", bg="#cde8c5",bd=3, )
        txtx_sla.place(x=0, y=0)
        txtx_sla=Label(self.fram_hole2,text=f"{horas_extras60/60:.2f} Hrs | {(horas_extras60/60)*vlr_hr_60 :.2f} R$",width=15,font="arial 10 bold",bg="#cde8c5",bd=3)
        txtx_sla.place(x=0,y=25)
        txtx_sla=Label(self.fram_hole2,text=f"{horas_extras110/60:.2f} Hrs | {(horas_extras110/60)*vlr_hr_110 :.2f} R$",width=15,font="arial 10 bold",bg="#cde8c5",bd=3)
        txtx_sla.place(x=0,y=50)
        txtx_sla=Label(self.fram_hole2,text=f"{(((horas_extras60/60) * vlr_hr_60) + ((horas_extras110/60) * vlr_hr_110)) / dias_uteis :.2f} Hrs | {reflexos :.2f} R$",width=15,font="arial 10 bold",bg="#cde8c5",bd=3)
        txtx_sla.place(x=0,y=75)
        txtx_sla=Label(self.fram_hole2,text=f"  7.92 % | {(valor110+valor60+self.sal+reflexos)*(7.92/100):.2f} R$",width=15,font="arial 10 bold",bg="#cde8c5",bd=3)
        txtx_sla.place(x=10,y=100)
        txtx_sla=Label(self.fram_hole2,text=f"{(valor110+valor60+self.sal+reflexos)-((valor110+valor60+self.sal+reflexos)*(7.92/100)):.2f} R$",width=15,font="arial 12 bold",bg="#cde8c5",bd=3)
        txtx_sla.place(x=0,y=150)

        
        
    def cliente(self):
        img = PhotoImage(file="ImageTk/add_usu.png")
        self.table_clientes = LabelFrame(
            self.janela_usu, width=1250, height=640, bg="blue"
        )
        self.table_clientes.place(x=(1550 - 1250)/2, y=205)
        self.clientes_add = Button(
            self.table_clientes, image=img, bd=0, compound=TOP,command=self.cadastro_cliente
        )
        self.clientes_add.place(x=1220, y=0)
        self.table_itens_add.image = img

        self.nome_cli_frame=Label(self.table_clientes,font="Arial 12 bold",text="Nome Cliente",bd=0,bg="cyan",foreground="black")
        self.nome_cli_frame.place(x=255,y=5)
        self.nome_clie_freme_entry=Entry(self.table_clientes,font="Arial 10 bold",bd=1,foreground="black",width=85)
        self.nome_clie_freme_entry.bind("<Return>",lambda event:self.vazio_nome_cli())
        self.nome_clie_freme_entry.place(x=5,y=25,height=20)


        self.nome_func_frame=Label(self.table_clientes,font="Arial 12 bold",text="Nome Funcionario",bd=0,bg="cyan",foreground="black")
        self.nome_func_frame.place(x=855,y=5)
        self.nome_func_frame_entry=Entry(self.table_clientes,font="Arial 10 bold",bd=1,foreground="black",width=85)
        self.nome_func_frame_entry.bind("<Return>",lambda event:self.vazio_nome_func())
        self.nome_func_frame_entry.place(x=610,y=25,height=20)

        
        img = PhotoImage(file="ImageTk/pesquisa_cli.png")
        self.pesquisa_func=Button(self.table_clientes, image=img, bd=0, compound=TOP,command=self.cadastro_cliente)
        self.pesquisa_func.place(x=1183,y=50)
        self.pesquisa_cli=Button(self.table_clientes, image=img, bd=0, compound=TOP,command=self.cadastro_cliente)
        self.pesquisa_cli.place(x=578,y=50)
        
        self.nome_clie_freme_entry.focus()

        if self.table_itens.winfo_exists:
            self.table_itens.place_forget()
        if self.table_pedidos.winfo_exists:
            self.table_pedidos.place_forget()
        if self.table_vendas.winfo_exists:
            self.table_vendas.place_forget()
        if self.table_funcionarios.winfo_exists:
            self.table_funcionarios.place_forget()

    def vazio_nome_cli(Self):
        nome_clie=Self.nome_clie_freme_entry.get()
        if nome_clie=="":
            Self.nome_func_frame_entry.focus()
        else:
            messagebox.showinfo("atoa")

    def vazio_nome_func(Self):
        nome_fun=Self.nome_func_frame_entry.get()
        if nome_fun=="":
            Self.nome_clie_freme_entry.focus()
        else:
            messagebox.showinfo("atoa")

    def cadastro_cliente(self):
        self.frame_cli=LabelFrame(self.table_clientes,bd=1,bg="cyan",width=1200,height=800)
        self.frame_cli.place(x=5,y=0)
        self.nome_cli=Label(self.frame_cli,font="Arial 12 bold",text="Nome",bd=0,bg="cyan",foreground="black")
        self.nome_cli.place(x=0,y=0)
        self.tell_clie=Label(self.frame_cli,font="Arial 12 bold",text="N° Celular",bd=0,bg="cyan",foreground="black")
        self.tell_clie.place(x=200,y=0)
        self.gmail_clie=Label(self.frame_cli,font="Arial 12 bold",text="Gmail",bd=0,bg="cyan",foreground="black")
        self.gmail_clie.place(x=300,y=0)
        self.nome_fantazia_clie=Label(self.frame_cli,font="Arial 12 bold",text="Apelido",bd=0,bg="cyan",foreground="black")
        self.nome_fantazia_clie.place(x=550,y=0)
        self.cpf_clie=Label(self.frame_cli,font="Arial 12 bold",text="CPF",bd=0,bg="cyan",foreground="black")
        self.cpf_clie.place(x=700,y=0)
        self.rg_clie=Label(self.frame_cli,font="Arial 12 bold",text="RG",bd=0,bg="cyan",foreground="black")
        self.rg_clie.place(x=850,y=0)
        self.ou_clie=Label(self.frame_cli,font="Arial 12 bold",text="Ou",bd=0,bg="cyan",foreground="black")
        self.ou_clie.place(x=950,y=0)
        self.cnpj_clie=Label(self.frame_cli,font="Arial 12 bold",text="CNPJ",bd=0,bg="cyan",foreground="black")
        self.cnpj_clie.place(x=1000,y=0)
        self.nome_clie_entry=Entry(self.frame_cli,font="Arial 10 bold",bd=1,foreground="black",width=25)
        self.nome_clie_entry.bind("<Return>",lambda event:self.tell_clie_entry.focus())
        self.nome_clie_entry.place(x=0,y=20,height=20)
        self.tell_clie_entry=Entry(self.frame_cli,font="Arial 10 bold",bd=1,foreground="black",width=13)
        self.tell_clie_entry.bind("<Return>",lambda event:self.gmail_clie_entry.focus())
        self.tell_clie_entry.place(x=200,y=20,height=20)
        self.gmail_clie_entry=Entry(self.frame_cli,font="Arial 10 bold",bd=1,foreground="black",width=30)
        self.gmail_clie_entry.bind("<Return>",lambda event:self.nome_fake_clie_entry.focus())
        self.gmail_clie_entry.place(x=300,y=20,height=20)
        self.nome_fake_clie_entry=Entry(self.frame_cli,font="Arial 10 bold",bd=1,foreground="black",width=20)
        self.nome_fake_clie_entry.bind("<Return>",lambda event:self.cpf_clie_entry.focus())
        self.nome_fake_clie_entry.place(x=550,y=20,height=20)
        self.cpf_clie_entry=Entry(self.frame_cli,font="Arial 10 bold",bd=1,foreground="black",width=20)
        self.cpf_clie_entry.bind("<Return>",lambda event:self.rg_clie_entry.focus())
        self.cpf_clie_entry.place(x=700,y=20,height=20)
        self.rg_clie_entry=Entry(self.frame_cli,font="Arial 10 bold",bd=1,foreground="black",width=20)
        self.rg_clie_entry.bind("<Return>",lambda event:self.cnpj_clie_entry.focus())
        self.rg_clie_entry.place(x=850,y=20,height=20)
        self.cnpj_clie_entry=Entry(self.frame_cli,font="Arial 10 bold",bd=1,foreground="black",width=25)
        self.cnpj_clie_entry.bind("<Return>",lambda event:self.Bairro_clie_entry.focus())
        self.cnpj_clie_entry.place(x=1000,y=20,height=20)
        self.endereço_cli=Label(self.frame_cli,font="Arial 15 bold",text="Endereço",bd=0,bg="cyan",foreground="black")
        self.endereço_cli.place(x=0,y=50)
        self.Bairro_clie=Label(self.frame_cli,font="Arial 12 bold",text="Bairro",bd=0,bg="cyan",foreground="black")
        self.Bairro_clie.place(x=0,y=80)
        self.Rua_clie=Label(self.frame_cli,font="Arial 12 bold",text="Rua",bd=0,bg="cyan",foreground="black")
        self.Rua_clie.place(x=300,y=80)
        self.N_casa_clie=Label(self.frame_cli,font="Arial 12 bold",text="N° Casa",bd=0,bg="cyan",foreground="black")
        self.N_casa_clie.place(x=600,y=80)
        self.complemento_clie=Label(self.frame_cli,font="Arial 12 bold",text="Complemento",bd=0,bg="cyan",foreground="black")
        self.complemento_clie.place(x=700,y=80)       
        self.Bairro_clie_entry=Entry(self.frame_cli,font="Arial 10 bold",bd=1,foreground="black",width=30)
        self.Bairro_clie_entry.bind("<Return>",lambda event:self.Rua_clie_entry.focus())
        self.Bairro_clie_entry.place(x=0,y=100,height=20)
        self.Rua_clie_entry=Entry(self.frame_cli,font="Arial 10 bold",bd=1,foreground="black",width=30)
        self.Rua_clie_entry.bind("<Return>",lambda event:self.N_cs_clie_entry.focus())
        self.Rua_clie_entry.place(x=300,y=100,height=20)
        self.N_cs_clie_entry=Entry(self.frame_cli,font="Arial 10 bold",bd=1,foreground="black",width=10)
        self.N_cs_clie_entry.bind("<Return>",lambda event:self.Complemento_clie_entry.focus())
        self.N_cs_clie_entry.place(x=600,y=100,height=20)
        self.Complemento_clie_entry=Entry(self.frame_cli,font="Arial 10 bold",bd=1,foreground="black",width=50)
        self.Complemento_clie_entry.bind("<Return>",lambda event:self.add_cli.focus())
        self.Complemento_clie_entry.place(x=700,y=100,height=20)

        self.add_cli=Button(self.frame_cli,font="Arial 12 bold",text="Novo Cliente",bg="black",command=self.banco_cliente,foreground="white",bd=1)
        self.add_cli.bind("<Return>",lambda event:self.banco_cliente())
        self.add_cli.bind("<Right>",lambda event:self.add_func.focus())
        self.add_cli.bind("<Left>",lambda event:self.nome_clie_entry.focus())
        self.add_cli.place(x=700,y=150)
        self.add_func=Button(self.frame_cli,font="Arial 12 bold",text="Novo Funcionario",bg="black",foreground="white",bd=1)
        self.add_func.bind("<Return>",lambda event:self.tell_clie_entry.focus())
        self.add_func.bind("<Right>",lambda event:self.voltar_cli.focus())
        self.add_func.bind("<Left>",lambda event:self.add_cli.focus())
        self.add_func.place(x=850,y=150)
        self.voltar_cli=Button(self.frame_cli,font="Arial 12 bold",text="Voltar",bg="black",command=self.volta_clie,foreground="white",bd=1)
        self.voltar_cli.bind("<Return>",lambda event:self.volta_clie())
        self.voltar_cli.bind("<Left>",lambda event:self.add_func.focus())
        self.voltar_cli.place(x=1050,y=150)

        self.nome_clie_entry.focus()

    def volta_clie(self):
        self.frame_cli.place_forget()

    def banco_cliente(self):
        self.nome=self.nome_clie_entry.get()
        self.tell=self.tell_clie_entry.get().replace(".","").replace("-","").replace("(","").replace(")","")
        self.gmail=self.gmail_clie_entry.get()
        self.nome_fake=self.nome_fake_clie_entry.get()
        self.cpf=self.cpf_clie_entry.get().replace(".","").replace("-","")
        self.rg=self.rg_clie_entry.get().replace(".","")
        self.cnpj=self.cnpj_clie_entry.get().replace(".","")
        self.bairro=self.Bairro_clie_entry.get()
        self.rua=self.Rua_clie_entry.get()
        self.n_cs=self.N_cs_clie_entry.get()
        self.complemento=self.Complemento_clie_entry.get()
        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()
        b.execute("SELECT cpf FROM Pessoas WHERE cpf=?",(self.cpf,))
        cpf=b.fetchall()
        if self.nome== "" or self.tell =="" or self.gmail == "" or self.bairro== "" or self.rua == "" or self.cpf=="" or self.rg =="": 
            messagebox.showinfo("Erro","Campo Vazio")
            self.nome_clie_entry.focus()
        else:
            if len(cpf)>=1:
                messagebox.showerror("erro","Cpf ja cadastrado")
                self.cpf_clie_entry.focus()                
            else:
                b.execute("INSERT INTO Pessoas (nome,tell,gmail,nome_fake,cpf,rg,cnpj,bairro,rua,n_cs,complemento) VALUES (?, ?, ?,?,?,?,?,?,?,?,?);",(self.nome,self.tell,self.gmail,self.nome_fake,self.cpf,self.rg,self.cnpj,self.bairro,self.rua,self.n_cs,self.complemento,))
                Banco.commit()    
                messagebox.showinfo("Sucesso","Cliente cadastrado com sucesso")
                self.limpa_entrys_clie()
    def limpa_entrys_clie(self):
        self.nome_clie_entry.delete(0,END)
        self.tell_clie_entry.delete(0,END)
        self.gmail_clie_entry.delete(0,END)
        self.nome_fake_clie_entry.delete(0,END)
        self.cpf_clie_entry.delete(0,END)
        self.rg_clie_entry.delete(0,END)
        self.cnpj_clie_entry.delete(0,END)
        self.Bairro_clie_entry.delete(0,END)
        self.Rua_clie_entry.delete(0,END)
        self.N_cs_clie_entry.delete(0,END)
        self.Complemento_clie_entry.delete(0,END) 
        self.nome_clie_entry.focus() 

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
        if self.table_pedidos.winfo_exists:
            self.table_pedidos.place_forget()
        if self.table_clientes.winfo_exists:
            self.table_clientes.place_forget()
        if self.table_funcionarios.winfo_exists:
            self.table_funcionarios.place_forget()

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

