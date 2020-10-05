"""
The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 lecture on heap applications). 
The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. 
Letting x_i denote the ith number of the file, the kkth median m_k is defined as the median of the numbers x_1,…,xk. 
(So, if k is odd, then m_k is ((k+1)/2)th smallest number among x_1,…,x_k; if k is even, then m_k is the (k/2)th smallest number among x_1,…,x_k.)

In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). 
That is, you should compute (m_1+m_2+m_3+⋯+m_10000)mod10000.
"""

import heapq
import time

file = open("Median.txt", 'r')
integers = file.readlines()

# 注意 low_Heap 適用 Extract_Max，所以存入的值必須變成負數

# 取值的概念為：
# 奇數時點 (中位數最終要丟入 high_Heap，此時 low & high_Heap 等長) --> 
# 先將值丟入 low_Heap ，接著取出最大值 (此時不知道比 high_Heap 的最小值大還是小)
# 丟入 high_Heap，再對 high_Heap 取最小值，此值保證為中位數，再將值塞回 high_Heap

# 偶數時點 (中位數最終要丟入 low_ Heap，此時 high_Heap 比 low_Heap 多 1 個 element) -->
# 先將值丟入 high_Heap，取出最小值 (此時不知道比 low_Heap 的最大值大還是小)
# 丟入 low_Heap ，再對 low_Heap 取最小值，此值保證為中位數，再將值塞回 low_Heap
t1 = time.time()
low_Heap = []
high_Heap = []
k = 1 # counter
median = 0
for i in integers:
    num = int(i)

    # 奇數時點
    if k % 2 == 1:
        
        # 將數字取負號
        num *= -1
        # 將數字丟進 low_Heap
        heapq.heappush(low_Heap, num)
        # 取出目前 low_Heap 最大數字
        low_Heap_max = heapq.heappop(low_Heap)
        # 轉回正整數
        low_Heap_max *= -1
        # 丟入 high_Heap
        heapq.heappush(high_Heap, low_Heap_max)
        # 取出中位數
        mid = heapq.heappop(high_Heap)
        # 中位數加總
        median += mid
        # 將數字推回 high_Heap
        heapq.heappush(high_Heap, mid)
    
    # 偶數時點
    else:
        # 將數字丟進 high_Heap
        heapq.heappush(high_Heap, num)
        # 取出目前 high_Heap 最小數字
        high_Heap_min = heapq.heappop(high_Heap)
        # 轉為負數
        high_Heap_min *= -1
        # 丟入 low_Heap
        heapq.heappush(low_Heap, high_Heap_min)
        # 取出中位數
        mid = heapq.heappop(low_Heap)
        # 中位數加總
        median += mid * -1
        # 將數字推回 high_Heap
        heapq.heappush(low_Heap, mid)
    
    k += 1

t2 = time.time() - t1
print(median % 10000)
print(t2)
