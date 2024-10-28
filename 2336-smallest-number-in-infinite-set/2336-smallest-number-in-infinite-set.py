class SmallestInfiniteSet:

    def __init__(self):
        l=list(range(1,1001))
        self.s=set(l)
        
    def popSmallest(self) -> int:
        lowest=min(self.s)
        self.s.remove(lowest)
        return lowest
        

    def addBack(self, num: int) -> None:
        if(num not in self.s):
            self.s.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)