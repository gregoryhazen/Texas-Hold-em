import random

class Card:
	numbers_to_values = {
		12: "ACE",
		0: "TWO",
		1: "THREE",
		2: "FOUR",
		3: "FIVE",
		4: "SIX",
		5: "SEVEN",
		6: "EIGHT",
		7: "NINE",
		8: "TEN",
		9: "JACK",
		10: "QUEEN",
		11: "KING"
	}
	
	numbers_to_suits = {
		3: "SPADES",
		2: "CLUBS",
		1: "DIAMONDS",
		0: "HEARTS"
	}

	values_to_numbers = {
		"ACE": 12,
		"TWO": 0,
		"THREE": 1,
		"FOUR": 2,
		"FIVE": 3,
		"SIX": 4,
		"SEVEN": 5,
		"EIGHT": 6,
		"NINE": 7,
		"TEN": 8,
		"JACK": 9,
		"QUEEN": 10,
		"KING": 11
	}

	suits_to_numbers = {
		"SPADES": 3,
		"CLUBS": 2,
		"DIAMONDS": 1,
		"HEARTS": 0
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
		return self

class Deck:
	def __init__(self, id):
		self.id = id
		self.deck = []
		for x in range(52):
			self.deck.append(Card(self.id.get_value_hash(x), self.id.get_suit_hash(x)))

	def get_id(self):
		return self.id

	def deal(self):
		return self.deck.pop(random.randint(0, len(self.deck) - 1))

class Hand:
	def __init__(self):
		self.hand = []

	def draw(self, deck):
		self.hand.append(deck.deal())

	def __str__(self):
		str = ""
		for x in self.hand:
			str += x.__str__() + ", "
		return str[:len(str) - 2]

	def compare_vals(self, hand):
		card = self.hand[0]
		for x in self.hand:
			card = card.compare(x)
		for x in hand.hand:
			if card.compare(x) == x:
				return hand
		return self

class __main__:
	deck = Deck(Card("ACE", "SPADES"))
	player1 = Hand()
	player2 = Hand()

	player1.draw(deck)
	player2.draw(deck)
	player1.draw(deck)
	player2.draw(deck)
	player1.draw(deck)
	player2.draw(deck)

	print player1
	print player2
	print
	print
	print player1.compare_vals(player2)