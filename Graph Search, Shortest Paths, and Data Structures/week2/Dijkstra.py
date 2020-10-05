import heapq
import time

# 定義無窮大
inf = float('Inf')

# 距離初始化
def initial(graph, source):
    distance = {}
    parent = {}
    for vertex in graph:
        distance[vertex] = inf
        parent[vertex] = None

    distance[source] = 0
    return distance, parent

def Relax(node, vertex):
    # 若計算的距離比原先的更小，則更新權重
    if distance[vertex] > distance[node] + graph[node][vertex]:
        distance[vertex] = distance[node] + graph[node][vertex]
        parent[vertex] = node
        
        # heappush vertex into heap if updated
        heapq.heappush(heap, (distance[vertex], vertex))   


def Dijkstra(graph, source):

    # 初始化
    global distance, parent
    distance, parent = initial(graph, source)

    # 紀錄探索過的節點
    processed = set()

    # 建立 Heap
    global heap
    heap = []
    heapq.heappush(heap, (distance[source], source))

    while heap:

        # 取出 crossing edges 的最小值
        node = heapq.heappop(heap)[1]
        # 將節點設為已探索
        processed.add(node)
        # 若沒有向外的邊，則繼續迴圈
        if not graph[node]:
            continue

        # 若存在向外的邊，則遍歷所有邊
        for vertex in graph[node]:
            if vertex not in processed:
                Relax(node, vertex)
        
    return distance, parent


file = open("dijkstraData.txt", 'r')
lines = file.readlines()
graph = {}
for line in lines:
    edges = line.split()
    vertex = edges.pop(0)
    graph[vertex] = {}
    for edge in edges:
        edge, length = edge.split(',')
        graph[vertex][edge] = int(length)

for i in range(1, 201):
    vertex = str(i)
    if vertex not in graph:
        graph[vertex] = []

t1 = time.time()
distance, parent = Dijkstra(graph, '1')
t2 = time.time() - t1
print(distance['7'], distance['37'], distance['59'], distance['82'], distance['99'], 
distance['115'], distance['133'], distance['165'], distance['188'], distance['197'])
print(t2)
