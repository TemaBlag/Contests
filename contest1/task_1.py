n, m = int(input()), int(input())
k = n
m = m % ((n * (n + 1)) // 2)
while m >= k:
    m -= k
    if k > 1:
        k -= 1
    else:
        k = n
print(m)