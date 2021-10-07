import time
from math import cos, asin, sqrt, pi

# start = time.time()

# method distance
def ucredient_distance(lat1, lon1, lat2, lon2):
    d = sqrt(((lat2-lat1)**2) + ((lon2-lon1)**2))
    return d

def haversine_distance(lat1, lon1, lat2, lon2): # great-circle distance
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a)) #2*R*asin...

# method transit time
def physic_fomular_time(s, v=40):
    t = (s/v) * 1.2  # --> v =s/t : v = km/min, s = km, t = min
    return t

# def cal_transit_time(route, df):
    

def cal_Distance_TransitTime(route, df): #--> distance and transit time
    distance_list = []
    transit_time_list = []
    
    #=====================calculate distance=================
    method = 'ucredient_distance'
    for idx, p1 in enumerate(route):
        distance_list.append([])
        transit_time_list.append([])
        
        lat1 = df['Lat'].loc[p1]
        lon1 = df['Long'].loc[p1]
        for p2 in route:
            lat2 = df['Lat'].loc[p2]
            lon2 = df['Long'].loc[p2]
            # print(lat1,lon1, lat2, lon2)
            
            # choose method
            if method == 'ucredient_distance':
                distance = ucredient_distance(lat1,lon1, lat2, lon2)
            elif method == 'haversine_distance':
                distance = haversine_distance(lat1,lon1, lat2, lon2)
              
            # cal transint time from distance 
            transit_time = physic_fomular_time(distance)
    
            transit_time_list[idx].append(distance)
            distance_list[idx].append(distance)
    
    return distance_list, transit_time_list

