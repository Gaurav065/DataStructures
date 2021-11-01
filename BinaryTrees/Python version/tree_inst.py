


import tree_root as tr
class Node_tree:
    def __init__(self,data):
        self.data = data
        self.node_left = None
        self.node_right = None

    def insert(self,data):
        if self.data==True:
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
        if self.node_left==True:
            self.node_left.display_tree()
        print(self.data)
        if self.node_right==True:
            self.node_right.display_tree()
        print(self.data)
