# 1a. 34
# 1b. 16
# 1c. Syntax Error
# 1d. 32 12 22
# 1e. 14 22 32

def add(num1, num2):
  return num1 + num2

def triple(num):
  return add(num, add(num, num))

def quadruple(num):
    return add(num, add(num, add(num, num)))

import module1

print("Hello", module1.name)
module1.spherevolume("cm3")



