def greedy(from2from_chart_distance, from2from_chart_TransitTime, quantity_demand, step_car):
    count_loop = 0
    route = [[]]
    sum_demand = sum(quantity_demand.values())
    