# %% [637. Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/)
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        return list(bfs([root]))


def bfs(lst):
    vals, chlds = [], []
    for tn in lst:
        if tn:
            vals.append(tn.val)
            chlds.extend([tn.left, tn.right])
    if vals:
        yield sum(vals) / len(vals)
        yield from bfs(chlds)
