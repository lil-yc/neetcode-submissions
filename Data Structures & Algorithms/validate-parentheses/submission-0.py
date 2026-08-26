class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mapping = {")":"(", "}":"{", "]":"["} # map closing to opening

        for char in s:
            if char in mapping.values(): # opening bracket
                stack.append(char)
            elif char in mapping.keys(): # closing bracket
                if not stack or mapping[char] != stack.pop():
                    return False # if stack empty or stack top not correct opening
        
        return not stack # stack should be empty