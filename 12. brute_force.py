def max_product(left_cards, right_cards):
    max = 0
    for i in range(len(left_cards)):
        for j in range(len(right_cards)):
            if left_cards[i] * right_cards[j] > max:
                max = left_cards[i] * right_cards[j]
            else:
                continue
    return max
    # 코드를 작성하세요.


# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))
print(max_product([-3, -2, 1, 4, -6], [2, 4, -1, -4]))