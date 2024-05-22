class Solution:
    def findSmallestMaxDist(self, stations, K):
        # Code here
        def possible(distance):
            stations_to_add = 0
            for i in range(len(stations)-1):
                stations_to_add += math.floor((stations[i+1] - stations[i])/distance)
            return stations_to_add <= K

        left = 0
        right = stations[-1] - stations[0]
        while right-left > 1e-6:
            mid = left + (right - left)/2.0
            if possible(mid):
                right = mid
            else:
                left = mid
        return right
