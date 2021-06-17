"""
car gui  display data
TODO: need too fix dynamic text UwU
"""

from pickletools import uint1
from matplotlib.pyplot import text

import pygame
import pygame_gui


inpark = None
inReverse = None
inNeural = None
inDrive = None
inSport = None
isManual = None

background = pygame.Surface((800, 600))
#x,y,width,hight rect   
label = pygame.Rect(20,100,100,20)
Parkrect = pygame.Rect(0,0,100,100)
Reverserect = pygame.Rect(130,0,100,100)
Neturalrect = pygame.Rect(260,0,100,100)
Driverect = pygame.Rect(390,0,100,100)
Sportdriverect = pygame.Rect(520,0,100,100)
Manualrect = pygame.Rect(650,0,100,100)



def text_to_screen(screen, text, x, y, size = 50,
            color = (200, 000, 000), font_type = '/home/nicholas/Desktop/cardev/src/gui/Kagura.ttf'):
    try:

        text = str(text)
        font = pygame.font.Font(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    except:
        print ('Font Error, saw it coming')
       


def setpark(self,park):
    self.inpark =  park

def setReverse(self,reverse):
    self.inReverse= reverse


def setNeural(self,neural):
    self.inNeural = neural


def setDrive(self,drive):
    self.inDrive= drive

def setSport(self,drive):
    self.inSport= drive


def setManual(self,drive):
    self.inManual= drive

def startUi():
    
    pygame.init()
    pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
    
    pygame.display.set_caption('Nicholas Blackburns Car Data Display UwU Furries Rulz')
    window_surface = pygame.display.set_mode((800, 600))

    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))

    manager = pygame_gui.UIManager((800, 600))
 
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0,100,100,50)),text="In Park",manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((130,100,100,50)),text="In Reverse ",manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((260,100,100,50)),text="In Neutral ",manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((390,100,100,50)),text="In Drive ",manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((520,100,100,50)),text="In Sport ",manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((650,100,100,50)),text="In Manual ",manager=manager)

    #pygame_gui.elements.UIImage(relative_rect=pygame.Rect((0,100,100,50)),image_surface="/home/nicholas/Desktop/cardev/src/gui/resources/gauge.png",manager=manager)
    
    clock = pygame.time.Clock()
    is_running = True
   
    while is_running:
      
        time_delta = clock.tick(144)/1000.0
        #text_to_screen(background,str("Car Data"),250,196,35,(255,255,255))    
        
        # displayes whether the car is in park or not 
        if(inpark):
            pygame.draw.rect(background,color='green',rect=Parkrect)
        else:
            pygame.draw.rect(background,color='red',rect=Parkrect)

        if(inReverse):
            pygame.draw.rect(background,color='green',rect=Reverserect)
        else:
            pygame.draw.rect(background,color='red',rect=Reverserect)

        if(inNeural):
            pygame.draw.rect(background,color='green',rect=Neturalrect)
        else:
            pygame.draw.rect(background,color='red',rect=Neturalrect)


        if(inDrive):
            pygame.draw.rect(background,color='green',rect=Driverect)
        else:
            pygame.draw.rect(background,color='red',rect=Driverect)


        if(inSport):
            pygame.draw.rect(background,color='green',rect=Sportdriverect)
        else:
            pygame.draw.rect(background,color='red',rect=Sportdriverect)

        if(isManual):
            pygame.draw.rect(background,color='green',rect=Manualrect)
        else:
            pygame.draw.rect(background,color='red',rect=Manualrect)



        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()

startUi()