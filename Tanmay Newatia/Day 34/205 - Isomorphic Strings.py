class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic={}
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] not in dic.values():
                    dic[s[i]]=t[i]
                else:
                    return 0
            else:
                if t[i]!=dic[s[i]]:
                    return 0
        return 1