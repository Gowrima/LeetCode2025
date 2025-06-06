/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode dummy;
    struct ListNode *prev = &dummy;

    if (head == NULL || head->next == NULL) return head;

    prev->next = head;

    struct ListNode *first = head, *second = NULL;

    while (first && first->next) {
        second = first->next;

        prev->next = second;
        first->next = second->next;
        second->next = first;

        prev = first;
        first = first->next;
    }
        
    return dummy.next;

}

