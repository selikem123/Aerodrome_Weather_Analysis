#importing libraries
import matplotlib as mplt
import csv 

#function to calculate density
def density(P,R,T):
    C_density = P/(R*T)
    return(C_density)
