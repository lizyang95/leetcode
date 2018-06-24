class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True



class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)

        start = intervals[0].start
        end = intervals[0].end

        for interval in intervals[1:]:
            if interval.start >= end:
                start = interval.start
                end = interval.end
            else:
                return False
        return True
