import pygame, ResourceExtractor, MapHandler

gScreen=pygame.display.set_mode((640,480))
clock=pygame.time.Clock()

gRsrcExtractor=ResourceExtractor.ResourceExtractor(['protoss_a', 'protoss_b', 'protoss_c'])

gCmdList=['IDLE', 'SELECT', 'MOVE', 'ATTACK']
gCmdListInt=(0, 1, 2, 3)
gCmdListDict=dict(zip(gCmdList, gCmdListInt))

map_h= MapHandler.MapHandler('MAP.png')
Map_group= pygame.sprite.Group()
map_h.ShowBlockLine()

