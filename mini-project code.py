from engi1020.arduino import *
from time import *
from random import choice
print("Hi!, This is a fun and interactive game of scrabble. Hope you enjoy")
sleep(3)

def letter_score(letter):
    #calculates the points assigned to the letter
    if letter== "A" or letter== "E" or letter== "I" or letter== "O" or letter== "N" or letter=="R" or letter== "T" or letter== "L" or letter== "S" or letter== "U":
        points=1
    elif letter=="D" or letter=="G":
        points=2
    elif letter== "B" or letter== "C" or letter=="M" or letter== "P":
        points=3
    elif letter== "F" or letter=="H" or letter=="V" or letter=="W" or letter=="Y":
        points=4
    elif letter== "K":
        points=5
    elif letter== "J" or letter=="X" :
        points=8
    elif letter== "Q" or letter=="Z":
        points=10
    elif letter==" " or letter=="":
        points=0
    return points

def word_score(word):
    #calculates the total points of a word and calls the letter_score function
        total=0
        for i in word:
            total+= letter_score(i)
        return total
    
def word_match(word,rand_letters):
    #checks whether the word contains only letters from a string of random letters
    for i in word:
        for j in rand_letters:
            if i==j:
                x=True
                break
            else:
                x= False
        if x==False:
            break
    return x
def generate_random_letters():
    vowels = "AEIOU"
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    rand_letters = [choice(vowels) for _ in range(2)] + [choice(consonants) for _ in range(6)]
    return ''.join(rand_letters)

#rules of the game
def print_instructions():
    print("Here are the instructions for the game:")
    sleep(2)
    print("   You have two rounds where you are presented with random letters.")
    sleep(2)
    print("   Each of you will get a chance to type in as many words as you can in a list from the letters generated.")
    sleep(2)
    print("   Make sure your words contain only letters from the generated list or you do not gain any points.")
    sleep(2)

def display_round_info(player, round_number):
    lcd_clear()
    lcd_print("Round: ")
    lcd_print(round_number)
    sleep(2)
    print(f"{player} starts in 2 seconds, and you have 25 seconds to figure out as many words as you can.")
    sleep(2)
def input_words_within_time_limit():
    t1 = perf_counter()
    words = []
    t = 0
    while t < 10:
        word = input("Enter word:")
        if word != "":
            words.append(word.upper())
        t2 = perf_counter()
        t = t2 - t1
    if t > 10:
        words = words[:-1]
    buzzer_note(6, 440, 1000)
    lcd_clear()
    lcd_print("TIME IS UP!!")
    sleep(2)
    return words

def input_words(player, time_limit):
    lcd_clear()
    print(f"Your random letters are on the LCD screen.")
    rand = generate_random_letters()
    lcd_clear()
    lcd_print(rand)
    sleep(time_limit)
    lcd_clear()
    buzzer_note(6, 440, 1000)
    print("Time is up! You have 10 seconds to type in your words. Press enter when you are done.")
    return input_words_within_time_limit()

def calculate_points(words, rand_letters):
    points = 0
    for word in words:
        if word_match(word, rand_letters):
            points += word_score(word) + 1
        else:
            points -= 5
    return points

def game_round(player, player_score, round_number, time_limit):
    display_round_info(player, round_number)
    words = input_words(player, time_limit)
    points = calculate_points(words, generate_random_letters())
    player_score += points
    lcd_clear()
    lcd_print(player)
    lcd_print(":")
    lcd_print(player_score)
    sleep(5)
    return player_score

def bonus_round(player1, player2):
    lcd_clear()
    lcd_print("BONUS ROUND!!")
    sleep(2)
    rounds = int(input("How many rounds do you all want to play:"))
    print(f"{player1} is the button, and {player2} is the touch sensor.")
    lcd_clear()
    lcd_print("READY")
    sleep(2)
    lcd_clear()
    lcd_print("SET")
    sleep(2)
    lcd_clear()
    lcd_print("GO")
    sleep(2)
    for i in range(rounds):
        player1_score = game_round(player1, player1_score, i + 1)
        player2_score = game_round(player2, player2_score, i + 1)

    determine_winner(player1_score, player2_score)

if __name__ == "__main__":
    print("Hi! This is a fun and interactive game of scrabble. Hope you enjoy.")
    sleep(3)
    
    print_instructions()

    player_1 = input("Enter your name player 1:")
    player_2 = input("Enter your name player 2:")

    player1_score = 0
    player2_score = 0
    
    for round_num in range(int(input("How many rounds do you want to play for the normals:"))):
        player1_score = game_round(player_1, player1_score, round_num + 1)
        player2_score = game_round(player_2, player2_score, round_num + 1)
    
    

for i in range(rounds):
    points=0
    lcd_clear()
    lcd_print("Round: ")
    lcd_print(i+1)
    sleep(3)
    rand=random()
    lcd_clear()
    lcd_print(rand)
    t=0
    p=None
    print("You have 15 seconds starting now")
    t1=perf_counter()
    while t<15:
        b1=digital_read(8)
        b2=digital_read(3)
        if b1==1:
            p=b1
            lcd_clear()
            lcd_print(player_1)
            lcd_print(" Plays!")
            sleep(3)
            break
        elif b2==1:
            p=b2
            lcd_clear()
            lcd_print(player_2)
            lcd_print(" Plays!")
            sleep(3)
            break
        t2=perf_counter()
        t=t2-t1
    if p==None:
        buzzer_note(6, 440, 1000)
        lcd_clear()
        lcd_print("TIME IS UP!")
        print("You both lose 10 points")
        player1-=10
        player2-=10
        lcd_clear()
        lcd_print(player_1)
        lcd_print(":")
        lcd_print(player1)
        sleep(5)
        lcd_clear()
        lcd_print(player_2)
        lcd_print(":")
        lcd_print(player2)
        sleep(5)
        continue
    t1=perf_counter()
    word=input("Enter your word:")
    t2=perf_counter()
    t=t2-t1
    if t>10:
        buzzer_note(6, 440, 1000)
        lcd_clear()
        lcd_print("TIME IS UP!")
        sleep(2)
        if p==b1:
            player1-=5
        elif p==b2:
            player2-=5
    elif word=="":
        buzzer_note(6, 440, 1000)
        lcd_clear()
        lcd_print("NO ENTRY")
        sleep(3)
        if p==b1:
            player1-=5
        elif p==b2:
            player2-=5
    else:
        if word_match(word.upper(),rand)==True:
                points+=word_score(word.upper())
        else:
            buzzer_note(6, 440, 1000)
            lcd_clear()
            lcd_print("INCORRECT WORD")
            sleep(3)
            points-=5
        if p==b1:
            player1+=points
        elif p==b2:
            player2+=points
    lcd_clear()
    lcd_print(player_1)
    lcd_print(":")
    lcd_print(player1)
    sleep(5)
    lcd_clear()
    lcd_print(player_2)
    lcd_print(":")
    lcd_print(player2)
    sleep(5)
lcd_clear()
lcd_print("Winner: ")
sleep(3)
if player1>player2:
    lcd_print(player_1)
elif player1<player2:
    lcd_print(player_2)
else:
    lcd_clear()
    lcd_print("It's a tie!")
sleep(5)
lcd_clear()
lcd_print("Good game!!")
