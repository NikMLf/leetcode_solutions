class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        unordered_map<int, int> counts;
        vector<int> result;
        int count = 0;
        for (int num : nums) {
            counts[num]++;
            if (counts[num] == 1) {count++; result.push_back(num);}
        }
        nums = std::move(result);

        return count;
    }
};