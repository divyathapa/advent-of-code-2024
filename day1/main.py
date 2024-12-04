location_id = []
historian_group_1 = [3,4,2,1,3,3]
historian_group_2 = [4,3,5,3,9,3]

sorted_group_1 = [1,2,3,3,3,4]
sorted_group_2 = [3,3,3,4,5,9]

distance_between_1_and_2 = [2,1,0,1,2,5]

def sort_list(to_be_sorted_list):
    sorted_list = to_be_sorted_list.sort()
    return sorted_list

def distance_to_calculate(sorted_list_1, sorted_list_2):
    total_distance = []

    for i in range(len(sorted_list_1)):
        if sorted_list_2[i]>= sorted_group_1[i]:
            total_distance.append(sorted_list_2[i]- sorted_list_1[i])
        else:
            total_distance.append(sorted_list_1[i])
    return total_distance

def calculate_total_distance(distance_to):
     print (sum(distance_to))


calculate_total_distance(distance_to_calculate(sorted_group_1, sorted_group_2))