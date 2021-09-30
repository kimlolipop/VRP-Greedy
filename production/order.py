import customer_DB
import pandas as pd


def Demand_list(): # input from api
    
    # {client id : [type, quantity, time request]}
    demand = {'0':[0,0],      
              '3':[1,2,500], 
              '223':[1,1,400],
              '21':[1,1,300],
             } 
    
    return demand




# def merge_table(): #-- > ไม่ต้อง merge น่าจะเร็วกว่า
#     locate = customer_DB.locate()
#     demand = Demand_list()
    
#     locate_df = pd.DataFrame.from_dict(locate, orient='index', columns=['Lat', 'Long'])
#     demand_df = pd.DataFrame.from_dict(demand, orient='index', columns=['type', 'quantity', 'time request'])
#     df = pd.concat([locate_df, demand_df], axis = 1,join="inner")
    

#     print(df)
# merge_table()