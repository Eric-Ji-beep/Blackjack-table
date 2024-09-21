import machine
import utime
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from neopixel import Neopixel


pixels = Neopixel(30, 2, 2, 'GRB') # FOR REFERENCE ONLY
pixels.fill((0,0,0))

pixels.show()

"""
pixels.fill((255, 0, 0))
pixels.brightness(100)
pixels.show()
pixels.fill(0,0,0) # turn off
"""

def light_up(r,g,b):
    pixels.fill((r,g,b))
    pixels.brightness(100)
    pixels.show()

"""
light_up(255,0,0) # red
light_up(0,255,0) # green
light_up(0,0,255) # blue
"""
#light_up(10, 81, 255) # neon blue
#light_up(0,150,250)


I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

def greeting():

    lcd.clear()
    lcd.move_to(5,0)
    lcd.putstr("Paramjot")
    lcd.move_to(3,1)
    lcd.putstr("Dhaliwal")
    utime.sleep(2)
    lcd.clear()




def customcharacter():

  #spade      
  lcd.custom_char(0, bytearray([
  0x00,
  0x04,
  0x0E,
  0x1F,
  0x1F,
  0x04,
  0x0E,
  0x00

        ]))

  #heart      
  lcd.custom_char(1, bytearray([
  0x00,
  0x0A,
  0x1F,
  0x1F,
  0x1F,
  0x0E,
  0x04,
  0x00

        ]))




  #diamond
  lcd.custom_char(2, bytearray([
  0x00,
  0x04,
  0x0E,
  0x1F,
  0x1F,
  0x0E,
  0x04,
  0x00

        ]))

  #heart
  lcd.custom_char(3, bytearray([
   0x00,
  0x00,
  0x0A,
  0x15,
  0x11,
  0x0A,
  0x04,
  0x00

        ]))

      #club
  lcd.custom_char(4, bytearray([
  0x00,
  0x0E,
  0x0E,
  0x1F,
  0x1F,
  0x04,
  0x04,
  0x00

        ]))
    #celcius
  lcd.custom_char(5, bytearray([
  0x07,
  0x05,
  0x07,
  0x00,
  0x00,
  0x00,
  0x00,
  0x00

        ])) 






#greeting()    
#customcharacter()
"""
lcd.move_to(0,0)
lcd.putstr("Custom Character")
lcd.move_to(0,1)
lcd.putchar(chr(0))
lcd.move_to(4,1)
lcd.putchar(chr(1))
lcd.move_to(8,1)
lcd.putchar(chr(2))
lcd.move_to(12,1)
lcd.putchar(chr(3))
lcd.move_to(15,1)
lcd.putchar(chr(4))
"""

def print_to_screen(x_coord, y_coord, phrase):
    # Method to print a phrase to lcd screen
    # x_coord: x-coordinate of print on screen
    # y_coord: y-coordinate of print on screen
    lcd.clear()
    lcd.move_to(x_coord, y_coord)
    lcd.putstr(phrase)
    utime.sleep(3) # 3 second delay to allow for better viewing experience

customcharacter() # set up and define the custom characters
def print_to_screen_char(x_coord1, x_coord2, phrase_top, phrase_bottom, character, char_x):
    # character: char number defined in list above
    # char_x: position of character along x-axis
    lcd.clear()
    lcd.move_to(x_coord1, 0)
    lcd.putstr(phrase_top)

    lcd.move_to(x_coord2, 1)
    lcd.putstr(phrase_bottom)
    lcd.move_to(char_x,1)
    lcd.putchar(chr(character))
    utime.sleep(3)
    # ADD IF STATEMENTS TO ALTER THE PLACEMENT OF CARD SYMBOL
def char_cor(card_val):
  if card_val == 'ACE':
      return 9

  elif card_val == 'KING':
      return 10

  elif card_val == 'JACK':
      return 10

  elif card_val == 'QUEEN':
      return 10

  elif card_val == '10':
      return 9

  else:
      return 8
def val_cor(card_val):
  if card_val == 'ACE':
      return 6

  elif card_val == 'JACK':
      return 6

  elif card_val == 'KING':
      return 6

  elif card_val == 'QUEEN':
      return 5

  elif card_val == '10':
      return 7

  else:
      return 7














from machine import Pin
import utime


button1_pin = Pin(15, Pin.IN, Pin.PULL_DOWN)  # Adjust pin number as needed
button2_pin = Pin(14, Pin.IN, Pin.PULL_DOWN)  # Adjust pin number as needed

def is_button_pressed(button_pin):
    """
    Returns True if the button is pressed, False otherwise.
    """
    return button_pin.value() == 1

def button_pressed():
    #button_pin = Pin(1, Pin.IN, Pin.PULL_DOWN)  # Adjust pin number as needed

    try:
        while True:
            if is_button_pressed(button1_pin):
                return True
            if is_button_pressed(button2_pin):
                return False
            utime.sleep(0.2)
    except KeyboardInterrupt:
        pass


#if __name__ == "__main__":
    #main()

###################################################################################################################




# Register board to network:
import network
import ubinascii

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
#print(mac)

# Connect to WIFI:
import time
ssid = 'airuc-guest' # This should be ‘airuc-guest’ on campus Wi-Fi
# password = 'YOUR WIFI PASSSWORD HERE'
def connect():
    # Connect to WLAN
    # Connect function from https://projects.raspberrypi.org/en/projects/get-started-pico-w/2
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid) # Remove password if using airuc-guest

    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
try:
    connect()
except KeyboardInterrupt:
    machine.reset()

print('Connected. End of code.')
##################################################################################################

# Define Deck and Use API:
import requests
import machine
response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6")
deck = response.json()
deck_id = deck['deck_id']
###################################################################
def draw_card(is_dealer): # is_dealer is True if card is for dealer, False if for player
  card_drawn_link = "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=1"
  card_drawn_api = requests.get(card_drawn_link)
  card_drawn = card_drawn_api.json()
  value = card_drawn['cards'][0]['value']
  suit = card_drawn['cards'][0]['suit']

  if is_dealer == True:
    if card_drawn['cards'][0]['suit'] == 'HEARTS':
        print_to_screen_char(0,val_cor(value),"Dealer's card is ", card_drawn['cards'][0]['value'],1,char_cor(card_drawn['cards'][0]['value']))
    if card_drawn['cards'][0]['suit'] == 'SPADES':
        print_to_screen_char(0,val_cor(value),"Dealer's card is ", card_drawn['cards'][0]['value'],0,char_cor(card_drawn['cards'][0]['value']))
    if card_drawn['cards'][0]['suit'] == 'DIAMONDS':
        print_to_screen_char(0,val_cor(value),"Dealer's card is ", card_drawn['cards'][0]['value'],2,char_cor(card_drawn['cards'][0]['value']))
    if card_drawn['cards'][0]['suit'] == 'CLUBS':
        print_to_screen_char(0,val_cor(value),"Dealer's card is ", card_drawn['cards'][0]['value'],4,char_cor(card_drawn['cards'][0]['value']))
    print(f"Dealer's card is {card_drawn['cards'][0]['value']} of {card_drawn['cards'][0]['suit']}")
    """
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr(f"Dealer's card is {card_drawn['cards'][0]['value']} of {card_drawn['cards'][0]['suit']}")
    utime.sleep(3)
    """
  else:

    if card_drawn['cards'][0]['suit'] == 'HEARTS':
        print_to_screen_char(0,val_cor(value),"  Your card is", card_drawn['cards'][0]['value'],1,char_cor(card_drawn['cards'][0]['value']))
    if card_drawn['cards'][0]['suit'] == 'SPADES':
        print_to_screen_char(0,val_cor(value),"  Your card is", card_drawn['cards'][0]['value'],0,char_cor(card_drawn['cards'][0]['value']))
    if card_drawn['cards'][0]['suit'] == 'DIAMONDS':
        print_to_screen_char(0,val_cor(value),"  Your card is", card_drawn['cards'][0]['value'],2,char_cor(card_drawn['cards'][0]['value']))
    if card_drawn['cards'][0]['suit'] == 'CLUBS':
        print_to_screen_char(0,val_cor(value),"  Your card is ", card_drawn['cards'][0]['value'],4,char_cor(card_drawn['cards'][0]['value']))
    print(f"Your card is {card_drawn['cards'][0]['value']} of {card_drawn['cards'][0]['suit']}")

  card = card_drawn['cards'][0]['value']
  # Convert values of card to numbers:
  if card == 'ACE':
    card = 11
  elif card == 'JACK':
    card = 10
  elif card == 'QUEEN':
    card = 10
  elif card == 'KING':
    card = 10
  else:
    card = int(card)
  return card # Returns numerical value of card


def start_game():
  print_to_screen(0,0,"Game Starting...")
  light_up(211,211,211) # light grey

  print("Game Starting...")
  dealers_hand.append(draw_card(True))
  players_hand.append(draw_card(False))
  players_hand.append(draw_card(False))
  utime.sleep(2)
  sum_player = sum_players_hand(players_hand)
  sum_dealer = sum_players_hand(dealers_hand)
  print_to_screen(0,0,"Player total:"+ str(sum_player) +" Dealer total:"+ str(sum_dealer))
  print('\nYour total is:', sum_players_hand(players_hand), '\n')


def sum_players_hand(hand):
  sum = 0
  for card in hand:
    sum += card
  return sum


def game_result():
  print_to_screen(5,0,'Stand')
  print('Stand')
  sum_player = sum_players_hand(players_hand)
  dealers_hand.append(draw_card(True)) # Give dealer second card
  sum_dealer = sum_players_hand(dealers_hand)

  while sum_dealer < 17:
    print("\nDealer's total:", sum_players_hand(dealers_hand), '\n')
    dealers_hand.append(draw_card(True))
    sum_dealer = sum_players_hand(dealers_hand)

  utime.sleep(2)
  print_to_screen(0,0,"Player total:"+ str(sum_player) +" Dealer total:"+ str(sum_dealer))
  print('Your hand totals', sum_player)
  print("Dealer's hand totals", sum_dealer)
  

  if sum_player == 21:
    if sum_dealer == 21:
      print_to_screen(0,0,'PUSH')
      print('PUSH')
      light_up(10, 81, 255) # neon blue
    else:
      print_to_screen(0,0,'WIN!')
      print('WIN!')
      light_up(0,255,0) # green
  elif sum_player < 21:
    if sum_dealer > 21:
      print_to_screen(0,0,'WIN!')
      print('WIN!')
      light_up(0,255,0) # green
    elif sum_player > sum_dealer:
      print_to_screen(0,0,'WIN!')
      print('WIN!')
      light_up(0,255,0) # green
    elif sum_player < sum_dealer:
      print_to_screen(0,0,'LOSE')
      print('LOSE')
      light_up(255,0,0) # red
    elif sum_player == sum_dealer:
      print_to_screen(0,0,'PUSH')
      print('PUSH')
      light_up(10, 81, 255) # neon blue
    else:
      print_to_screen(0,0,'LOSE')
      print('LOSE')
      light_up(255,0,0) # red
  else:
    print_to_screen(0,0,'LOSE')
    print('LOSE')
    light_up(255,0,0) # red


#################################################################
# Running the Game:
players_hand = [] # Define empty hand for player
dealers_hand = [] # Define empty hand for dealer
print_to_screen(1,0,'Blue to start.  Black to end.')
print('Press BLUE to start, WHITE to end the game.')
lcd.move_to(0,0)
lcd.putstr('BLUE to start')
lcd.move_to(0,1)
lcd.putstr('WHITE to end the game.')
lcd.clear()
ans = button_pressed()
print() # Print blank line (formatting purposes)
while ans == True:
  players_hand.clear()
  dealers_hand.clear()
  start_game()
  if sum_players_hand(players_hand) == 21:
      utime.sleep(2)
      print('BLACKJACK!')
      print_to_screen(0,0,'BLACKJACK')
      light_up(0,255,0) # green
  else:   
      print('\nPress BLUE to draw a card, WHITE to end the round.\n')
      print_to_screen(0,0,'BLUE to draw.   BlACK to stand.')
      #lcd.move_to(0,0)
      #lcd.putstr("TEST HERE")
      utime.sleep(2)
      draw_choice = button_pressed()
      while draw_choice == True:
        print_to_screen(7,0,'Hit')
        print('Hit')
        players_hand.append(draw_card(False))
        sum_player = sum_players_hand(players_hand)
        sum_dealer = sum_players_hand(dealers_hand)
        utime.sleep(2)
        print_to_screen(0,0,"Player total:"+ str(sum_player) +" Dealer total:"+ str(sum_dealer))
        print('\nYour total is:', sum_players_hand(players_hand), '\n')
        if sum_players_hand(players_hand) > 21:
            print('LOSE!')
            print_to_screen(0,0,'LOSE')
            light_up(255,0,0) # red
            break
        elif sum_players_hand(players_hand) == 21:
            print('BLACKJACK!')
            print_to_screen(0,0,'BLACKJACK')
            light_up(0,255,0) # green
            break
        print('Press BLUE to draw a card, WHITE to end the round.\n')
        draw_choice = button_pressed()
      # print('Stand')
      if sum_players_hand(players_hand) < 21:
          game_result()
  print('\nPress BLUE to play again, WHITE to end the game.\n')
  ans = button_pressed()
print('You have chosen to quit. Goodbye.')
light_up(0,0,0) # off
lcd.clear()
##################################################################
