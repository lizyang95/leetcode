class  TwoSumTwoSum(object):
	 def  __init__(self):
		self.numDict = collections.defaultdict(int)
		self.minVal = float( 		self.numDict = colle 'inf')
		self.maxVal = float('-inf')

	def add(self, n):
		self.numDict[n] += 1
		self.minVal = min(self.minVal, n)
		self.maxVal = max(self.maxVal, n)

	def find(self, value):
		if value < 2 * self.minVal or value > 2 * self.maxVal:
			return False

		for num in self.numDict:
			target = value - num

			# Check if the target is in the dictionary
			# and it isn't the same value as num
			if target in self.numDict and self.numDict[target] - (target is num):
				return True

		return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
