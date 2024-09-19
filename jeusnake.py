import sys,random
import pygame

class jeu :

    def __init__(self):
        self.ecran = pygame.display.set_mode((800,600))

        pygame.display.set_caption('Jeu Snake')
        self.jeu_encours=True

        self.serpent_position_x = 300
        self.serpent_position_y = 300
        self.serpent_direction_x = 0
        self.serpent_direction_y = 0
        self.serpent_corps = 10


        self.pomme_position_x = random.randrange(110,690,10)
        self.pomme_position_y = random.randrange(110,590,10)
        self.pomme = 10

        self.clock = pygame.time.Clock()

        self.position_serpent =[]

        self.taille_du_serpent = 1

        self.ecran_du_debut =True

        self.image_tete_serpent = pygame.image.load('la tete 5.png')


        self.image = pygame.image.load('snake-game.jpg')

        self.image_titre = pygame.transform.scale(self.image,(200,100))

        self.score = 0





    def fonction_principale(self):

        while self.ecran_du_debut:
            for evenement in pygame.event.get():
                if evenement.type==pygame.QUIT:
                    sys.exit()
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN :

                        self.ecran_du_debut = False
                self.ecran.fill((0,0,0))

                self.ecran.blit(self.image_titre,(300,50,100,50))
                self.creer_message('moyenne', ' Created By ing.Ayman Ben Amor ',(220,300,100,50),(255,255,255))
                self.creer_message('petite','le but du jeu est que le serpentse developpe', (250, 200, 200, 5), (240, 240, 240))
                self.creer_message('petite', 'pour cela , il a besoin de pomme, mangez-en autant que possible !!', (190, 220, 200, 5),  (240, 240, 240))

                self.creer_message('moyenne', 'appuyez sur Enter pour commencer',(200, 450, 200, 5), (255, 255, 255))




                pygame.display.flip()


        while self.jeu_encours:
            for evenement in pygame.event.get():
                if evenement.type==pygame.QUIT:
                    sys.exit()

                if evenement.type==pygame.KEYDOWN:

                    if evenement.key==pygame.K_RIGHT:
                        self.serpent_direction_x = 5
                        self.serpent_direction_y = 0


                    if evenement.key==pygame.K_LEFT:
                        self.serpent_direction_x = -5
                        self.serpent_direction_y = 0


                    if evenement.key==pygame.K_DOWN:
                        self.serpent_direction_x = 0
                        self.serpent_direction_y = 5


                    if evenement.key==pygame.K_UP:
                        self.serpent_direction_x = 0
                        self.serpent_direction_y = -5


            if self.serpent_position_x<=100 or self.serpent_position_x >= 700 or self.serpent_position_y <= 100 or self.serpent_position_y >= 600 :
                        self.ecran.fill((0, 0, 0))

                        self.ecran.blit(self.image_titre, (300, 50, 100, 50))
                        self.creer_message('moyenne', ' Game Over  ', (220, 300, 100, 50),
                                           (255, 255, 255))
                        self.creer_message('petite', 'le but du jeu est que le serpentse developpe', (250, 200, 200, 5),
                                           (240, 240, 240))
                        self.creer_message('petite',
                                           'pour cela , il a besoin de pomme, mangez-en autant que possible !!',
                                           (190, 220, 200, 5), (240, 240, 240))

                        self.creer_message('moyenne', 'appuyez sur Enter pour repeter le jeu ', (200, 450, 200, 5),
                                           (255, 255, 255))

                        pygame.display.flip()
                        for evenement in pygame.event.get():
                            if evenement.type == pygame.QUIT:
                                sys.exit()
                            if evenement.type == pygame.KEYDOWN:
                                if evenement.key == pygame.K_RETURN:
                                    self.ecran = pygame.display.set_mode((800, 600))

                                    pygame.display.set_caption('Jeu Snake')
                                    self.jeu_encours = True

                                    self.serpent_position_x = 300
                                    self.serpent_position_y = 300
                                    self.serpent_direction_x = 0
                                    self.serpent_direction_y = 0
                                    self.serpent_corps = 10

                                    self.pomme_position_x = random.randrange(110, 690, 10)
                                    self.pomme_position_y = random.randrange(110, 590, 10)
                                    self.pomme = 10

                                    self.clock = pygame.time.Clock()

                                    self.position_serpent = []

                                    self.taille_du_serpent = 1

                                    self.ecran_du_debut = True

                                    self.image_tete_serpent = pygame.image.load('la tete 5.png')

                                    self.image = pygame.image.load('snake-game.jpg')

                                    self.image_titre = pygame.transform.scale(self.image, (200, 100))

                                    self.score = 0

            #sys.exit()










            self.serpent_mouvement()








            if self.pomme_position_y == self.serpent_position_y and self.serpent_position_x == self.pomme_position_x:


                self.pomme_position_x = random.randrange(110,690,10)
                self.pomme_position_y = random.randrange(110,590,10)

                self.taille_du_serpent += 1
                self.score += 1

            la_tete_du_serpent = []
            la_tete_du_serpent.append(self.serpent_position_x)
            la_tete_du_serpent.append(self.serpent_position_y)


            self.position_serpent.append(la_tete_du_serpent)

            if len(self.position_serpent) > self.taille_du_serpent:
                self.position_serpent.pop(0)

            self.afficher_les_elements()
            #self.se_mord(la_tete_du_serpent)

            self.creer_message('grande','Snake Game',(320,10,100,50),(255,255,255))
            self.creer_message('grande', '{}'.format(str(self.score)), (375, 50, 50, 50), (255, 255, 255))




            self.creer_limites()
            self.clock.tick(20)
            pygame.display.flip()

    def creer_limites(self):
        pygame.draw.rect(self.ecran,(255,255,255),(100,100,600,500),3)

    def serpent_mouvement(self):
        self.serpent_position_x += self.serpent_direction_x
        self.serpent_position_y += self.serpent_direction_y

    def afficher_les_elements(self):
        self.ecran.fill((0, 0, 0))

        self.ecran.blit(self.image_tete_serpent,(self.serpent_position_x,self.serpent_position_y,self.serpent_corps,self.serpent_corps))


        pygame.draw.rect(self.ecran, (255, 0, 0),
                         (self.pomme_position_x, self.pomme_position_y, self.pomme, self.pomme))

        self.afficher_serpent()



    def afficher_serpent(self):
        for partie_du_serpent in self.position_serpent[:-1]:
            pygame.draw.rect(self.ecran, (0, 255, 0),
                             (partie_du_serpent[0], partie_du_serpent[1], self.serpent_corps, self.serpent_corps))



    #def se_mord(self.la_tete_du_serpent):                  #modification
        #for partie_du_serpent in self.position_serpent[:-1]:
            #(if la_tete_du_serpent == partie_du_serpent) :

                #sys.exit()


    def creer_message(self,font,message,message_rectangle,couleur):
        if font == 'petite':
            font = pygame.font.SysFont('Lato',20,False)
        elif font == 'moyenne':
            font = pygame.font.SysFont('Lato',30,False)
        elif font == 'grande':
            font = pygame.font.SysFont('Lato',40,True)

        message = font.render(message,True,couleur)
        self.ecran.blit(message,message_rectangle)


if __name__=="__main__":

    pygame.init()
    jeu().fonction_principale()
    pygame.quit()






