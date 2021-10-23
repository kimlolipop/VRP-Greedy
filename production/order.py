# import DB
import pandas as pd


def Demand_list(): # input from api
    
    # {client id : [type, quantity, time request]}
    AllDetail_demand = {'0':[0,0,0],      
              '3':[1,2,500], 
              '223':[1,1,400],
              '21':[1,4,300],
             } 
    
    type_demand = {'0':0,      
              '3':1, 
              '223':1,
              '21':1,
             } 
    
    quantity_demand = {'0':0,      
              '3':2, 
              '223':1,
              '21':4,
             } 
    
    TimeRequest_demand = {'0':0,      
              '3':500, 
              '223':400,
              '21':300,
             } 

    
    return AllDetail_demand, type_demand, quantity_demand, TimeRequest_demand












# def merge_table(): #-- > ไม่ต้อง merge น่าจะเร็วกว่า
#     locate = customer_DB.locate()
#     demand = Demand_list()
    
#     locate_df = pd.DataFrame.from_dict(locate, orient='index', columns=['Lat', 'Long'])
#     demand_df = pd.DataFrame.from_dict(demand, orient='index', columns=['type', 'quantity', 'time request'])
#     df = pd.concat([locate_df, demand_df], axis = 1,join="inner")
    

#     print(df)
# merge_table()