class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_value=float("inf")

        

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(value)
            self.min_value=value
        elif value>self.min_value:
            self.stack.append(value)
        else:
            self.stack.append(2*value-self.min_value)
            self.min_value=value
        
        

    def pop(self) -> None:
        if not self.stack:
            return -1
        top=self.stack.pop()
        if top<self.min_value:
            self.min_value=2*self.min_value-top


        

    def top(self) -> int:
        if not self.stack:
            return -1
        top=self.stack[-1]
        return self.min_value if top<self.min_value else top
        

    def getMin(self) -> int:
        if not self.stack:
            return -1
        return self.min_value
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()