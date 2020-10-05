import os
import time
import random
from collections import deque
from collections import defaultdict

def reverse_G(graph):
    G_rev = defaultdict(list)
    for tail, heads in graph.items():
        for head in heads:
            G_rev[head].append(tail)
            if tail not in G_rev:
                G_rev[tail]
    return G_rev

def create_G(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        G = defaultdict(list)
        for line in lines[1:]:
            x, y = line.split()
            x, y = int(x), int(y)
            ix, iy = -x, -y
            if y not in G[ix]:
                G[ix].append(y)
                if y not in G:
                    G[y]
            if x not in G[iy]:
                G[iy].append(x)
                if x not in G:
                    G[x]
    return G

def topo_Sort(graph):
    # order of vertices be explored
    t_v = 0
    T_V = {}
    # Visited
    V = set()
    for start in graph.keys():
        if start in V:
            continue
        # add start point to V
        V.add(start)
        # initialize stack for DFS
        stack = deque()
        stack.append(start)
        while stack:
            # select last node in stack 
            # (not pop because you're not sure whether it has unvisited outgoing edge)
            node = stack[-1]
            heads = graph[node]
            # if no head or all heads have been explored means reaching the end
            # record and update T_V and t_v
            if not heads:
                t_v += 1
                T_V[node] = t_v
                stack.pop()
            else:    
                for head in heads:
                    if head not in V:
                        # if head not visited, add to visited
                        V.add(head)
                        # put the vertex to stack
                        stack.append(head)
                        
                # if last element does not changed means
                # all child edges have been explored.
                # 若所有向外的邊都探索過，代表走到盡頭，且stack也不會更新
                # 因此可直接將 node 由stack pop()掉，並更新 timer 及 finish_time
                if node == stack[-1]:
                    t_v += 1
                    T_V[node] = t_v
                    stack.pop()
    return T_V

def find_SCCs(graph, topo_Order):
    # Visited
    V = set()
    # SCCs
    SCCs = defaultdict(list)
    for ver in topo_Order:
        if ver in V:
            continue
        # add start point to V
        V.add(ver)
        # initialize stack for DFS
        stack = deque()
        stack.append(ver)
        while stack:
            # select last node in stack 
            # (not pop because you're not sure whether it has unvisited outgoing edge)
            node = stack[-1]
            heads = graph[node]
            # if no head means reaching the end
            # update SCCs
            if not heads:
                SCCs[ver].append(node)
                stack.pop()
            else:    
                for head in heads:
                    if head not in V:
                        # if head not visited, add to visited
                        V.add(head)
                        # put the vertex to stack
                        stack.append(head)
                # if last element does not changed means
                # all child edges have been explored.
                if node == stack[-1]:
                    SCCs[ver].append(node)
                    stack.pop()
    return SCCs

def check_SAT(SCCs):
    # find any pair that sum equals to 0
    t = 0
    for leader, heads in SCCs.items():
        check = set()
        check.add(-int(leader))
        for head in heads:
            if int(head) not in check:
                check.add(-int(head))
            else:
                print("Not Satisfied")
                return 0
    print("Satisfied")
    return 1

t1 = time.time()
root = "/sat"
files = sorted(os.listdir(root))
check = []
for f in files:
    path = os.path.join(root, f)
    # create graph
    G = create_G(path)
    # create reverse graph
    G_rev = reverse_G(G)
    # topology order of reverse graph
    topo_Grev = topo_Sort(G_rev)
    # rearrange topology in decresing order
    topo_Grev = {v:t for v, t in sorted(topo_Grev.items(), key=lambda x: x[1], reverse=True)}
    # SCCs
    SCCs = find_SCCs(G, topo_Grev)
    check.append(check_SAT(SCCs))

t2 = time.time() - t1
print(check, t2)




