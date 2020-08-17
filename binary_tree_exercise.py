
class BinaryTree():

    def __init__(self, root):
        self.root = root
        self.left_branch = None
        self.right_branch = None

    def insert_left(self, newbranch):

        if self.left_branch is None:
            self.left_branch = BinaryTree(newbranch)
        else:
            t = BinaryTree(newbranch)
            t.left_branch = self.left_branch
            self.left_branch = t

    def insert_right(self, newbranch):

        if self.right_branch is None:
            self.right_branch = BinaryTree(newbranch)
        else:
            t = BinaryTree(newbranch)
            t.right_branch = self.right_branch
            self.right_branch = t

    def get_right_branch(self):

        return self.right_branch

    def get_left_branch(self):

        return self.left_branch

    def set_root_value(self, value):

        self.root = value

    def get_root_value(self):

        return self.root


def preorder(tree):
    if tree is not None:
        print(tree.get_root_value())
        preorder(tree.get_left_branch())
        preorder(tree.get_right_branch())


def postorder(tree):
    if tree is not None:
        postorder(tree.get_left_branch())
        postorder(tree.get_right_branch())
        print(tree.get_root_value())


def inorder(tree):
    if tree is not None:
        inorder(tree.get_left_branch())
        print(tree.get_root_value())
        inorder(tree.get_right_branch())


bt = BinaryTree('_')
# print(bt.get_root_value())
bt.insert_left('b')
bt.insert_right('1')
bt.insert_left('c')
bt.insert_right('2')
inorder(bt)






