import sqlite3
import re
import tkinter as tk
from tkinter import Label,ttk,messagebox
from tkinter import *
from PIL import Image, ImageTk
import random
import crcmod
import qrcode
class F_caixa():
    def fechar_venda(self,id):
        self.id_fecha=id
        self.din_zero = StringVar(value="00,00")
        self.deb_zero = StringVar(value="00,00")
        self.pix_zero = StringVar(value="00,00")
        self.cre_zero = StringVar(value="00,00")
        self.desc_zero = StringVar(value="00,00")
        self.fecha_caixa=Toplevel(self.caixa_frame,width=1000,height=500,bd=2,bg="#787777")
        self.fecha_caixa.geometry("+200+150")
        self.fecha_caixa.resizable(False,False)
        self.fecha_caixa.iconbitmap('ImageTk/logo.ico')
        self.fecha_caixa.title("Fechar venda...")
        self.fechar_venda_()
    def fechar_venda_(self):
        self.canvas = Canvas(self.fecha_caixa, width=1000, height=500, bg='black')
        for _ in range(random.randint(100,1000)):
            x = random.randint(0, 1000)
            y = random.randint(0, 500)
            tamanho = random.uniform(0.5, 3)
            self.canvas.create_oval(x, y, x + tamanho, y + tamanho, fill='white', outline='white')
        self.canvas.place(x=0,y=0)  
        self.fecha_caixa.focus_set()
        self.ven_valo_texto = Label(self.canvas,text="Valor:", font="Arial 12", bg="black", foreground="white")
        self.ven_valo_texto.place(x=5, y=5)
        self.valor_venda_cx=LabelFrame(self.canvas,width=200,height=25,font="Arial 12",bd=0,bg="#adacac",foreground="white")
        self.valor_venda_cx.place(x=75,y=5)

        self.ven_cliente_texto = Label(self.canvas,text="Cliente:", font="Arial 12", bg="black", foreground="white")
        self.ven_cliente_texto.place(x=720, y=5)
        
        self.valor_venda=LabelFrame(self.canvas,width=200,height=25,font="Arial 12",bd=0,bg="#adacac")
        self.valor_venda.place(x=790,y=5)

        self.confirma_venda=Button(self.canvas,width=10,text="Confirmar",bg="orange",fg="dimgray",font="arial 12",command=self.finaliza,foreground="white",bd=3)
        self.confirma_venda.place(x=880,y=400)

        self.voltar_fecha_vnd=Button(self.canvas,width=10,text="Voltar",bg="orange",fg="dimgray",font="arial 12",foreground="white",command=self.volta_caixa_f,bd=3)
        self.voltar_fecha_vnd.place(x=880,y=450)
        
        self.opicoes=LabelFrame(self.canvas,width=200,height=35,text="Forma de PG:",font="Arial 20",bd=0,bg="black",foreground="#04ff00")
        self.opicoes.place(x=520,y=20)
        
        self.opicoes_din_f=LabelFrame(self.canvas,width=450,height=70,font="Arial 15",bd=2,bg="black")
        self.opicoes_din_f.place(x=520,y=50)

        self.opicoes_din=LabelFrame(self.opicoes_din_f,width=200,height=25,text="DINHEIRO:",font="Arial 15",bd=0,bg="black",foreground="#ccff00")
        self.opicoes_din.place(x=200,y=0)

        self.card_din=Entry(self.opicoes_din_f,width=20,font="Arial 12",textvariable=self.din_zero,foreground="blue")
        self.card_din.bind("<KeyPress-v>",lambda event:self.volta_caixa_f())
        self.card_din.bind("<Return>",lambda event:self.card_cartao_deb.focus())
        self.card_din.bind("<KeyRelease>",lambda event:self.limpa_dim())
        self.card_din.bind("<KeyPress-f>",lambda event:self.finaliza())
        self.card_din.bind("<KeyPress-t>",lambda event:self.total_entry_din())
        self.card_din.place(x=200,y=28,height=30)
        self.opicoes_pix=LabelFrame(self.opicoes_din_f,width=150,height=25,text="PIX:",font="Arial 15",bd=0,bg="black",foreground="#ccff00")
        self.opicoes_pix.place(x=5,y=0)

        self.card_pix=Entry(self.opicoes_din_f,width=20,font="Arial 12",textvariable=self.pix_zero,foreground="blue")
        self.card_pix.bind("<KeyPress-v>",lambda event:self.volta_caixa_f())
        self.card_pix.bind("<Return>",lambda event:self.card_din.focus())
        self.card_pix.bind("<KeyPress>",lambda event:self.limpa_pix())
        self.card_pix.bind("<KeyRelease>",lambda event:self.conta_dim())
        self.card_pix.bind("<KeyPress-f>",lambda event:self.finaliza())
        self.card_pix.bind("<KeyPress-t>",lambda event:self.total_entry_pix())
        self.card_pix.place(x=5,y=28,height=30)
        self.card_pix.focus()

        self.opicoes_cartao=LabelFrame(self.canvas,width=450,height=100,text="CARTAO:",font="Arial 15",bd=2,bg="black",foreground="#04ff00")
        self.opicoes_cartao.place(x=520,y=120)

        self.opicoes_deb=LabelFrame(self.opicoes_cartao,width=200,height=25,text="DEBITO:",font="Arial 15",bd=0,bg="black",foreground="#ccff00")
        self.opicoes_deb.place(x=0,y=0)

        self.card_cartao_deb=Entry(self.opicoes_cartao,width=20,font="Arial 12",textvariable=self.deb_zero,foreground="blue")
        self.card_cartao_deb.bind("<KeyPress-v>",lambda event:self.volta_caixa_f())
        self.card_cartao_deb.bind("<Return>",lambda event:self.card_cartao_cre.focus())
        self.card_cartao_deb.bind("<KeyPress>",lambda event:self.limpa_deb())
        self.card_cartao_deb.bind("<KeyRelease>",lambda event:self.conta_dim())
        self.card_cartao_deb.bind("<KeyPress-f>",lambda event:self.finaliza())
        self.card_cartao_deb.bind("<KeyPress-t>",lambda event:self.total_entry_deb())
        self.card_cartao_deb.place(x=5,y=28,height=30)
        
        self.opicoes_cre=LabelFrame(self.opicoes_cartao,width=200,height=25,text="CREDITO:",font="Arial 15",bd=0,bg="black",foreground="#ccff00")
        self.opicoes_cre.place(x=200,y=0) 

        self.card_cartao_cre=Entry(self.opicoes_cartao,width=20,font="Arial 12",textvariable=self.cre_zero,foreground="blue")
        self.card_cartao_cre.bind("<KeyPress-v>",lambda event:self.volta_caixa_f())
        self.card_cartao_cre.bind("<Return>",lambda event:self.card_desc.focus())
        self.card_cartao_cre.bind("<KeyPress>",lambda event:self.limpa_cre())
        self.card_cartao_cre.bind("<KeyRelease>",lambda event:self.conta_dim())
        self.card_cartao_cre.bind("<KeyPress-f>",lambda event:self.finaliza())
        self.card_cartao_cre.bind("<KeyPress-t>",lambda event:self.total_entry_cre())
        self.card_cartao_cre.place(x=200,y=28,height=30)
        
        self.opicoes_desc=LabelFrame(self.canvas,width=450,height=75,text="DESCONTO:",font="Arial 15",bd=1,bg="black",foreground="#ccff00")
        self.opicoes_desc.place(x=520,y=320) 

        self.card_desc=Entry(self.opicoes_desc,width=20,font="Arial 12",textvariable=self.desc_zero,bd=1,foreground="blue")
        self.card_desc.bind("<KeyPress-v>",lambda event:self.volta_caixa_f())
        self.card_desc.bind("<Return>",lambda event:self.card_pix.focus())
        self.card_desc.bind("<KeyPress>",lambda event:self.limpa_desc())
        self.card_desc.bind("<KeyRelease>",lambda event:self.conta_dim())
        self.card_desc.bind("<KeyPress-f>",lambda event:self.finaliza())
        self.card_desc.place(x=5,y=5,height=30)

        self.dados_venda=LabelFrame(self.canvas,width=500,height=400,bd=0,bg="black")
        self.dados_venda.place(x=10,y=50)   
        
        banco=sqlite3.connect('banco.db')
        b=banco.cursor()
        
        if self.id_fecha is None:
            b.execute("SELECT Id FROM Venda ORDER BY Id DESC LIMIT 1")
            Id_venda = b.fetchone()
            Id_venda = re.sub(r"[^\d,\.\d{0,2}$]+", "", str(Id_venda)).replace(",", "")
            Id_venda=float(Id_venda)-1
        else:
            Id_venda=self.id_fecha
        Id_venda_1=float(Id_venda)
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
                if self.Valor is None: self.Valor=0
                self.valor_venda.config(text=f"{Cliente}")
                self.valor_venda_cx.config(text=f"{self.Valor}R$")

        else:
            self.mesa_base()
            self.fecha_caixa.destroy()
            
        if Id_venda_1 is not None:
            Nu_1 = Id_venda_1
            Nu =re.sub(r'[^\d,\.\d{0,2}$]+', '', str(Nu_1)).replace(',', '') 

        self.numero_venda_texto_f=Label(self.canvas,font="Arial 12 ",text=f"Venda N°:{Nu}",bg="black", foreground="white")
        self.numero_venda_texto_f.place(x=400,y=5)
        
        self.cont_dim=0
        self.cont_pix=0
        self.cont_deb=0
        self.cont_cre=0
        self.cont_desc=0

        self.conta_dim()
    def total_entry_din(self):
        self.din_zero = StringVar(value=self.Valor)
        self.deb_zero = StringVar(value="00,00")
        self.cre_zero = StringVar(value="00,00")
        self.desc_zero = StringVar(value="00,00")
        self.pix_zero = StringVar(value="00,00")
        self.canvas.place_forget()
        self.fechar_venda_()

    def total_entry_deb(self):
        self.deb_zero = StringVar(value=self.Valor)
        self.din_zero = StringVar(value="00,00")
        self.cre_zero = StringVar(value="00,00")
        self.desc_zero = StringVar(value="00,00")
        self.pix_zero = StringVar(value="00,00")
        self.canvas.place_forget()
        self.fechar_venda_()
    def total_entry_cre(self):
        self.cre_zero = StringVar(value=self.Valor)
        self.din_zero = StringVar(value="00,00")
        self.deb_zero = StringVar(value="00,00")
        self.desc_zero = StringVar(value="00,00")
        self.pix_zero = StringVar(value="00,00")
        self.canvas.place_forget()
        self.fechar_venda_()
    def total_entry_pix(self):
        self.pix_zero = StringVar(value=self.Valor)
        self.cre_zero = StringVar(value="00,00")
        self.din_zero = StringVar(value="00,00")
        self.deb_zero = StringVar(value="00,00")
        self.desc_zero = StringVar(value="00,00")
        self.canvas.place_forget()
        self.fechar_venda_()
    def conta_dim(self):
        self.dim=self.card_din.get().replace(",",".")
        self.cre=self.card_cartao_cre.get().replace(",",".")
        self.deb=self.card_cartao_deb.get().replace(",",".")  
        self.pix=self.card_pix.get().replace(",",".")
        self.des=self.card_desc.get().replace(",",".")    
        if self.dim=="":self.dim=0
        if self.cre=="":self.cre=0
        if self.deb=="":self.deb=0
        if self.pix=="":self.pix=0
        if self.des=="":self.des=0
        self.dim=float(self.dim)
        self.cre=float(self.cre)
        self.deb=float(self.deb)
        self.pix=float(self.pix)
        self.des=float(self.des)
        self.conta=-self.Valor+(self.dim + self.cre + self.deb+self.pix+self.des)
        self.conta=round(self.conta,2)
        self.conta=str(self.conta).replace(".",",")

        self.opicoes_final=LabelFrame(self.canvas,width=300,height=70,font="Arial 15",bd=2,bg="black")
        self.opicoes_final.place(x=520,y=400)

        self.Venda_valor=LabelFrame(self.opicoes_final,width=290,height=50,text=f"R$ {self.conta}",font="Arial 30",bd=0,bg="black",foreground="white")
        self.Venda_valor.place(x=5,y=10)

    def finaliza(self):
        if self.pix>0:
            self.paga_pix(self.pix)
        else:
            self.paga()
    def paga(self):
        banco=sqlite3.connect('banco.db')
        b=banco.cursor()
        add_if=float(self.dim) + float(self.cre) + float(self.deb)+float(self.pix)
        if add_if >= self.Valor:    
            b.execute("UPDATE venda SET dim=?, cre=?, deb=? , troco=?,Status=?,pix=? WHERE Id=?", (self.dim,self.cre,self.deb,self.conta,"Fechada",self.pix,self.id_vendaL))
            banco.commit()
            self.volta_caixa_f()
            self.fecha_volta()
        else:
            messagebox.showerror("Valor errado","Pagemento insuficiente")
            self.card_din.focus()
            self.limpa_geral()


    def volta_caixa_f(self):
        self.canvas.place_forget()
        self.fecha_caixa.destroy()

    def limpa_geral(self):
        self.canvas.place_forget()
        self.fechar_venda_()

    def limpa_pix(self):
        if self.cont_pix ==0:
            self.card_pix.delete(0,END)
            self.cont_pix+=1

    def limpa_dim(self):
        if self.cont_dim ==0:
            self.card_din.delete(0,END)
            self.cont_dim+=1

    def limpa_deb(self):
        if self.cont_deb==0:
            self.card_cartao_deb.delete(0,END)
            self.cont_deb+=1

    def limpa_cre(self):
        if self.cont_cre==0:
            self.card_cartao_cre.delete(0,END)
            self.cont_cre+=1

    def limpa_desc(self):
        if self.cont_desc==0:
            self.card_desc.delete(0,END)
            self.cont_desc+=1



    #-------------------------------------------------------------------------------------------------------------------------------------------------------
  
    def paga_pix(self,valor):
        self.tela_prin=Toplevel(self.fecha_caixa)
        self.tela_prin.geometry("500x600+50+10")
        self.tela_prin.title("Gerar Qr_code:)")
        self.tela_prin.iconbitmap('ImageTk/qr_code.ico')
        self.tela_prin.resizable(False, False)
        largura = 1195
        altura = 795
        self.fundim = Canvas(self.tela_prin, width=largura, height=altura, bg='black')
        for _ in range(random.randint(100,1000)):
            x = random.randint(0, largura)
            y = random.randint(0, altura)
            tamanho = random.uniform(0.5, 3)
            self.fundim.create_oval(x, y, x + tamanho, y + tamanho, fill='white', outline='white')
        self.fundim.place(x=0,y=0)     
        banco=sqlite3.connect('banco.db')
        b=banco.cursor()
        b.execute("SELECT gmail,cell,cnpj,pix FROM empresa WHERE nome=?", ("Giuseph",))
        dados = b.fetchone()
        gmail,cell,cnpj,pix=dados
        if pix=="TELEFONE":chave=f"+55{cell}"
        if pix=="CPF/CNPJ":chave=cnpj
        if pix=="GMAIL":chave=gmail
        if chave and valor !="":
            self.nome="Nome Sobrenome"
            self.chave=chave
            self.valor= "{:.2f}".format(float(valor))
            self.cidade="SINOP_MT"
            self.txt="LOJA01"
            self.payloadFormato= "000201"
            self.merchantCategoria="52040000"
            self.transationCurrect="5303986"
            self.contraCode="5802BR"
            self.nome_tamanho=len(self.nome)
            self.chave_tamanho=len(self.chave)
            self.valor_tamanho=len(self.valor)
            self.cidade_tamanho=len(self.cidade)
            self.txt_tamanho=len(self.txt)
            self.merchantAccont_tam=f"0014BR.GOV.BCB.PIX01{self.chave_tamanho}{self.chave}"
            self.merchantAccont=f"26{len(self.merchantAccont_tam)}{self.merchantAccont_tam}"
            self.transationAmount_valor_tam=f"0{self.valor_tamanho}{self.valor}"
            if self.txt_tamanho<=9:
                self.Data_tam=f"050{self.txt_tamanho}{self.txt}"
            else:
                self.Data_tam=f"05{self.txt_tamanho}{self.txt}"
            if self.nome_tamanho<=9:
                self.nome_tamanho=f"0{self.nome_tamanho}"
            if self.cidade_tamanho<=9:
                self.cidade_tamanho=f"0{self.cidade_tamanho}"
            self.transationAmount_valor=f"54{self.transationAmount_valor_tam}"
            self.merchant_Nome=f"59{self.nome_tamanho}{self.nome}"
            self.city=f"60{self.cidade_tamanho}{self.cidade}"
            self.Data=f"62{len(self.Data_tam)}{self.Data_tam}"
            self.crc16="6304"
            self.payload=f"{self.payloadFormato}{self.merchantAccont}{self.merchantCategoria}{self.transationCurrect}{self.transationAmount_valor}{self.contraCode}{self.merchant_Nome}{self.city}{self.Data}{self.crc16}"
            crc16=crcmod.mkCrcFun(poly=0x11021,initCrc=0xFFFF,rev=False,xorOut=0x0000)
            self.crc16codigo=hex(crc16(str(self.payload).encode("utf-8")))
            self.crc16codigo_formatado=str(self.crc16codigo).replace("0x","").upper()
            self.payload_pronta=f"{self.payload}{self.crc16codigo_formatado}"
            self.qrcode_=qrcode.make(self.payload_pronta)
            self.qrcode_.save("ImageTk/qr_code_principal.png")
            self.imagem_qrcode = Image.open("ImageTk/qr_code_principal.png")
            self.imagem_qrcode = self.imagem_qrcode.resize((500, 500), Image.LANCZOS)
            self.qrcode_img = ImageTk.PhotoImage(self.imagem_qrcode)
            self.desenho = Label(self.fundim, image=self.qrcode_img,foreground="black")
            self.desenho.place(x=0, y=30)
            self.novo = Button(self.fundim, text="Confirma pagamento",command=self.volta, font="arial 11 bold", height=1, fg="white", bg="black", bd=3)
            self.novo.bind("<Return>",lambda event: self.volta())
            self.novo.place(x=150, y=540)
            self.novo.focus_force()
            self.valor_label = Label(self.fundim, text=f"{self.valor}R$", font="arial 14 bold", bg="Black", fg="white")
            self.valor_label.place(x=200, y=0)
        else: 
            messagebox.showinfo("Aviso","Chave Pix ou Valor nao inserido!")
    def volta(self):
        self.tela_prin.destroy()
        self.paga()
