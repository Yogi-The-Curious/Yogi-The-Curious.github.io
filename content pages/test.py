import numpy as np

dist_arr = np.array([])
gas_arr = np.array([])
mpg = 34
gas2_arr = np.array([])


for num in range(8,51):
    gas_arr = np.append(gas_arr, [num])

for num in range(28,35):
    gas2_arr = np.append(gas2_arr, [num])


def rangecalc(gas_arr, dist_arr, mpg):

    for gal in gas_arr:
        dist = gal*mpg
        dist_arr = np.append(dist_arr,[dist])
    return dist_arr


dist1_arr = rangecalc(gas_arr,dist_arr,mpg)
dist2_arr = rangecalc(gas2_arr, dist_arr,mpg)

print(dist1_arr)
print(dist2_arr)


 



def caluclations():
ypos_arr = np.array([])
 ## takeoff()
    for t in time:
        calculations 
        
        if y < ypos_arr[t-1]
            return xpos,ypos,xvel,yvel, t


def nextcalc(xpos,ypos,xvel,yvel)
    for time in range(t,finaltime)
