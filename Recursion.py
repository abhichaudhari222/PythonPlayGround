from num2words import num2words as numToWord  
def facto(n):
    if (n == 0):
        return 1
    return n * facto(n-1)

Factorial=facto(12)
print(numToWord(Factorial))
