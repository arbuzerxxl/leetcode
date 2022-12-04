class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        string_map = {}

        s_data = []
        t_data = []

        for index, val in enumerate(s):

            if val in string_map:
                s_data.append(string_map[val])
                s_data[string_map[val]] = string_map[val]
            else:
                string_map[val] = index
                s_data.append(None)

        string_map.clear()

        for index, val in enumerate(t):

            if val in string_map:
                t_data.append(string_map[val])
                t_data[string_map[val]] = string_map[val]
            else:
                string_map[val] = index
                t_data.append(None)

        return s_data == t_data


data = [('egg', 'add'),
        ('foo', 'bar'),
        ('paper', 'title'),
        ("aaeaa", "uuxyy"),
        ("aab", "aaa")

        ]

iso = Solution()
for item in data:
    print(iso.isIsomorphic(s=item[0], t=item[1]))
