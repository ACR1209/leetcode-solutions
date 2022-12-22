from collections import defaultdict
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        # Initialize a colors array to store the group that each person belongs to
        colors = [-1] * (n+1)

        # Perform a breadth-first search on the graph to check if it is bipartite
        for i in range(1, n+1):
            # If the node has not been visited, perform a breadth-first search starting from it
            if colors[i] == -1:
                # Initialize a queue for the breadth-first search and add the starting node
                queue = [(i, 0)]
                colors[i] = 0

                # Perform the breadth-first search
                while queue:
                    # Get the next node in the queue and its color
                    node, color = queue.pop(0)

                    # Check the color of the node's neighbors
                    for neighbor in graph[node]:
                        # If the neighbor has the same color as the node, then the graph is not bipartite
                        if colors[neighbor] == color:
                            return False
                        # If the neighbor has not been visited, add it to the queue with the opposite color
                        elif colors[neighbor] == -1:
                            colors[neighbor] = 1 - color
                            queue.append((neighbor, 1 - color))

        # If the breadth-first search completes without finding any conflicting colors, the graph is bipartite
        return True
