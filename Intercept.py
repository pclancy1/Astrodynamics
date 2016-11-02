from example import Vector

class target:

    def __init__(self,x,y,z,vel0,m0,alt0,inc0):   # sets parameters for the target vehicle
        self.pos = Vector(x,y,z)
        self.vel = vel0
        self.m = m0
        self.alt = alt0
        self.inc = inc0

    def fgrav(self):     # determines force of gravity on target
        G = 6.67*10**(-11)
        M = 6*10**(26)
        return (G*M*self.m)/self.alt
