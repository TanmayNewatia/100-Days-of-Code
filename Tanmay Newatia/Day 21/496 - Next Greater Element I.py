class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            flag=1
            for j in range(nums2.index(i),len(nums2)):
                if nums2[j]>i:
                    flag=0
                    ans+=[nums2[j]]
                    break
            if flag:
                ans+=[-1]
        return ans