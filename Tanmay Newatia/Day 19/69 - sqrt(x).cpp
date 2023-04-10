class Solution {
public:
    int mySqrt(int x) {
        long long int beg=0,end=x;
        while(beg<=end){
            long long int mid=(beg+end)/2;
            long long int ans=mid*mid;
            if (ans==x){
                return mid;
            }
            else{
                if(ans>x){
                    end=mid-1;
                }
                else{
                    beg=mid+1;
                }
            }
        }
        return end;
    }
};