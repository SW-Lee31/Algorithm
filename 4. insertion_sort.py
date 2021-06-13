def insertion_sort(list):
    for i in range(len(list)):
        for j in range(i):
            if list[i] < list[j]:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp

    return list

print(insertion_sort([4,5,1,7,13,9,2,14,11,1,5,3,2,6]))
