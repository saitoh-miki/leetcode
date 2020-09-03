# %% [733. Flood Fill](https://leetcode.com/problems/flood-fill/)
# 問題：imageを(sr, sc)の位置からnewColorで塗りつぶせ
# 解法：未処理リストを管理する
class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        n, m, p, t = len(image), len(image[0]), image[sr][sc], [(sr, sc)]
        if p == newColor:
            return image
        while t:
            x, y = t.pop()
            image[x][y] = newColor
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if 0 <= (a := x + dx) < n and 0 <= (b := y + dy) < m:
                    if image[a][b] == p:
                        t.append((a, b))
        return image
