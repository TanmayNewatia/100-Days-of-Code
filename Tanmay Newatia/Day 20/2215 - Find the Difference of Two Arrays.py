class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1.sort()
        nums2.sort()
        a=[]
        for i in nums1:
            if i not in nums2:
                if a!=[]:
                    if a[-1]!=i:
                        a+=[i]
                else:
                    a+=[i]
        b=[]
        for i in nums2:
            if i not in nums1:
                if b!=[]:
                    if b[-1]!=i:
                        b+=[i]
                else:
                    b+=[i]
        return [a,b]