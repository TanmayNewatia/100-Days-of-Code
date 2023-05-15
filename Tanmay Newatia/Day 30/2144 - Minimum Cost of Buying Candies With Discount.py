class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        cost.reverse()
        c=0
        total=0
        for i in range(len(cost)):
            c+=1
            if c%3==0:
                c=0
            else:
                total+=cost[i]
        return total