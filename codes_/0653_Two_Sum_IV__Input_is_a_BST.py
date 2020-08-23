# %% [653. Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        return dfs(root, k, set())


def dfs(tn, k, st):
    if not tn:
        return False
    if tn.val in st:
        return True
    st.add(k - tn.val)
    return dfs(tn.left, k, st) or dfs(tn.right, k, st)
