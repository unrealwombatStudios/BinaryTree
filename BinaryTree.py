class BinaryTree:
    # [data, left[], right[]]
    # exemple: ['F', ['B', ['A', [], []], ['D', ['C', [], []], ['E', [], []]]], ['G', [], ['I', ['H', [], []], []]]]

    def __init__(self, tree = None):
        if tree != None:
            self.tree = tree
        else:
            self.tree = []

    def add(self, data):
        if len(self.tree) is 0:
            self.tree.append(data)
            self.tree.append([])
            self.tree.append([])
        else:
            self.insert(self.tree, data)

    def insert(self, node, data):
        if len(node) is 0:
            node.append(data)
            node.append([])
            node.append([])
        elif data < node[0]:
            self.insert(node[1], data)
        elif data >= node[0]:
            self.insert(node[2], data)

    def printMode(self, mode):
        if mode is "inOrder":
            print("inOrder: ", end = "")
            self.inOrder(self.tree)
        elif mode is "postOrder":
            print("postOrder: ", end = "")
            self.postOrder(self.tree)
        elif mode is "preOrder":
            print("preOrder: ", end = "")
            self.preOrder(self.tree)
        else:
            print("No mode!")

    def preOrder(self, node):
        if len(node) is not 0:
            print(node[0], end = "")
            self.preOrder(node[1])
            self.preOrder(node[2])

    def inOrder(self, node):
        if len(node) is not 0:
            self.inOrder(node[1])
            print(node[0], end = "")
            self.inOrder(node[2])

    def postOrder(self, node):
        if len(node) is not 0:
            self.postOrder(node[1])
            self.postOrder(node[2])
            print(node[0], end = "")

    def countNodes(self, node):
        if len(node) is not 0:
            return self.countNodes(node[1]) + self.countNodes(node[2]) + 1
        else:
            return 0

    def depthOfTree(self, node):
        if len(node) is not 0:
            return (max(self.depthOfTree(node[1]), self.depthOfTree(node[2])) + 1)
        else:
            return 0

    def containsData(self, data):
        if len(self.tree) is not 0:
            return self.searchRec(self.tree, data)
        else:
            return -1

    def searchRec(self, node, data):
        if len(node) is not 0:
            if node[0] is data:
                return True
            elif data <= node[0]:
                return self.searchRec(node[1], data)
            elif data > node[0]:
                return self.searchRec(node[2], data)
        else:
            return False


if __name__ == "__main__":
    tree = BinaryTree()
    tree.add("F")
    tree.add("B")
    tree.add("A")
    tree.add("D")
    tree.add("C")
    tree.add("E")
    tree.add("G")
    tree.add("I")
    tree.add("H")

    print("tree:", tree.tree)
    print(tree.printMode("preOrder"))
    print(tree.printMode("inOrder"))
    print(tree.printMode("postOrder"))

    print("")

    print("Nbr of Nodes: ", tree.countNodes(tree.tree))
    print("Depth of Tree: ", tree.depthOfTree(tree.tree))

    print("")

    print("Is ""G"" in Tree: ", tree.containsData("G"))
    print("Is ""A"" in Tree: ", tree.containsData("A"))
    print("Is ""Z"" in Tree: ", tree.containsData("Z"))
