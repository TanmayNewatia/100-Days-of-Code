class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        mxn=0
        start=0
        i=start
        while(i<len(s)):
            if s[i] not in dic:
                dic[s[i]]=1
                i+=1
            else:
                mxn=max(mxn,len(dic))
                start+=1
                i=start
                dic={}
        mxn=max(mxn,len(dic))
        return mxn