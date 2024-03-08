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
def random():
    #generates a set of random letters, 2 vowels and 6 consonants 
    x=[]
    for i in range(2):
        y=chr(choice([65,69,73,79,85]))
        x.append(y)
    for i in range(6):
        z=chr(choice([66,67,68,70,71,72,74,75,76,77,78,80,81,82,83,84,86,87,88,89,90]))
        x.append(z)
    x=''.join(x)    
    return x
#rules of the game
print("Here are the instructions for the game:")
sleep(2)
print("   You have two rounds were you both are presented with random letters")
sleep(2)
print("   Each of you will get a chance to type in as many words as you can in a list from the letters generated")
sleep(2)
print("   Make sure your words contains only letters from the generated list or you do not gain any points")
sleep(2)
player_1=input("Enter your name player 1:")
player_2=input("Enter your name player 2:")
rounds1=int(input("How many rounds do you want to play for the normals:"))
player1=0
player2=0
#loops for the amount of rounds the user wants
for x in range(rounds1):
    lcd_clear()
    lcd_print("Round: ")
    lcd_print(x+1)
    sleep(2)
    for i in range(2):
        if i==0:
            print(player_1,"starts in 2 seconds and you have 25 seconds to figure out as many words as you can")
        else:
            print(player_2,"starts in 2 seconds and you have 25 seconds to figure out as many words as you can")
        sleep(2)
        print("Your random letters are on the LCD screen")
        rand=random()
        lcd_clear()
        lcd_print(rand)
        sleep(25)
        lcd_clear()
        buzzer_note(6, 440, 1000)
        print("Time is up!, you have 10 seconds to type in your words, press enter when you are done")
        t1=perf_counter()
        p1=None
        words=[]
        t=0
        t1=perf_counter()
        while p1 != "" and t<10:
            p1=input("Enter word:")
            if p1 !="":
                words.append(p1.upper())
            t2=perf_counter()
            t=t2-t1
        if t>10:
            words=words[:-1]
        buzzer_note(6, 440, 1000)
        lcd_clear()
        lcd_print("TIME IS UP!!")
        sleep(2)
        points=0
        for w in words:
            if word_match(w,rand)==True:
                points+=word_score(w)+1
            else:
                points-=5
        if i==0:
            player1+=points
        else:
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
lcd_print("BONUS ROUND!!")
sleep(2)
rounds=int(input("How many rounds do you all want to play:"))
print(player_1,"is the button and",player_2,"is the touch sensor")
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
