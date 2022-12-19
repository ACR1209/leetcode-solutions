class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Create a list to store the edges for each vertex
        adj_list = [[] for _ in range(n)]

        # Add the edges to the adjacency list
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # Create a queue for the BFS and add the source vertex
        queue = deque([source])

        # Create a set to store the visited vertices
        visited = set()

        # While the queue is not empty
        while queue:
            # Get the next vertex from the queue
            vertex = queue.popleft()

            # If the vertex is the destination, return True
            if vertex == destination:
                return True

            # If the vertex has not been visited
            if vertex not in visited:
                # Mark it as visited
                visited.add(vertex)

                # Add its neighbors to the queue
                for neighbor in adj_list[vertex]:
                    queue.append(neighbor)

        # If we reach this point, it means there is no path from the source to the destination
        return False