import pygame as p


PANEL_HEIGHT = 200
PANEL_WIDTH = 400
NUM_OF_BUTTONS = 3
BUTTON_WIDTH = PANEL_WIDTH/NUM_OF_BUTTONS


def drawPanel(screen):
    p.draw.rect(screen, 'white', (0, 400, PANEL_WIDTH, PANEL_HEIGHT))


def drawButtons(screen):
    buttons = []
    colors = ['green', 'red', 'yellow']    
    labels = ['START', 'STOP', 'RESET']
    font = p.font.SysFont('Times New Roman', 30)
    for b in range(NUM_OF_BUTTONS):
        button = p.draw.rect(screen, colors[b],
                             (b*BUTTON_WIDTH, 400, BUTTON_WIDTH, PANEL_HEIGHT))
        text = font.render(labels[b], True, 'black')
        screen.blit(text, button.move(20, 90))
        buttons.append(button)

    return buttons
