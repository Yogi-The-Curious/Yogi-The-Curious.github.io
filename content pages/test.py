#from tabulate import tabulate
from decimal import *
getcontext().prec = 2 #setting precision of decimals to 2 for currency operations

print("Gas milegae calculator!")
def calc(gas,mileage):
    ''' input: int,int
        return: tuple(int,int)
        
        takes gas and mileage and divides them to return miles/gal and gal/mile'''

    gpm = Decimal(gas/mileage)
    mpg = Decimal(mileage/gas)
    return (mpg,gpm)


def price_per (gpm,price):
    ''' input int, decimal
        return decimal
        multiplies mpg by price.'''

    ppm = Decimal(gpm * price)
    return ppm

gas = Decimal(input("Please enter Gallons\n"))
mileage = Decimal(input("Please enter miles\n"))
price = Decimal(input("Please enter cost per gallon\n"))

calcul_1 = calc(gas,mileage)
ppm = price_per(calcul_1[1],price)

#print(tabulate([[calcul_1[1]],[calcul_1[2]],[ppm]], headers=['MPG','Gallons/Mile',"$/Mile"], tablefmt='orgtbl'))

print("\nMiles Per Gallon: ", calcul_1[0] ,"\nCost Per Mile: $", ppm)

