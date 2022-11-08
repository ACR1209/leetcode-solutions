class Solution:
    def makeGood(self, s: str) -> str:
        st = []

        for char in s:
            if len(st) != 0 and (ord(st[-1]) == ord(char) - 32 or ord(st[-1]) - 32 == ord(char)):
                st.pop()
                continue
            
            st.append(char)

        return ''.join(st)
