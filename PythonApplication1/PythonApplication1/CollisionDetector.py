import math

class CollisionDetector(object):
    """description of class"""
    def __init__(self):
        self.BlockLine=[]
        

    def AppendBlockLine(self, line):
        self.BlockLine.append(line)
        

    def CheckCollision(self, unit):
        for line in self.BlockLine:
            distance= self.dist(line, unit)

            #print('Distance is =', distance)
            if distance < 30:
                return True
           
        return False
                


    def dist(self, line, unit): # x3,y3 is the point
        x1=line[0]
        y1=line[1]
        x2=line[2]
        y2=line[3]
        x3=unit.position[0]
        y3=unit.position[1]

        px = x2-x1
        py = y2-y1

        something = px*px + py*py

        u =  ((x3 - x1) * px + (y3 - y1) * py) / float(something)

        if u > 1:
            u = 1
        elif u < 0:
            u = 0

        x = x1 + u * px
        y = y1 + u * py

        dx = x - x3
        dy = y - y3

        # Note: If the actual distance does not matter,
        # if you only want to compare what this function
        # returns to other results of this function, you
        # can just return the squared distance instead
        # (i.e. remove the sqrt) to gain a little performance

        dist = math.sqrt(dx*dx + dy*dy)

        return dist






