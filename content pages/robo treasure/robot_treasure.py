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




def alg_2(energy_dist):
    '''
    param: energy_dist int
    return  dist_reached_arr numpy array
            dist_total_arr  np array

    calculates the total distance traveled to cover the given distance to energy (params)
    utilizing our second algorithm:
    Bot travels out 10 meters and then back, repeats in the opposite direction.
     Then goes out e**(t/10) further and the same in the opposite direction,
    increasing logarithmically until the parameter is met.  
    '''
    dist_reached = 0
    increment = 0
    dist_total = 0
    dist_reached_arr = np.array(())
    dist_total_arr = np.array(())
    t = 0
    e = 2.718 #eulers number
    while dist_reached < energy_dist :
        increment = 10*(e**(t/10)) #increasing increment exponentially each time
        dist_total += increment * 4 #accounts for out right +back +out left +back
        dist_reached =increment
        dist_total_entry = dist_total/ 1000 #scaling up array entry to km for ease of reading
        dist_reached_arr = np.append(dist_reached_arr,[dist_reached])
        dist_total_arr = np.append(dist_total_arr,[dist_total_entry])
        t+= 1
     #   print(t)
    #print(increment)
    #print(dist_total)
    return dist_reached_arr, dist_total_arr

def alg_1(energy_dist):
    '''
    params: energy_dist: int 
    returns: dist_reached_arr: np array
             dist_total_arr: np arry

    calculates the total distance traveled to cover the given distance to energy (params)
    utilizing our first algorithm:  
    robot moves 10 m out and back, Then 10 meters out and back in the oppostie direction, 
    then 20 each way and so on incrementing by 10 each time. 
    '''
    dist_reached =0
    increment = 10
    dist_total = 0
    dist_reached_arr = np.array(())
    dist_total_arr = np.array(())
    t = 1

    while dist_reached < energy_dist :
        dist_reached = increment * t
        #assuming we are traveling the same dist on both sides of the axis with each pass
        dist_total += 4* dist_reached #accounts for out right +back +out left +back
        #now we are back at the origin ready to repeat
        dist_total_entry = dist_total/1000 # scaling up entry into array to km for ease of reading
        dist_reached_arr = np.append(dist_reached_arr,[dist_reached])
        dist_total_arr= np.append(dist_total_arr,[dist_total_entry])
        t +=1

    #print(dist_reached)
    #print(dist_total)
    return dist_reached_arr, dist_total_arr

def main():

    #calling algorithms to create data
    x,y = alg_1(1000)
    f,z = alg_2(1000)

    #plotting the data
    plt.figure()
    plt.subplot().set(xlabel = "Distance to Energy(m)", ylabel = "Total Distance (Km)", title = "Total Distance to Energy")
    plt.plot(x,y, "g--", label = "Alg 1")
    plt.plot(f,z, "b--", label = "Alg 2")
    plt.legend()
    plt.show()
    return

main()