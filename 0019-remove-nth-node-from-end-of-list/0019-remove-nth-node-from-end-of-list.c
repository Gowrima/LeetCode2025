/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {

    if (head == NULL) return NULL;

    struct ListNode *cur = head;
    struct ListNode *prev = NULL;
    
    int len = 0;

    while (cur != NULL) {
        len++;
        cur = cur->next;
    }

    cur = head;
    int m = len-n;

    while (m > 0 && cur != NULL) {
        prev = cur;
        cur = cur->next;
        m--;
    }

    if (cur != NULL) {
        if (prev != NULL) {
            prev->next = cur->next;
            free(cur);
            cur = NULL;
        } else {
            head = cur->next;
            free(cur);
            cur = NULL;
        }
    }

    return head;
}