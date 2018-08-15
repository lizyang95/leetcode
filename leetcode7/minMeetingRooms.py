# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Think about e as a pointer to the first available room.
class Solution(object):
    def minMeetingRooms(self, intervals):
            e = ret = 0
            start = sorted(i.start for i in intervals)
            end = sorted(i.end for i in intervals)

            for s in range(len(start)):
                if start[s] < end[e]:
                    ret += 1
                else:
                    e += 1
            return ret
