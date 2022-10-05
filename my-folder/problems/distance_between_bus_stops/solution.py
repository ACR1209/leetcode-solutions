class Solution:
    def distanceBetweenBusStops(self, d: List[int], start: int, destination: int) -> int:
        distance = 0
        totalDistance = 0
        
        for i, dis in enumerate(d):
            totalDistance += dis

            
            # If start is greater than destination
            # then that means we will have to do a "loop"
            # start = 2 destination = 1
            #     1
            # 0 ----- 1
            # |3      |2
            # |       |
            # 3 ----- 2
            #     2
            # in this case we will have the distances [1,_,2,3] = 6
            if start > destination and (i + 1 <= destination or i + 1 > start):
                distance += dis
            # If start is less than destination
            # then that means we will have to just go next
            # start = 2 destination = 1
            #     1
            # 0 ----- 1
            # |3      |2
            # |       |
            # 3 ----- 2
            #     2
            # in this case we will have the distances [_,_,2,_] = 2
            elif start < destination and ((i + 1 > start) and (i + 1 <= destination)):
                distance += dis
           
        # Return the min of the clockwise and counterclockwise route
        return min(distance, totalDistance - distance)
            
        
        