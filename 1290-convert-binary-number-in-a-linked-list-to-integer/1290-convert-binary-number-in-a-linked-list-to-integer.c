/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


int getDecimalValue(struct ListNode* head) {
    unsigned int result = 0;

    struct ListNode* cur = head;

    while (cur) {
        result = result << 1 | cur->val;
        cur = cur->next;
    }

    return result;
}