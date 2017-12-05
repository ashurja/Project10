# Jamshed Ashurov
# 12/04/2017
# system.py
# This program creates a window that will have an archery target and the user will have 5 clicks to score

import pygame


class Target:

    def __init__(self, mainSurface):
        self.mainSurface = mainSurface
        self.mainSurface.fill((255, 255, 255))
        pygame.init()

    def drawTarget(self):
        """
        The function draws 5 circles
        :return:
        """
        pygame.draw.circle(self.mainSurface, (0, 0, 0), (self.mainSurface.get_width()//2,
                                                         self.mainSurface.get_height() // 2), 100, 1)
        pygame.draw.circle(self.mainSurface, (0, 0, 0), (self.mainSurface.get_width()//2,
                                                         self.mainSurface.get_height() // 2), 80, 0)
        pygame.draw.circle(self.mainSurface, (0, 0, 255), (self.mainSurface.get_width() // 2,
                                                           self.mainSurface.get_height() // 2), 60, 0)
        pygame.draw.circle(self.mainSurface, (255, 0, 0), (self.mainSurface.get_width() // 2,
                                                           self.mainSurface.get_height() // 2), 40, 0)
        pygame.draw.circle(self.mainSurface, (255, 255, 0), (self.mainSurface.get_width() // 2,
                                                             self.mainSurface.get_height() // 2), 20, 0)
        pygame.display.update()

    def printScores(self, scores):
        """
        Up to five times the function covers the screen with the score on the top left corner and draws the circles on top the screen
        :param scores:
        :return:
        """
        self.mainSurface.fill((255, 255, 255))
        self.drawTarget()
        mouseFont = pygame.font.SysFont("Helvetica", 32)
        mouseLabel = mouseFont.render(str("Score:" + str(scores)), 1, (0, 255, 255))
        self.mainSurface.blit(mouseLabel, (30, 30))
        pygame.display.update()

    def gameOver(self, scores):
        """
        The function covers the screen with the words "game over" and the total score
        :param scores:
        :return:
        """
        self.mainSurface.fill((255, 0, 255))
        mouseFont = pygame.font.SysFont("Helvetica", 50)
        mouseLabel = mouseFont.render(str("Game over"), 1, (0, 0, 0))
        mouseLabel1 = mouseFont.render(str("Score:" + str(scores)), 1, (0, 0, 0))
        self.mainSurface.blit(mouseLabel, (150, 150))
        self.mainSurface.blit(mouseLabel1, (150, 200))
        pygame.display.update()


