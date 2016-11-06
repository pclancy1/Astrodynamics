from example import Vector   ## imports the vector function
import matplotlib.pyplot as plt
import numpy as np
import math


class target:

    def __init__(self,x,y,z,vel0,m0,alt0,inc0):   ## sets parameters for the target vehicle ## alt is distance above surface of earth
        self.pos = Vector(x,y,z)   ## <0,0,0> is the center of the earth
        self.vel = vel0
        self.m = m0
        self.alt = alt0
        self.inc = inc0
        self.thrust = 0      ## initial
        self.grav = 0        ## initial

    def fgrav(self):         ## determines force of gravity on target
        G = 6.67*10**(-11)   ## meters, kgs, seconds
        M = 6*10**(26)       ## mass of earth
        self.grav = (G*M*self.m)/(self.alt + EARTH_RADIUS)

    def updatepos(self):
        dt = 15          # default delta time of 15 sec
        Fnet = self.thrust + self.grav
        self.pos = self.pos + (Fnet*dt)/self.m

    def updatepos(self,dt):
        Fnet = self.thrust + self.grav
        self.pos = self.pos + (Fnet*dt)/self.m
