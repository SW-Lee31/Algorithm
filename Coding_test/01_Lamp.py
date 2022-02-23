lamp = []

def create_lamp(amount):
    global lamp
    lamp_input = input('램프 상태를 입력해주세요 : ')
    lamp_value = lamp_input.split(' ')

    if len(lamp_value) != amount:
        print('입력 개수가 일치 하지 않습니다.')
        return
    for lamp_value_check in range(len(lamp_value)):
        if int(lamp_value[lamp_value_check]) >= 2 or  int(lamp_value[lamp_value_check]) < 0:
            print('램프 상태의 입력이 잘못 됐습니다.')
            return
    
    for i in range(len(lamp_value)):
        lamp.append(int(lamp_value[i]))


def execute_1(lamp, i, x):
    lamp[i - 1] = x
    #print(lamp)

def execute_2(lamp, l, n):
    for i in range(l - 1, n):
        if int(lamp[i]) == 1:
            lamp[i] = 0
        else:
            lamp[i] = 1
    #print(lamp)

def execute_3(lamp, l, n):
    for i in range(l - 1, n):
        lamp[i] = 0
    #print(lamp)

def execute_4(lamp, l, n):
    for i in range(l - 1, n):
        lamp[i] = 1
    #print(lamp)
    
def input_string():
    global lamp
    input_value = input("명령어와 매개변수를 입력하세요 : ")
    input_result = input_value.split(' ')
    exe = int(input_result[0])
    param1 = int(input_result[1])
    param2 = int(input_result[2])

    # 제한 예외처리
    if len(input_result) != 3:
        print('명령어 형식이 잘못되었습니다. (명령어, 매개변수1, 매개변수2)')
        return
    # 명령어1 제한
    if exe == '1':
        if param1 <= 1:
            print('i값을 다시 입력해주세요 (조건 : 1 <= i <= N)')
            return
        if param2 > 1 or param2 < 0:
            print('x값을 다시 입력해주세요 (조건 : 0 <= x <= 1)')
            return
    # 명령어2, 3, 4 제한
    elif exe == '2' or exe == '3' or exe == '4':
        if param1 > param2:
            print('매개변수1은 매개변수2보다 작아야 합니다')
            return
        if param1 < 0 or param2 < 0:
            print('매개변수는 1이상 이어야 합니다.')
            return
    

    if exe == 1:
        execute_1(lamp, param1, param2)
    elif exe == 2:
        execute_2(lamp, param1, param2)
    elif exe == 3:
        execute_3(lamp, param1, param2)
    elif exe == 4:
        execute_4(lamp, param1, param2)

if __name__ == '__main__':
    amount, exe_amount = input('램프 개수와 명령어 횟수를 입력하세요 : ').split(' ')
    create_lamp(int(amount))

    for i in range(int(exe_amount)):
        input_string()

    print(lamp)