class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        res = []
        sort_ele = count.most_common()
        sort_ele = sorted(sorted(sort_ele, key = lambda x : x[0]), key = lambda x : x[1], reverse = True)

        for el, _freq in sort_ele[:k]:
            res.append(el)
        
        return res
            