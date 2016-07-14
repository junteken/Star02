import Global, pygame, UnitState
from UnitState import *

class UnitSprite(pygame.sprite.Sprite):    
    def __init__(self,Unit, image,spriteinfo, position):
        pygame.sprite.Sprite.__init__(self)
        self.Unit= Unit;        
        self.spriteinfoIdx=Unit.IdleSpriteList #생성시에는 Idle이미지로 보여준다.
        self.spritename=spriteinfo[0]
        self.currentFrame=0
        src_image=pygame.image.load(image)
        self.imageList=[]

        for idx in range(1, len(spriteinfo)):#자기 객체에 대한 이미지 list만 따로 만들어 사용한다.
            self.imageList.append(src_image.subsurface(spriteinfo[idx]).convert())               
        
        self.image=self.imageList[0]
        #self.isSelected=False #향후 refactoring필요       

    def update(self,deltat):
        # SIMULATION        
        self.Unit.StatusUpdate()
        self.currentFrame+=1
        if(self.currentFrame >= len( self.spriteinfoIdx) ):
            self.currentFrame=0
        #self.image= self.src_image.subsurface(self.spriteinfoList[self.currentFrame]).convert()
        self.image= self.imageList[self.spriteinfoIdx[self.currentFrame]]
        self.image.set_colorkey(pygame.Color(72,72,88))        
        #self.rect= self.Unit.position
        self.rect=  (self.Unit.position[0] - Global.map_h.GetRectOffset()[0] -self.image.get_rect().width//2, self.Unit.position[1]- Global.map_h.GetRectOffset()[1] -self.image.get_rect().height//2)

        print('current rect =', self.rect)

        if(self.Unit.stateInt == Global.gCmdListInt[1]):#selected state인 경우 자기주위에 원을 그리는 코드
            pygame.draw.circle(Global.gScreen, pygame.Color(255,0,0), self.Unit.GetRpos(), 30, 5)
            #pygame.draw.circle(Global.gScreen, pygame.Color(255,0,0), (self.Unit.position[0]+self.image.get_rect().width//2, self.Unit.position[1]+self.image.get_rect().height//2) , 30, 5)

class UnitBase(object):
    """UnitBase class"""
    
    stateObject= [IdleState(), SelectState(), MoveState(), AttackState()]
        
    def __init__(self, arg_name, position):        
        self.name=arg_name
        self.stateInt= Global.gCmdListInt[0] #생성시 Idle state로 setting
        self.targetPos= self.position= position
        return super().__init__()

    def draw(self):
        raise NotImplementedError("UnitBase class must not be instantiated!!!")

    def GetRpos(self):
        return (self.position[0] - Global.map_h.GetRectOffset()[0],  self.position[1]- Global.map_h.GetRectOffset()[1])
    

class Protoss(UnitBase):
    """Protoss class"""

    def __init__(self, arg_name, position):
        return super().__init__(arg_name, position)

    def draw(self):        
        print('I am Protoss class',self.name)        

    shield=0

class Zealot(Protoss):
    """Zealot class"""

    AttackSpriteList= list(range(1, 70, 17))
    MoveSpriteList= list(range(86, 205, 17))#85 ~ 204
    IdleSpriteList= list(range(1, 17))
    
    MOVE_SPEED=5    
    
    #__SpriteList는 모든 객체가 공통으로 가지는 이미지 리소스이므로 class 변수(C++에서는 static에 해당)로 정의함    
    def __init__(self, position):
        self.name= 'zealot'
        self.SpriteList= UnitSprite(self,  Global.gRsrcExtractor.GetUnitPngFileName(self.name), Global.gRsrcExtractor.GetSpriteInfo(self.name), position)
        return super().__init__('zealot', position)

    def draw(self):
        print('I am {0} class'.format(self.name))       
        return self.SpriteList

    def StatusUpdate(self):
        #자신의 상태에 맞게 행동을 계속 해야한다.
        
        if(self.stateInt == Global.gCmdListInt[2]):
            x=self.position[0]+ self.MOVE_SPEED
            y=self.position[1]+ self.MOVE_SPEED
            
            if(x> self.targetPos[0]):
                x= self.targetPos[0]
            if(y> self.targetPos[1]):
                y= self.targetPos[1]

            if((x,y) == self.targetPos):#이동이 완료되면 state를 변경해줘야 한다.
                self.stateInt= Global.gCmdListInt[0]

            self.position= (x,y)
        

        print('I am {0} class'.format(self.name))

    def Move(self, targetXY, targetOb):
        #17,34, 51, 68
        #
        self.targetPos= targetXY
        self.SpriteList.spriteinfoIdx = self.MoveSpriteList
        self.SpriteList.isSelected= False

        pygame.mixer.music.load('.\\sound\\protoss\\zealot\\pzewht00.wav')
        pygame.mixer.music.play()
        print('Move cmd received')

    def Attack(self,targetXY, targetOb):
        self.SpriteList.spriteinfoList = self.AttackSpriteList
        self.SpriteList.isSelected= False
        print('Attack cmd received')

    def Select(self,fake_arg1, fake_arg2):
        self.SpriteList.spriteinfoList = self.IdleSpriteList
        self.SpriteList.isSelected= True
        print('Select cmd received')

    def Idle(self,fake_arg1, fake_arg2):
        self.SpriteList.spriteinfoList = self.IdleSpriteList
        self.SpriteList.isSelected= False
        print('UnSelect cmd received')

    CmdOpList=[Idle, Select, Move, Attack]

    def HandleCmd(self, Cmd, Unit, targetXY, targetOb):
        self.stateObject[self.stateInt].handleInput(Cmd, self, targetXY, targetOb)
