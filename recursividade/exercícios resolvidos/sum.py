def sumDigits(number):
    if (number==0):
        return 0
    else:
        return int(number%10)+sumDigits(int(number/10))