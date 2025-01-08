import unittest
from src.deck import Deck


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()
        self.player_cards = []
        self.computer_cards = []
        self.player = True

    def tearDown(self):  # this method will be run after each test
        pass

    def test_number_of_cards(self):  # any method beginning with 'test_' will be run by unittest
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 13)

    def test_opening_hand_has_two_cards(self):
        self.deck.hand_card(self.player, self.player_cards, self.computer_cards)
        self.deck.hand_card(self.player, self.player_cards, self.computer_cards)
        self.assertEqual(len(self.player_cards), 2)

    def test_player_over_21(self):
        self.player_cards = [10, 10, 2]
        result = self.deck.check_over_21(self.player_cards, True)
        self.assertTrue(sum(self.player_cards) > 21)

    def test_computer_over_21(self):
        self.computer_cards = [10, 10, 5]
        result = self.deck.check_over_21(self.computer_cards, False)
        self.assertTrue(sum(self.computer_cards) > 21)

    def test_player_wins_with_higher_score(self):
        self.player_cards = [10, 8]
        self.computer_cards = [10, 5]
        result = self.deck.check_win(self.player_cards, self.computer_cards)
        self.assertTrue(sum(self.player_cards) > sum(self.computer_cards))

    def test_draw_with_equal_scores(self):
        self.player_cards = [10, 5]
        self.computer_cards = [10, 5]
        result = self.deck.check_win(self.player_cards, self.computer_cards)
        self.assertEqual(sum(self.player_cards), sum(self.computer_cards))

    def test_computer_wins_with_higher_score(self):
        self.player_cards = [10, 5]  # 15
        self.computer_cards = [10, 8]  # 18
        result = self.deck.check_win(self.player_cards, self.computer_cards)
        self.assertTrue(sum(self.computer_cards) > sum(self.player_cards))


if __name__ == '__main__':
    unittest.main()
