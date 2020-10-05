# using median element as pivot
def QuickSort3(arr, start, end):

    mid = (start + end) // 2
    p_can = [[arr[start], start], [arr[mid], mid], [arr[end], end]]
    p_can = sorted(p_can, key = lambda x: x[0])

    p_i = p_can[1][1]

    arr[start], arr[p_i] = arr[p_i], arr[start]
    pivot = arr[start]
    i = start + 1
    for j in range(start + 1, end + 1):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[start], arr[i - 1] = arr[i - 1], arr[start]

    count = end - start
    if end > i:
        count_l = QuickSort1(arr, i, end)
        count += count_l
    if i - 2 > start:
        count_r = QuickSort1(arr, start, i-2)
        count += count_r

    return count
    

# read txt file and convert to int type
file = open("QuickSort.txt", "r")
nums = [0] * 10000
index = 0
for line in file:
    nums[index] = int(line.rstrip())
    index += 1
file.close()

#QuickSort
start = 0
end = len(nums) - 1
count = QuickSort3(nums, start, end)

print(count)

