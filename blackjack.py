from blackjack_helper import *

def start_game_user(starting_hand_value):
  while True:
    if starting_hand_value<21:
      hit_miss = input(f"You have {starting_hand_value}. Hit (y/n)? ")
      if hit_miss.lower() =='y':
        new_card_value = draw_card()
        starting_hand_value += new_card_value
      elif hit_miss.lower() !='n':
        print("Sorry I didn't get that.")
      else:
        print_end_turn_status(starting_hand_value)
        return starting_hand_value
    else:
      print_end_turn_status(starting_hand_value)
      return starting_hand_value

def start_game_dealer(starting_hand_value):
  while True:
    if starting_hand_value < 17:
      print(f"Dealer has {starting_hand_value}.")
      new_card_value = draw_card()
      starting_hand_value += new_card_value
    else:
      print_end_turn_status(starting_hand_value)
      return starting_hand_value
      
if __name__ == '__main__':
  starting_hand_value_user = draw_starting_hand("YOUR")
  user_final_value = start_game_user(starting_hand_value_user)
  
  starting_hand_value_dealer = draw_starting_hand("DEALER")
  dealer_final_value = start_game_dealer(starting_hand_value_dealer)
  
  print_end_game_status(user_final_value, dealer_final_value)


