def Bsearch(nums: list, start: int, end: int, search_value: int) -> int:
    if start >= end:
        return start
    

    mid = int((start + end) / 2)
    if nums[mid] == search_value:
        return mid
    elif nums[mid] < search_value:
        return Bsearch(nums, mid + 1, end, search_value)
    else:
        return Bsearch(nums, start, mid - 1, search_value)

import time

file = open("2sum.txt", 'r')
lines = file.readlines()

# 因有重複資料，先以 set 儲存
nums = set()
for line in lines:
    nums.add(int(line))

# 將數字集合轉為串列
nums = sorted(list(nums))
size = len(nums)

# 建立總和是否出現過的字典
check_dict = dict([(i, 0) for i in range(-10000,10001)])

t1 = time.time()
for num in nums:

    # 計算某數字相對應另一數字的上下限
    low_bound = -10000 - num
    high_bound = 10000 - num

    # 以二元搜尋找出對應數字 index 的上下限
    low_index = Bsearch(nums, 0, size - 1, low_bound)
    high_index = Bsearch(nums, low_index, size - 1, high_bound)

    # 在對應 index 範圍，計算某個總和是否出現過
    for i in range(low_index, high_index + 1):

        # 找上限時有可能超過一個 index，所以要確認兩數相加是否在範圍內
        if nums[i] + num >= -10000 and nums[i] + num <= 10000: 
            if check_dict[num + nums[i]] == 0 and num != nums[i]:
                check_dict[num + nums[i]] = 1

# 計算不同總和出現的次數
count = 0
for key, value in check_dict.items():
    count += value

t2 = time.time() - t1
print(count)
print(t2)

