def both():
    counter = 1
    while counter < 3:
        counter += 1
        for i in range(8, -4, -1):
            print(i)
both()

def is_odd():
    for i in range (1, 11):
        num = i%2
        if num == 0:
            print(i, "= even")
        else:
            print(i, "= odd")

is_odd()

import random

def  dice_roll(n):
    counter = 0
    num = 0
    while num!= n:
        counter += 1
        a=random.randint(0, 6)
        b=random.randint(0, 6)
        c=random.randint(0, 6)
        num=a+b+c
    return counter

print(dice_roll(13))

def odd_even_count(n):
    even = 0
    odd = 0
    while n>0:
        num = n%10
        if num%2 == 0:
            even += 1
        else:
            odd += 1
    end = "Even = "+str(even)+" digits"+" Odd = "+str(odd)+" digits"
    return end

print(odd_even_count(1923612))

def string_analysis(spot):
    spaces = 0
    letters = 0
    numbers = 0
    for i in spot:
        if letters==" ":
            spaces+=1
        elif i.isalpha()==True:
            letters+=1
        elif i.isdigit()==True:
            numbers+=1
    end = "Spaces: "+str(spaces)+" Letters: "+str(letters)+" Numbers: "+str(numbers)
    return end

print(string_analysis("I'm not 89 years old"))