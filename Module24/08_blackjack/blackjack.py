class Card:

    values = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Валет': 10,
        'Дама': 10,
        'Король': 10,
        'Туз': 11
    }

    suits = ['черви', 'пики', 'бубны', 'крести']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class Deck:

    def __init__(self):
        self.deck = [
            Card(value, suit) for value in Card.values for suit in Card.suits
        ]

    def remove_card(self, index):
        return self.deck.pop(index)

    # Служебный метод
    def show_deck(self):
        print()
        for card in self.deck:
            print(card.value, card.suit)


class Human:

    def __init__(self):
        self.cards = []

    def get_card(self, current_deck, index):
        self.cards.append(current_deck.remove_card(index))

    def calculate_points(self):
        total_points = 0
        is_there_ace = False
        for card in self.cards:
            if card.value == 'Туз':
                is_there_ace = True
            total_points += card.values[card.value]
            if (total_points > 21) and is_there_ace:
                total_points -= 10
                is_there_ace = False
        return total_points

    def show_cards(self):
        for card in self.cards:
            print('\t{} {}'.format(card.value, card.suit))
