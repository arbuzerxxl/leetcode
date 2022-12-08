from random import randint


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    if version >= random_int:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:

        begin = 1
        end = n

        while begin != end:
            medium = (begin + end) // 2
            check_medium = isBadVersion(medium)
            check_prev_medium = isBadVersion(medium - 1)

            if check_medium and not check_prev_medium:
                return medium

            if not check_medium:
                begin = medium + 1
                continue
            else:
                end = medium
                continue

        return n


count = 20
random_int = randint(1, count)
print(f"Random: {random_int}")

solve = Solution()
print(solve.firstBadVersion(count))
