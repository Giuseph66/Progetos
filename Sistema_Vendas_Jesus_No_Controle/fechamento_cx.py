import sqlite3
import re
import tkinter as tk
from tkinter import Label,ttk,messagebox
from tkinter import *

class F_caixa():
    def fechar_venda(self):
        self.nova_venda()
        self.din_zero = StringVar(value="00,00")
        self.deb_zero = StringVar(value="00,00")
        self.cre_zero = StringVar(value="00,00")
        self.desc_zero = StringVar(value="00,00")
        self.fechar_venda_1()

    def fechar_venda_1(self):
        self.fecha_caixa=LabelFrame(self.caixa_frame,width=1000,height=500,bd=2,bg="#787777")
        self.fecha_caixa.place(x=200,y=150)
        self.ven_valo_texto = Label(self.fecha_caixa,text="Valor:", font="Arial 12", bg="#787777", foreground="white")
        self.ven_valo_texto.place(x=5, y=5)
        self.valor_venda_cx=LabelFrame(self.fecha_caixa,width=200,height=25,font="Arial 12",bd=0,bg="#adacac")
        self.valor_venda_cx.place(x=75,y=5)

        self.ven_cliente_texto = Label(self.fecha_caixa,text="Cliente:", font="Arial 12", bg="#787777", foreground="white")
        self.ven_cliente_texto.place(x=720, y=5)
        
        self.valor_venda=LabelFrame(self.fecha_caixa,width=200,height=25,font="Arial 12",bd=0,bg="#adacac")
        self.valor_venda.place(x=790,y=5)

        self.confirma_venda=Button(self.fecha_caixa,width=10,text="Confirmar",bg="orange",fg="dimgray",font="arial 12",command=self.finaliza,foreground="white",bd=3)
        self.confirma_venda.place(x=880,y=400)

        self.voltar_fecha_vnd=Button(self.fecha_caixa,width=10,text="Voltar",bg="orange",fg="dimgray",font="arial 12",foreground="white",command=self.volta_caixa_f,bd=3)
        self.voltar_fecha_vnd.place(x=880,y=450)
        
        self.opicoes=LabelFrame(self.fecha_caixa,width=200,height=35,text="Forma de PG:",font="Arial 20",bd=0,bg="#787777",foreground="#04ff00")
        self.opicoes.place(x=520,y=20)
        
        self.opicoes_din_f=LabelFrame(self.fecha_caixa,width=450,height=70,font="Arial 15",bd=2,bg="#787777")
        self.opicoes_din_f.place(x=520,y=50)

        self.opicoes_din=LabelFrame(self.opicoes_din_f,width=200,height=25,text="DINHEIRO:",font="Arial 15",bd=0,bg="#787777",foreground="#ccff00")
        self.opicoes_din.place(x=0,y=0)

        self.card_din=Entry(self.opicoes_din_f,width=20,font="Arial 12",textvariable=self.din_zero,foreground="blue")
        self.card_din.bind("<KeyPress-v>",lambda event:self.volta_caixa_f())
        self.card_din.bind("<Return>",lambda event:self.card_cartao_deb.focus())
        self.card_din.bind("<KeyPress-v>",lambda event:self.volta_caixa_f())
        self.card_din.bind("<KeyPress>",lambda event:self.limpa_dim())
        self.card_din.bind("<KeyPress-f>",lambda event:self.finaliza())
        self.card_din.bind("<KeyPress-t>",lambda event:self.total_entry_din())
        self.card_din.place(x=5,y=28,height=30)

        self.opicoes_cartao=LabelFrame(self.fecha_caixa,width=450,height=100,text="CARTAO:",font="Arial 15",bd=2,bg="#787777",foreground="#04ff00")
        self.opicoes_cartao.place(x=520,y=120)

        self.opicoes_deb=LabelFrame(self.opicoes_cartao,width=200,height=25,text="DEBITO:",font="Arial 15",bd=0,bg="#787777",foreground="#ccff00")
        self.opicoes_deb.place(x=0,y=0)

        self.card_cartao_deb=Entry(self.opicoes_cartao,width=20,font="Arial 12",textvariable=self.deb_zero,foreground="blue")
        self.card_cartao_deb.bind("<KeyPress-v>",lambda event:self.volta_caixa_f())
        self.card_cartao_deb.bind("<Return>",lambda event:self.card_cartao_cre.focus())
        self.card_cartao_deb.bind("<KeyPress>",lambda event:self.limpa_deb())
        self.card_cartao_deb.bind("<KeyPress-f>",lambda event:self.finaliza())
        self.card_cartao_deb.bind("<KeyPress-t>",lambda event:self.total_entry_deb())
        self.card_cartao_deb.place(x=5,y=28,height=30)
        
        self.opicoes_cre=LabelFrame(self.opicoes_cartao,width=200,height=25,text="CREDITO:",font="Arial 15",bd=0,bg="#787777",foreground="#ccff00")
        self.opicoes_cre.place(x=200,y=0) 

        self.card_cartao_cre=Entry(self.opicoes_cartao,width=20,font="Arial 12",textvariable=self.cre_zero,foreground="blue")
        self.card_cartao_cre.bind("<KeyPress-v>",lambda event:self.volta_caixa_f())
        self.card_cartao_cre.bind("<Return>",lambda event:self.card_desc.focus())
        self.card_cartao_cre.bind("<KeyPress>",lambda event:self.limpa_cre())
        self.card_cartao_cre.bind("<KeyPress-f>",lambda event:self.finaliza())
        self.card_cartao_cre.bind("<KeyPress-t>",lambda event:self.total_entry_cre())
        self.card_cartao_cre.place(x=200,y=28,height=30)
        
        self.opicoes_desc=LabelFrame(self.fecha_caixa,width=450,height=75,text="DESCONTO:",font="Arial 15",bd=1,bg="#787777",foreground="#ccff00")
        self.opicoes_desc.place(x=520,y=320) 

        self.card_desc=Entry(self.opicoes_desc,width=20,font="Arial 12",textvariable=self.desc_zero,bd=1,foreground="blue")
        self.card_desc.bind("<KeyPress-v>",lambda event:self.volta_caixa_f())
        self.card_desc.bind("<Return>",lambda event:self.desc_2())
        self.card_desc.bind("<KeyPress>",lambda event:self.limpa_desc())
        self.card_desc.bind("<KeyPress-f>",lambda event:self.finaliza())
        self.card_desc.place(x=5,y=5,height=30)

        self.dados_venda=LabelFrame(self.fecha_caixa,width=500,height=400,bd=0,bg="black")
        self.dados_venda.place(x=10,y=50)   
        
        banco=sqlite3.connect('banco.db')
        b=banco.cursor()
        
        b.execute("SELECT Id FROM Venda ORDER BY Id DESC LIMIT 1")
        Id_venda = b.fetchall() 
        Id_venda = re.sub(r'[^\d,\.\d{0,2}$]+', '', str(Id_venda)).replace(',', '') 
        Id_venda_1=float(Id_venda)-1
        self.id_vendaL=Id_venda_1
        b.execute("SELECT * FROM venda WHERE Id=? and Status=?", (Id_venda_1,"Aberto"))
        self.rows = b.fetchall()
        if len(self.rows)>=1:
            b.execute('SELECT Cdg FROM vendas_dados WHERE Id_venda = ?', (Id_venda_1,))
            Cdg2=b.fetchall()
            Cdg2 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(Cdg2)).replace(",,","\n").replace(",","")
            
            b.execute('SELECT PRODUTO FROM vendas_dados WHERE Id_venda = ?', (Id_venda_1,))
            produto1=b.fetchall()
            produto1 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(produto1)).replace(",,","\n").replace(",","")
                
            b.execute('SELECT Quantidade FROM vendas_dados WHERE Id_venda = ?', (Id_venda_1,))
            Quantidade1=b.fetchall()
            Quantidade1 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(Quantidade1)).replace(",,","\n").replace(",","")
            
            b.execute('SELECT PREÇO FROM vendas_dados WHERE Id_venda = ?', (Id_venda_1,))
            preco2=b.fetchall()
            preco2 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(preco2)).replace(",,","\n").replace(",","")

            self.dados_cdg=LabelFrame(self.dados_venda,width=900,height=400,font="Arial 12",bd=0,bg="black",foreground="white")
            self.dados_cdg.place(x=0,y=0)

            self.dados_produ=LabelFrame(self.dados_venda,width=900,height=400,font="Arial 12",bd=0,bg="black",foreground="white")
            self.dados_produ.place(x=100,y=0)

            self.dados_qntd=LabelFrame(self.dados_venda,width=900,height=400,font="Arial 12",bd=0,bg="black",foreground="white")
            self.dados_qntd.place(x=320,y=0)

            self.dados_preco=LabelFrame(self.dados_venda,width=900,height=400,font="Arial 12",bd=0,bg="black",foreground="white")
            self.dados_preco.place(x=450,y=0)  

            self.dados_cdg.config(text=f"Codigo\n{Cdg2}")
            self.dados_produ.config(text=f"Produto\n{produto1}")
            self.dados_qntd.config(text=f"Quantidade\n{Quantidade1}")
            self.dados_preco.config(text=f"Valor\n{preco2}")

            b.execute('SELECT Cliente,Valor FROM Venda WHERE Id = ?',(Id_venda_1,))
            result=b.fetchone()
            if result is not None:
                Cliente,self.Valor = result
                self.valor_venda.config(text=f"{Cliente}")
                self.valor_venda_cx.config(text=f"{self.Valor}R$")

        else:
            self.mesa_base()
            self.fecha_caixa.destroy()
            
        if Id_venda_1 is not None:
            Nu_1 = Id_venda_1
            Nu =re.sub(r'[^\d,\.\d{0,2}$]+', '', str(Nu_1)).replace(',', '') 

        self.numero_venda_texto_f=Label(self.fecha_caixa,font="Arial 12 ",text=f"Venda N°:{Nu}",bg="#787777", foreground="white")
        self.numero_venda_texto_f.place(x=400,y=5)
        
        self.card_din.focus()
        self.cont_dim=0
        self.cont_deb=0
        self.cont_cre=0
        self.cont_desc=0

        self.conta_dim()

    def total_entry_din(self):
        self.din_zero = StringVar(value=self.Valor)
        self.deb_zero = StringVar(value="00,00")
        self.cre_zero = StringVar(value="00,00")
        self.desc_zero = StringVar(value="00,00")
        self.fecha_caixa.place_forget()
        self.fechar_venda_1()

    def total_entry_deb(self):
        self.deb_zero = StringVar(value=self.Valor)
        self.din_zero = StringVar(value="00,00")
        self.cre_zero = StringVar(value="00,00")
        self.desc_zero = StringVar(value="00,00")
        self.fecha_caixa.place_forget()
        self.fechar_venda_1()
    def total_entry_cre(self):
        self.cre_zero = StringVar(value=self.Valor)
        self.din_zero = StringVar(value="00,00")
        self.deb_zero = StringVar(value="00,00")
        self.desc_zero = StringVar(value="00,00")
        self.fecha_caixa.place_forget()
        self.fechar_venda_1()

    def antes_conta(self):
        self.opicoes_final.place_forget()
        self.conta_dim()
    def desc_2(self):
        self.card_din.focus()
        self.desc=self.card_desc.get().replace(",",".")  
        self.desc=float(self.desc)

        self.Valor=self.Valor-self.desc
        self.conta_dim()
    def conta_dim(self):
        self.dim=self.card_din.get().replace(",",".")
        self.cre=self.card_cartao_cre.get().replace(",",".")
        self.deb=self.card_cartao_deb.get().replace(",",".")     

        self.dim=float(self.dim)
        self.cre=float(self.cre)
        self.deb=float(self.deb)
        
        self.conta=-self.Valor+(self.dim + self.cre + self.deb)
        self.conta=str(self.conta).replace(".",",")

        self.opicoes_final=LabelFrame(self.fecha_caixa,width=300,height=70,font="Arial 15",bd=2,bg="#787777")
        self.opicoes_final.place(x=520,y=400)

        self.Venda_valor=LabelFrame(self.opicoes_final,width=290,height=50,text=f"R$ {self.conta}",font="Arial 30",bd=0,bg="#787777",foreground="Black")
        self.Venda_valor.place(x=5,y=10)

    def finaliza(self):
        banco=sqlite3.connect('banco.db')
        b=banco.cursor()
        add_if=self.dim + self.cre + self.deb
        if add_if >= self.Valor:    
            b.execute("UPDATE venda SET dim=?, cre=?, deb=? , troco=?,Status=? WHERE Id=?", (self.dim,self.cre,self.deb,self.conta,"Fechada",self.id_vendaL))
            banco.commit()
            self.volta_caixa_f()
        else:
            messagebox.showerror("Valor errado","Pagemento insuficiente")
            self.card_din.focus()

        self.limpa_geral()

    def volta_caixa_f(self):
        self.fecha_caixa.place_forget()
        self.fecha_caixa.destroy()
        self.cdg_insert_digt.focus()

    def limpa_geral(self):
        self.fecha_caixa.place_forget()
        self.fechar_venda()

    def limpa_dim(self):
        self.conta_dim()
        if self.cont_dim ==0:
            self.card_din.delete(0,END)
            self.cont_dim=self.cont_dim+1

    def limpa_deb(self):
        self.conta_dim()
        if self.cont_deb==0:
            self.card_cartao_deb.delete(0,END)
            self.cont_deb=self.cont_deb+1

    def limpa_cre(self):
        self.conta_dim()
        if self.cont_cre==0:
            self.card_cartao_cre.delete(0,END)
            self.cont_cre=self.cont_cre+1

    def limpa_desc(self):
        if self.cont_desc==0:
            self.card_desc.delete(0,END)
            self.cont_desc=self.cont_desc+1

    