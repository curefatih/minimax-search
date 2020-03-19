import math  # for intinity numbers


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
        self.root = Node(self.nodeChildCount)
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
                childPoints = self.__minimax(
                    current_node, depth + 1, maxDepth, not(isMaximizing))
                child_best_move = max(childPoints) if not(
                    isMaximizing) else min(childPoints)
                # print("is max", not(isMaximizing), " best: ", child_best_move, " points:", childPoints)
                local_root_points[cn_index] = local_root_points[cn_index] + \
                    child_best_move
        return local_root_points

    def travel(self, path, node: "Node"):
        local_root = node
        for alpha in path:
            path_move = int(alpha)
            if(len(local_root.nodes()) > path_move):
                local_root = local_root.nodes()[path_move]
            else:
                print("Daha fazla ilerlenebilir değil!")
                break
        self.showPoints(local_root)
        return local_root

    def showPoints(self, node: "Node"):
        print("\nŞuan içerinde bulunduğunuz Node'un puan değeri: ", node.point)
        if(len(node.nodes()) > 0):
            print("Child node'ların puan değerleri: ", [x.point for x in node.nodes()])
        print(self.__minimax(node, 0, self.depth, True))
        print(self.__minimax(node, 0, self.depth, False))
        print()

# main function
# 
if __name__ == "__main__":
    gt = GameTree(5, 5)

    gt.randomizeGameTree()

    def printTree(root):
        if root:
            print(root.point)
            for node in root.nodes():
                printTree(node)

    # Game On
    maxMin = {
        1: True,
        -1: False
    }
    moves = ""
    currentNode = gt.root
    currentApproachMaximizing = True
    for i in range(4):
        bestMove = gt.bestMove(currentNode, i, gt.depth, maxMin[currentApproachMaximizing])
        print("En iyi hamle: ", bestMove, " max mı? : ", maxMin[currentApproachMaximizing], "\n")
        moves = moves + str(bestMove)
        currentApproachMaximizing = currentApproachMaximizing  * -1
        currentNode = currentNode.nodes()[bestMove]
    
    print("Yapılan hamleler sıraysıla: ", moves, "\n")

    # Travel for check
    local_root = gt.root
    while True:
        print("_______________________________________________")
        print("Node gezmek için: N\n" +
            "Geçerli konumun değerlerini görmek için: S\n" +
            "Sonlandırmak için: q\n")
        inp=input(":")

        if(inp == "q"):
            break

        if(inp == "N" or inp == "n"):
            print("-- Örneğin 123 -> iç içe olmak şartıyla 1, 2, 3 indexli değerlerin içerisine girer.\n root node' a dönmek için -1")
            gt.showPoints(local_root)
            move_inp = input(":")
            if(move_inp == "-1"):
                local_root= gt.root
                continue

            if not(str.isnumeric(move_inp)):
                print("!! Girdi nümerik değerlerden oluşmalı")
                continue
            local_root= gt.travel(move_inp, local_root)

        if(inp == "S" or inp == "s"):
            gt.showPoints(local_root)
