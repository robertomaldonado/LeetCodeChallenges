class MovingAverage:
    def __init__(self, size: int):
        self.movingAverage = size
        self.average = None
        self.stack = list()
        
    def next(self, val: int) -> float:
        if len(self.stack) < self.movingAverage:
            self.stack.append(val)
        elif len(self.stack) == self.movingAverage:
            print(self.stack.pop(0))
            self.stack.append(val)
            
        return sum(self.stack)/len(self.stack)
            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)