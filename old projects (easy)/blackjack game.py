
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def dealer():
    dealer_cards = []
    #we append twice for two cards.
    dealer_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
    return dealer_cards
#dealer actions should only execute if the player chooses to stand.
def dealer_actions(dealer_cards, actions):
    if sum(dealer_cards) <= 17:
        dealer_cards.append(random.choice(cards))
        if sum(dealer_cards) > 21:
            if 11 in dealer_cards:
              dealer_cards[dealer_cards.index(11)] = 1
        return dealer_cards
    else:
        return dealer_cards

def player():
    player_cards = []
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    return player_cards

def actions(player_cards, dealer_cards):
   player_actions = input("would you like to hit or stand? H or S: ").lower()
   if player_actions == "h":
        player_cards.append(random.choice(cards))
        return player()
   elif player_actions == "s":
        dealer_cards = dealer_actions(dealer_cards, player_cards)
        return dealer_cards
   elif sum(player_cards) > 21:
        if 11 in player_cards:
            player_cards[player_cards.index(11)] = 1
            return player()
   elif len(player_cards) < 5:
       return actions(player_cards, dealer_cards)
   else:
        print("Invalid input. Please try again.")
        return actions(player_cards, dealer_cards)
    
#a function to compare the sum of the cards and determine the winner.
def determining_outcome(player_cards, dealer_cards):
    if sum(player_cards) == sum(dealer_cards):
        print(f"push - player: {player_cards}, dealer: {dealer_cards}")
    elif sum(player_cards) == 21:
        print(f"Player wins! - player: {player_cards}, dealer: {dealer_cards}")
    elif sum(dealer_cards) == 21:
        print(f"Dealer wins! - player: {player_cards}, dealer: {dealer_cards}")
    elif sum(player_cards) > 21:
        print(f"Bust! - player: {player_cards}, dealer: {dealer_cards}")
    elif sum(dealer_cards) > 21:
        print(f"Dealer bust! - player: {player_cards}, dealer: {dealer_cards}")
    elif 11 in dealer_cards and sum(dealer_cards) == 21:
        print(f"Dealer BlackJack! - player: {player_cards}, dealer: {dealer_cards}")
    elif 11 in player_cards and sum(player_cards) == 21:
        print(f"Player BlackJack! - player: {player_cards}, dealer: {dealer_cards}")
    elif 11 in dealer_cards and any(card in player_cards for card in [10]):
        print(f"Dealer BlackJack! Dealer Wins! - player: {player_cards}, dealer: {dealer_cards}")
    elif sum(player_cards) > sum(dealer_cards):
        print(f"Player wins! - player: {player_cards}, dealer: {dealer_cards}")
    else:
        print(f"Dealer wins! - player: {player_cards}, dealer: {dealer_cards}")

def game_rules(player_cards, dealer_cards):
    

#function to ask if the player wants to play again when the game is over.    
  def play_again():
      play_again = input("Would you like to play again? Y or N: ").lower()
      if play_again == "y":
        play_game()
      else:
        print("Thank you for playing!")
        return
    
def play_game():
    print("Welcome to the annual underground blackjack tournament!")
    start_game = input("Would you like to start the game? Y or N: ").lower()
    
    while start_game == "y":
        player_cards = player()
        dealer_cards = dealer()
        print(f"player cards: {player_cards}")
        print(f"dealer cards: {dealer_cards[0]}")
        num_cards = 0

        for _ in range(1):
            if num_cards >= 5 or sum(player_cards) > 21:
                break
            if len(player_cards) < 5 and sum(player_cards) < 21:
              actions(player_cards, dealer_cards)
              print(f"player cards: {player_cards}")
              print(f"dealer cards: {dealer_cards[0]}")
              continue
            while actions == "s" or sum(dealer_cards) <= 17 or sum(player_cards) > 21:
              dealer_actions(dealer_cards, player_cards)
              
            game_rules(player_cards, dealer_cards)
            num_cards += 1
        determining_outcome(player_cards, dealer_cards)
        start_game = input("Would you like to play again? Y or N: ").lower()
    else:
        print("Thank you for playing!")
        return
    play_again()
play_game()