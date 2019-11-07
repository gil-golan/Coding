print(9 % 7)
print(8*4-4)
print(bool(4))
print(abs(10+4)*-1)
print((pow(1,2))%(4+4))
print(20-int(14.5))
print(bool(5*int(2.2)-10))
print(divmod(19,4))
print(str((5*10)-(13+5)))
print(float(int(4+True))-(15 % 4))

# 1. Float, Integer
# 2. True, False
# 3. Var1 += 1 : Saves time and memory
print()

print((4>3) and (1<2))
print(len("Hi")<3)
print((6>8) or (10<12))
print(not(7>10))
print(5<6 and 7>8)
print(not(5>6 and 7>8))
print(("A" != "0") and (10/5 == 2))
print(("A" == "0") and (10/5 != 2))
print()

a = 10
b = 99
print(a, b)

var1 = 100
var2 = 50
var3 = var1 + 10
print(var3)

a = 'Hi'
b = 'Bye'
a += a + b
a *= 2
print(a)

my_name = 'Mr. Bach'
your_name = 'Mr. Student'
print(my_name + ' or ' + your_name + '?')

this_val = False
that_val = True
some_val = 0
this_val += 1
that_val -= 0
print(this_val, that_val)
this_val = True
that_val = False
print(some_val + 0)

import cmath

a = 2
b = 5
c = 6

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

