n, h = list(map(int, input().strip().split()))
heights = list(map(int, input().strip().split()))


def summer(h1, h2, heights, count, own_sum):
    val = heights[count]
    while h1 + val < h:
        own_sum += val
        h1 += val
        count += 1
        val = heights[count]
    if h2 + val < h:
        own_sum += val
        h2 += val
        count, own_sum = summer(h1, h2, heights, count + 1, own_sum)
    return count, own_sum


h1 = 0
h2 = 0
count = 0
flag = True
own_sum = 0
while flag:
    count, own_sum = summer(h1, h2, heights, count, own_sum)
    sort_mas = heights[:count + 1]
    if own_sum + heights[count] > h + h:
        flag = False
    sort_mas.sort()
    end_index = -1
    val = sort_mas[end_index]
    while h1 + val < h:
        h1 += val
        end_index -= 1
        val = sort_mas[end_index]
    start_index = 0
    val = sort_mas[start_index]
    while h1 + val < h:
        h1 += val
        start_index += 1
        val = sort_mas[start_index]
    h2 = sum(sort_mas[start_index:end_index + 1])
    if h2 < h:
        flag = True
        count += 1
    else:
        flag = False
print(count)
