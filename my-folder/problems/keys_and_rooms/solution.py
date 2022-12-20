class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Create a queue for BFS
        queue = deque([0])
        # Create a set to store visited rooms
        visited = set()

        # Loop until the queue is empty
        while queue:
            # Get the next room from the queue
            room = queue.popleft()
            # Mark the room as visited
            visited.add(room)
            # Add the keys for the room to the queue
            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)

        # Return whether all rooms have been visited
        return len(visited) == len(rooms)