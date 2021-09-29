def Dem():
    
    # {client id : [type, quantity, time request]}
    demand = {'0':[0,0],      
              '3':[1,2,500], 
              '223':[1,1,400],
              '21':[1,1,300],
             } 
    
#     demand = [0, 2, 1, 1, 1, 1, 1] # 0 is distribute
    return demand


# def Time():
#     ordertime = [[],
#         [1, 9999],
#         [2, 570],
#         [3, 585],
#         [4, 601],
#         [5, 605],
#         [6, 645],
#         [7, 570]]

#     return ordertime
