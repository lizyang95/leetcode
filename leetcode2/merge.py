# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)

        result = []

        start = intervals[0].start
        end = intervals[0].end

        for interval in intervals:
            if  interval.start <=end:
                end = max(interval.end, end)
            else:
                result.append(Interval(start,end))
                start=interval.start
                end = interval.end

        result.append(Interval(start,end))
        return result



class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if not intervals:
            return []
        intervallist = [[interval.start,interval.end] for interval in intervals]
        intervallist.sort()

        minval = intervallist[0][0]
        maxval = intervallist[0][1]

        results = []
        for interval in intervallist[1:]:
            # print(results,minval,maxval)
            if interval[0] > maxval:
                results.append([minval,maxval])
                minval = interval[0]
                maxval = interval[1]
            elif interval[0] == maxval:
                maxval = interval[1]
            elif interval[1] >= maxval:
                maxval = interval[1]
            else:
                continue
        results.append([minval,maxval])
        return [Interval(s=interval[0],e=interval[1]) for interval in results]
