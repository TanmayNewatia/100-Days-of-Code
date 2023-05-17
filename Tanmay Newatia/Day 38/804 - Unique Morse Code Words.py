class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        dic={}
        for i in words:
            s=""
            for j in i:
                s+=morse[j]
            if s not in dic:
                dic[s]=1
            else:
                dic[s]+=1
        return len(dic)