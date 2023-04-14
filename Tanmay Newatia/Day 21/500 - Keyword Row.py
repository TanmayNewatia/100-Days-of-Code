class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans=[]
        for i in words:
            row=[]
            for j in range(len(i)):
                if j==0:
                    if i[j].lower() in ['q','w','e','r','t','y','u','i','o','p']:
                        row=['q','w','e','r','t','y','u','i','o','p']
                    elif i[j].lower() in ['a','s','d','f','g','h','j','k','l']:
                        row=['a','s','d','f','g','h','j','k','l']
                    else:
                        row=['z','x','c','v','b','n','m']
                else:
                    if i[j].lower() not in row:
                        break
            else:
                ans+=[i]
        return ans
            