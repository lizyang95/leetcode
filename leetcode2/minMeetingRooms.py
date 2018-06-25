 # Very similar with what we do in real life. Whenever you want to start a meeting,
 # you go and check if any empty room available (available > 0) and
 # if so take one of them ( available -=1 ). Otherwise,
 # you need to find a new room someplace else ( numRooms += 1 ).
 # After you finish the meeting, the room becomes available again ( available += 1 ).

 def minMeetingRooms(self, intervals):
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()
        s = e = 0
        numRooms = available = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                if available == 0:
                    numRooms += 1
                else:
                    available -= 1

                s += 1
            else:
                available += 1
                e += 1

        return numRooms

    def minMeetingRooms(self, intervals):
        # import headpq
        # intervals.sort(key=lambda x:x.start)
        # heap = []  # stores the end time of intervals
        # for i in intervals:
        #     if heap and i.start >= heap[0]:
        #         # means two intervals can use the same room
        #         heapq.heapreplace(heap, i.end)
        #     else:
        #         # a new room is allocated
        #         heapq.heappush(heap, i.end)
        # return len(heap)
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x.start)
        rooms, maxRoomNeed = [], 1
        heapq.heappush(rooms, intervals[0].end)
        for i in range(1, len(intervals)):
            if intervals[i].start >= rooms[0]:
                heapq.heappushpop(rooms, intervals[i].end)
            else:
                heapq.heappush(rooms, intervals[i].end)
                maxRoomNeed = max(maxRoomNeed, len(rooms))
        return maxRoomNeed
