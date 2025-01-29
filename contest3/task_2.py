n = int(input())
energy = [0] + list(map(int, input().split()))
m = int(input())
nums = [0] * (n + 1)
for i in range(m):
    friend1, friend2 = list(map(int, input().split()))
    if energy[friend1] > energy[friend2]:
        energy[friend1] = energy[friend2]
        nums[friend1] = 1
    else:
        energy[friend2] = energy[friend1]
        nums[friend2] = 1
sum_energy = 0
for i in range(1, n + 1):
    if nums[i] == 0:
        sum_energy += energy[i]
print(sum_energy)
