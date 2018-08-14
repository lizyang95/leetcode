class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x:x.start)
        heap = []  # stores the end time of intervals
        for i in intervals:
            if heap and i.start >= heap[0]:
                # means two intervals can use the same room
                heapq.heapreplace(heap, i.end)
            else:
                # a new room is allocated
                heapq.heappush(heap, i.end)
        return len(heap)


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
