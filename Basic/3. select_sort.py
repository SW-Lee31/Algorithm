def selection_sort(list):
    for i in range(len(list)):
        min = list[i]
        for j in range(i, len(list)):
            if min > list[j]:
                min = list[j]
                temp = j
        list[i], list[temp] = min, list[i]

    return list

print(selection_sort([3,4,6,2,13,4,5,2,1,4,7,8]))