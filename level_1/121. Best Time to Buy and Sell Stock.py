class Solution:
    def maxProfit(self, prices: list) -> int:

        save_price = float('inf')
        profit = 0

        for price in prices:

            if price < save_price:
                save_price = price
                continue

            elif price > save_price:
                if price - save_price > profit:
                    profit = price - save_price

        return profit


prices = [
    [7, 1, 5, 3, 6, 4],
    [7, 6, 4, 3, 1],
    [2, 4, 1],
    [2, 1, 2, 1, 0, 1, 2],
    [3, 2, 6, 5, 0, 3],
    [2, 11, 1, 4, 7]
]


solve = Solution()
for i in prices:
    print(solve.maxProfit(prices=i))
