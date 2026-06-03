class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;

        int insert_pos = 1; 

        for (size_t i = 1; i < nums.size(); ++i) {
            if (nums[i] != nums[i - 1]) {
                nums[insert_pos] = nums[i]; 
                insert_pos++;
            }
        }
        nums.resize(insert_pos);
        return nums.size();
    }
};