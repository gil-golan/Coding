def driving(driving):
    if driving<17:
        driving=False
    if driving>16:
        driving=True
    return driving

print(driving(16))
print(driving(25))

def id_triangle(a,b,c):
    if a**2+b**2 == c**2:
        id_triangle="Triangle is right angled"
    if a**2+b**2 > c**2:
        id_triangle="Triangle is acute"
    if a**2+b**2 < c**2:
        id_triangle = "Triangle is obtuse"
    return id_triangle

print(id_triangle(3,30,3))

def fizzbuzz(num):
    if num%3 == 0:
        fizzbuzz="FIZZ!"
    if num%5 == 0:
        fizzbuzz="Buzz!"
    if num%3 == 0 and num%5 == 0:
        fizzbuzz="FIZZ BUZZ!"
    return fizzbuzz

print(fizzbuzz(15))
print(fizzbuzz(6))
print(fizzbuzz(10))

import random

def guess_dice(a,b,c):
    count = 0
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    if dice1 == a:
        count=count+1
    if dice2 == b:
        count=count+1
    if dice3 == c:
        count=count+1
    print("Rolled",dice1,dice2,dice3,"and got right amount of guesses below:")
    return count
print(guess_dice(5,3,1))
print(guess_dice(6,5,4))

def gimme_random(type,low,high):
    if type=="float":
        num=random.uniform(low,high)
    if type=="int":
        num=random.randint(low,high)
    return num

print(gimme_random("float",0.2,0.9))