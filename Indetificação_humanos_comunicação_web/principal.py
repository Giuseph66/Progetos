from ultralytics import YOLO
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cv2
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from ttkthemes import ThemedTk
import time

class Tudo():
    def __init__(self):
        self.Disponível,self.d,self.cnt=[],9999,0
        self.model = YOLO("Modelo_treinado_n.pt")
        for i in range(10):
            cap = cv2.VideoCapture(i)
            if not cap.isOpened():
                if i >1:
                    messagebox.showerror("Error","Nenhuma camera encontrada")
                break
            self.Disponível.append(i)
            cap.release()        
        self.tela =ThemedTk(theme="black")
        self.tela.geometry("650x600+800+100")
        self.tela.title("Acesso e reconhecimento de pessoas!")
        self.tela.iconbitmap('icon.ico')
        self.f_camera = Frame(self.tela, width=800, height=800, bg="black")
        self.f_camera.place(x=0, y=0)
        self.permicao_treino,self.saber,self.permicao_comu,self.permicao_rec,self.avisa=False,False,False,False,True
        self.check_var_treino = BooleanVar()
        self.check_var_treino.set(self.saber)
        self.check_var_comu = BooleanVar()
        self.check_var_comu.set(self.saber)
        self.chekin_auto = Checkbutton(self.f_camera, bg="black", text="Acessa Whatts",fg="white", font="arial 12 bold", variable=self.check_var_treino, command=self.treino_chek)
        self.chekin_auto.place(x=5, y=40)
        self.check_var_rec = BooleanVar()
        self.check_var_rec.set(self.saber)
        self.chekin_rec = Checkbutton(self.f_camera, bg="black", text="Reconhecer",fg="white", font="arial 12 bold", variable=self.check_var_rec, command=self.treino_rec)
        self.chekin_rec.place(x=160, y=40)
        self.comu_ = Checkbutton(self.f_camera, bg="black", text="Avisa whatts",fg="white", font="arial 12 bold", variable=self.check_var_comu, command=self.comu)
        self.comu_.place(x=350, y=40)
        self.nomes_cap = Label(self.tela, text="Nome :", font="arial 12 bold", bg="Black", fg="white")
        self.nomes_cap.place(x=5, y=7)
        self.textos_atuto = Label(self.tela, text="Cameras disponiveis :", font="arial 10 bold", bg="black",fg="white")
        self.textos_atuto.place(x=0, y=0)
        self.camera_qual = ttk.Combobox(self.tela, width=13, font="arial 12 bold", height=20, background="black")
        self.camera_qual["values"] = self.Disponível
        self.camera_qual.set(self.Disponível[0])
        self.camera_qual.place(x=0, y=20)
        self.canvas = Canvas(self.f_camera, width=800, height=720)
        self.canvas.place(x=2, y=90)
        self.atualizar_tela()
        self.tela.mainloop()
        self.tela.protocol("WM_DELETE_WINDOW", self.fechar_janela)
    def treino_rec(self):
        self.permicao_rec=True if self.check_var_rec.get() else False
        if self.check_var_rec.get()==1:
            self.chekin_rec["fg"]="blue"
            self.chekin_rec["text"]="Reconhecendo..."
        else:
            self.chekin_rec["fg"]="white"
            self.chekin_rec["text"]="Reconhecer"
    def treino_chek(self):
        self.permicao_treino=True if self.check_var_treino.get() else False
        if self.check_var_treino.get()==1:
            cone=self.conectar()
            if cone:
                self.chekin_auto["fg"]="#00ff2a"
                self.chekin_auto["text"]="Conectado" 
            else:
                self.check_var_comu.set(False)
        else:
            self.chekin_auto["fg"]="white"
            self.chekin_auto["text"]="Conectar Whatts"
            self.nav.quit()
            self.check_var_comu.set(False)
            self.comu()
    def comu(self):
        self.permicao_comu=True if self.check_var_comu.get() else False
        if self.check_var_comu.get()==1:
            self.comu_["fg"]="#e5ff00"
            self.comu_["text"]="Avisando..."
            if not self.permicao_treino:
                self.check_var_treino.set(True)
                self.treino_chek()
        else:
            self.comu_["fg"]="white"
            self.comu_["text"]="Avisa whatts"
    def conectar(self):
        try:
            self.Serv= Service(ChromeDriverManager().install())
            self.nav=webdriver.Chrome(service=self.Serv)
            self.nav.get("https://web.whatsapp.com")
            element_present = False
            while not element_present:
                try:
                    WebDriverWait(self.nav, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/button/div[2]/span')))
                    element_present = True
                except:
                    pass
            time.sleep(1)
            self.nav.find_element('xpath','//*[@id="side"]/div[1]/div/div/button/div[2]/span').click()
            self.nav.find_element('xpath','//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys("Voce")
            self.nav.find_element('xpath','//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
            time.sleep(1)
            self.nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys("Test")
            self.nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
            return True
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao iniciar o WebDriver: {e}")
            return False 
    def atualizar_tela(self):
        c=self.camera_qual.get()
        if c=="":
            c=self.d
        c=int(c)
        if c != self.d:
            try:
                self.cap = cv2.VideoCapture(c)
            except:
                pass
        self.d=c
        ret, self.frame = self.cap.read()
        self.frame=cv2.flip(self.frame,1)
        self.faceLoc=None
        humano=False
        if self.permicao_treino:
            pass
        if ret:
            if self.permicao_rec:
                results = self.model(self.frame)
                for result in results:
                    classss=result.boxes.cls.numpy()
                    for num in classss:
                        if num ==0:            
                            humano=True
                            self.cnt=0
                            (x, y, w, h) = [int(i) for i in result.boxes.xyxy[0].cpu().numpy()]
                            cv2.rectangle(self.frame, (x, y), (w, h), (0, 255, 0), 2)
                            if self.permicao_comu:
                                if self.avisa:
                                    self.nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys("To vendo")
                                    self.nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
                                    self.avisa=False 
                                    try:
                                        caminho_completo = os.path.join(os.getcwd(), "precosse", "captura.png")
                                        cv2.imwrite(caminho_completo, self.frame)
                                        self.nav.find_element('xpath', '//div[@title="Anexar"]').click()
                                        self.nav.find_element('xpath', '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]').send_keys(caminho_completo)  
                                        time.sleep(10)
                                        self.nav.find_element('xpath','//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div/div[1]/div[1]/p').send_keys(Keys.ENTER)
                                        print("foi")
                                    except:
                                        pass
                if not humano and not self.avisa:
                    self.cnt+=1
                if self.cnt>=1000:
                    self.avisa=True
                if self.avisa:
                    txt="CAPTURA..."
                else:
                    txt=f"{self.cnt}/1000"
                cv2.putText(self.frame, txt, (520,20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            frame_rgb = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            self.img = ImageTk.PhotoImage(Image.fromarray(frame_rgb))
            self.canvas.config(width=self.img.width(), height=self.img.height())
            self.canvas.delete("all") 
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img, tags="current_image")
            self.canvas.image = self.img 
        self.canvas.after(10, self.atualizar_tela)
    
    def fechar_janela(self):
        self.cap.release()
        self.tela.destroy()
        if self.permicao_treino:
            self.nav.quit()

    def capture(self):
        pass
if __name__ == '__main__':
    Tudo()