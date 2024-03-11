import sqlite3
import re
import tkinter as tk
from tkinter import Label, ttk, messagebox
from tkinter import *
from fechamento_cx import F_caixa
from mesas import *


class caixa(F_caixa, mes_geral):
    def principal_frame(self):
        self.janela_principal.iconbitmap("ImageTk/logo.ico"
        )
        self.janela_principal.title("Caixa")
        self.caixa_frame = Frame(
            self.janela_principal, width=1800, height=800, bg="#616161"
        )
        self.caixa_frame.place(x=0, y=0)

        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()

        self.frame_gera = LabelFrame(self.caixa_frame, width=800, height=800,bd=3, bg="#616161",highlightbackground="white")
        self.frame_gera.place(x=700, y=0)

        b.execute("SELECT nome FROM Pessoas")
        Op = b.fetchall()
        opcoes = ["Consumidor",Op]

        escolha_var = tk.StringVar()
        escolha_var.set(opcoes[0])

        self.amostra_itens = LabelFrame(
            self.frame_gera, width=750, height=500, bg="#c4c2c2", bd=20
        )
        self.amostra_itens.configure(highlightbackground="#c4c2c2")
        self.amostra_itens.place(x=0, y=50)

        b.execute("SELECT Cliente FROM Venda ORDER BY Id DESC LIMIT 1")
        cliente = b.fetchone()

        self.def_cliente_texto = Label(
            self.frame_gera,
            text="Cliente:",
            font="Arial 12",
            bg="#616161",
            foreground="white",
        )
        self.def_cliente_texto.place(x=0, y=2)
        self.consumidor = StringVar(value=cliente)
        self.def_cliente_digito = ttk.Combobox(
            self.frame_gera, width=50, textvariable=escolha_var, values=opcoes
        )
        self.def_cliente_digito.config(
            font=("arial 12"), justify="left", textvariable=self.consumidor
        )
        self.def_cliente_digito.bind(
            "<Return>", lambda event: self.cdg_insert_digt.focus()
        )
        self.def_cliente_digito.place(x=60, y=2)

        self.chekin_test=Checkbutton(self.frame_gera,text="ADM",bg="#616161",command=self.ADM)
        self.chekin_test.place(x=200,y=25)
        b.execute("SELECT Id FROM Venda ORDER BY Id DESC LIMIT 1")
        resulta = b.fetchone()
        resulta = re.sub(r"[^\d,\.\d{0,2}$]+", "", str(resulta)).replace(",", "")
        if resulta is not None:
            Nu = resulta

        self.numero_venda_texto = Label(
            self.frame_gera,
            font="Arial 12 ",
            text=f"Venda N°:{Nu}",
            bg="#616161",
            foreground="white",
        )
        self.numero_venda_texto.place(x=0, y=25)

        self.voltar_caixa_bu = Button(
            self.frame_gera,
            width=10,
            text="Voltar(v)",
            bg="orange",
            fg="dimgray",
            font="arial 14",
            foreground="white",
            command=self.voltar_usu,
            bd=3,
        )
        self.voltar_caixa_bu.place(x=655, y=730, height=25)
        self.sair_cx = Button(
            self.frame_gera,
            width=10,
            text="Sair(s)",
            bg="orange",
            fg="dimgray",
            font="arial 14",
            foreground="white",
            command=self.exit,
            bd=3,
        )
        self.sair_cx.place(x=655, y=700, height=25)

        self.fecha_venda = Button(
            self.frame_gera,
            text="Finalizar Venda",
            font="Arial 14",
            width=20,
            bd=1,
            bg="green",
            command=self.fechamento,
            foreground="white",
        )
        self.fecha_venda.place(x=530, y=650, height=20)

        self.del_produto = Button(
            self.frame_gera,
            text="Deletar Produto(D)",
            font="Arial 14",
            width=20,
            bd=1,
            bg="green",
            command=self.Deletar_produto,
            foreground="white",
        )
        self.del_produto.place(x=530, y=670, height=20)

        self.nova_venda_bu = Button(
            self.frame_gera,
            text="Nova venda(N)",
            font="Arial 14",
            width=20,
            bd=1,
            bg="green",
            command=self.nova_venda,
            foreground="white",
        )
        self.nova_venda_bu.place(x=530, y=20, height=25)

        self.mesas_aberta_bu = Button(
            self.caixa_frame,
            text="Abertos(A)",
            font="Arial 14",
            width=20,
            bd=1,
            bg="yellow",
            command=self.mesa_base,
            foreground="black",
        )
        self.mesas_aberta_bu.place(x=10, y=20, height=25)

        self.inserir_dados()
    
    def ADM (self):
        self.adm_frame=LabelFrame(self.frame_gera,height=25,width=100,bg="#616161")
        self.adm_frame.place(x=250,y=25)

        self.adm_senha=Entry(self.adm_frame,font="Arial 12 bold")
        self.adm_senha.bind("<Return>", lambda event: self.verifica_senha_adm())
        self.adm_senha.place(x=0,y=0)

    def verifica_senha_adm(self):
        senha=self.adm_senha.get()

        if senha=="123":
            self.adm_frame.place_forget()
            self.custo_adm=Label(self.frame_insert,text="Custo",width=25,height=25)
            self.custo_adm.place(x=0,y=100)
        else:
            self.adm_frame.place_forget()
            messagebox.showinfo("erro","Senha Incorreta")



    def Atualiza_caixa(self):
        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()

        self.vlr_antt = 00, 00
        self.vlr_ant = re.sub(r"[^\d,\.\d{0,2}$]+", "", str(self.vlr_antt))

        b.execute("SELECT Id FROM Venda ORDER BY Id DESC LIMIT 1")
        Id_venda = b.fetchall()
        Id_venda = re.sub(r"[^\d,\.\d{0,2}$]+", "", str(Id_venda)).replace(",", "")

        b.execute(
            "SELECT cdg,PRODUTO, Quantidade,PREÇO,Preco_quant FROM vendas_dados WHERE Id_venda=?",
            (Id_venda,),
        )
        results = b.fetchall()

        for row in results:
            cdg, nome, qntde, valore, valor_finali = row
            valor = "{:.2f}".format(round(valore, 2))
            valor_final = "{:.2f}".format(round(valor_finali, 2))
            self.frame_item = LabelFrame(
                self.amostra_itens, width=750, height=50, bg="#c4c2c2", bd=2
            )
            self.frame_item.pack(side=TOP)

            self.cdg_ex = LabelFrame(
                self.frame_item,
                text=f"({cdg})",
                font="Arial 14 ",
                width=25,
                bd=0,
                height=45,
                bg="#c4c2c2",
                foreground="black",
            )
            self.cdg_ex.place(x=2, y=2)

            self.resu_nome = LabelFrame(
                self.frame_item,
                text="",
                font="Arial 14 ",
                width=700,
                bd=0,
                height=45,
                bg="#c4c2c2",
                foreground="black",
            )
            self.resu_nome.place(x=25, y=2)

            self.resu_valor = LabelFrame(
                self.frame_item,
                text="",
                font="Arial 26 ",
                width=200,
                bd=0,
                height=45,
                bg="#c4c2c2",
                foreground="#48ff00",
            )
            self.resu_valor.place(x=500, y=2)

            self.resu_valor_uni = LabelFrame(
                self.frame_item,
                text="",
                font="Arial 14 ",
                width=500,
                bd=0,
                height=45,
                bg="#c4c2c2",
                foreground="black",
            )
            self.resu_valor_uni.place(x=2, y=25)

            self.resu_quant = LabelFrame(
                self.frame_item,
                text="",
                font="Arial 14 ",
                width=200,
                bd=0,
                height=45,
                bg="#c4c2c2",
                foreground="black",
            )
            self.resu_quant.place(x=250, y=25)

            self.resu_nome.config(text=f"Produto= {nome}")
            self.resu_valor_uni.config(text=f"Valor unitario= {valor} R$")
            self.resu_quant.config(text=f"x{qntde}")
            self.resu_valor.config(text=f"= {valor_final} R$")

            b.execute(
                "SELECT SUM(Preco_quant) FROM vendas_dados WHERE Id_venda = ?",
                (Id_venda,),
            )
            self.vlr_antt = b.fetchone()[0]
            self.vlr_ant = "{:.2f}".format(round(self.vlr_antt, 2)).replace(".", ",")

        b.close()
        Banco.close()

        self.calc_item_total_cx = LabelFrame(
            self.frame_gera,
            width=300,
            height=100,
            bd=2,
            bg="#616161",
            foreground="#48ff00",
        )
        self.calc_item_total_cx.place(x=500, y=555)

        self.calc_item_total = LabelFrame(
            self.calc_item_total_cx,
            font="Arial 40",
            text=f"{self.vlr_ant}R$",
            width=290,
            height=60,
            bd=0,
            bg="#616161",
            foreground="#48ff00",
        )
        self.calc_item_total.pack(side=TOP)

    def calc_msm_item(self):
        qntde = self.qntd_insert_digt.get().replace(",", ".")

        codigo = self.cdg_insert_digt.get()

        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()

        if qntde == "":
            qntde = 1
        else:
            self.qntd_insert_digt.focus()

        b.execute("SELECT Id FROM Venda ORDER BY Id DESC LIMIT 1")
        Id_venda = b.fetchone()[0]
        Id_venda = re.sub(r"[^\d,\.\d{0,2}$]+", "", str(Id_venda)).replace(",", "")

        self.conn = sqlite3.connect("banco.db")
        self.cur = self.conn.cursor()
        self.cur.execute(
            "SELECT * FROM vendas_dados WHERE Id_venda=? and cdg=?", (Id_venda, codigo)
        )
        self.rows = self.cur.fetchall()
        if len(self.rows) >= 1:
            b.execute("SELECT QTDE FROM Estoque WHERE Codigo=?", (codigo,))
            qual = b.fetchone()
            qntde_up = qual
            qntd_diminui = qntde_up[0] - float(qntde)
            Banco.commit()
            b.execute(
                "SELECT Quantidade,PREÇO FROM vendas_dados WHERE Id_venda=? and cdg=?",
                (Id_venda, codigo),
            )
            dado = b.fetchone()
            dados, valore1 = dado
            qntde1 = float(qntde) + float(dados)
            valor_fini1 = float(valore1) * float(qntde1)
            Banco.commit()
            self.cur.execute(
                "UPDATE vendas_dados SET Preco_quant=?, Quantidade=? WHERE Id_venda=? AND cdg=?",
                (valor_fini1, qntde1, Id_venda, codigo),
            )
            self.cur.execute(
                "UPDATE Estoque SET QTDE=? WHERE Codigo=?", (qntd_diminui, codigo)
            )
            self.conn.commit()
            self.reload_aba()
        else:
            b.execute(
                "SELECT PRODUTO, PREÇO,QTDE FROM Estoque WHERE Codigo=?", (codigo,)
            )
            result = b.fetchone()
            if result is not None:
                nome, valore, qtde = result
                qntd_diminui = qtde - float(qntde)
                valor_finali = valore * float(qntde)
                valor = "{:.2f}".format(round(valore, 2))
                valor_final = "{:.2f}".format(round(valor_finali, 2))
                self.frame_item = LabelFrame(
                    self.amostra_itens, width=750, height=50, bg="#c4c2c2", bd=2
                )
                self.frame_item.pack(side=TOP)

                self.cdg_ex = LabelFrame(
                    self.frame_item,
                    text=f"({self.cdg_insert_digt.get()})",
                    font="Arial 14 ",
                    width=25,
                    bd=0,
                    height=45,
                    bg="#c4c2c2",
                    foreground="black",
                )
                self.cdg_ex.place(x=2, y=2)

                self.resu_nome = LabelFrame(
                    self.frame_item,
                    text="",
                    font="Arial 14 ",
                    width=700,
                    bd=0,
                    height=45,
                    bg="#c4c2c2",
                    foreground="black",
                )
                self.resu_nome.place(x=25, y=2)

                self.resu_valor = LabelFrame(
                    self.frame_item,
                    text="",
                    font="Arial 26 ",
                    width=200,
                    bd=0,
                    height=45,
                    bg="#c4c2c2",
                    foreground="#48ff00",
                )
                self.resu_valor.place(x=500, y=2)

                self.resu_valor_uni = LabelFrame(
                    self.frame_item,
                    text="",
                    font="Arial 14 ",
                    width=500,
                    bd=0,
                    height=45,
                    bg="#c4c2c2",
                    foreground="black",
                )
                self.resu_valor_uni.place(x=2, y=25)

                self.resu_quant = LabelFrame(
                    self.frame_item,
                    text="",
                    font="Arial 14 ",
                    width=200,
                    bd=0,
                    height=45,
                    bg="#c4c2c2",
                    foreground="black",
                )
                self.resu_quant.place(x=250, y=25)

                self.resu_nome.config(text=f"Produto= {nome}")
                self.resu_valor_uni.config(text=f"Valor unitario= {valor} R$")
                self.resu_quant.config(text=f"x{qntde}")
                self.resu_valor.config(text=f"= {valor_final} R$")
                self.limpa_entrys()

                try:
                    b.execute(
                        "INSERT INTO vendas_dados (Id_venda,Cdg, PRODUTO, Quantidade, PREÇO,Preco_quant) VALUES (?, ?, ?, ?,?,?);",
                        (Id_venda, codigo, nome, qntde, valor, valor_final),
                    )
                    b.execute(
                        "UPDATE Estoque SET QTDE=? WHERE Codigo=?",
                        (qntd_diminui, codigo),
                    )
                    Banco.commit()
                except:
                    Banco.rollback()

        b.execute(
            "SELECT SUM(Preco_quant) FROM vendas_dados WHERE Id_venda = ?", (Id_venda,)
        )
        self.vlr_antti = b.fetchone()[0]
        self.vlr_ant = "{:.2f}".format(round(self.vlr_antti, 2)).replace(".", ",")

        self.calc_item_total_cx = LabelFrame(
            self.frame_gera,
            width=300,
            height=100,
            bd=2,
            bg="#616161",
            foreground="#48ff00",
        )
        self.calc_item_total_cx.place(x=500, y=555)

        self.calc_item_total = LabelFrame(
            self.calc_item_total_cx,
            font="Arial 40",
            text=f"{self.vlr_ant}R$",
            width=290,
            height=60,
            bd=0,
            bg="#616161",
            foreground="#48ff00",
        )
        self.calc_item_total.pack(side=TOP)
        b.close()
        Banco.close()

    def inserir_dados(self):
        self.qntd_base = StringVar(value="1")
        self.frame_insert = LabelFrame(
            self.frame_gera, width=500, bd=2, height=200, bg="#616161"
        )
        self.frame_insert.place(x=0, y=555)

        self.cdg_insert = Label(
            self.frame_insert,
            text="Codigo:",
            font="Arial 12",
            bg="#616161",
            foreground="white",
        )
        self.cdg_insert.place(x=0, y=0)

        self.cdg_insert_digt = Entry(self.frame_insert, width=25, bg="white", bd=1)
        self.cdg_insert_digt.bind(
            "<Return>", lambda event: self.ex_item(self.cdg_insert_digt.get())
        )
        self.cdg_insert_digt.bind("<KeyPress-s>", lambda event: self.exit())
        self.cdg_insert_digt.bind("<KeyPress-a>", lambda event: self.mesa_base())
        self.cdg_insert_digt.bind("<KeyPress-v>", lambda event: self.voltar_usu())
        self.cdg_insert_digt.bind("<KeyPress-n>", lambda event: self.nova_venda())
        self.cdg_insert_digt.bind("<KeyPress-d>", lambda event: self.Deletar_produto())
        self.cdg_insert_digt.bind("<KeyPress-f>", lambda event: self.fechamento())
        self.cdg_insert_digt.place(x=0, y=25, height=25)

        self.qntd_insert = Label(
            self.frame_insert,
            text="Quantidade:",
            font="Arial 12",
            bg="#616161",
            foreground="white",
        )
        self.qntd_insert.place(x=200, y=0)

        self.qntd_insert_digt = Entry(
            self.frame_insert, width=25, textvariable=self.qntd_base, bg="white", bd=1
        )
        self.qntd_insert_digt.bind("<Return>", lambda event: self.calc_msm_item())
        self.qntd_insert_digt.bind("<KeyPress-s>", lambda event: self.exit())
        self.qntd_insert_digt.bind("<KeyPress-a>", lambda event: self.mesa_base())
        self.qntd_insert_digt.bind("<KeyPress-v>", lambda event: self.voltar_usu())
        self.qntd_insert_digt.bind("<KeyPress-n>", lambda event: self.nova_venda())
        self.qntd_insert_digt.bind("<KeyPress-d>", lambda event: self.Deletar_produto())
        self.qntd_insert_digt.bind("<KeyPress-f>", lambda event: self.fechamento())
        self.qntd_insert_digt.bind("<Left>", lambda event: self.cdg_insert_digt.focus())
        self.qntd_insert_digt.place(x=200, y=25, height=25)
        self.qntd_insert_digt.select_range(0, "end")

        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()

        b.execute("SELECT Id FROM Venda ORDER BY Id DESC LIMIT 1")
        Id_venda = b.fetchone()[0]
        Id_venda = re.sub(r"[^\d,\.\d{0,2}$]+", "", str(Id_venda)).replace(",", "")
        b.execute(
            "DELETE FROM vendas_dados WHERE Id_venda=? AND Quantidade=?", (Id_venda, 0)
        )
        Banco.commit()
        self.cdg_insert_digt.focus()
        self.Atualiza_caixa()

    def ex_item(self, codigo):
        self.qntd_insert_digt.focus()

        self.print_frame_nome = LabelFrame(
            self.frame_insert,
            text="Nome",
            font="Arial 18 ",
            width=490,
            bd=0,
            height=45,
            bg="#616161",
            foreground="white",
        )
        self.print_frame_nome.place(x=2, y=55)

        self.print_frame_valor = LabelFrame(
            self.frame_insert,
            text="Valor",
            font="Arial 18 ",
            width=240,
            bd=0,
            height=45,
            bg="#616161",
            foreground="white",
        )
        self.print_frame_valor.place(x=150, y=105)

        self.print_frame_qntd = LabelFrame(
            self.frame_insert,
            text="Qtde",
            font="Arial 18 ",
            width=140,
            bd=0,
            height=25,
            bg="#616161",
            foreground="white",
        )
        self.print_frame_qntd.place(x=300, y=155)

        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()

        b.execute("SELECT PRODUTO, PREÇO, QTDE FROM Estoque WHERE Codigo=?", (codigo,))
        result = b.fetchone()
        if result is not None:
            nome, valor, qtde = result
            self.print_frame_nome.config(text=f"Produto= {nome}")
            self.print_frame_valor.config(text=f"Valor= {valor} R$")
            self.print_frame_qntd.config(text=f"Qtde= {qtde}")
        else:
            messagebox.showinfo("Erro", "Produto nao encontrado")
            self.limpa_entrys()
            self.cdg_insert_digt.focus()

    def voltar_usu(self):
        self.frame_gera.place_forget()
        self.usuario_mainwmenu(8, 8)

    def exit(self):
        self.janela_principal.destroy()
        exit(0)

    def limpa_entrys(self):
        self.cdg_insert_digt.delete(0, END)
        self.qntd_insert_digt.delete(0, END)
        self.cdg_insert_digt.focus()

    def nova_venda(self):
        cliente = self.def_cliente_digito.get()
        Status = "Aberto"
        banco = sqlite3.connect("banco.db")
        b = banco.cursor()

        b.execute("SELECT Id FROM Venda ORDER BY Id DESC LIMIT 1")
        Id_venda = b.fetchone()[0]
        Id_venda = re.sub(r"[^\d,\.\d{0,2}$]+", "", str(Id_venda)).replace(",", "")

        b.execute(
            "SELECT SUM(Preco_quant) FROM vendas_dados WHERE Id_venda = ?", (Id_venda,)
        )
        Valure = b.fetchone()[0]

        if Valure is not None:
            b.execute(
                "UPDATE Venda SET Cliente = ?, Valor = ? WHERE Id = ?",
                (cliente, Valure, Id_venda),
            )

            b.execute(
                "INSERT INTO Venda (Cliente, Status) VALUES (?, ?)",
                ("Consumidor", Status),
            )

        banco.commit()
        banco.close()

        self.reload_aba()

    def fechamento(self):
        self.fechar_venda()

    def reload_aba(self):
        self.frame_gera.place_forget()
        self.principal_frame()

    def Deletar_produto(self):
        self.del_frame = LabelFrame(
            self.caixa_frame, width=1200, height=600, bd=5, bg="#787777"
        )
        self.del_frame.place(x=100, y=100)

        self.Codigo_del_text = Label(
            self.del_frame,
            width=10,
            text="Codigo",
            bg="#787777",
            font="arial 12",
            foreground="white",
            bd=0,
        )
        self.Codigo_del_text.place(x=5, y=0)
        self.Codigo_del = Entry(
            self.del_frame,
            width=10,
            fg="dimgray",
            font="arial 12",
            foreground="Black",
            bd=1,
        )
        self.Codigo_del.bind("<Return>", lambda event: self.Qntd_del.focus())
        self.Codigo_del.bind("<KeyPress-v>", lambda event: self.volta_caixa_())
        self.Codigo_del.place(x=5, y=20)

        self.Qntd_del_text = Label(
            self.del_frame,
            width=10,
            text="Quantidade",
            bg="#787777",
            font="arial 12",
            foreground="white",
            bd=0,
        )
        self.Qntd_del_text.place(x=200, y=0)
        self.Qntd_del = Entry(
            self.del_frame,
            width=10,
            fg="dimgray",
            font="arial 12",
            foreground="Black",
            bd=1,
        )
        self.Qntd_del.bind("<Return>", lambda event: self.exibi_valor_del())
        self.Qntd_del.bind("<KeyPress-v>", lambda event: self.volta_caixa_())
        self.Qntd_del.place(x=200, y=20)

        self.voltar_fecha_vnd = Button(
            self.del_frame,
            width=10,
            text="Voltar",
            bg="orange",
            fg="dimgray",
            font="arial 12",
            foreground="white",
            command=self.volta_caixa_,
            bd=3,
        )
        self.voltar_fecha_vnd.place(x=1080, y=550)

        self.confirma_del = Button(
            self.del_frame,
            width=10,
            text="Deletar",
            bg="orange",
            fg="dimgray",
            font="arial 12",
            foreground="white",
            command=self.exibi_valor_del,
            bd=3,
        )
        self.confirma_del.place(x=1080, y=500)

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
        self.table = ttk.Treeview(self.del_frame, height=200)
        self.table.place(x=0, y=50, width=800)
        self.table["columns"] = ("Codigo", "PRODUTO", "PREÇO", "QTDE")

        self.table.column("#0", width=1, minwidth=1)
        self.table.column("#1", width=50, minwidth=20)
        self.table.column("#2", width=20, minwidth=20)
        self.table.column("#3", width=50, minwidth=20)
        self.table.column("#4", width=50, minwidth=20)

        self.table.heading("#0", text="Codigo")
        self.table.heading("#1", text="Produto")
        self.table.heading("#2", text="Preço")
        self.table.heading("#3", text="Quantidade")
        self.table.heading("#4", text="Valor total")

        b.execute("SELECT Id FROM Venda ORDER BY Id DESC LIMIT 1")
        Id_venda = b.fetchall()
        Id_venda = re.sub(r"[^\d,\.\d{0,2}$]+", "", str(Id_venda)).replace(",", "")

        b.execute(
            "SELECT Cdg,PRODUTO,PREÇO,Quantidade,Preco_quant FROM vendas_dados WHERE Id_venda=?",
            (Id_venda,),
        )
        rows = b.fetchall()
        for row in rows:
            self.table.insert(
                parent="",
                index="end",
                text=row[0],
                values=(row[1], row[2], row[3], row[4]),
            )
            self.table.place(x=0, y=50, width=800, height=515)
        Banco.close()

        self.Codigo_del.focus()

    def exibi_valor_del(self):
        cdg_valor = self.Codigo_del.get()
        qntd_valor = self.Qntd_del.get()

        self.frame_ex = LabelFrame(
            self.del_frame, width=390, height=400, bd=2, bg="#787777"
        )
        self.frame_ex.place(x=800, y=50)

        conn = sqlite3.connect("banco.db")
        b = conn.cursor()

        b.execute("SELECT Id FROM Venda ORDER BY Id DESC LIMIT 1")
        Id_venda = b.fetchall()
        Id_venda = re.sub(r"[^\d,\.\d{0,2}$]+", "", str(Id_venda)).replace(",", "")

        b.execute(
            "SELECT PRODUTO,Quantidade,PREÇO FROM vendas_dados WHERE Id_venda=? AND cdg=?",
            (
                Id_venda,
                cdg_valor,
            ),
        )
        valor = b.fetchone()

        if valor is not None:
            produto, quantidade, preco = valor

            if qntd_valor == "":
                if messagebox.askyesno("Tem Certeza?", f"Deseja Deletar o {produto}?"):
                    b.execute(
                        "DELETE from vendas_dados WHERE Id_venda=? AND cdg=?",
                        (
                            Id_venda,
                            cdg_valor,
                        ),
                    )
                    b.execute("SELECT QTDE FROM Estoque WHERE Codigo=?", (cdg_valor,))
                    qual = b.fetchone()
                    qntde_up = qual
                    qntd_diminui = qntde_up[0] + float(quantidade)

                    b.execute(
                        "UPDATE Estoque SET QTDE=? WHERE Codigo=?",
                        (qntd_diminui, cdg_valor),
                    )
                    conn.commit()
                    self.reload_aba()

            if float(qntd_valor) <= quantidade:
                qntd_v = quantidade - int(qntd_valor)
                preto = qntd_v * preco
                if messagebox.askyesno(
                    "Tem Certeza?", f"Deseja deletar {qntd_valor} {produto}?"
                ):
                    b.execute(
                        "UPDATE vendas_dados SET  Quantidade= ? , Preco_quant=? WHERE Id_venda=? AND cdg=?",
                        (
                            qntd_v,
                            preto,
                            Id_venda,
                            cdg_valor,
                        ),
                    )
                    b.execute("SELECT QTDE FROM Estoque WHERE Codigo=?", (cdg_valor,))
                    qual = b.fetchone()
                    qntde_up = qual
                    qntd_diminui = qntde_up[0] + float(qntd_valor)

                    b.execute(
                        "UPDATE Estoque SET QTDE=? WHERE Codigo=?",
                        (qntd_diminui, cdg_valor),
                    )
                    conn.commit()
                    self.reload_aba()
            else:
                messagebox.showinfo("Erro", "Quantidade Invalida")
                self.Qntd_del.focus()
        else:
            messagebox.showerror("Erro", "Codigo não encontrado")
            self.Codigo_del.focus()

        b.execute(
            "DELETE FROM vendas_dados WHERE Id_venda=? AND Quantidade=?", (Id_venda, 0)
        )
        conn.commit()
        conn.close()

    def volta_caixa_(self):
        self.del_frame.place_forget()
        self.cdg_insert_digt.delete(0, END)
        self.qntd_insert_digt.delete(0, END)
        self.cdg_insert_digt.focus()
