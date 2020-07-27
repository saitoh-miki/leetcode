# %% [501. Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/)
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        lst = collections.Counter(to_list(root)).most_common()
        return [i[0] for i in lst if i[1] == lst[0][1]]


def to_list(tn, top=False):
    if tn:
        yield from [tn.val] if top else to_list(tn.left, top)
        yield from to_list(tn.left, top) if top else [tn.val]
        yield from to_list(tn.right, top)
