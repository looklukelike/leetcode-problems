class SmallestInfiniteSet:

    arr = []
    def __init__(self):
        self.arr = [x for x in range(1, 1001)]

    def popSmallest(self) -> int:
        smallest = self.arr[0]
        self.arr = self.arr[1:]
        return smallest
        

    def addBack(self, num: int) -> None:
        i = 0
        while num >= self.arr[i]:
            if num == self.arr[i]:
                return
            i += 1
        self.arr.insert(i, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)