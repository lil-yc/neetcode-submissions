class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for c in tokens: 
            if c == "+": # pop top 2 elems and add
                st.append(st.pop() + st.pop())
            elif c == "-": # pop top 2 elems and subtract
                second, first = st.pop(), st.pop()
                st.append(first - second)
            elif c == "*": # pop top 2 elems and mult
                st.append(st.pop() * st.pop())
            elif c == "/": # pop top 2 elems and div
                second, first = st.pop(), st.pop()
                st.append(int(first / second))                
            else: # push on stack
                st.append(int(c))
        
        return st[0]