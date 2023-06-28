#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list. */
struct ListNode {
    int val;
    struct ListNode *next;
};

/* Function to reverse a linked list. */
struct ListNode *reverseList(struct ListNode *head) {
    struct ListNode *prev = NULL;
    struct ListNode *curr = head;
    struct ListNode *next = NULL;

    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    return prev;
}

/* Function to check if a singly linked list is a palindrome. */
bool isPalindrome(struct ListNode* head) {
    /* Count the number of nodes in the linked list. */
    int count = 0;
    struct ListNode *current = head;
    while (current != NULL) {
        count++;
        current = current->next;
    }

    /* If the list has 0 or 1 nodes, it is a palindrome. */
    if (count == 0 || count == 1) {
        return true;
    }

    /* Find the middle node of the linked list. */
    int mid = count / 2;
    current = head;
    for (int i = 0; i < mid; i++) {
        current = current->next;
    }

    /* Reverse the second half of the linked list. */
    struct ListNode *secondHalf = reverseList(current);

    /* Compare the first half of the linked list with the reversed second half. */
    struct ListNode *firstHalf = head;
    for (int i = 0; i < mid; i++) {
        if (firstHalf->val != secondHalf->val) {
            return false;
        }
        firstHalf = firstHalf->next;
        secondHalf = secondHalf->next;
    }

    return true;
}
