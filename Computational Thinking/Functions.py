def mixed_number(a,b):
    print(str(a/b))
mixed_number(9,2)

var = "This is a sample"

print()

def vowel_count_1and2(string, vowels):
    string = string.casefold()
    count = {}.fromkeys(vowels, 0)

    for character in string:
        if character in count:
            count[character] += 1
    return count

vowels = 'aeiou'
string = "This is a sample"
print(vowel_count_1and2(string, vowels))

print()

def sphere_volume(r):

    pi = 3.1415926535897931
    V= 4.0/3.0*pi* r**3
    return V
print('The volume of the sphere is: ',(int(sphere_volume(10))))

print()

def surface_area(r):
    pi = 22 / 7
    sur_area = 4 * pi * r ** 2
    return sur_area
print("Surface Area is: ", (int(surface_area(10))))

print()


def rgbhex(r, g, b):
    fdr = r//16
    fdg = g//16
    fdb = b//16
    sdr = r%16
    sdg = g%16
    sdb = b%16
    list = [fdr, fdg, fdb, sdr, sdg, sdb]
    for x in range(len(list)):
        if list[x] == 15:
            list[x] = 'f'
        elif list[x] == 14:
            list[x] = 'e'
        elif list[x] == 13:
            list[x] = 'd'
        elif list[x] == 12:
            list[x] = 'c'
        elif list[x] == 11:
            list[x] = 'b'
        elif list[x] == 10:
            list[x] = 'a'
        else:
            list[x] = str(list[x])
    print(str(list[0] + list[3] + list[1] + list[4] + list[2] + list[5]))
rgbhex(255, 0, 0)

def hexrgb(number):
    split = [y for y in str(number)]
    for x in range(len(split)):
        if split[x] == 'f':
            split[x] = 15
        elif split[x] == 'e':
            split[x] = 14
        elif split[x] == 'd':
            split[x] = 13
        elif split[x] == 'c':
            split[x] = 12
        elif split[x] == 'b':
            split[x] = 11
        elif split[x] == 'a':
            split[x] = 10
        else:
            split[x] = int(split[x])
    red = ((split[0]) * 16 + split[1])
    green = ((split[2]) * 16 + split[3])
    blue = ((split[4]) * 16 + split[5])
    print(red, green, blue)
hexrgb('ff0000')


