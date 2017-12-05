# Jamshed Ashurov
# 12/04/2017
# system.py
# This program imports the target class and executes the functions

import pygame, sys
from pygame.locals import *
import target


def calculation():
    """
    This function gets the position of the mouse and detects the color it is on. If the user clicks on yellow he gets 9
    , red 7, blue 5, black 5, and white 1 point.
    :return:
    """
    coordinates = pygame.mouse.get_pos()
    colorClicked = mainSurface.get_at(coordinates)
    if colorClicked == (0, 0, 0, 255):
        return 3
    if colorClicked == (255, 255, 255, 255):
        return 1
    if colorClicked == (255, 255, 0, 255):
        return 9
    if colorClicked == (0, 0, 255, 255):
        return 5
    if colorClicked == (255, 0, 0, 255):
        return 7


mainSurface = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Jamshed's Archery")
theTarget = target.Target(mainSurface)
theTarget.drawTarget()
clicks = 0
scores = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            clicks = clicks + 1
            if clicks <= 5:
                scores = scores + calculation()
                theTarget.printScores(scores)
            else:
                theTarget.gameOver(scores)
