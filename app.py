import math #for intinity numbers

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

        recursiveCreator(0, self.depth, self.root)

    def bestMove(self, localRoot: "Node", depth, maxDepth, isMaximizing):
        result = self.__minimax(localRoot, depth, maxDepth, isMaximizing)
        print(result)
        return result.index(max(result) if isMaximizing else min(result))

    def __minimax(self, localRoot: "Node", depth, maxDepth, isMaximizing):
        local_root_points = [node.point for node in localRoot.nodes()]
        if (depth + 1 < maxDepth):
            for cn_index in range(len(localRoot.nodes())):
                current_node = localRoot.nodes()[cn_index]
                childPoints = self.__minimax(current_node, depth + 1, maxDepth, not(isMaximizing))
                child_best_move = max(childPoints) if not(isMaximizing) else min(childPoints)
                local_root_points[cn_index] = local_root_points[cn_index] + child_best_move
        return local_root_points


if __name__ == "__main__":
    gt = GameTree(3, 5)

    gt.randomizeGameTree()

    def printTree(root):

        if root:

            print(root.point)

            for node in root.nodes():
                printTree(node)

    # printTree(gt.root)

    print("__________________")

    # z = gt.minimax(gt.root, 0, 1, True)

    # print(z)

    # print([node.point for node in gt.root.nodes()])

    print("__________________")

    z = gt.bestMove(gt.root, 0, 3, True)

    print(z)
