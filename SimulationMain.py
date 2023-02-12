import FloorboardPannel
import ButtonPanel
import StatisticsPanel
import pygame as p


def main():
    p.init()
    screen = p.display.set_mode((600, 600))
    clock = p.time.Clock()

    FloorboardPannel.setup(screen)
    ButtonPanel.drawPanel(screen)
    buttons = ButtonPanel.drawButtons(screen)
    tossingNeedles = False
    done = False
    while not done:
        for event in p.event.get():
            if event.type == p.QUIT:
                done = True
            if event.type == p.MOUSEBUTTONDOWN:
                if buttons[0].collidepoint(event.pos):  # press START button
                    # how do we start the simulation?
                    print('start button pressed')
                    tossingNeedles = True
                if buttons[1].collidepoint(event.pos):  # press STOP button
                    print('stop button pressed')
                    tossingNeedles = False
                if buttons[2].collidepoint(event.pos):  # press RESET button
                    print('reset button pressed')

        if tossingNeedles:
            FloorboardPannel.tossNeedle(screen)
        StatisticsPanel.drawPanel(screen)
        p.display.flip()
        clock.tick(4)
    p.quit()


if __name__ == "__main__":
    main()
