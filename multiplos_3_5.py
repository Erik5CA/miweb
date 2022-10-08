
from tokenize import Intnumber
from trace import Trace


sum = 0

num1 = 0
num2 = 1

while num2 < 4000000:
    temp = num1
    num1 = num2
    num2 = num2 + temp
    if num1 % 2 == 0:
        sum += num1
        

num = 1000
p = 2

primeFactor = 1
i = 2

#Encuentre el ultimo numero primo divisor de un numero.
while i <= num:
    if num % i == 0:
        primeFactor = i
        num = num / i
    else:
        i = i + 1

#Funcion para determinar si un numero es palindromo
def isPal(num):
    numString = str(num)
    for i in range(0,int(len(numString)/2+1)):
        if numString[i] != numString[-i - 1]:
            return False
    return True