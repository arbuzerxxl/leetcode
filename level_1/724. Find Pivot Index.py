class Solution:
    def pivotIndex(self, nums: list) -> int:
        leftsum = 0
        for index, val in enumerate(nums):
            if index == 0 and sum(nums[1:]) == 0:
                return 0
            elif leftsum == sum(nums[(index + 1):]):  # медленно из-за 2 sum!
                return index
            leftsum += val
        return -1


# class Solution(object):
#     def pivotIndex(self, nums):
#         S = sum(nums)
#         leftsum = 0
#         for i, x in enumerate(nums):
#             if leftsum == (S - leftsum - x):
#                 return i
#             leftsum += x
#         return -1


nums = [
    [1, 7, 3, 6, 5, 6],
    [1, 2, 3],
    [2, 1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, 1, 1, 1],
    [-1, -1, 0, 1, 1, -1]
]

sol = Solution()

for i in nums:
    print(sol.pivotIndex(nums=i))
