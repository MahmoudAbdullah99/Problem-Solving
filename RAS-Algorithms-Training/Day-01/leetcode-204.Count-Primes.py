from math import ceil
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0

        prime_list = [False, False] + [True] * (n - 2)
        sqrt_n = ceil(n ** 0.5)
        for i in range(2, ceil(n ** 0.5)):
            if not prime_list[i]: continue

            for j in range(i * i, n, i):
                prime_list[j] = False

        return sum(prime_list)