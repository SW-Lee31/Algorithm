def factorial(num):
    if num == 0:
        return 1
    return factorial(num - 1) * num

def fact(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result

print(factorial(6))
print(fact(6))