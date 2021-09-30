# global --> I think it must call from csv
_vehicle = {'bike':[2,2],
            '4wheel':[1,4] # {type: [quantity, capacity]}
            }

def select_vehicle(order):
    
    if order > _vehicle['bike'][1]: # order more than bike in 1 round
        if _vehicle['4wheel'][0] > 0:
            return '4wheel'
    
    for typ in _vehicle: # normal situation choose smallest car first
        if _vehicle[typ][0] > 0:
            return typ
        
    return 'non' # no car in resource
    
    
def step_vehicle(car_type):
        
    if car_type == 'non':
        cartravel = 0
    elif car_type == '4wheel':
        cartravel = _vehicle[car_type][1]
    elif car_type == 'bike':
        cartravel = _vehicle[car_type][1]
    
    cal_resource(car_type)
    
    return cartravel

def cal_resource(car_type):
    
    if car_type == 'non':
        print('no car more')
        pass
    else:
        global _vehicle
        _vehicle[car_type][0] -= 1
    
        print(car_type)
        print(_vehicle)


