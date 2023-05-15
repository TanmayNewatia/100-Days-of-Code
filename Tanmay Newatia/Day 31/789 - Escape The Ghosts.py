class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        mxn=10**8
        for i in ghosts:
            gcost=abs(target[0]-i[0])+abs(target[1]-i[1])
            mxn=min(gcost,mxn)
            print(mxn)
        pcost=abs(target[0]-0)+abs(target[1]-0)
        if mxn>pcost:
            return True
        else:
            return False