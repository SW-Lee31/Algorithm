def select_sort(list):
    for i in range(len(list)):
        min = list[i]
        for j in range(i, len(list)): #i 에서 len(list)가 어떤 역할?
            if min > list[j]:
                min = list[j]
                temp = j
        list[i], list[temp] = min, list[i]

    return list

print(select_sort([4,2,6,4,1,2,4,7,9,5,1,11,5,44,7]))