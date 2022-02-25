import re
import sys

def insert_value(amount):
    input_lst = input("수열을 입력해주세요 : ")
    output_val = input_lst.split(' ')

    for i in range(len(output_val)):
        output_val[i] = int(output_val[i])

    # 예외처리 
    if len(output_val) != amount:
        print('입력 수열의 수가 일치 하지 않습니다.')
        return False

    return output_val

def check(list, value):
    result = []
    temp1 = []
    temp2 = prim(int(value))

    for i in range(len(list)):
        temp1 = prim(list[i])
        for j in range(len(temp1)):
            if temp1[j] in temp2:
                break
            result.append(list[i])
            break
            
    return result

def prim(digit):
    divisor = []

    for i in range(2, digit + 1):
        if digit % i == 0:
            divisor.append(i)

    return divisor

if __name__ == '__main__':
    amount = input('수열개수를 입력해주세요 : ')
    list = insert_value(int(amount))
    avg = 0

    if list == False:
        sys.exit()

    o_lst = check(list, input('서로소를 확인 할 값을 입력해주세요 : '))

    for i in range(len(o_lst)):
        avg += o_lst[i]
    
    result = avg / len(o_lst)
    print(result)