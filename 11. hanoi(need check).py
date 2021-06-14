def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))


def hanoi(num_disks, start_peg, end_peg):
    # base case : 옮길 원판이 없으면 함수를 끝냄
    if num_disks == 0:
        return
    else:
        # 1, 2, 3번 막대기를 합한 값은 언제나 6이다?
        middle_peg = 6 - start_peg - end_peg

        # 가장 큰 원판을 제외하고 나머지를 start_peg에서 middle_peg으로 옮김
        hanoi(num_disks - 1, start_peg, middle_peg)
        # 가장 큰 원판을 start_peg에서 end_peg으로 옮김
        move_disk(num_disks, start_peg, end_peg)
        # 나머지 원판들을 middle_peg에서 end_peg으로 옮김
        hanoi(num_disks - 1, middle_peg, end_peg)
    # 코드를 입력하세요.


# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)