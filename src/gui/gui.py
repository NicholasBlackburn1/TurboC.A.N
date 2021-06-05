

from pickletools import uint1
from matplotlib.pyplot import text

import pygame
import pygame_gui



def Inpark(inPark):
    if(inPark):
        pygame.draw.rect(background,color='green',rect=Parkrect)
    else:
        pygame.draw.rect(background,color='red',rect=Parkrect)



#x,y,width,hight rect 
Parkrect = pygame.Rect(0,0,100,100)
Reverserect = pygame.Rect(130,0,100,100)
Neturalrect = pygame.Rect(260,0,100,100)
Driverect = pygame.Rect(390,0,100,100)
Sportdriverect = pygame.Rect(520,0,100,100)

label = pygame.Rect(20,100,100,20)
pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

pygame.draw.rect(background,color='red',rect=Parkrect)
pygame.draw.rect(background,color='red',rect=Reverserect)
pygame.draw.rect(background,color='red',rect=Neturalrect)
pygame.draw.rect(background,color='red',rect=Driverect)
pygame.draw.rect(background,color='red',rect=Sportdriverect)

pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0,100,100,50)),text="In Park",manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect((130,100,100,50)),text="In Reverse ",manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect((260,100,100,50)),text="In Neutral ",manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect((390,100,100,50)),text="In Drive ",manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect((520,100,100,50)),text="In Sport ",manager=manager)


clock = pygame.time.Clock()
is_running = True


while is_running:
    time_delta = clock.tick(60)/1000.0
    Inpark(True)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        

        manager.process_events(event)

    pygame.draw.rect(window_surface,color='blue',rect=Parkrect)


    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()


