class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        class Node:
            self.id: int
            self.parent: int

            def __init__(self, _id):
                self.id = _id
                self.parent = self.id

        cities = [Node(x) for x in range(len(isConnected))]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                cities[root_b].parent = root_a

        def find(a):
            
            while a.parent != a.id:
                a = cities[a.parent]
            return a.id

        for i in range(len(cities) - 1):
            for j in range(i + 1, len(cities)):
                if isConnected[i][j] == 1 or isConnected[j][i] == 1:
                    union(cities[i], cities[j])
        
        provinces = set([find(node) for node in cities])
        return len(provinces)
            