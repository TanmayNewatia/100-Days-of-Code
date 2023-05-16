class Solution {
public:
    bool isSubsequence(string s, string t) {
        if(t.size()<s.size()){
            return 0;
        }
        else if (s.size()==0){
            return 1;
        }
        else{
            int i=s.size(),j=0;
            for(int k=0;k<t.size();k++){
                if(s[j]==t[k]){
                    j++;
                    i--;
                    if(i==0){
                        return 1;
                    }
                }
            }
            return 0;
        }
        return 0;
    }
};