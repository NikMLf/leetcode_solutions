#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    size_t partition(size_t left, size_t right, vector<int>& nums) {
        int pivot = nums[right];
        size_t i = left;
        
        for (size_t j = left; j < right; ++j) {
            if (nums[j] < pivot) {
                std::swap(nums[i], nums[j]);
                ++i;
            }
        }
        std::swap(nums[i], nums[right]);
        return i;
    }
    
    void quick_sort(size_t left, size_t right, vector<int>& nums) {
        if (left >= right) return;
        
        size_t pivot_index = partition(left, right, nums);
        
        if (pivot_index > left) {
            quick_sort(left, pivot_index - 1, nums);
        }
        
        if (pivot_index + 1 < right) {
            quick_sort(pivot_index + 1, right, nums);
        }
    }


    size_t partition_pairs(size_t left, size_t right, vector<pair<int, int>>& nums) {
        // Опорный элемент - пара
        pair<int, int> pivot = nums[right];
        size_t i = left;
        
        for (size_t j = left; j < right; ++j) {
           
            if (nums[j].first > pivot.first) {
                std::swap(nums[i], nums[j]);
                ++i;
            }
        }
        std::swap(nums[i], nums[right]);
        return i;
    }
    
    void quick_sort(size_t left, size_t right, vector<pair<int, int>>& nums) {
        if (left >= right) return;
        
        size_t pivot_index = partition_pairs(left, right, nums);
        
        if (pivot_index > left) {
            quick_sort(left, pivot_index - 1, nums);
        }
        
        if (pivot_index + 1 < right) {
            quick_sort(pivot_index + 1, right, nums);
        }
    }

    vector<int> topKFrequent(vector<int>& nums, int k) {

        unordered_map<int, int> counts;
        for (int num : nums) {
            counts[num]++;
        }
        
   
        vector<pair<int, int>> freq_pairs;
        for (auto& p : counts) {
            freq_pairs.push_back({p.second, p.first});
        }
        
        
        if (!freq_pairs.empty()) {
            quick_sort(0, freq_pairs.size() - 1, freq_pairs);
        }
        
     
        vector<int> res;
        
        int limit = min(k, (int)freq_pairs.size());
        
        for (int i = 0; i < limit; ++i) {
            res.push_back(freq_pairs[i].second);
        }
        
        return res;
    }
};