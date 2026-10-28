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
    bool hasCycle(ListNode* head) {
        ListNode* fast = head;
        ListNode* temp = head;

        while (fast != nullptr && fast->next != nullptr) {
            fast = fast->next->next;
            temp = temp->next;
            if (temp == fast) {
                return true;
            }
        }
        return false;
    }
};
