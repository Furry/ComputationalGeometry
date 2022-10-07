class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    #END
#END

class BalancedSearchTree:
    def __init__(self):
        self.root = None
    #END

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
        #END
    #END

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
            #END
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)
            #END
        #END
    #END

    def __repr__(self):
        return str(self.root)
    #END

    # Depth first leaf left to right traversal
    def traverse(self):
        if self.root is not None:
            return self._traverse(self.root)
        #END
    #END
    def _traverse(self, node):
        leaves = []
        if node.left is None and node.right is None:
            leaves.append(node.data)
        #END

        if node.left is not None:
            leaves.extend(self._traverse(node.left)) 
        #END

        if node.right is not None:
            leaves.extend(self._traverse(node.right))
        #END

        return leaves
    #END
#END