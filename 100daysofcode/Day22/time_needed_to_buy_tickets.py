class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        remaining_tickets = tickets[k]
        total_time = 0
        while remaining_tickets > 0:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    total_time += 1
                    if i == k:
                        remaining_tickets -= 1
                        if remaining_tickets == 0:
                            break
        return total_time
