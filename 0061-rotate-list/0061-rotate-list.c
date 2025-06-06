/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* rotateRight(struct ListNode* head, int k){
    if (!head || k == 0) {
        return head;
    }

    int len = 1;
    struct ListNode* tail = head;
    
    while (tail->next) {
        tail = tail->next;
        len++;
    }

    printf("len = %d\n", len);

    k %= len; // Effective rotations
    if (k == 0) {
        return head;
    }

    struct ListNode* curr = head;
    for (int i = 0; i < len - k - 1; i++) {
        curr = curr->next;
    }

    struct ListNode* newHead = curr->next;
    curr->next = NULL;
    tail->next = head;

    printf("newhead->next = %d\n", newHead->next->val);
    return newHead;
}