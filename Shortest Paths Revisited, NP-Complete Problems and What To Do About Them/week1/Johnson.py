import os
import copy
from multiprocessing import Pool
from collections import defaultdict
from heapq import heappop, heappush

def inf():
    return float('inf')

# 增加額外 s node 
def add_node(graph: dict, tail_list: dict):
    num_nodes = len(graph)
    add_node = str(num_nodes + 1)
    graph[add_node] = {}
    for node in graph.keys():
        if node == add_node:
            continue
        else:
            graph[add_node][node] = 0
            tail_list[node].append(add_node)

def Bellman(graph: dict, tail_list: dict, start: str):
    # 初始化 A[i, v]
    curr_len = defaultdict(inf)
    for node in graph.keys():
        curr_len[node]
    curr_len[start] = 0

    # Bellman-Ford
    for _ in range(len(graph)):
        # A[i-1, v]
        pre_len = copy.deepcopy(curr_len)
        for node in curr_len.keys():
            curr_min = pre_len[node]
            tails = tail_list[node]
            for tail in tails:
                if pre_len[tail] + graph[tail][node] < curr_min:
                    curr_min = pre_len[tail] + graph[tail][node]
            curr_len[node] = curr_min

    # 確認是否有 negative cycle
    diff_sum = 0
    for node in curr_len.keys():
        diff_sum += curr_len[node]-pre_len[node]

    if diff_sum != 0:
        return None
    else:
        return curr_len

def Dijkstra(graph: dict, start: str):
    num_nodes = len(graph)
    # initialization
    distance = defaultdict(dict)
    for node in graph.keys():
        distance[node] = float('inf')
    distance[start] = 0
    visited = set()
    heap = [(0, start)]

    while heap and len(visited) < num_nodes:
        _, node = heappop(heap)
        if node in visited:
            continue

        visited.add(node)
        for edge in graph[node]:
            if distance[edge] > distance[node] + graph[node][edge]:
                distance[edge] = distance[node] + graph[node][edge]
                heappush(heap, (distance[edge], edge))

    return distance


def Johnson(graph: dict, tail_list: dict):
    # step 1. -- 建立 G' 並建立額外點 s 連到所有 vertex
    add_node(graph, tail_list)
    extra_node = str(len(graph))
    # step 2. -- run Bellman-Ford
    add_weight = Bellman(graph, tail_list, extra_node)
    if add_weight is None:
        print("Negative Cycle Detected.")
        return None
    
    del graph[extra_node], tail_list[extra_node], add_weight[extra_node]

    # step 3. -- Ce' = Ce + Pu - Pv
    for tail, heads in graph.items():
        for head in heads:
            graph[tail][head] = graph[tail][head] + add_weight[tail] - add_weight[head]

    # step 4. Dijkstra
    num_nodes = len(graph)
    res = defaultdict(dict)
    for tail in range(num_nodes):
        for head in range(num_nodes):
            res[tail][head] = float('inf')

    # 多進程
    pool = Pool(5)
    nodes = [(graph, str(i)) for i in range(1, num_nodes+1)]
    # 每次以不同起點執行 Dijkstra
    res = pool.starmap(Dijkstra, nodes)
    # 將各節點結果存入字典
    res = {str(i+1) : res[i] for i in range(num_nodes)}

    # step 5. fix distance
    for tail, heads in res.items():
        for head in heads:
            res[tail][head] = res[tail][head] - add_weight[str(tail)] + add_weight[str(head)]
    
    return res

root = "/graphs"
paths = []
for file in os.listdir(root):
    paths.append(os.path.join(root, file))
paths = sorted(paths)

adj_list = defaultdict(dict)
tail_list = defaultdict(list)
max_key = 0
with open(paths[3]) as file:
    lines = file.readlines()
    for line in lines[1:]:
        tail, head, weight = line.split()
        weight = int(weight)

        adj_list[tail][head] = weight
        tail_list[head].append(tail)
        if max_key < int(tail) or max_key < int(head):
            max_key = max(int(tail), int(head))

# 補齊沒有向外邊的點
for i in range(1, int(max_key) + 1):
    if str(i) not in adj_list:
        adj_list[str(i)] = {}
    if str(i) not in tail_list:
        tail_list[str(i)] = []

distance = Johnson(adj_list, tail_list)
min_distance = float('inf')
for tail, heads in distance.items():
    for head in heads:
        if min_distance > distance[tail][head]:
            min_distance = distance[tail][head]

print(min_distance)
