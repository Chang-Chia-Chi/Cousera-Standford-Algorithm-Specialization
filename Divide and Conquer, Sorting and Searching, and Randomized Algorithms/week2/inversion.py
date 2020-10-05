def count_inv(nums, start, end):
    # 中止條件，若 start = end，表示拆到剩下一個元素
    if start == end:
        return 0

    mid = (start + end)//2
    # 分治法，將問題拆半再組合
    c1 = count_inv(nums, start, mid)
    c2 = count_inv(nums, mid+1, end)
    c3 = merge_inv(nums, start, end)
    return c1+c2+c3

def merge_inv(nums, start, end):
    mid = (start + end)//2

    # 左半邊及右半邊的陣列
    left = nums[start:mid+1]
    right = nums[mid+1:end+1]
    l_size, r_size = len(left), len(right)

    # 初始化左半、右半及合併陣列的 pointer
    id_l, id_r, id_m = 0, 0, start

    # 初始化 inversion 的計算數
    count = 0

    # 合併排序演算法
    while id_l < l_size and id_r < r_size:
        # 若左半邊元素小於右半邊，則取出左半邊元素
        # 若右半邊元素小於左半邊，則取出右半邊元素並計算 inversion
        if left[id_l] <= right[id_r]:
            nums[id_m] = left[id_l]
            id_l += 1       
        else:
            nums[id_m] = right[id_r]
            id_r += 1
            count += l_size-id_l
        id_m += 1
    
    # 若右半邊陣列先取完，將左半邊陣列剩下的元素合併
    if id_l < l_size:
        nums[id_m:end+1] = left[id_l:mid+1]

    # 若左半邊陣列先取完，將右半邊陣列剩下的元素合併
    if id_r < r_size:
        nums[id_m:end+1] = right[id_r:end+1]

    return count
    
with open("IntegerArray.txt", 'r') as file:
    nums = []
    lines = file.readlines()
    for line in lines:
        nums.append(int(line))

end = len(nums)-1
inversion = count_inv(nums, 0, end)
print(inversion)