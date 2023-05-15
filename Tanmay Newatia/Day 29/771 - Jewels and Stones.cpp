class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        map<char,int> mp1;
        for(char i: jewels){
            mp1[i]++;
        }
        int c=0;
        for(char i:stones){
            if (mp1[i]>0){
                c++;
            }
        }
        return c;
    }
};

/*class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int c=0,i=0,j=0;
        while(int(stones[i])!=0){
            j=0;
            while(int(jewels[j])!=0){
                if (stones[i]==jewels[j]){
                    c++;
                    break;}
                j++;}
            i++;}
        return c;
    }
};*/