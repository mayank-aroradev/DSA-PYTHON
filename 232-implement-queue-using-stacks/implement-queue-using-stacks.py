class MyQueue:

    def __init__(self):
        self.st2=[]
        self.st1=[]

        

    def push(self, x: int) -> None:
        while len(self.st1)>0:
            self.st2.append(self.st1.pop())
        self.st2.append(x)
        while len(self.st2)>0:
            self.st1.append(self.st2.pop())
    def pop(self):
        if not self.st1:
            return None
        return self.st1.pop()
    



    
        

    def peek(self) -> int:
        if not self.st1:
            return None
        return self.st1[-1]

        

    def empty(self) -> bool:
        return not self.st1

# O(N)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()