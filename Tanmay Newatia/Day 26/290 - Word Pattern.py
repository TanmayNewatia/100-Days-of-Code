class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat={}
        s=s.split()
        if len(pattern)!=len(s):
            return False
        for i in range(len(s)):
            if pattern[i] not in pat:
                if s[i] in pat.values():
                    return False
                pat[pattern[i]]=s[i]
            else:
                if pat[pattern[i]]==s[i]:
                    continue
                else:
                    return False
        return True