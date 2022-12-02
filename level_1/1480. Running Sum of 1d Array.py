class Solution:
    def runningSum(self, nums: list) -> list:
        data = []
        for index, val in enumerate(nums): data.append(val) if index == 0 else data.append(val + data[index - 1])
        return data


nums = [1, 1, 1, 1, 1]
# expected [1, 2, 3, 4, 5]
sol = Solution()
print(sol.runningSum(nums=nums))
