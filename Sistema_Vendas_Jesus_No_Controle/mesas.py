import sqlite3
import re
import tkinter as tk
from tkinter import Label,ttk,messagebox
from tkinter import *
from fechamento_cx import F_caixa

class mes_geral():
    def mesa_base(self):
        self.mesas_frame=LabelFrame(self.caixa_frame,bd=0,bg="#787777")
        self.mesas_frame.place(x=0,y=0,relwidth=1,relheight=1)

        self.mesas_text=Label(self.mesas_frame,text="MESAS",font="Arial 20 bold",bg="#787777",foreground="white",bd=0)
        self.mesas_text.place(x=20,y=20)

        self.entri_comandos=Entry(self.mesas_frame,width=1,font="Arial 1 bold",bd=0,bg="white")
        self.entri_comandos.bind("<KeyPress-v>",lambda event:self.volta_cx())
        self.entri_comandos.bind("<Return>",lambda event:self.button_mesas1.focus())
        self.entri_comandos.bind("<KeyPress-1>",lambda event:self.mesa_buton1())
        self.entri_comandos.bind("<KeyPress-2>",lambda event:self.mesa_buton2())
        self.entri_comandos.bind("<KeyPress-3>",lambda event:self.mesa_buton3())
        self.entri_comandos.bind("<KeyPress-4>",lambda event:self.mesa_buton4())
        self.entri_comandos.bind("<KeyPress-5>",lambda event:self.mesa_buton5())
        self.entri_comandos.bind("<KeyPress-6>",lambda event:self.mesa_buton6())
        self.entri_comandos.bind("<KeyPress-7>",lambda event:self.mesa_buton7())
        self.entri_comandos.bind("<KeyPress-8>",lambda event:self.mesa_buton8())
        self.entri_comandos.bind("<KeyPress-9>",lambda event:self.mesa_buton9())
        self.entri_comandos.place(x=0,y=8000,height=1)
        self.entri_comandos.focus()
        Banco = sqlite3.connect('banco.db')
        b = Banco.cursor()
        b.execute("SELECT Id FROM Venda WHERE Status = 'Aberto'")
        id=b.fetchall()
        if id is not None:
            self.id1, self.id2, self.id3, self.id4, self.id5, self.id6, self.id7, self.id8, self.id9, self.id10 = id[:10] + [None] * (10 - len(id))
        b.execute("SELECT Cliente FROM Venda WHERE Status = 'Aberto'")
        Cliente=b.fetchall()
        if Cliente is not None:
            Cliente1,Cliente2,Cliente3,Cliente4,Cliente5,Cliente6,Cliente7,Cliente8,Cliente9,Cliente10,*Cliente_resto=Cliente[:10] + [None] * (10 - len(Cliente))
            Cliente1 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(Cliente1)).replace("Consumidor","").replace(",","")
            Cliente2 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(Cliente2)).replace("Consumidor","").replace(",","")
            Cliente3 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(Cliente3)).replace("Consumidor","").replace(",","")
            Cliente4 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(Cliente4)).replace("Consumidor","").replace(",","")
            Cliente5 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(Cliente5)).replace("Consumidor","").replace(",","")
            Cliente6 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(Cliente6)).replace("Consumidor","").replace(",","")            
            Cliente7 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(Cliente7)).replace("Consumidor","").replace(",","")
            Cliente8 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(Cliente8)).replace("Consumidor","").replace(",","")
            Cliente9 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(Cliente9)).replace("Consumidor","").replace(",","")
            Cliente10 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(Cliente10)).replace("Consumido","").replace(",","")
            
        if Cliente1 == "0" or self.id1 ==None :
            self.button_mesas1=Button(self.mesas_frame,width=10,height=4,text="Vazio",command=self.volta_cx,font="Arial 15 bold",bd=1,bg="white")
            self.button_mesas1.bind("<Return>",lambda event:self.volta_cx())
            self.button_mesas1.place(x=50,y=80)
        else:
            self.mesas_text1=Label(self.mesas_frame,text="1",font="Arial 15 bold",bg="#787777",foreground="white",bd=0)
            self.mesas_text1.place(x=105,y=50)
            self.button_mesas1=Button(self.mesas_frame,width=10,height=3,font="Arial 15 bold",bd=1,command=self.mesa_buton1,bg="white")
            self.button_mesas1.config(text=self.id1)
            self.button_mesas1.bind("<Return>",lambda event:self.mesa_buton1())
            self.button_mesas1.bind("<Right>",lambda event:self.button_mesas2.focus())
            self.button_mesas1.place(x=50,y=80)
            self.txt_buton1=Button(self.mesas_frame,width=10,height=1,font="Arial 15 bold",bd=1,command=self.mesa_buton1,bg="white")
            self.txt_buton1.config(text=Cliente1)
            self.txt_buton1.place(x=50,y=168)
            if Cliente2 == "0" or self.id2 ==None :
                self.button_mesas2=Button(self.mesas_frame,width=10,height=4,text="Vazio",command=self.volta_cx,font="Arial 15 bold",bd=1,bg="white")
                self.button_mesas2.bind("<Return>",lambda event:self.volta_cx())
                self.button_mesas2.bind("<Left>",lambda event:self.button_mesas1.focus())
                self.button_mesas2.place(x=200,y=80)
            else:
                self.mesas_text2=Label(self.mesas_frame,text="2",font="Arial 15 bold",bg="#787777",foreground="white",bd=0)
                self.mesas_text2.place(x=265,y=50)     
                self.button_mesas2=Button(self.mesas_frame,width=10,height=3,font="Arial 15 bold",command=self.mesa_buton2,bd=1,bg="white")
                self.button_mesas2.config(text=self.id2)
                self.button_mesas2.place(x=200,y=80)
                self.button_mesas2.bind("<Return>",lambda event:self.mesa_buton2())
                self.button_mesas2.bind("<Right>",lambda event:self.button_mesas3.focus())
                self.button_mesas2.bind("<Left>",lambda event:self.button_mesas1.focus())
                self.txt_buton2=Button(self.mesas_frame,width=10,height=1,font="Arial 15 bold",command=self.mesa_buton2,bd=1,bg="white")
                self.txt_buton2.config(text=Cliente2)
                self.txt_buton2.place(x=200,y=168)
                if Cliente3 == "0" or self.id3 ==None:
                    self.button_mesas3=Button(self.mesas_frame,width=10,height=4,text="Vazio",command=self.volta_cx,font="Arial 15 bold",bd=1,bg="white")
                    self.button_mesas3.bind("<Return>",lambda event:self.volta_cx())
                    self.button_mesas3.bind("<Left>",lambda event:self.button_mesas2.focus())
                    self.button_mesas3.place(x=350,y=80)
                else:
                    self.mesas_text3=Label(self.mesas_frame,text="3",font="Arial 15 bold",bg="#787777",foreground="white",bd=0)
                    self.mesas_text3.place(x=405,y=50)    
                    self.button_mesas3=Button(self.mesas_frame,width=10,height=3,font="Arial 15 bold",command=self.mesa_buton3,bd=1,bg="white")
                    self.button_mesas3.config(text=self.id3)
                    self.button_mesas3.bind("<Return>",lambda event:self.mesa_buton3())
                    self.button_mesas3.bind("<Right>",lambda event:self.button_mesas4.focus())
                    self.button_mesas3.bind("<Left>",lambda event:self.button_mesas2.focus())
                    self.button_mesas3.place(x=350,y=80)
                    self.txt_buton3=Button(self.mesas_frame,width=10,height=1,font="Arial 15 bold",command=self.mesa_buton3,bd=1,bg="white")
                    self.txt_buton3.config(text=Cliente3)
                    self.txt_buton3.place(x=350,y=168)
                    if Cliente4 == "0" or self.id4 ==None:
                        self.button_mesas4=Button(self.mesas_frame,width=10,height=4,text="Vazio",command=self.volta_cx,font="Arial 15 bold",bd=1,bg="white")
                        self.button_mesas4.bind("<Return>",lambda event:self.volta_cx())
                        self.button_mesas4.bind("<Left>",lambda event:self.button_mesas3.focus())
                        self.button_mesas4.place(x=500,y=80)
                    else:
                        self.mesas_text4=Label(self.mesas_frame,text="4",font="Arial 15 bold",bg="#787777",foreground="white",bd=0)
                        self.mesas_text4.place(x=565,y=50)    
                        self.button_mesas4=Button(self.mesas_frame,width=10,height=3,font="Arial 15 bold",command=self.mesa_buton4,bd=1,bg="white")
                        self.button_mesas4.config(text=self.id4)
                        self.button_mesas4.bind("<Return>",lambda event:self.mesa_buton4())
                        self.button_mesas4.bind("<Right>",lambda event:self.button_mesas5.focus())
                        self.button_mesas4.bind("<Left>",lambda event:self.button_mesas3.focus())
                        self.button_mesas4.place(x=500,y=80)
                        self.txt_buton4=Button(self.mesas_frame,width=10,height=1,font="Arial 15 bold",command=self.mesa_buton4,bd=1,bg="white")
                        self.txt_buton4.config(text=Cliente4)
                        self.txt_buton4.place(x=500,y=168)
                        if Cliente5 == "0" or self.id5 ==None :
                            self.button_mesas5=Button(self.mesas_frame,width=10,height=4,text="Vazio",command=self.volta_cx,font="Arial 15 bold",bd=1,bg="white")
                            self.button_mesas5.bind("<Return>",lambda event:self.volta_cx())
                            self.button_mesas5.bind("<Left>",lambda event:self.button_mesas4.focus())
                            self.button_mesas5.place(x=650,y=80)
                        else:
                            self.mesas_text5=Label(self.mesas_frame,text="5",font="Arial 15 bold",bg="#787777",foreground="white",bd=0)
                            self.mesas_text5.place(x=705,y=50)    
                            self.button_mesas5=Button(self.mesas_frame,width=10,height=3,font="Arial 15 bold",command=self.mesa_buton5,bd=1,bg="white")
                            self.button_mesas5.config(text=self.id5)
                            self.button_mesas5.bind("<Return>",lambda event:self.mesa_buton5())
                            self.button_mesas5.bind("<Right>",lambda event:self.button_mesas6.focus())
                            self.button_mesas5.bind("<Left>",lambda event:self.button_mesas4.focus())
                            self.button_mesas5.place(x=650,y=80)
                            self.txt_buton5=Button(self.mesas_frame,width=10,height=1,font="Arial 15 bold",command=self.mesa_buton5,bd=1,bg="white")
                            self.txt_buton5.config(text=Cliente5)
                            self.txt_buton5.place(x=650,y=168)
                            if Cliente6 == "0" or self.id6 ==None:
                                self.button_mesas6=Button(self.mesas_frame,width=10,height=4,text="Vazio",command=self.volta_cx,font="Arial 15 bold",bd=1,bg="white")
                                self.button_mesas6.bind("<Return>",lambda event:self.volta_cx())
                                self.button_mesas6.bind("<Left>",lambda event:self.button_mesas5.focus())
                                self.button_mesas6.place(x=800,y=80)
                            else:
                                self.mesas_text6=Label(self.mesas_frame,text="6",font="Arial 15 bold",bg="#787777",foreground="white",bd=0)
                                self.mesas_text6.place(x=850,y=50)    
                                self.button_mesas6=Button(self.mesas_frame,width=10,height=3,font="Arial 15 bold",command=self.mesa_buton6,bd=1,bg="white")
                                self.button_mesas6.config(text=self.id6)
                                self.button_mesas6.bind("<Return>",lambda event:self.mesa_buton6())
                                self.button_mesas6.bind("<Right>",lambda event:self.button_mesas7.focus())
                                self.button_mesas6.bind("<Left>",lambda event:self.button_mesas5.focus())
                                self.button_mesas6.place(x=800,y=80)
                                self.txt_buton6=Button(self.mesas_frame,width=10,height=1,font="Arial 15 bold",command=self.mesa_buton6,bd=1,bg="white")
                                self.txt_buton6.config(text=Cliente6)
                                self.txt_buton6.place(x=800,y=168)
                                if Cliente7 == "0" or self.id7 ==None:
                                    self.button_mesas7=Button(self.mesas_frame,width=10,height=4,text="Vazio",command=self.volta_cx,font="Arial 15 bold",bd=1,bg="white")
                                    self.button_mesas7.bind("<Return>",lambda event:self.volta_cx())
                                    self.button_mesas7.bind("<Left>",lambda event:self.button_mesas6.focus())
                                    self.button_mesas7.place(x=950,y=80)
                                else:
                                    self.mesas_text7=Label(self.mesas_frame,text="7",font="Arial 15 bold",bg="#787777",foreground="white",bd=0)
                                    self.mesas_text7.place(x=1005,y=50)    
                                    self.button_mesas7=Button(self.mesas_frame,width=10,height=3,font="Arial 15 bold",command=self.mesa_buton7,bd=1,bg="white")
                                    self.button_mesas7.config(text=self.id7)
                                    self.button_mesas7.bind("<Return>",lambda event:self.mesa_buton7())
                                    self.button_mesas7.bind("<Right>",lambda event:self.button_mesas8.focus())
                                    self.button_mesas7.bind("<Left>",lambda event:self.button_mesas6.focus())
                                    self.button_mesas7.place(x=950,y=80)
                                    self.txt_buton7=Button(self.mesas_frame,width=10,height=1,font="Arial 15 bold",command=self.mesa_buton7,bd=1,bg="white")
                                    self.txt_buton7.config(text=Cliente7)
                                    self.txt_buton7.place(x=950,y=168)
                                    if Cliente8 == "0" or self.id8 ==None:
                                        self.button_mesas8=Button(self.mesas_frame,width=10,height=4,text="Vazio",command=self.volta_cx,font="Arial 15 bold",bd=1,bg="white")
                                        self.button_mesas8.bind("<Return>",lambda event:self.volta_cx())
                                        self.button_mesas8.bind("<Left>",lambda event:self.button_mesas7.focus())
                                        self.button_mesas8.place(x=1100,y=80)
                                    else:
                                        self.mesas_text8=Label(self.mesas_frame,text="8",font="Arial 15 bold",bg="#787777",foreground="white",bd=0)
                                        self.mesas_text8.place(x=1150,y=50)    
                                        self.button_mesas8=Button(self.mesas_frame,width=10,height=3,font="Arial 15 bold",command=self.mesa_buton7,bd=1,bg="white")
                                        self.button_mesas8.config(text=self.id8)
                                        self.button_mesas8.bind("<Return>",lambda event:self.mesa_buton8())
                                        self.button_mesas8.bind("<Right>",lambda event:self.button_mesas9.focus())
                                        self.button_mesas8.bind("<Left>",lambda event:self.button_mesas7.focus())
                                        self.button_mesas8.place(x=1100,y=80)
                                        self.txt_buton8=Button(self.mesas_frame,width=10,height=1,font="Arial 15 bold",command=self.mesa_buton7,bd=1,bg="white")
                                        self.txt_buton8.config(text=Cliente8)
                                        self.txt_buton8.place(x=1100,y=168)
                                        if Cliente9 == "0" or self.id9 ==None:
                                            self.button_mesas9=Button(self.mesas_frame,width=10,height=4,text="Vazio",command=self.volta_cx,font="Arial 15 bold",bd=1,bg="white")
                                            self.button_mesas9.bind("<Return>",lambda event:self.volta_cx())
                                            self.button_mesas9.bind("<Left>",lambda event:self.button_mesas8.focus())
                                            self.button_mesas9.place(x=50,y=260)
                                        else:
                                            self.mesas_text9=Label(self.mesas_frame,text="9",font="Arial 15 bold",bg="#787777",foreground="white",bd=0)
                                            self.mesas_text9.place(x=105,y=230)    
                                            self.button_mesas9=Button(self.mesas_frame,width=10,height=3,font="Arial 15 bold",command=self.mesa_buton7,bd=1,bg="white")
                                            self.button_mesas9.config(text=self.id9)
                                            self.button_mesas9.bind("<Return>",lambda event:self.mesa_buton9())
                                            self.button_mesas9.bind("<Right>",lambda event:self.button_mesas10.focus())
                                            self.button_mesas9.bind("<Left>",lambda event:self.button_mesas8.focus())
                                            self.button_mesas9.place(x=50,y=260)
                                            self.txt_buton9=Button(self.mesas_frame,width=10,height=1,font="Arial 15 bold",command=self.mesa_buton7,bd=1,bg="white")
                                            self.txt_buton9.config(text=Cliente9)
                                            self.txt_buton9.place(x=50,y=348)
                                            if Cliente10 == "0" or self.id10 ==None:
                                                self.button_mesas10=Button(self.mesas_frame,width=10,height=4,text="Vazio",command=self.volta_cx,font="Arial 15 bold",bd=1,bg="white")
                                                self.button_mesas10.bind("<Return>",lambda event:self.volta_cx())
                                                self.button_mesas10.bind("<Left>",lambda event:self.button_mesas9.focus())
                                                self.button_mesas10.place(x=200,y=260)
                                            else:
                                                self.mesas_text10=Label(self.mesas_frame,text="10",font="Arial 15 bold",bg="#787777",foreground="white",bd=0)
                                                self.mesas_text10.place(x=265,y=230)    
                                                self.button_mesas10=Button(self.mesas_frame,width=10,height=3,font="Arial 15 bold",command=self.mesa_buton7,bd=1,bg="white")
                                                self.button_mesas10.config(text=self.id10)
                                                self.button_mesas10.bind("<Return>",lambda event:self.mesa_buton10())
                                                self.button_mesas10.bind("<Left>",lambda event:self.button_mesas9.focus())
                                                self.button_mesas10.place(x=200,y=260)
                                                self.txt_buton10=Button(self.mesas_frame,width=10,height=1,font="Arial 15 bold",command=self.mesa_buton7,bd=1,bg="white")
                                                self.txt_buton10.config(text=Cliente10)
                                                self.txt_buton10.place(x=200,y=348)
    def volta_cx(self):
        self.mesas_frame.destroy()
        self.reload_aba()

    def mesa_buton1(self):
        self.Id_venda=self.id1
        self.Id_venda = re.sub(r'[^\d,\.\d{0,2}$]+', '', str(self.Id_venda)).replace(',', '') 
        self.principal_frame_mesa()

    def mesa_buton2(self):
        self.Id_venda=self.id2
        self.Id_venda = re.sub(r'[^\d,\.\d{0,2}$]+', '', str(self.Id_venda)).replace(',', '') 
        self.principal_frame_mesa()

    def mesa_buton3(self):
        self.Id_venda=self.id3
        self.Id_venda = re.sub(r'[^\d,\.\d{0,2}$]+', '', str(self.Id_venda)).replace(',', '') 
        self.principal_frame_mesa()

    def mesa_buton4(self):
        self.Id_venda=self.id4
        self.Id_venda = re.sub(r'[^\d,\.\d{0,2}$]+', '', str(self.Id_venda)).replace(',', '') 
        self.principal_frame_mesa()

    def mesa_buton5(self):
        self.Id_venda=self.id5
        self.Id_venda = re.sub(r'[^\d,\.\d{0,2}$]+', '', str(self.Id_venda)).replace(',', '') 
        self.principal_frame_mesa()

    def mesa_buton6(self):
        self.Id_venda=self.id6
        self.Id_venda = re.sub(r'[^\d,\.\d{0,2}$]+', '', str(self.Id_venda)).replace(',', '') 
        self.principal_frame_mesa()

    def mesa_buton7(self):
        self.Id_venda=self.id7
        self.Id_venda = re.sub(r'[^\d,\.\d{0,2}$]+', '', str(self.Id_venda)).replace(',', '') 
        self.principal_frame_mesa()

    def mesa_buton8(self):
        self.Id_venda=self.id8
        self.Id_venda = re.sub(r'[^\d,\.\d{0,2}$]+', '', str(self.Id_venda)).replace(',', '') 
        self.principal_frame_mesa()
    
    def mesa_buton9(self):
        self.Id_venda=self.id9
        self.Id_venda = re.sub(r'[^\d,\.\d{0,2}$]+', '', str(self.Id_venda)).replace(',', '') 
        self.principal_frame_mesa()
    
    def mesa_buton10(self):
        self.Id_venda=self.id10
        self.Id_venda = re.sub(r'[^\d,\.\d{0,2}$]+', '', str(self.Id_venda)).replace(',', '') 
        self.principal_frame_mesa()

    def principal_frame_mesa(self):
        self.janela_principal.iconbitmap('ImageTk/logo.ico')
        self.janela_principal.title("Caixa")
        self.caixa_frame1 = Frame(self.janela_principal, width=1500, height=800, bg="#616161")
        self.caixa_frame1.place(x=0, y=0)

        self.frame_bu1 = Frame(self.caixa_frame1, width=100, height=100, bg="#616161")
        self.frame_bu1.place(x=0, y=0)
        
        opcoes = ['Consumidor','Opção 1', 'Opção 2', 'Opção 3', 'Opção 4']

        # Crie a variável para armazenar a escolha do usuário
        escolha_var1 = tk.StringVar()
        escolha_var1.set(opcoes[0])

        self.amostra_itens = LabelFrame(self.caixa_frame1, width=800, height=500, bg="#c4c2c2", bd=20)
        self.amostra_itens.configure(highlightbackground="#c4c2c2")
        self.amostra_itens.place(x=500, y=80)

        Banco = sqlite3.connect('banco.db')
        b = Banco.cursor()
        b.execute('SELECT Cliente FROM Venda WHERE Id=?',(self.Id_venda,))
        cliente1=b.fetchone()

        self.def_cliente_texto = Label(self.caixa_frame1, text="Cliente:", font="Arial 12", bg="#616161", foreground="white")
        self.def_cliente_texto.place(x=500, y=2)
        self.consumidor=StringVar(value=cliente1)
        self.def_cliente_digito = ttk.Combobox(self.caixa_frame1,width=50,textvariable=escolha_var1, values=opcoes)
        self.def_cliente_digito.config(font=("arial 12"),justify='left',textvariable=self.consumidor)
        self.def_cliente_digito.bind("<Return>",lambda event:self.cdg_insert_digt1.focus())
        self.def_cliente_digito.place(x=560, y=2)

        if self.Id_venda is not None:
            Nu = self.Id_venda

        self.numero_venda_texto=Label(self.caixa_frame1,font="Arial 12 ",text=f"Venda N°:{Nu}",bg="#616161", foreground="white")
        self.numero_venda_texto.place(x=500,y=25)

        self.voltar_caixa_bu=Button(self.caixa_frame1,width=10,text="Voltar(v)",bg="orange",fg="dimgray",font="arial 14",foreground="white",command=self.voltar_usu,bd=3)
        self.voltar_caixa_bu.place(x=1225,y=730,height=25)
        self.sair_cx=Button(self.caixa_frame1,width=10,text="Sair(s)",bg="orange",fg="dimgray",font="arial 14",foreground="white",command=self.exit,bd=3)
        self.sair_cx.place(x=1225,y=700,height=25)

        
        self.fecha_venda=Button(self.caixa_frame1,text="Finalizar Venda",font="Arial 14",width=20,bd=1,bg="green",command=self.fechamento1,foreground="white")
        self.fecha_venda.place(x=1030,y=650,height=20)

        self.del_produto=Button(self.caixa_frame1,text="Deletar Produto(D)",font="Arial 14",width=20,bd=1,bg="green",command=self.Deletar_produto1,foreground="white")
        self.del_produto.place(x=1030,y=670,height=20)

        self.nova_venda_bu=Button(self.caixa_frame1,text="Nova venda(N)",font="Arial 14",width=20,bd=1,bg="green",command=self.nova_venda,foreground="white")
        self.nova_venda_bu.place(x=1030,y=20,height=25)

        self.mesas_aberta_bu=Button(self.caixa_frame1,text="Abertos(A)",font="Arial 14",width=20,bd=1,bg="yellow",command=self.mesa_base,foreground="black")
        self.mesas_aberta_bu.place(x=10,y=20,height=25)
        

        '''self.new_bu=Button(self.caixa_frame1,text="novo",font="Arial 14",width=20,bd=1,bg="green",command=self.cre_aate_button,foreground="white")
        self.new_bu.place(x=1030,y=700,height=20)'''

        self.inserir_dados1()

    def Atualiza_caixa1(self):        
        Banco = sqlite3.connect('banco.db')
        b = Banco.cursor()
        
        self.vlr_antt=00,00
        self.vlr_ant=re.sub(r'[^\d,\.\d{0,2}$]+', '', str(self.vlr_antt)) 
        
        b.execute('SELECT cdg,PRODUTO, Quantidade,PREÇO,Preco_quant FROM vendas_dados WHERE Id_venda=?', (self.Id_venda,))
        results = b.fetchall()
        
        for row in results:
            cdg,nome, qntdeL,valore,valor_finali = row   
            valor = "{:.2f}".format(round(valore, 2))
            valor_final = "{:.2f}".format(round(valor_finali, 2))
            self.frame_item=LabelFrame(self.amostra_itens,width=800,height=50,bg="#c4c2c2",bd=2)
            self.frame_item.pack(side=TOP)

            self.cdg_ex = LabelFrame(self.frame_item, text=f"({cdg})", font="Arial 14 ", width=25, bd=0, height=45, bg="#c4c2c2", foreground="black")
            self.cdg_ex.place(x=2, y=2)

            self.resu_nome = LabelFrame(self.frame_item, text="", font="Arial 14 ", width=700, bd=0, height=45, bg="#c4c2c2", foreground="black")
            self.resu_nome.place(x=25, y=2)

            self.resu_valor = LabelFrame(self.frame_item, text="", font="Arial 26 ",width=200, bd=0, height=45, bg="#c4c2c2", foreground="#48ff00")
            self.resu_valor.place(x=500, y=2)

            self.resu_valor_uni = LabelFrame(self.frame_item, text="", font="Arial 14 ", width=500, bd=0, height=45, bg="#c4c2c2", foreground="black")
            self.resu_valor_uni.place(x=2, y=25)

            self.resu_quant = LabelFrame(self.frame_item, text="", font="Arial 14 ", width=200, bd=0, height=45, bg="#c4c2c2", foreground="black")
            self.resu_quant.place(x=250, y=25)

            self.resu_nome.config(text=f"Produto= {nome}")
            self.resu_valor_uni.config(text=f"Valor unitario= {valor} R$")
            self.resu_quant.config(text=f"x{qntdeL}")
            self.resu_valor.config(text=f"= {valor_final} R$")

            b.execute("SELECT SUM(Preco_quant) FROM vendas_dados WHERE Id_venda = ?",(self.Id_venda,))
            self.vlr_antt=b.fetchone()[0]
            self.vlr_ant = "{:.2f}".format(round(self.vlr_antt, 2)).replace(".",",")

        b.close()
        Banco.close()

        self.calc_item_total_cx=LabelFrame(self.caixa_frame1,width=300,height=100,bd=2,bg="#616161",foreground="#48ff00")
        self.calc_item_total_cx.place(x=1030,y=555)

        self.calc_item_total=LabelFrame(self.calc_item_total_cx,font="Arial 40",text=f"{self.vlr_ant}R$",width=300,height=60,bd=0,bg="#616161",foreground="#48ff00")
        self.calc_item_total.pack(side=TOP)


    def calc_msm_item1(self):
        qntdeL=self.qntd_insert_digt1.get().replace(",",".")
        
        codigoL = self.cdg_insert_digt1.get()

        Banco = sqlite3.connect('banco.db')
        b = Banco.cursor()

        if qntdeL=="":
            qntdeL=1
        else:
            self.qntd_insert_digt1.focus()       
        self.conn = sqlite3.connect("banco.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM vendas_dados WHERE Id_venda=? and cdg=?", (self.Id_venda,codigoL))
        self.rows = self.cur.fetchall()
        if len(self.rows)>=1:
            b.execute('SELECT QTDE FROM Estoque WHERE Codigo=?', (codigoL,))
            qual = b.fetchone()
            qntde_up=qual
            qntd_diminui=qntde_up[0] - float(qntdeL)
            Banco.commit()
            b.execute("SELECT Quantidade,PREÇO FROM vendas_dados WHERE Id_venda=? and cdg=?", (self.Id_venda,codigoL))
            dado=b.fetchone()
            dados,valore1=dado
            qntde1 = float(qntdeL) + float(dados)
            valor_fini1 = float(valore1) * float(qntde1)  
            Banco.commit()
            self.cur.execute("UPDATE vendas_dados SET Preco_quant=?, Quantidade=? WHERE Id_venda=? AND cdg=?", (valor_fini1,qntde1, self.Id_venda, codigoL))
            self.cur.execute("UPDATE Estoque SET QTDE=? WHERE Codigo=?", (qntd_diminui, codigoL))
            self.conn.commit()
            self.reload_aba1()
        else:
            b.execute('SELECT PRODUTO, PREÇO,QTDE FROM Estoque WHERE Codigo=?', (codigoL,))
            result_a = b.fetchone()
            if result_a is not None:
                nome, valore,qtde = result_a
                qntd_diminui=qtde-float(qntdeL)
                valor_finali = valore * float(qntdeL)     
                valor = "{:.2f}".format(round(valore, 2))
                valor_final = "{:.2f}".format(round(valor_finali, 2))
                self.frame_item=LabelFrame(self.amostra_itens,width=800,height=50,bg="#c4c2c2",bd=2)
                self.frame_item.pack(side=TOP)

                self.cdg_ex = LabelFrame(self.frame_item, text=f"({self.cdg_insert_digt1.get()})", font="Arial 14 ", width=25, bd=0, height=45, bg="#c4c2c2", foreground="black")
                self.cdg_ex.place(x=2, y=2)

                self.resu_nome = LabelFrame(self.frame_item, text="", font="Arial 14 ", width=700, bd=0, height=45, bg="#c4c2c2", foreground="black")
                self.resu_nome.place(x=25, y=2)

                self.resu_valor = LabelFrame(self.frame_item, text="", font="Arial 26 ",width=200, bd=0, height=45, bg="#c4c2c2", foreground="#48ff00")
                self.resu_valor.place(x=500, y=2)

                self.resu_valor_uni = LabelFrame(self.frame_item, text="", font="Arial 14 ", width=500, bd=0, height=45, bg="#c4c2c2", foreground="black")
                self.resu_valor_uni.place(x=2, y=25)

                self.resu_quant = LabelFrame(self.frame_item, text="", font="Arial 14 ", width=200, bd=0, height=45, bg="#c4c2c2", foreground="black")
                self.resu_quant.place(x=250, y=25)

                self.resu_nome.config(text=f"Produto= {nome}")
                self.resu_valor_uni.config(text=f"Valor unitario= {valor} R$")
                self.resu_quant.config(text=f"x{qntdeL}")
                self.resu_valor.config(text=f"= {valor_final} R$")
                self.limpa_entrys1()

                try:           
                    b.execute("INSERT INTO vendas_dados (Id_venda,Cdg, PRODUTO, Quantidade, PREÇO,Preco_quant) VALUES (?, ?, ?, ?,?,?);", (self.Id_venda,codigoL, nome, qntdeL, valor,valor_final))
                    b.execute("UPDATE Estoque SET QTDE=? WHERE Codigo=?", (qntd_diminui, codigoL))
                    Banco.commit() 
                except:
                    Banco.rollback()
        
        b.execute("SELECT SUM(Preco_quant) FROM vendas_dados WHERE Id_venda = ?",(self.Id_venda,))
        self.vlr_antti=b.fetchone()[0]
        self.vlr_ant = "{:.2f}".format(round(self.vlr_antti, 2)).replace(".",",")
        
        self.calc_item_total_cx=LabelFrame(self.caixa_frame1,width=300,height=100,bd=2,bg="#616161",foreground="#48ff00")
        self.calc_item_total_cx.place(x=1030,y=555)

        self.calc_item_total=LabelFrame(self.calc_item_total_cx,font="Arial 40",text=f"{self.vlr_ant}R$",width=300,height=60,bd=0,bg="#616161",foreground="#48ff00")
        self.calc_item_total.pack(side=TOP)
        b.close()
        Banco.close()

    def inserir_dados1(self):        
        self.qntd_base=StringVar(value="1")
        self.frame_insert=LabelFrame(self.caixa_frame1,width=500,bd=2,height=200,bg="#616161")
        self.frame_insert.place(x=500,y=555)

        self.cdg_insert=Label(self.frame_insert,text="Codigo:", font="Arial 12", bg="#616161", foreground="white")
        self.cdg_insert.place(x=0, y=0)

        self.cdg_insert_digt1=Entry(self.frame_insert,width=25,bg="white",bd=1)
        self.cdg_insert_digt1.bind("<Return>",lambda event:self.ex_item1(self.cdg_insert_digt1.get()))
        self.cdg_insert_digt1.bind("<KeyPress-s>",lambda event:self.exit())
        self.cdg_insert_digt1.bind("<KeyPress-a>",lambda event:self.volta_aberto())
        self.cdg_insert_digt1.bind("<KeyPress-v>",lambda event:self.voltar_usu())
        self.cdg_insert_digt1.bind("<KeyPress-n>",lambda event:self.nova_venda())
        self.cdg_insert_digt1.bind("<KeyPress-d>",lambda event:self.Deletar_produto1())
        self.cdg_insert_digt1.bind("<KeyPress-f>",lambda event:self.fechamento1())
        self.cdg_insert_digt1.place(x=0,y=25,height=25)

        self.qntd_insert=Label(self.frame_insert,text="Quantidade:", font="Arial 12", bg="#616161", foreground="white")
        self.qntd_insert.place(x=200, y=0)

        self.qntd_insert_digt1=Entry(self.frame_insert,width=25,textvariable=self.qntd_base,bg="white",bd=1)
        self.qntd_insert_digt1.bind("<Return>",lambda event:self.calc_msm_item1())
        self.qntd_insert_digt1.bind("<KeyPress-s>",lambda event:self.exit())
        self.qntd_insert_digt1.bind("<KeyPress-a>",lambda event:self.volta_aberto())
        self.qntd_insert_digt1.bind("<KeyPress-v>",lambda event:self.voltar_usu())
        self.qntd_insert_digt1.bind("<KeyPress-n>",lambda event:self.nova_venda())
        self.qntd_insert_digt1.bind("<KeyPress-d>",lambda event:self.Deletar_produto1())
        self.qntd_insert_digt1.bind("<KeyPress-f>",lambda event:self.fechamento1())
        self.qntd_insert_digt1.bind("<Left>",lambda event:self.cdg_insert_digt1.focus())
        self.qntd_insert_digt1.place(x=200,y=25,height=25)
        self.qntd_insert_digt1.select_range(0,'end')

        Banco=sqlite3.connect('banco.db')
        b=Banco.cursor()
        b.execute('DELETE FROM vendas_dados WHERE Id_venda=? AND Quantidade=?', (self.Id_venda, 0))
        Banco.commit()
        self.cdg_insert_digt1.focus()
        self.Atualiza_caixa1()
    
    def ex_item1(self, codigoL):
        self.qntd_insert_digt1.focus()

        self.print_frame_nome=LabelFrame(self.frame_insert,text="Nome",font="Arial 18 ",width=490,bd=0,height=45,bg="#616161",foreground="white")
        self.print_frame_nome.place(x=2,y=55)
        
        self.print_frame_valor=LabelFrame(self.frame_insert,text="Valor",font="Arial 18 ",width=240,bd=0,height=45,bg="#616161",foreground="white")
        self.print_frame_valor.place(x=150,y=105)  

        self.print_frame_qntd=LabelFrame(self.frame_insert,text="Qtde",font="Arial 18 ",width=140,bd=0,height=25,bg="#616161",foreground="white")
        self.print_frame_qntd.place(x=300,y=155)  

        Banco=sqlite3.connect('banco.db')
        b=Banco.cursor()

        b.execute('SELECT PRODUTO, PREÇO, QTDE FROM Estoque WHERE Codigo=?', (codigoL,))
        result_a=b.fetchone()
        if result_a is not None:
            nome, valor, qtde = result_a
            self.print_frame_nome.config(text=f"Produto= {nome}")
            self.print_frame_valor.config(text=f"Valor= {valor} R$")
            self.print_frame_qntd.config(text=f"Qtde= {qtde}")
        else:
            messagebox.showinfo("Erro","Produto nao encontrado")
            self.limpa_entrys1()
            self.cdg_insert_digt1.focus()  
    
    def voltar_usu(self):
        self.caixa_frame1.place_forget()
        self.usuario_mainwmenu(8,8)

    def exit(self):
        self.janela_principal.destroy()
        exit(0)

    def limpa_entrys1(self):
        self.cdg_insert_digt1.delete(0,END)
        self.qntd_insert_digt1.delete(0,END)
        self.cdg_insert_digt1.focus()

    def nova_venda(self):
        cliente=self.def_cliente_digito.get()
        Status="Aberto"
        banco=sqlite3.connect('banco.db')
        b=banco.cursor()
    
        b.execute("SELECT SUM(Preco_quant) FROM vendas_dados WHERE Id_venda = ?",(self.Id_venda,))
        Valure=b.fetchone()[0]
        
        if Valure is not None:
            b.execute("UPDATE Venda SET Cliente = ?, Valor = ? WHERE Id = ?", (cliente, Valure, self.Id_venda))

            b.execute("INSERT INTO Venda (Cliente, Status) VALUES (?, ?)", (0, Status))
        else:
            messagebox.showerror('Erro','Nao me aperte atoa')    
        banco.commit() 
        banco.close()

        self.reload_aba1()

    def fechamento1(self):        
        self.fechar_venda1()

    def reload_aba1(self):
        self.caixa_frame1.place_forget()
        self.principal_frame_mesa()

    def Deletar_produto1(self):
        self.del_frame=LabelFrame(self.caixa_frame1,width=1200,height=600,bd=5,bg="#787777")
        self.del_frame.place(x=100,y=100)

        self.Codigo_del_text=Label(self.del_frame,width=10,text="Codigo",bg="#787777",font="arial 12",foreground="white",bd=0)
        self.Codigo_del_text.place(x=5,y=0)
        self.Codigo_del=Entry(self.del_frame,width=10,fg="dimgray",font="arial 12",foreground="Black",bd=1)
        self.Codigo_del.bind("<Return>",lambda event:self.Qntd_del.focus())
        self.Codigo_del.bind("<KeyPress-v>",lambda event:self.volta_caixa())
        self.Codigo_del.place(x=5,y=20)

        self.Qntd_del_text=Label(self.del_frame,width=10,text="Quantidade",bg="#787777",font="arial 12",foreground="white",bd=0)
        self.Qntd_del_text.place(x=200,y=0)
        self.Qntd_del=Entry(self.del_frame,width=10,fg="dimgray",font="arial 12",foreground="Black",bd=1)
        self.Qntd_del.bind("<Return>",lambda event:self.exibi_valor_del())
        self.Qntd_del.bind("<KeyPress-v>",lambda event:self.volta_caixa())
        self.Qntd_del.place(x=200,y=20)

        self.voltar_fecha_vnd=Button(self.del_frame,width=10,text="Voltar",bg="orange",fg="dimgray",font="arial 12",foreground="white",command=self.volta_caixa,bd=3)
        self.voltar_fecha_vnd.place(x=1080,y=550)

        self.confirma_del=Button(self.del_frame,width=10,text="Deletar",bg="orange",fg="dimgray",font="arial 12",foreground="white",command=self.exibi_valor_del,bd=3)
        self.confirma_del.place(x=1080,y=800)


        Banco=sqlite3.connect('banco.db')
        b=Banco.cursor()
        estilo = ttk.Style()
        estilo.configure('Treeview', font=('Arial', 15),background="#9DCFFA",foreground="black",rowheight=25,fieldbackground="#93FDF6")
        self.table=ttk.Treeview(self.del_frame,height=200)
        self.table.place(x=0,y=80,width=800)
        self.table['columns'] = ("Codigo", "PRODUTO", "PREÇO", "QTDE")

        self.table.column('#0', width=1,minwidth=1)
        self.table.column('#1', width=50,minwidth=20)
        self.table.column('#2', width=20,minwidth=20)
        self.table.column('#3', width=50,minwidth=20)
        self.table.column('#4', width=50,minwidth=20)

        self.table.heading('#0', text='Codigo')
        self.table.heading('#1', text='Produto')
        self.table.heading('#2', text='Preço')
        self.table.heading('#3', text='Quantidade')
        self.table.heading('#4', text='Valor total')

        
        b.execute('SELECT Cdg,PRODUTO,PREÇO,Quantidade,Preco_quant FROM vendas_dados WHERE Id_venda=?', (self.Id_venda,))
        rows = b.fetchall()
        for row in rows:
            self.table.insert(parent='', index='end', text=row[0], values=(row[1], row[2], row[3],row[4]))
            self.table.place(x=0,y=80,width=800,height=515)
        Banco.close()



        self.Codigo_del.focus()

    def exibi_valor_del(self):
        cdg_valor=self.Codigo_del.get()
        qntd_valor=self.Qntd_del.get()

        self.frame_ex=LabelFrame(self.del_frame,width=390,height=400,bd=2,bg="#787777")
        self.frame_ex.place(x=800,y=80)

        conn=sqlite3.connect('banco.db')
        b=conn.cursor 
        
        b.execute('SELECT PRODUTO,Quantidade,PREÇO FROM vendas_dados WHERE Id_venda=? AND cdg=?', (self.Id_venda,cdg_valor,))
        valor = b.fetchone()
               
        if valor is not None:
            produto,quantidade,preco=valor

            if qntd_valor =='':
                if messagebox.askyesno("Tem Certeza?",f"Deseja Deletar o {produto}?"):
                    b.execute("DELETE from vendas_dados WHERE Id_venda=? AND cdg=?", (self.Id_venda,cdg_valor,))
                    b.execute('SELECT QTDE FROM Estoque WHERE Codigo=?', (cdg_valor,))
                    qual = b.fetchone()
                    qntde_up=qual
                    qntd_diminui=qntde_up[0] + float(quantidade)
                    
                    b.execute("UPDATE Estoque SET QTDE=? WHERE Codigo=?", (qntd_diminui, cdg_valor))
                    conn.commit()
                    self.reload_aba1()
            
            if float(qntd_valor)<=quantidade:
                qntd_v = quantidade - int(qntd_valor)
                preto=qntd_v*preco
                if messagebox.askyesno("Tem Certeza?",f"Deseja deletar {qntd_valor} {produto}?"):
                    b.execute("UPDATE vendas_dados SET  Quantidade= ? , Preco_quant=? WHERE Id_venda=? AND cdg=?", (qntd_v,preto,self.Id_venda,cdg_valor,))
                    b.execute('SELECT QTDE FROM Estoque WHERE Codigo=?', (cdg_valor,))
                    qual = b.fetchone()
                    qntde_up=qual
                    qntd_diminui=qntde_up[0] + float(qntd_valor)
                    
                    b.execute("UPDATE Estoque SET QTDE=? WHERE Codigo=?", (qntd_diminui, cdg_valor))
                    conn.commit()
                    self.reload_aba1()
            else:
                messagebox.showinfo("Erro","Quantidade Invalida")
                self.Qntd_del.focus()
        else:
            messagebox.showerror("Erro","Codigo não encontrado")
            self.Codigo_del.focus()

        b.execute('DELETE FROM vendas_dados WHERE Id_venda=? AND Quantidade=?', (self.Id_venda, 0))
        conn.commit()
        conn.close()

    def volta_caixa(self):
        self.del_frame.place_forget()
        self.cdg_insert_digt1.delete(0,END)
        self.qntd_insert_digt1.delete(0,END)
        self.cdg_insert_digt1.focus()

    def volta_aberto (self):
        self.caixa_frame1.destroy()
        self.entri_comandos.focus()


    def fechar_venda1(self):
        self.nova_venda()
        self.din_zero = StringVar(value="00,00")
        self.deb_a_zero = StringVar(value="00,00")
        self.cre_a_zero = StringVar(value="00,00")
        self.desc_zero = StringVar(value="00,00")
        self.fechar_venda1_1()
        
    def fechar_venda1_1(self):
        self.fecha_caixa1=LabelFrame(self.caixa_frame,width=1000,height=500,bd=2,bg="#787777")
        self.fecha_caixa1.place(x=200,y=150)
        self.ven_valo_texto = Label(self.fecha_caixa1,text="Valor:", font="Arial 12", bg="#787777", foreground="white")
        self.ven_valo_texto.place(x=5, y=5)
        self.valor_aValor_a_venda_cx=LabelFrame(self.fecha_caixa1,width=200,height=25,font="Arial 12",bd=0,bg="#adacac")
        self.valor_aValor_a_venda_cx.place(x=75,y=5)

        self.ven_cliente_texto = Label(self.fecha_caixa1,text="Cliente:", font="Arial 12", bg="#787777", foreground="white")
        self.ven_cliente_texto.place(x=720, y=5)
        
        self.valor_aValor_a_venda=LabelFrame(self.fecha_caixa1,width=200,height=25,font="Arial 12",bd=0,bg="#adacac")
        self.valor_aValor_a_venda.place(x=790,y=5)

        self.confirma_venda=Button(self.fecha_caixa1,width=10,text="Confirmar",bg="orange",fg="dimgray",font="arial 12",command=self.finaliza_a,foreground="white",bd=3)
        self.confirma_venda.place(x=880,y=400)

        self.voltar_fecha_vnd=Button(self.fecha_caixa1,width=10,text="Voltar",bg="orange",fg="dimgray",font="arial 12",foreground="white",command=self.volta_caixa_f_a,bd=3)
        self.voltar_fecha_vnd.place(x=880,y=450)
        
        self.opicoes=LabelFrame(self.fecha_caixa1,width=200,height=35,text="Forma de PG:",font="Arial 20",bd=0,bg="#787777",foreground="#04ff00")
        self.opicoes.place(x=520,y=20)
        
        self.opicoes_din_f=LabelFrame(self.fecha_caixa1,width=450,height=70,font="Arial 15",bd=2,bg="#787777")
        self.opicoes_din_f.place(x=520,y=50)

        self.opicoes_din=LabelFrame(self.opicoes_din_f,width=200,height=25,text="DINHEIRO:",font="Arial 15",bd=0,bg="#787777",foreground="#ccff00")
        self.opicoes_din.place(x=0,y=0)

        self.card_din_a=Entry(self.opicoes_din_f,width=20,font="Arial 12",textvariable=self.din_zero,foreground="blue")
        self.card_din_a.bind("<KeyPress-v>",lambda event:self.volta_caixa_f_a())
        self.card_din_a.bind("<Return>",lambda event:self.card_cartao_deb_a.focus())
        self.card_din_a.bind("<KeyPress-v>",lambda event:self.volta_caixa_f_a())
        self.card_din_a.bind("<KeyPress>",lambda event:self.limpa_dim_a())
        self.card_din_a.bind("<KeyPress-f>",lambda event:self.finaliza_a())
        self.card_din_a.bind("<KeyPress-t>",lambda event:self.total_entry_din_a())
        self.card_din_a.place(x=5,y=28,height=30)

        self.opicoes_cartao_a=LabelFrame(self.fecha_caixa1,width=450,height=100,text="CARTAO:",font="Arial 15",bd=2,bg="#787777",foreground="#04ff00")
        self.opicoes_cartao_a.place(x=520,y=120)

        self.opicoes_deb_a=LabelFrame(self.opicoes_cartao_a,width=200,height=25,text="DEBITO:",font="Arial 15",bd=0,bg="#787777",foreground="#ccff00")
        self.opicoes_deb_a.place(x=0,y=0)

        self.card_cartao_deb_a=Entry(self.opicoes_cartao_a,width=20,font="Arial 12",textvariable=self.deb_a_zero,foreground="blue")
        self.card_cartao_deb_a.bind("<KeyPress-v>",lambda event:self.volta_caixa_f_a())
        self.card_cartao_deb_a.bind("<Return>",lambda event:self.card_cartao_cre_a.focus())
        self.card_cartao_deb_a.bind("<KeyPress>",lambda event:self.limpa_deb())
        self.card_cartao_deb_a.bind("<KeyPress-f>",lambda event:self.finaliza_a())
        self.card_cartao_deb_a.bind("<KeyPress-t>",lambda event:self.total_entry_deb_a())
        self.card_cartao_deb_a.place(x=5,y=28,height=30)
        
        self.opicoes_cre_a=LabelFrame(self.opicoes_cartao_a,width=200,height=25,text="CREDITO:",font="Arial 15",bd=0,bg="#787777",foreground="#ccff00")
        self.opicoes_cre_a.place(x=200,y=0) 

        self.card_cartao_cre_a=Entry(self.opicoes_cartao_a,width=20,font="Arial 12",textvariable=self.cre_a_zero,foreground="blue")
        self.card_cartao_cre_a.bind("<KeyPress-v>",lambda event:self.volta_caixa_f_a())
        self.card_cartao_cre_a.bind("<Return>",lambda event:self.card_desc_a.focus())
        self.card_cartao_cre_a.bind("<KeyPress>",lambda event:self.limpa_cre())
        self.card_cartao_cre_a.bind("<KeyPress-f>",lambda event:self.finaliza_a())
        self.card_cartao_cre_a.bind("<KeyPress-t>",lambda event:self.total_entry_cre_a())
        self.card_cartao_cre_a.place(x=200,y=28,height=30)
        
        self.opicoes_desc_a=LabelFrame(self.fecha_caixa1,width=450,height=75,text="DESCONTO:",font="Arial 15",bd=1,bg="#787777",foreground="#ccff00")
        self.opicoes_desc_a.place(x=520,y=320) 

        self.card_desc_a=Entry(self.opicoes_desc_a,width=20,font="Arial 12",textvariable=self.desc_zero,bd=1,foreground="blue")
        self.card_desc_a.bind("<KeyPress-v>",lambda event:self.volta_caixa_f_a())
        self.card_desc_a.bind("<Return>",lambda event:self.desc_2_a())
        self.card_desc_a.bind("<KeyPress>",lambda event:self.limpa_desc_a())
        self.card_desc_a.bind("<KeyPress-f>",lambda event:self.finaliza_a())
        self.card_desc_a.place(x=5,y=5,height=30)

        self.dados_venda_a=LabelFrame(self.fecha_caixa1,width=500,height=400,bd=0,bg="black")
        self.dados_venda_a.place(x=10,y=50)   
        
        banco=sqlite3.connect('banco.db')
        b=banco.cursor()
        b.execute("SELECT * FROM venda WHERE Id=? and Status=?", (self.Id_venda,"Aberto"))
        self.rows = b.fetchall()
        if len(self.rows)>=1:
            b.execute('SELECT Cdg FROM vendas_dados WHERE Id_venda = ?', (self.Id_venda,))
            Cdg2=b.fetchall()
            Cdg2 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(Cdg2)).replace(",,","\n").replace(",","")
            
            b.execute('SELECT PRODUTO FROM vendas_dados WHERE Id_venda = ?', (self.Id_venda,))
            produto1=b.fetchall()
            produto1 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(produto1)).replace(",,","\n").replace(",","")
                
            b.execute('SELECT Quantidade FROM vendas_dados WHERE Id_venda = ?', (self.Id_venda,))
            Quantidade1=b.fetchall()
            Quantidade1 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(Quantidade1)).replace(",,","\n").replace(",","")
            
            b.execute('SELECT PREÇO FROM vendas_dados WHERE Id_venda = ?', (self.Id_venda,))
            preco2=b.fetchall()
            preco2 = re.sub(r'[^\d,a-zA-Z,\.\d{0,2}$]+', '', str(preco2)).replace(",,","\n").replace(",","")

            self.dados_cdg=LabelFrame(self.dados_venda_a,width=900,height=400,font="Arial 12",bd=0,bg="black",foreground="white")
            self.dados_cdg.place(x=0,y=0)

            self.dados_produ=LabelFrame(self.dados_venda_a,width=900,height=400,font="Arial 12",bd=0,bg="black",foreground="white")
            self.dados_produ.place(x=100,y=0)

            self.dados_qntd=LabelFrame(self.dados_venda_a,width=900,height=400,font="Arial 12",bd=0,bg="black",foreground="white")
            self.dados_qntd.place(x=320,y=0)

            self.dados_preco=LabelFrame(self.dados_venda_a,width=900,height=400,font="Arial 12",bd=0,bg="black",foreground="white")
            self.dados_preco.place(x=450,y=0)  

            self.dados_cdg.config(text=f"Codigo\n{Cdg2}")
            self.dados_produ.config(text=f"Produto\n{produto1}")
            self.dados_qntd.config(text=f"Quantidade\n{Quantidade1}")
            self.dados_preco.config(text=f"Valor\n{preco2}")

            b.execute('SELECT Cliente,Valor FROM Venda WHERE Id = ?',(self.Id_venda,))
            result_a=b.fetchone()
            if result_a is not None:
                Cliente,self.Valor_a = result_a
                self.valor_aValor_a_venda.config(text=f"{Cliente}")
                self.valor_aValor_a_venda_cx.config(text=f"{self.Valor_a}R$")

        else:
            self.mesa_base()
            self.fecha_caixa1.destroy()
            
        if self.Id_venda is not None:
            Nu_1 = self.Id_venda
            Nu =re.sub(r'[^\d,\.\d{0,2}$]+', '', str(Nu_1)).replace(',', '') 

        self.numero_venda_texto_f_a=Label(self.fecha_caixa1,font="Arial 12 ",text=f"Venda N°:{Nu}",bg="#787777", foreground="white")
        self.numero_venda_texto_f_a.place(x=400,y=5)
        
        self.card_din_a.focus()
        self.cont_dim=0
        self.cont_deb=0
        self.cont_cre=0
        self.cont_desc=0

        self.conta_a_dim()

    def total_entry_din_a(self):
        self.din_zero = StringVar(value=self.Valor_a)
        self.deb_a_zero = StringVar(value="00,00")
        self.cre_a_zero = StringVar(value="00,00")
        self.desc_zero = StringVar(value="00,00")
        self.fecha_caixa1.place_forget()
        self.fechar_venda1_1()

    def total_entry_deb_a(self):
        self.deb_a_zero = StringVar(value=self.Valor_a)
        self.din_zero = StringVar(value="00,00")
        self.cre_a_zero = StringVar(value="00,00")
        self.desc_zero = StringVar(value="00,00")
        self.fecha_caixa1.place_forget()
        self.fechar_venda1_1()
    def total_entry_cre_a(self):
        self.cre_a_zero = StringVar(value=self.Valor_a)
        self.din_zero = StringVar(value="00,00")
        self.deb_a_zero = StringVar(value="00,00")
        self.desc_zero = StringVar(value="00,00")
        self.fecha_caixa1.place_forget()
        self.fechar_venda1_1()

    def antes_conta_a(self):
        self.opicoes_final_a.place_forget()
        self.conta_a_dim()
    def desc_2_a(self):
        self.card_din_a.focus()
        self.desc=self.card_desc_a.get().replace(",",".")  
        self.desc=float(self.desc)

        self.Valor_a=self.Valor_a-self.desc
        self.conta_a_dim()

    def conta_a_dim(self):
        self.dim_a=self.card_din_a.get().replace(",",".")
        self.cre_a=self.card_cartao_cre_a.get().replace(",",".")
        self.deb_a=self.card_cartao_deb_a.get().replace(",",".")     

        self.dim_a=float(self.dim_a)
        self.cre_a=float(self.cre_a)
        self.deb_a=float(self.deb_a)
        
        self.conta_a=-self.Valor_a+(self.dim_a + self.cre_a + self.deb_a)
        self.conta_a=str(self.conta_a).replace(".",",")

        self.opicoes_final_a=LabelFrame(self.fecha_caixa1,width=300,height=70,font="Arial 15",bd=2,bg="#787777")
        self.opicoes_final_a.place(x=520,y=400)

        self.Venda_valor_a=LabelFrame(self.opicoes_final_a,width=290,height=50,text=f"R$ {self.conta_a}",font="Arial 30",bd=0,bg="#787777",foreground="Black")
        self.Venda_valor_a.place(x=5,y=10)

    def finaliza_a(self):
        banco=sqlite3.connect('banco.db')
        b=banco.cursor()
        add_if_a=self.dim_a + self.cre_a + self.deb_a
        if add_if_a >= self.Valor_a:    
            b.execute("UPDATE venda SET dim=?, cre=?, deb=? , troco=?,Status=? WHERE Id=?", (self.dim_a,self.cre_a,self.deb_a,self.conta_a,"Fechada",self.Id_venda))
            banco.commit()
            self.volta_caixa_f_a()
        else:
            messagebox.showerror("Valor errado","Pagemento insuficiente")
            self.card_din_a.focus()

        self.limpa_geral()

    def volta_caixa_f_a(self):
        self.fecha_caixa1.place_forget()
        self.fecha_caixa1.destroy()
        self.cdg_insert_digt.focus()

    def limpa_geral(self):
        self.fecha_caixa1.place_forget()
        self.fechar_venda1()

    def limpa_dim_a(self):
        self.conta_a_dim()
        if self.cont_dim ==0:
            self.card_din_a.delete(0,END)
            self.cont_dim=self.cont_dim+1

    def limpa_deb(self):
        self.conta_a_dim()
        if self.cont_deb==0:
            self.card_cartao_deb_a.delete(0,END)
            self.cont_deb=self.cont_deb+1

    def limpa_cre(self):
        self.conta_a_dim()
        if self.cont_cre==0:
            self.card_cartao_cre_a.delete(0,END)
            self.cont_cre=self.cont_cre+1

    def limpa_desc_a(self):
        if self.cont_desc==0:
            self.card_desc_a.delete(0,END)
            self.cont_desc=self.cont_desc+1

    
                                    