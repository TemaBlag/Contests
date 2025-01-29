def upper_bound(arr, target):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low

n, m = list(map(int, input().split()))
x, y = list(map(int, input().split()))
k = int(input())
nums_a = []
nums_a_x = []
for i in input().split():
    num = int(i)
    nums_a.append(num)
    nums_a_x.append(num + x)
nums_b = []
nums_b_y = []
for i in input().split():
    num = int(i)
    nums_b.append(num)
    nums_b_y.append(num + y)
dp = [0] * k
i, p = 0, 0
if k >= m or k >= n:
    print(-1)
else:
    for l in range(k):
        index_i = upper_bound(nums_b[p:], nums_a_x[i+1]) + p
        index_p = upper_bound(nums_b[p+1:], nums_a_x[i]) + 1 + p
        if index_p >= index_i:
            p = index_p
        else:
            p = index_i
            i += 1
        if p >= m:
            print(-1)
            break
        time = nums_b_y[p]
        dp[l] = nums_b_y[p]
    print(dp[k-1])


