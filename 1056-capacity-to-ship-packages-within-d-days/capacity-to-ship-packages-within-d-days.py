class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def count_days(weight, capacity):
            day, cumulative_weight = 0, 0
            i, j = 0, 0
            while j < len(weight):
                if cumulative_weight + weight[j] <= capacity:
                    cumulative_weight += weight[j]
                else:
                    cumulative_weight = weight[j]
                    day += 1
                    i = j
                j += 1
            return day + 1

        l, r = max(weights), sum(weights)
        capacity = max(weights)
        while l <= r:
            mid = (l+r) // 2
            day = count_days(weights, mid)
            if day <= days:
                capacity = mid
                r = mid - 1
            else:
                l = mid + 1
        return capacity
