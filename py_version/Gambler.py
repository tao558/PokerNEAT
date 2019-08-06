from Card import Card, CardEnum
from MasterDeck import MasterDeck

#TODO: might want to change the name of this class later because its confusing.


class Gambler:
	def __init__(self, master_deck_t):
		self.num_soft_aces = 0
		self.hand = list()
		self.master_deck = master_deck_t  # This is a reference


	# Resets the gambler for another round
	def reset(self):
		self.num_soft_aces = 0
		self.hand.clear()



	def draw_card(self, visible):
		next_card = self.master_deck.give_card()
		next_card.is_visible = visible
		self.hand.append(next_card)
		
		if (next_card.value == CardEnum.HIGH_ACE):
			self.num_soft_aces += 1

		return next_card





