class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def  add_child(self, node):
        node.parent = self
        self.children.append(node)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        space = ' ' * self.get_level() * 3
        prifix = space + '|__ '
        print(prifix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_tree():
    node = TreeNode('Electronics')

    tv = TreeNode('TV')
    tv.add_child(TreeNode('LG'))
    tv.add_child(TreeNode('Samsung'))


    laptops = TreeNode('Laptops')
    laptops.add_child(TreeNode('Dell'))
    laptops.add_child(TreeNode('HP'))
    laptops.add_child(TreeNode('Mac'))

    mobiles = TreeNode('Mobiles')
    mobiles.add_child(TreeNode('Iphone'))
    mobiles.add_child(TreeNode('Galaxy'))
    mobiles.add_child(TreeNode('One plus'))

    node.add_child(tv)
    node.add_child(laptops)
    node.add_child(mobiles)

    return node

tree = build_tree()
tree.print_tree()