## Thinking of two algorithms to meet the conditions provided in the robot treasure hunt problem

# first algorithm. bot moves 10 m out and back, adding 10 meters on to travel each time it crosses the origin. 
# this would look something like,
# increment = 10 
# distance reached =increment * numpasses
# distance traveled = (for each iteration) increment*numpasses *4 (this is for out back in both directions)


# Second Algorithm. Bot moves out in a gradually increasing amount each direction, lets say exponential. 
# increment = 10*e^numpasses
# distance reached  = needs to be calculated iteratively. 
# distance traveled = again iteratively 

import numpy as np
from decimal import *
import matplotlib.pyplot as plt
getcontext().prec = 2
energy_dist = Decimal(1000)
dist_reached = 0
increment = 10
dist_total = 0
t = 1



print("Alg 1 dist total", dist_total)
print("Alg 1 dist reached", dist_reached)

energy_dist = 1000
dist_reached = 0
increment = 10
dist_total = 0
t = 0
e = 2.718 #eulers number
while dist_reached < energy_dist :
    increment = 10*(e**(t/10)) #increasing increment exponentially each time
    dist_reached = increment
    dist_total += increment * 4
    t+= 1
print ("Alg 2 dist total", dist_total) 
print ("Alg 2 dist reached", dist_reached)

def alg_1(energy_dist):

    dist_reached = Decimal(0)
    increment = Decimal(10)
    dist_total = Decimal(1000)
    t = 1
    dist_reached_arr = np.array(())
    dist_total_arr = np.array(())

    while dist_reached < energy_dist :
        dist_reached = increment * t
        #assuming we are traveling the same dist on both sides of the axis with each pass
        dist_total += 4* dist_reached
        #now we are back at the origin ready to repeat
        dist_reached_arr = np.append(dist_reached_arr,[dist_reached])
        dist_total_arr = np.append(dist_total_arr,[dist_total])
        t += 1
        return dist_reached_arr, dist_total_arr
x,y = alg_1(1000)
plt.plot(x,y)
plt.show()

