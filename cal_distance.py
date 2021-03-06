import time
from math import cos, asin, sqrt, pi

def ucredient(lat1, lon1, lat2, lon2):
    d = math.sqrt(((lat2-lat1)**2) + ((lon2-lon1)**2))
    return d

def haversine(lat1, lon1, lat2, lon2): # great-circle distance
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a)) #2*R*asin...

def cal(route, lat_long_df):
    distance = []
    for idx, p1 in enumerate(route):
        distance.append([])
        lat1 = lat_long_df['Lat'].loc[p1]
        lon1 = lat_long_df['Long'].loc[p1]

        for p2 in route:
            lat2 = lat_long_df['Lat'].loc[p2]
            lon2 = lat_long_df['Long'].loc[p2]
            
            #===============choose method
            d = haversine(lat1,lon1, lat2, lon2)
#             d = ucredient(lat1,lon1, lat2, lon2)

            distance[idx].append(d)
            

    return distance
   