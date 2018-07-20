
class Solution(object):
	def countPrimes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# https://www.programcreek.com/2014/04/leetcode-count-primes-java/
		if n < 3:
			return 0
		prime = [1] * n  # 1 to (n - 1)
		prime[0] = 0  # ignore 0
		prime[1] = 0  # 1 is not prime
		for k in range(2, int(n ** 0.5) + 1):  # consider k + 1
			if prime[k] == 1:  # k is prime
				prime[k ** 2: n: k] = [0] * ((n - 1) // k - k + 1)
		return sum(prime)

sol = Solution()
print(sol.countPrimes(10))
