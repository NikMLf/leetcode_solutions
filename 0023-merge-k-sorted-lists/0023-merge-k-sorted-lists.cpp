/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        map<int, vector<ListNode*>> nodes;
      
        for (int i = 0; i < lists.size(); ++i) {
            ListNode *ptr = lists[i];
            while (ptr != nullptr)
            {
                ListNode * next_ptr = ptr->next;
                nodes[ptr->val].push_back(ptr);
                ptr = next_ptr;
            }
        }

        ListNode *result = new ListNode(0);
        ListNode * ptr = result;    

        for (const auto & i : nodes) {
            for (ListNode* node : i.second) {
                ptr->next = node;
                ptr = ptr->next;
            }
        }
        ptr->next = nullptr;

        result = result->next;
        return result;
    }
};