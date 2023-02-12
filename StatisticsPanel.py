import FloorboardPannel
import pygame as p
import math


def drawPanel(screen):
    background = p.draw.rect(screen, 'plum2', (400, 0, 200, 600))
    number = FloorboardPannel.calculateProbability()
    font = p.font.SysFont('Times New Roman', 14)
    stats = ['Welcome to the Needle Simulation', '',
             'Click START to drop needles',
             'on the floor.',
             'You can also STOP or RESET',
             'the simulation.',
             str(math.pi)]
    for i in range(len(stats)):
        text = font.render(stats[i], True, 'black')
        screen.blit(text, background.move(0, 25*i))
