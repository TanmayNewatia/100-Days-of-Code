class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dic={}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=i
            else:
                dic[s[i]]=abs(i-dic[s[i]]-1)
        letter={"a":distance[0],"b":distance[1],"c":distance[2],"d":distance[3],"e":distance[4],"f":distance[5],"g":distance[6],"h":distance[7],"i":distance[8],"j":distance[9],"k":distance[10],"l":distance[11],"m":distance[12],"n":distance[13],"o":distance[14],"p":distance[15],"q":distance[16],"r":distance[17],"s":distance[18],"t":distance[19],"u":distance[20],"v":distance[21],"w":distance[22],"x":distance[23],"y":distance[24],"z":distance[25]}
        for i in dic.keys():
            if letter[i]!=dic[i]:
                return 0
        return 1