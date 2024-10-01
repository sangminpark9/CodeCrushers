import sys
sys.setrecursionlimit(10001)

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):

        if self.root is None:
            node = Node(data)
            self.root = node
        else:
            node = Node(data) # 새로운 값 노드 생성
            current = self.root
            while True:
                if current.data > data:
                    if current.left is None:
                        current.left = node
                        break

                    else:
                        current = current.left
                        
                else:
                    if current.right is None:
                        current.right = node
                        break

                    else:
                        current = current.right



def dfs(node):
    if node is None:
        return
    
    dfs(node.left)
    
    dfs(node.right)

    print(node.data)


def main():
    
    t = Tree()

    while True:
        try:
            data = int(input())
            t.insert(data)
            
        except EOFError:
            break

    
    if t is not None:
        dfs(t.root)

if __name__ == "__main__":
    main()
