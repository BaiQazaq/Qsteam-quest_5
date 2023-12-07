# 10. Implement a queue-based algorithm for a deck shuffling simulation.

from collections import deque
import random

def shuffle_deck(deck):
    if len(deck) <= 1:
        return deck

    queue = deque(deck)
    shuffled_deck = deque()

    while queue:
        # Move a random number of cards from the front of the queue to the back
        random_count = random.randint(1, min(len(queue), 5))
        for _ in range(random_count):
            queue.append(queue.popleft())

        # Move the remaining cards to the shuffled deck
        shuffled_deck.append(queue.popleft())

    return list(shuffled_deck)

# Example usage
if __name__ == "__main__":
    deck = list(range(1, 53))  # Standard deck of 52 cards

    print("Original Deck:", deck)

    shuffled_deck = shuffle_deck(deck)

    print("Shuffled Deck:", shuffled_deck)
