### Helpin aug with some physics

import sys
import numpy as np
import matplotlib.pyplot as plt
from decimal import *

getcontext().prec = 5


def horiz_dist (vi,t,deg): # calculate horizontal distance travelled after t seconds, with initial velocity v0, and deg shoot angle
    t_max= ground_speed(vi,deg)
    rad = np.radians(deg) 
    v_horiz = vi * np.cos(rad)
    if t <= t_max:
        dist = v_horiz * t
    else:
        dist = v_horiz * t_max
    return dist

GRVTY = 9.8       

def vert_dist(vi,t,deg): # calculate vertical distance to earth after t seconds, with initial velocity v0, and deg shoot angle
    h_i = Decimal(1.25) # intial height

    if t == 0: # returns initial height at time 0
        return h_i

    rad = np.radians(deg) 
    v_vert = vi * np.sin(rad)
    h = v_vert * t - (0.5 * GRVTY * t**2) + h_i #good ol kinematics

    if h >= 0:  
        return h

    else:
        return 0

def time_checker(vi,deg):
    h_i = Decimal(1.25) # intial height
    rad = np.radians(deg)

    while h > 0: 
        t += 1
        v_vert = vi * np.sin(rad)
        h = v_vert * t - (0.5 * GRVTY * t**2) + h_i #good ol kinematics
    return t


def ground_speed(vi,deg): #calculate airtime 
    rad = np.radians(deg) 
    v_horz = vi * np.cos(rad)
    speed = v_horz #good ol kinematics
    return speed



time = time_checker(20,0)
print("this is time until ground", time)
#def hls_d

vi=20 #initial velocity
degs = [0,15,25,35,45] #initial release angle
#t_grounds = [ground_speed(vi,d) for d in degs] # airtime for all angles
#t_ground = max(t_grounds)      

#print ("this is t_ground",t_ground)


time_interval = .01 #distance between each interval 
#t_steps = np.arange(0,t_ground+time_interval,time_interval) # produce list of times to iterate over, based on time interval and longest time till ground for all angles. 

#hls = [[horiz_dist(vi,t,d) for t in t_steps] for d in degs] # create list of horizontal position in each given time for each angle
#print(hls)
#hls = [horiz_dist(vi,t,degs[0]) for t in t_steps]

#print (hls)

#for deg in degs:

   # hls_[deg] = [[horiz_dist(vi,t,degs[deg])] for t in t_steps]

    #print ("this works",hls_[deg])
#hls_2 = [[]]

#plt.figure()

#plt .subplot().set(xlabel = 'Distance (m))', ylabel = 'Height(m)', title = '2d kinematics graph with no air resistance', )


