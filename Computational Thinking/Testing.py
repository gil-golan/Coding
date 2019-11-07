print("Computer Science")

# Press 'command' + '/' to add comment

a_int = 500
a_float = 5.0001

# Don't use int, str, float or boolean for variable names

a = 50
b = 16.7
c = "Hi"
d = "90"
e = True
f = False

print(a + b)
print(a + int(d))
print(int(b))
print(str(a) + c)
print((70*10)+100)
print(10 % 3)
print(10 // 3)

print(300 == 30)

val=5.000
def is_int(val):
    if type(val) == int:
        return True
    else:
        if val.is_integer():
            return True
        else:
            return False

print(is_int(val))

a=9
b=2
c=16
print("yes") if a<b else print ("winner") if a**b < 100 else print("no")

if c**0.5<5:
    print("<5")
elif c**0.5>10:
    print(">10")
else:
    print("Neither")

count=0
while count < 5.3:
    count=count+(1/5)
    print(round(count,1))


