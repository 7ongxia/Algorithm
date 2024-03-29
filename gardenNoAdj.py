class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        '''
        1. create graph using dict (bidirectional)
        2. use bfs to color nodes (use nodeColor)
        3. order colors by garden index
        '''
        # Base Case
        if not paths:
            return [1] * n

        nodeColor = [None] * (n + 1)
        graph = collections.defaultdict(set)
        for path in paths:
            graph[path[0]].add(path[1])
            graph[path[1]].add(path[0])

        for node in range(1, n + 1):
            # Alone
            if node not in graph:
                nodeColor[node] = 1
                continue
            # BFS
            if nodeColor[node] == None:
                queue = collections.deque([node])
                while queue:
                    nodeFrom = queue.popleft()
                    color = [1, 2, 3, 4]
                    for nodeTo in graph[nodeFrom]:
                        if nodeColor[nodeTo] == None:
                            queue.append(nodeTo)
                        elif nodeColor[nodeTo] in color:
                            color.remove(nodeColor[nodeTo])
                    nodeColor[nodeFrom] = color[0]

        return nodeColor[1:]
