class Solution:
    def repeatedCharacter(self, s: str) -> str:
        st = set()
        for char in s:
            if char not in st:
                st.add(char)
                continue
            
            return char