# %% [874. Walking Robot Simulation](https://leetcode.com/problems/walking-robot-simulation/)
# 問題：移動経路中の原点からの最大距離の2乗を返せ
# 解法：obstaclesをsetに変換する
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        mx, x, y, dr, dd = 0, 0, 0, 0, [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstacles = set(map(tuple, obstacles))
        for com in commands:
            if com < 0:
                dr = (dr + com * 2 + 3) % 4
            else:
                for _ in range(com):
                    nx, ny = x + dd[dr][0], y + dd[dr][1]
                    if (nx, ny) not in obstacles:
                        x, y = nx, ny
                mx = max(mx, x * x + y * y)
        return mx
