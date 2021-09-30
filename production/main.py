import pandas as pd

import cal_distance
import customer_DB
import order
import resource


# =============demand check
#demand
demand = order.Demand_list() # {client id : [type, quantity, time request]}
locate = customer_DB.locate() # {client id: [lat,long]} --> all user in client

# cal from to from
target_ClientID = list(demand) # [client id{1}, client id{2}, client id{...}, client id{n}]
target_LatLong = pd.DataFrame.from_dict(locate, orient='index', columns=['Lat', 'Long']) # df --> [client id, Lat, Long]
from2from_Chart = cal_distance.cal(target_ClientID, target_LatLong)



print(from2from_Chart) #-->  recheck from to from chart again








