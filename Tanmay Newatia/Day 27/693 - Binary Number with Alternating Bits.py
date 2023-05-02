class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        arr=[]
        while(n>0):
            arr+=[n&1]
            n>>=1
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                return False
        return True