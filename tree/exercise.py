class TreeNode:
    def __init__(self, data, designation):
        self.data = data
        self.designation = designation
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

    def print_tree(self, structure):
        space = ' ' * self.get_level() * 3
        prifix = space + '|__ '
        if structure == 'name':
            print(prifix + self.data)
        elif structure == 'designation':
            print(prifix + self.designation)
        else:
            print(prifix + self.data, ' (', self.designation ,')')

        if self.children:
            for child in self.children:
                child.print_tree(structure)

def build_management_tree():
    node = TreeNode('Nilupul', 'CEO')

    cto = TreeNode('Chinmay', 'CTO')
    i_head = TreeNode('Vishwa', 'Infrastructure Head')
    i_head.add_child(TreeNode('Dhaval', 'Cloud Manager'))
    i_head.add_child(TreeNode('Abhijith', 'App Manager'))
    a_head = TreeNode('Amir', 'Application Head')

    cto.add_child(i_head)
    cto.add_child(a_head)

    hr = TreeNode('Gels', 'HR Head')
    hr.add_child(TreeNode('Peter', 'Recruitement Manager'))
    hr.add_child(TreeNode('Waqas', 'Policy Manager'))

    node.add_child(cto)
    node.add_child(hr)

    return node

tree = build_management_tree()
tree.print_tree('name')
tree.print_tree('designation')
tree.print_tree('both')