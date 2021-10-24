def greedy(from2from_chart_distance, from2from_chart_TransitTime, quantity_demand, step_vehicle):
    # ใช้รถ ประเภทเดียวคำนวนเส้นทาง พอคำนวนเสร็จค่อยมาประเมินเวลาว่า เส้นทางไหน ระยะเวลารอ นานสุด ไปส่งอันนั้นก่อน
    # ถ้า route มากกว่า จำนวนรถ ที่เลือกมา ให้ตัดเส้นทางที่ ระยะคอยยังไม่นานออกไปก่อน

    sum_demand = sum(quantity_demand.values())
    sum_demand_dummy = sum(quantity_demand.values())
    target_ClientID = list(quantity_demand.keys())
    
    step_vehicle = step_vehicle
    count_route = -1
    route = []
    compare_distance = 9999
    
    while sum(quantity_demand.values()) > 0:
        route.append([])
        count_route += 1
        
        # =========select target that vehicle go to visit
       
        for i in range(0,step_vehicle + 1):
            
            # ====update location
            if i == 0: # ---> first location
                k = str(0)
                route[count_route].append(k)
            
            elif i == step_vehicle: # ---> next round is last step, come back store to fullfill goods
                k = 'last-step'
                route[count_route].append(destination)

            else: # ---> 
                k = destination
                route[count_route].append(k)
            ####end if
            
            
            # ====select target
            compare_distance = 9999
            if k == 'last-step': # ---> come back store to fullfill goods
                route[count_route].append(0)
                destination = str(0)
                k = destination
                
            else:
                for idx, ID in enumerate(target_ClientID):
                          
                    if compare_distance >= from2from_chart_distance[k][idx] and quantity_demand[ID] >= 1:
                        compare_distance = from2from_chart_distance[k][idx]
                        destination = ID
                        quantity_demand[destination] -= 1

                    elif compare_distance == 9999:
                        destination = str(0)

                    #### end if
                #### out for target_ClientID
            #### end if     
#             print(i,destination, quantity_demand, from2from_chart_distance[k]) ##--> print check value
            
        #### out for step
        
    #### out while
#     print(route) ##--> print check route

    return route
        