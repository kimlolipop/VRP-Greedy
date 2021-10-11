import pandas as pd
import cal_distance
import order
import DB

# =============demand check
#demand
demand = order.Demand_list() # {client id : [type, quantity, time request]}
locate = DB.locate() # {client id: [lat,long]} --> all user in client

# distance from to from
target_ClientID = list(demand) # [client id{1}, client id{2}, client id{...}, client id{n}]
target_LatLong = pd.DataFrame.from_dict(locate, orient='index', columns=['Lat', 'Long']) # df --> [client id, Lat, Long]
from2from_chart_distance, from2from_chart_TransitTime = cal_distance.cal_Distance_TransitTime(target_ClientID, target_LatLong)

print("target_clientID --> \n", target_ClientID)
print("target_LatLong --> \n", target_LatLong)

print('\nDistance\n',from2from_chart_distance) 
print('\n \nTransit_time\n', from2from_chart_TransitTime)

# ===========resource check
type_car = DB.select_vehicle(demand)
print(type_car)





