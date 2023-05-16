class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> bits;
        for(int i=0;i<=n;i++){
            int temp=i,c=0;
            while(temp>0){
                if(temp&1){
                    c++;
                }
                temp>>=1;
            }
            bits.push_back(c);
        }
        return bits;
    }
};