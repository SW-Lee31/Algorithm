import math

def insert_list(len_list):
    value = []
    input_list = input("최소공배수를 구할 값들을 입력해주세요 : ")
    temp = input_list.split(' ')

    # 예외처리
    if len(temp) != len_list:
        print("수열 개수와 입력 수열의 개수가 일치 하지 않습니다.")
        return

    for i in range(len(temp)):
        value.append(int(temp[i]))
    
    return value
    
def primary(value):
    for i in range(2, int(math.sqrt(value)) + 1):
        if value % i == 0:
            return False
        
    return True


if __name__ == '__main__':
    amount = input("처리할 수열의 개수를 입력해주세요 : ")
    value = insert_list(int(amount))
    result_list = []
    result = 1

    for i in range(len(value)):
        if primary(value[i]) == True:
            result_list.append(value[i])
    
    if len(result_list) == 0:
        result *= -1

    for i in range(len(result_list)):
        result *= result_list[i]

    print(result)