# Python Blackjack
# For this project you will make a Blackjack game using Python. Click here to familiarize yourself
#  with the the rules of the game. You won't be implementing every rule "down to the letter" with the game, 
# but we will doing a simpler version of the game. This assignment will be given to further test 
# your knowledge on object-oriented programming concepts.

# Rules:
# 1. The game will have two players: the Dealer and the Player. The game will start off with a deck of 52 cards. 
# The 52 cards will consist of 4 different suits: Clubs, Diamonds, Hearts and Spades.
# For each suit, there will be cards numbered 1 through 13.



# Note: No wildcards will be used in the program
# 2. When the game begins, the dealer will shuffle the deck of cards, making them randomized. 
# After the dealer shuffles, it will deal the player 2 cards and will deal itself 2 cards from. 
# The Player should be able to see both of their own cards, but should only be able to see one of the Dealer's cards.
# 3. The objective of the game is for the Player to count their cards after they're dealt. 
# If they're not satisfied with the number, they have the ability to 'Hit'. 
# A hit allows the dealer to deal the Player one additional card. 
# The Player can hit as many times as they'd like as long as they don't 'Bust'.
# A bust is when the Player is dealt cards that total more than 21.
# 4. If the dealer deals the Player cards equal to 21 on the first deal, the Player wins. 
# This is referred to as Blackjack. Blackjack is NOT the same as getting cards that equal up to 21 after the first deal. 
# Blackjack can only be attained on the first deal.
# 5. The Player will never see the Dealer's hand until the Player chooses to 'stand'. 
# A Stand is when the player tells the dealer to not deal it anymore cards. 
# Once the player chooses to Stand, the Player and the Dealer will compare their hands. 
# Whoever has the higher number wins. Keep in mind that the Dealer can also bust.


# This will be an exercise of how well you understand OOP(Object Oriented Programming). In this project, you will be using "Pair-Programming" to complete the assignment.



my_deck = {'1clubs' : 1, '2clubs' : 2, '3clubs' : 3, '4clubs' : 4, '5clubs' : 5, '6clubs' : 6, 
        '7clubs' : 7, '8clubs' : 8, '9clubs' : 9, '10clubs' : 10, '11clubs' : 11, '12clubs' : 12, '13clubs' : 13,
        '1diamonds' : 1, '2diamonds' : 2, '3diamonds' : 3, '4diamonds' : 4, '5diamonds' : 5, '6diamonds' : 6, 
        '7diamonds' : 7, '8diamonds' : 8, '9diamonds' : 9, '10diamonds' : 10, '11diamonds' : 11, '12diamonds' : 12, '13diamonds' : 13, 
        '1hearts' : 1, '2hearts' : 2, '3hearts' : 3, '4hearts' : 4, '5hearts' : 5, '6hearts' : 6, 
        '7hearts' : 7, '8hearts' : 8, '9hearts' : 9, '10hearts' : 10, '11hearts' : 11, '12hearts' : 12, '13hearts' : 13,
        '1spades' : 1, '2spades' : 2, '3spades' : 3, '4spades' : 4, '5spades' : 5, '6spades' : 6,
        '7spades' : 7, '8spades' : 8, '9spades' : 9, '10spades' : 10, '11spades' : 11, '12spades' : 12, '13spades' : 13,}


import random
import time
import re

class Blackjack(): 
    """ 
    Attributes for the class: 
    -Deck expected to be a dictionary
    -dealer_hand expected to be an empty list 
    -player_hand expected to be an empty list 
    """

    def __init__ (self, deck, dealer_hand, player_hand): 
        self.deck = deck
        self.dealer_hand = dealer_hand
        self.player_hand = player_hand
    
    def shuffle(self): 
        self.deck = list(self.deck)
        random.shuffle(self.deck)
        print("The Dealer is shuffling...")
        time.sleep(1)

    def firstDeal(self):
        print("The Dealer is dealing...")
        time.sleep(1)
        p_card1 = self.deck.pop()
        self.player_hand.append(p_card1)
        p_card2 = self.deck.pop()
        self.player_hand.append(p_card2)
        print("...")
        print(f"You've been dealt: {self.player_hand[0]} and {self.player_hand[1]}.")
        print('...')
        time.sleep(1)
        d_card1 = self.deck.pop()
        self.dealer_hand.append(d_card1)
        d_card2 = self.deck.pop()
        self.dealer_hand.append(d_card2)
        print('...')
        print(f"The Dealer has been dealt: {self.dealer_hand[0]} and ???.")
        print('...')
        time.sleep(1)

        s1 = self.player_hand[0]
        re.split('(\d+)', s1)
        for num1 in re.findall('\d+',s1):
            num1 = int(num1)
            # print(num1)
        s2 = self.player_hand[1]
        re.split('(\d+)', s2)
        for num2 in re.findall('\d+',s2):
            num2 = int(num2)
            # print(num2)
        if num1 + num2 == 21: 
            print("Lucky duck! You have Blackjack!")
            quit()
        elif num1 + num2 > 21: 
            print("Bad news: bust after the first round is dealt! The Dealer wins :(")
            quit()
        else: 
            pass
        s3 = self.dealer_hand[0]
        re.split('(\d+)', s3)
        for num3 in re.findall('\d+',s3): 
            num3 = int(num3)
            # print(num3)
        s4 = self.dealer_hand[1]
        re.split('(\d+)', s4)
        for num4 in re.findall('\d+',s4):
            num4 = int(num4)
            # print(num4)
        if num3 + num4 == 21: 
            print("Bad Luck! The Dealer has Blackjack!") 
            quit()
        elif num3 + num4 > 21: 
            print("Well, well, it's your lucky day! Dealer = bust, which means Player = winner!")
            quit()
        else: 
            pass
    
    def playerChoice(self): 
        selection = input("Would you like to hit or stand?")
        if selection.lower() == 'stand': 
            print("Time to reveal...")
            print('...')
            time.sleep(1)
            print(f"The Dealer has:") 
            time.sleep(1)
            for card in self.dealer_hand: 
                print(card) 
            print('...')
            time.sleep(1)
            print(f"The Player has:")
            time.sleep(1)
            d_total = []
            p_total = []
            for card2 in self.player_hand: 
                print(card2)
            print('...')
            for b in self.dealer_hand: 
                re.split('(\d+)', b)
                for num in re.findall('\d+', b):
                    num = int(num)
                    d_total.append(num)
            total2 = sum(d_total)
            for a in self.player_hand: 
                re.split('(\d+)', a)
                for num in re.findall('\d+', a):
                    num = int(num)
                    p_total.append(num)
            total1 = sum(p_total)
            if total1 > total2:
                time.sleep(2) 
                print(f"You have {total1}! You win, yayyyyyyy!")
            elif total1 == total2: 
                time.sleep(2)
                print(f"You both have {total1}...! It's a tie!")
            else: 
                time.sleep(2)
                print(f"Not your lucky day :( The Dealer wins with {total2}")

        elif selection.lower() == 'hit': 
            print("Dealing another card...")
            print('...')
            time.sleep(1)
            new_card = self.deck.pop()
            self.player_hand.append(new_card)
            print("You now have:")
            print('...')
            time.sleep(1)
            for card in self.player_hand: 
                print(card)
            print('...')
            sum_list = []
            for x in self.player_hand: 
                re.split('(\d+)', x)
                for num in re.findall('\d+', x):
                    num = int(num)
                    sum_list.append(num)
            count = sum(sum_list)
            if count > 21: 
                time.sleep(1)
                print("Bust! Sorry, you lose :(")
            else: 
                time.sleep(1)
                my_game.playerChoice()
        else: 
            print("Please select a valid option")
            my_game.playerChoice()
    

    

    

my_game = Blackjack(my_deck, [], [])


def playGame(): 
    my_game.shuffle()
    my_game.firstDeal()
    my_game.playerChoice()
    

playGame()