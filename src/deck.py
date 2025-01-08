from random import choice

class Deck:
    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def hand_card(self, player, player_cards, computer_cards):
        random_card = choice(self.cards)
        if player:
            player_cards.append(random_card)
        else:
            computer_cards.append(random_card)

    def check_over_21(self, array, player):
        if player:
            if sum(array) > 21:
                print("You went over! You lost!")
                print("\n" * 3)
        else:
            print("Computer went over! You win")
            print("\n" * 3)

    def check_win(self, player_arr, comp_arr):
        if sum(player_arr) > sum(comp_arr):
            print("CONGRATULATIONS! YOU WIN")
        elif sum(player_arr) == sum(comp_arr):
            print("OH DEAR, IT'S A DRAW!")
        else:
            print("COMPUTER WON! BETTER LUCK NEXT TIME")
