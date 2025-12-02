class MinStack:

    def __init__(self):
        self.stack = list()
        self.min_ = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_) > 0 and val <= self.min_[0]:
            self.min_.insert(0, val)
        else:
            self.min_.append(val)
            
    def pop(self) -> None:
        # remove from stack
        # update min
        to_remove = self.stack[-1]
        del self.stack[-1]
        if to_remove == self.min_[0]:
            #find next min elem    
            del self.min_[0]
        #print (self.min_)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # do not remove
        #print (self.min_)
        return self.min_[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()