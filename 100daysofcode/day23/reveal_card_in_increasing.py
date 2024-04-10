class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        
        # Initialize a queue with indices of the sorted deck
        indices = deque(range(len(deck)))
        
        # Initialize a result array
        result = [0] * len(deck)
        
        # Iterate through the sorted deck
        for card in deck:
            # Place the first card at the top of the deck
            result[indices.popleft()] = card
            
            # Move the next card to the bottom of the deck
            if indices:
                indices.append(indices.popleft())
        
        return result 
