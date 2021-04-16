def solution(bridge_length, weight, truck_weights):
    on_bridge = []
    total_weight = 0
    answer = 0
    
    truck_weights.reverse()
    
    while truck_weights:
        answer += 1
        
        if len(on_bridge) == bridge_length:
            total_weight -= on_bridge.pop(0)
        
        if (total_weight + truck_weights[-1]) <= weight:
            on_bridge.append(truck_weights[-1])
            total_weight += truck_weights.pop()
            
        else:
            on_bridge.append(0)
    
    
    answer += bridge_length
    
    return answer