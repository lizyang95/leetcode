# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

def findCelebrity(self, n):
    x = 0
    for i in xrange(n):
        if knows(x, i):
            x = i
    if any(knows(x, i) for i in xrange(x)):
        return -1
    if any(not knows(i, x) for i in xrange(n)):
        return -1
    return x

    # The key part is the first loop. To understand this you can think the knows(a,b) as a a < b comparison, if a knows b then a < b, if a does not know b, a > b. Then if there is a celebrity, he/she must be the "maximum" of the n people
