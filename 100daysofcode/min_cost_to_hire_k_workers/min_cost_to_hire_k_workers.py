class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted((w / q, q) for w, q in zip(wage, quality))
        ans = float('inf')
        sum_q = 0
        pq = []

        for wage_per_quality, q in workers:
            heapq.heappush(pq, -q)
            sum_q += q

            if len(pq) > k:
                sum_q += heapq.heappop(pq)

            if len(pq) == k:
                ans = min(ans, sum_q * wage_per_quality)

        return ans
