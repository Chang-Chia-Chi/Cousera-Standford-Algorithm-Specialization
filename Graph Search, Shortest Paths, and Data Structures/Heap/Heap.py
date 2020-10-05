class MinHeap:
    def __init__(self, array = []):
        self.heap = list([None])
        self.length = 0
        if len(array) > 0:
            for item in array:
                self.Insert(item)

    def Insert(self, node):
        if not isinstance(edge, tuple):
            raise TypeError("""Input should be a tuple 
                            in format (node, length).""")
        self.heap.append(node)
        self.length += 1
        self.bubble_up(self.length)
    
    def Extract_Min(self):
        # 將根節點與最後一個葉節點交換
        self.heap[1], self.heap[self.length] = self.heap[self.length], self.heap[1]
        # 將最小值取出
        heap_min = self.heap.pop()
        # Heap 長度減 1
        self.length -= 1
        # 由根節點執行 Bubble-down
        self.bubble_down(1)
        return heap_min
    
    def Delete(self, node): 
        # 尋找節點，並將該節點與最後一個葉節點交換
        for i in range(1, self.length + 1):
            if self.heap[i][0] == node:
                self.heap[i], self.heap[self.length] = self.heap[self.length], self.heap[i]
                # 將 node pop 掉
                del_node = self.heap.pop()
                # Heap 長度減 1
                self.length -= 1
                # 執行 Bubble-down
                self.bubble_down(i)
                return del_node
        else:
            print("Node not found.")


    def bubble_up(self, idx):
        parent = idx // 2
        current = idx
        # 當尚未到根節點時，繼續迴圈
        while parent >= 1:
            # 若子節點的值小於父節點，則交換
            if self.heap[parent][1] > self.heap[current][1]:
                self.heap[parent], self.heap[current] = self.heap[current], self.heap[parent]
                current = parent
                parent = current // 2
            # 反之則結束迴圈
            else:
                break

    def bubble_down(self, idx):
        current = idx
        # 當目前節點的索引值 <= 可能的最大父節點索引值，代表還有子節點，繼續迴圈
        while current <= self.length // 2:
            # 左子節點索引值
            pos = current * 2
            # 若左子節點索引值小於 heap 長度，代表目前的節點，有左跟右子節點
            if pos < self.length:
                # 若父節點的值小於左或右子節點，結束迴圈
                if self.heap[current][1] <= self.heap[pos][1] and self.heap[current][1] <= self.heap[pos+1][1]:
                    break
                else:
                # 反之則與子節點中值較小的交換
                    if self.heap[pos][1] < self.heap[pos+1][1]:
                        self.heap[current], self.heap[pos] = self.heap[pos], self.heap[current]
                        current = pos
                    else:
                        self.heap[current], self.heap[pos+1] = self.heap[pos+1], self.heap[current]                      
                        current = pos+1
            # 若左子節點的索引值，等於 heap 長度，代表目前的節點，只有左子節點。
            else:
                # 若父節點的值小於左子節點，結束迴圈
                if self.heap[current][1] <= self.heap[pos][1]:
                    break
                # 反之則與子節點交換
                else:
                    self.heap[current], self.heap[pos] = self.heap[pos], self.heap[current]
                    current = pos                
   

    def __len__(self):
        return len(self.heap[1:])