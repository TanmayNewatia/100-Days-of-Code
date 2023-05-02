class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na,nb=0,0
        for i in range(1,len(a)+1):
            na+=int(a[-i])*(pow(2,i-1))
        for i in range(1,len(b)+1):
            nb+=int(b[-i])*(pow(2,i-1))
        ba=str(bin(na+nb))
        return ba[2:]