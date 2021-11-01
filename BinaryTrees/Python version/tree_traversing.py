import tree_inst
class Node_tree():
    def __init__(self,data):
        self.data = data
        self.node_left = None
        self.node_right = None

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.node_left==None:
                    self.node_left =Node_tree(data)
                else:
                    self.node_left.insert(data)
            elif data>self.data:
                if self.node_right==None:
                    self.node_right = Node_tree(data)
                else:
                    self.node_right.insert(data)
        else:
            self.data= data

    def display_tree(self):
        if self.node_left:
            self.node_left.display_tree()
        print(self.data)
        if self.node_right:
            self.node_right.display_tree()
        print(self.data)

    def pre_ord(self, node):
        ctx_data = []
        if node :
            ctx_data.append(node.data)
            ctx_data = ctx_data + self.pre_ord(node.node_left)
            ctx_data = ctx_data + self.pre_ord(node.node_right)
        return ctx_data
root = Node_tree(65)
root.insert(6)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.pre_ord(root))