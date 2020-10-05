class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.size = 0


class BST:
    def __init__(self):
        self.root = None
        
    def search(self, value):
        return self._search(value, self.root)
    
    def _search(self, value, node):
        if node == None:
            print("Can't find node")
            return None
        
        if node.value == value:
            print("Find Node !")
            return node

        left = node.left
        if left and value < node.value:
            return self._search(value, left)
        elif not left and value < node.value:
            print("Can't find node")
            return None
        
        right = node.right
        if right and value > node.value:
            return self._search(value, right)
        elif not right and value > node.value:
            print("Can't find node")
            return None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            self.update_size()
        else:
            self._insert(value, self.root)
            self.update_size()

    def _insert(self, value, node):
        if value <= node.value:
            left = node.left
            if not left:
                insert_node = Node(value)
                insert_node.parent = node
                node.left = insert_node
            else:
                return self._insert(value, left)

        elif value > node.value:
            right = node.right
            if not right:
                insert_node = Node(value)
                insert_node.parent = node
                node.right = insert_node
            else:
                return self._insert(value, right)    

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)
    
    # In_Order Traversal
    def _print_tree(self, node):

        # 如果 node 存在，先走最左側，當 left child 為 None，
        # 代表找到目前最小值，將其 print 出來，再由該節點往右邊走，
        # 當 right child 為 None，代表小於某個 partent 的值都被印出
        # 因此遞迴最終可以照順序印出所有元素
        if node != None:
            self._print_tree(node.left)
            print("Value of node is {} and size is {}".format(node.value, node.size))
            self._print_tree(node.right)
    
    def height(self):
        if self.root == None:
            return 0
        else:
            return self._height(self.root, 0)
    
    def _height(self, node, h):
        if node == None:
            return h
        
        l_h = self._height(node.left, h + 1)
        r_h = self._height(node.right, h + 1)
        
        return max(l_h, r_h)
    
    def Max(self):
        if self.root == None:
            raise ValueError("No root for the tree")
        else:
            right_child = self.root.right
            while right_child.right != None:
                right_child = right_child.right
            return right_child.value

    def Min(self):
        if self.root == None:
            raise ValueError("No root for the tree")
        else:
            left_child = self.root.left
            while left_child.left != None:
                left_child = left_child.left
            return left_child.value

    def Pred(self, value):
        node = self.search(value)
        if not node:
            print("Can't find the node")
            return None
        else:
            if node.left != None:
                while node.right != None:
                    node = node.right
                return node
            else:
                pointer = node.parent
                while pointer != None:
                    if pointer.value >= node.value:
                        pointer = pointer.parent
                    else:
                        return pointer
                print("Can't find Pred")
                return None

    def Succ(self, value):
        node = self.search(value)
        if not node:
            print("Can't find the node")
            return None
        else:
            if node.right != None:
                right_child = node.right
                while right_child.left != None:
                    right_child = right_child.left
                return right_child
            else:
                pointer = node.parent
                while pointer != None:
                    if pointer.value <= node.value:
                        pointer = pointer.parent
                    else:
                        return pointer
                print("Can't find Succ")
                return None
    
    def delete_Node(self, value):
        node = self.search(value)
        if not node:
            print("Can't find node")
        else:
            return self._delete_Node(node)        

    def _delete_Node(self, node):

        def node_child_nums(node):
            child_nums = 0
            if node.left: child_nums += 1
            if node.right: child_nums += 1
            return child_nums

        child_nums = node_child_nums(node)
        # 注意沒法直接將 node 指向 None，一定要透過 parent 指向 left 或 right 
        # 再將其釋放掉
        if child_nums == 0:
            if node.parent.left == node:
                node.parent.left = None
            if node.parent.right == node:
                node.parent.right = None
            self.update_size()
        
        elif child_nums == 1:
            if node.left:
                node.value = node.left.value
                node.left = None
            if node.right:
                node.value = node.right.value
                node.right = None
            self.update_size()

        else:
            pred = Pred(node.value)
            node.value = pred.value
            return self._delete_Node(pred)

    def update_size(self):
        if self.root == None:
            print("No element in the tree")
        else:
            self._update_size(self.root)
    
    def _update_size(self, node):
        cur_size = 1
        if not node.left and not node.right:
            node.size = cur_size
            return cur_size

        if node.left:
            cur_size += self._update_size(node.left)
        if node.right:
            cur_size += self._update_size(node.right)
        
        node.size = cur_size
        return cur_size

    def select(self, value):
        if self.root == None:
            print("No element in the tree")
            return
        if value > self.root.size:
            print("Input larger than total elements in the tree")
            return
        else:
            return self._select(self.root, value)

    def _select(self, node, value):
        if node.left:
            left_size = node.left.size
        else:
            left_size = 0
        
        if left_size == value - 1:
            return node.value
        
        elif left_size >= value:
            return self._select(node.left, value)
        
        elif left_size < value - 1:
            return self._select(node.right, value - left_size - 1)


def fill_tree(tree, nums_ele = 10, maxInt = 100):
    from random import randint
    for _ in range(nums_ele):
        value = randint(1, maxInt)
        tree.insert(value)
    return tree

if __name__ == "__main__":
    tree = BST()
    tree = fill_tree(tree)
    tree.print_tree()
    print(tree.select(8))
    # tree.insert(20)
    # tree.print_tree()
    # tree.delete_Node(20)
    # tree.print_tree()
    # tree.insert(3)
    # tree.insert(1)
    # tree.insert(2)
    # tree.insert(5)
    # tree.insert(4)
    #tree.print_tree()
