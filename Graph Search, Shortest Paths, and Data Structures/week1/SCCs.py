
from collections import deque

# 讀取圖的函式
def load_Graph(file, mini, maxi):
    lines = file.readlines()
    graph = {}
    for line in lines:
        head, tail = line.split()
        if head not in graph:
            graph[head] = [tail]
        else:
            graph[head] += [tail]

    # 注意某些點可能沒有邊， file 不會有該點當 head 的資訊
    # 因此必須補齊
    for i in range(mini, maxi + 1):
        vert = str(i)
        if vert not in graph:
            graph[vert] = []
    return graph

# 產生反向圖的函式
def graph_Reverse(graph):
    # 初始化圖形
    g = {}
    for vert in graph:
        g[vert] = []

    # 將點、邊的對應反向，丟入 g 中
    for vert, edges in graph.items():
        size = len(edges)
        for i in range(size):
            edge = edges[i]
            g[edge] += [vert]
    return g

# 計算完成時間的函式
def finish_Time(graph):

    # 初始化完成時間以及 visited
    finish_time = {}
    explored = {}
    for vert in graph:
        finish_time[vert] = -1
        explored[vert] = False
    
    # 完成時間
    timer = 1

    # 要注意必須遍歷所有點，且確認某點走到盡頭或所有邊都已探索過，才可以 pop() 掉，否則某些點會 miss
    for vert in graph:
        if explored[vert]:
            continue
        else:
            explored[vert] = True
            stack = deque()
            stack.append(vert)
            while stack:
                # 取出節點
                node = stack[-1]

                # 若沒有向外的邊，代表走到盡頭，將 node 由stack pop()掉，並更新 timer 及 finish_time
                if not graph[node]:
                    stack.pop()
                    finish_time[node] = timer
                    timer += 1
                
                # 若有向外的邊，且該邊尚未探索過，則將邊加入 stack
                else:
                    edges = graph[node]
                    for edge in edges:
                        if not explored[edge]:
                            explored[edge] = True
                            stack.append(edge)

                    # 若所有向外的邊都探索過，代表走到盡頭，且stack也不會更新
                    # 因此可直接將 node 由stack pop()掉，並更新 timer 及 finish_time
                    if node == stack[-1]:
                        stack.pop()
                        finish_time[node] = timer
                        timer += 1
    return finish_time

# 計算 SCC 的函式
def SCCs(graph, time_dict):
    # 初始化 visited
    explored = {}
    for vert in time_dict:
        explored[vert] = False

    SCCs = {}

    # 要注意必須遍歷所有點，且確認某點走到盡頭或所有邊都已探索過，才可以 pop() 掉，否則某些點會 miss 
    # 傳入 time_dict 目的為：確保以 1st 的 finish_time 順序，由大到小遍歷所有點
    for vert in time_dict:
        if explored[vert]:
            continue
        else:
            leader = vert
            SCCs[leader] = []
            explored[leader] = True
            stack = deque()
            stack.append(leader)
            while stack:

                #取出節點
                node = stack[-1]

                # 若沒有向外的邊，代表走到盡頭，將 node 由stack pop()掉，並加入SCCs中
                if not graph[node]:
                    stack.pop()
                    SCCs[leader] += [node]
                
                # 若有向外的邊，且該邊尚未探索過，則將邊加入 stack
                else:
                    edges = graph[node]
                    for edge in edges:
                        if not explored[edge]:
                            explored[edge] = True
                            stack.append(edge)

                    # if last element does not changed means
                    # all child edges have been explored.
                    # 若所有向外的邊都探索過，代表走到盡頭，且stack也不會更新
                    # 因此可直接將 node 由stack pop()掉，並加入SCCs中
                    if node == stack[-1]:
                        stack.pop()
                        SCCs[leader] += [node]
    return SCCs

# 取得圖
file = open("SCC.txt", "r")
mini, maxi = 1, 875714 
graph = load_Graph(file, mini, maxi)

# 求反向圖
g_rev = graph_Reverse(graph)

# 計算反向圖完成時間
finish_time = finish_Time(g_rev)

# 排序反向圖
sorted_finish = dict(sorted(finish_time.items(), key = lambda x: x[1], reverse= True))

# 計算SCC並找出前五大元素個數
SCCs = SCCs(graph, sorted_finish)
sizeof_sccs = []
for scc in SCCs:
    sizeof_sccs.append(len(SCCs[scc]))

sizeof_sccs = sorted(sizeof_sccs, reverse = True)
print(sizeof_sccs[:5])
