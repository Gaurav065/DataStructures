import tree_inst as ti
class Node_tree:
    def __init__(self,data):
        self.data = data
        self.node_left = None
        self.node_right = None

    def pre_ord(self, node):
        
