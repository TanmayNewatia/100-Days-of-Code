class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=0
        for i in digits:
            n*=10
            n+=i
        n+=1
        l=[]
        while(n!=0):
            l+=[n%10]
            n//=10
        l.reverse()
        return l