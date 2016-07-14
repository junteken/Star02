import pygame,sys, Global, UnitBase, MapHandler
from pygame.locals import *
from Global import *


UnitList=[]
# zealot= UnitBase.Zealot()
Unit_group= pygame.sprite.Group()

Map_group.add(map_h)
isMousePressed=False
isRMousePressed=False
startPos= (0,0)
endPos= (0, 0)
selectedRect= (startPos, endPos)
# pygame.sprite.RenderPlain(zealot.draw())
pygame.mixer.init()
pygame.mixer.music.load('.\\music\\terran1.wav')
pygame.mixer.music.play()
#Unit_group.add(map_h)

while 1:
    #?USER?INPUT
    deltat=clock.tick(30)
    #gScreen.fill((0,0,0))
    
    for event in pygame.event.get():
        if hasattr(event, 'key'):
            if(event.type==KEYDOWN):
                if event.key==K_RIGHT: zealot.HandleCmd(gCmdList[0], zealot, '10, 10', 'hydra')
                elif event.key == K_LEFT: zealot.HandleCmd(gCmdList[1], zealot, '10, 10', 'hydra')
                elif event.key == K_UP: zealot.HandleCmd(gCmdList[2], zealot, '10, 10', 'hydra')
                elif event.key == K_DOWN: zealot.HandleCmd(gCmdList[3], zealot, '10, 10', 'hydra')
                elif event.key == K_c :
                    zealot= UnitBase.Zealot((pygame.mouse.get_pos()[0] + map_h.GetRectOffset()[0], pygame.mouse.get_pos()[1]+map_h.GetRectOffset()[1]))
                    UnitList.append(zealot)
                    Unit_group.add(zealot.draw())
                elif event.key == K_ESCAPE: sys.exit(0)
        elif event.type == MOUSEBUTTONDOWN:
            #zealot.draw().position = pygame.mouse.get_pos()
            button= pygame.mouse.get_pressed()

            if(button[0] == True):
                isMousePressed= True
                startPos= pygame.mouse.get_pos()                        
                print('mouse click down={0}', startPos)
            elif(button[2] == True):
                for unit in UnitList:
                    if(selectedRect.contains(Rect(unit.GetRpos(), (10, 10))) == True):
                       unit.HandleCmd(gCmdList[2], unit, (pygame.mouse.get_pos()[0] + map_h.GetRectOffset()[0], pygame.mouse.get_pos()[1]+map_h.GetRectOffset()[1]), 'hydra')


        elif event.type == MOUSEBUTTONUP:

            button= pygame.mouse.get_pressed()

            if(button[0] == False):
                isMousePressed= False
                endPos= pygame.mouse.get_pos()
                print('mouse click up={0}', endPos)
                for unit in UnitList:
                    if(selectedRect.contains(Rect(unit.GetRpos(), (10, 10))) == True):
                       unit.HandleCmd(gCmdList[1], unit, '10, 10', 'hydra')
                    else:
                       unit.HandleCmd(gCmdList[0], unit, '10, 10', 'hydra')


                #pygame.draw.rect(gScreen, pygame.Color(255,255,255), Rect(startPos, (endPos[0]-startPos[0], endPos[1] - startPos[1])), 10)

        
          
        else:
            continue
    #?RENDERING
    
 
    Map_group.update(deltat)
    Map_group.draw(gScreen)
    Unit_group.update(deltat)
    Unit_group.draw(gScreen)

   
    m_pos= pygame.mouse.get_pos()

    if m_pos[1] < gScreen.get_rect().top+20:
        map_h.MoveRect('up')
    elif m_pos[1] > gScreen.get_rect().bottom -20:
        map_h.MoveRect('down')
    elif m_pos[0] < gScreen.get_rect().left + 20:
        map_h.MoveRect('left')
    elif m_pos[0] > gScreen.get_rect().right - 20:
        map_h.MoveRect('right')

    if(isMousePressed):        
        endPos= pygame.mouse.get_pos()
        selectedRect= Rect(startPos, (endPos[0]-startPos[0], endPos[1] - startPos[1]))
        #print('mouse pressed cursor =', endPos , Rect(startPos, (endPos[0]-startPos[0], endPos[1] - startPos[1])))
        pygame.draw.rect(gScreen, pygame.Color(0,255,0), selectedRect, 10)


    

    pygame.display.flip()
