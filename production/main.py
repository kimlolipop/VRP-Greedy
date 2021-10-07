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
distance_from2from_chart, TransitTime_from2from_chart = cal_distance.cal_Distance_TransitTime(target_ClientID, target_LatLong)

print("target_clientID --> \n", target_ClientID)
print("target_LatLong --> \n", target_LatLong)


print(distance_from2from_chart) #-->  recheck from to from chart again
print(TransitTime_from2from_chart)








