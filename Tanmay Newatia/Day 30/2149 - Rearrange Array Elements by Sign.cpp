class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> p;
        vector<int> n;
        int len=nums.size();
        for(int i=0;i<len;i++){
            if (nums[i]>0){
                p.push_back(nums[i]);
            }
            else{
                n.push_back(nums[i]);
            }
        }

        nums={};
        for(int i=0;i<len;i++){
            if (i%2==0){
                nums.push_back(p[i/2]);
            }
            else{
                nums.push_back(n[i/2]);
            }
        }
        return nums;
    }
};