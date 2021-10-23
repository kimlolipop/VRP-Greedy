import pandas as pd
import numpy as np

import cal_distance
import order
import DB
import step_method

# =============demand check
#demand
AllDetail_demand, type_demand, quantity_demand, TimeRequest_demand = order.Demand_list() # {client id : [type, quantity, time request]}
locate = DB.locate() # {client id: [lat,long]} --> all user in client

# distance from to from
target_ClientID = list(AllDetail_demand) # [client id{1}, client id{2}, client id{...}, client id{n}]
target_LatLong = pd.DataFrame.from_dict(locate, orient='index', columns=['Lat', 'Long']) # df --> [client id, Lat, Long]
from2from_chart_distance, from2from_chart_TransitTime = cal_distance.cal_Distance_TransitTime(target_ClientID, target_LatLong)

## - - - print recheck value distace and transit time

# print(list(from2from_chart_distance.values())[0]) # --> find index of min value in dict
print(from2from_chart_distance[str(21)].index(min(from2from_chart_distance[str(21)]))) # --> find index of min value in dict

# print("target_clientID --> \n", target_ClientID)
# print("target_LatLong --> \n", target_LatLong)

# print('\nDistance\n',from2from_chart_distance) 
# print('\n \nTransit_time\n', from2from_chart_TransitTime)

# ===========================Setup Parameter
count_loop = 0
route = [[]]

# ===========resource check
type_car = DB.select_vehicle(quantity_demand)
# print(type_car)

step_car = DB.step_vehicle(type_car)
# print(step_car)

# Algorithm
step_method.greedy(from2from_chart_distance, from2from_chart_TransitTime, quantity_demand, step_car)







