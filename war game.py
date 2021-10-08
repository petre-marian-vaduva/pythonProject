
values = {
    'Two': 2, 'Three': 3, 'Four': 3, 'Five': 3, 'Six': 3, 'Seven': 3, 'Eight': 3, 'Nine': 3, 'Ten': 3,
    'Jack': 3, 'Queen': 3, 'Kind': 3, 'Ace': 3
}

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]
    def __str__(self):
        return self.rank + 'of' + self.suit
