# Name: Joaquim Myles Lagman
# Pong Game

# Added music to the game
# Music changes when score reaches 5
# Added a game menu
# Shows on the game window who won the game for 2 seconds before closing


import pygame
from pygame import mixer
pygame.init()

import random
import time

SCR_WID, SCR_HEI = 640, 480

mixer.music.load('musicOne.wav')
mixer.music.play(-1)

musicChange = mixer.Sound('musicTwo.wav')

player1win = pygame.image.load("player1wins.jpg")
player2win = pygame.image.load("player2wins.jpg")
player3win = pygame.image.load("player3wins.jpg")

class Player():
        def __init__(self, x):
                if x == "Player 1":
                        self.x, self.y = 8, SCR_HEI/2
                        self.padWid, self.padHei = 8, 64
                elif x == "Player 2":
                        self.x, self.y = SCR_WID - 16, SCR_HEI / 2
                        self.padWid, self.padHei = 8, 64
                elif x == "Player 3":
                        self.x, self.y = 290, SCR_HEI - 16
                        self.padWid, self.padHei = 64, 8
                self.speed = 3
                self.score = 0
                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)

        def scoring(self, x, y):
                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                if y == "Player 1":
                        screen.blit(scoreBlit, (x, 16))
                        if self.score == 10:
                                screen.blit(player1win, (0,0))
                                pygame.display.update()
                                print (y + " wins!")
                                time.sleep(2)
                                pygame.quit()
                                exit()
                elif y == "Player 2":
                        screen.blit(scoreBlit, (SCR_HEI + x, 16))
                        if self.score == 10:
                                screen.blit(player2win, (0,0))
                                pygame.display.update()
                                print (y + " wins!")
                                time.sleep(2)
                                pygame.quit()
                                exit()
                elif y == "Player 3":
                        screen.blit(scoreBlit, (x, 16))
                        if self.score == 10:
                                screen.blit(player3win, (0,0))
                                pygame.display.update()
                                print (y + " wins!")
                                time.sleep(2)
                                pygame.quit()
                                exit()


        def movement(self, x):
                keys = pygame.key.get_pressed()
                if x == "Player 1":
                        if keys[pygame.K_w]:
                                self.y -= self.speed
                        elif keys[pygame.K_s]:
                                self.y += self.speed
                        if self.y <= 0:
                                self.y = 0
                        elif self.y >= SCR_HEI-64:
                                self.y = SCR_HEI-64
                elif x == "Player 2":
                        if keys[pygame.K_UP]:
                                self.y -= self.speed
                        elif keys[pygame.K_DOWN]:
                                self.y += self.speed
                        if self.y <= 0:
                                self.y = 0
                        elif self.y >= SCR_HEI-64:
                                self.y = SCR_HEI-64
                elif x == "Player 3":
                        if keys[pygame.K_u]:
                                self.x -= self.speed
                        elif keys[pygame.K_i]:
                                self.x += self.speed
                        if self.x <= 0:
                                self.x = 0                       
                        elif self.x >= SCR_WID-64:
                                self.x = SCR_WID-64

        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))

class Ball():
        def __init__(self, x):
                if x == "ballOne":  
                        self.x, self.y = random.randint(213,427),random.randint(160,320)   # Starting position of the Ball
                        self.speed_x = -3                       # How far Ball will move horizontally
                        self.speed_y = 3                        # How far Ball will move vertically
                        self.size = 8                          
                if x == "ballTwo":
                        self.x, self.y = random.randint(213,427),random.randint(160,320)   # Starting position of the Ball
                        self.speed_x = 3                       # How far Ball will move horizontally
                        self.speed_y = -3                        # How far Ball will move vertically
                        self.size = 8    
        def movement(self, x):
                if x == "ballOne":
                        self.x += self.speed_x                  # Horizontal movement of the Ball                  
                        self.y += self.speed_y                  # Vertical movement of the Ball


                        if self.y <= 0:                         # WALL COLLISION TOP SCORE
                                self.__init__("ballOne")
                                self.speed_x = 3
                                player3.score += 1
                        elif self.y >= SCR_HEI-self.size:       # WALL COLLISION BOTTOM 
                                self.speed_y *= -1

                        if self.x <= 0:                         # WALL COLLISION SCORE
                                self.__init__("ballOne")
                                player2.score += 1
                        elif self.x >= SCR_WID-self.size:       # WALL COLLISION SCORE
                                self.__init__("ballOne")
                                self.speed_x = 3
                                player.score += 1
                                
                if player.score >= 5:
                        mixer.music.stop()
                        musicChange.play(-1)
                        if x == "ballTwo":
                                self.x -= self.speed_x                  # Horizontal movement of the Ball                  
                                self.y -= self.speed_y                  # Vertical movement of the Ball


                                if self.y <= 0:                         # WALL COLLISION TOP SCORE
                                        self.__init__("ballTwo")
                                        self.speed_x = 3
                                        player3.score += 1      
                                elif self.y >= SCR_HEI-self.size:       # WALL COLLISION BOUNCE
                                        self.speed_y *= -1

                                if self.x <= 0:                         # WALL COLLISION SCORE
                                        self.__init__("ballTwo")
                                        player2.score += 1
                                elif self.x >= SCR_WID-self.size:       # WALL COLLISION SCORE
                                        self.__init__("ballTwo")
                                        self.speed_x = 3
                                        player.score += 1
                elif player2.score >= 5:
                        mixer.music.stop()
                        musicChange.play(-1)
                        if x == "ballTwo":
                                self.x += self.speed_x                  # Horizontal movement of the Ball                  
                                self.y -= self.speed_y                  # Vertical movement of the Ball


                                if self.y <= 0:                         # WALL COLLISION TOP SCORE
                                        self.__init__("ballTwo")
                                        self.speed_x = 3
                                        player3.score += 1    
                                elif self.y >= SCR_HEI-self.size:       # WALL COLLISION BOUNCE
                                        self.speed_y *= -1

                                if self.x <= 0:                         # WALL COLLISION SCORE
                                        self.__init__("ballTwo")
                                        player2.score += 1
                                elif self.x >= SCR_WID-self.size:       # WALL COLLISION SCORE
                                        self.__init__("ballTwo")
                                        self.speed_x = 3
                                        player.score += 1
                                        
                elif player3.score >= 5:
                        mixer.music.stop()
                        musicChange.play(-1)
                        if x == "ballTwo":
                                self.x += self.speed_x                  # Horizontal movement of the Ball                  
                                self.y -= self.speed_y                  # Vertical movement of the Ball


                                if self.y <= 0:                         # WALL COLLISION TOP SCORE
                                        self.__init__("ballOne")
                                        self.speed_x = 3
                                        player3.score += 1      
                                elif self.y >= SCR_HEI-self.size:       # WALL COLLISION BOUNCE
                                        self.speed_y *= -1

                                if self.x <= 0:                         # WALL COLLISION SCORE
                                        self.__init__("ballTwo")
                                        player2.score += 1
                                elif self.x >= SCR_WID-self.size:       # WALL COLLISION SCORE
                                        self.__init__("ballTwo")
                                        self.speed_x = 3
                                        player.score += 1


                #player                                 # PADDLE COLLISION PLAYER 1
                for n in range(-self.size, player.padHei):                              
                        if self.y == player.y + n:
                                if self.x <= player.x + player.padWid:
                                        self.speed_x *= -1
                                        break
                        n += 1
                        
                #player2                                # PADDLE COLLISION PLAYER 2
                for n in range(-self.size, player2.padHei):
                        if self.y == player2.y + n:
                                if self.x >= player2.x - player2.padWid:
                                        self.speed_x *= -1
                                        break
                        n += 1
                        
                #player3                                # PADDLE COLLISION PLAYER 3
                for n in range(-self.size, player3.padWid):
                        if self.x == player3.x + n:
                                if self.y >= player3.y - player3.padHei:
                                        self.speed_y *= -1
                                        break
                        n += 1

        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 8, 8))

SCR_WID, SCR_HEI = 640, 480
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
pygame.display.set_caption("Pong")
pygame.font.init()
clock = pygame.time.Clock()
FPS = 60
background = pygame.image.load("pongbackground.jpg")
backgroundMenu = pygame.image.load("backgroundMenu.png")

player = Player("Player 1")
player2 = Player("Player 2")
player3 = Player("Player 3")
ball = Ball("ballOne")
ball2 = Ball("ballTwo")

def main():
        menu = True
        while True:
                while menu:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        print ("Game exited by user")
                                        pygame.quit()
                                        exit()
                                elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_SPACE:
                                                        menu = False
                                        if event.key == pygame.K_ESCAPE:
                                                print ("Game exited by user")
                                                pygame.quit()
                                                exit()
                                        
                        screen.fill((255,255,255))
                        screen.blit(backgroundMenu, (0,0))
                        clock.tick(30)
                        pygame.display.update()
                        
                #process
                for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        print ("Game exited by user")
                                        pygame.quit()
                                        exit()

                ##process
                #logic
                ball.movement("ballOne")
                ball2.movement("ballTwo")
                player.movement("Player 1")
                player2.movement("Player 2")
                player3.movement("Player 3")
                ##logic
                #draw
                screen.fill((0, 0, 0))
                screen.blit(background ,(0,0))

                ball.draw()
                ball2.draw()
                player.draw()
                player.scoring(32, "Player 1")
                player2.draw()
                player2.scoring(92, "Player 2")
                player3.draw()
                player3.scoring(320, "Player 3")
                ##draw
                ball.draw()

                #_______
                pygame.display.flip()
                clock.tick(FPS)
main()
