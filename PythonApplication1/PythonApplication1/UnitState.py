import Global

#gCmdList=['IDLE', 'SELECT', 'MOVE', 'ATTACK']
class IdleState(object):
    def __init__(self):
        pass
    """UnitState class"""
    def handleInput(self, Cmd, Unit, targetXY, targetOb):
        if(Cmd == Global.gCmdList[Global.gCmdListDict['SELECT']]):#idle state는 오직 select state로만 이동 가능하다.
            Unit.stateInt= Global.gCmdListDict[Cmd]
            Unit.CmdOpList[Unit.stateInt](Unit, targetXY, targetOb)


class SelectState(object):
    """UnitState class"""
    def __init__(self):
        pass

    def handleInput(self, Cmd, Unit, targetXY, targetOb):        
        Unit.stateInt= Global.gCmdListDict[Cmd] #select state는 모든 state로 이동 가능
        Unit.CmdOpList[Unit.stateInt](Unit, targetXY, targetOb)
        

class MoveState(object):
    """UnitState class"""
    def __init__(self):
        pass

    def handleInput(self, Cmd, Unit, targetXY, targetOb):
        if(Cmd == Global.gCmdList[Global.gCmdListDict['ATTACK']]):#move state는 cmd를 받아서 갈수 있는 state는 오직 ATTACK만 가능
            Unit.stateInt= Global.gCmdListDict[Cmd]
            Unit.CmdOpList[Unit.stateInt](Unit, targetXY, targetOb)

class AttackState(object):
    """UnitState class"""
    def __init__(self):
        pass

    def handleInput(self, Cmd, Unit, targetXY, targetOb):
        if(Cmd == Global.gCmdList[Global.gCmdListDict['MOVE']]):#attck state는 cmd를 받아서 갈수 있는 state는 오직 MOVE만 가능
            Unit.stateInt= Global.gCmdListDict[Cmd]
            Unit.CmdOpList[Unit.stateInt](Unit, targetXY, targetOb)