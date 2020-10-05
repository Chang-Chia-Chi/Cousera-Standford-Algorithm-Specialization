from heapq import heappop, heappush

# 節點的 class, idx 代表元素的編號，
# self.left & self.right 代表左邊與右邊的子節點
class Node:
    def __init__(self, idx=None):
        self.idx = idx
        self.left = None
        self.right = None

# 利用 DFS 計算元素代表的 Huffman code
def DFS(node: Node, code: str, H_C: dict):
    if (not node.left) and (not node.right):
        H_C[node.idx] = code
        return
    
    if node.left:
        l_code = code + '0'
        DFS(node.left, l_code, H_C)
    if node.right:
        r_code = code + '1'
        DFS(node.right, r_code, H_C)

idx = 1
W = []
with open("huffman.txt", 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:
        w = int(line)
        n = Node(idx)
        # 將子樹的權重、包含的元素以及子樹丟入 Heap 中
        heappush(W, (w, [idx], n))
        idx += 1

# Huffman Code 合併迴圈，執行直到剩下一個樹結束
while len(W) > 1:
    # 將前兩個最小權重的子樹取出
    t1 = heappop(W)
    t2 = heappop(W)
    # 創建子樹的父節點
    p = Node()
    p.left, p.right = t1[2], t2[2]
    # 將兩個子樹合併為一個子樹，並重新插入 Heap
    n_w = t1[0] + t2[0]
    idx = t1[1] + t2[1]
    heappush(W, (n_w, idx, p))

# 利用 DFS 計算元素代表的 Huffman code
H_C = {}
root = W[0][2]
code = str()
DFS(root, code, H_C)

# 找出最大及最小的 Huffman Code 長度
max_l = 0
min_l = float('inf')
for node, code in H_C.items():
    c_l = len(code)
    if c_l > max_l:
        max_l = c_l
    if c_l < min_l:
        min_l = c_l

print(max_l, min_l)

