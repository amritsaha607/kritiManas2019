import numpy as np

def deg2rad(deg):
    return (deg*(np.pi))/180

def calcDist(lat1, lon1, lat2, lon2):
    r = 6371 # Radius of earth
    dLat = deg2rad(lat2-lat1)
    dLon = deg2rad(lon2-lon1)
    a = (np.sin(dLat/2))**2 + (np.cos(deg2rad(lat1)))*(np.cos(deg2rad(lat2))) + (np.sin(dLon/2))**2
    c = 2 * np.arctan(np.sqrt(a)/np.sqrt(1-a))
    d = r*c
    return d

p = calcDist(21, 1 , 5 , 6)
