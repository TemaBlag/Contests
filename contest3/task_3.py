n = int(input())
numbers = list(map(int, input().split()))
count_ones = 1
index_one = 0
count_pull_ups = []
for i in range(1, len(numbers)):
    if numbers[i] == 1:
        count_ones += 1
        count_pull_ups.append(i - index_one)
        index_one = i
count_pull_ups.append(len(numbers) - index_one)
print(count_ones)
print(*count_pull_ups)