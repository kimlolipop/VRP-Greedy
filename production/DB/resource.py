# global --> I think it must call from csv
_vehicle = {'bike':[2,2],
            '4wheel':[1,4] # {type: [quantity, capacity]}
            }

# select car
def cal_SelectVehicle(quantity_demand):
    sum_demand = sum(quantity_demand.values())
    
    if sum_demand > _vehicle['bike'][1]: # order more than bike in 1 round
        if _vehicle['4wheel'][0] > 0:
            return '4wheel'
    
    for typ in _vehicle: # normal situation choose smallest car first
        if _vehicle[typ][0] > 0:
            return typ
        
    return 'non' # no car in resource
    
# calculate step and manage resource    
def cal_StepVehicle(type_car):
        
    if type_car == 'non':
        cartravel = 0
    elif type_car == '4wheel':
        cartravel = _vehicle[type_car][1]
    elif type_car == 'bike':
        cartravel = _vehicle[type_car][1]
    
#     cal_resource(type_car)
    
    return cartravel

def cal_resource(type_car):
    
    if type_car == 'non':
        print('no car more')
        pass
    else:
        global _vehicle
        _vehicle[type_car][0] -= 1
    
        print(type_car)
        print(_vehicle)

