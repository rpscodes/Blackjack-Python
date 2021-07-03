#!/usr/bin/env python
# coding: utf-8

# In[1]:


#CARD
#SUIT,RANK,VALUE
#Creating a value of dictionaries
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


# In[2]:


#Creating Individual Card with their corresponding attributes
#Later use this class to create decks, access individual cards etc

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit 
    


# In[ ]:





# In[3]:


class Deck():
    
    def __init__(self):
        
        #Creating a empty deck first
        self.all_cards = []
        
        #Building the main_deck to be an array of 52 Card type objects
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
        
    def shuffle_deck(self):
        random.shuffle(self.all_cards)
    
    def deal_card(self):
        return self.all_cards.pop(0)
        
    


# In[4]:


class Player():
    
    def __init__(self,name,funds=0):
        self.name = name
        self.funds = funds
        self.all_cards = []
        self.total = 0
        self.aces_count = 0
    
    def add_cards(self,new_cards):
        self.all_cards.append(new_cards)
        self.total += new_cards.value
        if new_cards.value == 11:
            self.aces_count += 1
        if self.total > 21 and self.aces_count > 0:
            self.total = self.total - 10
            self.aces_count = self.aces_count -1
        
            
    def show_cards(self):
        print(self.name + "'s open cards are: ", end ="")
        
        for card in self.all_cards:
            print(card, end =" ||")
            
        print('\n'+ self.name + "'s total is " + str(self.total))
        
        
    
    def reset_cards(self):
        self.all_cards.clear()
        self.total = 0
        self.aces_count = 0
    
   

    #def find_total(self):
        #self.total = 0
        #for card in self.all_cards:
            #self.total += card.value
        #if self.total > 21 and self.aces_count > 0:
            #self.total = self.total - 10
            #self.aces_count = self.aces_count -1
            
        
        


# In[5]:


#Validate Funds

def get_funds():
    fund_amount = 'u'
    while fund_amount.isdigit() == False or int(fund_amount) <= 0:
        fund_amount = input("Please enter the funds you would like to add to the table: ")
        if fund_amount.isdigit() == False:
            print("Please enter a valid number")
            continue
        if int(fund_amount) <= 0:
            print("Funds must be greater than zero ")
    return int(fund_amount)
    


# In[6]:


#Players turn where he decides to hit or stay

def player_turn():
    if player_one.total < 21:
        player_decision = input("What would you like to do? type h for hit or s for stand:")
        if player_decision == 's':
            complete_game()
            return False

        elif player_decision == 'h':
            clear_output()
            player_one.add_cards(main_deck.deal_card())
            return True

        else:
            clear_output()
                    
            print("Wrong entry - please type h or s \n \n ")
            return True
        
    elif player_one.total == 21:
                
        complete_game()
                
        return False
    
    else:
                
        print(player_one.name + ' busted!!! Dealer Wins!!!')
        player_one.funds -= bet
        return False


# In[7]:


#Winning Function or Delaers turn after the player decides to stand or reaches 21

#def complete_game(player,dealer):
def complete_game():
    
    while dealer.total < 17:
        dealer.add_cards(main_deck.deal_card())
        #dealer.find_total()
    clear_output()
    player_one.show_cards()
    dealer.show_cards()
    print('---------------------------------------------------')
        
    if dealer.total > 21:
        print("Dealer Busted!!! " + player_one.name + ' Wins!!!')
        player_one.funds += bet
    elif player_one.total > dealer.total :
        print(player_one.name + ' Wins!!')
        player_one.funds += bet
    elif player_one.total == dealer.total :
        print('Game tied')
    else:
        print("Dealer wins")
        player_one.funds -= bet
    
    


# In[8]:


#Continue Playing another game
#def play_new_hand_choice(player,dealer):
def play_new_hand_choice():
    next_game_decision = input("Would you like to play another game ? type y for yes  or n for no: ")
    while next_game_decision not in ('y','n'):
            print("Wrong entry - please type y or n")
            next_game_decision = input("Would you like to play another game ? type y for yes  or n for no")

    if next_game_decision == 'y':
        player_one.reset_cards()
        dealer.reset_cards()
        return True

    else:
        print("Thanks for playing -- End of the game")
        print(f'Take home funds: {player_one.funds}')
        return False


# In[9]:


def choose_bet():
    bet_amount = 't'
    while bet_amount.isdigit() == False or int(bet_amount) > player_one.funds or int(bet_amount) <= 0:
        bet_amount = input(f'Available funds: {player_one.funds}   Place your bet..')
        if bet_amount.isdigit() == False:
            print("Please enter a valid number")
            continue
        if int(bet_amount) > player_one.funds:
            print("You do not have enough funds to place this bet. Please choose a smaller bet")
            continue
        if int(bet_amount) <= 0:
            print("Minimum bet must be greater than Zero")
            continue
        
    return int(bet_amount)


# In[10]:


#Create Deck of Cards
#Shuffle the cards
#Deal the cards - 2 Each 
#Show Players cards and one of dealers card
#Bet amount
#Show the total or players cards - Think about Ace 11 or 1
#While Hit or Stand
#Stand 
    #Dealer Opens Card
    #Total of Dealers
    #Less than 17 or less than player hit


# In[ ]:





# In[ ]:





# In[11]:


#Game Setup
from IPython.display import clear_output

p_name = input("Welcome Player! Please enter your name: ")
print('Welcome to BlackJack! Get as close to 21 as you can without going over! \n Dealer hits until she reaches 17. \n Aces count as 1 or 11. \n')
p_funds = get_funds()
player_one = Player(p_name,p_funds)
dealer = Player('Dealer')


#GAME PLAY

game_on = True

while game_on == True:
    if player_one.funds <= 0:
        print("You have run out of funds.")
        player_one.funds = get_funds()
    clear_output()
    bet = choose_bet()
    print('----------------------Welcome To A NEW GAME OF BLACK JACK----------------------------')
    
    main_deck = Deck()
    main_deck.shuffle_deck()
    

    for i in range(2):
        player_one.add_cards(main_deck.deal_card())
        dealer.add_cards(main_deck.deal_card())

    hit = True
    while hit == True:
        player_one.show_cards()
        print('Dealers open card is: ', end =" ")
        print(dealer.all_cards[-1])
        print(f'Dealers total is {dealer.all_cards[-1].value}')
        print('---------------------------------------------')
        hit = player_turn()
        
    game_on = play_new_hand_choice()

    
    
        
        


# In[ ]:




