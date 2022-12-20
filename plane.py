"""
Problem: Solution to schedule transportation of people from source to destination, where there are N groups of people and M planes

Solution Overview:
    - Maintain people as a sorted list in descending order
    - Maintain planes as a sorted dictionary in descending order

    - There is a main loop that iterates through the people list, and keeps processing it, one element at a time, to move the group to destination, until there are no more elements in that list

TODO:
    - Currently the plan to group matching follows a first-fit approach. Needs to be improved to find an optimal fit
"""

def input_fn(people_list, plane_list): 
    if sum(plane_list) < max(people_list):
        return "It is not possible to transport the people"
    
    people_list.sort(reverse = True)
    plane_list.sort(reverse = True)
    print(people_list, plane_list)
    pos_list = [0] * len(plane_list)
    plane_dict = dict(zip(plane_list, pos_list))
    
    final_cost = 0
    #main while loop
    while (len(people_list) != 0):
        print("List of passengers: ", people_list)
        top = people_list[0]
        people_list.pop(0)
        
        num_planes = find_planes(top, plane_list)
        
        final_cost += calc_cost(num_planes, plane_dict)
        
    return final_cost

"""
Helper function find_planes returns the number of planes needed to transport a
"""
        
def find_planes(people, plane):
    cap = 0
    for i in range(len(plane)):
        cap += plane[i]
        if (cap >= people):
            return i+1

"""
Helper function calc_cost finds the cost needed for plans to move the group from source to destination, based on the current location of the planes
"""
def calc_cost(num_planes, pl_dict):
    cost = 0
    for i in range(num_planes):
        plane_id = list(pl_dict.keys())[i]
        if (list(pl_dict.values())[i] == 0):
            cost += 1
            pl_dict[plane_id] = 1
        else:
            cost += 2
            
    return cost