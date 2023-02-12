# AVOID CIRCULAR IMPORTS
# import SimulationMain
import pygame as p
import random as r
import math

PANEL_WIDTH = PANEL_HEIGHT = 400
NUM_OF_BOARDS = 6
BOARD_WIDTH = PANEL_WIDTH/NUM_OF_BOARDS
NEEDLE_LENGTH = (2/3)*BOARD_WIDTH


def setup(screen):
    p.draw.rect(screen, 'orange4', (0, 0, PANEL_WIDTH, PANEL_HEIGHT))
    gaps = []
    for n in range(NUM_OF_BOARDS + 1):
        gap = p.draw.line(screen, 'white', (n*BOARD_WIDTH, -BOARD_WIDTH),
                          (n*BOARD_WIDTH, PANEL_WIDTH + BOARD_WIDTH))
        gaps.append(gap)


def tossNeedle(screen):
    startPoint = (r.randint(0, PANEL_WIDTH), r.randint(0, PANEL_HEIGHT))
    angle = r.uniform(0, 2*math.pi)
    endPoint = (startPoint[0] + NEEDLE_LENGTH*math.cos(angle),
                startPoint[1] + NEEDLE_LENGTH*math.sin(angle))
    needle = p.draw.line(screen, 'gold2', startPoint, endPoint)
    isTossASuccess()


def isTossASuccess():
    # TODO - return True when a needle crosses a gap using colliderect
    
    return False


def calculateProbability():
    return
