from src.deck import Deck
from src.art import logo

def play():
    deck = Deck()
    player = True
    player_cards = []
    computer_cards = []

    print(logo)
    deck.hand_card(player, player_cards, computer_cards)
    deck.hand_card(player, player_cards, computer_cards)

    player = False
    deck.hand_card(player, player_cards, computer_cards)

    initial_q = input("Do you want to play Blackjack? Type 'y' or 'n': " + "\n")

    if initial_q.lower() == 'y':
        while True:
            total_player = sum(player_cards)
            total_computer = sum(computer_cards)
            print(f"Your cards: {player_cards}, current score: {total_player}" + "\n")
            print(f"Computer's first card: {computer_cards}" + "\n")
            player = True

            if total_player == 21:
                print("YOU GOT 21! YOU WON!!!!" + "\n")
                break
            if total_player > 21:
                print("YOU WENT OVER 21! YOU LOST!" + "\n")
                break

            another_card = input("Type 'hit' to HIT, or 'stand' to STAND: " + "\n")

            if another_card.lower() == 'hit':
                deck.hand_card(player, player_cards, computer_cards)
                if total_player == 21:
                    print("YOU GOT 21! You WON!!!!" + "\n")
                    break
            else:
                player = False
                while total_computer < 17:
                    deck.hand_card(player, player_cards, computer_cards)
                    total_computer = sum(computer_cards)
                    if total_computer == 21:
                        print("COMPUTER 21! YOU LOST!!!!" + "\n")
                        break

                print(f"Your final cards: {player_cards}, final score: {total_player}" + "\n")
                print(f"Computer's final hand: {computer_cards}, final score: {total_computer}" + "\n")

                if total_computer > 21:
                    print("COMPUTER WENT OVER 21! YOU WON!" + "\n")
                    break

                deck.check_win(player_cards, computer_cards)
                break
    else:
        print("No worries. Goodbye!")





if __name__ == '__main__':
    play()

