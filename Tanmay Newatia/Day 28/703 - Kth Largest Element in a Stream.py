class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.n=nums
        self.ind=k

    def add(self, val: int) -> int:
        self.n+=[val]
        self.n.sort()
        return self.n[-self.ind]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)