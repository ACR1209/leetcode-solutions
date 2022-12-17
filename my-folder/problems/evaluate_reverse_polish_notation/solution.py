class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for token in tokens:
            if token not in "+*-/":
                st.append(token)
            else:
                a = int(st.pop())
                b = int(st.pop())
                
                if token == "+":
                    st.append(b + a)
                elif token == "-":
                    st.append(b - a)
                elif token == "*":
                    st.append(b * a)
                else:
                    st.append(b / a)
        
        return int(st[0])

            
