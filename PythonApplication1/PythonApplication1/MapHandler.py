import pygame, Global, CollisionDetector

class MapHandler(pygame.sprite.Sprite):
    """MapHandler of class"""
    MOVE_OFFSET=10#map scroll 속도

    def __init__(self, mapimg):
        pygame.sprite.Sprite.__init__(self)
        self.src_image=pygame.image.load(mapimg)
        self.EntireMapRect= self.src_image.get_rect() #전체 map의 크기
        self.updateRect=self.rect= Global.gScreen.get_rect() #실제 화면에 그려지는 영역의 크기
        self.image= self.src_image.subsurface(self.rect).convert()

        self.col_detector= CollisionDetector.CollisionDetector()
        self.col_detector.AppendBlockLine((0,375, 627,76))
        self.col_detector.AppendBlockLine((642,71, 1263,369))
        self.col_detector.AppendBlockLine((577,487, 1073,738))      
        
        self.isShowBlockLine=False


    def update(self,deltat):
        self.image= self.src_image.subsurface(self.updateRect).convert()
        if(self.isShowBlockLine):
            for line in self.col_detector.BlockLine:
                relativeLine= self.GetRLine(line)
                #relativeLine= line
                pygame.draw.line(self.image, pygame.Color(255,0,0), (relativeLine[0], relativeLine[1]), (relativeLine[2], relativeLine[3]))

    def GetRLine(self, line):
        RLine=[]
        RLine.append(line[0] -self.GetRectOffset()[0])
        RLine.append(line[1] -self.GetRectOffset()[1])
        RLine.append(line[2] -self.GetRectOffset()[0])
        RLine.append(line[3] -self.GetRectOffset()[1])

        return RLine
 

    def MoveRect(self, direction): 

        current_left= self.updateRect[0]
        current_top= self.updateRect[1]
        current_right= self.updateRect[2]+current_left
        current_bottom = self.updateRect[3]+current_top        
        
        if direction == 'up':
            current_top-=self.MOVE_OFFSET #일단 좌상단 y축을 감소시켜보고
            if current_top<0: #0보다 작으면 안되므로
                current_top=0
                current_bottom= self.updateRect[3]
            else:
                current_bottom-=self.MOVE_OFFSET

        elif direction == 'down':
            current_bottom+=self.MOVE_OFFSET #일단 우하단 y축을 증가시켜보고

            if current_bottom> self.EntireMapRect[3]:
                current_bottom=self.EntireMapRect[3]
                current_top=self.EntireMapRect[3] - Global.gScreen.get_rect()[3]
            else:
                current_top+=self.MOVE_OFFSET           
        
        elif direction == 'left' :
            current_left-=self.MOVE_OFFSET

            if current_left <0:
                current_left=0
                current_right= Global.gScreen.get_rect()[2]
            else:
                current_right-=self.MOVE_OFFSET
        elif direction == 'right':
            current_right+=self.MOVE_OFFSET

            if current_right> self.EntireMapRect[2]:
                current_right= self.EntireMapRect[2]
                current_left= self.EntireMapRect[2]- Global.gScreen.get_rect()[2]
            else:
                current_left+=self.MOVE_OFFSET


        self.updateRect= (current_left, current_top, current_right- current_left, current_bottom- current_top)

    def GetRectOffset(self): 
        return (self.updateRect[0], self.updateRect[1])

    def ShowBlockLine(self):
        self.isShowBlockLine= True



        

        

class Tile(object):
    size=(64,64)

    def __init__(self, cost, blocking, rect):
        self.cost=1
        self.blocking= blocking



