q = int(input())
result = []
while q:
    number = 1
    values = input().split()
    for i in range(int(values[0]), int(values[1]) + 1):
        number *= i
        while number % 10 == 0 and number / 10 != 0:
            number = number // 10
    if number <= 9:
        result.append(number)
    strNum = str(number)
    lenStrNum = len(strNum)
    while lenStrNum != 1:
        sumVal = 0
        for i in range(lenStrNum):
            sumVal += int(strNum[i])
        strNum = str(sumVal)
        lenStrNum = len(strNum)
    result.append(int(strNum[0]))
    q -= 1

for k in range(len(result)):
    print(result[k])

"""
def digit_sum(x):
    if x < 10:
        return x
    return digit_sum(sum(int(digit) for digit in str(x)))

def product_digit_sum(l, r):
    digit_sums = [ digit_sum(x) for x in range(l, r+1)]
    product = 1
    for digit_sum in digit_sums:
        product *= digit_sum
    while product >= 10:
        product = digit_sum(product)
    return product


q = int(input())
result = []
while q:
    values = input().split()
    result.append(product_digit_sum(values[0], values[1]))
for k in range(len(result)):
    print(result[k])
"""
