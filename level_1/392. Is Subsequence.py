class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s and not t:
            return True

        if not s:
            return True

        if not t:
            return False

        counter = len(s)

        for i in t:
            if i == s[-counter]:
                counter -= 1
                if counter < 0:
                    break
                continue
            else:
                continue

        return counter == 0


data = [('abc', 'ahbgdc'),
        ('axc', 'ahbgdc'),
        ]

solve = Solution()
for item in data:
    print(solve.isSubsequence(s=item[0], t=item[1]))
