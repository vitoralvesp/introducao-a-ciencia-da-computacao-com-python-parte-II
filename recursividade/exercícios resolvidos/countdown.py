def countdown(n):
    print(n)
    if (n==1):
        return 0
    else:
        return countdown(n-1)

print(countdown(5))