import unittest
from src.deck import Deck


class BlackjackGameTestCase(unittest.TestCase):
    def setUp(self):  # this method will be run before each test
        self.deck = Deck()
        self.player_cards = []
        self.computer_cards = []
        self.player = True

    def tearDown(self):  # this method will be run after each test
        pass

    def test_initial_deal(self):
        self.deck.hand_card(self.player, self.player_cards, self.computer_cards)
        self.deck.hand_card(self.player, self.player_cards, self.computer_cards)

        self.player = False
        self.deck.hand_card(self.player, self.player_cards, self.computer_cards)

        self.assertEqual(len(self.player_cards), 2)
        self.assertEqual(len(self.computer_cards), 1)

    def test_hit_gives_one_card(self):
        initial_cards = len(self.player_cards)
        self.deck.hand_card(True, self.player_cards, self.computer_cards)
        self.assertEqual(len(self.player_cards), initial_cards + 1)

    def test_computer_plays_until_17(self):
        self.player = False
        self.computer_cards = [5]
        while sum(self.computer_cards) < 17:
            self.deck.hand_card(self.player, self.player_cards, self.computer_cards)

        self.assertGreaterEqual(sum(self.computer_cards), 17)

    def test_blackjack_win_condition(self):
        self.player_cards = [10, 11]
        total_player = sum(self.player_cards)
        self.assertEqual(total_player, 21)

    def test_computer_blackjack_win_condition(self):
        self.computer_cards = [10, 11]
        total_computer = sum(self.computer_cards)
        self.assertEqual(total_computer, 21)

    def test_over_21_player(self):
        self.player_cards = [10, 10, 5]
        total_player = sum(self.player_cards)
        self.assertGreater(total_player, 21)

    def test_over_21_computer(self):
        self.computer_cards = [10, 10, 5]
        total_computer = sum(self.computer_cards)
        self.assertGreater(total_computer, 21)
