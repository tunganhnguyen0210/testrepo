class TreeNode:
    def __init__(self, e):
        self.element = e
        self.parent = None
        self.children = []
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def preorder(self):
        print(self.element)
        for child in self.children:
            child.preorder()
    def postorder(self):
        for child in self.children:
            child.postorder()
        print(self.element)

    def get_node(self, ele):
        if self.element == ele:
            return self
        elif self.children: #Check if empty(is not None)
            for child in self.children:
                a = child.get_node(ele)
                if a:       #Check if empty(is not None)
                    return a
        return None


  
        
        
def build_tree():
    root = TreeNode('Electronics')
    
    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Macbook'))
    laptop.add_child(TreeNode('Dell'))
    laptop.add_child(TreeNode('Asus'))
    
    cellphone = TreeNode('Cellphone')
    cellphone.add_child(TreeNode('Iphone'))
    cellphone.add_child(TreeNode('Bphone'))
    cellphone.add_child(TreeNode('Xiaomi'))
    
    tv = TreeNode('TV')
    tv.add_child(TreeNode('Bravia'))
    tv.add_child(TreeNode('LG'))
    
    
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    
    
    return root
if __name__ == '__main__':
    E = build_tree()
    '''node = E.get_node('Iphone')
    node.add_child(TreeNode('3GS'))
    node.add_child(TreeNode('12'))
    E.preorder()'''

    node_lap = E.get_node('Laptop')
    node_lap.preorder()
    