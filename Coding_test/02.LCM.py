def insert_list(len_list):
    result = []
    input_list = input("최소공배수를 구할 값들을 입력해주세요 : ")
    temp = input_list.split(' ')

    # 예외처리
    if len(temp) != len_list:
        print("수열 개수와 입력 수열의 개수가 일치 하지 않습니다.")
        return

    for i in range(len(temp)):
        result.append(int(temp[i]))

    print(result)
    

if __name__ == '__main__':
    insert_list(3)