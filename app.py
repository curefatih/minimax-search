

# Step1. initial state -> game tree

# Game Tree
# --> init
#  -

# Game Node

class Node:
    def __init__(self, nodeCount, point=0):
        self.point = point
        self.nodeCount = nodeCount
        self.__nodes = []

    def addNewNode(self, newNode: "Node"):
        if(self.nodeCount != len(self.__nodes)):
            self.__nodes.append(newNode)
            return True
        return False

    def nodes(self):
        return self.__nodes


class GameTree:
    def __init__(self, depth, nodeChildCount, maxPoint=1000):
        self.depth = depth
        self.nodeChildCount = nodeChildCount
        self.root = Node(5)
        self.maxPoint = maxPoint

    def randomizeGameTree(self):
        import random

        def randomizeNode(): return Node(self.nodeChildCount,
                                         random.randint(0, self.maxPoint))

        def recursiveCreator(depth, maxDepth, localRoot: "Node"):
            if(depth == maxDepth):
                return
            for _ in range(self.nodeChildCount):
                localRoot.addNewNode(randomizeNode())
            for current_child_node in localRoot.nodes():
                recursiveCreator(depth + 1, maxDepth, current_child_node)

        recursiveCreator(1, 5, self.root)

    def minimax(self):
        pass


if __name__ == "__main__":
    gt = GameTree(5, 5)
    gt.randomizeGameTree()

    def printInorder(root):

        if root:

            print(root.point)

            for node in root.nodes():
                printInorder(node)

    printInorder(gt.root)