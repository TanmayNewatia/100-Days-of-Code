'''class Solution:
    def trap(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        trap=0
        while(abs(i-j)!=0):
            if height[i]>height[j]:
                mxn=min(height[i],height[j])
                while(height[j]<=mxn and abs(i-j)!=0):
                    trap+=abs(mxn-height[j])
                    j-=1
            elif height[i]<height[j]:
                mxn=min(height[i],height[j])
                while(height[i]<=mxn and abs(i-j)!=0):
                    trap+=abs(mxn-height[i])
                    i+=1
            else:
                mxn=height[i]
                while(height[i]<=height[j] and abs(i-j)!=0):
                    if mxn>=height[i]:
                        trap+=abs(mxn-height[i])
                    i+=1
                while(height[j]<=mxn and abs(i-j)!=0):
                    if mxn>=height[j]:
                        trap+=abs(mxn-height[j])
                    j-=1
        return trap'''


class Solution:
    def trap(self, height: List[int]) -> int:
        i,j=1,len(height)-2
        lm,rm=height[0],height[len(height)-1]
        trap=0
        while(i<=j):
            if height[i]>=lm:
                lm=height[i]
                i+=1                
            elif height[j]>=rm:
                rm=height[j]
                j-=1
            elif lm<=rm and height[i]<lm:
                trap+=lm-height[i]
                i+=1
            else:
                trap+=rm-height[j]
                j-=1
        return trap