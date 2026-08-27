class MinStack:
    
    def __init__(self):
        self.stack = deque()

    # when pushing, store pair [val, min_val]
    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val == None or min_val > val:
            min_val = val # found new mininum value
        self.stack.append([val, min_val])   

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None
        
    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None # the min so far at top of stack
        
