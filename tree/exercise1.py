class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, node):
        node.parent = self
        self.children.append(node)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self, level):
        space = ' ' * self.get_level() * 3
        prifix = space + '|__ '
        if level+1 > self.get_level():
            if self.get_level() == 0:
                print(self.data)
            else:
                print(prifix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

def build_location_tree():
    node = TreeNode('Global')

    india = TreeNode('India')
    usa = TreeNode('USA')

    gujarat = TreeNode('Gujarat')
    gujarat.add_child(TreeNode('Ahmedabad'))
    gujarat.add_child(TreeNode('Baroda'))

    karnataka = TreeNode('Karnataka')
    karnataka.add_child(TreeNode('Bangalore'))
    karnataka.add_child(TreeNode('Mysore'))

    new_jersey = TreeNode('New Jersey')
    new_jersey.add_child(TreeNode('Princeton'))
    new_jersey.add_child(TreeNode('Trenton'))

    california = TreeNode('San Francisco')
    california.add_child(TreeNode('Mountain View'))
    california.add_child(TreeNode('Palo Alto'))


    india.add_child(gujarat)
    india.add_child(karnataka)

    usa.add_child(new_jersey)
    usa.add_child(california)
    
    node.add_child(india)
    node.add_child(usa)

    return node

root_node = build_location_tree()
root_node.print_tree(0)
print('< ------------------------------ >')
root_node.print_tree(1)
print('< ------------------------------ >')
root_node.print_tree(2)
print('< ------------------------------ >')
root_node.print_tree(3)
print('< ------------------------------ >')