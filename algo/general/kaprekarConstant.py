
import string

KAP_CONSTANT = 6174

def kaprekar_constant_steps(num):
    numString = string(num)
    numDigits = len(numString)
    numArray  = numString.split("")

    # Case for if the num entered is not 4-digit integer
    if numDigits != 4:
        return False

    # Create the highest and lowest int
    for i in range(numDigits):
        for j in range(0, n-i-1):
            if numArray[j] > numArray[j + 1]:
                numArray[j], numArray[j + 1] = numArray[j + 1], numArray[j]

    print(numArray)

def get_digit(number, n):
    return number // 10**n % 10

print(get_digit(987654321, 0))
# 1

print(get_digit(987654321, 5))
# 6

kaprekar_constant_steps(2050)
