class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Create a graph where each node is a key and its value is a list of its neighbors
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Initialize the sums array to store the sum of distances for each node
        sums = [0] * n

        # Initialize the count array to store the number of nodes reachable from each node
        count = [1] * n

        # Perform a depth-first search to calculate the sum and count for each node
        def dfs(node, parent):
            # Iterate over the neighbors of the current node
            for neighbor in graph[node]:
                # Skip the parent node
                if neighbor == parent:
                    continue
                # Recursively visit the neighbor and add the distance to the sum and count for the current node
                dfs(neighbor, node)
                sums[node] += sums[neighbor] + count[neighbor]
                count[node] += count[neighbor]

        # Perform a depth-first search starting from node 0 to calculate the initial sums and counts
        dfs(0, -1)

        # Initialize the result array to store the final sum of distances for each node
        result = [0] * n

        # Perform a breadth-first search to update the result array
        def bfs(node, parent):
            # Iterate over the neighbors of the current node
            for neighbor in graph[node]:
                # Skip the parent node
                if neighbor == parent:
                    continue
                # Update the result for the neighbor based on the sum and count of the current node
                result[neighbor] = result[node] + n - 2 * count[neighbor]
                # Recursively visit the neighbor
                bfs(neighbor, node)

        # Perform a breadth-first search starting from node 0 to update the result array
        result[0] = sums[0]
        bfs(0, -1)

        return result