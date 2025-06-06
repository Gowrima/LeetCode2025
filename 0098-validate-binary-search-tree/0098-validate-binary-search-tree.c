#include <limits.h>
#include <stdbool.h>

bool isValidBST_helper(struct TreeNode* root, long min, long max) {
    if (root == NULL) return true;

    if (root->val <= min || root->val >= max) {
        return false;
    }

    return isValidBST_helper(root->left, min, root->val) &&
           isValidBST_helper(root->right, root->val, max);
}

bool isValidBST(struct TreeNode* root) {
    return isValidBST_helper(root, LONG_MIN, LONG_MAX);
}
