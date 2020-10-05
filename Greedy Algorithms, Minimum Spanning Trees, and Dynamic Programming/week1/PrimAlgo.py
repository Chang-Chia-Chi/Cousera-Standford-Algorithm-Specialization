import Heap
import random

inf = float('inf')

# 建立 Adajacency List
with open("edges.txt", 'r') as file:
    lines = file.readlines()
    edge_dict = {}
    for line in lines[1:]:
        node, edge, weight = line.split()
        weight = int(weight)
        if node not in edge_dict:
            edge_dict[node] = [(edge, weight)]
        else:
            edge_dict[node].append((edge, weight))
        
        if edge not in edge_dict:
            edge_dict[edge] = [(node, weight)]
        else:
            edge_dict[edge].append((node, weight))

# 所有邊的 key value 先設為無窮大
min_heap = Heap.MinHeap()
for edge in edge_dict.keys():
    min_heap.Insert((edge, inf))

# 隨機取出一個 key 值
rand_key = random.choice(list(edge_dict.keys()))
visit = {rand_key:1}
MST_edges = []
# 對第一個取出點相對應的邊，更新 key value
for edge in list(edge_dict[rand_key]):
    min_heap.Delete(edge[0])
    min_heap.Insert(edge)


# Prim 演算法主迴圈
while visit.keys() != edge_dict.keys():
    # 取出當前最小邊
    min_edge = min_heap.Extract_Min()
    # 將邊加入 MST 邊集合
    MST_edges.append(min_edge)
    # 設該節點已搜尋過
    visit[min_edge[0]] = 1
    # 更新 heap
    for edge in edge_dict[min_edge[0]]:
        # 判斷邊是否已遍歷過
        if edge[0] not in visit.keys():
            # 沒遍歷過則先把點從 heap 刪除
            del_edge = min_heap.Delete(edge[0])
            # 更新 heap
            if edge[1] < del_edge[1]:
                min_heap.Insert(edge)
            else:
                min_heap.Insert(del_edge)

total_weight = 0
cost = []
for mst_edge, mst_weight in MST_edges:
    total_weight += mst_weight

print(total_weight)


            
    


    

