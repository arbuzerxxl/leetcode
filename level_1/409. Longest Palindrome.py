class Solution:
    def longestPalindrome(self, s: str) -> int:

        string_map = {}
        not_even = False
        output = 0

        for i in s:
            if not string_map.get(i):
                string_map.setdefault(i, 1)
            else:
                string_map[i] += 1

        for value in string_map.values():
            if value % 2 == 0:
                output += value
            else:
                output += value - 1
                not_even = True

        if not_even:
            return output + 1
        else:
            return output


data = ["abb",
        'abccccdd',
        'a',
        "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth",
        ]


solve = Solution()

for i in data:
    print(solve.longestPalindrome(s=i))