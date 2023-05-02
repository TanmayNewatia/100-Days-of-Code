class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        size=len(nums)
        k=k%size
        removed=[nums[i] for i in range(0,size-k)]
        j=0
        for i in range(size-k,size):
            nums[j]=nums[i]
            j+=1
        for i in range(len(removed)):
            nums[j]=removed[i]
            j+=1