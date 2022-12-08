class Solution:

    def search(self, nums: list, target: int) -> int:
        return nums.index(target) if target in nums else -1


data = [
    [-2, 1, 2, 3, 4, 5, 7, 12],
    [-1, 4, 8, 17, 23, 35],
    [],
    [1]
]

for i in data:
    solve = Solution()
    target = 7
    print(solve.search(nums=i, target=target))
