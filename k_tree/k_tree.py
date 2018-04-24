class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.right = None
        self.left = None
    
    def __repr__(self):
        """This is used in tests. This is for the dev"""
        pass
        
    def __str__(self):
        """This is for the user"""
        pass

class KTree:

    def __init__(self, iter=[]):
        self.root = None
        self.size = 0
        for item in iter:
            self.insert(item)

    def __repr__(self):
        return '<BST Root {}>'.format(self.root.val)

    
    def __str__(self):
        return self.root.val

    def __len__(self):
        return self.size

    def pre_order(self, operation):

        def _walk(node=Node):
            if node is None:
                return
            
            operation(node)

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)


    def post_order(self, operation):

        def _walk(node=Node):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)

            operation(node)


    def insert(self, val):
        node = Node(val)
        current = self.root
        self.size += 1
        if self.root is None:
            self.root = node
            return node

        while current:
            if val >= current.val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = node
                    break

            elif val < current.val:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = node
                    break
        return node