from src.deck import Deck


def play():
    deck = Deck()
    player = True
    player_cards = []
    computer_cards = []

    deck.hand_card(player, player_cards, computer_cards)
    deck.hand_card(player, player_cards, computer_cards)

    player = False
    deck.hand_card(player, player_cards, computer_cards)

    initial_q = input("Do you want to play Blackjack? Type 'y' or 'n': ")
    print(initial_q)

    if initial_q.lower() == 'y':
        while True:
            total_player = sum(player_cards)
            total_computer = sum(computer_cards)
            print(f"Your cards: {player_cards}, current score: {total_player}")
            print(f"Computer's first card: {computer_cards}")
            player = True

            if total_player == 21:
                print("You got 21! You WON!!!!")
                break
            if total_player > 21:
                print("You went over 21! You lost!")
                break

            another_card = input("Type 'hit' to HIT, or 'stand' to STAND: ")
            print(another_card)

            if another_card.lower() == 'hit':
                #player continues drawing
                deck.hand_card(player, player_cards, computer_cards)
                if total_player == 21:
                    print("You got 21! You WON!!!!")
                    break
            else:
                #computer plays
                player = False
                while total_computer < 17:
                    deck.hand_card(player, player_cards, computer_cards)
                    total_computer = sum(computer_cards)
                    if total_computer == 21:
                        print("Computer got 21! You LOST!!!!")
                        break

                print(f"Your final cards: {player_cards}, final score: {total_player}")
                print(f"Computer's final hand: {computer_cards}, final score: {total_computer}")

                if total_computer > 21:
                    print("Computer went over 21! You WON!")
                    break

                deck.check_win(player_cards, computer_cards)
                break
    else:
        print("No worries. Goodbye!")





if __name__ == '__main__':
    play()

