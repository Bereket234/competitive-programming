class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        vector<int>targetIndex;
        int temp, min;
        for(int i=0;i<nums.size();i++){
             min=i;
            for(int j=i;j<nums.size();j++){
                if(nums[j] < nums[min]){
                    min= j;
            }
        }
            temp=nums[i];
            nums[i]=nums[min];
            nums[min]=temp;
        }
        for(int i=0; i<nums.size();i++){
            if(nums[i]==target){
                targetIndex.push_back(i);
            }
        }
        return(targetIndex);
    }
};
