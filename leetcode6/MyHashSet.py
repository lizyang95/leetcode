class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset={}

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.hashset[key]=True


    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.hashset[key]=False


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.hashset[key] if key in self.hashset else False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
