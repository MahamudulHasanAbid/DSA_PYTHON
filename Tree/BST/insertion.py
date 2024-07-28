class BinarySearchTreeNode:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # BST can not contain duplicate element or data. here self.data means there is data stored before.
        if data == self.data:
            return
        
        if data <self.data:
            # add data/element in left susbtree
            if self.left:                   #self.left means there is data in left node and is another subtree have add_child value.
                self.left.add_child(data)   #recursively called. Why: This allows the method to continue the insertion process in the left subtree, finding the correct position recursively. 
            else:                           #if my left node is empty then
                self.left = BinarySearchTreeNode(data)  
        else: 
            # add data/element in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
        
    def inorder_traversal(self):
        # goal is to return the list of elements in LNR
        elements=[]

        # visit left subtree
        if self.left:
            elements += self.left.inorder_traversal()

        # visit base node
        elements.append(self.data)

        # visit right subtree   
        if self.right:
            elements += self.right.inorder_traversal()
 
        return elements  
    
    def search(self, value):
        if self.data == value:
            return True
        
        if value < self.data :
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value > self.data: 
            if self.right:
                return self.right.search(value)
            else:
                return False

    def total_sum(self):
        total = self.data

        if self.left:
            total += self.left.total_sum()
        if self.right:
            total += self.right.total_sum()

        return total
          
    def max_value(self):
        if self.right is None:
            return self.data
        return self.right.max_value()
    def min_value(self):
        if self.left is None:
            return self.data
        return self.left.min_value()

    def delete(self, value):
        if value<self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value>self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # If the node or element is leaf/terminal node
            if self.left is None and self.right is None:
                return None
            # If the node or element has right child
            if self.left is None:
                return self.right
            # If the node or element has left child
            if self.right is None:
                return self.left
            
            # If the node or element has both child there are two ways.
            
            # 1st one:
            # min_value = self.right.min_value()
            # self.data = min_value
            # self.right = self.right.delete(min_value)

            # 2nd one:
            max_value = self.left.max_value()
            self.data = max_value
            self.left = self.left.delete(max_value)

        return self     #correctly updates its parent node’s reference while recursion


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 20, 9, 23, 18, 34]

    num_tree = build_tree(numbers)

    print(num_tree.inorder_traversal())
    print(num_tree.total_sum())
    print(num_tree.search(23))
    num_tree.delete(9)
    print(f"After deleting 9: {num_tree.inorder_traversal()}")
    num_tree.delete(23)
    print(f"After deleting 23: {num_tree.inorder_traversal()}")

    num_tree.delete(20)
    print(f"After deleting 20: {num_tree.inorder_traversal()}")