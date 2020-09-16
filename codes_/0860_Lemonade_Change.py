# %% [860. *Lemonade Change](https://leetcode.com/problems/lemonade-change/)
# 問題：すべての支払いでおつりを返せるかどうかを返せ
# 解法：5$と10$の数をカウントする
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a5 = a10 = 0
        for bill in bills:
            if bill == 5:
                a5 += 1
            elif bill == 10:
                a10 += 1
                a5 -= 1
            else:
                if a10:
                    a10 -= 1
                    a5 -= 1
                else:
                    a5 -= 3
            if a5 < 0:
                return False
        return True
