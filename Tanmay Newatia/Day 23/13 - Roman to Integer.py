class Solution:
    def romanToInt(self, s: str) -> int:
        length=len(s)
        ans=0
        i=0
        while(i<length):
            if i!=length-1:
                if s[i]=='I':
                    if s[i+1]=='V':
                        ans+=4
                        i+=2
                    elif s[i+1]=='X':
                        ans+=9
                        i+=2
                    else:
                        ans+=1
                        i+=1
                elif s[i]=='X':
                    if s[i+1]=='L':
                        ans+=40
                        i+=2
                    elif s[i+1]=='C':
                        ans+=90
                        i+=2
                    else:
                        ans+=10
                        i+=1
                elif s[i]=='C':
                    if s[i+1]=='D':
                        ans+=400
                        i+=2
                    elif s[i+1]=='M':
                        ans+=900
                        i+=2
                    else:
                        ans+=100
                        i+=1
                else:
                    if s[i]=='V':
                        ans+=5
                    elif s[i]=='L':
                        ans+=50
                    elif s[i]=='D':
                        ans+=500
                    elif s[i]=='M':
                        ans+=1000
                    i+=1
            else:
                if s[i]=='I':
                    ans+=1
                elif s[i]=='V':
                    ans+=5
                elif s[i]=='X':
                    ans+=10
                elif s[i]=='L':
                    ans+=50
                elif s[i]=='C':
                    ans+=100
                elif s[i]=='D':
                    ans+=500
                elif s[i]=='M':
                    ans+=1000
                i+=1
        return ans