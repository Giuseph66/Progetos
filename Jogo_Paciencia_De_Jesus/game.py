import pygame
import sys
import random

pygame.init()

def tela_inicio():
    tela = pygame.display.set_mode((1100, 700))
    pygame.display.set_caption("Jesus_Ateu Progetoss")

    preto = (255, 255, 255)
    BRANCO = (0, 0, 0)
    amarelo = (255, 255, 0)

    background = pygame.image.load("Jogo_Paciencia_De_Jesus/img/fundo_inicio.jpg").convert()
    asp=pygame.image.load("Jogo_Paciencia_De_Jesus/img/asp.png").convert()
    asp = pygame.transform.scale(asp, (1200,1200))
    fundo=pygame.image.load("Jogo_Paciencia_De_Jesus/img/fundo.png").convert()

    angulo = 0

    largura_botao = 250
    altura_botao = 50

    posicao_botao_play = (450, 300)
    posicao_botao_creditos = (580, 500)
    posicao_botao_tela_cheia = (450, 500)
    posicao_botao_configuracao = (450, 400)
    tamanho_fonte = 36

    fonte_animada = pygame.font.Font(None, tamanho_fonte)
    fonte_28 = pygame.font.Font(None, 28)
    fonte_25 = pygame.font.Font(None, 25)

    texto_play = fonte_28.render("Play", True, preto)
    texto_configuracao = fonte_28.render("Configuração", True, preto)
    texto_creditos = fonte_25.render("Créditos", True, preto)
    texto_tela_cheia = fonte_25.render("Tela Cheia(T)", True, preto)

    posicao_texto_superior = [tela.get_width() // 2, 200]
    animando_fonte = True
    incremento_fonte = 1
    incremento_posicao = 1
    def gerar_posicao_aleatoria():
        x = random.randint(0, 1100 - 55)
        y = random.randint(0, 700 - 30)
        return x, y
    def render_texto_com_sombra(
        fonte_animada, texto, cor_principal, cor_sombra, deslocamento_sombra
    ):
        texto_superior_principal = fonte_animada.render(texto, True, cor_principal)
        texto_superior_sombra = fonte_animada.render(texto, True, cor_sombra)
        tela.blit(
            texto_superior_sombra,
            (
                posicao_texto_superior[0] + deslocamento_sombra,
                posicao_texto_superior[1] + deslocamento_sombra,
            ),
        )
        tela.blit(texto_superior_principal, posicao_texto_superior)

    def acao_botao_play():
        tela = pygame.display.set_mode((1100, 700))
        pygame.display.toggle_fullscreen()
        pygame.display.set_caption("Paciencia de Jesus")
        tela.fill((0,0,0))


        fds_ = pygame.image.load("Jogo_Paciencia_De_Jesus/img/fds.png").convert_alpha()
        img_boneco_1 = pygame.image.load("Jogo_Paciencia_De_Jesus/img/boneco_1.png").convert_alpha()
        img_boneco_2 = pygame.image.load("Jogo_Paciencia_De_Jesus/img/boneco_2.png").convert_alpha()
        img_ponto=pygame.image.load("Jogo_Paciencia_De_Jesus/img/ponto.png").convert_alpha()
        img_add=pygame.image.load("Jogo_Paciencia_De_Jesus/img/botao_adicionar.png").convert_alpha
        vez,ganhei,fds=False,False,False
        
        posicao_botao_nao = (350, 150)
        cor_transparencia = (255, 0, 255)

        img_boneco_1.set_colorkey(cor_transparencia)
        img_boneco_2.set_colorkey(cor_transparencia)
        img_ponto.set_colorkey(cor_transparencia)
        class Boneco(pygame.sprite.Sprite):
            def __init__(self, image, pos, size=(50, 50)):
                super().__init__()
                self.image = pygame.transform.scale(image, size)
                self.rect = self.image.get_rect(center=pos)
                self.is_removed = False
                self.remove_time = 0
                self.removal_duration = 10000  
                self.is_boneco_2 = image == img_boneco_2
                self.is_boneco_1 = image == img_boneco_1
                self.is_ponto = image == img_ponto  

            def update(self):
                current_time = pygame.time.get_ticks()
                    
                if self.is_removed and current_time - self.remove_time >= self.removal_duration:
                    self.rect.center = (random.randint(50, 1050), random.randint(50, 650))
                    self.is_removed = False
                    
                if not self.is_removed:
                    self.is_removed = True
                    self.remove_time = current_time

                if self.is_boneco_2:
                    self.rect.move_ip(random.randint(-10, 10), random.randint(-5, 5))
                if self.is_boneco_1:
                    self.rect.move_ip(random.randint(-1, 1), random.randint(-1, 1))
                if self.is_ponto:
                    self.rect.move_ip(random.randint(-5, 5), random.randint(-5, 5))
        bonecos_1 = pygame.sprite.Group()
        bonecos_2 = pygame.sprite.Group()
        botao_add = pygame.sprite.Group()
        pontos = pygame.sprite.Group()
        rotated_ceu=fundo
        rect_ceu =0,0
        pontos_ = 0
        uma=0
        angulo_1=0
        ang=1
        ang_=1
        fonte_28 = pygame.font.Font(None, 28)
        fonte_50 = pygame.font.Font(None, 50)
        fonte_100 = pygame.font.Font(None, 100)
        tempo_inicial = pygame.time.get_ticks() 
        num_bonecos = 5  
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        sys.exit()
                elif evento.type == pygame.MOUSEMOTION:
                    pos_mouse = pygame.mouse.get_pos()
                    if posicao_botao_nao[0] < pos_mouse[0] < posicao_botao_nao[0] + 100 and \
                    posicao_botao_nao[1] < pos_mouse[1] < posicao_botao_nao[1] + 50:
                        posicao_botao_nao = gerar_posicao_aleatoria()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    pos_mouse = pygame.mouse.get_pos()
                    for boneco_1 in bonecos_1:
                        if boneco_1.rect.collidepoint(pos_mouse):
                            bonecos_1.remove(boneco_1)
                            pontos_ += 1
                            novo_boneco = Boneco(img_boneco_1, (random.randint(50, 1050), random.randint(50, 650)))
                            bonecos_1.add(novo_boneco)
                    for boneco_2 in bonecos_2:
                        if boneco_2.rect.collidepoint(pos_mouse):
                            bonecos_2.remove(boneco_2)
                            pontos_ += 5
                            novo_boneco_2 = Boneco(img_boneco_2, (random.randint(50, 1050), random.randint(50, 650)))
                            bonecos_2.add(novo_boneco_2) 
                    for ponto in pontos:
                        if ponto.rect.collidepoint(pos_mouse):
                            pontos.remove(ponto)
                            pontos_ += 2
                            novo_ponto = Boneco(img_ponto, (random.randint(50,1050), random.randint(50, 650)))
                            pontos.add(novo_ponto)            
                if pontos_>=5:
                    for boneco_1 in bonecos_1:
                        if evento.type == pygame.MOUSEMOTION:
                            pos_mouse = pygame.mouse.get_pos()
                angulo_1 -= ang
                
            if uma ==0:
                uma+=1
                for _ in range(num_bonecos):
                    novo_boneco = Boneco(img_boneco_1, (random.randint(50, 1050), random.randint(50, 650)))
                    bonecos_1.add(novo_boneco)
                
            elif pontos_ ==5:
                if uma ==1:
                    uma+=1
                    for _ in range(num_bonecos):
                        novo_boneco = Boneco(img_boneco_1, (random.randint(50, 1050), random.randint(50, 650)))
                        bonecos_1.add(novo_boneco)
                        
            elif pontos_==10:
                if uma ==2:
                    uma+=1
                    for _ in range(num_bonecos):
                        novo_ponto = Boneco(img_ponto, (random.randint(50, 1050), random.randint(50, 650)))
                        pontos.add(novo_ponto)
                
            elif pontos_ >=30 :
                if uma ==3:
                    uma +=1
                    for _ in range(num_bonecos):
                        novo_boneco_2 = Boneco(img_boneco_2, (random.randint(50, 1050), random.randint(50, 650)))
                        bonecos_2.add(novo_boneco_2)            
                    for _ in range(num_bonecos):
                        novo_ponto = Boneco(img_ponto, (random.randint(50, 1050), random.randint(50, 650)))
                        pontos.add(novo_ponto)
                        
            if pontos_ >= 50:
                vez=True
                if uma == 4:
                    uma += 1
                    rotated_ceu=asp
            if vez:
                for boneco_1 in bonecos_1:
                    bonecos_1.remove(boneco_1)
                vez=False

            if pontos_ >=75:
                angulo_1 -= ang_
                rotated_ceu = pygame.transform.rotate(asp, angulo_1)
                rect_ceu = rotated_ceu.get_rect(center=tela.get_rect().center)

            if pontos_>=80:
                ang =3
                ang_=2
            if pontos_>=85:
                ang =4
                ang_=3
            if pontos_>=90:
                ang =5
                ang_=3
            if pontos_>=100:
                ganhei=True
                ang =6
                ang_=3
            if pontos_>=120:
                ang =7
                ang_=4
            if pontos_>=140:
                fds=True
                ang =10
                ang_=5
            
            tela.blit(rotated_ceu, (rect_ceu))
        
            bonecos_1.update()
            bonecos_2.update()
            pontos.update()

            bonecos_1.draw(tela)
            bonecos_2.draw(tela)
            pontos.draw(tela)
            
            botao_nao=pygame.draw.rect(tela, BRANCO, (posicao_botao_nao[0], posicao_botao_nao[1], 55, 30))
            tela.blit(fonte_25.render("Não", True, preto), (posicao_botao_nao[0] + 10, posicao_botao_nao[1] + 10))

            tempo_decorrido = pygame.time.get_ticks() - tempo_inicial

            segundos_decorridos = tempo_decorrido // 1000
            
            texto_renderizado = fonte_28.render(f"Pontos: {pontos_}", True, amarelo)
            tela.blit(texto_renderizado, (10, 30))
            texto_contador = fonte_28.render(f"Tempo: {segundos_decorridos}", True, amarelo)
            tela.blit(texto_contador, (10, 10))  
            if ganhei:
                ganhou = fonte_100.render(f"Parabéns você Ganhou !!!", True, amarelo)
                ganhou_ = fonte_50.render(f"Aperte 'esc' para finalizar o jogo!", True, amarelo)
                tela.blit(ganhou, (100, 300))
                tela.blit(ganhou_, (300, 800))
            if fds:
                tela.blit(fds_, (1100 // 2 - fds_.get_width() // 2, 700 // 2 - fds_.get_height() // 2))
                            
            pygame.time.Clock().tick(1000)
            pygame.display.flip()

    def acao_botao_configuracao():
        print("Botão Configuracao foi clicado!")

    def acao_botao_creditos():
        print("Botão Créditos foi clicado!")

    def acao_botao_tela_cheia():
        global posicao_botao_play
        global posicao_botao_creditos
        global posicao_botao_configuracao
        global posicao_botao_tela_cheia

        pygame.display.toggle_fullscreen()
        if tela.get_flags() & pygame.FULLSCREEN:
            posicao_botao_play = (
                (tela.get_width() - largura_botao) // 2,
                (tela.get_height() - altura_botao) // 2,
            )
            posicao_botao_creditos = (
                (tela.get_width() - largura_botao / 2) // 1.8,
                (tela.get_height() - altura_botao) // 2 + 200,
            )
            posicao_botao_tela_cheia = (
                (tela.get_width() - largura_botao / 2) // 2.25,
                (tela.get_height() - altura_botao) // 2 + 200,
            )
            posicao_botao_configuracao = (
                (tela.get_width() - largura_botao) // 2,
                (tela.get_height() - altura_botao) // 2 + 100,
            )
        else:
            posicao_botao_play = (450, 300)
            posicao_botao_creditos = (580, 500)
            posicao_botao_tela_cheia = (450, 500)
            posicao_botao_configuracao = (450, 400)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if (
                    evento.key == pygame.K_t
                ): 
                    pygame.display.toggle_fullscreen()
                    if tela.get_flags() & pygame.FULLSCREEN:
                        posicao_botao_play = (
                            (tela.get_width() - largura_botao) // 2,
                            (tela.get_height() - altura_botao) // 2,
                        )
                        posicao_botao_creditos = (
                            (tela.get_width() - largura_botao / 2) // 1.8,
                            (tela.get_height() - altura_botao) // 2 + 200,
                        )
                        posicao_botao_tela_cheia = (
                            (tela.get_width() - largura_botao / 2) // 2.25,
                            (tela.get_height() - altura_botao) // 2 + 200,
                        )
                        posicao_botao_configuracao = (
                            (tela.get_width() - largura_botao) // 2,
                            (tela.get_height() - altura_botao) // 2 + 100,
                        )
                    else:
                        posicao_botao_play = (450, 300)
                        posicao_botao_creditos = (580, 500)
                        posicao_botao_tela_cheia = (450, 500)
                        posicao_botao_configuracao = (450, 400)

                    animando_fonte = True
                elif evento.key == pygame.K_RETURN:  
                    acao_botao_play()

                elif evento.key == pygame.K_ESCAPE:
                    sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_play.collidepoint(evento.pos):
                    acao_botao_play()

                elif botao_configuracao.collidepoint(evento.pos):
                    acao_botao_configuracao()

                elif botao_creditos.collidepoint(evento.pos):
                    acao_botao_creditos()

                elif botao_tela_cheia.collidepoint(evento.pos):
                    acao_botao_tela_cheia()

        angulo -= 1/3  
        rotated_background = pygame.transform.rotate(background, angulo)
        rect_background = rotated_background.get_rect(center=tela.get_rect().center)
        tela.blit(rotated_background, rect_background)

        for deslocamento in range(5, 0, -1):
            sombra_botao_play = pygame.Rect(
                posicao_botao_play[0] + deslocamento,
                posicao_botao_play[1] + deslocamento,
                largura_botao,
                altura_botao,
            )
            pygame.draw.rect(tela, preto, sombra_botao_play)

            sombra_botao_creditos = pygame.Rect(
                posicao_botao_creditos[0] + deslocamento,
                posicao_botao_creditos[1] + deslocamento,
                largura_botao / 2,
                altura_botao,
            )
            pygame.draw.rect(tela, preto, sombra_botao_creditos)

            sombra_botao_tela_cheia = pygame.Rect(
                posicao_botao_tela_cheia[0] + deslocamento,
                posicao_botao_tela_cheia[1] + deslocamento,
                largura_botao / 2,
                altura_botao,
            )
            pygame.draw.rect(tela, preto, sombra_botao_tela_cheia)

            sombra_botao_configuracao = pygame.Rect(
                posicao_botao_configuracao[0] + deslocamento,
                posicao_botao_configuracao[1] + deslocamento,
                largura_botao,
                altura_botao,
            )
            pygame.draw.rect(tela, preto, sombra_botao_configuracao)

        botao_play = pygame.draw.rect(
            tela, BRANCO, pygame.Rect(posicao_botao_play, (largura_botao, altura_botao))
        )
        botao_configuracao = pygame.draw.rect(
            tela,
            BRANCO,
            pygame.Rect(posicao_botao_configuracao, (largura_botao, altura_botao)),
        )
        botao_creditos = pygame.draw.rect(
            tela,
            BRANCO,
            pygame.Rect(posicao_botao_creditos, (largura_botao / 2, altura_botao)),
        )
        botao_tela_cheia = pygame.draw.rect(
            tela,
            BRANCO,
            pygame.Rect(posicao_botao_tela_cheia, (largura_botao / 2, altura_botao)),
        )

        tela.blit(
            texto_play,
            (
                posicao_botao_play[0] + (largura_botao - texto_play.get_width()) // 2,
                posicao_botao_play[1] + (altura_botao - texto_play.get_height()) // 2,
            ),
        )
        tela.blit(
            texto_creditos,
            (
                posicao_botao_creditos[0]
                + (largura_botao / 2 - texto_creditos.get_width()) // 2,
                posicao_botao_creditos[1]
                + (altura_botao - texto_creditos.get_height()) // 2,
            ),
        )
        tela.blit(
            texto_tela_cheia,
            (
                posicao_botao_tela_cheia[0]
                + (largura_botao / 4 - texto_tela_cheia.get_width() / 2),
                posicao_botao_tela_cheia[1]
                + (altura_botao - texto_tela_cheia.get_height()) // 2,
            ),
        )
        tela.blit(
            texto_configuracao,
            (
                posicao_botao_configuracao[0]
                + (largura_botao / 2 - texto_configuracao.get_width() / 2),
                posicao_botao_configuracao[1]
                + (altura_botao - texto_configuracao.get_height()) // 2,
            ),
        )

        if animando_fonte:
            tamanho_fonte += incremento_fonte
            if tamanho_fonte > 150 or tamanho_fonte < 36:
                incremento_fonte *= -1
            fonte_animada = pygame.font.Font(None, tamanho_fonte)

            posicao_texto_superior = [
                tela.get_width() // 2
                - fonte_animada.size("Paciencia de Jesus")[0] // 2,
                50,
            ]

            posicao_texto_superior[1] += incremento_posicao
            if posicao_texto_superior[1] > 70 or posicao_texto_superior[1] < 50:
                incremento_posicao *= -1

        render_texto_com_sombra(fonte_animada, "Paciencia de Jesus", amarelo, BRANCO, 2)

        texto_renderizado = fonte_28.render(
            "JesusAteu/GiusephGiangareli", True, amarelo
        )

        texto_renderizado_sombra = fonte_28.render(
            "JesusAteu/GiusephGiangareli",
            True,
            (amarelo[0] // 2, amarelo[1] // 2, amarelo[2] // 2),
        )

        posicao_texto_autor = (
            20,
            tela.get_height() - texto_renderizado.get_height() - 20,
        )

        posicao_texto_autor_sombra = (
            posicao_texto_autor[0] + 2,
            posicao_texto_autor[1] + 2,
        )

        tela.blit(texto_renderizado_sombra, posicao_texto_autor_sombra)

        tela.blit(texto_renderizado, posicao_texto_autor)

        pygame.display.flip()


tela_inicio()