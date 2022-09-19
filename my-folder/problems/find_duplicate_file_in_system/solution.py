class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        lookup = {}
        res = []
        
        for path in paths:
            contents = path.split(" ")
            for i, val in enumerate(contents[1:]):
                file = val.split("(")
                file[1] = file[1].replace(")", "")
                
                if file[1] not in lookup:
                    lookup[file[1]] = [contents[0] + "/" + file[0]]
                else:
                    lookup[file[1]].append(contents[0] + "/" + file[0])
                
                
        for k, v in lookup.items():
            if(len(v) > 1):
                res.append(v)
        
        return res