import random

class Card:
	numbers_to_values = {
		0: "ACE",
		1: "TWO",
		2: "THREE",
		3: "FOUR",
		4: "FIVE",
		5: "SIX",
		6: "SEVEN",
		7: "EIGHT",
		8: "NINE",
		9: "TEN",
		10: "JACK",
		11: "QUEEN",
		12: "KING"
	}
	
	numbers_to_suits = {
		0: "SPADES",
		1: "CLUBS",
		2: "DIAMONDS",
		3: "HEARTS"
	}

	values_to_numbers = {
		"ACE": 0,
		"TWO": 1,
		"THREE": 2,
		"FOUR": 3,
		"FIVE": 4,
		"SIX": 5,
		"SEVEN": 6,
		"EIGHT": 7,
		"NINE": 8,
		"TEN": 9,
		"JACK": 10,
		"QUEEN": 11,
		"KING": 12
	}

	suits_to_numbers = {
		"SPADES": 0,
		"CLUBS": 1,
		"DIAMONDS": 2,
		"HEARTS": 3
	}

	def __init__(self, value, suit):
		self.value = self.values_to_numbers[value]
		self.suit = self.suits_to_numbers[suit]

	def get_value(self):
		return self.numbers_to_values[self.value]

	def get_suit(self):
		return self.numbers_to_suits[self.suit]

	def get_value_number(self):
		return self.value

	def get_suit_number(self):
		return self.suit

	def get_hash(self):
	 	return self.suit * 14 + self.value

	def get_value_hash(self, hash):
		return self.numbers_to_values[hash % 13]

	def get_suit_hash(self, hash):
		return self.numbers_to_suits[hash / 13]

	def __str__(self):
		return self.numbers_to_values[self.value] + " of " + self.numbers_to_suits[self.suit]

	def compare(self, card):
		if self.value > card.value:
			return self
		elif self.value < card.value:
			return card
		elif self.value == card.value:
			if self.suit > card.suit:
				return self
			elif self.suit < card.suit:
				return card
			else:
				return None

class Deck:
	def __init__(self, id):
		self.id = id
		self.deck = []
		for x in range(52):
			self.deck.append(Card(self.id.get_value_hash(x), self.id.get_suit_hash(x)))

	def get_id(self):
		return self.id

	def deal(self):
		return self.deck.pop(random.randint(0, len(self.deck)))

class Hand:
	def __init__(self):
		self.hand = []

	def draw(self, deck):
		self.hand.append(deck.deal())

class __main__:
	deck = Deck(Card("ACE", "SPADES"))
	hand = Hand()

	hand.draw(deck)
	hand.draw(deck)

	print hand.hand[0].compare(hand.hand[1])
	