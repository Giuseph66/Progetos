import pygame
import sys
import random
import math
from cvzone.HandTrackingModule import HandDetector
import cv2
import time
from moviepy.editor import VideoFileClip

class meu():
    def __init__(self):
        pygame.init()
        self.PRETO = (0, 0, 0)
        self.BRANCO = (255, 255, 255)
        self.VERMELHO = (255, 0, 0)
        self.AZUL = (0, 0, 255)
        self.VERDE=(0,255,0)
        self.GRAY = (200, 200, 200)
        self.AMARELO=(255, 255, 0)
        self.largura_tela = 1550
        self.altura_tela = 820
        self.tamanho_nave = 50
        self.tamanho_tiro = 8
        self.nave1_img = pygame.image.load("imgs/nave (1).png")
        self.nave2_img = pygame.image.load("imgs/nave (2).png")
        self.nave3_img = pygame.image.load("imgs/nave (3).png")
        self.nave4_img = pygame.image.load("imgs/nave (4).png")
        self.vn1_selecionada=self.nave1_img
        self.vn2_selecionada=self.nave2_img
        self.complemento=1
        self.tela_prin()
    def tela_prin(self):
        b_width, b_height = 200, 50
        b_x, b_y = (self.largura_tela - b_width) // 2, (self.altura_tela - b_height) // 2
        self.dis_x,self.dis_y=-50,0
        self.tela_inicial = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        pygame.display.set_caption("Batalha Espacial")
        fundo=self.criar_fundo_estrelado(self.largura_tela, self.altura_tela, 100)
        self.nave1_img_s=self.nave1_img
        self.nave2_img_s=self.nave2_img
        self.nave3_img_s=self.nave3_img
        self.nave4_img_s=self.nave4_img
        core=[self.AZUL,self.VERDE]
        click=0
        webcam=self.VERMELHO
        self.texto="WebCam Notebook OFF..."
        self.tu_cor = self.GRAY
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if b_x <= mouse_pos[0] <= b_x + b_width and b_y <= mouse_pos[1] <= b_y + b_height:
                        self.inicia_game()
                        break
                
                    mouse_pos_click = pygame.mouse.get_pos()
                    if self.nave_ex_1.collidepoint(mouse_pos_click):
                        self.nave1_img_s=self.pinta(self.nave1_img,core[click])
                        if click==0:
                            self.vn1_selecionada=self.nave1_img
                        else:
                            self.vn2_selecionada=self.nave1_img
                        click+=1
                    if self.nave_ex_2.collidepoint(mouse_pos_click):
                        self.nave2_img_s=self.pinta(self.nave2_img,core[click])
                        if click==0:
                            self.vn1_selecionada=self.nave2_img
                        else:
                            self.vn2_selecionada=self.nave2_img
                        click+=1
                    if self.nave_ex_3.collidepoint(mouse_pos_click):
                        self.nave3_img_s=self.pinta(self.nave3_img,core[click])
                        if click==0:
                            self.vn1_selecionada=self.nave3_img
                        else:
                            self.vn2_selecionada=self.nave3_img
                        click+=1
                    if self.nave_ex_4.collidepoint(mouse_pos_click):
                        if click==0:
                            self.vn1_selecionada=self.nave4_img
                        else:
                            self.vn2_selecionada=self.nave4_img
                        self.nave4_img_s=self.pinta(self.nave4_img,core[click])
                        click+=1
                    if self.web.collidepoint(mouse_pos_click):
                        if self.texto=="WebCam Notebook OFF...":
                            self.texto="Webcam Notebook ON..."
                            webcam=self.VERDE
                            self.complemento=0
                        else:
                            self.texto="WebCam Notebook OFF..."
                            webcam=self.VERMELHO
                            self.complemento=1
                    if self.tu.collidepoint(mouse_pos_click):
                        self.tutu_video("imgs/tutorial.mp4")
                          
            mouse_pos = pygame.mouse.get_pos()


            self.dis_x += 0.5
            if self.dis_x > 1820:
                self.dis_x = -50
                self.dis_y += 100
                if self.dis_y >= 700:
                    self.dis_y = 0

            cor = self.PRETO
            ota = self.BRANCO
            if b_x <= mouse_pos[0] <= b_x + b_width and b_y <= mouse_pos[1] <= b_y + b_height:
                cor = self.BRANCO
                ota = self.PRETO

            self.desenha_inicio(fundo, b_height, b_width, b_x, b_y, cor, ota, webcam)

            if click == 2:
                click = 0

            if self.tu.collidepoint(mouse_pos):
                self.tu_cor = self.VERDE
            else:
                self.tu_cor = self.GRAY
    def pinta(self,olichinal,cor):
        width, height = olichinal.get_size()
        copia = olichinal.copy()
        for x in range(width):
            for y in range(height):
                pixel_color = olichinal.get_at((x, y))
                if pixel_color != (0, 0, 0, 0):  
                    copia.set_at((x, y), cor)
        return copia
    
    def tutu_video(self, caminho):
        clip = VideoFileClip(caminho)
        clip = clip.resize((1550, 820))
        clip.preview()
    def desenha_inicio(self,fundo,b_height,b_width,b_x,b_y,cor,ota,webcam):
        self.ponto_1,self.ponto_2=0,0
        self.tela_inicial.blit(fundo, (0, 0))
        self.nave_ex_1 = pygame.Rect(self.dis_x,self.dis_y, self.tamanho_nave*1.5, self.tamanho_nave*1.5)
        self.tela_inicial.blit(pygame.transform.rotate(self.nave1_img_s, 0), self.nave_ex_1)
        self.nave_ex_2 = pygame.Rect(self.dis_x-80,self.dis_y+100, self.tamanho_nave*1.5, self.tamanho_nave*1.5)
        self.tela_inicial.blit(pygame.transform.rotate(self.nave2_img_s, 0), self.nave_ex_2)
        self.nave_ex_3 = pygame.Rect(self.dis_x-160,self.dis_y+200, self.tamanho_nave*1.5, self.tamanho_nave*1.5)
        self.tela_inicial.blit(pygame.transform.rotate(self.nave3_img_s, 0), self.nave_ex_3)
        self.nave_ex_4= pygame.Rect(self.dis_x-240,self.dis_y+300, self.tamanho_nave*1.5, self.tamanho_nave*1.5)
        self.tela_inicial.blit(pygame.transform.rotate(self.nave4_img_s, 0), self.nave_ex_4)

        self.nave_ex_1 = pygame.Rect(self.dis_x,self.dis_y, self.tamanho_nave, self.tamanho_nave)
        self.tela_inicial.blit(pygame.transform.rotate(self.nave1_img, 0), self.nave_ex_1)
        self.nave_ex_2 = pygame.Rect(self.dis_x-80,self.dis_y+100, self.tamanho_nave, self.tamanho_nave)
        self.tela_inicial.blit(pygame.transform.rotate(self.nave2_img, 0), self.nave_ex_2)
        self.nave_ex_3 = pygame.Rect(self.dis_x-160,self.dis_y+200, self.tamanho_nave, self.tamanho_nave)
        self.tela_inicial.blit(pygame.transform.rotate(self.nave3_img, 0), self.nave_ex_3)
        self.nave_ex_4 = pygame.Rect(self.dis_x-240,self.dis_y+300, self.tamanho_nave, self.tamanho_nave)
        self.tela_inicial.blit(pygame.transform.rotate(self.nave4_img, 0), self.nave_ex_4)
        self.play = pygame.Rect(600,380, self.tamanho_nave, self.tamanho_nave)
        self.tela_inicial.blit(pygame.transform.rotate(self.vn1_selecionada, 0), self.play)
        self.play = pygame.Rect(880,380, self.tamanho_nave, self.tamanho_nave)
        self.tela_inicial.blit(pygame.font.Font(None, 30).render("P1", True, self.AZUL), (620, 450))
        self.tela_inicial.blit(pygame.transform.rotate(self.vn2_selecionada, 0), self.play)
        self.tela_inicial.blit(pygame.font.Font(None, 30).render("P2", True, self.VERDE), (900, 450))
        pygame.draw.rect(self.tela_inicial, cor, (b_x, b_y, b_width, b_height),border_radius=10)
        text = pygame.font.Font(None, 36).render("Inicia Game", True, ota)
        text_rect = text.get_rect(center=(b_x + b_width // 2, b_y + b_height // 2))
        self.tela_inicial.blit(text, text_rect)
        renderizado = pygame.font.Font(None, 28).render(str(self.texto), True, webcam)
        largura_texto, altura_texto = renderizado.get_size()
        self.web = pygame.Rect((b_x + b_width // 2)-(largura_texto/2),750, largura_texto, altura_texto)
        self.tela_inicial.blit(renderizado, ((b_x + b_width // 2)-(largura_texto/2),750))
        
        tutu = pygame.font.Font(None, 28).render("Tutorial", True, self.tu_cor)
        largura_texto, altura_texto = tutu.get_size()
        self.tu = pygame.Rect((b_x + b_width // 2) - (largura_texto / 2), 700, largura_texto, altura_texto)
        self.tela_inicial.blit(tutu, ((b_x + b_width // 2) - (largura_texto / 2), 700))

        pygame.display.flip()

    def inicia_game(self):
        self.play_1 = cv2.VideoCapture(0+self.complemento)
        self.play_2 = cv2.VideoCapture(1+self.complemento)
        self.tela_game = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        pygame.display.set_caption("Batalha Espacial")
        self.FATOR_VELOCIDADE=5
        explosao = pygame.image.load("imgs/explosao.gif")
        explosao = pygame.transform.scale(explosao, (100, 100))
        self.nave1_im=self.vn1_selecionada
        self.nave2_im=self.vn2_selecionada
        self.variasao=25
        self.velocidade_nave = 2*self.FATOR_VELOCIDADE
        self.velocidade_tiro = 4*self.FATOR_VELOCIDADE
        self.angulo_nave1 = -90 
        self.angulo_nave2 = 90
        self.morreu,self.escudo_1,self.escudo_2=False,False,False
        self.mini_blocos_1 = []
        self.mini_blocos_2 = []
        self.detector = HandDetector(detectionCon=0.8)
        self.pri,self.seg=True,True
        self.fundo_estrelado = self.criar_fundo_estrelado(self.largura_tela, self.altura_tela, 100)
        self.nave1 = pygame.Rect(50, self.altura_tela // 2 - self.tamanho_nave // 2, self.tamanho_nave, self.tamanho_nave)
        self.nave2 = pygame.Rect(self.largura_tela - 50 - self.tamanho_nave, self.altura_tela // 2 - self.tamanho_nave // 2, self.tamanho_nave, self.tamanho_nave)
        self.tiros_jogador1 = []
        self.tiros_jogador2 = []
        self.desenhar_elementos()
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()            
            self.ver_mao()
            self.nave1 = self.nave1.clamp(self.tela_game.get_rect())
            self.nave2 = self.nave2.clamp(self.tela_game.get_rect())
            
            tiros_jogador1_nova = []
            for tiro, ang in self.tiros_jogador1:
                tiro.x += self.velocidade_tiro * math.sin(math.radians(-ang))
                tiro.y -= self.velocidade_tiro * math.cos(math.radians(-ang))
                remove_tiro = False
                for bloco in self.mini_blocos_2:
                    if tiro.colliderect(bloco):
                        print("colidiu")
                        remove_tiro = True
                        break
                if not remove_tiro and not tiro.colliderect(self.nave2):
                    tiros_jogador1_nova.append((tiro, ang))
                elif tiro.colliderect(self.nave2):
                    self.nave2_im = explosao
                    self.morreu = True
                    self.ponto_1 += 1
            self.tiros_jogador1 = tiros_jogador1_nova

            tiros_jogador2_nova = []
            for tiro, ang in self.tiros_jogador2:
                tiro.x += self.velocidade_tiro * math.sin(math.radians(-ang))
                tiro.y -= self.velocidade_tiro * math.cos(math.radians(-ang))
                remove_tiro = False
                for bloco in self.mini_blocos_1:
                    if tiro.colliderect(bloco):
                        print("colidiu")
                        remove_tiro = True
                        break
                if not remove_tiro and not tiro.colliderect(self.nave1):
                    tiros_jogador2_nova.append((tiro, ang))
                elif tiro.colliderect(self.nave1):
                    self.nave1_im = explosao
                    self.morreu = True
                    self.ponto_2 += 1
            self.tiros_jogador2 = tiros_jogador2_nova

            self.tiros_jogador1 = [tiro for tiro in self.tiros_jogador1 if tiro[0].x < self.largura_tela]
            self.tiros_jogador2 = [tiro for tiro in self.tiros_jogador2 if tiro[0].x < self.largura_tela]
            self.desenhar_elementos()
            if self.morreu:
                time.sleep(1)
                self.tiros_jogador1=[]            
                self.tiros_jogador2=[]
                self.nave1_im=self.vn1_selecionada
                self.nave2_im=self.vn2_selecionada
                self.nave1 = pygame.Rect(50, self.altura_tela // 2 - self.tamanho_nave // 2, self.tamanho_nave, self.tamanho_nave)
                self.nave2 = pygame.Rect(self.largura_tela - 50 - self.tamanho_nave, self.altura_tela // 2 - self.tamanho_nave // 2, self.tamanho_nave, self.tamanho_nave)
                self.morreu=False
            if self.ponto_1>= 5 or self.ponto_2>=5:    
                cv2.destroyAllWindows()
                self.tela_prin()
                break
    def cal(self,x1,y1,x2,y2,img):
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  
        return distance
    def ver_mao(self):
        frente_1,re_1=False,False
        lmList_d_1="sl"
        success_1, img_1 = self.play_1.read()
        if success_1:
            self.mini_blocos_1=[]
            self.escudo_1=False
            img_1 = cv2.flip(img_1, 1)
            hands,img_1 = self.detector.findHands(img_1) 
            if hands:
                mao_d_1 = [0, 0, 0, 0, 0]
                mao_e_1 = [0, 0, 0, 0, 0]
                for hand in hands:
                    posi_1 = self.detector.fingersUp(hand)
                    if hand['type'] == "Left":
                        mao_d_1 = posi_1
                        lmList_d_1 = hand["lmList"] 
                    elif hand['type'] == "Right":
                        mao_e_1 = posi_1
                if self.pri:
                    if len(lmList_d_1) >= 4:  
                        p_d=self.cal(lmList_d_1[4][0], lmList_d_1[4][1],lmList_d_1[0][0], lmList_d_1[0][1],img_1)
                        i_d=self.cal(lmList_d_1[8][0], lmList_d_1[8][1],lmList_d_1[0][0], lmList_d_1[0][1],img_1)
                        m_d=self.cal(lmList_d_1[12][0], lmList_d_1[12][1],lmList_d_1[0][0], lmList_d_1[0][1],img_1)
                        c_d=self.cal(lmList_d_1[16][0], lmList_d_1[16][1],lmList_d_1[0][0], lmList_d_1[0][1],img_1)
                        min_d=self.cal(lmList_d_1[20][0], lmList_d_1[20][1],lmList_d_1[0][0], lmList_d_1[0][1],img_1)
                        dis_p_i=self.cal(lmList_d_1[4][0], lmList_d_1[4][1],lmList_d_1[8][0], lmList_d_1[8][1],img_1)
                        
                        angulo_rad = math.atan2(lmList_d_1[0][1]-lmList_d_1[20][1],lmList_d_1[0][0]-lmList_d_1[20][0])
                        angulo_graus = math.degrees(angulo_rad)
                        self.angulo_nave1=-angulo_graus
                        cv2.putText(img_1, str(angulo_graus), (lmList_d_1[0][0], lmList_d_1[0][1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (69, 252, 3), 2)
                        if p_d>140 and i_d>150 and m_d >150 and c_d>150 and min_d>150 or mao_d_1 == [0,1,1,1,1]:
                            self.mini_blocos_1=[]
                            self.mini_blocos_1=self.cal_blocos(self.nave1.center[0], self.nave1.center[1], dis_p_i,-angulo_graus)
                            self.escudo_1=True
                        if dis_p_i>100 and p_d>140 and i_d>220 and m_d >230 and c_d<100 and min_d<100 or mao_d_1 == [0,1,1,0,0]:
                            tiro = pygame.Rect(self.nave1.x + self.tamanho_nave//1.8 + 10, self.nave1.y + self.tamanho_nave // 1.5 - self.tamanho_tiro // 2 + 10, self.tamanho_tiro, self.tamanho_tiro)
                            self.tiros_jogador1.append([tiro,self.angulo_nave1])                        
                    if mao_e_1 == [0,1,0,0,0]:
                        frente_1=True
                        re_1=False
                    if mao_e_1 == [0,1,0,0,1]:
                        re_1=True
                        frente_1=False
                    delta_x = self.velocidade_nave * math.sin(math.radians(self.angulo_nave1))
                    delta_y = self.velocidade_nave * math.cos(math.radians(self.angulo_nave1))
                    if frente_1:
                        self.nave1.x -= delta_x
                        self.nave1.y -= delta_y  
                    if re_1:
                        self.nave1.x += delta_x
                        self.nave1.y += delta_y  
            img_1=cv2.resize(img_1,(400,300))
            cv2.imshow("Player_1", img_1)
            cv2.moveWindow("Player_1",0,0)
        #play_2
        frente_2,re_2=False,False
        lmList_e_2="sl"
        success_2, img_2 = self.play_2.read()
        if success_2:
            self.mini_blocos_2=[]
            self.escudo_2=False
            img_2 = cv2.flip(img_2, 1)
            hands,img_2 = self.detector.findHands(img_2) 
            if hands:
                mao_d_2 = [0, 0, 0, 0, 0]
                mao_e_2 = [0, 0, 0, 0, 0]
                for hand in hands:
                    posi_2 = self.detector.fingersUp(hand)
                    if hand['type'] == "Left":
                        mao_d_2 = posi_2
                    elif hand['type'] == "Right":
                        mao_e_2 = posi_2
                        lmList_e_2 = hand["lmList"] 
                if self.seg:
                    if len(lmList_e_2) >= 4:  
                        p_d=self.cal(lmList_e_2[4][0], lmList_e_2[4][1],lmList_e_2[0][0], lmList_e_2[0][1],img_2)
                        i_d=self.cal(lmList_e_2[8][0], lmList_e_2[8][1],lmList_e_2[0][0], lmList_e_2[0][1],img_2)
                        m_d=self.cal(lmList_e_2[12][0], lmList_e_2[12][1],lmList_e_2[0][0], lmList_e_2[0][1],img_2)
                        c_d=self.cal(lmList_e_2[16][0], lmList_e_2[16][1],lmList_e_2[0][0], lmList_e_2[0][1],img_2)
                        min_d=self.cal(lmList_e_2[20][0], lmList_e_2[20][1],lmList_e_2[0][0], lmList_e_2[0][1],img_2)
                        dis_p_i=self.cal(lmList_e_2[4][0], lmList_e_2[4][1],lmList_e_2[8][0], lmList_e_2[8][1],img_2)
                        angulo_rad = math.atan2(lmList_e_2[0][1]-lmList_e_2[20][1],lmList_e_2[0][0]-lmList_e_2[20][0])
                        angulo_graus = math.degrees(angulo_rad)
                        if angulo_graus < 0:
                            angulo_graus += 360
                        if angulo_graus > 180:
                            angulo_graus = 360 - angulo_graus
                        angulo_graus_invertido = 180 - angulo_graus
                        self.angulo_nave2 = angulo_graus_invertido
                        cv2.putText(img_2, str(angulo_graus), (lmList_e_2[0][0], lmList_e_2[0][1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (69, 252, 3), 2)
                        if p_d>140 and i_d>150 and m_d >150 and c_d>150 and min_d>150 or mao_e_2 == [0,1,1,1,1]:
                            self.mini_blocos_2=[]
                            self.mini_blocos_2=self.cal_blocos(self.nave2.center[0], self.nave2.center[1], dis_p_i,angulo_graus_invertido)
                            self.escudo_2=True
                        if dis_p_i>100 and p_d>140 and i_d>220 and m_d >230 and c_d<100 and min_d<100 or mao_e_2 == [0,1,1,0,0]:
                            tiro = pygame.Rect(self.nave2.x + self.tamanho_nave//1.8 + 10, self.nave2.y + self.tamanho_nave // 1.5 - self.tamanho_tiro // 2 + 10, self.tamanho_tiro, self.tamanho_tiro)
                            self.tiros_jogador2.append([tiro,self.angulo_nave2])
                    if mao_d_2 == [0,1,0,0,1]:
                        frente_2=True
                        re_2=False
                    if mao_d_2 == [0,1,0,0,0]:
                        re_2=True
                        frente_2=False
                    delta_x = self.velocidade_nave * math.sin(math.radians(self.angulo_nave2))
                    delta_y = self.velocidade_nave * math.cos(math.radians(self.angulo_nave2))
                    if frente_2:
                        self.nave2.x += delta_x
                        self.nave2.y += delta_y  
                    if re_2:
                        self.nave2.x -= delta_x
                        self.nave2.y -= delta_y  
            img_2=cv2.resize(img_2,(400,300))
            cv2.imshow("Player_2", img_2)
            cv2.moveWindow("Player_2",1130,520)

    def criar_fundo_estrelado(self,largura, altura, num_estrelas):
        fundo = pygame.Surface((largura, altura))
        fundo.fill((0, 0, 0)) 
        for _ in range(num_estrelas):
            x = random.randint(0, largura)
            y = random.randint(0, altura)
            pygame.draw.circle(fundo, (255, 255, 255), (x, y), 1)
        return fundo

    def desenhar_elementos(self):
        self.tela_game.blit(self.fundo_estrelado, (0, 0))
        self.tela_game.blit(pygame.transform.rotate(self.nave1_im, self.angulo_nave1), self.nave1)
        self.nave2_im=pygame.transform.flip(self.nave2_im, True, False)
        self.tela_game.blit(pygame.transform.rotate(self.nave2_im, self.angulo_nave2),self.nave2)
        self.tela_game.blit(pygame.font.Font(None, 50).render(f"{str(self.ponto_1)} | {str(self.ponto_2)}", True, self.AMARELO), ((self.largura_tela/2)-35, 10))
        for tiro in self.tiros_jogador1:
            pygame.draw.rect(self.tela_game, self.VERMELHO, tiro[0])
        for tiro in self.tiros_jogador2:
            pygame.draw.rect(self.tela_game, self.AMARELO, tiro[0])
        if self.escudo_1:
            for bloco in self.mini_blocos_1:
                pygame.draw.rect(self.tela_game, self.VERDE, bloco)
        if self.escudo_2:
            for bloco in self.mini_blocos_2:
                pygame.draw.rect(self.tela_game, self.AZUL, bloco)
        pygame.display.flip()
    def cal_blocos(self,nave_x, nave_y, num_blocos,ang):
        mini_blocos=[]
        angulo_inicial = (-ang - 160)+math.pi
        angulo_final = (-ang- 20)+math.pi
        num_blocos=int(num_blocos)
        if num_blocos>0:
            passo_angular = (angulo_final - angulo_inicial) / num_blocos
            for i in range(num_blocos):
                angulo_atual = angulo_inicial + i * passo_angular
                bloco = pygame.Rect(nave_x + self.tamanho_nave * math.cos(math.radians(angulo_atual)),nave_y + self.tamanho_nave * math.sin(math.radians(angulo_atual))+10, 8, 8)
                mini_blocos.append(bloco)
        return mini_blocos
meu()
