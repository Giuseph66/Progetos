import sqlite3
import re
import tkinter as tk
from tkinter import Label,ttk,messagebox
from tkinter import *
from fechamento_cx import F_caixa
import random

class mes_geral():
    def mesa_base(self):
        self.mesas_frame=Canvas(self.caixa_frame,bd=0,bg="black")
        self.mesas_frame.place(x=0,y=0,relwidth=1,relheight=1)
        
        for _ in range(random.randint(100,1000)):
            x = random.randint(0, 1800)
            y = random.randint(0, 1000)
            tamanho = random.uniform(0.5, 3)
            self.mesas_frame.create_oval(x, y, x + tamanho, y + tamanho, fill='white', outline='white')
            
        self.mesas_text=Label(self.mesas_frame,text="MESAS",font="Arial 20 bold",bg="black",foreground="white",bd=0)
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
            self.mesas_text1=Label(self.mesas_frame,text="1",font="Arial 15 bold",bg="black",foreground="white",bd=0)
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
                self.mesas_text2=Label(self.mesas_frame,text="2",font="Arial 15 bold",bg="black",foreground="white",bd=0)
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
                    self.mesas_text3=Label(self.mesas_frame,text="3",font="Arial 15 bold",bg="black",foreground="white",bd=0)
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
                        self.mesas_text4=Label(self.mesas_frame,text="4",font="Arial 15 bold",bg="black",foreground="white",bd=0)
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
                            self.mesas_text5=Label(self.mesas_frame,text="5",font="Arial 15 bold",bg="black",foreground="white",bd=0)
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
                                self.mesas_text6=Label(self.mesas_frame,text="6",font="Arial 15 bold",bg="black",foreground="white",bd=0)
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
                                    self.mesas_text7=Label(self.mesas_frame,text="7",font="Arial 15 bold",bg="black",foreground="white",bd=0)
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
                                        self.mesas_text8=Label(self.mesas_frame,text="8",font="Arial 15 bold",bg="black",foreground="white",bd=0)
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
                                            self.mesas_text9=Label(self.mesas_frame,text="9",font="Arial 15 bold",bg="black",foreground="white",bd=0)
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
                                                self.mesas_text10=Label(self.mesas_frame,text="10",font="Arial 15 bold",bg="black",foreground="white",bd=0)
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
        self.principal_frame(self.Id_venda)