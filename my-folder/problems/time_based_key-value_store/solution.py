class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
       
        if key not in self.dict:
            self.dict[key] = [None] * timestamp
            self.dict[key][timestamp - 1] = value
            return            

        while len(self.dict[key]) <= timestamp - 1:
            self.dict[key].append(None)
            
        self.dict[key][timestamp - 1] = value
        

    def get(self, key: str, timestamp: int) -> str:  
        if key in self.dict:
            if timestamp - 1 < len(self.dict[key]) and self.dict[key][timestamp - 1]:
                return self.dict[key][timestamp - 1]
            
            current = timestamp - 2
            while current >= len(self.dict[key]) or not self.dict[key][current]:
                current -= 1
            
            
            return self.dict[key][current] if current != -1 else ""
                
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)