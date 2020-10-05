import math
import copy

def distance(c1, c2):
    x1, x2 = c1[0], c2[0]
    y1, y2 = c1[1], c2[1]
    return (x1-x2)**2 + (y1-y2)**2

with open("nn.txt", 'r') as file:
    n_c = int(file.readline())
    coords = {}
    
    c = 1
    line = file.readline()
    while line:
        _, x, y = line.split()
        coords[c] = (float(x), float(y))
        line = file.readline()
        c += 1

coords_copy = copy.deepcopy(coords)

# 建立城市 set
cities = set((i for i in range(1, n_c+1)))
# 建立遍歷 set
visit = set()
# 第一個城市的座標點
c1 = coords[1]
# 第一個城市加入遍歷 set
visit.add(1)
# 初始化總距離
res = 0
# 將第一個城市從字典中刪除
del coords[1]

last_c = 1
# 遍歷所有城市
while visit != cities:
    # 初始化最短距離
    d_m = float('inf')
    # 初始化最近城市
    close = 1
    # 遍歷尚未走過的城市
    for c, c2 in coords.items():
        # 計算城市 i 與其他城市的距離
        d12 = distance(c1, c2)
        # 若兩城市距離小於目前最短距離，更新資訊
        if d12 < d_m:
            close = c
            d_m = d12
        elif d12 == d_m:
            continue
    
    # 將最小距離加至結果
    res += math.sqrt(d_m)
    # 更新下一個新座標點
    c1 = coords[close]
    # 紀錄目前最新城市
    last_c = close
    # 將最新城市加入遍歷，並從字典中刪除
    visit.add(close)
    del coords[close]

dl1 = math.sqrt(distance(coords_copy[1], coords_copy[last_c]))
res += dl1
print(res)
