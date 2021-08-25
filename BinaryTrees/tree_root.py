class Node_tree:
    def __init__(self,data):
        self.data= data
        self.node_left= None
        self.node_right = None

    def display_root(self):
        print(self.data)
